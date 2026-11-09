# Extreme reference first; investigate blebbistatin next

Nocodazole is the opening extreme example, not the entire investigation. Use **blebbistatin-(+/-)** for the main live query. All computation/backends run on Oppy; use the forwarded interface on the MacBook. These are presenter prompts, not instructions to execute on opening this file.

## Opening question, with the nocodazole image pair

> Nocodazole gives an obvious change in these example images. Could cell density or a broad growth effect dominate its morphological profile? Treat it as an extreme reference, not proof that every similar profile shares its mechanism.

## Simple questions for the second drug

1. **Find it:** “Find blebbistatin in JUMP, using the Hub documentation. Resolve its reagent identity and stereochemical formulation. What annotations, doses and replicates are available?”
2. **Activity:** “Does this blebbistatin reagent have a detectable CellProfiler-derived profile? Distinguish overall activity from individual feature significance.”
3. **Matches:** “Which compounds have similar published profiles? Resolve names and mechanism annotations where possible. Do not label them myosin-II inhibitors or unrelated compounds without evidence.”
4. **Measurements:** “Which morphological measurements change? What could we measure to investigate contractility or cytokinesis, and which measurements would be insufficient?”
5. **Images:** “Show blebbistatin-treated cells beside DMSO controls from the same source and plate. Inspect several fields, not only one favorable image.”

The preflight verified summary values and one deterministic preview pair. Dose/time metadata, image/profile alignment, full-profile replicates and direct cytokinesis measures are not already checked.

## Live investigation

> Blebbistatin is known to inhibit myosin II and can affect contractility and cytokinesis. Starting at https://broadinstitute.github.io/jump_hub/, investigate JCP2022_052617 using CellProfiler profiles. Inspect measurements, images and matched controls; check whether cell shape and nuclear organization are consistent across replicates. Use nuclei-per-cell only after checking the segmentation and cell–nucleus assignments. Keep prior biology, actual observations and hypotheses separate. Show source URLs and the code you run; save the query and input hashes. Do not infer failed cytokinesis from DNA staining intensity alone.

## Human intervention

> Could this reflect cell density, staining, toxicity or segmentation errors? Check true cell counts and available QC. Do the image cohort, dose/time and profile release actually match? Tell me what remains untested.

## Produce something useful

> Create one slide answering: “Is the JUMP morphology consistent with blebbistatin's known biological effects?” Include a control/treatment image comparison, one defensible quantitative check and the main limitation. If the evidence is insufficient, say so instead of illustrating the expected answer. Build a preview without publishing.

## Optional editorial follow-up

> Make the headline less causal and show me the revised slide.

## Off-screen setup and interpretation checks

- Main reagent: **JCP2022_052617 / LZAXPYOBKSJSEX-UHFFFAOYSA-N**, annotated **blebbistatin-(+/-)**. Nocodazole reference: JCP2022_047835.
- No model/representation comparison or new image-encoder inference.
- Use the recorded summary tables as a bounded start; full replicate analysis needs aligned well-level profiles and metadata.
- Similarity is not proof of mechanism. The top saved match is not annotated as a myosin-II inhibitor; other high matches lack annotation in the saved snapshot. Do not silently substitute an expected peer.
- Match tables use processed/batch-corrected CP-derived profiles; feature tables provide separate interpretable summaries.
- DNA intensity is not DNA content, ploidy or nuclei-per-cell. Nearby nuclei are not necessarily in the same cell. Cell count, staining and segmentation matter.
- A less extreme published activity score does not establish lower toxicity or better specificity. Neither preview pair establishes replicate consistency.
- Reuse approved running backends; do not invent ports or reconfigure services without checking.
- If execution stalls, use `rehearsal-blebbistatin/` and explicitly identify it as a saved preflight. Nocodazole's old detailed extracts remain separate.
