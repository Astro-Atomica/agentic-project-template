# Mixins Rules

Use this file for mixin-specific rules about composition, shared behavior, inheritance boundaries, and reuse.

References: [Mixin](https://en.wikipedia.org/wiki/Mixin), [Trait](https://en.wikipedia.org/wiki/Trait_%28computer_programming%29).

In software development, mixins package reusable behavior so it can be composed into multiple types, components, or modules without copying the implementation. Use them when shared behavior is real and semantic, not just visually similar code. Good mixins have narrow responsibility, explicit dependencies, predictable conflict behavior, and tests that prove the shared behavior works in more than one host.

Mixins sit near several multiple-inheritance-adjacent patterns: traits, protocols, interfaces with default methods, modules, extension methods, delegation, and object composition. Use the local language's clearest mechanism, but keep the same design rule: shared behavior should have an explicit name, explicit requirements, and obvious conflict behavior. Do not create separate pattern files for every variant unless the project develops enough specific rules to justify the split.

In agentic programming, mixins can prevent agents from producing flat copy-and-paste code when several files need the same capability. A well-named mixin gives the agent a semantic reuse point to extend, test, and document. Avoid using mixins as a dumping ground for unrelated helper behavior; when the composition boundary gets unclear, prefer a smaller helper, service, trait, component, or plain function.

## Related Patterns

1. [Object-oriented design](object-oriented.md) often provides the class, interface, or lifecycle boundary where mixins are applied.
2. [Functional reactive programming](functional-reactive-programming.md) can use mixins to share reactive sources, subscriptions, or effect cleanup patterns.
3. [State machines](state-machines.md) can be mixed into hosts when several objects share the same lifecycle model.
4. [Stigmergy](stigmergy.md) benefits when mixins centralize how traces, logs, review artifacts, or process markers are written and cleaned up.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
