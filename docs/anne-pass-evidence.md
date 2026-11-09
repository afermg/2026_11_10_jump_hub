# Evidence for the Anne-comment revision

Checked 18 October 2026. External working evidence is retained at
`/work/users/amunoz/datasets/jump_conference_talk_20261014/anne-pass.c0RwJi/`.
This is a presentation revision, not a new biological analysis. Other projects'
working files were read only; no raw microscopy data were processed or published.

## Sources and supported statements

| Topic | Pinned source | Supported use |
|---|---|---|
| Hub questions and export | `broadinstitute/jump_hub` at `e742f5aa37472eb17f326ba8315d22b27e58f330`, `howto/interactive/1_jumprr_steps.md` | Availability/activity/features are distinct; filter tables, inspect images, export filtered data through the JSON link. CSV is not promised. |
| Feature interpretation | `broadinstitute/monorepo` at `704c365e621e456e9b5ad8d43f72dfb5c5fad4d0`, `libs/jump_rr/src/jump_rr/metadata.py` and `calculate_features.py` | Feature values are normalized; the displayed median aggregates replicates. K is not interpreted as a raw spatial-overlap fraction. |
| AVPR2 identity | `jump-cellpainting/datasets` at `016e865fa0691244e0860943e41c7d6a88ed2580`, `metadata/orf.csv.gz` | `JCP2022_905491` maps to AVPR2, NCBI Gene ID 554, in the ORF table. The screenshot is therefore an overexpression example. |
| AVPR2 example | Existing `hub-features.png`, sourced from the pinned 2024 Cell Circuits talk | Cells / Correlation_K_Mito / AGP, displayed normalized median −0.21309228714749423. A concrete follow-up inspects mitochondrial patterns relative to AGP staining; no new directional colocalization claim is made. |
| cp_measure Python/features | `afermg/cp_measure` at `6ffe85e0e7111f4599ec5c884542a69bbbb9dc42`, README and featurizer | Python images/masks → feature matrices. Synthetic schema check: 995 columns/object × three object types = 2,985 object-feature pairs for a combined profile. |
| cp_measure speed | Same revision, `benchmarks/releases/v0.2.0.md` | Median **28.07× intensity-kernel speedup**, v0.2.0 vs v0.1.19. This is the published release benchmark, not a newly measured whole-pipeline or CellProfiler comparison. |
| Kenneth's application | User-identified `afermg/uoe-kenneth-amiodarone` at `0bbf6c86aa51b1cd6c70b5b49485ae06cf875f93`, committed README | Kenneth Li / Marc Vendrell group, University of Edinburgh; amiodarone-treated iPSC-derived cardiomyocytes; morphological profiling, probe uptake/localization and time courses. No unpublished result is claimed. |
| Spatial omics | Muñoz et al., [cp_measure preprint v1](https://arxiv.org/abs/2507.01163v1), section 2.2.2 and appendix | cp_measure-based morphology featurization integrated with Squidpy/SpatialData, demonstrated with Xenium/H&E tissue and comparisons to molecularly defined cell populations. |

The old AVPR2 screenshot is preserved unchanged. Its normalized K measurement
does not by itself establish “less overlap” in physical localization. The slide
uses the supported concrete measurement and an actionable image-inspection
question instead of that suggested, unverified interpretation. Technical scope
is retained in speaker notes rather than defensive visible wording.

## Subsequent application clarification and GSK example

The presenter confirmed that lysosomal-probe evaluation and Kenneth's
cardiomyocyte analysis are one project; their columns are merged. The presenter
also requested a cross-modality comparison from `broadinstitute/gsk-ia`.

The local checkout is pinned at `cf183a70f25174b9598136219314e7dcc8763e9e`.
The relevant tracked files matched that commit and were inspected without
executing the notebooks or modifying the repository:

- `README.md`: dataset modalities and naming conventions. Its older checklist
  still lists modality integration as unfinished, so it alone is not evidence
  for a completed integration result.
- `notebooks/nb01_extract_profiles.py`: extraction for Cell Painting, cell cycle,
  viability, bright-field time courses and virtual-staining variants.
- `notebooks/nb11_assay_concordance.py`: cross-batch/assay scoring, Jaccard overlap
  of active-compound sets and Spearman correlation of compound activity rankings.
- `notebooks/nb15_timeseries_featurization.py`: bright-field versus bright-field
  plus virtual-staining feature comparisons.

The slide describes comparing compound responses across these modalities. It
asserts neither a concordance result nor a measured benefit of one modality over
another. No raw data, private paths, compound identities or numerical findings
are included. Existing untracked files were left untouched.

## Modern toolbox and AI lessons

The requested compact overview is supported by the upstream Cellpose and
Trackastra READMEs, retrieved on 18 October 2026, and the nahual model catalogue:

- [Cellpose](https://github.com/MouseLand/cellpose): cell and nucleus segmentation;
  its documentation also describes adaptation/fine-tuning to labelled data.
- [Trackastra](https://github.com/weigertlab/trackastra): association/linking of
  already segmented cells in time-lapse images, with nucleus and bacteria
  examples. It is not cited as validation for arbitrary organelles.
- [nahual](https://github.com/afermg/nahual): interfaces to generalist encoders
  (DINO) and specialised microscopy encoders (e.g. scDINO). The slide does not
  claim every wrapper exposes training or that every model licence permits
  fine-tuning; these requirements are explicit in notes.
- [Parquet](https://parquet.apache.org/), [Zarr](https://zarr.dev/) and
  [JPEG XL](https://jpeg.org/jpegxl/) serve tabular, array and image-compression
  roles respectively; no unverified size/speed comparison is asserted.

The observations about agents reducing integration friction and independently
choosing different solutions come from the presenter, not a controlled study.
Slides state positive design principles: biological expertise for validation,
and robust, reproducible tools for consistent methods. No analysis was rerun.

## cp_measure schema check

Executable script: `anne-pass.c0RwJi/check_feature_count.py`.
Results: `anne-pass.c0RwJi/cp-measure-feature-count.json` and the source copy
`docs/cp-measure-feature-count.json`.

- Fixed random seed 42; synthetic five-channel 48×48 image.
- Three object types: nuclei, cells and cytoplasm; one synthetic label each.
- Default feature families with Costes disabled.
- API output: three object-type rows × 995 feature columns. Combining the
  object types into a well/cell profile by aggregation/pivoting gives 2,985
  distinct object-feature combinations; the API does not directly return a
  2,985-column matrix for each row.
- Counts depend on channels, compartments and configuration. This is not a
  biological fidelity check or speed benchmark.
- The existing Python environment initially lacked the Nix C++ shared-library
  path; rerunning with a process-local `LD_LIBRARY_PATH` succeeded. No environment
  dependencies or source files in cp_measure were changed.

The speed slide separately cites the release report: synthetic image dimensions
256/512/1024, object counts 16/64/256, matched dependency versions, single thread,
three seeds/repetitions. The slide names the intensity benchmark and both versions;
the detailed scope remains in notes.

## Figure adaptations

The generation script is `anne-pass.c0RwJi/adapt_figures.py`. Original PNGs are
preserved in `anne-pass.c0RwJi/original-assets/`, upstream source repositories,
and source history at `72b7403`. Updated hashes are in `docs/assets.json`.

- **Cell Painting overview:** only pixel box `[0,218,112,268]` changes, replacing
  the generic patient-cell-line label with “Human U2OS cells”. The diagram is
  explicitly an adaptation for JUMP. Its slide width increases from 0.82 to
  0.99 text width, with one concise explanatory bullet.
- **JUMP partner sheet:** only header band `[0,0,1581,60]` changes. Headings become
  “JUMP partners”, “JUMP supporting partners” and “JUMP collaborators”. The first
  colored logo pixels start below the band; every logo and collaborator entry
  outside the band is unchanged. The roster remains historical.
- For both images, exact RGBA equality outside the declared region is asserted
  by the generation script. Other 15 assets, including all QR images and the
  original Cell Painting channel panel, are untouched.

## Scope and remaining decision

All 21 review threads are accounted for in `docs/anne-review.md`; no thread was
resolved or modified. The combined closing contains the existing three QR codes
in JUMP-lite / JUMP Hub / cp_measure order, alongside acknowledgements.
All three QR codes were decoded successfully from the rendered 1400×788 closing
slide and matched their exact expected URLs (`closing-qr-validation.json`).
The final build has no overfull/underfull boxes or compiler warnings. Page counts,
all pacing totals, playback cues, all asset hashes and all 21 thread IDs were
checked against source/evidence.

A fourth slide-PDF QR still requires a stable, presenter-approved sharing URL.
No source/project visibility settings were changed.
