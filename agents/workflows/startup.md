# Startup Workflow

Use this once when adapting the scaffold into a new project. Ordinary tasks use the relevant links in root `AGENTS.md`.

## Customize The Project

1. Read the human README, inspect Git status, and check existing workspace guidance and project decisions. Infer choices already recorded; ask only for missing decisions needed to adapt the project.
2. Establish the product goal, stack, supported runtime/platform floor, and useful local verification commands. Use profiles as optional starting points and retain only relevant scaffold material.
3. Update the README and workspace instructions with actual project commands and decisions. Existing branch, author-attribution, and disclosure conventions apply; introduce optional policies only when the project needs them.
4. Choose a public Git identity and customize [the publication policy](../privacy-policy.json). Keep private detection identifiers in ignored local policy or protected environment configuration. See [privacy setup](../rules/privacy-and-publication.md#project-setup).
5. Verify the customized scaffold and run the working privacy preflight. Summarize choices, checks, and unresolved requirements. Commit or publish only within the user's authorization.

Preserve user work, unknown untracked files, `_private/` content, and review/process records. Clean up only known disposable output owned by the task. Add project-specific guidance when there is a concrete need, rather than filling every optional folder.

## Local Resource Boundaries

- Use the project's configured ports. If none are specified, agent-started preview servers and temporary services default to `localhost:8100` or higher; check availability before starting one.
- Track long-running processes in an ignored file such as `_logs/processes.md`: purpose, command, working directory, port, PID when available, and shutdown method.
- Check existing process records before reusing or replacing a service. Confirm it serves the intended project and stop only processes whose ownership is known.
- Stop task-owned services when no longer needed, or document why they remain running and how to stop them.
