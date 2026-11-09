# Tools and final QR update — 19 October 2026

## Requested changes

- Add marimo (reactive notebooks/apps) and uv (Python packages, environments and
  lockfiles) to “Modern tools make image analysis more accessible”, PDF page 15.
- Add Nahual on page 16: try alternative image-analysis models through separate
  environments from one Python workflow. Examples: DINOv2/DINOv3, OpenPhenom,
  MorphEm, Cellpose, StarDist and Trackastra.
- Remove the historical cp_measure speed-benchmark citation and retain the
  requested Data formats reference cleanup.
- End with Thank you (21), References (22), then JUMP Hub and slides (23).
  Preserve two 40-mm QR codes, their destinations and `broad.io/jump`.
- Retain the 23-minute plan: reassign 15 seconds each from the toolbox,
  cp_measure and JUMP-lite segments to the new 45-second Nahual segment.

## Source and scope

The latest direct Overleaf content was inspected through
`25527fbb59c29e59235b04e7608e6aca414fad76`. Canonical starting revision:
`04f2dc3fa30264ba3fbe86c26b6e431c582bd5a4`.
Preserve the revised toolbox wording, tool/cp_measure/JUMP-lite ordering,
Minh Doan/GSK and Tim Treis/Helmholtz-Munich credits, and removed application
footer. Nahual's newly requested slide restores its reference intentionally.

The Nahual catalogue was verified from README.md at
`56aa3fe1c36fe891a933a76d05db6fca2c3673f1`:
<https://github.com/afermg/nahual/blob/56aa3fe1c36fe891a933a76d05db6fca2c3673f1/README.md>.
Model examples are documented wrappers, not new model implementations or runtime
benchmark results. Most neural wrappers use GPUs; input/output conventions,
preprocessing, licences and availability of weights remain model-specific.

marimo and uv descriptions were checked against their official READMEs:
<https://github.com/marimo-team/marimo> and <https://github.com/astral-sh/uv>.
Their role in reducing Python workflow friction is presenter experience, not a
claim of solving every reproducibility or dependency problem.

The presenter-authored Fastest / >2x CellProfiler bullet is preserved, not
independently validated. The historical 28.07x result compared intensity kernels
between cp_measure versions and cannot substantiate the CellProfiler claim.

## Validation and release holds

Evidence, preview, comparison script and validation results:
`/work/users/amunoz/datasets/jump_conference_talk_20261014/tools-update.nC5Wv6/`.
Validation covers 23 PDF pages, 1,380 seconds, unchanged unrelated frames/assets,
no benchmark URL, demo links only on pages 13/14, both final QR payloads, new
model/tool text and final-pass compile diagnostics. New slides and closing pages
are also visually inspected before publication.

The delegated page-2 SVG is a separate asset proposal, not substituted into the
deck by this update. Scientific imagery remains unchanged. The independent
`docs/closing-slide-update-20261019.md` is not modified.

The distribution repository stays private. No slide PDF is uploaded or committed;
PDF upload and public visibility each require separate explicit approval.
Only the previously approved MP4 is public on Zenodo. No Overleaf comments are
modified. Live edits must still be fetched and guarded immediately before a
normal reconciliation commit and established-publisher sync.
