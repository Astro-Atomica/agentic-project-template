# Git Workflow

Use this workflow to decide how agents should branch, stage, commit, merge, and hand off work.

1. Inspect `git status --short --branch` before changing files.
2. Default to `main` as the central branch unless the project explicitly defines another branch strategy.
3. Identify the project branch strategy before creating commits or pull requests.
4. Preserve user work. Do not revert, overwrite, or stage unrelated changes unless the user explicitly asks.
5. Keep changes small enough to review, test, and revert.
6. Use the commit message templates in `agents/commit-templates/` when the project has selected one.
7. Respect the startup decision about agent author-role attribution. If the user said no, that is a hard no.

## Integration Branch Pattern

Some projects use an integration branch as the agent landing zone before work reaches `main` or another protected central branch. Integration branch names can be simple, such as `dev`, user-scoped, such as `dev-{nickname}`, or project-specific.

1. Treat the integration branch as the shared merge surface for agent-authored work.
2. Create task branches from the integration branch unless the project says otherwise.
3. Merge or PR task branches back into the integration branch first.
4. Keep the integration branch passing tests and review checks so it remains safe to promote.
5. Promote from the integration branch to `origin/main`, a staged branch, or another protected target only through the project-approved path.

Record the selected branch strategy in project-specific guidance, such as `workspace/AGENTS.md`, when customizing this scaffold.
