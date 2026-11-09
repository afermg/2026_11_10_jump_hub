# Presenter notes — 25 minutes

**Uncovering biological relationships through morphological profiling: The JUMP-Cell Painting dataset and tools**

Current revision: **28PDF pages,25main and3additional**. Main narration remains **23minutes /1380seconds**,plus2minutes buffer. At the presenter's request,the word2vec and biological-representation slides are restored separately on5and6;JUMP follows on7. Their30+30seconds replace the combined60seconds. Other slide contents are unchanged from the latest live version,including the clarified take-homes and the prompt beside the demo screenshot.

Tools15 is60seconds;demo16 is180seconds. Play the unchanged recording on **PDF16 / visible15**,return to **PDF17**. Controls18 precedes extraction19;Applications20 and MisLocus21 remain adjacent. Take-homes22,thanks23,references24,QR25. Additional workflow26,Nahual27,published model comparison28. Counters are one lower than PDF page numbers.

This is an explicit owner override of the earlier representation-merge suggestion;it does not reopen or resolve any review thread. Original artwork/data and release holds remain unchanged. Current cue authority: `page-map.json`.

## 1. Title — 0:15 (end 0:15)

Introduce the biological aim: connect cellular appearance to relationships among
genes, compounds and cell states. Name the FASEB Organelle Cross-Talk in Cellular
Homeostasis meeting. The confirmed date is 21 October 2026. The title gives the
presenter-supplied affiliation: **Carpenter-Shen Lab, Purdue University; Carpenter-Singh Lab, Broad Institute**, preserving the latest direct Overleaf edit.
The role label is omitted at the presenter's request.

## 2. What is Cell Painting? — 1:15 (end 1:30)

Explain the six-dye, five-channel assay using the unchanged I2K/Broad Retreat
channel panel. Point out nucleus, ER, nucleoli/cytoplasmic RNA,
actin/Golgi/plasma membrane, mitochondria and merged view. Describe staining
before measurements. Original labels and scale bar are unchanged.

## 3. Cell Painting turns images into measurements — 0:45 (end 2:15)

Follow stain → image → measure → compare. Introduce profiles as numerical descriptions of cells here, before the two feature-extraction routes. At the presenter's request, the displayed workflow is restored to the exact Mac-edited PDF from before the color-consistency edits. The earlier palette and cell drawings are unchanged; no new shape or color edits were made. These are illustrative schematic colors and shapes, not acquired fluorescence, measured phenotypes or validated health labels. Segmentation-object colors and heatmap colors have separate meanings. Original SVG/PDF bytes and the superseded derivative remain preserved.

Credit Chandrasekaran et al. (2021), Figure1a, with the intermediate I2K and Mac provenance retained. Similarity prioritizes hypotheses; it does not establish mechanism.

## 4. Morphological profiling: How to turn images into profiles — 0:45 (end 3:00)

Lead with: **Are control and perturbed cells different?** This grounds the A-versus-B case before the representation analogy.

Vectors make appearance practical to compare, search and group across a large
dataset. Classical CellProfiler features measure predefined quantities such
as area, shape, intensity, texture and spatial relationships. Learned
representations encode visual patterns through model training.

Features can be extracted per cell or image and aggregated into well/perturbation
profiles. Preserve the images so observations can be inspected. Normalization,
training objectives and experimental context affect comparisons. Neither route
alone removes batch effects or establishes mechanism; no universal superiority
claim is needed. Do not infer the exact representation used by an archived
interface screenshot from this general methods distinction. The author's new “Non-redundant” wording is preserved on-screen; learned representations are not mathematically guaranteed to have independent or non-redundant coordinates.

## 5. Words as vectors: word2vec — 0:30 (end 3:30)

Restored as a standalone slide at the presenter's request;allow30seconds. The control-versus-perturbed comparison is already established before this analogy.

On-slide sentence above the plot,using the presenter's final wording: **Learning can be viewed as compression**. The proposed “(fuzzy)” qualifier is not included. Use compression as a representational analogy,not a claim of lossless coding,guaranteed reconstruction or a formal property of every model.

Start with language: word2vec learns numerical representations from neighboring
words. Similar contexts can yield similar vectors, and some relationships can
appear as directions. Use man → woman and king → queen:
**v(king) − v(man) + v(woman) ≈ v(queen)**. The diagram is an original teaching
schematic with invented 2D coordinates, not a trained-model result or an accuracy
test. Real embeddings have many dimensions, not predefined age/gender axes.
Analogy behavior depends on training/evaluation and can reflect corpus biases.
The presenter requested removal of the visible “Illustrative 2D positions”
caption; the clarification remains here and in the SVG description.
Method reference: Mikolov et al. (2013), <https://arxiv.org/abs/1301.3781>.

The presenter replaced the removed Coordinate labels with **Feature 1**
(horizontal) and **Feature 2** (vertical). These are generic dimensions, not
invented semantic attributes. Follow this analogy with cell profiles,
then introduce JUMP, preserving the latest author-edited order.

## 6. From words to cells: vectors for comparison — 0:30 (end 4:00)

Standalone slide;allow30seconds. Blue denotes Control examples A/B;orange denotes Perturbation examples C/D,not different cell types. The legend labels are Control/Perturbation and the heading is Classical features;the figure's coordinates,colors,cell drawings and axes remain unchanged.

Transition: words describe language context; cell profiles describe morphological
appearance. This is an analogy for numerical representations, not a claim that
word2vec generated the cell features. Classical measurements and learned image
embeddings are distinct routes. Shortened figure labels retain this distinction.

Use A/B as Control examples and C/D as Perturbation examples. The vertical
axis reads exactly **Granularity Mito Channel**: an image-signal measurement
at a specified spatial scale in the mitochondrial channel. Granularity describes
signal structure across spatial scales, not mitochondrial fragmentation,
organelle number or cristae. Its value depends on scale and analysis settings;
the redrawn network-like/punctate cartoons do not define or determine a score. Larger outlines, clearer nuclei and separated tubules improve readability. The requested visible illustrative-data footer is removed, but these qualifications remain.
Both groups span the invented granularity values. The larger orange examples
illustrate one possible morphological difference,not a universal perturbation
response or evidence of causality. Controls,context and experimental validation
are required. The original artwork remains preserved;this is a label-only derivative.

Left: coordinates refer to defined measurements. Right: the same cells are
represented by abstract learned coordinates that can mix many visual patterns.
A useful vector need not have a one-to-one biological meaning for each axis.
Both plots are invented teaching schematics, not measured results, fitted
projections or embeddings from a named model. Two coordinates stand in for
many-dimensional profiles. Classical features are not automatically mechanistic,
and learned representations may be investigated with interpretability methods.

## 7. JUMP: Joint Undertaking for Morphological Profiling — 1:30 (end 5:30)

Expand Joint Undertaking for Morphological Profiling. Explain CRISPR knockout,
open reading frame (ORF) overexpression and compound treatment. ORF delivery
uses a lentiviral expression construct, not activation of the endogenous gene.
The published JUMP Methods specify a 48-hour ORF readout and no blasticidin
selection in the imaging wells. Call it **gene overexpression (ORF)**, not
necessarily transient expression: lentiviral delivery can support persistent
expression, and short assay duration does not establish transience. More protein
is not necessarily more normal protein activity; dosage, isoforms, localization,
cofactors and variable delivery can affect the phenotype. Cell Painting reads
morphology, not a direct measurement of expression/function for every construct.
Source: <https://doi.org/10.1038/s41592-025-02753-9>, Methods: Time point and ORF experiments.
Emphasize that **12 laboratories/data-generating centers** acquired the principal
JUMP dataset. This is not a count of every consortium/supporting partner. The
metadata has 13 source IDs: `source_7` and `source_13` came from the same center.
The JUMP Hub dataset overview and Terra guide confirm the 12-center interpretation
at revision `e742f5aa37472eb17f326ba8315d22b27e58f330`. Not every laboratory acquired
every modality or perturbation; source effects still matter when comparing profiles.
Give their scale: **7,975 CRISPR targets, ~12,600 ORF genes, and 115,794
compounds**. The presenter requested genes only on the ORF card. The latest direct Overleaf edit removes the audience-question bullet; do not restore it.

Counting basis: consortium metadata revision `016e865fa0691244e0860943e41c7d6a88ed2580`;
unique JCP2022 IDs present in wells, excluding canonical negative-control and
empty IDs, retaining positive controls. Total **138,897 perturbation IDs**.
The **15,128 ORF constructs** have **12,598** nonmissing supplied gene/locus
annotations, including XLOC annotations and eGFP. Constructs and genes are not
interchangeable. The presenter changed the visible headline to **nearly 136,000**:
115,794 compounds + 7,975 CRISPR targets + 12,598 ORF gene/locus IDs = **136,367**
modality-specific entries. That gene-level tally differs from the **138,897**
construct/reagent-ID total above; it is not a deduplicated count of unique genes
across modalities. These are full JUMP metadata counts, not JUMP-lite.
The verified construct-level inputs remain in `docs/jump-perturbation-counts.json`.

The overview also shows **~58.3 million single-channel TIFF images**. Sum the
`tiffs` column in the public `stats/cpg0016_source_images_tiff_count.csv` at
revision `016e865fa0691244e0860943e41c7d6a88ed2580`: **58,267,491** files across
12 source rows. This is the published cpg0016 image archive, including controls,
not a cell count, five-channel field count, or QC-passing profile subset. Source
rows are not acquisition-center counts. The published site table sums to
8,126,570 and does not reconcile with the TIFF total via a five-channel factor;
do not derive a site count by dividing the TIFF total. Exact sources, hashes
and the cross-check are in `docs/jump-image-counts.json`.

## 8. We make JUMP accessible via the JUMP Hub — 1:15 (end 6:45)

The removed methods-versus-biologists transition is now the subheading: **For experimental biologists and computational experts alike.** Its30seconds are retained here,for75seconds total. The screenshot is a fresh21October2026 capture of the homepage's “Choose Your Own Path” section,rendered at native3×browser pixel density (2280×1230pixels for the displayed crop). It is not an enlarged copy of the old screenshot; no page content was edited or redrawn.

Lead with accessibility: the Hub helps researchers find and explore JUMP data.
Retain the presenter's clarification to Anne in narration: complementary to methods such as
transcriptomics and to experiments already running in the lab. Introduce the
questions rather than a software taxonomy: phenotype, related perturbations,
organelle/feature changes, and cell subpopulations. These are independent entry
points, not mandatory steps. The single-cell notebook comes later and is not a
built-in Hub page. Availability alone is not a detectable phenotype; the current
tutorial separates perturbation-level activity from feature-level significance.

## 9. Tutorials, how-tos and resources — 0:30 (end 7:15)

Present the easiest entry point first: no-code how-to guides for gene/compound queries and Morpheus similarity heatmaps. Then mention curated runnable tutorials for people who want to work with profiles, metadata and statistics. Finish with clearly named further resources: dataset explanations, the protein-localisation companion workflow and the external Cimini Lab Guide to Cell Painting for Biologists.

The six notebook topics remain profiles, metadata, activity, images, clusters and external gene information; no fresh runtime-test claim is made. Their documented environments include Colab, Terra and local Python. The separate MisLocus/VarChAMP companion is not one of those Colab notebooks. These are independent starting points, not a compulsory pipeline.

## 10. Was my gene or compound tested? — 1:00 (end 8:15)

Distinguish availability from requesting a new experiment: find a compound and check whether it was tested; find a gene and check whether knockout or overexpression data exist. Inspect the available profiles, images and metadata. Availability is not evidence of phenotypic activity. The archived screenshot is from2024; use current tools for a new query.

## 11. Which perturbations produce related phenotypes? — 1:15 (end 9:30)

Introduce **MYT1** as the example above the table. Describe **precomputed
comparisons between perturbation profiles**, not exhaustive “every pair” coverage
or experiments combining two perturbations. Explain the ranked candidates
and the documented JSON export link. Preserve scores, comparison context and
identifiers when exporting. The current tutorial documents JSON, not a CSV
button. This is a historical illustration, not a newly executed query or proof
of shared mechanism. Do not present AVPR2 as its next result. The rightmost screenshot column identifies MYT1 as JCP2022_804400, the same CRISPR reagent in the new additional embedding figures. Those figures use another processing method, not a reproduction of this similarity ranking.

## 12. How does cell morphology change? — 1:15 (end 10:45)

The displayed `JCP2022_905491` is **AVPR2 overexpression**, verified against the
pinned ORF metadata. The row highlights **Cells / Correlation_K_Mito / AGP**;
AGP labels actin, Golgi and plasma membrane. Its displayed normalized median
is approximately **−0.213**. The K overlap measurement is intensity-dependent,
not a raw overlap fraction or a negative Pearson correlation.

Make the follow-up concrete: inspect mitochondrial distribution relative to
AGP-labelled structures across images, replicates and controls. Ask whether
mitochondrial redistribution, AGP changes or intensity differences explain the
measurement. Do not turn the normalized median into an unverified claim of
“less physical colocalization”. This is a more concrete, supported example
without adding a new biological result.

## 13. Use JUMP as a screen for your phenotype of interest — 1:15 (end 12:00)

Introduce feature families with biological examples: size/shape, intensity,
texture, channel correlation, and spatial distribution. Use the question
**“Which perturbations change nuclear size?”** to explain a single-feature
screen: select nuclear area, rank perturbations by feature value, separately
check perturbation activity, then inspect images and replicate measurements.

The underlying feature is `Nuclei_AreaShape_Area`. This is a documented query
recipe, not a newly generated hit list. Interactive tables retain ranked
subsets; use full profiles for an exhaustive screen. Keep perturbation-level
activity separate from feature-level tests and account for controls, batches
and multiple testing. Mitochondrial staining intensity is not absolute organelle
abundance; staining, cell size and acquisition context also matter.

## 14. What do the perturbed cells look like? — 1:15 (end 13:15)

Label the **MYT1 and PROZ** gallery examples above the image. Explain fields,
channels and image retrieval. PROZ is not a negative-control label; the figure
is not a matched-control comparison. Appropriate controls must be retrieved
for a new biological comparison.

## 15. Modern tools make image analysis more accessible — 1:00 (end 14:15)

Keep this slide focused on the four tool/task rows. The workflow statement, example prompt and validation sentence now appear alongside the demo screenshot on the next slide (PDF16), at the presenter's explicit request.

Lead with four biological actions; tool names are supporting examples, not
separate topics the audience must learn or steps in a compulsory pipeline:

- **Find cells,nuclei and spots.** Cellpose supplies cell/nucleus masks; Spotiflow detects
  fluorescent spots. Its wrapper's constructed disks are not measured boundaries.
- **Follow cells and organelles over time.** This preserves the author's latest task label. Trackastra / Ultrack link objects through time with
  model-specific segmentation/tracking inputs; not universal organelle tracking.
- **Measure cell and organelle appearance.** cp_measure turns images and masks into profiles.
- **Explore your results.** marimo hosts interactive notebooks/dashboards; the
  notebook supplies the analysis and comparisons, not marimo itself.

For questions only: Parquet stores tables, Zarr stores chunked arrays, and JPEG XL
compresses images. These implementation names have moved off the visible toolbox.
Reactive notebooks help reduce hidden execution state. The post-QR Nahual model
catalogue remains available without narrating every model in the main talk.
The presenter removed the **uv** row and its visible reference. Internal
implementation provenance remains; do not narrate uv as a displayed item.

These tools have addressed recurring problems in the presenter's Python work;
this is not a claim that they solve every dependency or reproducibility problem.
References precede the final QR. Advance to the screenshot before discussing the AI workflow or example prompt.

## 16. Identify and explore cell subpopulations — 3:00 (end 17:15)

The full block sits beside the unchanged demo screenshot: **AI can assemble these tools into workflows.** The exact example prompt and the standard-tools/biological-expertise sentence are retained. Spend the transferred60seconds explaining the connection between the prompt and the implemented notebook, then use the existing120seconds for the demonstration. This is presenter experience, not measured time savings or full autonomy.

Lead with the bridge: **“The tools and documentation we build for researchers
can also be used by AI agents.”** Ask an external assistant to write a notebook
using the documented tools. The researcher defines the biological question
and checks images, measurements and code. This is not a built-in Hub chatbot.
Mention nahual once as a way to add public image-model interfaces; do not imply
that every AI assistant or image model is supported. Introduce the next example
as an implemented marimo notebook.

Make the two experience-based lessons explicit: **biological expertise is
essential for validating results**, and **robust, reproducible tools help agents
use consistent methods across analyses**. The presenter has observed that agents
may solve the same problem in different ways without shared tools. Reusing tested
implementations and recording versions, inputs and parameters supports comparison;
experts still validate the biological interpretation.

Current presenter-authored prompt: “Using the JUMP Hub docs, create a marimo
dashboard to link selected cells to images and measurements.” The removed
record-identifiers sentence is not restored on screen.

**Before the talk:** open `jump-cell-interactivity.mp4` in a local player and pause
at its start. Keep the PDF at **page 16**, visible slide number **15**. Playback
instructions are in these notes only. No notebook server is needed.

The unchanged clip is also public on Zenodo under CC BY 4.0:
<https://doi.org/10.5281/zenodo.23462248>. The snapshot images on pages 16/17 open it. The presenter removed the separate demo-text link from the second still. The final QR
page has no separate recording link.
Use the local file during the talk rather than depending on network playback.

1. Spend about 30 seconds orienting the audience: each dot is a cell; images
   are on the right; summaries follow the selection. There are 2,223 cells.
2. Play the **23.16-second** clip once at normal speed. Narrate select → inspect
   → change channel → reset → select elsewhere.
3. Pause or replay once if useful. Explain linked views rather than dwelling on
   numerical results; do not loop continuously.
4. Return to the PDF and advance to **page 17**.

The first still shows the 545-cell selection and a reproducible sample of six
cells. If playback fails, explain the two stills and move on. The implemented
notebook is `/work/users/amunoz/projects/jump-cell-browser-demo/notebook.py`;
no public notebook-download link is claimed.

## 17. How do cells in another region compare? — 1:15 (end 18:30)

The second still shows **224 cells**. Describe images, areas and summaries;
source IDs allow later inspection. Keep this about exploration and traceability.

- One JUMP Target-2 plate, six wells, twelve fields; no treatment/control assignments.
- Reference: all loaded cells, including the selection, not a vehicle control.
- Selection on measured features changes distributions by construction. UMAP
  separation is not a treatment effect or mechanism.
- The middle 50% is an interquartile range, not a confidence interval. Cells are
  not independent experimental replicates.
- Crops share pixel scale and fixed contrast. White outlines identify selected
  objects; neighbors and some truncation may remain.
- This Zstd Target-2 compression subanalysis is separate from the main JUMP-lite
  release cohort.

## 18. Positive controls contextualize perturbations in both learned and classical representations — 0:30 (end 19:00)

One combined figure uses **567 PLK1 positive-control wells, 10 GJA8 perturbation wells and 5,173 negative controls** (5,750 matched wells; six imaging runs). GJA8 is a selected phenotype example, **not an annotated positive control**. Two PLK1 wells were excluded for known missing MQ chunks. These are replicate wells of the same reagents, not independent guides.

The larger left panel shows genuine **nuclear area and eccentricity**, standardized to plate-negative controls using the discovery-negative robust scale. All wells remain in the full view; a labeled inset magnifies the control/GJA8 region. PLK1 measurements indicate smaller, more eccentric nuclei; GJA8 measurements indicate larger, moderately more eccentric nuclei relative to controls. The selected feature directions also persist in Run 5 (GJA8 has only two wells there). Describe measurements, not a mechanism or diagnosis.

The other six panels are fixed UMAPs of CellProfiler + Harmony, MorphEm, DINOv2, OpenPhenom, **SubCell**, then **ViT-random last**. SubCell still uses clipped-input profiles only; the shorter display label does not change the data. Cell count and standard SubCell are removed from display. Shared UMAP settings: 15 neighbors, min_dist 0.1, Euclidean, spectral initialization, seed 20261020, one thread. No new inference/Harmony fit or separation-driven tuning. The released CP input includes upstream PCA/corrections, but the displayed projection is UMAP.

GJA8 was chosen in the prior discovery-only CP screen; the two named axes were chosen exploratorily from discovery comparisons. PLK1 was originally highlighted post hoc. This is not an unbiased benchmark or independent-guide validation. GJA8 need not form a separate UMAP island. Removing the count panel does not negate the archived finding that counts strongly predict PLK1. Density, viability, well position, batch effects and unaudited pretraining exposure remain limitations. See `figures/two-phenotypes/` for current plotted values and provenance; earlier 125/130-well analyses remain historical.

Pacing:30seconds here and45seconds for the following extraction slide preserve their previous combined75seconds. The plural title describes the role of control wells; GJA8 is still not an annotated positive control.

## 19. Not just JUMP: Extract morphological profiles from your own images — 0:45 (end 19:45)

Explain images + masks → feature tables → profiles using **cp_measure in Python**.
Profiles can contain thousands of features across channels and compartments.
A synthetic schema check at commit `6ffe85e0e7111f4599ec5c884542a69bbbb9dc42`
produced **995 columns for each of three object types**, or **2,985 object-feature
pairs** when combined across nuclei/cells/cytoplasm, with five channels and
Costes disabled. Aggregation/pivoting combines the API's object-type rows;
feature counts depend on configuration. This checks schema, not biological
validity or performance.

The presenter requested **Fast** instead of **Fastest**. The **>2x CellProfiler** comparison is retained from
Overleaf; this revision does not independently validate that comparison.
The historical **28.07× median intensity-kernel speedup**, v0.2.0 versus v0.1.19,
is not evidence for a CellProfiler comparison or a whole-pipeline speedup.
It used synthetic 256/512/1024-pixel images, 16/64/256 objects and one thread.
Its citation is removed from References; the historical evidence remains.

Latest live author wording is “~5x CellProfiler”; it is preserved,not independently re-benchmarked in this editorial pass. Do not interpret it as a universal end-to-end guarantee.

## 20. Applications of JUMP and our tools across biological questions — 1:00 (end 20:45)

The presenter confirmed that probe evaluation and Kenneth's cardiomyocyte work
are one project, and added GSK cross-modality and MisLocus examples. The slide
presents four distinct examples:

- **Lysosomal probes — Kenneth Li, University of Edinburgh / Marc Vendrell group:**
  evaluate lysosomal acidification probes in amiodarone-treated iPSC-derived
  cardiomyocytes, measuring uptake, localization and morphological changes over
  time. Calibration, controls and spectral spillover matter; fluorescence and
  localization alone do not establish pH. Project context is verified from the
  user-identified repository's committed README at
  `0bbf6c86aa51b1cd6c70b5b49485ae06cf875f93`. No unpublished effect size, private
  microscopy figure, internal data URL or efficacy result is shown. The repo's
  user-modified analysis files were not changed.
- **MisLocus protein mislocalisation — Johan Fredin, Carpenter-Shen Lab, Purdue University:** compare microscopy of reference and
  variant proteins in the public VarChAMP collection. The presenter supplied
  the rare-mutation framing. Not every variant mislocalises, and localisation
  changes do not establish clinical pathogenicity. MisLocus contributes
  image-analysis resources and evaluation, not the underlying image acquisition.
  Retain the prior source verification in provenance; do not add unpublished
  figures or new numerical results.
- **GSK cross-modality comparison — Minh Doan, GSK Bioimaging Analytics:** compare compound responses across bright-field
  time courses, Cell Painting, cell-cycle and viability assays. The user-identified
  `broadinstitute/gsk-ia` repository at `cf183a70f25174b9598136219314e7dcc8763e9e`
  implements profile extraction and cross-assay concordance (Jaccard overlap of
  active-compound sets and Spearman correlation of activity rankings). Time-series
  analysis also compares bright-field features with added virtual-staining features.
  Describe the comparison task and workflow, not an unverified outcome or numeric
  performance claim. No private dataset paths, compound identities or results are
  shown, and no analysis was rerun for the slides.
- **Spatial omics with Squidpy — Tim Treis, Theis Lab, Helmholtz-Munich:** the cp_measure paper demonstrates morphology
  featurization of Xenium/H&E breast tissue and comparison with molecularly
  defined cell populations. Cite the existing paper; this is not a built-in Hub
  capability.

## 21. MisLocus: a single-cell image benchmark — 0:30 (end 21:15)

Scale overview added at the presenter's request: **about 3 million cells, 1,541 reference/variant alleles and 282 genes, excluding controls**. The public README reports 3,002,837 biological-cohort cells (250 reference and 1,291 variant alleles); including controls gives 3,332,309 cells and 1,562 alleles across six batches. Only 1,055 variants in 125 genes have a matched reference. These are source-reported counts, not a new manifest census; pinned README evidence accompanies the artwork.

Adapted from slide4 of the supplied `get_slide_3.pptx`, as clarified by the
presenter. JUMP-lite remains after the QR, with its artwork unchanged. The two original
microscopy panels show LZTR1 reference and LZTR1 G248R, respectively; labels are
verified from source XML positions. Their bytes and original aspect ratios are
preserved. No image enhancement or new analysis has been performed.

Use this pair to introduce comparing reference/variant proteins, testing
localisation changes and evaluating image representations. The public VarChAMP
collection underlies MisLocus; this adaptation does not claim new acquisition.
Retain the existing application's Johan Fredin / Carpenter-Shen Lab credit.
At the presenter's request, the displayed Hugging Face link is removed and this slide is attributed as **Unpublished data**, retaining Johan Fredin/Carpenter-Shen Lab/Purdue credit. This describes the on-slide attribution, not a claim that the source data are inaccessible. For internal provenance only, the supplied QR decoded to the dataset URL;
the URL returned HTTP200 when checked. The source's malformed text hyperlink is
not used. No new QR is added to the deck.

Images alone do not establish a reproducible localisation effect or pathogenicity.
Do not infer that this variant causes Noonan syndrome from the illustrated pair.
The clinical photograph, disease framing, personal emails and dense model/workflow
lists are omitted. Independent controls, replicates and biological evidence remain
necessary. This page immediately follows Applications and receives30seconds, split from the existing90-second applications allocation.

## 22. Take-home messages — 1:00 (end 22:15)

Use four complete sentences, as on the slide, preserving the author's21October2026 removal of the final take-home bullet:

- JUMP provides public Cell Painting data for around 136,000 chemical and genetic perturbations.
- Biologists can use JUMP Hub to find tested genes and compounds, compare phenotypes and inspect images.
- Open-source image-analysis tools extend morphological profiling to your own experiments.
- Guides and notebooks help scientists or AI agents build analysis workflows.

The scale uses the same around136,000 modality-specific perturbation counting convention as the JUMP overview; it is not a count of independent profiles or unique genes across modalities. JUMP Hub supports data exploration; image-analysis tools extend the approach to new experiments. AI-generated workflows require verification, recorded inputs/versions and biological expertise. Similarity is a hypothesis-generating observation, not causality.

## 23. Thank you — 0:30 (end 22:45)

The Broad logo is centered over the Carpenter-Singh and Cimini columns together;the Purdue logo is centered over Carpenter-Shen only. Logo pixels,lab names,individual names,the partner sheet and funding wording are unchanged.

Explicitly thank **Anne E. Carpenter and Shantanu Singh (Carpenter-Singh Lab)**,
**Beth Cimini and Paula Llanos together (Cimini Lab)**, and **Runxi Shen
(Carpenter-Shen Lab)**. The presenter requested the Cimini Lab grouping. Runxi's
full name is confirmed on the supplied PowerPoint's title slide. Retain Broad,
Purdue and the JUMP partners. The presenter will explain orally that the lab
moved a couple of months ago; no date or extra relocation claim is put on the
slide. The latest direct author edit extends the visible funding sentence to **cp_measure and JUMP-lite** (preserved as owner-supplied wording, not a new independent verification):
acknowledge **GSK and NIH MIRA
(R35 GM122547)**. The presenter confirmed support from MIRA; the award is to
Anne E. Carpenter, not an individual award to the presenter. The grant and
GSK support are acknowledged in cp_measure, <https://arxiv.org/abs/2507.01163v1>;
the JUMP genetic-map paper explicitly identifies it as NIH MIRA:
<https://doi.org/10.1038/s41592-025-02753-9>, Acknowledgments.
At the presenter's request, the separate Edinburgh collaboration line is removed
from this closing page because Edinburgh is already credited on Kenneth's
application slide. The partner sheet is historical; its headings explicitly
say JUMP, with logos and collaborator names intact.

Show or skip References, then finish on the QR slide. The closing order is
Thank you → References → JUMP Hub and slides, without extending the 23-minute plan.

## 24. References — 0:00 (end 22:45)

Sources, papers and resources are collected here. The JUMP image-count citation
remains here with the other references, not on the dataset overview slide. The cp_measure speed-benchmark
link and the Data formats bullet were removed at the presenter's request.
Small source credits are now displayed below the relevant figures; adapted artwork is explicitly credited as “Adapted from …”. Full provenance remains in
`docs/provenance.md`. Continue to the final QR slide and leave it visible.

The presenter removed the visible uv reference. Internal dependency/provenance notes are retained; no package change is implied.

## 25. JUMP Hub and slides — 0:15 (end 23:00)

Leave this dedicated QR page visible. From left to right: JUMP Hub and Slides
(PDF), with 40-mm codes. The visible Hub shortlink is `broad.io/jump`.
The Slides QR targets GitHub's PDF viewer:
`https://github.com/afermg/2026_10_21_faseb_jump_hub/blob/main/slides.pdf`.

The presentation mirror is **private**, and `slides.pdf` is intentionally absent.
Do not upload the PDF until the presenter explicitly approves the final slides;
do not make the repository public until separately and explicitly instructed.
The audience cannot retrieve the PDF until those release steps are completed.
The two retained QR payloads remain unchanged, as does the private status of
the original Overleaf and authoring projects. JUMP-lite, cp_measure and the
separate recording link were removed from this simplified closing page.

**Stop here for the main talk. The following additional slides are not scheduled narration.**

## 26. JUMP-lite: a compact benchmark — 0:00 (end 23:00)

Adapted from slide 3 of the presenter-supplied `get_slide_3.pptx`, using its
image/profile/evaluation illustrations and the deck's Fira Sans/moloch style.
Explain **images → profiles → evaluation**: compare methods on shared images,
using replicate and known biological relationships to evaluate profiles. This
is the purpose of a benchmark, not a new performance or biological claim.

The simplified nested squares retain **storage-area ratios** for the 115 TB
full release, 8.7 TB selected original images and 92 GB compressed selected
images. They include **both subset selection and compression**, not a
compression-only comparison. Intermediate lossless tiers, Venn counts,
preprocessing graphs, model names, repeated dataset counts and the supplied
slide's 200 TB claim are omitted. Figure/paper: <https://arxiv.org/abs/2608.07632v3>.

The footer isolates the **same-image comparison**: **8.7 TB of original/raw TIFFs**
versus **92.0 GB with medium-quality (MQ) lossy JPEG XL**, approximately **94-fold**
smaller. These are rounded published totals from section 3.1, not new measurements.
Lossy compression changes pixels, so suitability still requires validation for
the intended analysis; no performance-equivalence claim is made. The recorded
Target-2 cohort remains separate. Citation stays on References (page 25) and a discreet figure credit; this
slide stays after QR, outside scheduled narration.

### Historical note: Reality check — slide removed by presenter — consultation only

Use the three approved points: batch effects can resemble biology; similar
profiles do not establish a shared mechanism; experimental follow-up is the
bottleneck. Batch correction helps, but it cannot replace experimental design,
matched controls and independent replication. Prioritized hypotheses still need
targeted experiments and independent readouts in the appropriate context.
Close with: **We can generate hypotheses faster than we can experimentally
validate them.** This is a practical observation, not a measured throughput
comparison. This slide follows QR and JUMP-lite and is not scheduled narration.

## 27. Nahual: swap models within one workflow — 0:00 (end 23:00)

The presenter requested this names-and-swaps overview as an additional slide at
the end, not part of the main narrative. The older detailed Nahual explanation
remains hidden. Swap alternatives **within a task**, not arbitrary task types.
Use the common setup/process interface while respecting model-specific input
preparation, outputs, parameters, licences and validation. This is not a promise
that every model can be substituted without adapting the surrounding analysis.

Nahual connects a Python workflow to model servers in separate environments,
avoiding incompatible dependencies in one environment. The catalogue at
`56aa3fe1c36fe891a933a76d05db6fca2c3673f1` documents DINOv2/DINOv3,
OpenPhenom/MorphEm, Cellpose/StarDist, **Spotiflow** and Trackastra/Ultrack.
Spotiflow is separately labeled **spot detection**, not connected by a swap arrow
to cell-segmentation models. Its wrapper converts detected centroids to configurable
per-spot disks (default radius3pixels); disk area is not a measured physical boundary.
These are wrappers for existing models, not new performance results. Nix deploys
the wrappers; most neural models need GPU resources. Embeddings need not share
dimensions or coordinates. The catalogue was checked, not every runtime/model.

## 28. JUMP-lite: comparing image representations — 0:00 (end 23:00)

Show the published main comparison,Figure5 of arXiv:2608.07632v3. This complements the workflow/storage slide28 rather than repeating it. The question is whether each representation retrieves replicate perturbations and known annotated chemical/gene relationships.

Eleven tasks:four PA replicate-retrieval tasks,two RefChemDB PC shared-target tasks,and five MOTIVE CC/GG/CG tasks. CC is compound-compound,GG gene-gene,and CG compound-gene retrieval. Printed task numbers are absolute NAP or Recall@1%,not a common accuracy metric. Colors normalize within each column; the final All column averages normalized scores. A dark red cell can still have low absolute recall. Results average over normalization configurations.

Keep all published rows and labels. This is a Raw-image comparison; CellProfiler and the cell-count reference use more sites per well than the four-site learned representations. Do not claim controlled CellProfiler superiority or apply this ranking to compressed inputs. Exact middle-model ranks are uncertain; some pretraining overlaps JUMP. Annotation retrieval does not prove mechanism or physical interactions. The paper's inputs differ from the MQ/clipped illustrative control figure20. No new analysis was performed. Caption and exact public-PDF pixel provenance are in `figures/jump-lite-model-comparison/`.

The cell-count row is retained as part of the faithful published figure; it is not reintroduced into the bespoke control comparison20. That slide's “Measured feature axes...” footer was removed,not its underlying data or the methods in these notes.

## Historical provenance: superseded individual model slides

The material below describes the former130-well/PCA slides and is **not the current figure**. All six separate slides and the MYT1 comparator have been superseded by the current paired-perturbation figure above.

The presenter relaxed the MYT1 requirement and requested a visibly separated example. PLK1 already shows a clear positive-control shift in the pretrained-model plots, so it is now the highlighted example. This was chosen **after inspecting the projections**, not prospectively. Every well, coordinate and normalization step remains unchanged: MYT1 is retained as a comparator, and the random-weight baseline's overlap remains visible. This selection is illustrative, not an unbiased benchmark or model ranking. Positive-control shifts can include density/viability effects; do not assert a specific mechanism.

### Former MorphEm panel — consultation only

Original analysis of archived JUMP-lite MQ embeddings, not an adaptation of a published plot. Same130wells and520sites for all six released MQ collections:5MYT1 CRISPR wells (JCP2022_804400),20PLK1 positive-control wells (JCP2022_805264),55no-guide and50non-targeting control wells. One MYT1 reagent at B05 on each of five source_13 plates ending -20; these are replicate wells, not independent guides. This matches the reagent in the historical Hub screenshot, not an ORF experiment.

Each point is one well. Median across all tile records from its four sites, subtract plate-control coordinate medians, scale by pooled plate-centred control SD, then unsupervised full-SVD PCA of the whole fixed cohort. Show all controls; shapes mark plate/run. Arrows are group-average displacement from the control centroid. Explained variance is model-specific; coordinate axes are not comparable between models. The random-weight ViT and clipped-input SubCell variant are explicitly labeled.

MYT1 overlaps controls in these leading2D projections: do not claim clear MYT1 separation, infer absence of a phenotype, or tune projections until it separates. PLK1 provides a strong shift in the pretrained examples and can dominate variance. This selected demonstration is not a model-ranking benchmark. Density, viability, fixed well positions, residual batch variation and model-specific inputs can matter. Pretraining independence was not audited; do not claim out-of-distribution validation. No senescence or mechanistic interpretation is assigned.

All3,120local input hashes are recorded and rechecked. One deterministic public sample per collection is byte-identical to its local input. An independent grouped-median/eigenvalue check agrees with the analysis. None of the520sites intersects the119known missing MQ chunks in the frozen release audit. Full metadata, sample keys, embeddings, coordinates, loadings, scaling, scripts and checks are under `figures/real-embedding-examples/`; data/model links are on each figure. No new inference or biological experiment was performed.

### Former DINOv2 panel — consultation only

Original analysis of archived JUMP-lite MQ embeddings, not an adaptation of a published plot. Same130wells and520sites for all six released MQ collections:5MYT1 CRISPR wells (JCP2022_804400),20PLK1 positive-control wells (JCP2022_805264),55no-guide and50non-targeting control wells. One MYT1 reagent at B05 on each of five source_13 plates ending -20; these are replicate wells, not independent guides. This matches the reagent in the historical Hub screenshot, not an ORF experiment.

Each point is one well. Median across all tile records from its four sites, subtract plate-control coordinate medians, scale by pooled plate-centred control SD, then unsupervised full-SVD PCA of the whole fixed cohort. Show all controls; shapes mark plate/run. Arrows are group-average displacement from the control centroid. Explained variance is model-specific; coordinate axes are not comparable between models. The random-weight ViT and clipped-input SubCell variant are explicitly labeled.

MYT1 overlaps controls in these leading2D projections: do not claim clear MYT1 separation, infer absence of a phenotype, or tune projections until it separates. PLK1 provides a strong shift in the pretrained examples and can dominate variance. This selected demonstration is not a model-ranking benchmark. Density, viability, fixed well positions, residual batch variation and model-specific inputs can matter. Pretraining independence was not audited; do not claim out-of-distribution validation. No senescence or mechanistic interpretation is assigned.

All3,120local input hashes are recorded and rechecked. One deterministic public sample per collection is byte-identical to its local input. An independent grouped-median/eigenvalue check agrees with the analysis. None of the520sites intersects the119known missing MQ chunks in the frozen release audit. Full metadata, sample keys, embeddings, coordinates, loadings, scaling, scripts and checks are under `figures/real-embedding-examples/`; data/model links are on each figure. No new inference or biological experiment was performed.

### Former OpenPhenom panel — consultation only

Original analysis of archived JUMP-lite MQ embeddings, not an adaptation of a published plot. Same130wells and520sites for all six released MQ collections:5MYT1 CRISPR wells (JCP2022_804400),20PLK1 positive-control wells (JCP2022_805264),55no-guide and50non-targeting control wells. One MYT1 reagent at B05 on each of five source_13 plates ending -20; these are replicate wells, not independent guides. This matches the reagent in the historical Hub screenshot, not an ORF experiment.

Each point is one well. Median across all tile records from its four sites, subtract plate-control coordinate medians, scale by pooled plate-centred control SD, then unsupervised full-SVD PCA of the whole fixed cohort. Show all controls; shapes mark plate/run. Arrows are group-average displacement from the control centroid. Explained variance is model-specific; coordinate axes are not comparable between models. The random-weight ViT and clipped-input SubCell variant are explicitly labeled.

MYT1 overlaps controls in these leading2D projections: do not claim clear MYT1 separation, infer absence of a phenotype, or tune projections until it separates. PLK1 provides a strong shift in the pretrained examples and can dominate variance. This selected demonstration is not a model-ranking benchmark. Density, viability, fixed well positions, residual batch variation and model-specific inputs can matter. Pretraining independence was not audited; do not claim out-of-distribution validation. No senescence or mechanistic interpretation is assigned.

All3,120local input hashes are recorded and rechecked. One deterministic public sample per collection is byte-identical to its local input. An independent grouped-median/eigenvalue check agrees with the analysis. None of the520sites intersects the119known missing MQ chunks in the frozen release audit. Full metadata, sample keys, embeddings, coordinates, loadings, scaling, scripts and checks are under `figures/real-embedding-examples/`; data/model links are on each figure. No new inference or biological experiment was performed.

### Former SubCell panel — consultation only

Original analysis of archived JUMP-lite MQ embeddings, not an adaptation of a published plot. Same130wells and520sites for all six released MQ collections:5MYT1 CRISPR wells (JCP2022_804400),20PLK1 positive-control wells (JCP2022_805264),55no-guide and50non-targeting control wells. One MYT1 reagent at B05 on each of five source_13 plates ending -20; these are replicate wells, not independent guides. This matches the reagent in the historical Hub screenshot, not an ORF experiment.

Each point is one well. Median across all tile records from its four sites, subtract plate-control coordinate medians, scale by pooled plate-centred control SD, then unsupervised full-SVD PCA of the whole fixed cohort. Show all controls; shapes mark plate/run. Arrows are group-average displacement from the control centroid. Explained variance is model-specific; coordinate axes are not comparable between models. The random-weight ViT and clipped-input SubCell variant are explicitly labeled.

MYT1 overlaps controls in these leading2D projections: do not claim clear MYT1 separation, infer absence of a phenotype, or tune projections until it separates. PLK1 provides a strong shift in the pretrained examples and can dominate variance. This selected demonstration is not a model-ranking benchmark. Density, viability, fixed well positions, residual batch variation and model-specific inputs can matter. Pretraining independence was not audited; do not claim out-of-distribution validation. No senescence or mechanistic interpretation is assigned.

All3,120local input hashes are recorded and rechecked. One deterministic public sample per collection is byte-identical to its local input. An independent grouped-median/eigenvalue check agrees with the analysis. None of the520sites intersects the119known missing MQ chunks in the frozen release audit. Full metadata, sample keys, embeddings, coordinates, loadings, scaling, scripts and checks are under `figures/real-embedding-examples/`; data/model links are on each figure. No new inference or biological experiment was performed.

### Former ViT-random panel — consultation only

Original analysis of archived JUMP-lite MQ embeddings, not an adaptation of a published plot. Same130wells and520sites for all six released MQ collections:5MYT1 CRISPR wells (JCP2022_804400),20PLK1 positive-control wells (JCP2022_805264),55no-guide and50non-targeting control wells. One MYT1 reagent at B05 on each of five source_13 plates ending -20; these are replicate wells, not independent guides. This matches the reagent in the historical Hub screenshot, not an ORF experiment.

Each point is one well. Median across all tile records from its four sites, subtract plate-control coordinate medians, scale by pooled plate-centred control SD, then unsupervised full-SVD PCA of the whole fixed cohort. Show all controls; shapes mark plate/run. Arrows are group-average displacement from the control centroid. Explained variance is model-specific; coordinate axes are not comparable between models. The random-weight ViT and clipped-input SubCell variant are explicitly labeled.

MYT1 overlaps controls in these leading2D projections: do not claim clear MYT1 separation, infer absence of a phenotype, or tune projections until it separates. PLK1 provides a strong shift in the pretrained examples and can dominate variance. This selected demonstration is not a model-ranking benchmark. Density, viability, fixed well positions, residual batch variation and model-specific inputs can matter. Pretraining independence was not audited; do not claim out-of-distribution validation. No senescence or mechanistic interpretation is assigned.

All3,120local input hashes are recorded and rechecked. One deterministic public sample per collection is byte-identical to its local input. An independent grouped-median/eigenvalue check agrees with the analysis. None of the520sites intersects the119known missing MQ chunks in the frozen release audit. Full metadata, sample keys, embeddings, coordinates, loadings, scaling, scripts and checks are under `figures/real-embedding-examples/`; data/model links are on each figure. No new inference or biological experiment was performed.

### Former clipped-input SubCell panel — consultation only

Original analysis of archived JUMP-lite MQ embeddings, not an adaptation of a published plot. Same130wells and520sites for all six released MQ collections:5MYT1 CRISPR wells (JCP2022_804400),20PLK1 positive-control wells (JCP2022_805264),55no-guide and50non-targeting control wells. One MYT1 reagent at B05 on each of five source_13 plates ending -20; these are replicate wells, not independent guides. This matches the reagent in the historical Hub screenshot, not an ORF experiment.

Each point is one well. Median across all tile records from its four sites, subtract plate-control coordinate medians, scale by pooled plate-centred control SD, then unsupervised full-SVD PCA of the whole fixed cohort. Show all controls; shapes mark plate/run. Arrows are group-average displacement from the control centroid. Explained variance is model-specific; coordinate axes are not comparable between models. The random-weight ViT and clipped-input SubCell variant are explicitly labeled.

MYT1 overlaps controls in these leading2D projections: do not claim clear MYT1 separation, infer absence of a phenotype, or tune projections until it separates. PLK1 provides a strong shift in the pretrained examples and can dominate variance. This selected demonstration is not a model-ranking benchmark. Density, viability, fixed well positions, residual batch variation and model-specific inputs can matter. Pretraining independence was not audited; do not claim out-of-distribution validation. No senescence or mechanistic interpretation is assigned.

All3,120local input hashes are recorded and rechecked. One deterministic public sample per collection is byte-identical to its local input. An independent grouped-median/eigenvalue check agrees with the analysis. None of the520sites intersects the119known missing MQ chunks in the frozen release audit. Full metadata, sample keys, embeddings, coordinates, loadings, scaling, scripts and checks are under `figures/real-embedding-examples/`; data/model links are on each figure. No new inference or biological experiment was performed.
