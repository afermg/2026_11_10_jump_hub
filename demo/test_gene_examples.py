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
        tex = (ROOT / 'slides.tex').read_text()
        for *identity, effect in expected:
            selected = [r for r in rows if [r[k] for k in keys] == identity]
            self.assertEqual(len(selected), 1)
            self.assertEqual(float(selected[0]["Cohen's d"]), effect)
            self.assertIn(f'${effect:+.2f}$', tex)

    def test_literature_precedes_jump_and_crop_hashes(self):
        shared = (ROOT / 'slides.tex').read_text()
        self.assertLess(shared.index('literature:opa1-siRNA'), shared.index('JUMP example: OPA1'))
        self.assertLess(shared.index('literature:dnm1l-siRNA'), shared.index('JUMP example: OPA1'))
        self.assertIn('Fig. 3G/A', shared)
        self.assertIn('Fig. 3B/A', shared)
        manifest = json.loads((ROOT / 'docs/opa1-literature-provenance.json').read_text())
        self.assertEqual(len(manifest['panels']), 3)
        for panel in manifest['panels']:
            data = (ROOT / panel['path']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), panel['sha256'])
            x0, y0, x1, y1 = panel['crop_xyxy']
            self.assertEqual(struct.unpack('>II', data[16:24]), (x1-x0, y1-y0))

    def test_question_table_example_order(self):
        shared = (ROOT / 'slides.tex').read_text()
        sequence = [
            'label={tutorial:availability}',
            'label={filtering_example}', 'label={tutorial:gallery-controls}',
            'label={tutorial:interface}', 'label={tutorial:filters}',
            'label={tutorial:activity}', 'label={tutorial:rows}', 'label={tutorial:features}',
            'CellProfiler detects mitochondrial feature changes',
            'label={tutorial:orf}', 'label={tutorial:matches}', 'label={tutorial:export}',
            'JUMP example: OPA1', 'JUMP example: DNM1L',
        ]
        positions = [shared.index(item) for item in sequence]
        self.assertEqual(positions, sorted(positions))
        for item in sequence:
            self.assertEqual(shared.count(item), 1)
        tutorial = (ROOT / 'slides.tex').read_text()
        self.assertEqual(tutorial.count('\\textbf{How:}'), 11)
        self.assertIn('Can we validate the phenotypes using our high-throughput methods?', shared)
        self.assertIn('Mitochondrial organization changes.', shared)
        self.assertNotIn('These features do not directly establish', shared)

    def test_expected_phenotype_uses_gallery_and_hover_tip(self):
        shared = (ROOT / 'slides.tex').read_text()
        frame = shared.split(']{How do the cells look?}', 1)[1].split('\\end{frame}', 1)[0]
        self.assertIn('00-opa1-crispr-gallery.png', frame)
        self.assertIn('CRISPR Gallery --- OPA1', frame)
        self.assertLess(shared.index('00-opa1-crispr-gallery.png'), shared.index('label={filtering_example}'))
        self.assertIn('Imagus (Firefox)', frame)
        self.assertIn('Hover Zoom+ (Chrome)', frame)
        self.assertIn('\\scriptsize', frame)
        self.assertNotIn('\\begin{itemize}', frame)

    def test_full_opa1_gallery_capture(self):
        manifest = json.loads((ROOT / 'docs/opa1-full-gallery-provenance.json').read_text())
        self.assertEqual(manifest['title'], 'CRISPR Gallery')
        self.assertEqual(manifest['rows'], 5)
        self.assertEqual(len(manifest['images']), 45)
        self.assertTrue(all(image['loaded'] and (image['width'], image['height']) == (1280, 1080)
                            for image in manifest['images']))
        self.assertEqual([h for h in manifest['headers'] if h.startswith('Site ')],
                         [f'Site {i}' for i in range(9)])
        self.assertIn('Perturbation__exact=OPA1', manifest['url'])
        self.assertNotIn('Plate__exact', manifest['url'])
        data = (ROOT / manifest['path']).read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(), manifest['sha256'])

    def test_sources_aligned_and_tools_preserved(self):
        org = (ROOT / 'slides.org').read_text()
        tex = (ROOT / 'slides.tex').read_text()
        shared = (ROOT / 'slides.tex').read_text()
        self.assertIn('Historical: extreme nocodazole example :noexport:', org)
        self.assertNotIn('demo:extreme-nocodazole', tex)
        self.assertIn('Historical presenter notes', org)
        self.assertNotIn('\\input{', tex)
        self.assertNotIn('\\include{', tex)
        self.assertNotIn('\\newcommand', tex)
        starts = [line.removeprefix('% BEGIN FRAME: ') for line in tex.splitlines()
                  if line.startswith('% BEGIN FRAME: ')]
        ends = [line.removeprefix('% END FRAME: ') for line in tex.splitlines()
                if line.startswith('% END FRAME: ')]
        self.assertEqual(starts, ends)
        self.assertEqual(len(starts), 44)
        self.assertEqual(len(set(starts)), 44)
        self.assertEqual([p.name for p in ROOT.glob('*.tex')], ['slides.tex'])
        for gene in ['OPA1', 'DNM1L']:
            for role in ['treatment', 'control']:
                self.assertIn(f'{gene}-{role}-center512.png', shared)
        self.assertIn('AI-assisted tools: gene and raw-image explorer', shared)
        self.assertNotIn('AI-assisted tools: phenotype comparison viewer', shared)
        self.assertIn('Record which differences are visible.', shared)
        self.assertNotIn('You define the question.', shared)
        app_frames = [f for f in shared.split('\\begin{frame}') if 'assets/vibe-coded/' in f]
        self.assertEqual(len(app_frames), 1)
        for frame in app_frames:
            self.assertEqual(frame.count('assets/vibe-coded/'), 1)
        self.assertNotIn('Vibe coding', shared)
        self.assertNotIn('phenotype-review.png', shared)
        self.assertIn('gene-explorer.png', shared)
        self.assertNotIn('99\\%', shared)
        self.assertNotIn('Central 512', shared)
        self.assertIn('intensity limits 219--3985', shared)
        self.assertIn('intensity limits 187--4463', shared)

    def test_validation_slide_and_baseline(self):
        shared = (ROOT / 'slides.tex').read_text().replace('\\\\', ' ')
        title = 'we can validate existing knowledge to develop methods leading to new discoveries'
        self.assertEqual(shared.count(title), 1)
        self.assertLess(shared.index('JUMP example: DNM1L'), shared.index(title))
        self.assertLess(shared.index(title), shared.index('Agents can help'))
        frame = shared.split(']{' + title + '}', 1)[1].split('\\end{frame}', 1)[0]
        self.assertIn('feature-validation.pdf', frame)
        self.assertNotIn('exploratory', frame.lower())
        self.assertNotIn('caveat', frame.lower())
        with (ROOT / 'demo/opa1-dnm1l-analysis/all-features.csv').open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 3651)
        self.assertEqual(sum(float(r['OPA1_d'])*float(r['DNM1L_d'])>0 for r in rows), 3154)
        hits = [r for r in rows if r['opposite']=='true' and r['both_q05']=='true']
        self.assertEqual(len(hits), 15)
        self.assertEqual(sum(r['both_welch_q05']=='true' for r in hits), 8)


if __name__ == '__main__':
    unittest.main()
