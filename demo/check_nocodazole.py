# /// script
# requires-python = ">=3.10"
# dependencies = ["polars==1.40.1"]
# ///
"""Bounded CP-only preflight; published summaries, not new retrieval statistics.

Inputs: three cached JUMP_rr compound Parquets, compound.csv.gz, and the
Repurposing annotation TSV. Output must be new. No network or LLM calls.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import polars as pl

NOC = "JCP2022_047835"
DMSO_KEY = "IAZDPXIOMUYVGZ-UHFFFAOYSA-N"
ROOT = "https://d3dw4c1b79pj57.cloudfront.net/latest/"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data", type=Path, required=True)
    p.add_argument("--annotations", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    a = pl.read_csv(args.annotations, separator="\t").unique()
    # Define the comparison class from annotations before examining match scores.
    peers = a.filter(
        pl.col("Metadata_repurposing_moa").str.contains("tubulin polymerization inhibitor|microtubule inhibitor")
        & ~pl.col("Metadata_repurposing_moa").str.contains("stabilizing")
    ).rename({"Metadata_JCP2022": "JCP2022"})
    frames = {name: pl.read_parquet(args.data / f"{name}.parquet") for name in
              ("compound", "compound_interpretable_features", "compound_gallery")}
    m, f, g = (frames[name] for name in ("compound", "compound_interpretable_features", "compound_gallery"))
    identity = ["JCP2022", "Perturbation", "Corrected p-value", "Phenotypic activity"]
    presence = peers.join(m.select(identity).unique(), on="JCP2022", how="left")
    presence = presence.join(g.group_by("JCP2022").len().rename({"len": "gallery_wells"}), on="JCP2022", how="left")
    presence = presence.join(f.group_by("JCP2022").len().rename({"len": "feature_rows"}), on="JCP2022", how="left")
    presence.sort("Metadata_repurposing_name").write_csv(args.output / "peer-presence.csv")
    matches = m.filter((pl.col("JCP2022") == NOC) & (pl.col("Match JCP2022") != NOC)).sort(
        ["Perturbation-Match Similarity", "Match JCP2022"], descending=[True, False])
    matches = matches.with_row_index("published_rank", offset=1).join(
        a.select("Metadata_JCP2022", "Metadata_repurposing_name", "Metadata_repurposing_moa").unique(),
        left_on="Match JCP2022", right_on="Metadata_JCP2022", how="left")
    matches.write_csv(args.output / "nocodazole-matches.csv")
    matches.filter(pl.col("Match JCP2022").is_in(peers["JCP2022"].to_list())).write_csv(args.output / "returned-peers.csv")
    features = f.filter(pl.col("JCP2022") == NOC).sort("Feature Rank")
    features.write_csv(args.output / "nocodazole-features.csv")
    activity = m.filter(pl.col("JCP2022") == NOC).select(identity).unique()
    assert activity.equals(features.select(identity).unique()), "Activity differs between tables"
    activity.write_csv(args.output / "activity.csv")
    treated = g.filter(pl.col("JCP2022") == NOC)
    compound_metadata = pl.read_csv(args.data / "compound.csv.gz")
    dmso_ids = compound_metadata.filter(pl.col("Metadata_InChIKey") == DMSO_KEY)["Metadata_JCP2022"].to_list()
    assert dmso_ids == ["JCP2022_033924"]
    controls = g.filter(pl.col("JCP2022").is_in(dmso_ids)).join(
        treated.select("Source", "Plate").unique(), on=["Source", "Plate"], how="semi")
    pl.concat([treated.with_columns(pl.lit("nocodazole").alias("condition")),
               controls.with_columns(pl.lit("DMSO").alias("condition"))]).write_csv(args.output / "images-and-controls.csv")
    inputs = {}
    for name in frames:
        path = args.data / f"{name}.parquet"
        inputs[name] = {"url": ROOT + name + ".parquet/content", "bytes": path.stat().st_size,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    for name, path in (("annotations", args.annotations), ("compound_metadata", args.data / "compound.csv.gz")):
        inputs[name] = {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    inputs["annotations"]["source"] = "https://github.com/afermg/JUMP_lite/blob/dedfa397eea20542ce113c7dba38945ba6f26afd/metadata/repurposed_compounds.tsv"
    inputs["compound_metadata"]["source"] = "https://raw.githubusercontent.com/jump-cellpainting/datasets/main/metadata/compound.csv.gz"
    summary = {"annotated_class_including_nocodazole": peers.height,
               "class_present_in_matches": presence.filter(pl.col("Perturbation").is_not_null()).height,
               "class_present_in_features": presence.filter(pl.col("feature_rows").is_not_null()).height,
               "nocodazole_gallery_wells": treated.height,
               "nocodazole_gallery_wells_excluding_source7": treated.filter(pl.col("Source") != "source_7").height,
               "same_source_plate_DMSO_wells": controls.height,
               "published_match_rows": matches.height}
    manifest = {"queried_utc": datetime.now(timezone.utc).isoformat(), "inputs": inputs, "summary": summary,
                "representation": "CellProfiler-derived batch-corrected match profiles; interpretable CP feature summaries separately",
                "limits": ["Published ranked subsets; no exhaustive enrichment or replicate analysis performed.",
                           "Gallery counts are image availability, not profile replicate counts.",
                           "Dose/time and profile-image cohort alignment still need verification.",
                           "Use MOA class, not the incomplete target column, to define peers."]}
    (args.output / "provenance.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
