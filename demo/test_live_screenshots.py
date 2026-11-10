import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LiveScreenshotTests(unittest.TestCase):
    def test_complete_authentic_capture_manifest(self):
        manifest = json.loads((ROOT / 'docs/opa1-tutorial-screenshots-provenance.json').read_text())
        self.assertIn('Actual Firefox', manifest['method'])
        self.assertEqual(len(manifest['screenshots']), 11)
        for record in manifest['screenshots']:
            self.assertEqual(hashlib.sha256((ROOT / record['path']).read_bytes()).hexdigest(), record['sha256'])
            self.assertTrue(record['url'].startswith(('https://lite.datasette.io/', 'https://broadinstitute.github.io/jump_hub/')))


if __name__ == '__main__':
    unittest.main()
