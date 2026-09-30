# Coding Principles

Use these principles when writing, reviewing, or refactoring code in this project. Existing project requirements and the user's requested scope determine the implementation. Avoid speculative features, configurability, abstractions, and unrelated cleanup.

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
4. Test utility functions and shared modules where their contracts, behavior, and callers need regression protection.

Reasoning: clean reuse is evidence that a boundary is meaningful. If code can be reused cleanly, it is usually better factored, easier to test, and less likely to duplicate behavior elsewhere.

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
4. Name non-obvious or shared values and derive related values from their authoritative source. Keep environment-specific thresholds in configuration.
5. Validate config at startup or load time so failures are early and clear.
6. Document required config keys, acceptable values, and where local overrides belong.

Reasoning: code and config change for different reasons. Keeping them distinct makes deployments safer, tests clearer, and local customization less likely to leak into shared source.

## Security Concerns

1. Treat security-sensitive code as high risk.
2. Prefer explicit allowlists over broad trust at system boundaries. Respect established internal contracts without speculative defensive layers.
3. Avoid logging secrets, credentials, tokens, raw auth headers, private keys, or sensitive payloads.
4. Review authentication, authorization, filesystem, network, shell, and deserialization changes with extra care.
5. Follow the project's disclosure policy for sensitive findings. Keep raw sensitive evidence in private notes; routine fixes do not require a new disclosure interview.

## Privacy And Data Leaks

1. Do not commit secrets, full local paths, usernames, tokens, passwords, private keys, credentials, or machine-specific account data.
2. Do not commit email addresses, street addresses, phone numbers, SSNs, account numbers, or any other personal or private information without explicit approval.
3. Treat secrets in comments, deleted files, old commits, logs, generated output, and review artifacts as real leaks. Once committed, sensitive data is buried in Git history and can be very difficult to remove or hide.
4. Treat accidentally committed secrets as very high risk in public, shared, or open source repositories. Committed secrets should be assumed likely to become compromised secrets.
5. Treat a committed secret as both an active credential incident and an information-exposure incident. Revoke or rotate it and remove public evidence immediately and in parallel; then audit, coordinate, rewrite reachable history, and verify both containment paths.
6. Keep private notes, raw tool outputs, logs, exports, caches, and review artifacts in ignored underscore folders.
7. Use the configured privacy preflight as a commit and publication gate. Run staged, push-range, history, and auxiliary-ref modes according to the [privacy rules](rules/privacy-and-publication.md).
8. Do not treat a new `.gitignore` rule as remediation for content already tracked, committed, or retained by another ref.

## Verification

- Choose checks that demonstrate the requested behavior and likely regressions. Add focused tests for behavior changes, bug fixes, and shared contracts where they provide useful confidence.
- TDD is an available technique, not a required sequence for every edit. Documentation and low-impact mechanical changes can use direct checks rather than new tests that mirror the implementation.
- Run relevant existing checks and address failures caused by the change. Broaden or repeat verification when changes, failures, or unresolved risks justify it.
- Observe visual and interactive results in the app or a representative rendered surface. State what was checked and any remaining observation gaps.

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

1. Treat slow feedback loops as technical debt, product risk, and engineering risk. Fast feedback enables several focused good changes; slow feedback encourages one large, risky change.
2. Prefer hot reload, direct app inspection, internal state inspection, screenshots, logs, and targeted tests when working on web pages, apps, and visual interfaces.
3. Avoid relying only on slow continuous integration for debugging. A slow CI-only loop makes agentic workflows tedious, error-prone, and easy to abandon.
4. When build or test loops get long, recommend improving the pipeline: parallel tasks, cached builds, affected-only tests, focused test commands, stable fixtures, or faster local previews.
5. Make loop speed visible. Document useful commands, expected runtimes, ports, preview URLs, and observation tools.
6. Treat loop improvements as enabling work, not gold plating, when they materially improve iteration speed and reliability.

## Supported Targets

For a new project, record the required runtime/platform floor when choosing its stack. Preserve established support in existing projects. Ask when a change needs an unresolved support decision; add or remove compatibility paths only within the agreed scope.

## Named Event Handlers And Callbacks

Extract complex, reused, or independently testable callback behavior into named
functions at module scope when practical, or at stable component scope when a
framework lifecycle requires it. Use the language and framework's idioms; inline
callbacks are appropriate when their behavior and captured state are clear.

In larger apps, deeply nested callbacks can hide dependencies, duplicate behavior,
complicate cleanup, retain state, and make code difficult to test or reuse. Named
callbacks help keep files flatter, dependencies explicit, and lifecycles observable.

1. Flat control flow: named callbacks keep setup and orchestration readable instead of nesting behavior inside registrations, effects, timers, or animation loops.
2. Explicit dependencies: inputs and captured values should be visible in parameters or an explicit context rather than inherited accidentally from a closure.
3. Testability: meaningful callback behavior should be importable or separable into a unit that can be tested with explicit inputs.
4. Reuse and DRY: one named callback or underlying function can serve multiple callers without copying the implementation.
5. Stable identity and cleanup: the same function reference can be passed to registration and removal APIs, making lifecycle symmetry mechanical and reviewable.
6. Diagnostics: named functions appear clearly in stack traces, profiles, logs, and developer tools.
7. Leak prevention: naming alone does not release resources. Every listener, timer, animation frame, subscription, observer, or external callback registration must also have explicit symmetric teardown or cancellation. Any intentionally captured values must be bounded and auditable.
8. Code review: inspect complex callbacks and hidden closure dependencies. Extract behavior when that improves clarity, reuse, or testing, and verify the cleanup path.
9. Thin adapters: when a value genuinely must be captured at registration or schedule time, pass it through a minimal adapter such as `() => handleSnapTimeout(snapId)`. The adapter delegates; it does not own behavior.

Example:

```js
// At module or stable component scope: named, reusable, testable.
function handleNodeTransitionStart(event) { /* ... */ }
function handleNodeTransitionEnd(event) { /* ... */ }
function handleSnapQuietTimeout(snapId) { /* ... */ }

function attachNodeListeners(target) {
  target.addEventListener("transitionstart", handleNodeTransitionStart);
  target.addEventListener("transitionend", handleNodeTransitionEnd);
}

function detachNodeListeners(target) {
  target.removeEventListener("transitionstart", handleNodeTransitionStart);
  target.removeEventListener("transitionend", handleNodeTransitionEnd);
}

attachNodeListeners(element);
const snapQuietTimer = setTimeout(
  () => handleSnapQuietTimeout(currentSnapId),
  SNAP_EDGE_TAIL_MS,
);

// Teardown uses the same listener identities and cancels scheduled work.
detachNodeListeners(element);
clearTimeout(snapQuietTimer);
```

## File Length

1. Treat file length as a signal to inspect cohesion. Split files when responsibilities or navigation justify it; line counts alone do not require refactoring.
2. Generated files, declarative data, and demonstrably cohesive modules may remain long.
3. Choose decomposition that fits the code: focused modules, separation of concerns, reusable functions, components, or other language-appropriate units.

## Completion

Finish the authorized task and its relevant verification before handing it back. A progress summary is not completion while requested work remains. Report concrete blockers and continue independent work when possible; keep updates and the final result concise and evidence-based.
