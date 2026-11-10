# OPA1 literature example and integrated JUMP workflows

The main sequence is now **nocodazole as an extreme opening image example → published OPA1 genetic-perturbation evidence → gene lookup → interpretation of published JUMP tutorial examples → agent-assisted navigation**. Slide wording is direct; study-design and provenance details live here.

## Published genetic example

**Griparic L, Kanazawa T, van der Bliek AM. (2007). Regulation of the mitochondrial dynamin-like protein Opa1 by proteolytic cleavage. Journal of Cell Biology 178:757–764.**

- [DOI](https://doi.org/10.1083/jcb.200704112); [full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064541/).
- Published microscopy: Fig. 3A, scrambled-siRNA control; Fig. 3G, pan-Opa1 siRNA at two days. HeLa cells, MitoTracker staining.
- The slide reproduces those two panels, with their original panel labels. The 400×726 source JPEG is retained in full; panel crops are 198×147 and 198×148 pixels. No source-image resampling, recoloring or contrast editing was performed.
- The figure caption reports a 10 µm scale bar for the complete figure; individual cropped panels do not include that bar. Do not add a newly inferred scale bar.
- Published Results report that **99% of cells transfected with Opa1 siRNA alone had fragmented mitochondria**. The slide quotes that result; no image recount or new statistical analysis was performed.
- The study distinguishes pan-Opa1 depletion from exon-specific knockdowns and combined Opa1/Yme1 depletion. The selected example is pan-Opa1 depletion, not a claim that every OPA1 manipulation has an identical effect.
- These images are RNA-interference experiments, not JUMP CRISPR images. The labels on the slide identify the actual perturbation.

**Song Z, Chen H, Fiket M, Alexander C, Chan DC. (2007). OPA1 processing controls mitochondrial fusion and is regulated by mRNA splicing, membrane potential, and Yme1L. Journal of Cell Biology 178:749–755.**

- [DOI](https://doi.org/10.1083/jcb.200704110); [full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064540/).
- Fig. 1C: re-expression of individual OPA1 splice forms in OPA1-null mouse embryonic fibroblasts; mitochondrial morphology scored in 100 cells per experiment, with three independent experiments.
- Fig. 1D: fusion measured using the PEG cell-hybrid assay, seven hours after cell fusion.
- Selected fusion-active forms restore tubulation and fusion. The review slide describes those published findings without implying that all isoforms behave identically.

## JUMP coverage and workflow examples

The published gene-coverage reference lists **OPA1 in both CRISPR and ORF collections**. Source: [Zenodo record 16883068](https://zenodo.org/records/16883068), CSV SHA256 `40f12b266d632d8593b29c4a327cd82cffc36ad354e92815bf77e6d2f5008ec7`. This revision uses a lookup in that existing reference, not a new OPA1 profile analysis.

The annotated Hub screenshots keep their original examples visible: SLC2A-family availability, SLC2A2 feature/match tables, and MYT1 image/control lookup. Titles name those examples. They teach the route through the tools; they are not relabeled as OPA1 results.

- **Workflow 1:** start with a gene from the literature, find availability, read definitions, apply exact/family/synonym filters, and save the relevant view.
- **Workflow 2:** read rows, distinguish overall activity from feature changes, compare CRISPR with ORF, follow matches, and inspect images with same-source/plate controls.
- **Agent handoff:** retrieve primary papers, summarize published findings and link the corresponding Hub resources. No new statistics, model inference or experimental proposal is required for this literature review.

## Sources and image rights

The Griparic article's full-text license is **CC BY-NC-SA 4.0** after the initial publication restriction period. The cropped panels remain under that license. This is separate from the **CC BY 4.0** license of the Hub tutorial screenshots. Credit and source links remain on the primary literature-image slide; tutorial screenshot credit remains in source comments and provenance, as requested.

[opa1-literature-provenance.json](opa1-literature-provenance.json) records the full-text and figure URLs, hashes, crop coordinates, license and coverage reference. [tutorial-screenshots-provenance.json](tutorial-screenshots-provenance.json) records the untouched Hub images.

The superseded compound-analysis scripts and results are retained as historical artifacts. Their findings are not presented as OPA1 evidence. The presenter's concurrent Overleaf edits to the affiliation and nocodazole opening were preserved. Visible “checked November …” timestamps have been removed; retrieval dates remain in provenance files.
