# Live prompts: use an agent to query JUMP

Use an external coding agent with web access and a Python execution tool. These are prompts for the presenter to send, not instructions to execute automatically on opening this file. Start in a fresh, disposable analysis folder. SLC2A2 is a worked example in the Hub tutorial, not a surprise discovery.

## 1. Find the data (~2 minutes)

> I study SLC2A2. Is it represented in JUMP, and does perturbing it change cell morphology? Start at https://broadinstitute.github.io/jump_hub/ and read the relevant documentation. Use the public data and tools linked there, not an answer from memory. Check gene availability and resolve the exact JCP2022 reagent IDs. Treat CRISPR and ORF separately. Inspect the actual table schemas before writing queries. Execute the code and show a small table of reagent IDs, phenotypic activity and corrected activity p-values, with source URLs. Download only the small summary tables, not the full image dataset. If the data cannot be reached or the symbol is absent, say so; do not invent results.

## 2. Follow the evidence (~2 minutes)

> For SLC2A2 CRISPR, retrieve the five most similar and five most opposing non-self perturbations among the published match rows. Include their JCP2022 IDs and signed similarity values. Identify the leading reported morphological features with effect sizes and feature ranks. Distinguish perturbation-level activity statistics from per-feature statistics. Tell me whether these tables contain all comparisons/features or only ranked subsets. Save the query code, CSV outputs, retrieval time and input hashes so I can reproduce what you did.

## 3. Check the images and interpretation (~2 minutes)

> Find image examples for SLC2A2 CRISPR and documented negative controls from the same source and plates. Show the source, plate, well and image URLs; explain how you matched the controls. Open a small, clearly labeled selection of images, rather than downloading all fields. Tell me what we can inspect for cell-count, staining, focus or segmentation issues. Separate actual visual observations from hypotheses. Do these results establish a shared mechanism with a match, or only suggest follow-up experiments? State the main limitations and one useful follow-up.

## Optional stretch: turn the query into a small explorer

> Now that the query is checked, make a small interactive explorer with a gene input, separate CRISPR/ORF results, source links, match tables and labeled image/control views. Reuse the verified query code and cached data. Display missing data and source limitations explicitly. Do not silently change analysis parameters or recompute significance.

Building an explorer is optional; the core demo succeeds with sourced tables and inspected images. Do not start an application server or install new tools on the presenter's machine without checking first.
