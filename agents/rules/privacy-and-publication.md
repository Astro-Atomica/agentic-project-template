# Privacy And Publication Safety

Use the versioned policy at [`agents/privacy-policy.json`](../privacy-policy.json) and the standard-library preflight at [`agents/tools/privacy_preflight.py`](../tools/privacy_preflight.py) before committing or publishing a generated project.

## Project Setup

Customize the policy before the first project commit.

1. Add only approved public Git author names or narrow name patterns.
2. Prefer a professional project address or a Git-host noreply address. The template permits GitHub noreply and reserved `example.com`, `example.org`, and `example.net` addresses; replace the example allowance when the project has a real publication policy.
3. Replace the synthetic disallowed identifiers and fixture names with project rules. Do not put private names, usernames, addresses, or account identifiers into a public policy merely to detect them.
4. Put actual private identifiers in ignored `_private/privacy-policy.local.json`, one of the injected CI policy mechanisms, or newline-separated `PRIVACY_PREFLIGHT_IDENTIFIERS` environment data.
5. Keep only unmistakably fake placeholder-secret formats in `allowedPlaceholderSecrets`. An example file is not permission to commit a working test or development credential.
6. Add project media roots, account-specific application paths, generated folders, and any intentionally public exceptions narrowly.

This repository's policy includes its maintainer's explicitly approved public email address. That is a repository-specific allowance, not a rule for generated projects; remove or replace it when adapting the scaffold. An address is not private merely because it uses a personal email provider. Approval and the intended publication policy determine which identities may be published.

Local policy fragments use the same JSON shape and extend list values from the tracked policy. CI can supply a JSON fragment through `PRIVACY_PREFLIGHT_POLICY_JSON`. Treat both environment variables as sensitive configuration and do not print them.

The `ruleDefinitionPaths` setting only suppresses self-matches for configured identifiers and sensitive-path expressions in the policy/tool source. Secret and email rules still scan those files. Keep this list limited to privacy-rule definitions.

## Commands

Run from the repository root with Python 3.10+ and Git 2.x installed. Examples use `python`; choose the appropriate launcher from the root [prerequisites](../../README.md#prerequisites).

```text
python -m unittest discover -s agents/tools/tests -v
python agents/tools/privacy_preflight.py working
python agents/tools/privacy_preflight.py staged
python agents/tools/privacy_preflight.py push
git fetch --all --prune
python agents/tools/privacy_preflight.py remote-history
python agents/tools/privacy_preflight.py local-refs
```

- `working` scans tracked and non-ignored untracked files, current Git identity, and reports ignored artifact roots as warnings.
- `staged` scans the complete index plus current author and committer identity. This is the commit gate.
- `push` scans author/committer identities, complete commit subjects and bodies, and files changed by commits ahead of the configured upstream. Use `--upstream origin/main` when the branch has no upstream or needs an explicit comparison base.
- `remote-history` scans history reachable from fetched `refs/remotes/**`. Fetch first; the command cannot inspect remote objects that do not exist locally.
- `local-refs` scans `refs/codex/**` by default. Use `--ref-prefix` for another auxiliary namespace.

An optional sanitized JSON report may be written only below `_code_review/` or `_tool_results/`:

```sh
python agents/tools/privacy_preflight.py staged --report _code_review/privacy/staged.json
```

The console and JSON report contain rule, file, line, ref, and abbreviated commit context, but never the matched secret or private line content.

Commit-message findings use `<commit-message>` as the location, with line numbers relative to the full message. The message text is not echoed. The same content rules apply to commit messages in `push`, `remote-history`, and commit-backed `local-refs` scans.

## Explicit Hook Setup

Hooks are opt-in. Install both local gates only after reviewing the commands:

```sh
python agents/tools/privacy_preflight.py install-hooks
```

This creates managed `pre-commit` and `pre-push` hooks and refuses to replace an unrelated existing hook. Git for Windows runs the shell wrappers through its bundled shell; macOS and Linux use the same wrappers. Run the commands manually if the project uses another hook manager.

## What The Gate Treats As Unsafe

Blocking findings include likely keys, tokens, private keys, credential assignments and files, non-allowlisted emails and Git identities, configured personal or careless fixture identities, absolute user/account paths, media and transcript artifacts, face/profile images, exports, browser captures, logs, dependencies, caches, build output, and ignored files that remain versioned.

Browser profiles, Playwright storage state, cookies, HAR files, traces, screenshots, and videos cross a trust boundary: they can contain authenticated sessions, private page content, local filesystem paths, or user data. Never treat a capture from a signed-in browser or local app as a safe fixture merely because it was generated by a test tool.

## Git History And Ignore Limits

`.gitignore` is preventive, not retroactive. It does not remove:

- a file already tracked in the index;
- a blob in an earlier commit;
- author or committer metadata;
- remote-tracking history already fetched;
- auxiliary refs such as `refs/codex/**` that bundles, mirrors, backups, or broad refspecs may retain.

A normal `git push origin main` does not send `refs/codex/**`, but that is not a privacy guarantee for bundles, mirrors, backups, or later wildcard pushes. Audit and delete or rewrite unsafe refs deliberately.

If a real credential is found, do not print or paste it into a report. Revoke or rotate it, remove public evidence, inspect reachable and auxiliary history, coordinate any rewrite, and verify both credential containment and information containment.
