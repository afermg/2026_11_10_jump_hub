# Historical blebbistatin preflight — superseded

The active talk now uses published OPA1 literature and integrated Hub workflows. The following records the earlier compound-analysis plan; use [README.md](README.md) for current presentation instructions.

**Sequence:** nocodazole as an obvious extreme example → blebbistatin as the main CellProfiler-only investigation → ask the agent to query, inspect and test rather than assume mechanism from a match.

## Stage cues

- **PDF7:** show nocodazole and same-plate DMSO. Ask whether the obvious density/appearance change could dominate the profile. This is one field pair, not a direct assay of microtubule loss or proof of toxicity.
- **PDF8:** introduce blebbistatin's known myosin-II inhibition and possible effects on contractility/cytokinesis. These are prior biology, not conclusions inferred from JUMP.
- **PDF9–12:** ask about matches, activity, measurements, images and controls for blebbistatin. Keep the distinction between published observations and the expected phenotype.
- **PDF13:** switch to the live agent using [prompts.md](prompts.md).
- **PDF14:** return to the full-width investigation checklist. The checked-results column and closing slogan were removed at the presenter's request.
- Main talk ends at **PDF21**; existing extra slides are PDF22–31. The annotated tutorial walkthrough is **PDF32–42**, still at the end. The two historical single-cell recording slides are PDF30–31.

## Why blebbistatin?

Known action: inhibition of myosin II, which can alter actomyosin contractility and cytokinesis. [Straight et al., Science (2003)](https://doi.org/10.1126/science.1081412) established the cytokinesis application. The JUMP annotation identifies **blebbistatin-(+/-)**, not an enantiopure reagent.

The example lets us ask concrete morphology questions: cell shape, nuclear organization and, with validated segmentation, nuclei per cell. It does **not** let us infer cytokinesis failure from DNA intensity, nearby nuclei, or a single merged image.

Cytochalasin D was considered first but its exact PubChem InChIKey (`SDZRWUKZFQQKKV-JHADDHBZSA-N`) did not resolve in the cached JUMP compound metadata used here; no claim that it is universally absent from every JUMP release is made. Blebbistatin was selected for known biology and availability, not a flattering mechanism-retrieval result. The actual matches are retained even when their biology is unresolved.

## Checked blebbistatin preflight

Reused the same public summary-table snapshot as the nocodazole preflight. These are **published summary values**, not newly computed p-values or a completed replicate analysis.

- Reagent **JCP2022_052617**, InChIKey **LZAXPYOBKSJSEX-UHFFFAOYSA-N**.
- Corrected activity p-value **0.01278**, activity score **0.67118**; feature and match views agree.
- Nocodazole's activity score in the same snapshot is **0.88636**. A lower score is not proof of lower toxicity, a weaker mechanism, greater specificity or better reproducibility. The two drugs' doses/times have not been aligned.
- Reported nuclear DNA-channel median intensity: **Cohen's d = 2.241**. This is not an assay of DNA content, ploidy or failed cytokinesis. Staining, morphology and processing can affect it.
- Top returned match **PF-04418948 / JCP2022_052140, similarity 0.737**. The saved annotation calls it a prostaglandin inhibitor, not a verified myosin-II peer. Next: **JCP2022_018073 (0.732)** and **JCP2022_034452 (0.731)**, whose names/MOAs are unresolved in this limited annotation snapshot. Do not label unannotated compounds unrelated or infer a common mechanism from similarity.
- **8 gallery wells**, only **3 excluding source_7**. These counts describe image availability, not validated profile replicates. Across the full set, **256** DMSO wells match source+plate.

The public match and feature tables are ranked subsets; they do not support exhaustive enrichment or replicate-consistency claims. [Saved outputs and input hashes](rehearsal-blebbistatin/) retain those limitations.

## Image comparison

Original 996×996 merged JPEG previews: **source_2 / plate 1086291986 / site 1**, blebbistatin **M16**, DMSO **A02**. Selection was deterministic before viewing: lexically first treatment source/plate/well and same-source/plate lexically first control, site 1. No cropping, recoloring or contrast editing was performed. [Image provenance](rehearsal-blebbistatin/image-provenance.json) stores URLs and hashes.

Visual review: extended outlines and several closely paired/neighboring nuclei can be seen in the treatment field. This does not assign nuclei to individual cells, quantify multinucleation or establish failed cytokinesis. Boundaries require validated segmentation; pre-rendered contrast calibration is undocumented, so do not compare intensities quantitatively between the JPEGs. The image/profile cohort, dose/time, actual counts, QC and replicate consistency still need verification.

The original nocodazole field pair and saved analysis are retained independently. [Historical preflight details](nocodazole-reference.md) describe its source_2 / 1086292020 comparison and annotation-based match results; those are not blebbistatin results.

## Reproduce the offline summary extraction

```sh
uv run demo/check_blebbistatin.py \
  --data /work/scratch/amunoz/jump-nocodazole-preflight-20261109/data \
  --annotations /work/users/amunoz/projects/JUMP_lite/metadata/repurposed_compounds.tsv \
  --output /path/to/new-results
```

The script pins Polars 1.40.1, performs no network/LLM calls and refuses existing output directories. Prefetch the three compound Parquets and recorded annotation TSV from URLs in the saved provenance; cache the uv environment for offline use. Exact input hashes are recorded, including the annotation snapshot. The extractor records preview URLs but does not download images itself.

## Remaining live-workflow requirements

1. Confirm the intended full well-level CP profile release and image/profile alignment, source, dose and timing.
2. Retrieve true cell counts, QC and replicate metadata. Object IDs and parent IDs are not biological counts.
3. Validate cell/nucleus segmentation before using nuclei-per-cell as a cytokinesis-related measure.
4. Test consistency across replicates, distinguish cell density/technical changes from the expected morphology, and resolve match annotations before mechanistic interpretation.
5. Rehearse analysis and slide-preview backends on **Oppy**, using the forwarded **MacBook** interface. Backend readiness has not been established by this preflight.

If execution stalls, show the saved blebbistatin query and image pair and identify them honestly as **preflight results**, not a live or completed replicate-level analysis. Reuse approved running backends; do not launch duplicate services or download full datasets to the laptop without checking.
