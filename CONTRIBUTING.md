# Contributing To Agentic Project Template

This guide covers contributions to **Astro-Atomica/agentic-project-template**: its shared agent guidance, reusable profiles, documentation, privacy tooling, and repository infrastructure. Repositories created from this template should provide their own contributor guide.

Contributions that make the template easier to adopt, inspect, and maintain are welcome. Keep it useful across languages, platforms, and coding agents.

## Develop The Template

Fork this repository on GitHub, then clone your fork. Replace `YOUR-OWNER` with your GitHub account or organization:

```text
git clone https://github.com/YOUR-OWNER/agentic-project-template.git
cd agentic-project-template
git remote add upstream https://github.com/Astro-Atomica/agentic-project-template.git
git fetch upstream
```

Keep the template's Git history and scaffold structure. Create a contribution branch from `upstream/main`. The README's fresh-project workflow is for users creating their own project; template contributors work in this fork without resetting history or running project customization.

Read [AGENTS.md](AGENTS.md), [README.md](README.md), and [agents/README.md](agents/README.md). For tool or workflow changes, read the relevant shared rules before editing.

Git 2.x and Python 3.10 or newer are required to run the privacy tooling and tests. No Python dependencies need installing. Use the launcher table and verification notes in [Prerequisites](README.md#prerequisites); examples here use `python` and work with `py -3` or `python3` substituted where appropriate.

Use a Git name and email you intend to publish in this template's history, and check them against [the template's publication policy](agents/privacy-policy.json). Configure them for this checkout with `git config --local user.name` and `git config --local user.email`. For an intentionally public address not already covered, a narrow local allowance can go in ignored `_private/privacy-policy.local.json`; a shared policy change belongs in the pull request and needs maintainer review. CI does not inherit local overrides.

## Scope And Style

- Improve the template itself: shared workflows, reusable profile notes, adoption documentation, executable tools, or GitHub infrastructure.
- Keep generated applications and personal project configuration in their own repositories. Template examples should be small, synthetic, and directly demonstrate a reusable convention.
- Keep shared agent instructions in `AGENTS.md` and `agents/`; avoid duplicating them into client-specific files.
- Preserve platform and language neutrality. Mark project-specific tools and opinions as optional.
- Update documentation when behavior, setup steps, or workflow expectations change.
- Add focused regression tests for executable behavior changes. Prefer synthetic fixtures that demonstrate the actual failure and expected result.
- Keep local notes, reports, logs, and captures in the ignored underscore folders described in the README.
- When updating agent compatibility, cite current vendor documentation, record the review date, and distinguish documentation checks from runtime verification.

## Verify Changes

Run from the repository root:

```text
python -m unittest discover -s agents/tools/tests -v
python agents/tools/privacy_preflight.py working
git diff --check
```

Review and stage only the intended changes, then run the commit gate:

```text
git diff --cached
python agents/tools/privacy_preflight.py staged
```

Before pushing commits, run:

```text
python agents/tools/privacy_preflight.py push
```

Also check the complete contribution range against the fetched template branch:

```text
python agents/tools/privacy_preflight.py push --upstream upstream/main
```

The default push command checks against your branch's configured upstream; the explicit comparison above checks the commits proposed for the template. See [Privacy And Publication Safety](agents/rules/privacy-and-publication.md) for fetched history, local refs, reports, and optional hooks.

Run commands individually and resolve failures before proceeding. A local successful check is evidence for its tested scope, not proof of a completed CI run or every client's behavior.

## Issues And Pull Requests

Open template issues in [Astro-Atomica/agentic-project-template](https://github.com/Astro-Atomica/agentic-project-template/issues). Include expected and actual behavior, relevant tool/runtime versions, and a minimal synthetic reproduction. For a feature request, describe the adoption problem and why the change belongs in the shared scaffold. Reports about an application built from this template belong in that application's issue tracker.

Open a pull request from your contribution branch to this template's `main` branch. Keep it focused, explain the resulting behavior, document verification performed, and identify any relevant limitations. Use the repository's PR template. Agent-assisted contributions have the same review and verification expectations as other contributions.

Do not include real credentials, private identities, authenticated browser state, or raw private logs in an issue or pull request. If a report needs sensitive evidence, request a private reporting route without posting the evidence publicly.

## License

Contributions are made under the repository's [MIT No Attribution license](LICENSE).
