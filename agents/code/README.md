# Code Guidance

Read the guidance relevant to the current change. These files are customization points and focused references, not a required reading list. Follow [shared principles](../PRINCIPLES.md) and applicable project instructions.

## Layout

- [lang/](lang): language, framework, runtime, and markup rules. Includes small stubs such as [Python](lang/python.md), [TypeScript](lang/typescript.md), and [Godot](lang/godot.md), alongside substantive [CSS guidance](lang/css.md).
- [platform/](platform): operating system, browser, device, store, and automation constraints. Includes customization stubs and existing platform guidance.
- [env/](env): environment-specific agent behavior for [local development](env/local.md), [CI](env/ci.md), and [production](env/production.md).
- [patterns/](patterns): focused architecture references. Use them when the actual problem warrants it.

## Customize For The Project

Replace a relevant stub's prompts with short, concrete instructions: supported targets, conventions, commands, constraints, and verification expectations. Unfilled prompts are topics to customize, not requirements or evidence that a target is supported. Keep useful stubs as future customization points; add or remove them to suit the project.

Link applicable files from scoped `AGENTS.md` instructions or a project profile. Language files govern code conventions, platform files govern target constraints, and environment files govern where work runs; put shared rules in their authoritative home and resolve conflicting guidance explicitly.

Keep examples small and reference shared principles rather than repeating them. Keep secrets, private paths, account data, and restricted partner material local. Date vendor-dependent constraints and link public documentation when recording them.
