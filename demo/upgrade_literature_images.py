"""Use the original Figure 3 JPEG extracted losslessly from the paper PDF.

Run pdfimages -f 5 -l 5 -j PAPER.pdf PREFIX first, then pass the JPEG and PDF.
No resampling, contrast adjustment or sharpening is applied.
"""
import hashlib
import json
from pathlib import Path
import shutil
import sys
from PIL import Image

root = Path(__file__).resolve().parents[1]
manifest_path = root / 'docs/opa1-literature-provenance.json'
manifest = json.loads(manifest_path.read_text())
source, paper = map(Path, sys.argv[1:])
destination = root / manifest['original_figure']['path']
shutil.copyfile(source, destination)
with Image.open(destination) as image:
    assert image.size == (1202, 2181)
    # Same panel boundaries as the original 400x726 web preview.
    boxes = [(0, 0, 595, 442), (0, 1340, 595, 1784), (604, 0, 1202, 442)]
    for panel, box in zip(manifest['panels'], boxes):
        target = root / panel['path']
        image.crop(box).save(target)
        panel.update(crop_xyxy=list(box), sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                     transform='Native-resolution crop of Figure 3 embedded in the published PDF; no resize, contrast change, sharpening or recoloring.')
manifest['original_figure'].update(
    url='https://pdfs.semanticscholar.org/6044/721d80bd2b60a7bdc15fe1ccd742811fb681.pdf',
    extraction='Published article PDF, page 5, image object 45 0, extracted losslessly with pdfimages -j.',
    pdf_sha256=hashlib.sha256(paper.read_bytes()).hexdigest(),
    sha256=hashlib.sha256(destination.read_bytes()).hexdigest(), size=[1202, 2181])
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
