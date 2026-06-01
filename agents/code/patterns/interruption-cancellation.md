# Interruption / Cancellation Rules

Use this file for interruption- and cancellation-specific rules about stopping work, cleanup, abort signals, timeouts, teardown, and cancellation-aware APIs.

References: [Effect interruption](https://effect-ts.github.io/effect/effect/Effect.ts.html), [Effect Fiber interruption](https://effect-ts.github.io/effect/effect/Fiber.ts.html).

In software development, interruption and cancellation let work stop intentionally before normal completion. Use this pattern for long-running requests, background jobs, streams, subprocesses, file operations, previews, tests, watchers, and any workflow that may be superseded. Good cancellation runs cleanup, releases resources, distinguishes cancellation from failure, avoids leaving partial state, and makes uninterruptible regions small and justified.

In agentic programming, cancellation is essential because agents often start work speculatively, rerun tests, restart servers, or abandon a path after new information appears. Agents should prefer cancellable APIs, record shutdown commands for external processes, and verify that cleanup actually happens. A workflow that cannot be cancelled safely can trap future agents in stale processes, locked files, or misleading state.

## Related Patterns

1. [Fibers / structured concurrency](fibers-structured-concurrency.md) define who owns cancellable child work.
2. [Typed errors / cause trees](typed-errors-cause-trees.md) preserve cancellation as a distinct cause.
3. [Schedules / retry policies](schedules-retry-policies.md) should stop retrying when cancellation or a deadline occurs.
4. [Singletons](singleton.md) and [factories](factory.md) should expose cleanup paths when they create or own cancellable external resources.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
