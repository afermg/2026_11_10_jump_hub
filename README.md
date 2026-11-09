# JUMP Hub — 10 November 2026

Alán F. Muñoz's November 10 talk, adapted from the FASEB presentation. Nocodazole opens as an extreme image example, then blebbistatin's known contractility/cytokinesis effects motivate the main CellProfiler-only investigation. Published summary values and same-plate DMSO preview pairs have been checked; the full replicate/QC/segmentation analysis and backend forwarding still need rehearsal. Word2vec, representation background/comparison and the modern-tools overview are now extra slides. The earlier single-cell recording remains available as backup.

- [Overleaf editor](https://overleaf.quasimorphic.com/project/6af238ebaa6d5b0395871289) — root **slides.tex**, compiler **XeLaTeX**. Its current link-sharing setting was preserved.
- [Private GitHub repository](https://github.com/afermg/2026_11_10_jump_hub).
- [PDF preview](slides.pdf) — **42 pages**: main talk through the QR on PDF21, ten existing extra slides, then the eleven-step tutorial screenshot walkthrough on **PDF32–42**. Gray tutorial footers are hidden; images and interpretation captions remain.
- [Tutorial walkthrough source](tutorial-walkthrough.tex) and [interpretation notes](docs/tutorial-walkthrough.md). Original highlighted tutorial images are preserved unchanged; placement in the main talk will be decided later.
- [Agent demo runbook](demo/README.md), [copyable prompts](demo/prompts.md), [blebbistatin preflight code](demo/check_blebbistatin.py) and [saved results](demo/rehearsal-blebbistatin/). The [nocodazole reference](demo/nocodazole-reference.md) and earlier SLC2A2 artifacts remain available.
- Local checkout: `/home/amunoz/Documents/broad/drafts/slides/2026_11_10_jump_hub`.

## Editing and synchronization

`slides.tex` is the Overleaf entry point. `slides.org` retains the editable Org source and extensive presenter notes; keep both aligned when changing content. Both include `tutorial-walkthrough.tex` for the temporary end-of-deck screenshot sequence, so edit those frames there. `main.tex` is a fallback that inputs `slides.tex`.

This deck is **independent** of the original FASEB repository/project and its Org publishing timer. There is **no automatic synchronization** for this new deck. Fetch both remotes before editing and preserve direct author changes. Do not regenerate TeX from stale Org over newer Overleaf wording.

```sh
git fetch origin main
git fetch oppy-overleaf master
git status --short
git log --oneline --left-right HEAD...oppy-overleaf/master
```

**Presenter preference (9 November 2026): push requested slide updates to Overleaf by default after building, validating and committing them, unless explicitly asked for a local-only preview.** This is authorization for the requested deck edits, not permission to overwrite concurrent author changes, alter project sharing, or submit anything to a venue. No background synchronization service is implied.

Reconcile upstream changes first; stop on substantive conflicts. Publish without force and verify local HEAD equals the freshly fetched live Overleaf branch:

```sh
git push oppy-overleaf HEAD:master
git fetch oppy-overleaf master
test "$(git rev-parse HEAD)" = "$(git rev-parse oppy-overleaf/master)"
```

The GitHub mirror can be synchronized separately with `git push origin HEAD:main`.

Keep GitHub private unless explicitly approved otherwise; preserve the presenter's Overleaf sharing settings. The closing **Slides QR and link intentionally still point to the public FASEB PDF**, not this new draft. Replace them together only after deciding how to distribute the new talk. The inherited demo recording and JUMP Hub links are unchanged.

## Build

Requires XeLaTeX, latexmk, moloch and Fira Sans (TeX Live full).

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build slides.tex
# Or:
nix shell nixpkgs#texliveFull --command latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build slides.tex
```

Review `build/slides.pdf`, then copy it to `slides.pdf` and commit the snapshot. Overleaf compilation does not update the GitHub PDF automatically. Do not apply the old FASEB 25-page truncation unless requested.

## Provenance and scope

Source: [FASEB deck](https://github.com/afermg/2026_10_21_faseb_jump_hub), exact commit `abdd682d172d44a7f3b5d514328dd37bc8b4bfab`. All tracked source assets were copied unchanged. The original repository and Overleaf project were not modified.

Most of `docs/` is a historical copy of the FASEB provenance, speaker notes, timing, demo instructions and operations records from `/work/users/amunoz/projects/org-overleaf-sync/docs`. Those inherited files describe the **October deck**, not new November validations or active automation. The newly added `tutorial-walkthrough.md` and `tutorial-screenshots-provenance.json` document the November screenshot addition. **Do not follow its old project-binding or publishing commands for this deck.** Use this README for the new workflow.

The nocodazole and blebbistatin preflights reproduce published summary-table values, with URLs and input hashes in their saved provenance. Nocodazole's annotation-defined peers are retained as reference evidence; blebbistatin's top matches are not relabeled as mechanistic peers. Two deterministic image/control pairs were visually reviewed and added without pixel modification; source URLs/hashes and limitations are recorded separately. No full replicate-level analysis, peer enrichment, dose/time alignment or end-to-end live backend rehearsal has been completed. Existing attribution and third-party terms remain; no new blanket license is granted. The inherited cp_measure speed claim and other date-sensitive content can be revisited during revision.

Validation: local XeLaTeX build and QPDF checks; native Overleaf compilation is a separate gate. Browser preview rendering is not implied by a Git push. Both compound preflights were executed against cached inputs; saved outputs and preview hashes are recorded. Historical SLC2A2 query tests are retained. Publish validated slide edits to Overleaf by default as specified above; report Git publication separately from native Overleaf compilation and browser rendering.
