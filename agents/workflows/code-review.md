# Code Review Workflow

Use this workflow when a human asks for a review, audit, critique, or risk pass.

For a product-manager review focused on feature completeness, user flows, and UX requirements, use [product-manager-review.md](product-manager-review.md).

## Private Review Workspace

Store local review notes in `_code_review/`.

This folder is ignored by Git. It is for draft findings, scratch notes, raw diffs, check outputs, and review working files that should not appear on GitHub by default.

Suggested layout:

```text
_code_review/
  YYYY-MM-DD-{agent-model-version}-short-topic/
    notes.md
    findings.md
    technical-debt.md
    commands.md
    artifacts/
```

## Review Stance

Prioritize:

- bugs
- behavioral regressions
- security or privacy risks
- data-loss risks
- missing tests
- confusing operational hazards

Avoid turning reviews into style-only rewrites unless style creates real maintenance or correctness risk.

## Workflow

1. Create a review folder under `_code_review/`.
2. Capture the review target: branch, commit, PR, diff, path, or user request.
3. Inspect the relevant files and tests before writing findings.
4. Put scratch notes and command output summaries in `_code_review/`.
5. Keep a technical debt list in `_code_review/` for issues that should be documented and tracked but not tackled in the current task.
6. Report only polished findings to the user or PR.
7. Keep final findings actionable, specific, and tied to files/lines when possible.

## Technical Debt Tracking

Use `technical-debt.md` for issues discovered during review that are real but out of scope for the current task.

Track:

- architecture concerns
- cleanup candidates
- deferred test gaps
- temporary workarounds
- `!important` CSS usage
- risky duplication
- migration follow-ups
- slow build, test, preview, or CI feedback loops

Do not mix technical debt with the primary findings unless it affects the current task's correctness, security, privacy, or release risk.

## Finding Format

Use this shape in `findings.md` while drafting:

```text
## [P1] Short Finding Title

- File:
- Lines:
- Risk:
- Evidence:
- Suggested fix:
```

Priorities:

- `P0` - blocks release or can cause severe data/security loss
- `P1` - important bug or high-confidence regression
- `P2` - moderate correctness, reliability, or maintainability issue
- `P3` - minor issue, cleanup, or question

## Public Output

Do not paste raw scratch notes. Summarize:

- findings first, ordered by severity
- open questions or assumptions
- verification performed
- residual risk or test gaps

If there are no findings, say that clearly and mention what was checked.
