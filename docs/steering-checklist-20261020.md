# Steering-request audit — 20 October 2026

Checked against actual presenter messages, including the follow-ups after “ready”. **Current revision:29pages,26main-talk plus3additional;1,380seconds of narration.** PDF numbers include the title; visible counters are one lower. Exact publication/mirror/delivery status is recorded in transaction receipts and the delivery manifest, not inferred from a preview.

The earlier35-page revision was published as `d8158c46169dee3c234026495b755d54e27240a9`. The following follow-up supersedes its six individual model slides, MYT1 comparator, Reality check slide and specified visible credits. Direct author edits through28f4ae2 remain preserved; fresh-fetch guards still apply.

## Latest follow-ups

| Request | Current implementation |
|---|---|
| Combine all embeddings and controls into one plot | One combined seven-panel figure on PDF29, replacing the six separate slides |
| Include positive and negative controls | Every panel:20PLK1 positive-control wells and105negative controls (55no-guide,50non-targeting), same125wells across five plates |
| Ignore MYT1 comparator | Excluded from both fitting and display; original evidence retained only historically |
| Include Harmony-corrected interpretable features | Seventh panel: released Harmony/PCA/arm-corrected CellProfiler representation, exact same125wells; PCA view labeled separately. Derived from interpretable measurements, not individually interpretable transformed axes |
| Use UMAP for deep-learning embeddings | All six DL panels: shared fixed15neighbors,min_dist0.1,Euclidean,spectral initialization,seed20261020. No tuning after viewing results |
| Remove Reality check | Not exported; additional slides are JUMP-lite27,Nahual28,combined controls29 |
| Remove MisLocus Hugging Face and use unpublished data | PDF22 has **Unpublished data**, retained Johan Fredin/Carpenter-Shen/Purdue credit, no displayed dataset link. Source README remains internal count provenance |
| Remove “Adapted from Muñoz, Cell Circuits (2024)” | Removed from all four affected slides11,12,13,15; underlying image provenance remains |

## Requests from the preceding two hours

| Request | Current implementation / location |
|---|---|
| Correct “every pair” | PDF12: **Precomputed comparisons between perturbation profiles.** |
| Reduce software overload | PDF16: four biological actions, all six tools retained as examples; formats moved to notes |
| Replace Fastest with Fast | PDF20; retained>2×CellProfiler claim remains independently unvalidated |
| Improve cell cartoons | PDF6: clearer boundaries,nuclei/nucleoli,punctate and branched mitochondria; original invented vector geometry retained |
| Rename axis exactly | PDF6: **Granularity Mito Channel** |
| Remove visible “Same cells; illustrative positions, not measured data” | Absent; teaching-schematic caveat retained in notes |
| Genuine MorphEm and every released MQ embedding example at end | Six DL collections on PDF29: MorphEm,DINOv2,OpenPhenom,SubCell,ViT-random,clipped-input SubCell; no new inference or simulated coordinates |
| Do not use NPC1; initially MYT1, later another separated example | PLK1 chosen after inspecting earlier results; MYT1 requirement explicitly superseded, then comparator excluded |
| Discreet figure credits and “Adapted from” for adaptations | Supported credits retained except explicitly removed Cell Circuits lines; original analyses cite data/models |
| Move MisLocus immediately after Applications, in main talk | PDF21 → PDF22, both before QR26 |
| Add MisLocus scale in one sentence | Approximately3million cells,1,541reference/variant alleles,282genes,excluding controls; pinned source evidence retained |
| Modern tools before AI and notebook | PDF16 → PDF17 → PDF18 |
| Tutorials, how-tos and useful resources beyond this talk | PDF10 after Hub9; six runnable notebooks,no-code guides,dataset explanations,protein-localisation and external Cell Painting guidance |
| Preserve latest direct Overleaf changes | Dual affiliation,headings,task labels,funding and audience-question removal retained; later changes guarded by fresh fetch |

## Earlier requests preserved

- Word2vec5 → cells6 → JUMP7; Feature1/Feature2,analogy,equation,citation and original artwork unchanged.
- Mac-edited workflow pixels/vector bytes,MP4,both40-mm QR payloads and `broad.io/jump` unchanged.
- Cellpose,Spotiflow,Trackastra,Ultrack,cp_measure,marimo retained; spot detection is not measured cell-boundary segmentation; tools are complementary,not a compulsory pipeline.
- Five acknowledgements on24: Anne E. Carpenter/Shantanu Singh in Carpenter-Singh; Beth Cimini/Paula Llanos in Cimini; Runxi Shen in Carpenter-Shen. Dual institutional affiliation preserved.
- Funding on24: Work on cp_measure was supported by GSK and NIH MIRA(R35GM122547);awardee Anne E. Carpenter.
- MisLocus uses supplied PowerPointslide4; original LZTR1 microscopy pixels/aspect ratios retained. JUMP-lite artwork remains unchanged on27 with nested squares and qualified compression comparison.
- JUMP headline nearly136,000 and~58.3million single-channel images retained; counting caveats and References25 remain.
- Reality-check slide placement request is superseded by explicit removal; scientific qualifications remain in notes.

## Scientific and release qualifications

All panels match wells, not necessarily identical preprocessing/site aggregation: DL uses500MQsites, while CellProfiler uses released original-well corrected profiles. UMAP axes and distances are not comparable between models. PLK1 selection is post-hoc illustration, not a model-ranking benchmark,mechanistic proof or independent validation. No target/projection search was used to optimize UMAP separation. Original130-well/PCA evidence is historical and excluded from the current figure.

**Still unauthorized:** presentation-PDF upload/push,public repository visibility,and a new Mac transfer. Preserve author edits; use the established publisher,ordinary commits and no force push/manual baseline reset. Verify final live content,private mirror,delivery hashes and no-change sync before restoring automatic synchronization.
