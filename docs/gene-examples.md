# OPA1 / DNM1L image examples and AI-assisted interfaces

## Presenter decision

The presenter confirmed a visible OPA1 CRISPR/control difference, reported that the other example looked brighter, requested zoom, and then selected OPA1 and DNM1L as the two examples. This is visual review, not a quantified finding of mitochondrial fragmentation or connectivity. YME1L1 is not an active slide example. Nocodazole and the earlier OPA1-siRNA/rescue sequence are archived rather than deleted from the repository.

## Expected biology versus displayed observations

- OPA1 supports mitochondrial inner-membrane fusion; loss is expected to favor fragmentation. [Griparic et al., JCB 2007](https://doi.org/10.1083/jcb.200704112), [Song et al., JCB 2007](https://doi.org/10.1083/jcb.200704110).
- DNM1L/DRP1 supports mitochondrial division; impaired division is expected to favor elongated/interconnected networks. [Smirnova et al., MBoC 2001](https://doi.org/10.1091/mbc.12.8.2245), [Griparic et al., Fig. 3A/B](https://doi.org/10.1083/jcb.200704112).
- The displayed fields are JUMP CRISPR images, not the siRNA paper's microscopy. Do not apply its 99% fragmentation value to JUMP.
- Brightness alone does not establish connectivity. Mito-channel intensity also depends on staining and acquisition; no new mechanism or phenotype quantification is claimed. Display magnification adds no optical resolution.

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

PDF7: expected biology; PDF8: OPA1 pair; PDF9: DNM1L pair; PDF10: shape versus brightness; PDF11: availability of both genes; PDF12–15 and 17–23: original SLC2A2/MYT1 Hub tutorials; PDF24: agent prompt; PDF25: the two built interfaces. Main talk ends at PDF32; ten extra slides follow. Original tutorial gene labels are preserved and are not presented as results for OPA1 or DNM1L.
