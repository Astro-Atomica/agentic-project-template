# Fibers / Structured Concurrency Rules

Use this file for fiber- and structured-concurrency-specific rules about child work, joining, interruption, supervision, ownership, and observable concurrent execution.

References: [Effect Fiber](https://effect-ts.github.io/effect/effect/Fiber.ts.html), [Effect runFork](https://effect-ts.github.io/effect/effect/Effect.ts.html).

In software development, fibers are lightweight units of concurrent work, and structured concurrency means child work has an explicit owner, lifetime, result, and cancellation path. Use this pattern when a program starts background tasks, parallel jobs, watchers, worker pools, long-running IO, or independent workflow branches. Good structured concurrency makes spawned work joinable, interruptible, supervised, and cleaned up when the owning scope ends.

In UX, structured concurrency helps turn non-sequential behavior into traceable logic and state. Real interfaces often have overlapping async work: animations, network requests, optimistic updates, input streams, background validation, autosave, loading indicators, and cancellation. Agents can struggle to reconstruct UX state progression from scattered callbacks, so pair structured concurrency with functional state machines when a path must move cleanly from one state to the next under async pressure.

In agentic programming, structured concurrency prevents agents from losing track of subprocesses, preview servers, watchers, MCP helpers, test runs, and background jobs. Agents should record what they start, know how to observe it, and have a reliable cleanup path. A task that cannot be joined, interrupted, or inspected becomes hidden state and should be treated as technical debt.

Agents can be time-blind without structured data that ties concurrent work together. Record enough state, timing, parent-child relationships, start/stop events, and outcomes for an agent to reconstruct ordering, duration, causality, and what is still running.

## Related Patterns

1. [Interruption / cancellation](interruption-cancellation.md) defines how concurrent work stops safely.
2. [Tracing / spans](tracing-spans.md) make concurrent work observable across parent-child relationships.
3. [Singletons](singleton.md) can prevent duplicate competing process managers or preview services.
4. [State machines](state-machines.md) make UX and workflow progression explicit when concurrent work can complete in different orders.
5. [Stigmergy](stigmergy.md) benefits when concurrent work leaves durable process notes, logs, and status traces.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
