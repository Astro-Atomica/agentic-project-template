# Android Rules

Use this file for Android-specific platform quirks, requirements, constraints, device behavior, store guidelines, and compatibility notes.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a platform-specific file limits it to only that platform.

## File And Path Names

1. Treat Android device storage and app assets as case-sensitive unless the specific filesystem or API says otherwise.
2. Keep asset and resource names lowercase, stable, and ASCII-safe when they may pass through Android build tooling.
3. Avoid spaces and shell-special characters in generated filenames because paths often pass through Gradle, adb, archives, and device shells.
4. Keep paths short enough to survive packaging, extraction, and host OS tooling.
5. Do not assume direct filesystem access to arbitrary shared storage; Android storage APIs and permissions may constrain paths.
