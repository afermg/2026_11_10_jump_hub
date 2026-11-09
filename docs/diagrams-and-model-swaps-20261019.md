# Vector illustrations and model swaps — 19 October 2026

## Slide update

- PDF page 5: same illustrative cell examples shown with named cell-area/
  mitochondrial-fragmentation measurements and abstract learned coordinates.
  Four cells combine non-senescent/senescent examples with interconnected/
  fragmented mitochondria. No measured results, diagnostic rule, mitochondrial
  causality or direct organelle-contact evidence is asserted.
- PDF page 17: the requested simple Nahual slide shows only model names, task
  groups, swap arrows and the message “Swap models. Keep your workflow.”
  Swaps are within a task and may require model-specific input/output handling;
  hidden technical notes do not imply universally interchangeable outputs.
- The prior longer Nahual slide remains `:noexport:` to preserve the presenter's
  direct Overleaf decision to hide it. The later request adds a simpler slide,
  rather than silently restoring the old explanation.
- Preserve the live JUMP-lite wording: “Use our compressed images to contrast
  your own vs the state-of-the-art.”
- Deck: 24 pages; demo playback 14 → 15, toolbox 16, applications 20, take-homes
  21, gratitude 22, References 23 and final two-code QR page 24.
- Plan: 23 minutes. New diagram 45 s; simplified Nahual 15 s rather than 45 s;
  second-selection narration 60 s rather than 75 s.

Starting canonical commit: `a2100d5543c2e171fc2c9fdf86ea4069d833142d`.
Live content preserved through `bf0e603de8df7ae4e0d0cd71687a0b082c2b7f37`.
A fresh pre-publication guard is still required. No baseline reset or force push.

## Diagram sources

`deck/assets/vector-interpretability.svg` is entirely vector, including text.
`deck/assets/vector-interpretability.pdf` is the consumed vector figure asset,
not the presentation PDF. The standalone cell-vector and learned-vector SVGs,
source reference, deterministic generator and explanation are in
`figures/vector-interpretability/`.

The learned example uses abstract coordinates; it is not a computed model output
or fitted dimensionality reduction. There need not be a fixed one-to-one
biological meaning for each coordinate. This does not claim that learned models
can never be interpreted, or that engineered features are mechanistic evidence.

Model catalogue: Nahual README at
`56aa3fe1c36fe891a933a76d05db6fca2c3673f1`, which documents DINOv2, DINOv3,
OpenPhenom, MorphEm, Cellpose, StarDist, Trackastra and Ultrack wrappers.
No model runtime benchmark was performed for this slide.

## Corrected editable Cell Painting illustration

The presenter clarified that the requested editable SVG is the wide workflow
`cell-painting.png`, not the microscopy montage `cell-painting-channels.png`.
A resumed worker produced a separate genuinely vector reconstruction:
`/work/users/amunoz/datasets/jump_conference_talk_20261014/editable-page2-svg/cell-painting-overview/cell-painting-editable.svg`.
Its labels, organelle callouts, arrows and schematic components are editable;
its original raster is only on a hidden reference layer. Parent inspected the
preview/tests and independently reran all six passing tests. This is a redrawing,
not recovered original vector artwork or measured heatmap/graph data.

Original published schematic identified as Chandrasekaran et al. (2021),
Nature Reviews Drug Discovery, Figure 1a, DOI 10.1038/s41573-020-00117-w.
The existing original deck image is not replaced without further approval.
The corrected SVG and helper SVGs were transferred with checksum verification
to the user's Mac for local editing; no public release is implied.

## Evidence and release holds

Validation, transfer hashes and publication records live under
`/work/users/amunoz/datasets/jump_conference_talk_20261014/helper-diagram.ySrp7G/`.
Existing scientific image bytes and unrelated frames remain unchanged. Validate
all live frames after removing commented-out frames, 24 pages, vector-only helper
asset, model labels, 1,380-second timing, QR payloads, new demo page links and
final compile diagnostics before publication.

The slide PDF stays local and the source mirror private; each release needs its
own explicit approval. A vector PDF figure asset is source artwork and is not
`slides.pdf`. No Overleaf comments are modified. Background organelle-feature
mining is independent and does not contribute unvalidated results to this deck.
