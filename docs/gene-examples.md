# OPA1 / DNM1L image examples and AI-assisted interfaces

## Presenter decision

The presenter confirmed a visible OPA1 CRISPR/control difference, reported that the other example looked brighter, requested zoom, and then selected OPA1 and DNM1L as the two examples. This is visual review, not a quantified finding of mitochondrial fragmentation or connectivity. YME1L1 is not an active slide example. Published OPA1 and DNM1L/DRP1 siRNA examples precede the JUMP images. Nocodazole and the earlier OPA1 rescue sequence remain archived.

## Expected biology versus displayed observations

- OPA1 supports mitochondrial inner-membrane fusion; loss is expected to favor fragmentation. [Griparic et al., JCB 2007](https://doi.org/10.1083/jcb.200704112), [Song et al., JCB 2007](https://doi.org/10.1083/jcb.200704110).
- DNM1L/DRP1 supports mitochondrial division; impaired division is expected to favor elongated/interconnected networks. [Smirnova et al., MBoC 2001](https://doi.org/10.1091/mbc.12.8.2245), [Griparic et al., Fig. 3A/B](https://doi.org/10.1083/jcb.200704112).
- PDF8–9 show published siRNA microscopy (Griparic et al., Fig. 3G/A and B/A) before the JUMP CRISPR fields on PDF17–18, with the gene-selection and image/control table operations in between. The paper's panel A is the scrambled Yme1 oligonucleotide comparator, reused as published context for both examples—not a claim of separate matched DRP1-control acquisition. The figures show HeLa cells stained with MitoTracker; gene-targeting siRNA panels are at 2 days. Do not apply the paper's 99% fragmentation value to JUMP.
- Brightness alone does not establish connectivity. Mito-channel intensity also depends on staining and acquisition; no new mechanism or phenotype quantification is claimed. Display magnification adds no optical resolution.

## Published feature summary (PDF22)

The slide shows OPA1 cytoplasmic Mito texture correlation (scale 3, orientation 00, 256 levels), Cohen's d +3.56; DNM1L mito-skeleton branch ends, −5.953; cellular Mito granularity at scale 3, +4.09; and mito-skeleton total length, −3.551. Skeleton rows carry the `Nuclei` object label and `mito_skel` suffix in the source; they are not nuclear shape measures. Do not reinterpret them as a direct measurement of individual mitochondrial length.

Exact decomposed feature names, reagent IDs, all published rows for both genes and input hashes are retained in `demo/gene-feature-summary/`. These summaries describe the CRISPR profiles, not the displayed image crops. They support changes in mitochondrial organization, not direct confirmation of the expected fragmentation/elongation directions. The total skeleton-length feature is included to avoid selectively presenting only apparently supportive measurements. No stable-nucleus baseline was added: OPA1 also has strong nuclear morphology changes. Missing features in this ranked subset are not evidence of stability. Source feature p-values displayed as 0.0 were rounded, not exactly zero; the slide uses effect sizes rather than these rounded values.

## Image provenance and reproducibility

`demo/export_gene_pairs.py` exports two explicitly selected raw-field pairs from the local viewer API. Both use source_13 / 20220914_Run1 / index site 0 / Mito:

| Example | Treatment | Same-plate negative control | Shared raw display limits |
| --- | --- | --- | --- |
| OPA1, JCP2022_804796 | CP-CC9-R1-06, D20 | CP-CC9-R1-06, B02; no-guide JCP2022_800001 | 219–3985 |
| DNM1L, JCP2022_801877 | CP-CC9-R1-02, P18 | CP-CC9-R1-02, B02; no-guide JCP2022_800001 | 187–4463 |

The genes are on different plates. Both controls are the same **type**, not the same image or well. Using one image as the shared control would be incorrect.

Each raw 1280×1080 uint16 TIFF is displayed as an 8-bit grayscale PNG using pooled 0.5–99.5 percentile limits from its treatment/control pair. Values outside these limits are clipped. Limits are identical within a pair but differ across plates; do not compare brightness across the two example slides. Every slide panel is a fixed central 512×512 crop `(384,284,896,796)`, with no search for dramatic cells, additional contrast adjustment or sharpening. Full-field PNGs are retained alongside crops; original TIFF URLs, dimensions, exact well identity, scaling and image hashes are in `gene-examples-provenance.json`. No physical scale bar is invented.

These are the viewer's default first CRISPR fields and documented no-guide controls. They are not asserted to reconstruct the user's exact unlogged browser state. Public JUMP image/source terms remain applicable; no new blanket image license is granted.

## Preserve and demonstrate both interfaces

1. **Gene/raw-image explorer:** `/work/users/amunoz/projects/jump-gene-image-browser`, http://127.0.0.1:8766/ on Oppy and through the existing private Mac forward. Search genes; exact CRISPR/ORF identity; same-source/batch/plate controls; lazy TIFF loading; shared display scaling; fit/1×/2×/4× zoom and independent pan. Source README records start/stop commands and validation.
2. **Phenotype review:** `/work/users/amunoz/projects/phenotype-comparator`, http://127.0.0.1:8765/. Published microscopy and JUMP JPEG previews are explicitly distinguished. Compare candidates, open sources, zoom, record browser-local visibility decisions and export the review. It is not the raw-image explorer.

Both remain separate functioning projects. No service or interface was removed for the slide update. The slide screenshots are from isolated test browsers: `assets/vibe-coded/gene-explorer.png` and `phenotype-review.png`. The latter contains Griparic Fig. 3A/G (CC BY-NC-SA 4.0, attributed in the app and retained source notes). The former shows JUMP raw-field derivatives. Screenshots show actual interfaces, not mockups. Localhost links require the existing private tunnel and are not public audience links.

Suggested demonstration: define a question in plain language, have the agent build a narrowly scoped viewer, inspect the results, request a refinement (the matched zoom), then validate it. AI-assisted development includes testing and scientific checking, not accepting generated output without review.

## Navigation

PDF7: expected biology; PDF8–9: published siRNA examples; PDF10–13: find the genes → OPA1 availability/definitions/filters; PDF14–16: inspect phenotype → OPA1 image/control table operations; PDF17–18: JUMP OPA1/DNM1L image pairs; PDF19–21: OPA1 activity/feature tables; PDF22: OPA1/DNM1L feature summary; PDF23–25: OPA1 ORF/matches/export; PDF26: agent prompt; PDF27: gene/raw-image explorer; PDF28: phenotype comparison viewer. Each interface has its own larger screenshot and slide. Main talk ends at PDF35; ten extra slides follow. Active table panels are generated from published OPA1 rows; the original tutorial PNGs remain archived separately.
