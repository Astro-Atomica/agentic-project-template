# Local Output Conventions

Use these ignored folders to keep agent and tool byproducts predictable.

## Folders

- `_private/` - private local notes, secrets, machine paths, account-specific state.
- `_code_review/` - review notes, draft findings, raw diffs, command summaries, review artifacts.
- `_logs/` - logs from tools, scripts, agents, dev servers, debugging, and test runs.
- `_exports/` - ad hoc exports, reports, snapshots, converted files, and handoff artifacts.
- `_tool_results/` - raw tool output, captured command results, intermediate analysis files, and scratch artifacts.
- `_build/` - generated builds, release candidates, compiled outputs, installers, and packaged artifacts.
- `_cache/` - downloaded/generated caches, datasets, model caches, embeddings, and other reusable local acceleration artifacts.

## Rules

- These folders are ignored by Git by default.
- Do not use them as canonical documentation.
- Promote durable knowledge into `docs/`, `agents/`, `workspace/`, or `packages/`.
- Keep raw byproducts local unless the user explicitly asks to preserve or publish them.
- If a generated artifact becomes part of the source of truth, move it to a visible tracked folder and explain why.

## Choosing A Folder

Use `_logs/` for chronological event streams.

Use `_exports/` when a tool produces a user-facing file or bundle.

Use `_tool_results/` when the file is mainly for the agent's intermediate reasoning or verification.

Use `_build/` when the file is a build product or release candidate.

Use `_cache/` when the file is expensive to fetch or regenerate but is not source material.

Use `_private/` when the file contains private data or machine-specific context.
