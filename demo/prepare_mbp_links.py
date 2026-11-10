import html
import json
import sys
from pathlib import Path

manifest = json.loads(Path(sys.argv[1]).read_text())
links = {
    'Local backup slides (PDF)': 'JUMP-OPA1-slides.pdf',
    'Overleaf slides': 'https://overleaf.quasimorphic.com/project/6af238ebaa6d5b0395871289',
    'JUMP Hub': 'https://broadinstitute.github.io/jump_hub/',
    'Gene / raw-image explorer': 'http://127.0.0.1:8766/',
    'Phenotype comparison viewer': 'http://127.0.0.1:8765/',
    **manifest['links'],
}
items = ''.join('<li><a target="_blank" rel="noopener" href="' + html.escape(url, quote=True) + '">' + html.escape(title) + '</a></li>' for title, url in links.items())
document = '<!doctype html><meta charset="utf-8"><title>JUMP talk — OPA1 demo links</title><style>body{font:20px system-ui;max-width:850px;margin:50px auto;padding:20px;line-height:1.6}li{margin:12px 0}a{color:#075a85}h1{font-size:32px}</style><h1>JUMP talk — OPA1 demo links</h1><p>Real JUMP Hub tools, prefiltered for OPA1. The two localhost demos use the private connection to Oppy.</p><ol>' + items + '</ol><p>Gene availability: enter <b>OPA</b> in Search. Raw-image explorer: OPA1 → CRISPR → Mito → Load pair → 2×. The public tables can take a minute to load their datasets.</p>'
Path(sys.argv[2]).write_text(document)
