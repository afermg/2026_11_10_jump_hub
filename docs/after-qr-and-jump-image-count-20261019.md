# After-QR JUMP-lite and JUMP image count — 19 October 2026

The presenter requested moving JUMP-lite after QR and adding the JUMP image
numbers. This also incorporates the already-approved reality-check slide and
compression-only comparison, previously held while concurrent edits were resolved.

## Current order and content

- PDF 5: existing JUMP overview gains **~58.3 million single-channel TIFF images**.
  No new image-count slide is added; existing perturbation cards remain intact.
- PDF 18: existing four applications, including MisLocus, unchanged.
- PDF 19: approved reality check: batch effects, similarity versus mechanism,
  and experimental follow-up as the bottleneck.
- PDF 20/21/22/23: take-homes, gratitude, References and the main-talk closing QR.
- PDF 24: first additional slide, JUMP-lite **8.7 TB → 92 GB (~94× smaller)**,
  comparing the same image set. Native labels explicitly identify lossy JPEG XL.
- PDF 25/26/27: Nahual, word2vec and cell vectors; all remain additional material.

Total **27 pages, main 23 + additional 4**. Main narration remains **1,380 seconds**.
The old 75-second JUMP-lite narration is reassigned to framing/reality check
(30 seconds each) and applications (15 extra seconds). Toolbox remains one minute.
The video is unchanged; play at PDF 14 / visible 13, return to PDF 15.

## Number provenance

The full JUMP cpg0016 image-archive total is **58,267,491 TIFF files**, summed
from the 12 source rows of the public
[count table](https://github.com/jump-cellpainting/datasets/blob/016e865fa0691244e0860943e41c7d6a88ed2580/stats/cpg0016_source_images_tiff_count.csv)
at the same pinned revision as the perturbation metadata. This is the archive
count including controls, not cells, five-channel imaging sites or a QC-passing
profile subset. Source rows are not acquisition-center counts. The public
site-count table sums to 8,126,570 and does not reconcile via a five-channel
factor; no derived site count is shown. `jump-image-counts.json` records exact
rows, input hashes, URLs and sums. Only public metadata was used.

JUMP-lite's 8.7 TB original TIFF and 92.0 GB MQ JPEG XL sizes, and approximate
94-fold reduction, are stated in section 3.1 of
[arXiv:2608.07632v3](https://arxiv.org/abs/2608.07632v3).
The 115 TB full release would conflate subset selection and compression;
4.8 TB Zstd is already compressed. No quality/performance equivalence is claimed.
The old cropped paper panel stays in canonical history/assets, but is not consumed.

## Preservation and checks

Source starts from 3c03980, after the intervening owner-approved reconciliation;
live baseline is e564d550d9fba92af51d3e90b43007b0b6b5985b. Keep all current author
wording, including marimo dashboards, individual tools, plain take-home labels
and funding scoped to cp_measure/JUMP-lite. Twenty-two other live content frames
are unchanged after normalizing generated labels. The only other changes are
the overview count, its reference link, the JUMP-lite replacement/reorder and
new reality-check frame. All source image/vector bytes remain unchanged.

Validation covers page order, 27-page count, 1,380-second timing, source/asset
hashes, exact count aggregation, unchanged author frames, new reference link,
QR decoding, demo links and final compile warnings. Changed pages were visually
inspected. Evidence: `/work/users/amunoz/datasets/jump_conference_talk_20261014/jump-lite-after-qr.eljewL/`.

Publication uses fresh-fetch/baseline and Emacs guards, followed by the established
publisher. Unowned main.tex and Overleaf comments remain unchanged. The private
mirror omits the now-unused paper PNG but retains its three specific source-figure
PDF exceptions. Presentation slides.pdf stays unpushed and repository visibility
stays private until the two separate release approvals.
