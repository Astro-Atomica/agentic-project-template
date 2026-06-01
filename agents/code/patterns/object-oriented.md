# Object-Oriented Rules

Use this file for object-oriented rules about classes, interfaces, inheritance, composition, and lifecycle boundaries.

References: [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming), [Multiple inheritance](https://en.wikipedia.org/wiki/Multiple_inheritance).

In software development, object-oriented design groups related state, behavior, identity, and lifecycle rules behind named boundaries. Use it when the domain has meaningful entities, services, resources, policies, or collaborators that benefit from stable interfaces. Good OO code favors clear responsibilities, composition over deep inheritance, explicit ownership, testable collaborators, and small objects that protect invariants instead of becoming broad containers for unrelated behavior.

Multiple inheritance lets a class or object inherit from more than one parent, which can be useful when capabilities are genuinely orthogonal. Treat it carefully because it can create ambiguity, especially when two parents provide the same member or share a common ancestor. Prefer explicit conflict resolution, shallow hierarchies, and composition when behavior ownership is unclear.

In agentic programming, OO boundaries help agents edit safely because they make ownership and behavior local. A class, interface, or service with a crisp contract gives an agent a smaller surface to inspect, test, and refactor. Weak OO does the opposite: vague manager objects, hidden global state, and deep inheritance make agents chase behavior across too many files and increase the chance of partial fixes.

## Related Patterns

1. [Mixins](mixins.md) can add reusable behavior to OO systems when inheritance would be too broad, multiple inheritance would be ambiguous, or copy-paste would drift.
2. [State machines](state-machines.md) fit naturally inside objects that have lifecycle, permissions, workflow, or mode-dependent behavior.
3. [Event streams](event-streams.md) can be represented with OO producers, consumers, event stores, and subscription lifecycles.
4. [Stigmergy](stigmergy.md) benefits when OO boundaries define where traces are created, read, validated, and retired.

Put general programming guidance in `agents/PRINCIPLES.md`, `agents/code/README.md`, or the most general file you can. Placing it in a language- or pattern-specific file limits it to only that language or pattern.
