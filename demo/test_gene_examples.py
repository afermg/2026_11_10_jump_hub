"""Offline integrity tests for the two displayed JUMP image pairs."""
import csv
import hashlib
import json
from pathlib import Path
import struct
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GeneExamplesTests(unittest.TestCase):
    def test_pair_identity_and_controls(self):
        records = json.loads((ROOT / 'docs/gene-examples-provenance.json').read_text())['pairs']
        self.assertEqual([p['gene'] for p in records], ['OPA1', 'DNM1L'])
        plates = []
        for pair in records:
            treatment, control = pair['images']
            self.assertEqual(treatment['well']['gene'], pair['gene'])
            self.assertEqual(control['well']['jcp'], 'JCP2022_800001')
            self.assertEqual(control['well']['pert_type'], 'negcon')
            for key in ('source', 'batch', 'plate', 'modality'):
                self.assertEqual(treatment['well'][key], control['well'][key])
            plates.append(treatment['well']['plate'])
            self.assertLess(pair['scaling']['low'], pair['scaling']['high'])
            for image in pair['images']:
                self.assertEqual(image['channel'], 'Mito')
                self.assertEqual(image['site'], 0)
                self.assertEqual(image['crop_xyxy'], [384, 284, 896, 796])
                self.assertTrue(image['original_url'].startswith('https://cellpainting-gallery.s3.amazonaws.com/cpg0016-jump/'))
                for kind, size in [('full', (1280, 1080)), ('crop', (512, 512))]:
                    data = (ROOT / image[kind + '_png']).read_bytes()
                    self.assertEqual(hashlib.sha256(data).hexdigest(), image[kind + '_png_sha256'])
                    self.assertEqual(struct.unpack('>II', data[16:24]), size)
        self.assertEqual(len(set(plates)), 2)

    def test_published_feature_values(self):
        with (ROOT / 'demo/gene-feature-summary/all-published-features.csv').open() as source:
            rows = list(csv.DictReader(source))
        expected = [
            ('OPA1', 'Cytoplasm', 'Texture_Correlation', 'Mito', '_3_00_256', 3.56),
            ('DNM1L', 'Nuclei', 'ObjectSkeletonNumberBranchEnds', '', '_mito_skel', -5.953),
            ('DNM1L', 'Cells', 'Granularity_3', 'Mito', '', 4.09),
            ('DNM1L', 'Nuclei', 'ObjectSkeletonTotalObjectSkeletonLength', '', '_mito_skel', -3.551),
        ]
        keys = ['Perturbation', 'Compartment', 'Feature', 'Channel', 'Suffix']
        tex = (ROOT / 'opa1-literature.tex').read_text()
        for *identity, effect in expected:
            selected = [r for r in rows if [r[k] for k in keys] == identity]
            self.assertEqual(len(selected), 1)
            self.assertEqual(float(selected[0]["Cohen's d"]), effect)
            self.assertIn(f'${effect:+.2f}$', tex)

    def test_sources_aligned_and_tools_preserved(self):
        org = (ROOT / 'slides.org').read_text()
        tex = (ROOT / 'slides.tex').read_text()
        shared = (ROOT / 'opa1-literature.tex').read_text()
        self.assertIn('Historical: extreme nocodazole example :noexport:', org)
        self.assertNotIn('demo:extreme-nocodazole', tex)
        for source in [org, tex]:
            self.assertEqual(source.count('\\input{opa1-literature.tex}'), 1)
        for gene in ['OPA1', 'DNM1L']:
            for role in ['treatment', 'control']:
                self.assertIn(f'{gene}-{role}-center512.png', shared)
        self.assertIn('AI-assisted tools: gene and raw-image explorer', shared)
        self.assertIn('AI-assisted tools: phenotype comparison viewer', shared)
        app_frames = [f for f in shared.split('\\begin{frame}') if 'assets/vibe-coded/' in f]
        self.assertEqual(len(app_frames), 2)
        for frame in app_frames:
            self.assertEqual(frame.count('assets/vibe-coded/'), 1)
        self.assertNotIn('Vibe coding', shared)
        self.assertIn('phenotype-review.png', shared)
        self.assertIn('gene-explorer.png', shared)
        self.assertNotIn('99\\%', shared)


if __name__ == '__main__':
    unittest.main()
