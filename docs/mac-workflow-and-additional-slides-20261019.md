# Mac-edited workflow and additional slides — 2026-10-19

## Requested changes

Use the presenter's saved Mac edit of `cell-painting-editable.svg` to improve
the workflow illustration, and move the Nahual overview and vector comparison
to additional slides after the main talk. The microscopy montage is unchanged.
The older detailed Nahual slide stays `:noexport:`; no hidden slide is restored.

- Main talk: 22 pages, ending Thank you (20), References (21), QR (22).
- Additional slides: Nahual names/swaps (23), vector comparison (24).
- Total: 24 pages; main narration remains 1,380 seconds, plus two-minute buffer.
- Demo playback moves to PDF 13 / visible 12; second still is PDF 14.
- No slide wording changes except technical source notes and the workflow asset.

## Exact saved artwork

Mac file: `/Users/alan/Downloads/jump-editable-figures.MS4HFe/cell-painting-editable.svg`.
Saved modification time: 2026-10-19 10:02:02 -0400. The remote-before, transferred
and remote-after hashes matched. Canonical `deck/assets/cell-painting-edited.svg`
is that exact 740,077-byte file, not regenerated artwork.

- SVG SHA-256: `ba164a5f732ac0fc826bc026b86b898e84f31180b9cafc269cdc119ac48056aa`.
- Consumed vector PDF SHA-256: `f84d50e232b9a742e8bd122611c59ad9af2f033a2dc06754f1bcc8b0d546f8be`.
- 3000-pixel preview PNG SHA-256: `885bf928e2f0c1c6ad3267f38beab18acb0d34b221617ca8f6e168debec98aae`.

The Mac's Inkscape 1.4.4 exported the PDF with `--export-text-to-path`, preserving
the saved appearance without runtime font dependencies. The SVG keeps its 18
editable text objects. The single hidden raster reference is not exported;
the PDF and the compiled workflow slide contain **zero raster images**. No
external SVG href dependencies, scripts or foreignObject elements were found.
Mac Fontconfig reported a nonfatal configuration warning. Both exports were
produced and visually checked for complete, legible labels and unclipped artwork;
the final PDF contains no font resources because text is outlined.

The original PNG remains in canonical assets/history. The publisher removes it
from the consumed Overleaf bundle because the slide now uses the PDF. Other
figure bytes are unchanged. The raw SVG is retained in the authoring repository;
the private distribution mirror receives only consumed source artwork.

## Attribution and limitations

The schematic was redrawn from the earlier workflow PNG, then edited by the
presenter. The original published schematic was identified as Figure 1a in
Chandrasekaran et al., *Image-based profiling for drug discovery: due for a
machine-learning upgrade?*, Nature Reviews Drug Discovery 20, 145–159 (2021),
<https://doi.org/10.1038/s41573-020-00117-w>. The intermediate I2K asset and its
previous U2OS-label adaptation remain documented in `docs/assets.json`.

This is illustrative reconstruction, not recovered original vector artwork,
raw microscopy or quantitative heatmap/network data. Attribution is not a new
licensing clearance. Do not rerun the original reconstruction generator over
the presenter's edited SVG. The original editable package remains archived.

## Acceptance and publication boundaries

Validated two-pass XeLaTeX/QPDF preview: 24 pages, no final-pass warnings or box
warnings. All active frame contents match the fetched live deck after accounting
for ordering, generated labels and the one authorized PNG→PDF reference change.
Existing model names, live JUMP-lite wording, hidden detailed Nahual, unchanged
figures and both 40-mm QR destinations are preserved. Demo links resolve on
pages 13/14; the removed benchmark citation remains absent.

Before integration, verify clean source, no open canonical Emacs file buffers,
fresh Overleaf head and inactive publisher service. Use normal guarded sync;
never rewrite its baseline or force-push. Preserve unowned `main.tex` and leave
Overleaf comments untouched. Keep the mirror private and `slides.pdf` absent.
The workflow PDF is source figure artwork, not presentation-PDF release approval.

Full transfer, preview, validation and publication evidence is retained outside
Git under `mac-workflow-svg.FpueEe` in the conference evidence directory.
