# One example throughout: nocodazole, CellProfiler only

Start with the simple JUMP_rr questions, then switch to the longer live investigation. All computation/backends run on Oppy; use the forwarded interface on the MacBook. These are presenter prompts, not instructions to execute on opening this file.

## Simple questions

1. **Find it:** “Find nocodazole in JUMP. What annotations, doses and replicates are available?”
2. **Activity:** “Does nocodazole produce a detectable morphological profile?”
3. **Matches:** “Which compounds have CellProfiler-derived profiles most similar to nocodazole? Show their mechanism-of-action annotations.”
4. **Measurements:** “Which morphological measurements change after nocodazole treatment?”
5. **Images:** “Show nocodazole-treated cells beside DMSO controls from the same source and plate.”

Presenter note: availability, activity, published match/feature rows and a single preview pair have been checked. Dose/time metadata and profile replicate alignment have not. Do not imply that every part of question 1 is already answered.

## Live investigation

> Investigate whether nocodazole retrieves other microtubule-disrupting compounds using CellProfiler profiles. Compare their retrieval against unrelated compounds, check consistency across replicates, and show representative images alongside the quantitative results.

## Human intervention

> Could this reflect cell density or toxicity? Check cell counts and available quality-control measurements before interpreting the matches.

## Produce something useful

> Create one slide answering: “Can morphology recover nocodazole's annotated mechanism?” Include a control/treatment image comparison, a retrieval plot and one sentence describing the main limitation. Build a preview without publishing.

## Optional editorial follow-up

> Make the headline less causal and show me the revised slide.

## Off-screen analysis setup

- Keep to CellProfiler-derived data; no representation comparison or model inference.
- Start from JCP2022_047835 / KYRVNWMVYQXFEU-UHFFFAOYSA-N, with the cached public summary tables and documented annotation snapshot.
- Use annotations to define peers before ranking. Do not classify unannotated compounds as unrelated; use a documented, annotated comparator set.
- The published match table is a ranked subset, not enough to calculate exhaustive peer enrichment or replicate consistency. Fetch aligned full well-level profiles only after confirming the intended source/cohort, dose/time and metadata.
- Match tables use processed/batch-corrected CP-derived profiles. Feature tables report interpretable CP measurements; they are not raw axes of the match space.
- Use true cell counts and QC measurements. Object numbers, parent IDs and closest-object IDs are not cell-count measurements even if ranked highly in the feature table.
- Standard Cell Painting does not stain tubulin. Image appearance is downstream morphology, not direct visualization of microtubule loss.
- Reuse approved running backends; do not invent ports or launch/reconfigure services on either host without checking.
- If the live analysis stalls, show `rehearsal-nocodazole/` and label it as the preflight, not a completed live replicate/enrichment analysis.
