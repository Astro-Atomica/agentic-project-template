# Agentic Project Template

A visible-by-default scaffold for human-and-agent software projects.

This template is intentionally small. It gives a new project a shared operating layer for agents, docs, workspace conventions, and future package growth without assuming a specific language or framework.

## Principles

- **Visible by default:** human-authored agent guidance lives in `agents/`, not hidden dotfolders.
- **One agent stack:** all coding agents start at `AGENTS.md`; avoid platform-specific instruction files that duplicate the shared contract.
- **Root stays boring:** root files are entrypoints and repo infrastructure, not the whole project.
- **Private stays local:** `_private/` is gitignored.
- **Reviews stay draftable:** `_code_review/` is gitignored for private review notes and artifacts.
- **Agent byproducts stay local:** `_logs/`, `_exports/`, and `_tool_results/` are gitignored by default.
- **Generated stays disposable:** `_build/`, `dist/`, caches, and dependency folders are gitignored.
- **Profiles are additive:** start with the base scaffold, then copy in only the project profile you need.
- **Agents are auditable:** rules, workflows, and assumptions should be readable by humans first.
- **Publication is gated:** a configurable privacy preflight checks content, Git identities, history, and auxiliary refs without echoing discovered secrets.

## Structure

### Managed Folders

These folders are part of the Git-managed project scaffold and are intended to appear on GitHub.

```text
.github/      GitHub issue/PR templates and optional workflows
agents/       Shared agent rules, workflows, skills, and personas
docs/         Durable human-facing documentation
packages/     Optional monorepo packages
templates/    Optional project profile scaffolds
workspace/    Default active project surface
AGENTS.md     Agent entrypoint
README.md     Human entrypoint
```

### Private Local Folders

These folders are local-only by default and ignored by Git.

```text
_private/       Private notes, secrets, machine paths, account-specific state
_code_review/   Draft review notes, raw diffs, findings, review artifacts
_logs/          Logs from tools, scripts, agents, dev servers, and debugging
_exports/       Ad hoc exports, reports, snapshots, converted files, handoff artifacts
_tool_results/  Raw tool outputs, command captures, intermediate agent results
_build/         Generated builds, release candidates, compiled output, installers
_cache/         Downloaded/generated caches, datasets, model caches, embeddings
```

Editor/tool folders, dependency folders, and generated artifacts are also ignored by Git unless a project intentionally commits a small shared config file.

Code-review scratch work belongs in `_code_review/`, which is also ignored by Git. Logs, ad hoc exports, and raw tool outputs belong in `_logs/`, `_exports/`, and `_tool_results/`.

## Agent Document Stack

Start at [AGENTS.md](AGENTS.md) and follow applicable scoped instructions, such as [workspace/AGENTS.md](workspace/AGENTS.md). The root entrypoint routes agents to coding principles, privacy rules, design guidance, and workflows according to the task. The [agents index](agents/README.md) is a document map, not a required reading list for every edit.

Keep the shared contract in one place. Client-specific files may provide minimal adapters, and native skills may use a tool-required discovery path; neither should duplicate the shared rules. See [skills and workflow notes](agents/skills/README.md) for the distinction between ordinary documents and installed skills.

Use the small [code guidance stubs](agents/code/README.md) to customize agent behavior for the project's languages, platforms, and environments. Fill in only relevant project choices and link them from scoped instructions or a profile.

### Agent Compatibility

The initial scaffold was developed in May–July 2026. Agent instruction discovery has evolved since then; the shared entrypoint is the repository's convention, not a claim that every client automatically imports every linked document. Guidance is task-scoped so routine work can use the relevant context without loading the entire scaffold.

See [Agent Compatibility](agents/rules/agent-compatibility.md) for vendor documentation checked on **2026-09-29**, setup notes, and the distinction between documented support and testing in this repository. Recheck those notes when changing clients or upgrading them.

## Prerequisites

The scaffold itself is plain text. Its privacy tool and tests require **Git 2.x** and **Python 3.10 or newer**, with no third-party Python packages. A copied project may add its own runtime requirements through a profile.

Choose a Python launcher that resolves to a supported interpreter:

| Environment | Typical command | Version check |
| --- | --- | --- |
| Windows PowerShell or Command Prompt | `py -3` | `py -3 --version` |
| macOS or Linux terminal | `python3` | `python3 --version` |
| Any platform with Python on PATH or an active virtual environment | `python` | `python --version` |

Examples below use `python`; substitute your chosen launcher in each command. Check `git --version` too. Local verification on 2026-09-29 used Windows, Python 3.14.3, and Git 2.52.0.windows.1. The CI configuration targets Ubuntu with Python 3.12; that configuration is not a record of a completed CI run or a full platform matrix.

## Getting Started

1. Download the source ZIP from GitHub and extract it into a new project folder, or use GitHub's **Use this template** action when it is enabled. Both paths avoid inheriting the template's commit history.
2. Open the extracted folder or clone your newly generated repository.
3. Point your coding agent at the repository root.
4. Send the first prompt, such as `hi`, and ask the agent to customize the scaffold for the new project.
5. Work with the agent through [agents/workflows/startup.md](agents/workflows/startup.md) to choose profiles, update docs, and remove scaffold pieces you do not need.
6. Review the customized project.
7. Run tests and the privacy preflights, commit the reviewed customization, then run the push preflight.
8. Create and push the customized project to its new repository.

### Fresh Repo Workflow

Use a fresh source ZIP for the shell-independent path: extract it with your platform's archive tool and open a terminal in the extracted project folder. If you cloned the template instead, remove only that new copy's `.git` directory with your file manager before initializing it. Do not remove `.git` from an existing project you want to retain.

Customize the scaffold with your agent before staging it. Set a repository-local Git identity that you intend to publish, then make the privacy policy agree with that choice. Replace both identity examples with your approved public name and email; a professional address, an explicitly public personal address, or your GitHub noreply address can be appropriate.

These commands work in PowerShell, Command Prompt, and POSIX shells when the chosen Git and Python commands are on PATH:

```text
git init
git config --local user.name "Your Public Name"
git config --local user.email "your-public-address@example.org"
```

Customize [agents/privacy-policy.json](agents/privacy-policy.json) before continuing. Remove this template maintainer's public email allowance when it does not belong to your project. Then run:

```text
python -m unittest discover -s agents/tools/tests -v
python agents/tools/privacy_preflight.py working
git add .
python agents/tools/privacy_preflight.py staged
git commit -m "Initial project scaffold"
git branch -M main
```

Run each command separately and continue only if it succeeds. Review `git diff --cached` before committing. If GitHub generated your new repository and it already has a commit history, keep that history and commit only your customization changes.

Create an empty remote repository under your own account or organization, replace `YOUR-OWNER` and `YOUR-REPOSITORY` below, and publish:

```text
git remote add origin https://github.com/YOUR-OWNER/YOUR-REPOSITORY.git
python agents/tools/privacy_preflight.py push
git push -u origin main
```

If your generated repository already has an `origin`, verify it with `git remote -v` and keep the correct remote instead of adding it again. HTTPS cloning does not require SSH keys; pushing requires authentication with your Git host.

## Starting With An Agent

This template is meant to become yours before the first project commit.

After cloning or copying it, open the folder with your agent and start the conversation. A simple first prompt is enough:

```text
hi, help me customize this scaffold for my new project
```

The agent should read the shared instructions, ask only the questions needed to adapt the scaffold, update the visible docs, and leave you with a clean project ready to commit.

## Privacy And Publication Preflight

Each generated project owns its allowlists and sensitive-pattern policy in [agents/privacy-policy.json](agents/privacy-policy.json). Customize the approved public Git names and professional or noreply email patterns, synthetic fixture restrictions, placeholder-secret formats, private-path rules, and artifact patterns before publishing.

The dependency-free Python tool can inspect the working tree, staged index, unpublished commits, fetched remote history, and auxiliary local refs such as `refs/codex/**`. Commit-history modes check author/committer identities and full commit subjects and bodies using the same content rules:

```text
python -m unittest discover -s agents/tools/tests -v
python agents/tools/privacy_preflight.py working
python agents/tools/privacy_preflight.py staged
python agents/tools/privacy_preflight.py push
```

Local hooks are never installed automatically. Opt in with `python agents/tools/privacy_preflight.py install-hooks`. See [Privacy And Publication Safety](agents/rules/privacy-and-publication.md) for private policy overrides, history/ref audits, remediation, and report handling.

`.gitignore` is not retroactive. It cannot untrack a file, remove historical blobs or commit metadata, or remove auxiliary refs retained by bundles, mirrors, and backups.

## Project Profiles

Initial profile stubs are included for:

- static TypeScript apps
- Node.js apps
- Electron / Tauri apps
- Godot apps
- C# tools
- CUDA / TensorFlow projects
- iOS / macOS / iPadOS / visionOS apps
- Steam / Xbox / Switch game projects

Profiles are notes and scaffolds, not mandatory architecture.

## Contributing

To contribute to this template, see [CONTRIBUTING.md](CONTRIBUTING.md) for fork setup, verification, template issue reports, and pull request expectations. Projects created from the template should supply their own contributor guide.
