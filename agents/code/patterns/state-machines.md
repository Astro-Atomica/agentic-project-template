# State Machine Rules

Use this file for state-machine-specific rules about states, transitions, guards, events, and invalid-state prevention.

References: [Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine), [State pattern](https://en.wikipedia.org/wiki/State_pattern).

In software development, state machines make allowed states and transitions explicit. Use them when behavior changes by mode, workflow step, lifecycle phase, permission state, protocol status, animation phase, or long-running process status. Good state machines name every state, define valid transitions, reject invalid transitions deliberately, keep guards testable, and make side effects visible at transition boundaries.

In agentic programming, state machines reduce ambiguity for both humans and agents. When a workflow has a table or typed model of states and events, an agent can inspect the current state, determine the valid next actions, add tests for missing transitions, and avoid patching one branch while leaving another branch inconsistent. They also make product-manager review easier because expected user flows can be mapped directly to states and transitions.

## Related Patterns

1. [Event streams](event-streams.md) often provide the events that trigger transitions and the audit log that proves which path occurred.
2. [Functional reactive programming](functional-reactive-programming.md) can derive UI or system state from machine state and transition events.
3. [Object-oriented design](object-oriented.md) can encapsulate a machine behind a domain object, service, or policy interface.
4. [Stigmergy](stigmergy.md) appears when the current state, transition history, or validation artifacts guide the next human or agent action.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
