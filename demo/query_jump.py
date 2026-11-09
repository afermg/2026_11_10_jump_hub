# /// script
# requires-python = ">=3.10"
# dependencies = ["polars==1.40.1"]
# ///
"""Read-only rehearsal query, not an AI agent or a new statistical analysis.

uv run demo/query_jump.py --gene SLC2A2 --cache-dir /path/to/cache --output /path/to/results
Downloads only public summary tables (~83 MB total), never the full image dataset.
Cached inputs are retained for offline rehearsal; provenance records their hashes.
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import shutil
import urllib.request

import polars as pl

COVERAGE_URL = "https://zenodo.org/api/records/16883068/files/table.csv/content"
COVERAGE_HASH = "40f12b266d632d8593b29c4a327cd82cffc36ad354e92815bf77e6d2f5008ec7"
ROOT = "https://d3dw4c1b79pj57.cloudfront.net/latest/"
TABLES = ("crispr", "orf", "crispr_interpretable_features", "orf_interpretable_features", "crispr_gallery")
IDENTITY = ["Perturbation", "JCP2022", "Corrected p-value", "Phenotypic activity"]
SCORE = "Perturbation-Match Similarity"


def retrieve(url, path, offline):
    if not path.exists():
        if offline:
            raise FileNotFoundError(f"Offline input missing: {path}")
        part = path.with_suffix(path.suffix + ".part")
        try:
            with urllib.request.urlopen(url, timeout=60) as source, part.open("wb") as target:
                shutil.copyfileobj(source, target)
            part.replace(path)
        finally:
            part.unlink(missing_ok=True)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return {"url": url, "sha256": digest, "bytes": path.stat().st_size}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gene", default="SLC2A2", help="Exact official gene symbol; no synonym expansion")
    parser.add_argument("--cache-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path, help="Must be a new directory")
    parser.add_argument("--offline", action="store_true", help="Never use the network")
    args = parser.parse_args()
    gene = args.gene.strip().upper()
    if not gene:
        parser.error("Gene cannot be blank")
    args.output.mkdir(parents=True, exist_ok=False)
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    provenance = {"query_utc": datetime.now(timezone.utc).isoformat(), "gene": gene,
                  "polars_version": pl.__version__, "offline": args.offline, "inputs": {}}
    coverage = args.cache_dir / "gene-coverage.csv"
    info = retrieve(COVERAGE_URL, coverage, args.offline)
    if info["sha256"] != COVERAGE_HASH:
        raise ValueError("Gene-coverage checksum mismatch")
    provenance["inputs"]["coverage"] = info
    availability = pl.read_csv(coverage).filter(pl.col("Gene") == gene)
    availability.write_csv(args.output / "availability.csv")
    frames = {}
    for name in TABLES:
        path = args.cache_dir / (name + ".parquet")
        provenance["inputs"][name] = retrieve(ROOT + name + ".parquet/content", path, args.offline)
        frames[name] = pl.read_parquet(path)
    activities = []
    for modality in ("crispr", "orf"):
        matches = frames[modality].filter(pl.col("Perturbation") == gene)
        features = frames[modality + "_interpretable_features"].filter(pl.col("Perturbation") == gene)
        # Check that the two published views agree per reagent; never merge ORF and CRISPR.
        a = matches.select(IDENTITY).unique().sort("JCP2022")
        b = features.select(IDENTITY).unique().sort("JCP2022")
        if not a.equals(b):
            raise ValueError(f"{modality}: missing/inconsistent activity rows; inspect sources")
        activities.extend({"modality": modality, **row} for row in a.to_dicts())
        # Reagent-specific top/bottom five among PUBLISHED rows, excluding self matches.
        candidates = matches.filter(pl.col("JCP2022") != pl.col("Match JCP2022"))
        for direction, descending in (("similar", True), ("opposing", False)):
            selected = candidates.sort([SCORE, "Match JCP2022"], descending=[descending, False]).group_by("JCP2022", maintain_order=True).head(5)
            selected.write_csv(args.output / f"{modality}-{direction}.csv")
        features.sort(["JCP2022", "Feature Rank", "Feature significance"]).group_by("JCP2022", maintain_order=True).head(5).write_csv(args.output / f"{modality}-features.csv")
    activity = pl.DataFrame(activities) if activities else pl.DataFrame(schema={"modality": pl.String, **{key: pl.String for key in IDENTITY}})
    activity.write_csv(args.output / "activity.csv")
    gallery = frames["crispr_gallery"]
    treated = gallery.filter(pl.col("Perturbation") == gene)
    # Compound controls differ: this demo only uses the documented genetic control names.
    controls = gallery.filter(pl.col("Perturbation").is_in(["no-guide", "non-targeting"]))
    controls = controls.join(treated.select("Source", "Plate").unique(), on=["Source", "Plate"], how="semi")
    pl.concat([treated, controls]).write_csv(args.output / "crispr-images-and-controls.csv")
    provenance["summary"] = {"availability_rows": availability.height, "activity_rows": activity.height,
                              "crispr_image_wells": treated.height, "same_plate_control_wells": controls.height}
    (args.output / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(activity)
    print(json.dumps(provenance["summary"], indent=2))
    print("Published subsets only. No new p-values; no image inspection or mechanism validation performed.")


if __name__ == "__main__":
    main()
