# Demo: ask an agent to query JUMP

## Story and stage cues

**Question:** Is SLC2A2 represented in JUMP, does its perturbation change morphology, and what looks similar?

The audience sees a researcher ask an ordinary-language question, an external coding agent consult documentation and run a query, then the researcher check the returned evidence. This is not a built-in JUMP chatbot, autonomous biological discovery, or a benchmark of agents.

- **PDF16:** show the question; switch to the agent in a fresh analysis folder.
- **First turn (~2 min):** use [prompt 1](prompts.md). Read the Hub, resolve identifiers, query CRISPR and ORF separately.
- **Second turn (~2 min):** use prompt 2. Retrieve signed profile matches and feature summaries; show sources and code.
- **Third turn (~2 min):** use prompt 3. Open a few labeled images with same-source/plate controls. Discuss artifacts and limits.
- **PDF17:** return to the checked evidence summary. Conclude: faster access to evidence, not a replacement for interpretation.
- **PDF29–30:** optional, separate prerecorded single-cell explorer from FASEB. Do not present that recording as the SLC2A2 query.

Allow **5–7 minutes**. The original FASEB 23-minute narration plan is historical and needs a new full-talk rehearsal. The example gene is easily changed, but the saved results and slide values are specifically SLC2A2. Re-query and update them before switching genes.

## What has actually been checked

A read-only Python rehearsal retrieved the public summary tables and the checksum-verified gene-coverage table. It did not rehearse an independent live agent, run a new statistical analysis, or visually validate phenotypes. The [saved CSVs](rehearsal-slc2a2/) are the offline fallback.

| Modality | Reagent | Corrected activity p-value | Activity score |
|---|---|---:|---:|
| CRISPR | JCP2022_806487 | 0.00018 | 0.91909 |
| ORF | JCP2022_910380 | 0.09482 | 0.74732 |

At 0.05, the published CRISPR activity result is significant and the ORF result is not. This is not proof of no ORF effect, nor a claim of statistical significance for every feature. Scores are reproduced from source tables, not recomputed.

Top returned non-self CRISPR match: **RAD51, JCP2022_805807, similarity 0.621**. Other leading returned matches include BACE1, FANCM, TONSL and POLE. These are candidates for interpretation, not established pathway members or direct interactions. Opposing matches do not establish phenotypic rescue.

Leading returned CRISPR features include DNA granularity and reduced cell count. Inspect cell density, viability and technical effects before inferring a specific mechanism. Feature significance displayed as 0.0 is rounded source output, not an exact probability of zero. Both feature and match tables are published ranked subsets, not exhaustive screens.

The gallery query returned **6 SLC2A2 CRISPR wells and 125 genetic-control wells** on matching source+plate pairs. Those are retrieved metadata rows, not a claim that all images were reviewed, nor proof that controls share every experimental condition. Image fields contain JSON with URLs; do not execute their contents. The live demo still needs an image-viewing rehearsal.

## Reproduce or use the fallback

Requires `uv`; the script pins Polars 1.40.1. It does not invoke an LLM.

```sh
uv run demo/query_jump.py --gene SLC2A2 \
  --cache-dir /path/to/jump-demo-cache \
  --output /path/to/new-results-folder
```

First run downloads approximately 83 MB of public summary tables, not the full images. The output directory must not exist; the script refuses to overwrite prior evidence. Use a new cache directory to refresh mutable `latest` URLs. Existing cached inputs are intentionally reused.

For offline rehearsal after prefetching inputs:

```sh
uv run demo/query_jump.py --gene SLC2A2 \
  --cache-dir /path/to/jump-demo-cache \
  --output /path/to/new-offline-results-folder --offline
```

Preinstall/cache the `uv` dependency too; `--offline` blocks data retrieval, not uv's environment provisioning. Saved CSVs require no Python environment. They include availability, separate modality activity/features, similar/opposing matches and CRISPR images/controls. `provenance.json` records source URLs, query time, input SHA256 hashes and library version. The coverage file is checked against the hash published by JUMP Hub; the other hashes identify this rehearsal snapshot, not independently authenticated releases.

On Oppy, the rehearsal input cache is `/work/scratch/amunoz/oppy-builds/jump-hub-20261110-agent-demo/data`. Transfer/cache it on the actual presentation laptop before travel; this setup did not perform that transfer. Cached raw Parquet files are not committed to the presentation repository.

If TLS certificate discovery fails in a managed Python installation, configure its trusted system CA bundle (on Oppy, `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`). Never disable TLS verification.

## On-stage failure plan

If the agent/network stalls for roughly 30 seconds, say: **“I saved the same query ahead of time; let's inspect that result.”** Open the committed CSVs, provenance and query code, then return to PDF17. Do not imply a cached result was generated live. The saved image URLs still require network access; download a small reviewed selection before relying on an offline image demonstration. The old recording is a separate optional illustration, not a substitute claimed as this query.

## Sources and maintenance

- [JUMP Hub](https://broadinstitute.github.io/jump_hub/).
- [Worked tutorial](https://broadinstitute.github.io/jump_hub/howto/interactive/1_jumprr_steps.html): availability, activity/features, matches and same-plate controls.
- [Public JUMP_rr access links](https://github.com/broadinstitute/monorepo/tree/main/libs/jump_rr#quick-data-access): links resolved to Datasette Lite with public Parquet inputs during rehearsal.
- [Gene coverage](https://zenodo.org/records/16883068): official symbols; availability counts are reagent coverage, not replicate counts.

Documentation inspected in the existing local JUMP Hub checkout at commit `80810c06bfc47f8482cfb9fddcf1a352bc38f9f0`; that checkout and its unrelated work were not modified. Runtime table snapshots are identified by the output manifest, not that documentation commit. Dynamic `latest` inputs can change: re-query shortly before the talk and check against the committed reference; investigate discrepancies rather than hard-coding expected biology.
