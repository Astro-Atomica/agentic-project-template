# Task Execution Workflow

Use this as the default agent work loop.

1. Clarify the goal only if the next action is genuinely ambiguous or risky.
2. Inspect the relevant files before editing.
3. Make the smallest useful change.
4. Keep generated, private, and dependency files out of Git.
5. Run the narrowest meaningful verification.
6. Run `python agents/tools/privacy_preflight.py staged` before a commit and the `push` mode before publication.
7. Summarize what changed, where, and how it was checked.

If the task changes project conventions, update `AGENTS.md`, `agents/`, or `docs/` so the learning is durable.

For review tasks, use the private code-review workflow in [code-review.md](code-review.md).
