import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


TOOL = Path(__file__).resolve().parents[1] / "privacy_preflight.py"


def run(command, cwd, check=True):
    result = subprocess.run(
        command,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if check and result.returncode != 0:
        raise AssertionError(result.stdout + result.stderr)
    return result


class PrivacyPreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        run(["git", "init", "-q"], self.repo)
        run(["git", "config", "user.name", "Project Contributor"], self.repo)
        run(
            ["git", "config", "user.email", "contributor@users.noreply.github.com"],
            self.repo,
        )
        (self.repo / "agents").mkdir()
        policy = {
            "version": 1,
            "identity": {
                "allowedAuthorNames": ["Project Contributor"],
                "allowedAuthorNamePatterns": [],
                "allowedEmailPatterns": [
                    r"^[A-Za-z0-9._%+-]+@users\.noreply\.github\.com$"
                ],
                "disallowedPersonalIdentifiers": ["Example " + "Personal Name"],
                "disallowedFixtureNames": ["Careless " + "Demo User"],
            },
            "secrets": {
                "allowedPlaceholderSecrets": [
                    {
                        "pathPatterns": ["**/.env.example"],
                        "valuePatterns": [r"^replace-me(?:-[a-z-]+)?$"],
                    }
                ],
                "allowedCredentialFilePatterns": ["**/.env.example"],
            },
            "paths": {
                "sensitivePatterns": [
                    {
                        "id": "windows-user-home",
                        "pattern": r"(?i)\b[A-Z]:\\Users\\(?!<name>\\|username\\|user\\|example\\)[^\\\s]+\\",
                    },
                    {
                        "id": "posix-user-home",
                        "pattern": r"/(?:Users|home)/(?!<name>/|username/|user/|example/)[^/\s]+/",
                    },
                ]
            },
            "artifacts": {
                "patterns": [
                    {"id": "playwright-cli", "pattern": "**/.playwright-cli/**"},
                    {"id": "video", "pattern": "**/*.webm"},
                ]
            },
            "localPolicyFiles": [],
            "scan": {
                "maxTextBytes": 1048576,
                "ruleDefinitionPaths": ["agents/privacy-policy.json"],
            },
        }
        (self.repo / "agents" / "privacy-policy.json").write_text(
            json.dumps(policy), encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def preflight(self, *args):
        return run(
            [
                sys.executable,
                str(TOOL),
                *args,
                "--policy",
                "agents/privacy-policy.json",
            ],
            self.repo,
            check=False,
        )

    def commit_all(self, message="test commit"):
        run(["git", "add", "-A"], self.repo)
        run(["git", "commit", "-q", "-m", message], self.repo)

    def test_staged_secret_is_blocked_and_never_printed(self):
        leaked_value = "ghp_1234567890" + "abcdefghijklmnopqrstuvwxyzAB"
        (self.repo / "unsafe.txt").write_text("token=" + leaked_value + "\n", encoding="utf-8")
        run(["git", "add", "unsafe.txt"], self.repo)

        result = self.preflight(
            "staged", "--report", "_tool_results/privacy/staged.json"
        )

        self.assertEqual(1, result.returncode)
        self.assertIn("secret", result.stdout.lower())
        self.assertIn("unsafe.txt:1", result.stdout)
        self.assertNotIn(leaked_value, result.stdout + result.stderr)
        report = (self.repo / "_tool_results" / "privacy" / "staged.json").read_text(
            encoding="utf-8"
        )
        self.assertIn('"category": "secret"', report)
        self.assertNotIn(leaked_value, report)

    def test_env_example_placeholder_is_allowed(self):
        (self.repo / ".env.example").write_text(
            "API_" + "KEY=replace-me-project-key\n", encoding="utf-8"
        )
        run(["git", "add", "-f", ".env.example"], self.repo)

        result = self.preflight("staged")

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_machine_paths_and_configured_identities_are_classified(self):
        (self.repo / "notes.txt").write_text(
            "C:\\" + "Users\\actual-user\\App" + "Data\\Roaming\n"
            "/" + "Users/actual-user/Library/" + "Application Support\n"
            "Example " + "Personal Name\n"
            "Careless " + "Demo User\n",
            encoding="utf-8",
        )
        run(["git", "add", "notes.txt"], self.repo)

        result = self.preflight("staged")

        self.assertEqual(1, result.returncode)
        self.assertIn("machine_path", result.stdout)
        self.assertIn("personal_identifier", result.stdout)
        self.assertIn("fixture_identity", result.stdout)

    def test_disallowed_fixture_name_is_blocked_in_git_identity(self):
        run(["git", "config", "user.name", "Careless " + "Demo User"], self.repo)
        (self.repo / "safe.txt").write_text("safe\n", encoding="utf-8")
        run(["git", "add", "safe.txt"], self.repo)

        result = self.preflight("staged")

        self.assertEqual(1, result.returncode)
        self.assertIn("fixture_identity", result.stdout)
        self.assertIn("<git-metadata>", result.stdout)

    def test_nested_playwright_capture_is_blocked_when_tracked(self):
        capture = self.repo / "workspace" / "tmp" / ".playwright-cli" / "shot.webm"
        capture.parent.mkdir(parents=True)
        capture.write_bytes(b"not-a-real-video")
        run(["git", "add", "-f", str(capture.relative_to(self.repo))], self.repo)

        result = self.preflight("staged")

        self.assertEqual(1, result.returncode)
        self.assertIn("generated_artifact", result.stdout)
        self.assertIn("playwright-cli", result.stdout)

    def test_tracked_file_that_is_now_ignored_is_blocked(self):
        (self.repo / "capture.log").write_text("safe log\n", encoding="utf-8")
        self.commit_all("track log")
        (self.repo / ".gitignore").write_text("*.log\n", encoding="utf-8")
        run(["git", "add", ".gitignore"], self.repo)

        result = self.preflight("staged")

        self.assertEqual(1, result.returncode)
        self.assertIn("tracked_ignored", result.stdout)
        self.assertIn("capture.log", result.stdout)

    def test_non_branch_codex_ref_history_is_audited(self):
        self.commit_all("safe root")
        leaked_value = "AKIA12345678" + "90ABCDEF"
        (self.repo / "old.txt").write_text(leaked_value + "\n", encoding="utf-8")
        self.commit_all("unsafe auxiliary history")
        unsafe_commit = run(["git", "rev-parse", "HEAD"], self.repo).stdout.strip()
        run(["git", "update-ref", "refs/codex/archive", unsafe_commit], self.repo)
        run(["git", "reset", "-q", "--hard", "HEAD~1"], self.repo)

        result = self.preflight("local-refs")

        self.assertEqual(1, result.returncode)
        self.assertIn("refs/codex/archive", result.stdout)
        self.assertIn("old.txt:1", result.stdout)
        self.assertNotIn(leaked_value, result.stdout + result.stderr)

    def test_push_audits_only_commits_ahead_of_upstream(self):
        self.commit_all("safe upstream")
        upstream = run(["git", "rev-parse", "HEAD"], self.repo).stdout.strip()
        run(["git", "update-ref", "refs/remotes/origin/main", upstream], self.repo)
        leaked_value = "glpat-" + "1234567890abcdefghijklmnop"
        (self.repo / "pushed.txt").write_text(leaked_value + "\n", encoding="utf-8")
        self.commit_all("unsafe push")

        result = self.preflight("push", "--upstream", "refs/remotes/origin/main")

        self.assertEqual(1, result.returncode)
        self.assertIn("HEAD vs refs/remotes/origin/main", result.stdout)
        self.assertIn("pushed.txt:1", result.stdout)
        self.assertNotIn(leaked_value, result.stdout + result.stderr)

    def test_fetched_remote_history_is_audited_on_request(self):
        self.commit_all("safe root")
        leaked_value = "AIza" + "123456789abcdefghijklmnopqrstuvwxyz"
        (self.repo / "remote.txt").write_text(leaked_value + "\n", encoding="utf-8")
        self.commit_all("unsafe remote")
        unsafe_commit = run(["git", "rev-parse", "HEAD"], self.repo).stdout.strip()
        run(["git", "update-ref", "refs/remotes/origin/leaked", unsafe_commit], self.repo)
        run(["git", "reset", "-q", "--hard", "HEAD~1"], self.repo)

        result = self.preflight("remote-history")

        self.assertEqual(1, result.returncode)
        self.assertIn("refs/remotes/origin/leaked", result.stdout)
        self.assertIn("remote.txt:1", result.stdout)
        self.assertNotIn(leaked_value, result.stdout + result.stderr)

    def test_commit_subject_and_body_are_scanned_in_every_history_mode(self):
        self.commit_all("safe upstream")
        upstream = run(["git", "rev-parse", "HEAD"], self.repo).stdout.strip()
        run(["git", "update-ref", "refs/remotes/origin/main", upstream], self.repo)
        leaked_value = "ghp_" + "1234567890abcdefghijklmnopqrstuvwxyzAB"
        private_email = "synthetic" + "@example.test"
        private_path = "C:\\" + "Users\\actual-user\\project"
        private_name = "Example " + "Personal Name"
        message = "diagnostic " + leaked_value + "\n\n" + "\n".join(
            [private_email, private_path, private_name]
        )
        run(["git", "commit", "-q", "--allow-empty", "-m", message], self.repo)
        unsafe_commit = run(["git", "rev-parse", "HEAD"], self.repo).stdout.strip()
        run(["git", "update-ref", "refs/remotes/origin/probe", unsafe_commit], self.repo)
        run(["git", "update-ref", "refs/codex/probe", unsafe_commit], self.repo)

        cases = [
            ("push", "--upstream", "refs/remotes/origin/main"),
            ("remote-history",),
            ("local-refs",),
        ]
        for args in cases:
            with self.subTest(mode=args[0]):
                report_path = "_tool_results/privacy/" + args[0] + ".json"
                result = self.preflight(*args, "--report", report_path)
                self.assertEqual(1, result.returncode, result.stdout + result.stderr)
                self.assertIn("<commit-message>:1", result.stdout)
                self.assertIn("<commit-message>:3", result.stdout)
                self.assertIn("<commit-message>:4", result.stdout)
                self.assertIn("<commit-message>:5", result.stdout)
                self.assertIn(unsafe_commit[:12], result.stdout)
                self.assertIn("secret", result.stdout)
                self.assertIn("personal_email", result.stdout)
                self.assertIn("machine_path", result.stdout)
                self.assertIn("personal_identifier", result.stdout)
                report = (self.repo / report_path).read_text(encoding="utf-8")
                findings = json.loads(report)["findings"]
                self.assertTrue(any(
                    item["path"] == "<commit-message>"
                    and item["commit"] == unsafe_commit
                    for item in findings
                ))
                for private_value in [leaked_value, private_email, private_path, private_name]:
                    self.assertNotIn(private_value, result.stdout + result.stderr + report)

    def test_public_email_in_commit_message_is_allowed(self):
        self.commit_all("Document contributor@users.noreply.github.com\n\nPublic contact.")
        result = self.preflight("push")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_push_excludes_commit_message_before_upstream(self):
        leaked_value = "glpat-" + "1234567890abcdefghijklmnop"
        self.commit_all("synthetic prior message " + leaked_value)
        upstream = run(["git", "rev-parse", "HEAD"], self.repo).stdout.strip()
        run(["git", "update-ref", "refs/remotes/origin/main", upstream], self.repo)
        run(["git", "commit", "-q", "--allow-empty", "-m", "safe followup"], self.repo)
        result = self.preflight("push", "--upstream", "refs/remotes/origin/main")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_hook_installation_is_explicit_and_preserves_unrelated_hooks(self):
        result = self.preflight("install-hooks")
        hooks = Path(run(["git", "rev-parse", "--git-path", "hooks"], self.repo).stdout.strip())
        if not hooks.is_absolute():
            hooks = self.repo / hooks

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("managed-by-agentic-privacy-preflight", (hooks / "pre-commit").read_text(encoding="utf-8"))
        self.assertIn("staged", (hooks / "pre-commit").read_text(encoding="utf-8"))
        self.assertIn("push", (hooks / "pre-push").read_text(encoding="utf-8"))

        (hooks / "pre-commit").write_text("#!/bin/sh\necho existing\n", encoding="utf-8")
        refused = self.preflight("install-hooks")
        self.assertEqual(2, refused.returncode)
        self.assertIn("refusing to replace", refused.stderr)
        self.assertIn("echo existing", (hooks / "pre-commit").read_text(encoding="utf-8"))

    def test_report_must_stay_in_private_review_or_tool_folder(self):
        result = self.preflight("working", "--report", "public-report.json")

        self.assertEqual(2, result.returncode)
        self.assertFalse((self.repo / "public-report.json").exists())


if __name__ == "__main__":
    unittest.main()
