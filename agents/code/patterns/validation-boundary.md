# Validation Boundary Rules

Use this file for validation-boundary-specific rules about parsing, schemas, runtime guards, trust boundaries, normalization, sanitization, and safe internal data shapes.

Reference: [Data validation](https://en.wikipedia.org/wiki/Data_validation).

In software development, a validation boundary is the place where unknown or untrusted data is checked before it enters trusted internal code. Use validation boundaries at inputs such as APIs, forms, files, CLIs, environment variables, webhooks, database reads, generated artifacts, model output, and tool output. Good validation parses once, reports precise failures, preserves raw input only when safe, converts valid data into semantic internal types, and keeps validation rules close to schemas, contracts, or domain policies.

In agentic programming, validation boundaries are especially important because agents often consume tool output, generated files, logs, model responses, browser state, and user-provided snippets. Agents should not assume these inputs are correct just because they came from a familiar tool. A small validator, schema check, fixture, or smoke test can turn uncertain external data into observable, repeatable evidence before implementation code depends on it.

## Related Patterns

1. [Error handling / result types](error-handling-result-types.md) define how validation failures are represented, propagated, logged, and shown to users.
2. [State machines](state-machines.md) can reject invalid transitions and keep invalid input from creating impossible states.
3. [Functional reactive programming](functional-reactive-programming.md) benefits when validated inputs feed deterministic derived state.
4. [Stigmergy](stigmergy.md) benefits when validation artifacts, fixtures, and reports leave traces that guide future review and testing.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
