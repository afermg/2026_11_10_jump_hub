"""Offline consistency checks for saved evidence and the revised slide sequence."""
import csv
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "demo/rehearsal-nocodazole"


def rows(name):
    with (EVIDENCE / name).open(newline="") as stream:
        return list(csv.DictReader(stream))


class NocodazoleTests(unittest.TestCase):
    def test_presence_and_activity(self):
        peers = rows("peer-presence.csv")
        self.assertEqual(len({r["JCP2022"] for r in peers}), 20)
        self.assertTrue(all(r["Perturbation"] and int(r["feature_rows"]) > 0 for r in peers))
        activity = rows("activity.csv")
        self.assertEqual(len(activity), 1)
        self.assertEqual(activity[0]["JCP2022"], "JCP2022_047835")
        self.assertAlmostEqual(float(activity[0]["Corrected p-value"]), 0.00003)

    def test_returned_peers_not_unannotated_comparators(self):
        peers = rows("returned-peers.csv")
        self.assertEqual({r["Metadata_repurposing_name"] for r in peers},
                         {"colchicine", "CYT-997", "parbendazole", "oxibendazole"})
        self.assertTrue(all(int(r["published_rank"]) <= 5 for r in peers))
        top = min(rows("nocodazole-matches.csv"), key=lambda r: int(r["published_rank"]))
        self.assertEqual(top["Metadata_repurposing_name"], "colchicine")
        self.assertAlmostEqual(float(top["Perturbation-Match Similarity"]), 0.934)

    def test_control_identity_and_source_plate(self):
        gallery = rows("images-and-controls.csv")
        treated = [r for r in gallery if r["condition"] == "nocodazole"]
        controls = [r for r in gallery if r["condition"] == "DMSO"]
        keys = {(r["Source"], r["Plate"]) for r in treated}
        self.assertEqual(len(treated), 18)
        self.assertEqual(len(controls), 969)
        self.assertTrue(all(r["JCP2022"] == "JCP2022_033924" for r in controls))
        self.assertTrue(all((r["Source"], r["Plate"]) in keys for r in controls))

    def test_preview_hashes_and_pair(self):
        images = json.loads((EVIDENCE / "image-provenance.json").read_text())["images"]
        self.assertEqual(len(images), 2)
        self.assertEqual(len({(r["source"], r["plate"], r["site"]) for r in images}), 1)
        for record in images:
            self.assertEqual(hashlib.sha256((ROOT / record["file"]).read_bytes()).hexdigest(), record["sha256"])

    def test_requested_extra_slides_and_prompt_wording(self):
        org = (ROOT / "slides.org").read_text()
        tex = (ROOT / "slides.tex").read_text()
        for title in ("Morphological profiling: How to turn images into profiles", "Words as vectors: word2vec",
                      "From words to cells: vectors for comparison", "Modern tools make image analysis more accessible",
                      "Positive controls contextualize perturbations in both learned and classical representations"):
            self.assertGreater(org.index("** " + title), org.index("* Additional slides"))
            self.assertEqual(org.count("** " + title), 1)
            self.assertEqual(tex.count("{" + title + "}"), 1)
        self.assertNotIn("Keep the analysis reproducible", org + tex + (ROOT / "demo/prompts.md").read_text())


if __name__ == "__main__":
    unittest.main()
