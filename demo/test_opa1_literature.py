"""Static source/provenance checks for the literature-review workflow."""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Opa1LiteratureTests(unittest.TestCase):
    def test_primary_figure_and_crop_hashes(self):
        p = json.loads((ROOT / "docs/opa1-literature-provenance.json").read_text())
        for record in [p["original_figure"], *p["panels"]]:
            self.assertEqual(hashlib.sha256((ROOT / record["path"]).read_bytes()).hexdigest(), record["sha256"])
        self.assertEqual(p["paper"]["doi"], "10.1083/jcb.200704112")
        self.assertEqual(p["paper"]["license"], "CC BY-NC-SA 4.0")
        self.assertEqual(p["coverage_reference"]["OPA1"], {"CRISPR": 1, "ORF": 1})

    def test_each_tutorial_frame_is_used_once_in_workflows(self):
        definitions = (ROOT / "tutorial-walkthrough.tex").read_text()
        workflow = (ROOT / "opa1-literature.tex").read_text()
        commands = re.findall(r"\\newcommand\{(\\Tutorial\w+Slide)\}", definitions)
        self.assertEqual(len(commands), 11)
        self.assertTrue(all(workflow.count(command) == 1 for command in commands))
        root = (ROOT / "slides.tex").read_text()
        self.assertEqual(root.count(r"\input{tutorial-walkthrough.tex}"), 1)
        self.assertLess(root.index(r"\input{tutorial-walkthrough.tex}"), root.index(r"\input{opa1-literature.tex}"))
        self.assertNotIn("Tutorial screenshot walkthrough", root)

    def test_review_wording_and_presenter_edits(self):
        workflow = (ROOT / "opa1-literature.tex").read_text()
        root = (ROOT / "slides.tex").read_text()
        self.assertIn("OPA1 siRNA", workflow)
        self.assertIn(r"99\%", workflow)
        self.assertNotIn("blebbistatin", workflow.lower())
        self.assertNotIn("live investigation", workflow.lower())
        self.assertNotIn("checked 9 November", root + workflow)
        self.assertIn(r"\institute{Carpenter-Shen Lab, Purdue University}", root)
        self.assertIn("{An extreme example: nocodazole}", root)
        self.assertNotIn("An obvious change in this field pair", root)


if __name__ == "__main__":
    unittest.main()
