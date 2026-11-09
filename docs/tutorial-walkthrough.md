# Annotated JUMP Hub tutorial walkthrough

Temporarily at **PDF32–42**, after the main talk and all existing extra slides, at the presenter's request. Do not move these into the main story yet. Each frame in `tutorial-walkthrough.tex` is independent and carries an interpretation cue. Both Org and the Overleaf root include that one file.

The eleven source images are the figures from the [JUMP_rr step-by-step tutorial](https://broadinstitute.github.io/jump_hub/howto/interactive/1_jumprr_steps.html), including its two annotated gallery/control screenshots. Red boxes, arrows, panel labels and original pixels are unchanged. The images are stored at their original resolution; only their proportional display size changes on the slides. Their mixed aspect ratios mean some text is small in the full-image overview. Targeted zooms can be chosen later without losing the original artwork.

## Step-by-step interpretation

| PDF | Step | Source | What to explain |
|---|---|---|---|
| 32 | Is my gene represented? | Figure 3 | Read the highlighted search field and dataset columns. Counts represent gene/reagent coverage, not replicate numbers or evidence of a phenotype. |
| 33 | Read the definitions | Figure 1 | The highlighted definitions and filter controls establish what each field means before interpreting its values. |
| 34 | Understand a result row | Figure 2 | A row summarizes a feature–perturbation association, not an individual cell or experimental replicate. The screenshot's sort order is not a biological ranking. |
| 35 | Choose the query | Figure 4 | Panels A–D show column selection, an exact symbol, a family pattern and a synonym search. A broader query changes the set of perturbations returned. |
| 36 | Combine filters and export | Figure 5 | The red box identifies export links. These are filtered results from a ranked subset, not exhaustive profiles. Save filters, identifiers and source. The pictured interface is historical; avoid promising today's exact export behavior from this screenshot. |
| 37 | Interpret overall activity | Figure 6 | The boxed corrected p-value is computed per perturbation. Repeating it across feature rows does not make the rows independent evidence. It is not a per-feature p-value or an effect size. |
| 38 | Interpret feature changes | Figure 7 | The red box marks per-feature significance. A displayed 0.0 is rounded source output, not an exact probability of zero. Review effect size, rank, cell count and image quality as well. |
| 39 | Separate the two questions | Figure 8 | ORF example: individual features can be significant even if the overall perturbation activity test is not. Keep modalities and tests distinct; lack of overall significance is not proof of no effect. |
| 40 | Interpret profile matches | Figure 9 | Red marks signed similarity; blue marks external resources. Similarity prioritizes hypotheses, not proof of a common pathway, mechanism or physical interaction. Anticorrelation does not establish rescue. Example images are not automatically matched-control comparisons. |
| 41 | Find the perturbed images | Gallery steps 1–3 | Follow the numbered annotations: select the perturbation and apply the filter. Identify source/plates before selecting comparison images. |
| 42 | Add appropriate controls | Gallery steps 4–9 | Retain source and plates, then include the documented negative controls. Inspect density, staining, focus and fields/replicates before making biological claims. Match other design variables where available. |

These are **historical SLC2A2 and MYT1 tutorial examples**, not outputs from the current nocodazole/blebbistatin examples. In particular, the gallery figures show genetic controls (`no-guide`, `non-targeting`); the compound demo instead uses DMSO controls. The images do not constitute a fresh analysis or validation of their displayed numbers.

## Sources, attribution and unchanged originals

The tutorial markdown was read from JUMP Hub commit `86c0ff7c3420b236ab6c29fe49587bc3ba96fb77`. The images themselves come from the three linked Zenodo records. Each record credits **Broad Institute** and specifies **CC BY 4.0**:

- [Main tutorial figures](https://zenodo.org/records/15252378).
- [Gene availability figure](https://zenodo.org/records/16878487).
- [Gallery/control figures](https://zenodo.org/records/16878778).
- [License](https://creativecommons.org/licenses/by/4.0/).

At the presenter's request, the gray source/license/history footers have been removed from all eleven walkthrough slides. Attribution is retained in the per-frame TeX comments, the source links and license above, and the provenance manifest. New interpretation captions are distinct from the source artwork. `tutorial-screenshots-provenance.json` records source URLs, original filenames, exact SHA256 hashes, dimensions, byte sizes, retrieval time, tutorial-document hash and source license metadata. This license applies to these tutorial images, not to all other presentation material.

When first appended, these screenshots left the existing 30-page deck pixel-identical. Subsequent main-talk edits added the extreme-nocodazole/blebbistatin sequence and shifted this bank by one page; gray source footers were then hidden at the presenter's request. The screenshot pixels and interpretation captions remain unchanged.
