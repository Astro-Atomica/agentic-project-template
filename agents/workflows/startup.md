# Startup Workflow

Use this after a user points an agent at this scaffold and sends the first prompt to customize it into a project.

1. Read root `AGENTS.md`.
2. Read root `README.md`.
3. Read `agents/README.md`.
4. Read `agents/PRINCIPLES.md`.
5. Inspect `git status --short --branch`.
6. Check `workspace/AGENTS.md` for project-specific instructions.
7. Delete unnecessary local clutter when it is clearly safe: OS junk, generated scratch files, stale tool output, or agent-created temp files in ignored locations.
8. Do not delete tracked source, user work, unknown untracked files, or project artifacts unless the user explicitly approves.

Never delete `_private/` content automatically, and preserve review/process
records until their ownership and retention state are known.

9. Customize `agents/privacy-policy.json` before the first commit. Confirm approved public Git author names and narrow professional or noreply email patterns, fake fixture identities, placeholder-secret formats, private paths, and generated artifact rules.
10. Keep actual private identifiers in `_private/privacy-policy.local.json` or protected environment configuration rather than publishing them in the tracked detection policy.
11. Run `python agents/tools/privacy_preflight.py working`. Resolve blocking findings; ignored local artifacts may remain as warnings when they are intentionally contained.
12. Ask whether legacy support is required. If yes, record the supported version floor or support time window before adding compatibility paths.
13. Ask whether agents should put their author role in commit messages or commit metadata. Record the chosen project pattern before the first agent-authored commit. If the user says no, treat it as a hard no and do not add agent role attribution to commit messages or metadata.
14. Identify the active profile, if any, under `templates/profiles/`.
15. Read any relevant repo rules in `agents/rules/`.
16. Read relevant language, framework, runtime, or pattern rules in `agents/code/`.
17. For visual or interface work, read `agents/DESIGN.md` when it has content and use `agents/workflows/design-development.md` when developing or revising design guidance.
18. For UX features that transform state, read `agents/workflows/composable-ux-testing.md`.
19. For review tasks, use `agents/workflows/code-review.md`.
20. For implementation tasks, use `agents/workflows/task-execution.md`.
21. Ignore platform-specific instruction files if they duplicate `AGENTS.md`; they should only be compatibility shims.
22. Identify the edit-review loop for the project: fastest local build, test, preview, hot reload, direct app inspection, internal state inspection, and visual validation path.
23. Confirm there is a way to observe or test the result. Warn the user when the available tools cannot close the loop.
24. If the loop is slow or CI-only, advise a small improvement that keeps the loop fast, such as hot reload, targeted tests, caching, parallel tasks, or a local preview.

Keep startup lightweight. Load deeper docs only when they are relevant to the task.

## Local Resource Boundaries

Respect separate local space for users, developers, and agents.

1. User/dev services own the lower local dev range by default. Start user-facing or developer-run services at `localhost:8000` unless the project says otherwise.
2. Agent-started services follow the global port and process tracking rules in root `AGENTS.md`.
3. Record enough process metadata to clean it up later: command, working directory, port, PID when available, start time, purpose, and expected shutdown command.
4. Before declaring work complete, stop processes that are no longer needed or document why they are intentionally left running.
5. On startup, inspect existing process notes when local services appear to be running. Processes can survive context compaction and new threads.
