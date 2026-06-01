# Factory Pattern Rules

Use this file for factory-pattern-specific rules about object creation, construction boundaries, product selection, dependency setup, and hiding concrete implementation choices.

Reference: [Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern).

In software development, the factory pattern centralizes object creation so callers do not need to know every concrete class, constructor detail, setup step, or dependency choice. Use factories when construction has semantic rules, configuration-based selection, validation, dependency wiring, platform variation, test doubles, or repeated setup that would otherwise be copied across the codebase. Good factories return stable interfaces or semantic types, keep creation logic close to the decision rules, and avoid becoming broad service locators with hidden global behavior.

In agentic programming, factories help agents avoid copy-and-paste construction code. A well-named factory gives the agent one obvious place to add a new implementation, update setup rules, inject test doubles, or validate configuration. Agents should test factory selection and failure paths because a broken factory can make many callers fail in the same way.

## Related Patterns

1. [Object-oriented design](object-oriented.md) often provides the interfaces, products, and lifecycle boundaries a factory creates.
2. [Validation boundaries](validation-boundary.md) can check configuration or input before a factory creates trusted internal objects.
3. [Error handling / result types](error-handling-result-types.md) define how unsupported product types, missing dependencies, and construction failures are reported.
4. [Singletons](singleton.md) sometimes use factories for controlled creation, but shared lifetime should be explicit and tested.
5. [Stigmergy](stigmergy.md) benefits when factories create observable traces for generated resources, temporary services, or workflow artifacts.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
