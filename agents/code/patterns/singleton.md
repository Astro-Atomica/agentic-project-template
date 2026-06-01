# Singleton Pattern Rules

Use this file for singleton-pattern-specific rules about unique process-wide instances, shared resources, global access, lifecycle ownership, testing seams, and concurrency safety.

Reference: [Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern).

In software development, the singleton pattern restricts a class or service to one shared instance and often provides a global access point. Use it sparingly for resources that are genuinely unique within the process, such as runtime registries, app configuration views, resource pools, or platform handles. Good singleton usage makes lifecycle, initialization order, thread safety, teardown, and test replacement explicit instead of hiding mutable global state behind convenient access.

In agentic programming, singletons are risky when they hide mutable global state, but they can be useful when a program must explicitly own one external resource. For example, a singleton process manager can prevent agents from accidentally launching duplicate competing preview servers, test runners, MCP helpers, watchers, or background workers. Prefer dependency injection, explicit context objects, factories, or module-level pure functions unless the project has a clear reason for one shared instance. When a singleton is necessary, add tests for initialization, repeated access, duplicate-start prevention, cleanup, and failure behavior so future agents can change callers without accidentally preserving stale state.

## Related Patterns

1. [Factory patterns](factory.md) can centralize singleton creation, but should not obscure the fact that the returned object has shared lifetime.
2. [Object-oriented design](object-oriented.md) defines the ownership and lifecycle boundary for a singleton service.
3. [Validation boundaries](validation-boundary.md) should validate singleton configuration before the instance becomes shared state.
4. [Error handling / result types](error-handling-result-types.md) define how initialization and teardown failures are reported.
5. [Stigmergy](stigmergy.md) benefits when singleton lifecycle events leave observable traces in tests, logs, or process notes.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
