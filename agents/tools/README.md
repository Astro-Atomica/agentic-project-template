# Agent Tools

Reusable repo-local tools for agents and humans.

Use this folder for executable scripts, command wrappers, validation helpers, generators, small utilities, CLI helpers, and app integrations that support agent work across the project.

## Guidelines

- Prefer small tools with clear inputs and outputs.
- Document how to run each tool.
- Keep destructive actions opt-in and obvious.
- Do not store secrets, tokens, private machine paths, or generated outputs here.
- Put temporary output in `_build/` or another ignored location.
- If a tool becomes project-specific rather than agent-harness-specific, move it closer to the project code under `workspace/` or `packages/`.

## Suggested Layout

```text
agents/tools/
  README.md
  tool-name/
    README.md
    scripts-or-source-files
```
