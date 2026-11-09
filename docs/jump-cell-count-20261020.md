# JUMP dataset-scale cell count

At the presenter's request,PDF7 (JUMP: Joint Undertaking for Morphological Profiling) now states **1.8 billion cells**,beside the unchanged approximately58.3million-image count. The cell-count text links to the pinned public inputs:

https://github.com/broadinstitute/jump-profiling-recipe/tree/d2512d978ca17aafead0e99de66386337e6312e4/inputs/cell_counts

Supporting documentation: JUMP Hub,explanations/data_description.md,Dataset scale and cell counts section (verified there on2026-10-20):

| Modality | Cells |
|---|---:|
| Compounds | 1,533,879,336 |
| ORF | 91,186,488 |
| CRISPR | 185,774,701 |
| Total | 1,810,840,525 |

The documentation reports summing Metadata_Count_Cells in the three modality-specific inputs and agreement with all_cell_counts.csv.gz. This slide revision reuses that documented verification;it does not claim a fresh independent recount or new segmentation.

Scope: cells across wells represented in those inputs,including source_7;source_15 has no counts there and is excluded. The three pilot datasets are excluded. These are not image counts,unique perturbations,or necessarily cells retained in a particular filtered profile release. The historical approximately1.6billion estimate was not reconciled by the documentation and is not used here. No largest-dataset claim is made.

The published PDF still ends at QR25. The full Overleaf deck retains28pages. References stays at39links with UMAP intentionally omitted. All other slide content,scientific assets and timings are unchanged.
