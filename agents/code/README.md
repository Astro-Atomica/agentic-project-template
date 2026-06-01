# Code Rules

Additional coding rules for specific languages, frameworks, runtimes, patterns, or situations.

Use this folder when guidance is narrower than the shared principles in `agents/PRINCIPLES.md`.

## Layout

1. `lang/` - language, framework, runtime, and markup-specific rules.
2. `patterns/` - programming pattern and architecture-shape rules.
3. `platform/` - operating system, device, console, store, CI, automation, and distribution-platform quirks, requirements, constraints, and guidelines.

## Guidelines

1. Keep rules focused on one language, framework, runtime, or situation.
2. Put language, framework, runtime, and markup rules under `lang/`.
3. Put reusable programming pattern rules under `patterns/`.
4. Put operating system, device, console, store, CI, automation, and distribution-platform quirks, requirements, constraints, and guidelines under `platform/`.
5. Prefer names that make scope obvious, such as `lang/typescript.md`, `lang/python.md`, `lang/svelte.md`, `patterns/state-machines.md`, `patterns/event-streams.md`, `platform/windows.md`, or `platform/github-actions.md`.
6. Do not duplicate broad principles from `agents/PRINCIPLES.md`.
7. Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language-, pattern-, or platform-specific file limits it to only that scope.
8. Link related rules from the relevant project profile or workspace instructions when they apply.
9. Keep examples small and directly tied to the rule.
10. Do not put platform secrets, publishing credentials, private partner docs, account data, or NDA-restricted material in `platform/`.
