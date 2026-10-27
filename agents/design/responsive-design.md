# Responsive Design Across Screen Sizes

Responsive design must preserve the usefulness of each page or app at a wide
variety of sizes. Fitting inside a screen is only one part of success: users must
still understand the content, find the important actions, and complete tasks.

## Select And Refresh Targets

Start with currently popular mobile viewport sizes for the intended audience.
Use available aggregate audience data or current, relevant device/viewport
sources; record the source and date. If neither is available, label selected
targets as provisional rather than claiming they are popular. Do not introduce
analytics collection merely to obtain a test matrix.

Specify dimensions in CSS viewport pixels rather than physical panel resolution.
Record supported width/height ranges, orientations, and browser targets. Revisit
the matrix during significant responsive changes and release reviews as audience
data and device usage evolve. Popular sizes set the initial test priority; they
do not replace coverage of the rest of the supported range.

## Test In This Order

1. Use the [test sitemap](test-sitemap.md) to identify each page type and its
   primary user task. Test the priority mobile sizes first.
2. Build indexed arrays of eligible viewport options deterministically from the
   supported width/height ranges. Include sizes between common device presets;
   group candidates across narrow, intermediate, and wide sizes and different
   aspect ratios. Execute an RNG program to sample indices from each group for
   bounded coverage, following the [random-selection rules](../PRINCIPLES.md#random-choices-must-use-a-program).
   Do not ask the LLM to invent random dimensions or indices. Record the candidate
   arrays or generation rules, sample count, RNG implementation/seed, selected
   indices, and exact dimensions so failures can be replayed.
   Use bounded candidate arrays; do not materialize every possible width/height
   pair. Sample each dimension or use a manageable set of viewport pairs.
3. Add deliberate checks just below and above layout breakpoints and at the
   supported range boundaries. Include landscape, tablet, and desktop where
   supported; random sampling does not replace these checks.
4. Exercise navigation, forms, primary actions, and relevant alternate states.
   Check text enlargement, long content, overlays, safe areas, and available
   height when browser chrome or the on-screen keyboard is present. Confirm
   touch behavior on a real supported device when available; record the limits
   of viewport emulation when it is the only observation path.

Inspect readability, content priority above the fold, control reachability,
clipping/overlap, and unintended horizontal scrolling. Natural vertical scrolling
is expected. Dense tables or canvases may have intentional contained scrolling,
provided it remains discoverable and usable. Adapt the layout instead of merely
shrinking everything or hiding functionality to make a screenshot fit.
Where [persistent actions](../DESIGN.md#keep-important-actions-accessible-while-scrolling)
are used, test their usefulness and visibility throughout scrolling, including
the end of the page and focused form fields with the keyboard open.

## Rate Usefulness

Assign a rating per page/state and tested viewport after observing the primary
task. Record a short rationale and the specific friction or failure observed.

| Rating | Meaning |
| --- | --- |
| 5 - Excellent | Primary value is clear and the task is straightforward; content and controls remain comfortably usable |
| 4 - Good | Task completes easily, with minor visual compromises that do not impede use |
| 3 - Impaired | Task completes, but layout creates avoidable confusion, awkward navigation, or difficult controls |
| 2 - Poor | Important content/actions are hard to reach or understand; task completion is seriously hindered |
| 1 - Blocked | The primary task cannot be completed or essential content/control is inaccessible |

Aim for 4 or 5 throughout the supported range. Fix ratings of 1-3 or explicitly
record unresolved limitations; do not hide failures behind an average score.
Keep results and private captures in ignored review/output folders. Include page,
state, viewport, browser/device, task, rating, evidence, and next action.

Retest the failing size after a fix and retain it as a regression case. Recheck
nearby widths and affected priority layouts. Add fresh random samples on later
responsive changes while retaining known failure cases; avoid unbounded testing
once the agreed coverage passes and no new concern remains.
