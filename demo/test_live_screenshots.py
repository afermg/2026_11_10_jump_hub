import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LiveScreenshotTests(unittest.TestCase):
    def test_complete_authentic_capture_manifest(self):
        manifest = json.loads((ROOT / 'docs/opa1-tutorial-screenshots-provenance.json').read_text())
        self.assertIn('Actual Firefox', manifest['method'])
        self.assertIn('no red or blue callout boxes', manifest['method'])
        self.assertNotIn("style.outline='4px", (ROOT / 'demo/capture_opa1_walkthrough.py').read_text())
        self.assertEqual(len(manifest['screenshots']), 11)
        for record in manifest['screenshots']:
            self.assertEqual(hashlib.sha256((ROOT / record['path']).read_bytes()).hexdigest(), record['sha256'])
            self.assertTrue(record['url'].startswith(('https://lite.datasette.io/', 'https://broadinstitute.github.io/jump_hub/')))
            self.assertEqual(record['highlighted_columns'], [])
            self.assertGreaterEqual(record['device_pixel_ratio'], 2)
            self.assertTrue(all(image['loaded'] for image in record['image_sources']))
            if 'gallery' in record['path']:
                for image in record['image_sources']:
                    self.assertGreaterEqual(image['display_width'] * record['device_pixel_ratio'], image['width'])
                    self.assertGreaterEqual(image['display_height'] * record['device_pixel_ratio'], image['height'])


if __name__ == '__main__':
    unittest.main()
