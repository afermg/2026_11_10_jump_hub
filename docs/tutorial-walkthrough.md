# Question → JUMP_rr action → example

The main sequence now interleaves the biological question with the corresponding table operation and example, rather than presenting the results first and placing all instructions in a separate walkthrough. `tutorial-walkthrough.tex` defines the eleven reusable screenshot frames; `opa1-literature.tex` calls each exactly once in context. The deck remains 45 pages, with the main talk ending at PDF35 and ten existing extra slides following.

## Find the perturbations

| PDF | What we want to do | How to do it |
|---|---|---|
| 7–9 | Establish expectations for OPA1 and DNM1L | Introduce fusion/division and inspect published siRNA examples before JUMP |
| 10 | Find those perturbations in JUMP | Start with OPA1 and DNM1L, then carry exact reagent IDs between tables |
| 11 | Check whether a gene is represented | Search gene availability; read CRISPR/ORF columns (Fig. 3) |
| 12 | Know which fields answer the question | Read column definitions (Fig. 1) |
| 13 | Isolate the intended gene | Apply exact-gene, family or synonym filters (Fig. 4; SLC2A2/SLC2A/GLUT2 tutorial) |

## Inspect the phenotype and controls

| PDF | What we want to do | How to do it |
|---|---|---|
| 14 | See the expected phenotype in JUMP | Find the perturbation's source/plate, bring in controls and inspect Mito images |
| 15 | Find perturbed cells | Filter the image table and identify sources/plates (MYT1 gallery steps 1–3) |
| 16 | Choose the right comparison | Retain source/plates and include genetic negative controls (MYT1 gallery steps 4–9) |
| 17 | Inspect OPA1 knockout | Actual raw-field-derived crop and its own same-plate no-guide control |
| 18 | Inspect DNM1L knockout | Actual raw-field-derived crop and its own same-plate no-guide control |

## Read the profiles and follow up

| PDF | What we want to do | How to do it |
|---|---|---|
| 19 | Check for a measurable phenotype | Read overall activity and corrected p-value (Fig. 6; SLC2A2 CRISPR) |
| 20 | Understand one feature result | Read gene/reagent, feature, compartment, channel and statistical summary (Fig. 2) |
| 21 | Describe the differences | Inspect feature significance, rank and effect size (Fig. 7; SLC2A2 CRISPR) |
| 22 | Connect the table to our image examples | Published OPA1/DNM1L mitochondrial feature summary |
| 23 | Compare perturbation types | Open the same gene in the ORF table and compare activity/features (Fig. 8; SLC2A2) |
| 24 | Find related perturbations | Filter the match table, sort signed similarity, follow annotations/images (Fig. 9; SLC2A2) |
| 25 | Keep and share the result | Select compartments and export the filtered view with identifiers/source (Fig. 5) |
| 26 | Ask an agent to combine the steps | Cited expectations, traceable image pairs and an interactive viewer |
| 27–28 | Build tools for the question | Separate gene/raw-image explorer and phenotype-review interface examples |

Each screenshot slide uses a question title and a concrete **How** caption. Screenshot pixels, highlights and original SLC2A2/MYT1 identities are unchanged; these are navigation examples, not relabeled OPA1/DNM1L results. User-authored wording in the biology and mitochondrial-feature result slides is preserved.

## Interpretation details for speaker notes

Availability counts describe gene/reagent coverage, not replication or activity. Feature-table rows are feature–perturbation summaries from published ranked subsets. Overall activity and individual-feature significance answer different questions; displayed 0.0 values are rounded. Profile similarity is a lead to inspect alongside annotations and images, not independent identification of a molecular mechanism. ORF effects need not be the reverse of CRISPR effects. Genetic comparisons use no-guide/non-targeting controls rather than DMSO. These details remain in notes rather than adding defensive slide captions.

## Sources and rights

The [JUMP_rr tutorial](https://broadinstitute.github.io/jump_hub/howto/interactive/1_jumprr_steps.html) was read at JUMP Hub commit `86c0ff7c3420b236ab6c29fe49587bc3ba96fb77`. Broad Institute is credited by all three source records, under **CC BY 4.0**:

- [Main figures](https://zenodo.org/records/15252378).
- [Gene-availability figure](https://zenodo.org/records/16878487).
- [Gallery/control figures](https://zenodo.org/records/16878778).
- [License](https://creativecommons.org/licenses/by/4.0/).

`tutorial-screenshots-provenance.json` preserves URLs, original filenames, SHA256 hashes, dimensions, retrieval date and license metadata. Captions do not alter underlying images. Published OPA1/DRP1 microscopy is documented under CC BY-NC-SA in `opa1-literature-provenance.json`; JUMP raw-image derivatives in `gene-examples-provenance.json`.
