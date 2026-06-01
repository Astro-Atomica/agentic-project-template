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

All agents should use the same document stack:

1. [AGENTS.md](AGENTS.md)
2. [agents/README.md](agents/README.md)
3. [agents/PRINCIPLES.md](agents/PRINCIPLES.md)
4. relevant files under [agents/rules](agents/rules), [agents/workflows](agents/workflows), [agents/skills](agents/skills), [agents/personas](agents/personas), or [agents/tools](agents/tools)
5. project-specific notes in [workspace/AGENTS.md](workspace/AGENTS.md), if needed

Do not create parallel platform-specific instruction files such as `CLAUDE.md`, `.cursorrules`, or `.windsurfrules` unless a tool absolutely requires a compatibility shim. If a shim is required, it should be tiny and point back to `AGENTS.md`.

## Getting Started

1. Use this repository as a template or clone it.
2. Point your coding agent at the repository root.
3. Send the first prompt, such as `hi`, and ask the agent to customize the scaffold for the new project.
4. Work with the agent through [agents/workflows/startup.md](agents/workflows/startup.md) to choose profiles, update docs, and remove scaffold pieces you do not need.
5. Review the customized project.
6. Create and commit the customized project in your new repository.

## Starting With An Agent

This template is meant to become yours before the first project commit.

After cloning or copying it, open the folder with your agent and start the conversation. A simple first prompt is enough:

```text
hi, help me customize this scaffold for my new project
```

The agent should read the shared instructions, ask only the questions needed to adapt the scaffold, update the visible docs, and leave you with a clean project ready to commit.

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
