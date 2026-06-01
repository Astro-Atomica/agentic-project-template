# Windows Rules

Use this file for Windows-specific platform quirks, requirements, constraints, filesystem behavior, path and filename limits, service behavior, shell behavior, and compatibility notes.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a platform-specific file limits it to only that platform.

## File And Path Names

1. Treat Windows paths as case-insensitive by default; do not create files that differ only by case.
2. Avoid reserved characters: `<`, `>`, `:`, `"`, `/`, `\`, `|`, `?`, and `*`.
3. Avoid trailing spaces or trailing periods in file and directory names.
4. Avoid reserved device names such as `CON`, `PRN`, `AUX`, `NUL`, `COM1` through `COM9`, and `LPT1` through `LPT9`, even with extensions.
5. Keep paths short and test long generated paths. Long-path support depends on OS, policy, tooling, and runtime configuration.
6. Be careful with alternate data stream syntax using `:` and with backslash escaping in strings.
