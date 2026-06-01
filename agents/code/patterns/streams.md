# Streams Rules

Use this file for stream-specific rules about incremental values over time, backpressure, chunking, transformation, resource safety, cancellation, and observation.

Reference: [Effect Stream](https://effect-ts.github.io/effect/effect/Stream.ts.html).

In software development, streams model values that arrive over time or too large to handle all at once. Use streams for logs, process output, file reads, network responses, UI events, telemetry, queue messages, generated content, and data pipelines. Good stream code makes ordering, termination, error behavior, backpressure, buffering, batching, and cleanup explicit.

In agentic programming, streams are one of the best ways to keep the loop observable while work is still running. Agents can watch test output, dev-server logs, tool output, browser/app events, and generation progress without waiting for a final blob. Streaming surfaces should expose enough structure for agents to summarize progress, detect hangs, cancel safely, and preserve useful traces.

## Related Patterns

1. [Event streams](event-streams.md) focus on ordered domain or system events; streams are the broader incremental data-flow shape.
2. [Schedules / retry policies](schedules-retry-policies.md) can pace polling streams, retries, and periodic observations.
3. [Interruption / cancellation](interruption-cancellation.md) should stop active streams and release upstream resources.
4. [Tracing / spans](tracing-spans.md) make long-running streams inspectable across chunks, stages, and downstream consumers.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
