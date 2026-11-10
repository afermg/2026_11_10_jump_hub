# /// script
# dependencies = ["Pillow==12.1.1"]
# ///
"""Export explicitly selected raw-field display pairs from the local gene viewer.
No search for dramatic cells: identical central 512x512 crop rule for all panels.
Run on Oppy: uv run demo/export_gene_pairs.py (viewer on 127.0.0.1:8766).
"""
import base64
import hashlib
import io
import json
from pathlib import Path
from urllib.request import Request, urlopen
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/gene-examples'
OUT.mkdir(parents=True, exist_ok=True)
records = []
for gene, treatment, control, jcp in [('OPA1', 1804, 1743, 'JCP2022_804796'), ('DNM1L', 683, 367, 'JCP2022_801877')]:
    selection = dict(treatment=treatment, control=control, site=0, channel='Mito')
    request = Request('http://127.0.0.1:8766/api/pair', data=json.dumps(selection).encode(), headers={'Content-Type': 'application/json'})
    with urlopen(request, timeout=120) as response:
        pair = json.load(response)
    a, b = pair['images']
    assert a['well']['gene'] == gene and a['well']['jcp'] == jcp
    assert b['well']['pert_type'] == 'negcon' and b['well']['jcp'] == 'JCP2022_800001'
    for key in ('source', 'batch', 'plate', 'modality'):
        assert a['well'][key] == b['well'][key]
    for role, image in zip(('treatment', 'control'), pair['images']):
        png = base64.b64decode(image.pop('png').split(',', 1)[1])
        full = OUT / f'{gene}-{role}-full.png'
        full.write_bytes(png)
        with Image.open(io.BytesIO(png)) as im:
            assert im.size == (image['width'], image['height'])
            assert min(im.size) >= 512
            x, y = (im.width - 512) // 2, (im.height - 512) // 2
            box = (x, y, x + 512, y + 512)
            crop = OUT / f'{gene}-{role}-center512.png'
            im.crop(box).save(crop)
        image.update(full_png=str(full.relative_to(ROOT)), crop_png=str(crop.relative_to(ROOT)), crop_xyxy=box,
                     full_png_sha256=hashlib.sha256(png).hexdigest(), crop_png_sha256=hashlib.sha256(crop.read_bytes()).hexdigest())
    pair.pop('stats', None)
    records.append(dict(gene=gene, selection=selection, **pair))
manifest = dict(selection_rule='Default first production CRISPR well and first documented same-plate no-guide control in the viewer; site index 0, Mito. Not a claim to reconstruct exact browser selections.',
                display_rule='Original uint16 TIFF -> full-resolution grayscale PNG with common pooled 0.5–99.5 percentile limits within each pair. Limits differ across plates; no cross-pair brightness comparison. Center 512x512 crop, no additional contrast or sharpening.',
                interpretation='User confirmed visible OPA1 CRISPR/control difference and selected OPA1 and DNM1L as examples. DNM1L increased brightness does not establish increased connectivity. No phenotype quantification.', pairs=records)
(ROOT / 'docs/gene-examples-provenance.json').write_text(json.dumps(manifest, indent=2)+'\n')
print(json.dumps([{ 'gene': r['gene'], 'scaling': r['scaling']} for r in records], indent=2))
