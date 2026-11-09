# /// script
# requires-python = ">=3.10"
# dependencies = ["polars==1.40.1"]
# ///
"""Offline summary-table preflight for the second example; not a new analysis."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import polars as pl

COMPOUND = "JCP2022_052617"  # Annotation: blebbistatin-(+/-), not an enantiopure reagent.
DMSO = "JCP2022_033924"
ROOT = "https://d3dw4c1b79pj57.cloudfront.net/latest/"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--annotations", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    inputs = {}
    frames = {}
    for name in ("compound", "compound_interpretable_features", "compound_gallery"):
        path = args.data / (name + ".parquet")
        inputs[name] = {"url": ROOT + name + ".parquet/content", "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        frames[name] = pl.read_parquet(path)
    a = pl.read_csv(args.annotations, separator="\t").unique()
    annotation = a.filter(pl.col("Metadata_JCP2022") == COMPOUND)
    assert annotation.height == 1 and annotation["Metadata_repurposing_name"][0] == "blebbistatin-(+/-)"
    annotation.write_csv(args.output / "annotation.csv")
    identity = ["JCP2022", "Perturbation", "Corrected p-value", "Phenotypic activity"]
    m = frames["compound"].filter(pl.col("JCP2022") == COMPOUND)
    f = frames["compound_interpretable_features"].filter(pl.col("JCP2022") == COMPOUND).sort("Feature Rank")
    activity = m.select(identity).unique()
    assert activity.height == 1 and activity.equals(f.select(identity).unique())
    activity.write_csv(args.output / "activity.csv")
    f.write_csv(args.output / "features.csv")
    m.filter(pl.col("Match JCP2022") != COMPOUND).sort("Perturbation-Match Similarity", descending=True).join(
        a, left_on="Match JCP2022", right_on="Metadata_JCP2022", how="left").write_csv(args.output / "matches.csv")
    g = frames["compound_gallery"]
    treated = g.filter(pl.col("JCP2022") == COMPOUND).sort(["Source", "Plate", "Well"])
    controls = g.filter(pl.col("JCP2022") == DMSO).join(treated.select("Source", "Plate").unique(), on=["Source", "Plate"], how="semi")
    pl.concat([treated.with_columns(pl.lit("blebbistatin").alias("condition")), controls.with_columns(pl.lit("DMSO").alias("condition"))]).write_csv(args.output / "images-and-controls.csv")
    first = treated.row(0, named=True)
    control = controls.filter((pl.col("Source") == first["Source"]) & (pl.col("Plate") == first["Plate"])).sort("Well").row(0, named=True)
    previews = []
    for label, row in (("blebbistatin", first), ("DMSO", control)):
        previews.append({"condition": label, **{k:row[k] for k in ("Source", "Plate", "Well", "JCP2022")}, "site": 1, "url": json.loads(row["Site 1"])["img_src"]})
    (args.output / "preview-selection.json").write_text(json.dumps(previews, indent=2) + "\n")
    inputs["annotations"] = {"source": "https://github.com/afermg/JUMP_lite/blob/dedfa397eea20542ce113c7dba38945ba6f26afd/metadata/repurposed_compounds.tsv", "sha256": hashlib.sha256(args.annotations.read_bytes()).hexdigest()}
    summary = {"gallery_wells": treated.height, "gallery_wells_excluding_source7": treated.filter(pl.col("Source") != "source_7").height, "same_source_plate_DMSO_wells": controls.height, "published_match_rows": m.height}
    manifest = {"queried_utc": datetime.now(timezone.utc).isoformat(), "compound": COMPOUND, "inputs": inputs, "summary": summary, "limitations": ["Published ranked subsets, not new p-values or an exhaustive retrieval analysis.", "A lower activity score is not proof of lower toxicity or better biological specificity.", "Three non-source_7 gallery wells are availability, not validated profile replicates.", "Dose/time, image/profile alignment, replicate analysis and direct cytokinesis readouts remain unchecked.", "Expected contractility/cytokinesis effects are prior biology, not inferred from these summary values."]}
    (args.output / "provenance.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(activity)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
