"""Network-free checks for second-example evidence and requested slide edits."""
import csv
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SAVED = ROOT / "demo/rehearsal-blebbistatin"


def rows(name):
    with (SAVED / name).open(newline="") as stream:
        return list(csv.DictReader(stream))


class BlebbistatinTests(unittest.TestCase):
    def test_identity_and_published_activity(self):
        a = rows("annotation.csv")
        self.assertEqual(len(a), 1)
        self.assertEqual(a[0]["Metadata_repurposing_name"], "blebbistatin-(+/-)")
        activity = rows("activity.csv")[0]
        self.assertEqual(activity["JCP2022"], "JCP2022_052617")
        self.assertAlmostEqual(float(activity["Corrected p-value"]), 0.01278)
        self.assertAlmostEqual(float(activity["Phenotypic activity"]), 0.67118)
        feature = next(row for row in rows("features.csv") if row["Compartment"] == "Nuclei" and row["Feature"] == "Intensity_MedianIntensity" and row["Channel"] == "DNA")
        self.assertAlmostEqual(float(feature["Cohen's d"]), 2.241)

    def test_top_matches_preserve_unknown_annotations(self):
        m = rows("matches.csv")
        self.assertEqual(m[0]["Match JCP2022"], "JCP2022_052140")
        self.assertEqual(m[0]["Metadata_repurposing_name"], "PF-04418948")
        self.assertAlmostEqual(float(m[0]["Perturbation-Match Similarity"]), 0.737)
        self.assertEqual(m[1]["Metadata_repurposing_name"], "")

    def test_controls_and_preview_hashes(self):
        g = rows("images-and-controls.csv")
        treated = [r for r in g if r["condition"] == "blebbistatin"]
        controls = [r for r in g if r["condition"] == "DMSO"]
        self.assertEqual(len(treated), 8)
        self.assertEqual(len(controls), 256)
        keys = {(r["Source"], r["Plate"]) for r in treated}
        self.assertTrue(all((r["Source"], r["Plate"]) in keys and r["JCP2022"] == "JCP2022_033924" for r in controls))
        images = json.loads((SAVED / "image-provenance.json").read_text())["images"]
        self.assertEqual(len({(r["Source"], r["Plate"], r["site"]) for r in images}), 1)
        for r in images:
            self.assertEqual(hashlib.sha256((ROOT / r["path"]).read_bytes()).hexdigest(), r["sha256"])

    def test_requested_slide_sequence_and_removals(self):
        tex = (ROOT / "slides.tex").read_text()
        self.assertLess(tex.index("{First, an extreme example: nocodazole}"), tex.index("{Next: blebbistatin, a known biological effect}"))
        self.assertIn("{What we will check}", tex)
        self.assertNotIn("Checked before the demo", tex)
        self.assertNotIn("From a recognizable phenotype to a testable biological hypothesis", tex)
        bank = (ROOT / "tutorial-walkthrough.tex").read_text()
        self.assertNotIn("\\color{gray}", bank)
        self.assertEqual(bank.count("% Attribution:"), 11)
        self.assertEqual(bank.count("\\includegraphics"), 11)


if __name__ == "__main__":
    unittest.main()
