# OPA1 and DNM1L: images, controls and AI-assisted tools

**Story:** fusion versus division → inspect actual JUMP knockout/control images → distinguish shape from brightness → follow genes through the Hub → build the interface needed to inspect them.

| PDF pages | Content |
| --- | --- |
| 7 | OPA1 and DNM1L: literature expectations |
| 8 | OPA1 CRISPR, zoomed Mito image versus its same-plate no-guide control |
| 9 | DNM1L CRISPR, zoomed Mito image versus its own same-plate no-guide control |
| 10 | Compare morphology, not just brightness |
| 11 | Both genes have CRISPR and ORF coverage; start with CRISPR |
| 12–15 | Hub availability/navigation tutorial (original example labels preserved) |
| 16 | Reading returned phenotype tables |
| 17–23 | Original SLC2A2/MYT1 table and gallery tutorials |
| 24 | Agent prompt: expectations → traceable images → usable viewer |
| 25 | Two interfaces built with AI assistance |
| 26–32 | Existing applications/resources and closing QR |
| 33–42 | Existing extra slides |

## Live interfaces

- Gene/raw-image explorer: http://127.0.0.1:8766/ (Oppy + private Mac forward). Choose OPA1 or DNM1L, CRISPR, exact reagent/well and Mito; press Load pair; use 2× zoom to inspect cells. Refreshing resets the selection. Each gene needs its own same-plate control.
- Phenotype review: http://127.0.0.1:8765/. Compare candidate images and literature expectations, inspect originals, record whether differences are visible. It is distinct from raw-image retrieval.

These are examples of interfaces built and refined through natural-language requests. Keep both running and retain their projects; do not replace them with static screenshots alone. Screenshot fallbacks are embedded in the deck. Localhost URLs are not public audience resources.

The presenter selected OPA1/DNM1L after visual review. DNM1L looked brighter; do not narrate this as confirmed increased connectivity. The literature expectations and the actual JUMP observations are different evidence layers. No new phenotype quantification or CellProfiler profile analysis was performed for these slides.

See [exact field provenance](../docs/gene-examples-provenance.json), [current presenter notes](../docs/gene-examples.md) and [copyable prompts](prompts.md). Historical nocodazole/blebbistatin/SLC2A2 extracts and OPA1 literature/rescue materials are retained as archives, not new results.
