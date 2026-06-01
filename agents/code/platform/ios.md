# iOS Rules

Use this file for iOS-specific platform quirks, requirements, constraints, device behavior, App Store guidelines, permissions, and compatibility notes.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a platform-specific file limits it to only that platform.

## File And Path Names

1. Treat app bundle resources as case-sensitive for portability, even when development happens on a case-insensitive macOS volume.
2. Do not rely on case-only filename differences; they can fail on common developer machines and confuse build artifacts.
3. Avoid spaces, punctuation-heavy names, and non-portable Unicode in generated bundle resource names.
4. Keep paths stable across Xcode, asset catalogs, archives, and App Store packaging.
5. Store user-generated files through the appropriate app container APIs rather than assuming arbitrary filesystem paths.
