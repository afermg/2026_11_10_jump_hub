**Current playback cue:PDF16 / visible15;returnPDF17.** The AI workflow statement, example prompt and validation sentence now sit beside the first demo screenshot onPDF16,not on the tools slide. The MP4 and screenshot bytes and playback behavior are unchanged. Older revision notes below are historical where they give a different page number.

# Offline playback and fallback

The presentation bundle contains:

- `slides.pdf` — 29 pages: 26 main-talk pages, then 3 additional. Word2vec/cells/JUMP stay5/6/7; tutorials are10, Modern tools16, AI17, demo18–19, Applications21 and MisLocus22. Main talk ends with References25 and QR24. JUMP-lite is27, Nahual28, and the combined seven-panel PLK1/negative-control figure29. Reality check is removed; MYT1 is excluded. Six DL panels use UMAP; Harmony-corrected CellProfiler uses PCA. The delivery manifest identifies the verified publication.
- `jump-cell-interactivity.mp4` — local prerecorded demonstration, 23.16 seconds.
- `presenter-notes.md` — 23-minute pacing and narration cues.
- `README.md` and `manifest.json` — playback instructions and file provenance.

The video is a **companion file**, not embedded in the PDF or hosted by Overleaf.
The Overleaf project receives the slide source and the two PNG fallback stills.
Keep the PDF and video on the presentation computer; playback needs no network,
marimo server, browser, or analysis environment.

## Public recording on Zenodo

The same MP4 is publicly available under **CC BY 4.0**:
<https://doi.org/10.5281/zenodo.23462248>.
Record: <https://zenodo.org/records/23462248>.
Creator: **Alán F. Muñoz, Carpenter-Shen Lab, Purdue University**.

The snapshot images on PDF pages **18 and 19** open this recording. The
presenter removed the separate demo-text link from the second still. The main-talk closing QR slide is page **26**, with the two
unchanged JUMP Hub and Slides codes and no separate recording link. Prefer
offline playback on stage.

The public record contains **only `jump-cell-interactivity.mp4`**. Anonymous
download and DOI resolution were verified; its SHA-256 is
`1085f74b56edb0d6006d8f7d83af6a8a74907b4a30693988ce3004383e4599ca`.
The slide PDF, notebook source and dataset were not uploaded. Publishing this
video does not authorize the separate PDF upload or GitHub visibility change.

## On stage

Open the video in a local player before the talk and pause at the beginning.
At **PDF page 18** (visible slide number **17**), switch to the player and play
once at normal speed. Explain the linked views; optionally replay once. Return
to PDF page 19 for the second selection. Rehearse the window switch and projector
behavior on the actual presentation computer. If playback is unavailable, use
the two stills and continue without troubleshooting.

The video has no audio. H.264 and yuv420p were chosen for broad player support,
but playback on the actual conference computer still needs checking.

## Recording provenance

Source:
`/work/users/amunoz/datasets/jump_conference_talk_20261014/notebook-demo/jump-cell-interactivity.gif`

Source SHA-256:
`cd18e53f2d7b452510be7ae26c6b78f1fe30be94678553e1bfaeeace5057d71c`

The GIF records actual Firefox selections, channel changes and resets in the
existing single-cell notebook. It already includes captions, a cursor indicator
and held views. Conversion retains the 1270 × 990 frame size and 23.16-second
duration; it does not generate new results, synthesize actions, or retime events.
The output uses 579 frames at 25 fps, H.264, yuv420p, no audio, and faststart.

Recreate into a **new** output path (the command refuses to overwrite files):

```sh
ffmpeg -hide_banner -loglevel error -n \
  -i /work/users/amunoz/datasets/jump_conference_talk_20261014/notebook-demo/jump-cell-interactivity.gif \
  -an -c:v libx264 -crf 18 -pix_fmt yuv420p -r 25 -fps_mode cfr \
  -movflags +faststart /path/to/new/jump-cell-interactivity.mp4
```

The two slide stills use `recording/large-013.jpg` and `recording/small-013.jpg`.
For each, crop the UMAP panel at `[155,200,790,605]` and gallery at
`[810,210,1225,560]`; place them at `[0,0]` and `[655,10]` on a white
1070 × 405 canvas. This removes surrounding UI and lower text without changing
plot points, image pixels or source labels. It does not recreate the omitted
statistics. `docs/assets.json` records source and output hashes.

The scientific interpretation limits are retained in `docs/presenter-notes.md`
and the notebook's README, rather than added as slide caveats.
