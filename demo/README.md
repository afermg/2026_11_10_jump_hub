# OPA1: literature review and realistic JUMP workflows

**Story:** an extreme nocodazole image example → published OPA1 depletion and rescue evidence → find a gene in JUMP → interpret the returned views → use an agent to navigate sources.

## Stage cues

| PDF | Purpose |
|---|---|
| 7 | Nocodazole opening image pair, preserving the presenter's concise Overleaf edit. |
| 8–11 | OPA1's role in mitochondrial fusion, published control/depletion images, reported fragmentation and rescue evidence. |
| 12 | Workflow 1: take a gene from the papers into JUMP. OPA1 is listed in both CRISPR and ORF coverage. |
| 13–16 | Annotated tutorial screenshots: availability, column definitions, filters and saved views. |
| 17 | Workflow 2: read the returned phenotype and follow it to images. |
| 18–24 | Tutorial screenshots: rows, activity, features, ORF comparison, matches, MYT1 images and matched controls. |
| 25 | Agent handoff: sources, published findings and a linked route through the Hub. |
| 26–32 | Applications, take-home messages, acknowledgements, references and QR. |
| 33–42 | Existing extra slides, including the historical single-cell recording. |

The tutorial images are now embedded in the workflow, not repeated in an appendix. Their titles identify the original SLC2A2/MYT1 examples. The main talk uses direct language; provenance and study details are in [the literature notes](../docs/opa1-literature.md).

## Published sources

- [Griparic et al., JCB (2007)](https://doi.org/10.1083/jcb.200704112): OPA1 depletion, MitoTracker microscopy in HeLa cells, Fig. 3A/G. The paper reports 99% fragmented mitochondria after Opa1 siRNA.
- [Song et al., JCB (2007)](https://doi.org/10.1083/jcb.200704110): selected OPA1 splice forms restore tubular morphology and fusion in OPA1-null mouse fibroblasts, Fig. 1C/D.
- [JUMP gene availability](https://broadinstitute.github.io/jump_hub/reference/00_gene_index.html) and [published coverage reference](https://zenodo.org/records/16883068).
- [JUMP_rr tutorial](https://broadinstitute.github.io/jump_hub/howto/interactive/1_jumprr_steps.html): the highlighted worked examples used in the two workflows.

## Agent walkthrough

Use [prompts.md](prompts.md) to retrieve and summarize literature, locate published examples and link the Hub resources. This review does not require a new dataset analysis, an experiment, a backend deployment or new significance calculations.

If a source cannot be opened during the presentation, use the cited slide and saved source notes. The figures are published examples; no live computation is implied.

## Historical artifacts

Earlier compound-query plans and cached extracts remain available in `nocodazole-reference.md`, `blebbistatin-reference.md`, `blebbistatin-prompts.md`, `rehearsal-nocodazole/` and `rehearsal-blebbistatin/`. The SLC2A2 query extracts are also retained. These are archives, not the active literature-review instructions or OPA1 results.
