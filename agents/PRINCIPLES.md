# Coding Principles

Use these principles when writing, reviewing, or refactoring code in this project.

## Core Principles

### Single Source Of Truth (SSOT)

Every meaningful fact, rule, schema, constant, workflow, or derived value should have one authoritative home.

1. Store canonical data in one place and reference it from everywhere else.
2. Derive secondary values from the source instead of copying them by hand.
3. Avoid parallel definitions that can drift, such as duplicate config defaults, repeated route names, copied validation rules, or mirrored type definitions.
4. When two places must agree, make the relationship explicit through shared code, generated output, tests, or documentation.

Reasoning: duplicated truth creates hidden synchronization work. Once there are two or more sources, no caller can know which one is canonical without substantial analysis, testing, or documentation review. SSOT keeps data consistent, meaningful, and semantic.

### Don't Repeat Yourself (DRY)

Repeated logic should become a shared function, module, type, test helper, component, mixin, or configuration entry when the repetition represents the same concept.

1. Remove duplication in behavior before duplication in appearance.
2. Keep intentional similarity when two concepts only happen to look alike for now.
3. Prefer small shared helpers over broad abstractions that hide important differences.
4. Use tests to lock down shared behavior before consolidating risky duplicated code.
5. Do not copy and paste mostly similar blocks of code. Use helpers, pure functions, generators, data-driven mappings, mixins, components, templates, or other patterns that preserve semantics and make shared behavior explicit.

Reasoning: DRY is about reducing semantic duplication, not forcing unrelated code through the same shape. Flat copied code lacks semantics and drifts slowly; fixing one copy while missing the others can turn a small change into hours of follow-up work. Good DRY makes changes safer; bad DRY couples things that should evolve independently.

### Good Code Is Modular Code

Code should be organized into small, understandable units with clear inputs, outputs, and responsibilities.

1. Keep modules focused on one coherent responsibility.
2. Push reusable logic out of large UI, command, route, or orchestration files.
3. Hide implementation details behind stable boundaries.
4. Prefer composition of small modules over large all-knowing files.
5. Make dependencies explicit so modules can be tested and replaced.

Reasoning: modular code lowers cognitive load. A reader should be able to understand, test, and change one part without loading the whole system into their head.

### Reusable Code Is Good Code

Reusable code captures a stable idea in a form that can serve more than one caller without special-case knowledge.

1. Design utility functions around clear contracts, not current call-site accidents.
2. Keep reusable code free of hidden global state and project-specific side effects unless those are part of its contract.
3. Name reusable code after the concept it implements, not the first place it was used.
4. Require tests for utility functions and shared modules.

Reasoning: reuse proves that a boundary is meaningful. If code can be reused cleanly, it is usually better factored, easier to test, and less likely to duplicate behavior elsewhere.

### Separate Concerns Clearly

Different kinds of work should live in different places: domain logic, presentation, persistence, networking, validation, orchestration, configuration, and side effects should not be tangled together.

1. Keep business rules out of rendering details.
2. Keep persistence and network code behind explicit interfaces.
3. Keep validation close to the boundary where data enters the system.
4. Keep orchestration thin; move real behavior into named modules or functions.
5. Avoid files that mix unrelated responsibilities just because they run in the same lifecycle.

Reasoning: tangled concerns make every change risky because unrelated behavior can break together. Clear separation lets each layer evolve, fail, and be tested independently.

### Keep Code And Config Distinct

Code should express behavior. Config should express environment-specific choices, feature switches, paths, thresholds, credentials references, and deployment settings.

1. Do not hard-code environment-specific values in source code.
2. Do not put complex business logic into config files.
3. Keep safe defaults in versioned config when useful, but keep secrets and private machine values out of Git.
4. Avoid magic numbers. Numbers should be named constants in configuration or derived semantically at runtime from other authoritative values.
5. Validate config at startup or load time so failures are early and clear.
6. Document required config keys, acceptable values, and where local overrides belong.

Reasoning: code and config change for different reasons. Keeping them distinct makes deployments safer, tests clearer, and local customization less likely to leak into shared source.

## Security Concerns

1. Treat security-sensitive code as high risk.
2. Prefer explicit allowlists over broad trust.
3. Avoid logging secrets, credentials, tokens, raw auth headers, private keys, or sensitive payloads.
4. Review authentication, authorization, filesystem, network, shell, and deserialization changes with extra care.
5. Do not explicitly call out security fixes in commit messages, branch names, PR titles, or public changelog entries unless the user requests it.
6. Ask the user for their security commit and disclosure patterns before committing security-sensitive changes.
7. Document security commit patterns in `_private/` rather than tracked docs so public history does not shine a light on security patches.

## Privacy And Data Leaks

1. Do not commit secrets, full local paths, usernames, tokens, passwords, private keys, credentials, or machine-specific account data.
2. Do not commit email addresses, street addresses, phone numbers, SSNs, account numbers, or any other personal or private information without explicit approval.
3. Treat secrets in comments, deleted files, old commits, logs, generated output, and review artifacts as real leaks. Once committed, sensitive data is buried in Git history and can be very difficult to remove or hide.
4. Treat accidentally committed secrets as very high risk in public, shared, or open source repositories. Committed secrets should be assumed likely to become compromised secrets.
5. Repair Git history after any accidentally committed secret or private data. A follow-up commit that deletes the value is not enough because the secret remains recoverable from history.
6. Keep private notes, raw tool outputs, logs, exports, caches, and review artifacts in ignored underscore folders.

## TDD First

1. Tests come first, then implementation.
2. Utility functions must have tests.
3. When changing behavior, add or update tests that define the expected behavior before relying on manual verification.

## Performance Is User Experience

Performance is a requirement and a feature, not an afterthought.

1. Treat performance as part of user experience. Slow software can feel frozen, confusing, broken, or unusable.
2. Treat performance as an energy concern. Wasteful work can waste battery, compute, bandwidth, and infrastructure.
3. Do not guess at the performance of a function, API, tool, page, or workflow. Test it.
4. Run a small, simple experiment and produce a baseline before making performance claims.
5. Choose an evaluation tool appropriate to the surface: benchmark, profiler, trace, timing log, load test, browser performance panel, screenshot/video timing, or resource monitor.
6. Record the baseline, input size, environment, command, and result location so future agents can compare changes.
7. If performance cannot be measured with current tools, say so and treat that as an observation-loop gap.

## Keep Edit-Review Loops Tight

The agent should advise the user on how to keep the project's edit-review loop fast, observable, and reliable.

1. Start simple and small. KISS first: use the smallest useful local workflow before adding infrastructure.
2. Treat slow feedback loops as technical debt, product risk, and engineering risk. Fast feedback enables several focused good changes; slow feedback encourages one large, risky change.
3. Prefer hot reload, direct app inspection, internal state inspection, screenshots, logs, and targeted tests when working on web pages, apps, and visual interfaces.
4. Avoid relying only on slow continuous integration for debugging. A slow CI-only loop makes agentic workflows tedious, error-prone, and easy to abandon.
5. When build or test loops get long, recommend improving the pipeline: parallel tasks, cached builds, affected-only tests, focused test commands, stable fixtures, or faster local previews.
6. Make loop speed visible. Document useful commands, expected runtimes, ports, preview URLs, and observation tools.
7. Treat loop improvements as enabling work, not gold plating, when they materially improve iteration speed and reliability.

## Legacy Support

This is a greenfield project by default. Legacy support must be scoped and clearly defined.

1. Until a legacy target is defined, the project does not support legacy APIs, legacy code, compatibility fallbacks, shims, or dual runtime paths.
2. Keep the project forward-looking by default.
3. Legacy support is opt-in. Ask for the supported version floor or support time window before adding compatibility paths.
4. Record the legacy support target in project documentation when it exists.
5. If no target is defined, prefer current-generation code and remove old paths instead of keeping them reachable.

## Named Event Handlers And Callbacks

Event handlers, `setTimeout` / `setInterval` callbacks, `requestAnimationFrame` callbacks, and listener functions must be defined as named functions at module or component scope, not inline anonymous functions.

Inline arrows are acceptable only as a thin adapter when closure variables must be captured at the call site.

1. Delegation and reuse: one named handler can be attached to multiple targets without duplicating the function body.
2. Symmetry with `removeEventListener`: the same reference must be passed to add and remove. Anonymous functions break this; named handlers make lifecycle cleanup mechanical and obvious.
3. Testability: a named handler can be imported and unit-tested with a synthetic event object. Logic trapped inside an anonymous closure inside an effect or setup block cannot.
4. Stack traces and DevTools: named functions appear by name in call stacks, profiling output, and DevTools listener panels. Anonymous arrows show up as `(anonymous)`.
5. Code review rule: flag any `addEventListener`, `on:xxx={...}`, `setTimeout`, `setInterval`, or `requestAnimationFrame` call whose second argument is a non-trivial inline function. Push for extraction to a named function.
6. Lambda wrap exception: when the callback genuinely needs a variable captured at schedule time, such as a monotonic round id, write the handler as `function handleFoo(roundId) { ... }` and pass `() => handleFoo(mySnapId)` at the call site. The inline arrow is a thin closure adapter, not a handler body.

Example:

```js
// At component scope: named, reusable, testable.
function _onNodeTransitionStart(ev) { /* ... */ }
function _onNodeTransitionEnd(ev) { /* ... */ }
function _onSnapQuietTimeout(snapId) { /* ... */ }

// At assignment: bare reference, or thin lambda adapter only.
el.addEventListener("transitionstart", _onNodeTransitionStart);
el.addEventListener("transitionend", _onNodeTransitionEnd);
_snapQuietTimer = setTimeout(() => _onSnapQuietTimeout(mySnapId), SNAP_EDGE_TAIL_MS);
```

## File Length

1. Keep files a reasonable length and under 800 lines.
2. Use or create a local tool to keep files under 1000 lines.
3. Error over 1000 lines.
4. Warn over 500 lines.
5. Treat file length as a forcing function for better coding patterns: modular code, separation of concerns, reusable units, object-oriented structure, mixins, or other appropriate decomposition.
