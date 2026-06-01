# Tracing / Spans Rules

Use this file for tracing- and span-specific rules about operation names, parent-child work, timing, attributes, correlation IDs, diagnostics, and observability.

References: [Effect tracing](https://effect-ts.github.io/effect/effect/Effect.ts.html), [Effect Stream tracing](https://effect-ts.github.io/effect/effect/Stream.ts.html), [Effect Tracer](https://effect-ts.github.io/effect/opentelemetry/Tracer.ts.html).

In software development, tracing records named operations as spans with timing, parent-child relationships, attributes, and outcomes. Use tracing when a workflow crosses APIs, queues, subprocesses, streams, background jobs, user actions, or external services. Good tracing names work semantically, preserves correlation across boundaries, avoids secrets in attributes, and makes slow or failed paths easy to find.

In agentic programming, traces give agents direct evidence about what happened during a run. A trace can show which tool call, build step, server request, stream stage, or retry consumed time and where failure started. Agents should add spans around important workflow boundaries when logs alone are too flat, and should treat missing observability for complex workflows as technical debt.

## Related Patterns

1. [Fibers / structured concurrency](fibers-structured-concurrency.md) need parent-child trace relationships for concurrent work.
2. [Typed errors / cause trees](typed-errors-cause-trees.md) provide failure provenance that traces can attach to spans.
3. [Streams](streams.md) benefit from spans around long-running or multi-stage processing.
4. [Stigmergy](stigmergy.md) treats traces as durable coordination artifacts for future humans and agents.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
