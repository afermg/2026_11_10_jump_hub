# Agent-assisted gene examples and interactive tools

## 1. Establish expectations

> Find primary studies explaining how OPA1 and DNM1L/DRP1 affect mitochondrial fusion and division. Explain the expected effects of loss of function and show the published evidence. Start with Griparic et al., JCB 2007 (10.1083/jcb.200704112), and Smirnova et al., MBoC 2001 (10.1091/mbc.12.8.2245). Keep the study perturbation and cell system clear.

## 2. Find the data

> Locate OPA1 and DNM1L in JUMP Hub. Show exact CRISPR and ORF identifiers, then link the CellProfiler feature, match and image resources. Use the Hub's worked tutorials to explain the views; keep their original example gene names visible.

## 3. Build the raw-image explorer

> Build an interactive interface where I can select a gene, modality and reagent; choose an available treatment field and documented genetic negative control from the same source, batch and plate; and load the original raw TIFFs only when requested. Show provenance and use shared display limits within each pair. Add matched zoom and independent pan so I can inspect individual cells.

Existing implementation: `/work/users/amunoz/projects/jump-gene-image-browser`; local private URL http://127.0.0.1:8766/. Do not redeploy or replace it during the talk. OPA1 and DNM1L occupy different plates and therefore require separate matched control fields.

## 4. Build the image-review interface

> Build a comparison viewer for candidate perturbations, with control/treated images, source links and optional literature expectations. Clearly label published figure crops versus JUMP previews. Let me record whether I can actually see the difference before selecting an example.

Existing implementation: `/work/users/amunoz/projects/phenotype-comparator`; local private URL http://127.0.0.1:8765/. This viewer uses published images and JUMP JPEG previews; it is not a raw-image loader.

## 5. Inspect and refine

> The image looks brighter overall. Add zoom while retaining shared intensity limits, so I can assess structure rather than brightness alone. Confirm that zoom does not fetch more raw images or alter intensity scaling.

The matched zoom refinement is implemented and tested. The presenter selected OPA1 and DNM1L after visual review. This selection does not establish a quantified mitochondrial phenotype. No automatic biological interpretation follows from the viewer's output.
