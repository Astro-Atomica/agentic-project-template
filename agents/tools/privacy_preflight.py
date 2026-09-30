#!/usr/bin/env python3
"""Audit Git content and metadata for privacy and publication hazards."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import fnmatch
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from typing import Iterable


DEFAULT_POLICY = "agents/privacy-policy.json"
PRIVATE_REPORT_ROOTS = ("_code_review", "_tool_results")
HOOK_MARKER = "managed-by-agentic-privacy-preflight"

EMAIL_RE = re.compile(r"(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![A-Za-z0-9.-])")
SECRET_RULES = (
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"), None),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"), None),
    ("gitlab-token", re.compile(r"\bglpat-[A-Za-z0-9_-]{20,}\b"), None),
    ("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"), None),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"), None),
    ("stripe-secret", re.compile(r"\bsk_(?:live|test)_[0-9A-Za-z]{16,}\b"), None),
    ("slack-token", re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b"), None),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"), None),
    (
        "credential-assignment",
        re.compile(
            r"(?i)\b(?:api[_-]?key|token|secret|password|passwd|client[_-]?secret|access[_-]?token)\b"
            r"\s*[:=]\s*[\"']?(?P<value>[^\s\"'`;,#]{8,})"
        ),
        "value",
    ),
    (
        "credential-url",
        re.compile(r"\b[a-z][a-z0-9+.-]*://[^\s/:@]+:[^\s/@]{4,}@", re.IGNORECASE),
        None,
    ),
)

DEFAULT_CREDENTIAL_FILES = (
    "**/.env",
    "**/.env.*",
    "**/*.pem",
    "**/*.key",
    "**/*.p12",
    "**/*.pfx",
    "**/id_rsa",
    "**/id_ed25519",
    "**/.netrc",
    "**/.npmrc",
    "**/.pypirc",
    "**/.aws/credentials",
    "**/*credentials*.json",
    "**/*service-account*.json",
    "**/*storage-state*.json",
    "**/*auth-state*.json",
    "**/*cookies*.json",
)


class PreflightError(RuntimeError):
    pass


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    rule: str
    message: str
    source: str
    path: str = ""
    line: int | None = None
    commit: str = ""
    ref: str = ""


def git(repo: Path, *args: str, check: bool = True, text: bool = True):
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        capture_output=True,
        text=text,
        encoding="utf-8" if text else None,
    )
    if check and result.returncode != 0:
        stderr = result.stderr.strip() if text else result.stderr.decode("utf-8", "replace").strip()
        raise PreflightError(f"git {' '.join(args)} failed: {stderr}")
    return result


def deep_merge(base, addition):
    if isinstance(base, dict) and isinstance(addition, dict):
        merged = dict(base)
        for key, value in addition.items():
            merged[key] = deep_merge(merged[key], value) if key in merged else value
        return merged
    if isinstance(base, list) and isinstance(addition, list):
        return [*base, *addition]
    return addition


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise PreflightError(f"cannot load policy {path}: {error}") from error


def load_policy(repo: Path, policy_arg: str):
    policy_path = (repo / policy_arg).resolve() if not Path(policy_arg).is_absolute() else Path(policy_arg)
    policy = load_json(policy_path)
    if policy.get("version") != 1:
        raise PreflightError("privacy policy version must be 1")

    for local_name in policy.get("localPolicyFiles", []):
        local_path = (repo / local_name).resolve()
        if local_path.is_file():
            policy = deep_merge(policy, load_json(local_path))

    inline_policy = os.environ.get("PRIVACY_PREFLIGHT_POLICY_JSON", "").strip()
    if inline_policy:
        try:
            policy = deep_merge(policy, json.loads(inline_policy))
        except json.JSONDecodeError as error:
            raise PreflightError(f"PRIVACY_PREFLIGHT_POLICY_JSON is invalid: {error}") from error

    private_identifiers = [
        value.strip()
        for value in os.environ.get("PRIVACY_PREFLIGHT_IDENTIFIERS", "").splitlines()
        if value.strip()
    ]
    if private_identifiers:
        identity = policy.setdefault("identity", {})
        identity.setdefault("disallowedPersonalIdentifiers", []).extend(private_identifiers)

    validate_policy(policy)
    return policy


def validate_policy(policy):
    regex_fields = []
    identity = policy.get("identity", {})
    regex_fields.extend(("allowed author name", value) for value in identity.get("allowedAuthorNamePatterns", []))
    regex_fields.extend(("allowed email", value) for value in identity.get("allowedEmailPatterns", []))
    for item in policy.get("paths", {}).get("sensitivePatterns", []):
        regex_fields.append((item.get("id", "sensitive-path"), item.get("pattern", "")))
    for group in policy.get("secrets", {}).get("allowedPlaceholderSecrets", []):
        regex_fields.extend(("placeholder secret", value) for value in group.get("valuePatterns", []))
    for label, pattern in regex_fields:
        try:
            re.compile(pattern)
        except re.error as error:
            raise PreflightError(f"invalid {label} regex: {error}") from error


def glob_matches(path: str, pattern: str) -> bool:
    normalized = path.replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    candidates = (pattern, pattern[3:]) if pattern.startswith("**/") else (pattern,)
    for candidate in candidates:
        candidate = candidate.replace("\\", "/")
        if fnmatch.fnmatchcase(normalized, candidate):
            return True
        if candidate.endswith("/**") and normalized.rstrip("/") == candidate[:-3].rstrip("/"):
            return True
    return False


class Auditor:
    def __init__(self, repo: Path, policy):
        self.repo = repo
        self.policy = policy
        self.findings: list[Finding] = []
        self.seen: set[Finding] = set()
        identity = policy.get("identity", {})
        self.allowed_names = set(identity.get("allowedAuthorNames", []))
        self.allowed_name_patterns = [re.compile(value) for value in identity.get("allowedAuthorNamePatterns", [])]
        self.allowed_email_patterns = [re.compile(value, re.IGNORECASE) for value in identity.get("allowedEmailPatterns", [])]
        self.personal_identifiers = identity.get("disallowedPersonalIdentifiers", [])
        self.fixture_names = identity.get("disallowedFixtureNames", [])
        self.sensitive_paths = [
            (item.get("id", "sensitive-path"), re.compile(item["pattern"]))
            for item in policy.get("paths", {}).get("sensitivePatterns", [])
        ]
        secret_config = policy.get("secrets", {})
        self.placeholder_groups = [
            (
                item.get("pathPatterns", []),
                [re.compile(value, re.IGNORECASE) for value in item.get("valuePatterns", [])],
            )
            for item in secret_config.get("allowedPlaceholderSecrets", [])
        ]
        self.allowed_credential_files = secret_config.get("allowedCredentialFilePatterns", [])
        self.credential_files = [
            *DEFAULT_CREDENTIAL_FILES,
            *secret_config.get("credentialFilePatterns", []),
        ]
        self.artifact_patterns = [
            (item.get("id", "generated-artifact"), item["pattern"])
            for item in policy.get("artifacts", {}).get("patterns", [])
        ]
        self.max_text_bytes = int(policy.get("scan", {}).get("maxTextBytes", 1024 * 1024))
        self.rule_definition_paths = policy.get("scan", {}).get("ruleDefinitionPaths", [])

    def add(self, finding: Finding):
        if finding not in self.seen:
            self.seen.add(finding)
            self.findings.append(finding)

    def email_allowed(self, email: str) -> bool:
        return any(pattern.fullmatch(email) for pattern in self.allowed_email_patterns)

    def name_allowed(self, name: str) -> bool:
        return name in self.allowed_names or any(pattern.fullmatch(name) for pattern in self.allowed_name_patterns)

    def placeholder_allowed(self, path: str, value: str) -> bool:
        for path_patterns, value_patterns in self.placeholder_groups:
            if any(glob_matches(path, item) for item in path_patterns):
                if any(pattern.fullmatch(value) for pattern in value_patterns):
                    return True
        return False

    def context(self, source: str, path: str = "", line: int | None = None, commit: str = "", ref: str = ""):
        return dict(source=source, path=path, line=line, commit=commit, ref=ref)

    def scan_identity(self, name: str, email: str, role: str, **context):
        if not self.name_allowed(name):
            self.add(Finding("block", "git_identity", f"{role}-name", f"{role} name is not allowlisted", **context))
        if not self.email_allowed(email):
            self.add(Finding("block", "git_identity", f"{role}-email", f"{role} email is not allowlisted", **context))
        lowered_identity = f"{name}\n{email}".casefold()
        for index, identifier in enumerate(self.personal_identifiers):
            if identifier and identifier.casefold() in lowered_identity:
                self.add(Finding("block", "personal_identifier", f"{role}-configured-{index + 1}", f"{role} identity contains a configured personal identifier", **context))
        for index, fixture in enumerate(self.fixture_names):
            if fixture and fixture.casefold() in lowered_identity:
                self.add(Finding("block", "fixture_identity", f"{role}-configured-{index + 1}", f"{role} identity contains a disallowed fixture name", **context))

    def scan_current_identity(self, source: str):
        for role, variable in (("author", "GIT_AUTHOR_IDENT"), ("committer", "GIT_COMMITTER_IDENT")):
            result = git(self.repo, "var", variable, check=False)
            if result.returncode != 0:
                self.add(Finding("block", "git_identity", f"{role}-missing", f"{role} identity is not configured", source=source, path="<git-metadata>"))
                continue
            match = re.match(r"^(.*) <([^<>]+)> ", result.stdout.strip())
            if not match:
                raise PreflightError(f"cannot parse {variable}")
            self.scan_identity(match.group(1), match.group(2), role, source=source, path="<git-metadata>")

    def scan_commit_metadata(self, commit: str, source: str, ref: str):
        raw = git(self.repo, "show", "-s", "--format=%an%x00%ae%x00%cn%x00%ce%x00%B", commit).stdout
        parts = raw.split("\x00", 4)
        if len(parts) != 5:
            raise PreflightError(f"cannot parse metadata for commit {commit}")
        context = dict(source=source, path="<git-metadata>", commit=commit, ref=ref)
        self.scan_identity(parts[0], parts[1], "author", **context)
        self.scan_identity(parts[2], parts[3], "committer", **context)
        self.scan_text(parts[4], "<commit-message>", source, commit, ref)

    def scan_text(self, text: str, path: str, source: str, commit: str = "", ref: str = ""):
        is_rule_definition = any(glob_matches(path, item) for item in self.rule_definition_paths)
        for line_number, line in enumerate(text.splitlines(), 1):
            context = self.context(source, path, line_number, commit, ref)
            for rule, pattern, value_group in SECRET_RULES:
                for match in pattern.finditer(line):
                    value = match.group(value_group) if value_group else match.group(0)
                    if not self.placeholder_allowed(path, value):
                        self.add(Finding("block", "secret", rule, "likely credential or secret material", **context))
            for match in EMAIL_RE.finditer(line):
                if not self.email_allowed(match.group(0)):
                    self.add(Finding("block", "personal_email", "email-not-allowlisted", "email address is not allowlisted for publication", **context))
            if not is_rule_definition:
                lowered = line.casefold()
                for index, identifier in enumerate(self.personal_identifiers):
                    if identifier and identifier.casefold() in lowered:
                        self.add(Finding("block", "personal_identifier", f"configured-{index + 1}", "configured personal identifier found", **context))
                for index, fixture in enumerate(self.fixture_names):
                    if fixture and fixture.casefold() in lowered:
                        self.add(Finding("block", "fixture_identity", f"configured-{index + 1}", "disallowed demo or fixture identity found", **context))
                for rule, pattern in self.sensitive_paths:
                    if pattern.search(line):
                        self.add(Finding("block", "machine_path", rule, "machine-specific or account-specific absolute path", **context))

    def currently_ignored(self, path: str) -> bool:
        return git(self.repo, "check-ignore", "--no-index", "--quiet", "--", path, check=False).returncode == 0

    def scan_path(self, path: str, data: bytes | None, source: str, tracked: bool, commit: str = "", ref: str = "", warning_only: bool = False):
        normalized = path.replace("\\", "/")
        context = self.context(source, normalized, None, commit, ref)
        severity = "warning" if warning_only else "block"

        if tracked and self.currently_ignored(normalized):
            category = "history_ignored" if commit else "tracked_ignored"
            self.add(Finding("block", category, "ignored-but-versioned", "file is ignored now but remains versioned", **context))

        credential_match = next((item for item in self.credential_files if glob_matches(normalized, item)), None)
        credential_allowed = any(glob_matches(normalized, item) for item in self.allowed_credential_files)
        if credential_match and not credential_allowed:
            self.add(Finding(severity, "credential_file", credential_match, "credential-bearing filename is unsafe to publish", **context))

        for rule, pattern in self.artifact_patterns:
            if glob_matches(normalized, pattern):
                self.add(Finding(severity, "generated_artifact", rule, "generated, captured, private, or dependency artifact", **context))

        self.scan_text(normalized, normalized, source, commit, ref)
        if data is None or len(data) > self.max_text_bytes or b"\x00" in data:
            return
        self.scan_text(data.decode("utf-8", "replace"), normalized, source, commit, ref)

    def scan_working(self):
        self.scan_current_identity("working")
        tracked = nul_items(git(self.repo, "ls-files", "-z", text=False).stdout)
        untracked = nul_items(git(self.repo, "ls-files", "--others", "--exclude-standard", "-z", text=False).stdout)
        for path in sorted(set(tracked + untracked)):
            file_path = self.repo / Path(path)
            data = file_path.read_bytes() if file_path.is_file() else None
            self.scan_path(path, data, "working", path in tracked)

        ignored = nul_items(
            git(
                self.repo,
                "ls-files",
                "--others",
                "--ignored",
                "--exclude-standard",
                "--directory",
                "-z",
                text=False,
            ).stdout
        )
        for path in ignored:
            self.scan_path(path, None, "working-ignored", False, warning_only=True)

    def scan_staged(self):
        self.scan_current_identity("staged")
        raw = nul_items(git(self.repo, "ls-files", "-s", "-z", text=False).stdout)
        for entry in raw:
            metadata, path = entry.split("\t", 1)
            _mode, object_id, stage = metadata.split()
            if stage != "0":
                self.add(Finding("block", "git_index", "unmerged", "unmerged index entry cannot be published", source="staged", path=path))
                continue
            data = git(self.repo, "cat-file", "blob", object_id, text=False).stdout
            self.scan_path(path, data, "staged", True)

    def scan_commit(self, commit: str, source: str, ref: str):
        self.scan_commit_metadata(commit, source, ref)
        changed = nul_items(
            git(
                self.repo,
                "diff-tree",
                "--root",
                "--no-commit-id",
                "--name-only",
                "-r",
                "-z",
                commit,
                text=False,
            ).stdout
        )
        for path in changed:
            object_spec = f"{commit}:{path}"
            exists = git(self.repo, "cat-file", "-e", object_spec, check=False)
            if exists.returncode != 0:
                continue
            data = git(self.repo, "cat-file", "blob", object_spec, text=False).stdout
            self.scan_path(path, data, source, True, commit, ref)

    def scan_commits(self, commits: Iterable[tuple[str, str]], source: str):
        for commit, ref in commits:
            self.scan_commit(commit, source, ref)


def nul_items(data: bytes) -> list[str]:
    return [item.decode("utf-8", "surrogateescape") for item in data.split(b"\x00") if item]


def commits_for_refs(repo: Path, refs: list[str]) -> list[tuple[str, str]]:
    found: dict[str, str] = {}
    for ref in refs:
        result = git(repo, "rev-list", "--reverse", ref, check=False)
        if result.returncode != 0:
            continue
        for commit in result.stdout.splitlines():
            found.setdefault(commit, ref)
    return list(found.items())


def list_refs(repo: Path, prefix: str) -> list[str]:
    output = git(repo, "for-each-ref", "--format=%(refname)", prefix).stdout
    return [line for line in output.splitlines() if line]


def push_commits(repo: Path, upstream_arg: str) -> list[tuple[str, str]]:
    head = git(repo, "rev-parse", "--verify", "HEAD", check=False)
    if head.returncode != 0:
        raise PreflightError("push audit requires at least one commit")
    if upstream_arg:
        upstream = git(repo, "rev-parse", "--verify", upstream_arg, check=False)
        if upstream.returncode != 0:
            raise PreflightError(f"upstream ref does not exist: {upstream_arg}")
        output = git(repo, "rev-list", "--reverse", f"{upstream_arg}..HEAD").stdout
        label = upstream_arg
    else:
        detected = git(repo, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}", check=False)
        if detected.returncode == 0:
            label = detected.stdout.strip()
            output = git(repo, "rev-list", "--reverse", f"{label}..HEAD").stdout
        else:
            label = "unpublished"
            output = git(repo, "rev-list", "--reverse", "HEAD", "--not", "--remotes").stdout
            if not output.strip() and not list_refs(repo, "refs/remotes/"):
                output = git(repo, "rev-list", "--reverse", "HEAD").stdout
    return [(commit, f"HEAD vs {label}") for commit in output.splitlines() if commit]


def safe_context(value: str, auditor: Auditor) -> str:
    safe = value.replace("\r", "?").replace("\n", "?")
    for identifier in [*auditor.personal_identifiers, *auditor.fixture_names]:
        if identifier:
            safe = re.sub(re.escape(identifier), "<redacted-identifier>", safe, flags=re.IGNORECASE)
    safe = EMAIL_RE.sub("<redacted-email>", safe)
    for _rule, pattern in auditor.sensitive_paths:
        safe = pattern.sub("<redacted-path>", safe)
    for _rule, pattern, _group in SECRET_RULES:
        safe = pattern.sub("<redacted-secret>", safe)
    return safe


def render(auditor: Auditor):
    ordered = sorted(
        auditor.findings,
        key=lambda item: (item.severity != "block", item.source, item.ref, item.commit, item.path, item.line or 0, item.category, item.rule),
    )
    for finding in ordered:
        location = safe_context(finding.path or "<unknown>", auditor)
        if finding.line is not None:
            location += f":{finding.line}"
        details = []
        if finding.ref:
            details.append(f"ref={safe_context(finding.ref, auditor)}")
        if finding.commit:
            details.append(f"commit={finding.commit[:12]}")
        suffix = f" ({', '.join(details)})" if details else ""
        print(
            f"{finding.severity.upper()} [{finding.category}/{safe_context(finding.rule, auditor)}] "
            f"{location}: {finding.message}{suffix}"
        )
    blockers = sum(item.severity == "block" for item in ordered)
    warnings = len(ordered) - blockers
    print(f"Privacy preflight: {blockers} blocking finding(s), {warnings} warning(s).")
    return blockers


def write_report(repo: Path, report_arg: str, auditor: Auditor):
    if not report_arg:
        return
    target = (repo / report_arg).resolve() if not Path(report_arg).is_absolute() else Path(report_arg).resolve()
    allowed = False
    for root_name in PRIVATE_REPORT_ROOTS:
        root = (repo / root_name).resolve()
        if target == root or root in target.parents:
            allowed = True
            break
    if not allowed:
        raise PreflightError("detailed reports may only be written under _code_review/ or _tool_results/")
    target.parent.mkdir(parents=True, exist_ok=True)
    safe_findings = []
    for finding in auditor.findings:
        item = asdict(finding)
        for key in ("path", "source", "ref", "rule"):
            item[key] = safe_context(item[key], auditor)
        safe_findings.append(item)
    target.write_text(json.dumps({"version": 1, "findings": safe_findings}, indent=2) + "\n", encoding="utf-8")


def install_hooks(repo: Path):
    hooks_path = Path(git(repo, "rev-parse", "--git-path", "hooks").stdout.strip())
    if not hooks_path.is_absolute():
        hooks_path = repo / hooks_path
    hooks_path.mkdir(parents=True, exist_ok=True)
    commands = {"pre-commit": "staged", "pre-push": "push"}
    for hook_name, mode in commands.items():
        hook_path = hooks_path / hook_name
        if hook_path.exists() and HOOK_MARKER not in hook_path.read_text(encoding="utf-8", errors="replace"):
            raise PreflightError(f"refusing to replace existing hook: {hook_path}")
        content = f"""#!/bin/sh
# {HOOK_MARKER}
ROOT=$(git rev-parse --show-toplevel) || exit 2
if command -v python3 >/dev/null 2>&1; then
  exec python3 "$ROOT/agents/tools/privacy_preflight.py" {mode}
fi
exec python "$ROOT/agents/tools/privacy_preflight.py" {mode}
"""
        hook_path.write_text(content, encoding="utf-8", newline="\n")
        hook_path.chmod(hook_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        print(f"Installed {hook_name} privacy hook.")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode",
        choices=("working", "staged", "push", "remote-history", "local-refs", "install-hooks"),
        help="audit target or explicit hook setup action",
    )
    parser.add_argument("--policy", default=os.environ.get("PRIVACY_PREFLIGHT_POLICY", DEFAULT_POLICY))
    parser.add_argument("--upstream", default="", help="push comparison base (defaults to configured upstream)")
    parser.add_argument("--ref-prefix", default="refs/codex/", help="prefix used by local-refs mode")
    parser.add_argument("--report", default="", help="optional sanitized JSON report under _code_review/ or _tool_results/")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    try:
        repo_result = git(Path.cwd(), "rev-parse", "--show-toplevel", check=False)
        if repo_result.returncode != 0:
            raise PreflightError("run the privacy preflight from inside a Git worktree")
        repo = Path(repo_result.stdout.strip()).resolve()
        if args.mode == "install-hooks":
            install_hooks(repo)
            return 0

        policy = load_policy(repo, args.policy)
        auditor = Auditor(repo, policy)
        if args.mode == "working":
            auditor.scan_working()
        elif args.mode == "staged":
            auditor.scan_staged()
        elif args.mode == "push":
            auditor.scan_commits(push_commits(repo, args.upstream), "push")
        elif args.mode == "remote-history":
            refs = list_refs(repo, "refs/remotes/")
            auditor.scan_commits(commits_for_refs(repo, refs), "remote-history")
        elif args.mode == "local-refs":
            refs = list_refs(repo, args.ref_prefix)
            auditor.scan_commits(commits_for_refs(repo, refs), "local-refs")
        write_report(repo, args.report, auditor)
        return 1 if render(auditor) else 0
    except PreflightError as error:
        print(f"Privacy preflight error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
