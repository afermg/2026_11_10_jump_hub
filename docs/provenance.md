# Current restoration update

28pages/25main;word2vec5 and biological representations6 are separate again,using their exact original PDF artwork. Tools15 and prompt-with-demo16 remain separate. Play16,return17,controls18,extraction19,QR25,additional26–28. The merged triptych remains historical,unused. All original artwork and scientific data are unchanged. See `restore-separate-representations-20261020.md`.

The following provenance describes earlier revisions;current page numbers are in `page-map.json`.

# Current open-comment update

27pages/24main;play15,return16,controls17,extraction18,QR24,additional25–27. Only12open Anne threads addressed;resolved threads excluded. See `anne-open-comments-20261020.md` and `figures/anne-open-comments/provenance.json`. Original protected artwork/data unchanged;display derivatives only. No public release.

# Sources for the JUMP Hub conference draft

The current deck focuses on JUMP Hub and practical use of public data. It replaces
the amiodarone starter, which remains intact in Git history at `1bd2f56`.
No confocal measurements, manuscript files or historical deliveries were changed.

## Earlier presentations and posters

The main sequence comes from the Cell Circuits talk and the I2K and Broad Retreat
posters. First, identify a perturbation. Second, compare profiles and features.
Third, inspect images and controls before deciding on a follow-up experiment.
The supporting tools are introduced when an audience member needs a next step.

| Source repository | Pinned revision | Material used |
|---|---|---|
| [2024 Cell Circuits JUMP tools](https://github.com/afermg/2024_05_JUMPTools_CellCircuits) | `141710eed1eee8f7c4c6efcf595dc9f4922858ae` | Org source, PDF text and selected interface screenshots. The question-led sequence is the main narrative source. |
| [2024 JUMP developer tools](https://github.com/afermg/2024_07_JUMP_devtools) | `bf93e79b0940b6adb6edb1dedd4ca3dbca655a19` | Org material and repository tree, consulted for the programmatic access context. |
| [I2K poster and flash talk](https://github.com/afermg/2024_10_i2k_poster_flashtalk) | `bf1db9f818dcc2704bd5ad388c3173a3426f8faf` | Org sources, poster and slide PDF text, rendered poster and the profiling illustration. |
| [2025 nahual talk](https://github.com/afermg/2025_07_10_ST_nahual) | `0a611da4611a605dded0d5c6125b8bd8746361f3` | Org source explaining separate model environments and array transport. Its historical MVP status and HTTP-size claims are not repeated. The downloaded PDF matched its Git blob but could not be parsed. |
| [2025 CODEML cp_measure poster](https://github.com/afermg/2025_07_19_poster_icml_cpmeasure) | `1eef3fd1c3ee643705ef31d74ae4b5f2fbd7069f` | Org poster source explaining image and mask inputs, measurements and applications. No old performance figure was reused as a new validation. |
| [2025 Broad Retreat JUMP Hub poster](https://github.com/afermg/2025_12_broad_retreat_poster_jump_hub) | `31a890665c639747bff49fcadc27827db7371777` | Poster TeX, workflow sections and palette. |
| [2026 JUMP-lite Special Topics](https://github.com/afermg/2026_03_SpecialTopics_JUMP_lite) | `15939f0ff7559a73b2c8edf381bbf3a3e73c143c` | Org source, moloch style and the compact-data rationale. The historical 557-plate working cohort is not presented as the current release. |

The deck retains Org Beamer with two-star frame headings, 16:9 format, moloch
and Fira Sans loaded from TeX Live. The deck uses moloch's default colors without
custom overrides. The poster palette was inspected but is not applied.
No theme source is vendored. Acknowledgement logos are reused at the presenter's
request, as described below.

## Current tool documentation

Historical presentations establish the narrative, not current APIs or release
status. The following documentation was checked separately on 14 October 2026.

| Repository | Pinned revision | Supported statements |
|---|---|---|
| [JUMP Hub](https://github.com/broadinstitute/jump_hub) | `e49a8cd90b68322fe2a74ad910acf676e8abc6de` | Interactive exploration, tutorials and programmatic tools; identifier lookup, similarity, feature and image resources. |
| [JUMP-lite](https://github.com/afermg/JUMP_lite) | `94f19cfe1865ad9a07858908dce0caa679627204` | v1.0 cohort of 551 plates and 655,101 sites; described image variants, embeddings, masks, metadata and original-TIFF links. |
| [cp_measure](https://github.com/afermg/cp_measure) | `1f2ef4dc1fa0bfd81c2b3203b9e31af8d4e2e8c0` | Images and object masks support feature measurements. The current API was checked, but the biology-focused slides contain no code example. |
| [nahual](https://github.com/afermg/nahual) | `56aa3fe1c36fe891a933a76d05db6fca2c3673f1` | Parameters and arrays can pass between isolated model environments and an analysis process; model wrappers have their own input requirements. |

The JUMP-lite README still includes a prospective public-promotion date. An
anonymous HTTP HEAD request to the documented `jump_lite_site_index.parquet`
returned 200 and Content-Length 6,914,554. Only access to that index was checked;
the full image, embedding and mask collections were not downloaded or validated.
A live demonstration must verify the particular objects it intends to use.

The AI-assisted sequence proposes building an interactive notebook around existing
documented tools. Scientists can inspect images, outlines and controls beside the
measurements, then change selections or settings to check the conclusions.
It is not a claim that JUMP Hub includes a chatbot. The historical examples in the
slides remain separate illustrations, not new biological findings. Nahual is
mentioned only as a way to test a broad range of public image models, without
deployment details or a claim that every model is already supported.

A companion marimo notebook was subsequently implemented in
`/work/users/amunoz/projects/jump-cell-browser-demo/`. It links 2,223 existing
JUMP Target-2 cell measurements to a newly computed UMAP, matching cell crops
and descriptive summaries. The separate Target-2 compression subanalysis is not
part of the main JUMP-lite release cohort. The demo uses one plate and only the
Zstd image version, with no treatment or control assignment. Eight unit tests,
original-pixel comparisons, browser selections and a fresh notebook execution
were checked. The notebook's provenance and recorded GIF are in the external
`notebook-demo/` evidence directory. No confocal data are included.

## Introductory definitions

The added Cell Painting slide cites [Bray et al., 2016](https://doi.org/10.1038/nprot.2016.105)
for the six-dye, five-channel assay. The initial explanatory boxes have been
replaced with `figs/cellpainting.png` from the pinned I2K 2024 poster repository,
also referenced by the Broad Retreat poster. This original panel shows five
labelled channels and a merged view. It is reused byte-for-byte, including its
labels and scale bar; its Git blob and SHA-256 are recorded in `docs/assets.json`.
The JUMP slide expands Joint Undertaking for Morphological Profiling in its title and
links the [consortium](https://jump-cellpainting.broadinstitute.org/) and
[dataset documentation](https://github.com/jump-cellpainting/datasets). It separates
the consortium and dataset from JUMP Hub, which provides routes to the resources.

The presenter identified the FASEB meeting through its
[conference summary](https://events.faseb.org/event/organelle-cross-talk/summary),
which names "Organelle Cross-Talk in Cellular Homeostasis". No private confocal
case study or data has been added while collaborator permission is pending.

## Reused figures

[`assets.json`](assets.json) records each source repository, commit, path, source
SHA-256, displayed SHA-256 and any crop coordinates. Downloads were checked
against Git blob hashes before use. Cropping removes unused interface space and
selects a few rows for legibility; it does not change displayed measurements.
The `.jpg` source screenshots contain PNG data, so their displayed files use
`.png` names.

The profiling illustration was initially copied from the I2K poster without
transformation; the later JUMP-specific label adaptation is documented below.
The slides link the image-based profiling review cited in that poster for
background. The interface images are credited to the 2024 talk on the final References
slide, with their archived status and interpretation limits retained in speaker
notes. MYT1, AVPR2 and the MYT1/PROZ gallery are separate illustrations, not a
new continuous analysis. PROZ is not described as a negative control.

The source repositories did not provide a general reuse license for all figures.
The user's requested reuse in their own private draft does not relicense the
illustrations, upstream paper material, fonts or themes. Retain attribution and
check any requirements before distributing a final presentation.

## Paper diagrams, acknowledgements and QR codes

The biology-focused revision uses diagrams instead of code examples:

- cp_measure Figure 1 is extracted from [arXiv:2507.01163v1](https://arxiv.org/abs/2507.01163v1), PDF page 1. It shows images and object outlines becoming measurements.
- JUMP-lite Figure 1b was extracted from [arXiv:2608.07632v3](https://arxiv.org/abs/2608.07632v3), PDF page 2, and cropped to the right-hand storage-size panel. That original crop is retained as historical artwork. The latest presenter-requested PowerPoint adaptation uses three original workflow components and a simplified redrawing of the nested squares on additional page 25. Hashes, crop coordinates and transformations are in `docs/assets.json` and `figures/jump-lite-overview/provenance.json`. The 115 TB full-release square includes selection, not compression alone; the footer isolates the same-cohort 8.7 TB → 92 GB (~94×; lossy JPEG XL) comparison.

Both diagrams were rendered at 300 dpi from the downloaded paper PDFs, without
changing their scientific content. The manifest records source PDF hashes,
versions, page numbers and crop coordinates. Full papers remain outside Git.

The acknowledgement slide uses only the Broad Institute logo and JUMP partner
logo sheet from the 2024 Cell Circuits presentation, with no lab photo. The
presenter supplied the statement that GSK provided part of the funding. No grant
number or further sponsorship claim was added.

The QR slide, immediately before the final References slide, contains exactly
three QR codes, ordered left to right as
JUMP-lite, JUMP Hub and cp_measure. JUMP Hub occupies the centre. The codes were generated locally with error correction M and a
four-module quiet zone. Decoding is checked against the exact destination URLs.
There are no QR codes for nahual or copairs.

## 25-minute prerecorded presentation revision

The presenter requested 25 minutes with a prerecorded demonstration. That initial
revision had 20 PDF pages, with 23 minutes of planned content/playback and two minutes
of buffer; subsequent additions are documented below. Citations and figure credits have moved to one final References slide;
interpretation limits remain in Org comments and `docs/presenter-notes.md`, not
visible footnotes. The title includes the FASEB conference name and the
presenter-confirmed date and affiliation: 21 October 2026, Purdue University.
The Cell Painting/JUMP background now precedes the audience-question slide,
which comes immediately before the Hub overview. The Hub resources are framed
as complementary workflows rather than mandatory sequential steps. JUMP is
expanded in its slide title, and the AI transition explicitly explains that
researcher-facing tools and documentation can also be used by AI agents.
JUMP-lite reference data and cp_measure measurements are positioned as supporting
end-to-end analysis of newly acquired images.

Two new assets show actual recorded selections of 545 and 224 cells. The UMAP
and image-gallery panels are cropped and placed side by side for projection;
points, image pixels, object outlines and labels are not edited. The source
screenshots and exact crop/layout operations are recorded in `docs/assets.json`.
The screenshots are from the same previously validated notebook recording, not
a new biological analysis. The existing 23.16-second GIF is converted to H.264
for offline playback at the same size and duration. See `docs/recorded-demo.md`.
The MP4 is a separate local companion, not embedded PDF media or an Overleaf
asset. Its checksum is recorded with the delivered presentation bundle.

At the presenter's explicit approval, the unchanged MP4 was subsequently
published publicly under **CC BY 4.0** at
<https://doi.org/10.5281/zenodo.23462248>. The record contains only the video and
credits the JUMP data sources; no slide PDF, notebook source or dataset was
uploaded. Anonymous download, DOI resolution, byte count (1,647,131) and SHA-256
`1085f74b56edb0d6006d8f7d83af6a8a74907b4a30693988ce3004383e4599ca`
were verified. Snapshot images and text on PDF pages 13/14 and a text link on
resources page 21 open the public record. Image bytes, four QR destinations,
22-page structure and 23-minute pacing remain unchanged. The PDF-upload and
GitHub-public-release gates remain independent and withheld.

The Purdue University logo is added at the presenter's request alongside Broad,
above the existing consortium partner sheet. The official full-color horizontal
SVG for light backgrounds was downloaded from Purdue's own site and rasterized
at 1600 pixels wide, without recoloring or stretching. The source URL, brand
page and hashes are recorded in `docs/assets.json`. This acknowledgement does
not establish a formal presenter affiliation or change logo usage rights.

## Title, homepage screenshot and direct-edit reconciliation

On 18 October 2026, the presenter confirmed 21 October 2026 and Purdue
University for the title slide and requested a current Hub screenshot. The
homepage was captured at 1600 × 1000 in a clean, isolated Firefox profile, with
no image cropping or content edits. Its URL, capture date and hash are in
`docs/assets.json`; it appears alongside the Hub's complementary workflows.

The presenter instructed that direct Overleaf edits take priority. The four
text changes present in live commit `312fb09` are preserved in the Org source:
the CRISPR and ORF labels, `Researchers can use`, and the edited workflow
heading. The direct wording is retained as supplied, including rough text,
rather than silently reverting to the older generated wording. Publication
uses the documented, owner-approved reconciliation process; no baseline
state is rewritten and no force push is used.

The prerecorded MP4 was copied to the presenter's MacBook Pro as
`/Users/alan/Downloads/jump-hub-demo.mTCyVx/jump-cell-interactivity.mp4`.
The SHA-256 matched the local video, and macOS `open` succeeded.

## Perturbation counts, profiles rationale and review checklist

The presenter subsequently requested the exact title **Uncovering biological
relationships through morphological profiling: The JUMP-Cell Painting dataset
and tools**, perturbation counts, a slide contrasting engineered features and
learned representations, and a review of Anne's comments and the presenter's
replies. That revision added a profiles page; the subsequent applications slide
brought that revision to 22 PDF pages while retaining the 23-minute plan and
two-minute buffer. Playback moves to PDF page 13 (visible number 12), followed
by the second still on PDF page 14.

Counts were computed from the consortium's own
[metadata](https://github.com/jump-cellpainting/datasets/tree/016e865fa0691244e0860943e41c7d6a88ed2580/metadata),
pinned at `016e865fa0691244e0860943e41c7d6a88ed2580`. The files are
`compound.csv.gz`, `crispr.csv.gz`, `orf.csv.gz`, `well.csv.gz`, and
`perturbation_control.csv`. Count unique `Metadata_JCP2022` IDs observed in the
well table, excluding IDs designated `negcon` or `empty` in the canonical control
table, retaining positive-control perturbations. The modality sets are disjoint:
**115,794 compounds + 7,975 CRISPR targets + 15,128 ORF constructs = 138,897**.
The ORF gene/locus count is **12,598** nonmissing supplied identifiers, rounded
to approximately 12,600 on the slide. It excludes blank/NA/nan/None values but
retains supplied XLOC annotations and the eGFP positive-control annotation.
Constructs and genes are not interchangeable. These are full JUMP metadata
counts, not a JUMP-lite cohort count. Definitions and input SHA-256 values are
recorded in [jump-perturbation-counts.json](jump-perturbation-counts.json).

The new profiles slide explains comparison/search at scale and distinguishes
predefined CellProfiler measurements from learned feature vectors. It cites
[Carpenter et al., 2006](https://doi.org/10.1186/gb-2006-7-10-r100) and the existing
image-based profiling review on the final References slide. It makes no new
benchmark or biological-result claim. Normalization, training objectives,
aggregation and interpretation limits remain in notes. No new image asset is
introduced by this revision.

The requested count-card revision retains the biological meaning of the direct
CRISPR/ORF edits and explicitly corrects their typo/capitalization. The other
direct wording remains unchanged. This is a requested revision, not reversion
to an older export.

Project-scoped read-only queries recovered 21 comment threads, 24 messages from
Anne Carpenter and one reply from the presenter. The read-only assessment and
remaining-action checklist are in [anne-review.md](anne-review.md). No database
writes or thread-resolution operations were performed. Raw messages and public
metadata inputs remain in the external `comments-profiles-counts.2KUcLD/` evidence
directory, not in the published slide assets.

## End-to-end applications and Edinburgh collaboration

The presenter requested application examples covering evaluation of new probes
for lysosomal acidification and new integrations with spatial omics through
Squidpy. These are presented as application areas supplied by the presenter,
not as newly validated experimental results or performance claims. No private
microscopy images, unpublished measurements or confocal figures are reused.
The final References slide links [Squidpy documentation](https://squidpy.readthedocs.io/).
Kenneth's example is held pending clarification of the identification task and
project name rather than inventing a biological endpoint.

The presenter also requested a University of Edinburgh acknowledgement similar
to the existing GSK text. The added line reads **“In collaboration with the
University of Edinburgh.”** It does not assert Edinburgh funding, alter the
Purdue affiliation or introduce an unverified logo. The GSK funding statement
and existing logos remain intact.

The 22-page pacing plan shortens the two recorded-demo discussion segments to
2:00 and 1:15, respectively, and allows 1:15 for the applications slide. Total
planned narration/playback remains 23:00 plus two minutes of buffer. The video
itself and its PDF page 13 playback cue are unchanged by this later insertion.

## Implementing Anne's feedback and identifying Kenneth's project

The presenter asked to tackle Anne's comments, provided the repository
`afermg/uoe-kenneth-amiodarone`, and requested that slides avoid defensive
phrasing. The resulting revision has **20 PDF pages**, a **23-minute plan plus
two-minute buffer**, and unchanged playback at PDF page 13 followed by page 14.

The introduction now follows Cell Painting → images/measurements → why profiles
→ JUMP plus the audience question → Hub. Biological questions drive the Hub
sections. Separate example headings identify MYT1, AVPR2 overexpression and the
notebook. A new single-feature screening page explains feature families and
uses nuclear size as a concrete query. The demo is explicitly a marimo notebook;
playback instructions are no longer visible. JUMP-lite emphasizes development
and benchmarking, and cp_measure emphasizes Python profiles from the audience's
own images, with a verified feature-count schema and a cited, version-specific
intensity benchmark. Technical scope remains in notes.

The Cell Painting overview is enlarged and its cell-source label adapted to
“Human U2OS cells”. The partner sheet headings receive JUMP prefixes. Both
transformations are confined to declared label regions, with exact pixel equality
verified elsewhere; original assets remain in Git history and external evidence.
The unchanged original channel panel, other scientific images and QR codes are
preserved. Updated transformations and hashes are in `docs/assets.json`.

Kenneth Li's application is identified from the committed README at
`0bbf6c86aa51b1cd6c70b5b49485ae06cf875f93`: amiodarone-treated iPSC-derived
cardiomyocytes, morphology, probe uptake and time courses. No private data URL,
unpublished effect size or microscopy figure is included. Existing uncommitted
analysis work in that repository is untouched. The spatial-omics example is
supported by the published cp_measure paper's Squidpy/Xenium/H&E application.

One independent-use-case summary replaces two closing content pages, and the
final display combines acknowledgements and the three existing QR codes.
Broad/Purdue/JUMP, GSK funding and Edinburgh collaboration remain represented.
The optional slide-PDF QR awaits an approved stable sharing URL; private project
visibility is unchanged. The presenter requested a subsequent take-home-message
drafting pass; that is intentionally not conflated with the use-case summary.

`docs/anne-review.md` records **20 addressed and one partly addressed** comment
threads. These are content assessments, not Overleaf resolution operations.
`docs/anne-pass-evidence.md` records the checked sources, transformations and
claim boundaries. External evidence and scripts are at
`/work/users/amunoz/datasets/jump_conference_talk_20261014/anne-pass.c0RwJi/`.

## Approved take-home messages

The presenter approved three closing messages: morphological profiles as a
quantitative representation of cell state; JUMP data and query tools accessible
to researchers and AI agents; and ongoing foundations for agent-driven workflows
connecting new microscopy images to quantitative insights, with experts in the
loop to validate biology. Their exact approved wording replaces the intermediate
use-case summary on PDF page 18. This is a conclusion slide rather than a list
of compulsory workflow steps. The independent use cases remain in the preceding
slides. There are no new assets, quantitative claims or changes to the 20-page,
23-minute plan, playback cues, acknowledgements or references. The corresponding
Anne checklist entries now describe the approved ending accurately.

The presenter also supplied the title-slide role/lab line **Research scientist,
Carpenter-Shen Lab**, displayed above **Purdue University**. This is an explicit
presenter-provided affiliation update, not an inference from acknowledgements.
The date, author, talk title and Edinburgh collaborator acknowledgement remain
unchanged.

The presenter clarified that lysosomal-probe evaluation and Kenneth's
cardiomyocyte work are the same project. They are merged into one column on
**“From lysosomal probes to spatial omics”**. The presenter then requested the
cross-modality comparison from `broadinstitute/gsk-ia` as another example.
The resulting three columns are Kenneth's probe project, GSK cross-modality
comparison, and Squidpy/spatial omics. GSK modalities and comparison tasks were
verified in committed sources at `cf183a70f25174b9598136219314e7dcc8763e9e`:
profile extraction across Cell Painting, cell-cycle, viability and bright-field
time-course assays, plus active-compound concordance and activity-rank comparisons.
Only the application and analysis task are described; no private data, compound
identities, unpublished numerical results or new performance claims are shown.
Existing untracked work in that repository was left untouched. The 20-page,
23-minute plan is unchanged.

## AI lessons, accessible image analysis and acknowledgement cleanup

The presenter requested two explicit experience-based lessons: biological
expertise is essential for validating results, and robust, reproducible tools
help agents use consistent methods instead of independently reimplementing the
same problem. These are now explicit on the AI notebook slide and the take-home
slide. The earlier third take-home is split so expert validation stands alone;
reproducible tools form a fifth point. The original core conclusions are retained.

At the presenter's request, the duplicate “In collaboration with the University
of Edinburgh” closing line is removed. Edinburgh remains credited on Kenneth's
application; GSK funding and Broad/Purdue/JUMP acknowledgements are unchanged.

A new modern-toolbox overview follows cp_measure: Cellpose masks; images/masks
into profiles; Trackastra for cells/nuclei and specialised organelle trackers;
generalist/specialised learned features that can be fine-tuned; and Parquet,
Zarr and JPEG XL. Cellpose and Trackastra descriptions were checked against
upstream READMEs; the model-interface examples are supported by nahual's model
catalogue. The notes distinguish Trackastra's documented cell tracking from
organelle tracking, fine-tuning subject to model/licence/data requirements, and
the separate storage roles of tables, arrays and image codecs. The agent claim
is the presenter's experience of reduced integration friction, not a benchmark.
References and figure credits remain on one final page, now in three columns.

The deck now has **21 pages**. The new overview receives one minute, balanced
by shortening pages 4, 10, 12 and 15 by 15 seconds each. The total remains **23
minutes**, with two minutes of buffer. Playback stays on PDF page 13 and returns
to page 14. Applications move to page 18, take-homes to 19, closing to 20 and
references to 21. No microscopy assets or video contents changed.

## Private presentation mirror and deferred PDF release

The presenter requested a repository mirroring the slides, using the date-prefixed
format of existing talks/posters, and explicitly instructed that it stay private
until permission to make it public. The new repository is
`afermg/2026_10_21_faseb_jump_hub`, following repositories such as
`2025_04_09_nix_softeng_retreat` and `2025_07_19_poster_icml_cpmeasure`.
It mirrors the current Overleaf files; the original authoring and Overleaf
projects remain private. No automatic GitHub publication is configured.

A fourth closing QR encodes
`https://github.com/afermg/2026_10_21_faseb_jump_hub/blob/main/slides.pdf`,
which is GitHub's file viewer rather than the raw-download endpoint. The new
`qr-slides.png` uses medium error correction and a four-module quiet zone; its
payload and hash are recorded in `docs/assets.json`. All four closing codes
remain 20 mm wide; the other 17 assets are unchanged. The deck stays at 21 pages
with the same 23-minute plan.

**Release gates:** do not commit/push the PDF before explicit final-slide approval;
do not make the repository public before separate explicit visibility approval.
The QR target file is intentionally absent while editing. A valid QR payload is
not a claim that the PDF is already uploaded or accessible to a public audience.
All 21 reviewer requests are implemented in slide content, but PDF distribution
is deliberately deferred. No review threads have been marked resolved.

## Presenter-directed closing split and gene-only ORF card

The presenter requested separate gratitude and QR slides, superseding the earlier
combined layout suggested in review. Page 20 now contains the acknowledgements
and unchanged GSK funding text; page 21 contains the four unchanged QR destinations,
with displayed codes enlarged from 20 to 30 mm. The partner sheet is displayed
larger, without changing its pixels. References move to page 22. The former
45-second closing segment is divided into 30 seconds of gratitude and 15 seconds
for the QR page, retaining the **23-minute plan plus two minutes of buffer**.
Timing is approximately one minute per slide on average, not a fixed duration
for every slide. The 18 asset files and prerecorded video are unchanged.

The presenter also requested removing the visible **15,128 constructs** from the
ORF card and reporting genes only. It now shows **~12,600 genes**, using the same
verified 12,598 nonmissing supplied gene/locus annotations. The exact construct
count and definitions remain in notes/evidence; the overall 138,897 perturbation-ID
total remains unchanged and is not a sum of gene-level card counts. No recount or
new scientific result is implied. The repository remains private and the PDF
remains unpushed pending the separate explicit release approvals.

## Affiliation and learned-representation wording

The presenter updated the displayed affiliation to exactly **Carpenter-Shen Lab,
Purdue University**, removing the role label and displaying the affiliation as
one line. The learned-representation slide now reads **“Models learn visual
features from training data using neural networks.”** The presenter requested
removing “for example”; this describes the neural representations discussed in
the talk, not a taxonomy of all machine-learning methods. The 22-page deck,
23-minute plan, figures, QR destinations and private/PDF-release gates are unchanged.

The presenter also requested the number of acquiring laboratories and the heading
**“We make JUMP accessible via the JUMP Hub.”** The JUMP overview now states
**12 laboratories**. The authoritative Hub documentation calls these data-generating
centers: `explanations/data_description.md` and `misc/terra_workspace.md` at
`e742f5aa37472eb17f326ba8315d22b27e58f330`. Both files were verified against the
public pinned revision. Counting `Metadata_Source` in the existing pinned well
metadata yields 13 IDs, but the Terra guide identifies `source_7` and `source_13`
as the same center, accounting for the 12-center total. This is not the number
of all consortium/supporting partners, nor a claim that every lab acquired every
modality. A source link is added on the final References slide. The earlier
complementary-to-existing-experiments explanation is retained in speaker notes.

Concurrent direct Overleaf edits at `3fbaee030230d50735552a80e92b61bb9035133d`
shortened Kenneth's visible example to cardiomyocytes and reduced the spatial
omics column to **“Integration of morphological features with Squidpy.”** These
changes were ported into Org before publication, including removal of the second
spatial-omics bullet. The missing preposition in the shortened probe sentence
was repaired to **“Evaluate lysosomal acidification probes in cardiomyocytes.”**
Verified project context remains in notes. The captured upstream diff is retained
outside Git; publication uses normal reconciliation commits, never a force push
or manual baseline rewrite.

## Current workflow artwork and additional-slide order — 2026-10-19

The presenter-edited Mac SVG now supplies the vector PDF on workflow page 3.
Earlier descriptions of a label-only PNG adaptation above refer to the retained
historical raster, not the current reconstruction. The original published
schematic is Chandrasekaran et al. (2021), Figure 1a,
<https://doi.org/10.1038/s41573-020-00117-w>. The heatmap, graph and internal
schematic details are illustrative redrawings, not recovered measurements.
The exact edited SVG, source/export hashes, render warning and acceptance scope
are recorded in [mac-workflow-and-additional-slides-20261019.md](mac-workflow-and-additional-slides-20261019.md)
and `docs/assets.json`. The microscopy montage and other assets are unchanged.

The main talk now closes on QR page 22; Nahual and the vector comparison are
additional pages 23/24. Total 24 pages, planned main narration 23 minutes.
The detailed Nahual slide remains hidden. Earlier page numbers in this
historical provenance log describe their respective revisions.

## Shorter text and word2vec teaching bridge — 2026-10-19

The subsequent user-requested pass reduces extractable text on main content
pages 2–19 by 32.7%, with full explanations retained in speaker notes. An original
word2vec analogy now precedes the renamed cell-vector comparison. The 25-page
PDF has 22 main-talk pages and additional Nahual/word2vec/cell-vector pages 23–25.
The main talk still closes on QR page 22; timing and release holds are unchanged.
The word positions are invented, not trained output; source SVGs, generators,
method citation and limitations are retained. The Mac-edited workflow and all
scientific image bytes are unchanged. See
[text-and-word2vec-20261019.md](text-and-word2vec-20261019.md) for current scope.
Older page counts above describe historical revisions.

## Easy deletions and MIRA acknowledgment — 19 October 2026

The presenter approved four narrow deletions: the redundant workflow caption
(page 3), the JSON-export bullet (8), the gallery instruction (11), and two
explanatory sentences in the word2vec diagram (24). Relevant explanation stays
in speaker notes. Word positions, vector geometry, equation, method citation and
the illustrative/not-trained-output qualifier are unchanged.

At the presenter's request, page 20 now acknowledges **GSK and NIH MIRA
(R35 GM122547)**. The grant to Anne E. Carpenter is recorded in cp_measure's
[Acknowledgements](https://arxiv.org/abs/2507.01163v1); its NIH MIRA designation
is explicit in the JUMP genetic-map paper's
[Acknowledgments](https://doi.org/10.1038/s41592-025-02753-9). The presenter
confirmed support through this grant, not an individual award in their name.
No new funder logo, private correspondence or unpublished material is included.
See [easy-deletions-and-funding-20261019.md](easy-deletions-and-funding-20261019.md).
The 25-page order, 23-minute timing and independent release holds are unchanged.

## Practical access, size comparison and MisLocus, 19 October 2026

The presenter requested an overarching question after the JUMP overview and
before JUMP Hub: "How do better models become tools that experimental biologists
can use?" It contrasts a benchmark question with a biological-use question and
names setup, computing and coding barriers. The notes frame this as the talk's
motivation, not a measured claim about every ML researcher.

The former JUMP-lite slide 16 now shows only Figure 1b's storage-size comparison.
The crop preserves the original panel pixels and labels; composition is omitted.
MisLocus joins the application examples in a two-by-two layout. Its text asks
whether rare mutations change protein location and describes microscopy of
reference and variant proteins. The rare-mutation framing comes from the
presenter. The paired reference/variant design and public VarChAMP source were
checked against `0_abstract.tex` and `3_dataset.tex` at MisLocus manuscript commit
`97758809014a3d647569a4f24732d525f02551a0`. No new figure, numerical result,
diagnostic claim or claim of original image acquisition is added.

The 26-page local preview places the framing on PDF page 6, JUMP-lite on page 18
(displayed slide 17), and applications on page 19. The two direct Overleaf edits
through `29eef3f` are preserved in Org. All 22 other content frames match that
live TeX snapshot after normalizing generated Org labels. Initial validation and
rendered pages are retained under
`/work/scratch/amunoz/jump-lite-slide16-size-only-20261019/`.

After the presenter paused editing and said "ready", the further Overleaf edits
through `49ac92b` were preserved in source commit `c2ba181`. They change the
marimo wording to dashboards, clarify "individual tools", remove emphasis from
the take-home labels and scope the funding acknowledgment to cp_measure and
JUMP-lite. The source was rebuilt and all 22 unaffected content frames still
match the newest live snapshot.

The documented ownership reconciliation and normal fast-forward publisher
completed at 16:16 UTC as Overleaf commit
`e564d550d9fba92af51d3e90b43007b0b6b5985b`.
The exact consumed Org/TeX/assets match the inspected preview, and all 26 rendered
pages match it. Unowned remote files are unchanged. A subsequent sync returned
`no-change`, and the two-minute timer resumed. No PDF input was uploaded, no
GitHub visibility changed, and no manuscript was modified. Publication evidence
is under `/work/scratch/amunoz/jump-lite-slide-publication-20261019T1613Z/`.

## Lab acknowledgements and preserved author edits — 19 October 2026

The presenter requested both Carpenter-Singh Lab and Carpenter-Shen Lab on the
Thank you slide (PDF 20), with the recent lab move explained orally. A single
lab-name line is added below the Broad/Purdue logos. No date is placed on-screen;
current affiliation, partner artwork and the scoped GSK/NIH MIRA sentence remain.

This candidate preserves direct Overleaf changes through
7fce4a2a7d3c0088b2fc825b9c67898b499f1cb8: deletion of the separate demo-text link
and visible uv row, plus updated application headings and collaborator credits.
All other 25 live content frames match after normalizing exporter labels.
The application heading is preserved exactly as authored, including "Evaluat".
Only the lab-name line changes visible content relative to that live snapshot.

The timer was paused after the publisher reported an owned slides.tex conflict.
Preparation used canonical source 70771ce9f73341fdca7ed47e4558bce113a7da99 and
publisher baseline 0a8936336e2b3fda33ec1809c17fc31a1ab440b8. The presenter then
paused editing and said "ready". A fresh fetch confirmed that the reviewed live
snapshot was unchanged. Publication uses the documented normal reconciliation
and existing publisher checks, never a manual ownership-baseline reset.
Evidence: `/work/users/amunoz/datasets/jump_conference_talk_20261014/lab-acknowledgements.rgngdw84/`.
The separate NPC1 public-literature research does not add content to the deck.

## Latest placement update — reality check after QR, 19 October 2026

At the presenter's subsequent request, move the reality check unchanged into
additional material after JUMP-lite. The current order is take-homes 19,
gratitude 20, References 21, QR 22; additional JUMP-lite 23, reality check 24,
Nahual 25, word2vec 26 and cell vectors 27. The deck still has 27 pages, now
22 main and five additional. The image-count citation already appears in the
References source list and remains there; no citation is added to the overview.
The JUMP-lite paper citation also remains on References.

All 26 content frames, their scientific qualifications, figures and links are
unchanged; only their order and speaker-note scheduling change. The main-talk
plan remains 1,380 seconds by reallocating the reality check's 30 seconds to the
existing JUMP overview for the newly added image count and units. Playback
remains PDF 14/15. Preserve all current author wording, unowned main.tex, the
hidden Nahual frame, private visibility and the separate PDF-release gate.

Source baseline: 04285248c299085a4e075863c9cc56daedb73e2e; live baseline:
361356cb0d96181a05f709e54815a00e8e6ae1cf. Isolated evidence is under
`/work/users/amunoz/datasets/jump_conference_talk_20261014/reality-after-qr.1_lqzrib/`.
Earlier page maps below are historical and superseded by this placement update.

## After-QR JUMP-lite, reality check and full-JUMP image count — 19 October 2026

The presenter moved JUMP-lite to the additional slides immediately after QR.
Its authorized size-only version shows 8.7 TB of original TIFFs → 92 GB of lossy
JPEG XL (MQ), approximately 94× smaller, for the same cohort. Rounded values and
fold change come from arXiv:2608.07632v3 section 3.1; 115 TB would additionally
include subset selection. No lossless-quality or performance-equivalence claim
is made. Native typesetting replaces the previously cropped figure.

The approved reality check is inserted immediately before take-homes: batch
effects can resemble biology; similar profiles do not establish a shared
mechanism; experimental follow-up is the bottleneck. Notes retain experimental
design, controls, independent replication and targeted/orthogonal readouts.

The existing JUMP overview now adds **~58.3 million single-channel TIFF images**.
The [public archive count](https://github.com/jump-cellpainting/datasets/blob/016e865fa0691244e0860943e41c7d6a88ed2580/stats/cpg0016_source_images_tiff_count.csv)
sums to **58,267,491**. This is not a cell or five-channel site count. The
published site table totals 8,126,570 and does not reconcile through a factor
of five; its accounting/coverage was not reconciled here, so no derived site
count is displayed. `jump-image-counts.json` records exact URLs, input hashes,
source rows and the reproducible sum. No private manuscript counts are used.

This revision preserves the intervening source/live reconciliation, marimo
"dashboards", "individual tools", plain take-home labels and narrowed funding
scope. It has 27 pages: main 23; additional JUMP-lite/Nahual/word2vec/cell vectors
24–27. Reality check is 19, take-homes 20, gratitude 21, References 22 and QR 23.
Playback remains 14/15. Timing remains 1,380 seconds: JUMP-lite is no longer
narrated, framing/reality check each receive 30 seconds and applications 90.
See [after-qr-and-jump-image-count-20261019.md](after-qr-and-jump-image-count-20261019.md).
All original image/vector bytes remain intact. Publication follows the normal
fresh-fetch/baseline guards; PDF release and public visibility remain deferred.

## Nested-square JUMP-lite graphic — 19 October 2026

The presenter requested the right-hand nested-square artwork instead of the
numeric-only layout and paused Overleaf editing with “ready.” The prepared
revision uses the existing `deck/assets/jump-lite-paper.png` bytes, changes only
the JUMP-lite content frame relative to live, and preserves the direct author
correction **Tim Treis, Theis Lab, Helmholtz-Munich** captured at
`c62888239080e70afd924d9fb6ca0ee9b7fe3ebc`.

JUMP-lite stays on additional page 23, after QR page 22; the reference stays on
page 21. The 27-page deck, 22-page main talk and 1,380-second plan are unchanged.
Selection versus compression and lossy suitability qualifications remain in the
notes; the footer preserves the same-image 8.7 TB → 92 GB comparison. The
source artwork, Mac-edited workflow and demo MP4 are unchanged. No presentation
PDF release or public visibility change is authorized. Preview/publication
receipts are held in the isolated `jump-lite-squares.aymajkz6` evidence workspace.

## PowerPoint slide 3 adaptation and word2vec caption removal — 19 October 2026

The presenter supplied `get_slide_3.pptx` and requested slide 3 adapted to this
deck, with extracted components and less technical detail. SHA-256:
`d9754486403b3f232dea90a62f47965f33d46c52c4790d7551e5267044096cd5`.
Only its JUMP-lite figure (`ppt/media/image14.png`) is used; the source
PowerPoint and unrelated slides are not distributed. Three unchanged pixel
crops illustrate images, profiles and evaluation. A new editable SVG redraws
only the 115 TB / 8.7 TB / 92 GB squares with area proportional to storage.
Intermediate tiers, model names, preprocessing charts, Venn counts and repeated
cohort totals are omitted. The unsupported 200 TB/cell-total wording is not imported.

The user separately requested removal of “Illustrative 2D positions…” from the
word2vec artwork. Only that text element is removed; vector coordinates, labels,
arrows, equation and method citation stay unchanged. The original schematic's
qualification remains in the SVG description, source provenance and speaker notes.

The prepared Org source also preserves the newly fetched direct Overleaf edit
“Evaluate new lysosomal fluorescence probes” from
`ab7bd56e5f626d61013fbee0cf27a3b0ad924630`. Automatic sync was paused to protect
that edit. The presenter subsequently said “ready” and requested explicit names
on the acknowledgements. A fresh fetch captured further wording changes in
`9128e309ff6b793f9b3b90e593016a1718b3ed9c`; all are ported before reconciliation:
morphological-profiling and AI-assistant titles, engineered-feature description,
136,000 headline, heterogeneous-phenotype question, removal of the setup-barriers
sentence and plain marimo label. The gene-level headline tally (136,367) is
separated in notes from the verified construct-level count (138,897), without
changing the pinned inputs. Fresh checks and normal reconciliation remain
mandatory; no baseline reset or forced update is permitted.
Evidence and preview are in the isolated `pptx-slide3.2inq2drq` workspace.
The 27 pages, 22-page main talk, 1,380 seconds, QR payloads, exact Mac workflow,
other artwork, demo and publication/privacy holds are unchanged.

## Explicit named acknowledgements — 19 October 2026

The presenter requested **Anne E. Carpenter, Shantanu Singh, Beth Cimini,
Paula Llanos and Runxi** explicitly on the existing Thank you page (PDF 20).
Runxi is written **Runxi Shen**, as confirmed by the supplied PowerPoint title
slide. The names occupy two lines beneath the retained lab names; the partner
sheet's height cap changes from 0.60 to 0.50 textheight to make room, with its
pixels and aspect ratio unchanged. Both institutions, both labs, all partners
and the scoped GSK/NIH MIRA funding sentence remain. No page or time is added.

## Vector teaching slides around JUMP — 19 October 2026

The presenter requested **word2vec → JUMP overview → From words to cells**.
These are now PDF pages **5, 6 and 7**. No slides were added or dropped: the deck
still has 27 pages, now 24 main-talk pages and three additional pages. Take-homes
are 21, named acknowledgements 22, References 23, QR 24; JUMP-lite/reality/Nahual
follow on 25/26/27. Playback moves to PDF 16 / visible 15, returning to PDF 17.

Both Coordinate axis labels were removed from the word2vec SVG and regenerated
outlined PDF at the presenter's request. The previously removed footer remains
absent; country/capital labels, equation, axes/grid and all vector geometry are
unchanged. Axes remain unlabeled rather than being given unsupported semantic
meanings. The cell-vector diagram and exact Mac workflow are unchanged.

Each vector slide receives 30 seconds of main-talk narration, taken from the
profiles introduction (75 to 45 seconds) and JUMP overview (120 to 90 seconds).
All later cumulative times and the 1,380-second plan remain unchanged. Scientific
qualifications remain in notes, including invented coordinates and the distinction
between word2vec and cell-profile methods.

The renewed “ready” authorizes reconciliation of the latest direct prompt edit
captured at `5cb51ea8bec9a178ec24fc31b483495687771ecf`: “Using the JUMP Hub docs,
create a marimo dashboard to link selected cells to images and measurements.”
The earlier double-period intermediate text and removed record-identifiers
sentence are not restored. All other live frame content is preserved, including
the five names and recent JUMP-lite adaptation. Validation/publication receipts
are in the isolated `vectors-around-jump.a1z8pte0` evidence workspace. Release
and privacy holds remain unchanged.

A final pre-publication guard subsequently detected live author commit
`75382c485209cdafa5f36a72e22d481f1aca8a34` and stopped before canonical writes.
The prepared revision now also preserves “Interpretable but partially redundant”
and the new title “Computational methods improve in benchmarks, how do we ensure
they benefit experimental biologists?”. These are kept verbatim. The presenter
subsequently confirmed “ready” again, and a fresh fetch matched this preserved
snapshot. No source/mirror/delivery update occurred during the earlier aborted
attempt; renewed permission now authorizes guarded publication.

## Mitochondrial granularity and Cimini Lab grouping — 19 October 2026

The presenter requested **mitochondrial granularity** instead of mitochondrial
fragmentation in the engineered-feature example (now PDF6 after the latest author reorder). The vertical-axis label
and example vector use granularity. The companion feature diagram and editable
generator are updated consistently; every coordinate, arrow, cell outline,
legend and learned-embedding element is unchanged. SVG source SHA-256:
`c0200398e0ba9856af7f66d30f1ecfbd7769ab0a789bd102ad93e65539afdc85`;
vector PDF SHA-256:
`95e7851eff7e4d691c8023a933349713b8504813419c14e3a7d16e1837b5142f`.
The existing PDF font-export mode is retained; the learned panel renders
pixel-identically to the prior figure. Outlining was tested but rejected because
it changed the rendering of bold text.

Granularity is an image-signal measurement at specified spatial scales in the
mitochondrial channel. It is not a direct fragmentation, organelle-count or
cristae measurement. The retained network-like/punctate cartoons do not define
the invented values or establish a monotonic relationship with fragmentation.
The measurement is illustrative; no assay or image analysis was performed.

On Thank you (PDF 22), **Beth Cimini and Paula Llanos share the Cimini Lab group**,
as requested. Anne E. Carpenter/Shantanu Singh and Runxi Shen remain under the
Carpenter-Singh and Carpenter-Shen groups, respectively. All five names, logos,
partner-sheet pixels/aspect ratio and scoped funding remain. The three-column
lab layout replaces the previous ungrouped name lines without adding a slide
or changing the partner-image height cap.

Fresh inspection captured direct author commit
`3966bf0b669936801e469908bf90374bf36c1458`: “We precalculated statistical metrics
for every pair.” That wording is ported verbatim; this revision does not newly
validate or extend its scope. All other author edits are preserved. Preparation
and preview evidence are in `granularity-cimini.ngn8l8lz`. The presenter then said
“ready” and clarified the PowerPoint request as slide4, explicitly retaining
JUMP-lite unchanged. A fresh fetch captured `9821c3e86e08cad112f66fe414726ab7cd7b8420`,
which moves cell vectors before JUMP; that order is preserved (word2vec5, cells6,
JUMP7). All later cumulative times remain unchanged. A subsequent author edit
`8101b036f1cef96244a7e661c062a7d94315f6c6` narrows the visible funding sentence to
cp_measure only; that wording is also preserved. The presenter subsequently
confirmed “ready” again; a fresh fetch initially matched this captured snapshot.
A later publication guard detected `5e332723e3c870bd6425ada44f7a50c230ed6407`
and stopped before canonical/config/remote writes. Its revised application question,
“Which rare genetic mutations change protein location?”, is retained verbatim.
The presenter then confirmed that editing was finished and asked to continue.
Fresh final capture `e4159e4d41d3029857dfbd0d0f4c98cef4186cab` removes the two
count-alert wrappers and shortens the image headline to “~58.3 million images”.
That wording is preserved; the single-channel-TIFF definition remains in notes.
The renewed editing pause authorizes the combined guarded publication.

## MisLocus slide4 adaptation and alert removal — 19 October 2026

The presenter clarified that the requested PowerPoint adaptation is **slide4**,
not slide3; the existing JUMP-lite page25 is unchanged. A new additional page28
uses the exact `image17.png` / `image18.png` microscopy panels, with reference
and G248R identity verified from slide XML positions. Original aspect ratios
are preserved. Editable labels and concise comparison/benchmarking aims replace
the dense source layout. No images are enhanced, cropped or reanalysed.

The source's clinical photograph, Noonan-syndrome framing, personal contact
emails, dense workflow/model lists and redundant QR are omitted. The dataset
link is decoded from the source QR, not its malformed text hyperlink, and checked
for HTTP200. Full provenance and a reproducible two-image extractor are under
`figures/mislocus-example/`. The full PowerPoint and unrelated proposal material
are not redistributed. No diagnostic or causal inference is drawn from the pair.

The presenter also requested removing alert highlighting while retaining its
contents. All five Org emphasis spans that generate Beamer alerts are removed:
136,000 perturbations, ~58.3 million single-channel TIFF images, MYT1 example,
AVPR2 overexpression example, and MYT1/PROZ gallery examples. Their text is kept.
Other formatting, including lab-group headings, is retained.

The deck is now28pages:24main and4additional. The1,380-second plan, playback16/17,
QR24 and existing additional pages25–27 remain unchanged. Presentation-PDF release,
public visibility and a Mac transfer remain separately gated.

## Generic word2vec axis labels — 19 October 2026

While the combined publication was prepared, the presenter requested **Feature 1**
on the horizontal axis and **Feature 2** on the vertical axis of word2vec (PDF5).
These generic labels replace the previously removed Coordinate labels without
assigning invented semantic meanings. Only two SVG text nodes are added; vector
geometry, country/capital labels, equation and citation are unchanged. The visible
illustrative-position footer remains absent; scientific qualification remains in
notes and SVG metadata. This request is included in the renewed approved update.

## Tracking restored and Spotiflow added — 19 October 2026

During the approved update, the presenter requested restoring **Trackastra and
Ultrack** to Modern tools (PDF18), and adding **Spotiflow** there and on the
post-QR Nahual slide (PDF27). Tracking names are restored in their own row;
Spotiflow is labeled as fluorescent-spot detection, distinct from Cellpose's
cell/nucleus masks. The Nahual overview retains Cellpose/StarDist swaps and adds
Spotiflow under a separate spot-detection row, not as an interchangeable
cell-boundary model.

The Nahual catalogue at `56aa3fe1c36fe891a933a76d05db6fca2c3673f1` documents all
three wrappers. Spotiflow returns detected centres; the wrapper rasterises
configurable disks (default radius3pixels) into label masks. Those artificial
disks are not measured punctum boundaries. Trackastra links segmented objects;
Ultrack couples candidate segmentations with tracking. No new runtime evaluation,
organelle-tracking generalisation or model-performance claim is made. Page counts
and the23-minute narration plan remain unchanged.

## Biology-first toolbox and bounded comparison wording — 19 October 2026

The presenter requested correcting “every pair” and reducing software overload.
The MYT1 slide (PDF11) now says **Precomputed comparisons between perturbation
profiles.** It does not imply exhaustive coverage or two-perturbation experiments.

Modern tools (PDF18) leads with four actions: **find cells and spots, follow cells
over time, measure cell appearance, explore your results**. Requested Cellpose,
Spotiflow, Trackastra, Ultrack, cp_measure and marimo names remain as smaller
supporting examples. Parquet/Zarr/JPEG XL details move into notes rather than
being deleted from the scientific context. The post-QR Nahual catalogue and all
other application/feature-family material remain unchanged. Spot detection and
cell segmentation remain distinct; the AI/workflow closing sentence is retained.

The presenter separately requested **Fast** instead of **Fastest** on PDF19.
Only that word changes; the >2x CellProfiler comparison remains and has not been
independently validated. The historical intensity-kernel release comparison is
not evidence for that claim.

All other frame content, assets,28pages,24main pages,1380seconds, Cimini Lab grouping,
JUMP-lite25, MisLocus28, playback16/17 and QR24 are preserved. Preview/publication
evidence is under `biology-actions.hkarn4f9`; public-PDF, visibility and Mac-transfer
holds remain unchanged.

## External evidence and scope

Research cache:
`/work/users/amunoz/datasets/jump_conference_talk_20261014/research/`.
It contains repository metadata, pinned file trees, selected downloaded source
files and PDFs, extracted text, and HTTP checks. It is not part of the source
repository. The first draft is retained in `build-v1/`, and the first
biology-focused revision is retained in `biology-deck-v2/`. The centred JUMP Hub
QR layout and logos-only acknowledgement revision are in `biology-deck-v3/`.
The Cell Painting and JUMP definition slides and 18-page validation are in
`biology-deck-v4/`.

The earlier starter's provenance and validation remain available at
[`1bd2f56:docs/provenance.md`](https://github.com/afermg/org-overleaf-sync/blob/1bd2f566f61610c1cb8186559c0d58d6659492d8/docs/provenance.md).
The publication target binding is unchanged. At the presenter's request, the
publisher now includes the exact validated Org source snapshot beside the TeX.
Upstream edits or pre-existing collisions in the Org path stop publication, and
Org-only edits are published even when the rendered TeX is unchanged. Tests use
a fixed four-page synthetic fixture instead of depending on the evolving talk.

## Current follow-up — final JUMP-lite model comparison

The presenter requested an additional final slide showing how JUMP-lite compared representations. Page30 reproduces the complete main-comparison Figure5 from public arXiv v3,not the existing workflow on28. Original embedded RGB/alpha pixels are composited on white without changing values,rows,labels,geometry or color scale. Full figure caption/source hashes are in `figures/jump-lite-model-comparison/`. CellProfiler/count references have more sites per well; this caveat remains visible. The figure is Raw-only and not a new fit or controlled model-superiority result.

Cellpose's visible toolbox label now explicitly includes cells and nuclei. The “Measured feature axes...” footer is removed from the separate control figure20; its numeric inputs,axes and methods are unchanged. The direct-author “Does the model match known biology?” wording and JUMP-list spacing are preserved. Total30pages,27main/3additional,1380scheduled seconds. Main order,QR27,play18/return19 and release holds are unchanged. The unrelated dirty manuscript checkout was read-only and is not the figure source.

## Historical follow-up — control context in the main talk

The presenter moved the existing comparison from29 to20, directly before extraction21, and requested the title **Positive controls contextualize the perturbations**. The display label is now SubCell; its clipped-input data are unchanged. ViT-random is the final panel. The uv environments/dependencies reference is removed. No model refitting, cohort change or new positive-control claim is involved. GJA8 remains a selected phenotype example,not an annotated positive control.

Total29pages now means27main and2additional: Applications22,MisLocus23,thanks25,references26,QR27,JUMP-lite28,Nahual29. Playback18/return19 are unchanged. The pacing plan shares the previous75seconds as30seconds for controls plus45seconds for extraction, preserving1380seconds total. Current figure display checks are in `figures/two-phenotypes/display-validation.json`. All unrelated author edits,protected assets,unowned main.tex and release holds remain unchanged.

## Historical follow-up — paired example on additional page29

Page29 now compares 567 PLK1 positive-control wells,10 GJA8 selected-phenotype wells and5,173 negative controls. A larger nuclear-area/eccentricity panel accompanies six fixed UMAPs: CellProfiler+Harmony,MorphEm,DINOv2,OpenPhenom,ViT-random and clipped SubCell. GJA8 is not an annotated positive control. Standard SubCell and cell count are omitted from display,not from the archived evidence. Full-range feature points and a labeled zoom are shown; overlap in UMAP is retained. Selection is exploratory; no mechanism,model ranking or new independent validation is claimed. Current plotted values,source receipts,normalization,checks and rendering code are in `figures/two-phenotypes/`.

The deck remains29pages,26main and1,380scheduled seconds. Direct author edits to Tutorials10,Applications21 and MisLocus22 are preserved verbatim,including removal of the displayed Johan Fredin/Carpenter-Shen/Purdue caption. MisLocus retains Unpublished data and its small adaptation footer. Private Overleaf publication is authorized; presentation-PDF/public-repository/Mac release holds remain unchanged. See `two-phenotypes-20261020.md`.

## Historical follow-up — superseded 125-well controls figure and attribution

Current deck:29pages,26main plus3additional. Main ordering and tutorial/scale additions remain. Reality check is removed; JUMP-lite27,Nahual28,one combined control figure29. All four visible “Adapted from Muñoz, Cell Circuits(2024)” lines are removed at the presenter's request without altering source images. MisLocus22 displays Unpublished data with Johan Fredin/Carpenter-Shen/Purdue credit and no Hugging Face link. Its pinned public README remains count provenance, not a claim of inaccessible data.

The combined figure has seven panels, matched125wells:20PLK1positive controls and105negative controls(55no-guide,50non-targeting). MYT1 is excluded before fitting/display. Six DL collections reuse validated control-scaled well medians from500MQsites and fixed UMAP(15neighbors,min_dist0.1,Euclidean,spectral initialization,seed20261020). No separation-driven tuning or new inference. The seventh panel uses the released259-dimensional Harmony/PCA/chromosome-arm-corrected CellProfiler representation with new2D PCA, no new Harmony fit or extra scaling. It derives from interpretable measurements, but transformed axes are not individual interpretable features. Same wells do not imply identical site aggregation,encoding or preprocessing. PLK1 selection is post-hoc illustration, not model ranking or independent validation. Current outputs/settings/checks are in comparison-data/; matched CP inputs and pinned recipe are in harmony-input/. Historical130-well/PCA evidence remains unchanged but is not displayed.

## Historical revision —20October2026: tutorials, clearer cells, real MYT1 examples

35pages,26main,23-minute plan. New tutorials10 follows Hub9; tool overview16 precedes AI17; MisLocus22 follows Applications21. Credits added as slide-level text without altering source pixels. Original analysis uses data/model citations, not “Adapted from”. Exact Mac workflow, word2vec, original microscopy, storage artwork, QR payloads and video remain unchanged.

The tutorials overview is grounded in `broadinstitute/jump_hub` at6bbf82c9d1a9e2f0347f3a90a314e6a707975484: howto/notebooks/0_overview.md, interactive/1_jumprr_steps.md and notebooks/17_mislocus_example.md. Public overview/MisLocus URLs returnedHTTP200. Six notebooks cover profiles, metadata, activity, perturbation images, clusters and external gene information. MisLocus is a separate VarChAMP companion workflow, not Colab. The latest steering expands page 10 to explicitly explain resources beyond today's examples: Morpheus similarity heatmaps (`howto/interactive/0_overview.md`), dataset explanations (`explanations/data_description.md`) and the external Cimini Lab Guide to Cell Painting for Biologists linked by `index.md`. The guide is not claimed as newly authored here. All new URLs were checked with certificate verification enabled; `new-link-checks.json` in the revision workspace records the HTTP 200 results.

The cell schematic uses larger smooth cartoons and clearer nuclei/mitochondria, exact Granularity Mito Channel wording and no visible illustrative-positions footer. SVG/source/asset hashes updated; caveats remain in notes. Original embedded-font PDF export is retained; no text-to-path conversion. Teaching coordinates remain invented.

Real-profile figures30–35 use the same130wells/520MQsites for all six released model/input collections. The latest steering relaxed mandatory MYT1 focus and asked for a visibly separated example; PLK1 is now highlighted as a positive control chosen after inspecting the existing projections. No new samples, transforms or coordinates were selected, and MYT1/random-baseline overlap remains. The evaluated selection pool here was MYT1 and PLK1, not an exhaustive target search. This post-hoc illustrative choice is disclosed on each figure and in selection-update.json. Details, recorded inputs, raw well profiles, coordinates, transforms, provenance and independent checks are in `figures/real-embedding-examples/`. MYT1 overlaps controls in leading2D projections; no tuning for separation or model-superiority claim. The historical screenshot shows the same CRISPR reagentJCP2022_804400, not ORF. None of these sites intersects the119known missing-MQ chunks. Public byte identity was sampled once per collection, not exhaustively remote-verified. Pretraining independence was not audited.

Direct author changes through28f4ae2 are ported, including the dual affiliation, Non-redundant wording, revised motivation/Hub questions, cells-and-organelles tracking label, spatial-omics heading and audience-question removal. Preserve these unless the presenter revises them again. Scientific qualifications in notes do not claim embeddings are mathematically non-redundant or every organelle can be tracked by every listed model.

Prepared and validated as an isolated candidate. The presenter then confirmed “ready” for guarded publication after an editing pause. Publication, mirror and delivery receipts record the exact resulting commits and hashes; preview validation alone does not imply publication. The direct-edit conflict uses fresh fetches and guarded normal-commit reconciliation; no force push or baseline reset. Public PDF, repository visibility and new Mac transfer remain separately unauthorized.
