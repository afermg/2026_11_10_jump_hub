# Closing-slide simplification — 19 October 2026

Presenter request: keep only JUMP Hub and the slides on the QR page; display
`broad.io/jump`; remove illustration credits from the last slide; publish source
updates to the live Overleaf project and GitHub.

PDF page 21 now has two 40-mm QR codes, with their existing payloads retained:
JUMP Hub and the reserved GitHub slides-PDF URL. The visible shortlink is
clickable. The additional JUMP-lite/cp_measure codes and separate recording link
are removed from this page. The recording still links from its demonstration
slides as specified by the direct Overleaf edits.

PDF page 22 retains scientific references and resources, but not the
illustration/logo-credit bullets or figure-number annotations. Original figure
and logo provenance and rights remain recorded in `docs/provenance.md` and
`docs/assets.json`; this display change does not alter those rights.

## Preserve direct Overleaf edits

The direct changes through `77620e9` (including the earlier `27f89d0`) were preserved in the Org source before
publication: revised nuclear-area bullet and AI heading; removal of the first
demo text link; tools / cp_measure / JUMP-lite ordering; the revised AI sentence,
cp_measure bullet and JUMP-lite heading; and removal of the visible intensity
benchmark. The later removal of the application-slide pipeline footer was also
preserved after the live-head race guard stopped publication. Their speaker-note
context remains available without reinstating the
removed visible claims.

Normalized frame comparison against that live snapshot confirms that only PDF
pages 21 and 22 change. The separate title and the other 19 content frames match,
ignoring generated Org frame IDs and whitespace. XeLaTeX's second pass has no
warnings, QPDF validation succeeds, and the deck remains 22 pages. Both QR codes
decode from the rendered page to the intended unchanged destinations. Closing
pages were visually inspected. An initial comparison fixture incorrectly counted
the separate title as a begin-frame block; that failure is retained in evidence.

Evidence and before-state Git bundles:
`/work/scratch/amunoz/jump-hub-closing-slides-20261019/`.

## Release restrictions unchanged

Both GitHub repositories and Overleaf remain private. The PDF is a local preview,
not a released artifact. The slides QR target is intentionally unavailable to a
public audience until final-slide/PDF approval and separate visibility approval.
No PDF upload, visibility change, or Overleaf comment resolution is authorized by
this source publication. The legacy unowned `main.tex` remains untouched.

## Follow-up reference cleanup

The presenter then requested removal of the cp_measure speed-benchmark link and
the `Data formats: Parquet, Zarr, JPEG XL` bullet from References. The cp_measure
paper and code references remain. Direct Overleaf edits through `7a02bcab`
(12:50 UTC) are ported into Org: revised tools/AI wording, cp_measure integration
and fastest/>2x CellProfiler bullets, named application collaborators, removal
of the application footer, and removal/commenting of Trackastra/nahual references.
These are presenter-authored changes; the performance statement is not
independently validated by this cleanup, and the historical 28.07x intensity-kernel
comparison does not establish it. The QR slide remains unchanged from the
validated two-code/shortlink version. Publication is still paused while live
editing continues; no owned-file restoration or new live export has occurred.
