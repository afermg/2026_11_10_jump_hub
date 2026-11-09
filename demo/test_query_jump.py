"""Fast, network-free checks for the rehearsal helper and committed reference."""
import csv
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from query_jump import retrieve

REFERENCE = Path(__file__).parent / "rehearsal-slc2a2"


def rows(name):
    with (REFERENCE / name).open(newline="") as stream:
        return list(csv.DictReader(stream))


class RehearsalTests(unittest.TestCase):
    def test_offline_cache_miss_does_not_access_network(self):
        with tempfile.TemporaryDirectory() as folder, patch("urllib.request.urlopen") as request:
            with self.assertRaises(FileNotFoundError):
                retrieve("https://example.com/missing", Path(folder) / "missing", True)
            request.assert_not_called()

    def test_cached_input_is_hashed_without_network(self):
        with tempfile.TemporaryDirectory() as folder, patch("urllib.request.urlopen") as request:
            path = Path(folder) / "cached"
            path.write_bytes(b"verified input")
            result = retrieve("https://example.com/cached", path, True)
            self.assertEqual(result["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
            request.assert_not_called()

    def test_rehearsal_activity_and_identifiers(self):
        activity = {row["modality"]: row for row in rows("activity.csv")}
        self.assertEqual(activity["crispr"]["JCP2022"], "JCP2022_806487")
        self.assertEqual(activity["orf"]["JCP2022"], "JCP2022_910380")
        self.assertAlmostEqual(float(activity["crispr"]["Corrected p-value"]), 0.00018)
        self.assertAlmostEqual(float(activity["orf"]["Corrected p-value"]), 0.09482)
        matches = rows("crispr-similar.csv")
        self.assertEqual(matches[0]["Match"], "RAD51")
        self.assertAlmostEqual(float(matches[0]["Perturbation-Match Similarity"]), 0.621)
        self.assertTrue(all(row["JCP2022"] != row["Match JCP2022"] for row in matches))

    def test_controls_share_source_and_plate_with_query(self):
        gallery = rows("crispr-images-and-controls.csv")
        treated = [row for row in gallery if row["Perturbation"] == "SLC2A2"]
        controls = [row for row in gallery if row["Perturbation"] != "SLC2A2"]
        self.assertEqual(len(treated), 6)
        self.assertEqual(len(controls), 125)
        keys = {(row["Source"], row["Plate"]) for row in treated}
        self.assertTrue(all(row["Perturbation"] in ("no-guide", "non-targeting") for row in controls))
        self.assertTrue(all((row["Source"], row["Plate"]) in keys for row in controls))


if __name__ == "__main__":
    unittest.main()
