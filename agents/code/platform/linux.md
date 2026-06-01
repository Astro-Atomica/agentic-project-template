# Linux Rules

Use this file for Linux-specific platform quirks, requirements, constraints, filesystem behavior, service behavior, desktop behavior, and compatibility notes.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a platform-specific file limits it to only that platform.

## File And Path Names

1. Linux filenames are generally case-sensitive; `File.txt` and `file.txt` may be different files.
2. Avoid `/` because it is the path separator and avoid the NUL byte because it cannot appear in path names.
3. Do not assume spaces, newlines, leading dashes, or shell metacharacters are safe in scripts; quote paths and prefer simple generated names.
4. Keep generated paths portable to common archive, container, package, and CI tooling.
5. Do not create names that differ only by case when the project may also be used on macOS or Windows.
