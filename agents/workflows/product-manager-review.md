# Product Manager Review Workflow

Use this workflow when reviewing as a product manager, especially before declaring a feature, UX change, or user-facing flow complete.

## Review Lens

A PM review focuses on features, functionality, and fully integrated user flows. It asks whether the delivered experience matches the requested product intent, not only whether the code is technically correct.

## Inputs

1. User request, issue, PR, ticket, or planning note.
2. `_private/feature-requests.md`, if present.
3. Relevant tracked product docs, design docs, UX requirements, screenshots, and acceptance criteria.
4. The running app, rendered artifact, screenshot, or other observation path.

## Workflow

1. List the requested features and expected user-visible outcomes.
2. Check `_private/feature-requests.md` for feature requests or product decisions that may have been lost across context compaction or new threads.
3. Compare the implementation against each requested feature, acceptance criterion, and UX requirement.
4. Walk every primary user flow end to end from the user's point of view.
5. Check integration points: navigation, empty states, loading states, error states, permissions, persistence, undo/redo, refresh, and cross-device or responsive behavior when relevant.
6. Visually validate all UX requirements using the best available observation path: direct app inspection, screenshot, rendered document, app preview, video, artifact inspection, or browser tooling when applicable.
7. Record missing or deferred feature work in `_private/feature-requests.md` when it should survive the current thread.
8. Record technical debt separately in `_code_review/` when it should be tracked but not fixed in the current task.
9. Report product findings first, ordered by user impact.

## Findings To Flag

1. Requested feature is missing, partially implemented, or hidden behind an unreachable path.
2. A user flow works only in isolation but is not integrated into the real app or surface.
3. UX requirement was implemented in code but not visually validated.
4. State is lost across refresh, navigation, reload, save/load, undo/redo, or handoff when the product expects continuity.
5. Empty, loading, disabled, permission, and error states are missing or inconsistent.
6. Copy, labels, controls, or layout contradict the requested product behavior.
7. A feature request appears to have been dropped during context compaction, scope shifts, or thread changes.

## Output Shape

1. Findings first, with feature or flow references.
2. Missing feature requests or lost requirements.
3. Visual validation performed.
4. User flows exercised.
5. Residual product risks and follow-ups.
