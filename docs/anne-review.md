# Anne's Overleaf review — implemented pass

Source: the private [FASEB slide project](https://overleaf.quasimorphic.com/project/6acfad6134af14083d8c4c89), read through project-scoped MongoDB queries on 18 October 2026: **21 threads, 24 messages from Anne Carpenter and one reply from Alán**. The original export remains outside Git in `comments-profiles-counts.2KUcLD/comments.json`.

The presenter subsequently asked to tackle Anne's comments, identified Kenneth's project as `afermg/uoe-kenneth-amiodarone`, and requested direct slide wording without defensive phrases. This revision implements the comment pass. The previous checklist is preserved in Git history at `72b7403`.

**Status: 20 addressed; the closing-layout request superseded by the presenter's preference.** The presenter now requests separate gratitude and QR slides. The main-talk closing page has two QR codes, for JUMP Hub and the reserved GitHub PDF-viewer URL; additional slides follow. PDF upload and public access are intentionally deferred until the presenter's explicit approvals; the repository remains private and contains no PDF. These are content assessments, not changes to Overleaf's resolved status. No comments were posted, edited, resolved or deleted, and no database writes were performed.

**This revision:**29pages: main1–26, additional27–29. Word2vec/cells/JUMP stay5/6/7. Tutorials10 follows Hub9; Modern tools16 precedes AI17; MisLocus22 follows Applications21. QR26 closes the23-minute main talk, then JUMP-lite27,Nahual28,and one combined seven-panel control figure29. Reality check is removed. DL uses fixed UMAP; Harmony-corrected CellProfiler uses PCA. MYT1 is excluded; PLK1 and negative controls retained. Direct author changes through28f4ae2 are preserved. The historical comment assessment is retained; no comment state is changed. The presenter confirmed “ready”; exact guarded publication status is recorded in the revision receipts and delivery manifest.

## Your reply and how it was used

On the “complementary” thread, you wrote:

> Complementary to whatever their main methods are, e.g., transcriptomics. I rephrased it to be clearer

That reply initially informed **“JUMP Hub complements your existing experiments”**. At your later request, the heading now reads **“We make JUMP accessible via the JUMP Hub”**. Speaker notes retain the complementary positioning and explicitly mention transcriptomics. Workflow entry points remain independent rather than compulsory stages.

## Comment-by-comment outcome

| # | Anne's request | Assessment | Applied change / evidence |
|---|---|---|---|
| 1 | Use biological perturbation names. | **Addressed** | CRISPR knockout and gene overexpression (ORF) remain explicit on the count cards. The unsupported transient label is removed; notes describe lentiviral delivery and the 48-hour readout. |
| 2 | Show perturbation counts. | **Addressed** | Shows 7,975 CRISPR targets, ~12,600 ORF genes, and 115,794 compounds. At the presenter's request, the construct count is removed from the visible ORF card; exact construct/gene definitions remain in notes and evidence. |
| 3 | Replace the diagram's cell-source label with Human U2OS cells; enlarge it. | **Addressed** | Changed only that label and enlarged the diagram from 0.82 to 0.99 text width. Pixel equality outside the label region was verified. |
| 4 | Put images-to-measurements immediately after Cell Painting; merge the audience-question page with JUMP. | **Addressed** | Intro is Cell Painting → images/measurements → why profiles → word2vec → cell vectors → JUMP → accessibility/Hub. The presenter subsequently removed the audience-question bullet directly in Overleaf; that newer preference supersedes retaining it. |
| 5 | Clarify “complementary to what”. | **Addressed** | Clarified the complementary positioning using your reply, including transcriptomics. Your later accessibility-focused heading replaces the earlier title; the explanation remains in speaker notes. |
| 6 | Use biological questions in the overview and workflow titles. | **Addressed** | Titles now ask about tested perturbations, related phenotypes, cellular changes, nuclear size and image appearance. Notes distinguish availability, perturbation-level activity and feature-level significance. |
| 7 | Replace awkward wording about retaining similarity details with export wording. | **Addressed** | JSON export is documented in the current JUMP_rr tutorial and retained in speaker notes. The presenter subsequently requested deleting the on-screen export bullet to reduce text. No CSV button is promised. |
| 8 | Put MYT1 and subsequent examples above their tables/images. | **Addressed** | Separate example labels identify MYT1, AVPR2 overexpression, MYT1/PROZ and the notebook selections. |
| 9 | Make feature interpretation and the follow-up question concrete. | **Addressed** | Verified AVPR2 as ORF overexpression. Highlighted the mitochondria–AGP K overlap measurement and a concrete image-inspection follow-up. The suggested “less overlap” direction is not asserted: the screenshot contains a normalized, intensity-dependent coefficient, not a direct spatial-overlap result. |
| 10 | Make clear that an external AI writes exploration code. | **Addressed** | The presenter now titles this “We can leverage the curated documentation to build AI assistants”; the prompt and researcher-tools/AI-agents bridge remain explicit. The notes identify this as an external assistant, not a Hub chatbot. |
| 11 | Remove the on-slide playback instruction. | **Addressed** | Playback instructions now appear only in notes/operational documentation. |
| 12 | Explain where the cell-browser capability comes from and frame it as a biological question. | **Addressed** | “Identify and explore cell subpopulations” with an explicit “Interactive marimo notebook built from JUMP images and measurements” label. Notes identify the implemented notebook source. |
| 13 | Emphasize JUMP-lite's benchmarking/method-development role. | **Addressed** | The latest presenter-requested PowerPoint adaptation restores explicit benchmarking context: images → profiles → evaluation, alongside simplified nested storage squares. The footer compares 8.7 TB original TIFFs → 92 GB lossy JPEG XL for the same cohort. |
| 14 | Add paper/preprint references. | **Addressed** | Tool-paper links remain on References, immediately before the final QR slide. Illustration/logo provenance remains in the evidence documents; the speed-benchmark citation is removed at the presenter's request. |
| 15 | Use “your own” instead of “newly acquired”. | **Addressed** | cp_measure retains audience-facing “your own images” wording. JUMP-lite now uses the presenter's simplified PowerPoint adaptation for benchmarking and dataset size. |
| 16 | Emphasize profiles, thousands of features, Python and time savings. | **Addressed** | cp_measure focuses on profiles/Python. A synthetic schema check supports thousands of object-feature combinations across channels/compartments. The historical 28× intensity benchmark citation is removed. The presenter changed Fastest to Fast. The >2x CellProfiler comparison remains, not independently validated; the historical benchmark does not substantiate that comparison. |
| 17 | Make the tool-selection content an ending summary. | **Addressed** | Consolidated the two prior closing pages into one take-home slide. It now contains five conclusions, including the two subsequently requested AI lessons. |
| 18 | Avoid implying everyone must follow all three steps. | **Addressed** | The closing states conclusions, not tasks everyone must complete. Independent phenotype, related-profile, subpopulation, single-feature and own-image use cases remain throughout the deck. |
| 19 | Add a single-feature screen and explain feature families. | **Addressed** | New “Use JUMP as a screen for your phenotype” page pairs nuclear-size screening with size/shape, intensity, texture, correlation and distribution examples. It is a query recipe, not an invented hit list. |
| 20 | Add JUMP to partnership headings. | **Addressed** | Figure headings now say JUMP partners, JUMP supporting partners and JUMP collaborators. Logos and collaborator entries below the heading band are unchanged. |
| 21 | Combine acknowledgements/QR codes; consider a slide-PDF QR. | **Layout superseded by presenter; QR implemented** | After the combined version, the presenter requested separate gratitude and QR slides. Broad/Purdue/JUMP and the author's latest funding sentence for cp_measure are on page24; References25 is followed by the two retained40-mm QR codes on main-talk closing page26. Additional JUMP-lite27,Nahual28 and combined controls29 follow the QR. MisLocus is main page22, labeled unpublished data with its Hugging Face link removed. Six DL UMAP panels and Harmony-CellProfiler PCA share only PLK1/negative-control wells; Reality check is removed. Word2vec/cell vectors are main-talk pages5/6. The repository stays private and the PDF unpushed pending explicit approvals. Edinburgh remains credited on Kenneth's application. No private project was made public. |

## Additional requested changes

- Acknowledgements on PDF24 explicitly name Anne E. Carpenter and Shantanu Singh (Carpenter-Singh Lab), Beth Cimini and Paula Llanos together (Cimini Lab), and Runxi Shen (Carpenter-Shen Lab), retaining all five names. The presenter will explain the recent move orally; no date is added on-screen. The latest author edit scopes GSK/NIH MIRA funding to cp_measure.
- Preserve the latest direct application credits for Kenneth Li/Vendrell Lab, Johan Fredin/Carpenter-Shen Lab, Minh Doan/GSK Bioimaging Analytics and Tim Treis/Theis Lab (latest direct Overleaf correction). The author also removed the separate demo-text link; both snapshot-image links remain.

- The presenter confirmed that lysosomal-probe evaluation and Kenneth's work are the same project. They are merged into one example on **“Applications across biological questions”**: **Kenneth Li, University of Edinburgh; lysosomal acidification probes in amiodarone-treated iPSC-derived cardiomyocytes**, with uptake, localization and morphology measured over time. No private data URL, unpublished effect size or microscopy figure is exposed.
- Added GSK's cross-modality comparison as a separate example: compare compound responses across bright-field, Cell Painting, cell-cycle and viability readouts. Modalities and the comparison workflow were verified in the user-identified `broadinstitute/gsk-ia` repository; no new biological result is claimed.
- Squidpy/spatial omics remains a separate third example, supported by the published cp_measure paper. Later direct Overleaf edits shorten it to integration of morphological features with Squidpy and shorten Kenneth's visible description to cardiomyocytes; both edits are preserved, with the verified scientific context retained in notes.
- MisLocus adds a fourth application: reference-versus-variant protein localisation, with no new unpublished figures/results or clinical-pathogenicity claim.
- Slides use direct, positive descriptions. Interpretation limits and historical/benchmark details remain in speaker notes. The approved reality check, now additional PDF28, makes batch effects, mechanism limits and the experimental-follow-up bottleneck visible.
- The take-home messages on PDF page23 retain the approved core and two AI lessons, with the author's latest plain labels preserved.
- Modern tools (PDF16) now leads with four biological actions: find cells/spots, follow them over time, measure appearance, explore results. Cellpose/Spotiflow, Trackastra/Ultrack, cp_measure and marimo are retained as smaller supporting names. Storage-format details move to notes; uv stays off-screen and its References link remains. Nahual stays on additional page29.
- MYT1 (PDF12) now says “Precomputed comparisons between perturbation profiles”, removing the unqualified every-pair claim and avoiding confusion with combinatorial perturbation experiments.
- The latest author-edited order is word2vec (main page5), cell vectors (6), JUMP (7). Both are illustrative, not trained-model results. The visible word2vec caption and Coordinate labels remain removed; the latest request adds generic Feature 1 / Feature 2 axis labels. Qualifications remain in notes.
- The earlier text-pass statistics describe their historical versions. Qualifications remain in notes, and the easy deletions remain in place. The newly authorized JUMP-lite adaptation, word2vec-caption removal and five named acknowledgements are included, alongside all preserved direct Overleaf wording edits.
- The main workflow figure on page 3 now uses the presenter's Mac-edited vector reconstruction rather than the lower-resolution PNG.
- Deck: **26main-talk pages plus3additional slides**, **23-minute plan plus2minutes of buffer**. Tutorials10 takes30seconds from Hub; MisLocus22 takes30seconds from Applications. Original JUMP-lite artwork remains after QR26, on27, with a new discreet credit. Nahual follows28, then one combined control figure29; Reality check and the MYT1 comparator are removed. The cell cartoon is clearer, its axis is Granularity Mito Channel and its requested visible footer is removed; qualifications remain in notes. Adapted figures have small credits except the explicitly removed Cell Circuits lines; original data plots cite data/models. MisLocus is attributed as unpublished data. Playback is PDF18 / visible17; return PDF19. No new PDF release or Mac transfer is authorized.

## What remains

1. **Deferred release:** explicitly approve the final PDF upload and, separately, making `afermg/2026_10_21_faseb_jump_hub` public. The PDF QR is prepared; its target file is intentionally absent. Original Overleaf/authoring projects remain private.
2. Rehearse the 23-minute plan and the offline video transition on the presentation setup. The take-home-message drafting step is complete.

## Thread identifiers

1. `6ad12311e6433d2e66000001`
2. `6ad1249bafd8a83970000001`
3. `6ad1251c4884c37da7000001`
4. `6ad1261a30f1e90a67000001`
5. `6ad16d1f7a72ac29d1000001`
6. `6ad16deb9d3fd85ebb000001`
7. `6ad16e1d601a643135000001`
8. `6ad16e826bf58f0484000001`
9. `6ad16f349b55204cb4000001`
10. `6ad16faa550deb0702000001`
11. `6ad16fd48d7b906464000001`
12. `6ad170050ee2cc244e000001`
13. `6ad17070d202712c3c000001`
14. `6ad1709e6c30aa0d2e000001`
15. `6ad170b31e66681043000001`
16. `6ad1712dae46733f15000001`
17. `6ad17156fb615444af000001`
18. `6ad171c090ecd123a0000001`
19. `6ad172449d07923eb3000001`
20. `6ad17277e711c23c44000001`
21. `6ad172dd6316136829000001`
