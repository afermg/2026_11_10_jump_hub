# Nocodazole demo — CellProfiler only

**Story:** simple JUMP_rr questions → investigate whether morphology retrieves related biology → create a slide preview.

The main talk uses one compound throughout. Word2vec, representation comparisons, and “Modern tools make image analysis more accessible” are now extra slides. The previous SLC2A2 query and saved results remain historical fallback material, not the current example.

## Checked preflight

Public JUMP_rr compound match, interpretable-feature and gallery tables were retrieved on November 9, 2026. Their CloudFront response headers identified Zenodo record **20496083**. URLs, byte counts and SHA-256 hashes are in [provenance.json](rehearsal-nocodazole/provenance.json). Mutable `latest` URLs may subsequently change.

- **Nocodazole:** `JCP2022_047835`, InChIKey `KYRVNWMVYQXFEU-UHFFFAOYSA-N`.
- Published corrected activity p-value **0.00003**, activity score **0.88636**; match and feature views agree.
- **20 distinct compounds including nocodazole** have an annotation containing “microtubule inhibitor” or “tubulin polymerization inhibitor”, excluding labels also containing “stabilizing”. All 20 are present in the match and feature tables.
- Names/annotations come from the recorded Repurposing TSV in JUMP_lite; the actual query is against full JUMP_rr, not the JUMP-lite image cohort. Duplicate annotation rows were deduplicated. The target column is incomplete/inconsistent for this purpose (nocodazole lists HPGDS); use the MOA class, not inferred target genes.

| Example | JCP2022 ID | Gallery wells | Corrected activity p-value |
| --- | --- | ---: | ---: |
| Nocodazole | JCP2022_047835 | 18 | 0.00003 |
| Colchicine | JCP2022_033814 | 145 | 0.00003 |
| Vinblastine | JCP2022_042769 | 5 | 0.00160 |
| Vincristine | JCP2022_063730 | 10 | 0.00003 |
| Mebendazole | JCP2022_065384 | 5 | 0.00060 |

Gallery counts are **not validated profile replicate counts**. Nocodazole includes five source_7 gallery wells (13 excluding source_7). Confirm the live analysis's profile cohort before selecting images/replicates.

Four annotation-defined peers appear among nocodazole's five highest returned matches:

| Peer | Published cosine similarity |
| --- | ---: |
| Colchicine | 0.934 |
| CYT-997 | 0.916 |
| Parbendazole | 0.916 |
| Oxibendazole | 0.902 |

The fifth compound, `JCP2022_096054` (0.913), lacks a name/MOA in the chosen annotation snapshot; do not label it unrelated. Vinblastine/vincristine/mebendazole are present but not in nocodazole's 20 returned rows. That is not evidence of low similarity: these are published ranked subsets.

Leading meaningful feature examples include fewer neighboring cells (Cohen's d −3.306) and lower nuclear form factor (−3.110). Some other highly ranked columns are object/parent/neighbor identifiers: **do not interpret them as biological cell counts**. Obtain actual cell-count and QC metadata for the live check.

## Image preview

The deck includes two unmodified 996×996 JPEG previews: source_2, plate 1086292020, site 1; nocodazole P15 and DMSO A02. The selection was deterministic (first treated gallery row; lexically first matched DMSO well), not chosen by appearance. DMSO was resolved by its exact InChIKey and JCP2022 ID, not a substring search.

Visual review: the treatment field is sparser with several small rounded bright objects, while the control field is denser and more spread out. This is one illustrative field pair, not evidence of replicate consistency, toxicity, mitotic arrest or mechanism. Original JPEG contrast calibration is undocumented; no intensity comparison is claimed. Cell Painting does not directly stain tubulin. URLs, hashes and selection details are in [image-provenance.json](rehearsal-nocodazole/image-provenance.json).

Across the full 18-well nocodazole gallery set, 969 DMSO gallery wells match source+plate. This does not establish dose/time or image/profile-cohort equivalence.

## Flow and deployment

- Main PDF7–11: simple questions about nocodazole—availability, matches, activity/features, investigation plan and image comparison.
- PDF12: switch to the agent for the longer investigation; use [prompts.md](prompts.md).
- Intervene with the cell-density/toxicity question.
- Ask for one-slide output and a preview, not publication.
- PDF13: return to “What we know, and what we will check”. Do not present unfinished checks as results.
- Main talk ends at PDF20. Ten extra slides follow, including the five moved slides and the historical single-cell recording.

Run computation and backends on **Oppy**, with the interface forwarded to the **MacBook**. Do not copy the full dataset to the laptop or start duplicate services. Backend availability, forwarding, authenticated editor access and end-to-end live execution still need rehearsal; this preflight did not configure them.

## Remaining live-workflow prerequisites

1. Select the actual full well-level CP profile release; verify source/cohort and profile-image alignment.
2. Retrieve dose/time, replicate, actual count and QC metadata.
3. Define annotated peers and a defensible annotated comparator set before ranking.
4. Check replicate consistency and peer retrieval versus the comparator set.
5. Rehearse the running analysis and slide-preview backends through the forwarded MBP interface.

The example is ready for the simple-question slides, but the deeper statistical workflow is not yet validated.

## Reproduce the summary extraction

```sh
uv run demo/check_nocodazole.py \
  --data /work/scratch/amunoz/jump-nocodazole-preflight-20261109/data \
  --annotations /work/users/amunoz/projects/JUMP_lite/metadata/repurposed_compounds.tsv \
  --output /path/to/new-results
```

The extractor is offline: prefetch the three compound Parquets, `compound.csv.gz`, and the recorded annotation TSV from the URLs in the manifest. It pins Polars 1.40.1 and refuses an existing output directory. This reproduces summary extraction, not a new statistical analysis. Cache the uv environment before an offline rehearsal.

If live execution stalls for roughly 30 seconds, open the saved extracts and preview pair and say: **“This is the query I checked ahead of time; the replicate-level investigation is the next step.”** Do not claim cached results were generated live.
