# Question → JUMP_rr action → example

The main sequence now interleaves the biological question with the corresponding table operation and example, rather than presenting the results first and placing all instructions in a separate walkthrough. `tutorial-walkthrough.tex` defines the eleven reusable screenshot frames; `opa1-literature.tex` calls each exactly once in context. The deck remains 45 pages, with the main talk ending at PDF35 and ten existing extra slides following.

## Find the perturbations

| PDF | What we want to do | How to do it |
|---|---|---|
| 7–9 | Establish expectations for OPA1 and DNM1L | Introduce fusion/division and inspect published siRNA examples before JUMP |
| 10 | Find those perturbations in JUMP | Start with OPA1 and DNM1L, then carry exact reagent IDs between tables |
| 11 | Check whether a gene is represented | Search the OPA prefix, select OPA1, and carry its CRISPR/ORF reagent IDs |
| 12 | Know which fields answer the question | Read the fields in an actual OPA1 CRISPR feature row |
| 13 | Isolate the intended gene | Apply `Perturbation = OPA1`, use synonym `MGM1`, and add object filters |

## Inspect the phenotype and controls

| PDF | What we want to do | How to do it |
|---|---|---|
| 14 | See the expected phenotype in JUMP | Find the perturbation's source/plate, bring in controls and inspect Mito images |
| 15 | Find perturbed cells | Filter the image table for OPA1; identify source_13, CP-CC9-R1-06 and D20 |
| 16 | Choose the right comparison | Retain that source/plate and include its no-guide/non-targeting controls |
| 17 | Inspect OPA1 knockout | Actual raw-field-derived crop and its own same-plate no-guide control |
| 18 | Inspect DNM1L knockout | Actual raw-field-derived crop and its own same-plate no-guide control |

## Read the profiles and follow up

| PDF | What we want to do | How to do it |
|---|---|---|
| 19 | Check for a measurable phenotype | Read OPA1 CRISPR and ORF activity and corrected p-values |
| 20 | Understand one feature result | Read the OPA1 reagent, object, feature, channel, significance, effect and rank |
| 21 | Describe the differences | Inspect OPA1 CRISPR feature rank, significance and signed effect size |
| 22 | Connect the table to our image examples | Published OPA1/DNM1L mitochondrial feature summary |
| 23 | Compare perturbation types | Open OPA1 ORF JCP2022_906243 and compare its activity/features with CRISPR |
| 24 | Find related perturbations | Sort OPA1 CRISPR matches; inspect MFN1 and the other leading published rows |
| 25 | Keep and share the result | Export filtered OPA1 rows with reagent, filters and source URL |
| 26 | Ask an agent to combine the steps | Cited expectations, traceable image pairs and an interactive viewer |
| 27–28 | Build tools for the question | Separate gene/raw-image explorer and phenotype-review interface examples |

Each screenshot slide uses a question title and a concrete **How** caption. The eleven active panels are newly rendered from published OPA1 JUMP_rr extracts and their embedded preview URLs; no SLC2A2/MYT1 pixels were relabeled. User-authored wording in the biology and mitochondrial-feature result slides is preserved.

## Interpretation details for speaker notes

Availability counts describe gene/reagent coverage, not replication or activity. Feature-table rows are feature–perturbation summaries from published ranked subsets. Overall activity and individual-feature significance answer different questions; displayed 0.0 values are rounded. Profile similarity is a lead to inspect alongside annotations and images, not independent identification of a molecular mechanism. ORF effects need not be the reverse of CRISPR effects. Genetic comparisons use no-guide/non-targeting controls rather than DMSO. These details remain in notes rather than adding defensive slide captions.

## Sources and rights

The [JUMP_rr tutorial](https://broadinstitute.github.io/jump_hub/howto/interactive/1_jumprr_steps.html) was read at JUMP Hub commit `86c0ff7c3420b236ab6c29fe49587bc3ba96fb77`. Its original SLC2A2/MYT1 figures remain archived unchanged and credited to Broad Institute under **CC BY 4.0**:

- [Main figures](https://zenodo.org/records/15252378).
- [Gene-availability figure](https://zenodo.org/records/16878487).
- [Gallery/control figures](https://zenodo.org/records/16878778).
- [License](https://creativecommons.org/licenses/by/4.0/).

`tutorial-screenshots-provenance.json` preserves those historical files. The active OPA1 images are actual Firefox screenshots of the public JUMP Hub gene table and Datasette Lite tools, captured on the MBP by `demo/capture_opa1_walkthrough.py`. The capture script applies real URL filters and waits for live results and visible images; red/blue DOM outlines are the only presentation annotations. No interface or data is reconstructed. `opa1-tutorial-screenshots-provenance.json` records the exact filtered URLs, browser version, capture time, viewport scroll positions and image hashes. The prior synthetic panel renderer has been removed. Published OPA1/DRP1 microscopy is documented under CC BY-NC-SA in `opa1-literature-provenance.json`; JUMP raw-image derivatives in `gene-examples-provenance.json`.

Run the capture script with `FIREFOX` and `GECKODRIVER` pointing to the installed executables and `CAPTURE_OUTPUT` set to a fresh evidence directory. The script requires Selenium. `demo/prepare_mbp_links.py MANIFEST OUTPUT.html` creates a local launch page containing the exact OPA1-filtered links plus the two private demos. The availability search uses substring matching, so OPA also returns COPA; identify the OPA1 row explicitly.

For projection, captures use a 1400-pixel window and 125% page zoom rather than shrinking a whole wide table onto the slide. The availability image is an element screenshot of the real searchable table. Feature captures concentrate on the first columns, while activity is horizontally scrolled to its metrics. Gallery URLs use Datasette's `_col` selection to display the gene, reagent, Site 0, source, plate and well; other sites remain available in the live tool. No cell values or image pixels are changed. The TeX applies explicit `trim`/`clip` bounds to remove excess screenshot area, allowing the relevant row to fill the slide width; full originals and their hashes remain intact. `CAPTURE_ONLY` accepts comma-separated PNG filenames for a focused recapture while retaining the other manifest entries.
