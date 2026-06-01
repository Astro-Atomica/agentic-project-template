# Apple Platform Rules

Use this file for shared Apple-platform quirks, requirements, constraints, device behavior, store guidelines, and compatibility notes across macOS, iOS, iPadOS, visionOS, or related Apple targets.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a platform-specific file limits it to only that platform.

## File And Path Names

1. Treat Apple filesystems as case-preserving but often case-insensitive by default; do not rely on case-only filename differences.
2. Avoid `:` in filenames because classic Apple path conventions and some tooling treat it specially.
3. Avoid `/` because it is the POSIX path separator.
4. Avoid leading or trailing whitespace and visually similar Unicode names; normalization differences can confuse cross-platform tools.
5. Keep generated paths portable across macOS, iOS packaging, archives, and Git.
