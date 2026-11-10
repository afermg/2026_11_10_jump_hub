# Tutorial images integrated with realistic workflows

The eleven highlighted tutorial images now sit inside the main talk, next to the question each view answers. There is no separate end-of-deck screenshot bank and no duplicate set of figures. `tutorial-walkthrough.tex` defines reusable frame commands; `opa1-literature.tex` calls each once in context. The main talk ends at PDF32; ten existing extra slides follow.

## Workflow 1: follow a gene from the papers to JUMP

OPA1 and DNM1L supply the biological questions, with actual JUMP CRISPR/control images before the workflow. The Hub's original worked examples illustrate the navigation.

| PDF | View | Original figure | What the presenter does |
|---|---|---|---|
| 11 | Workflow overview | OPA1/DNM1L availability reference | Start from a gene in the papers and locate its CRISPR and ORF resources. |
| 12 | Gene availability | Fig. 3 | Search a gene family and read the available datasets/perturbation types. |
| 13 | Column definitions | Fig. 1 | Establish what each field means before interpreting a number. |
| 14 | Filtering | Fig. 4 | Compare exact SLC2A2, SLC2A-family and GLUT2 synonym searches. |
| 15 | Filtered view/export | Fig. 5 | Choose the relevant compartments and save the source, identifiers and filters. |

## Workflow 2: read a phenotype and inspect the images

| PDF | View | Original figure | What the presenter does |
|---|---|---|---|
| 16 | Workflow overview | — | Connect activity, individual features, perturbation types, profile matches and image controls. |
| 17 | Feature-table rows | Fig. 2 | Read perturbation, feature, compartment, channel and statistical summary across a row. |
| 18 | Overall activity | Fig. 6 | Read the corrected perturbation-level p-value for SLC2A2 CRISPR. |
| 19 | Individual features | Fig. 7 | Use feature significance, rank and effect size to describe the changes. |
| 20 | ORF comparison | Fig. 8 | Contrast the overall activity result with individual feature results. |
| 21 | Profile matches | Fig. 9 | Sort by signed similarity and follow annotation/image links. |
| 22 | Perturbation images | Gallery steps 1–3 | Select MYT1 and identify its source and plates. |
| 23 | Image controls | Gallery steps 4–9 | Bring in negative controls from the same source/plates; inspect appearance, density, staining and focus. |
| 24 | Agent handoff | — | Connect cited expectations, traceable image pairs and an interactive viewer. |
| 25 | Vibe-coded interfaces | Actual interface screenshots | Demonstrate the gene/raw-image explorer and phenotype-review viewer. |

The screenshots retain their original highlighted regions, panel labels and pixels. Their titles identify the actual SLC2A2/MYT1 examples, rather than relabeling them as OPA1/DNM1L results. The caption wording is direct and action-oriented. Gray source/history footers and visible verification-date labels are removed; attribution remains in frame comments, this document and the provenance manifest.

## Interpretation details for speaker notes

Availability counts describe gene/reagent coverage, not replication or activity. Feature-table rows are feature–perturbation summaries from published ranked subsets. The overall activity p-value and per-feature significance answer different questions; displayed 0.0 values are rounded. Profile similarity supports biological interpretation alongside annotations and images, rather than independently identifying a molecular mechanism. The original gallery examples use genetic controls (no-guide/non-targeting); compound comparisons use DMSO. These details stay in notes rather than adding defensive slide captions.

## Sources and rights

The [JUMP_rr tutorial](https://broadinstitute.github.io/jump_hub/howto/interactive/1_jumprr_steps.html) was read at JUMP Hub commit `86c0ff7c3420b236ab6c29fe49587bc3ba96fb77`. Broad Institute is credited by all three source records, under **CC BY 4.0**:

- [Main figures](https://zenodo.org/records/15252378).
- [Gene-availability figure](https://zenodo.org/records/16878487).
- [Gallery/control figures](https://zenodo.org/records/16878778).
- [License](https://creativecommons.org/licenses/by/4.0/).

`tutorial-screenshots-provenance.json` preserves the URLs, original filenames, SHA256 hashes, dimensions, retrieval date and source-license metadata. New slide captions do not alter the underlying images. The archived OPA1 literature microscopy (also visible in the phenotype-review screenshot) has its source and CC BY-NC-SA license in `opa1-literature-provenance.json`. Active OPA1/DNM1L JUMP images have exact original TIFF URLs and transformations in `gene-examples-provenance.json`.
