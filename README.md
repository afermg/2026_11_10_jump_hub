# JUMP Hub — 10 November 2026

Starter for Alán F. Muñoz's November 10 talk, adapted from the FASEB presentation. The original scientific content, figures, references and additional slides are unchanged. Only the date and obsolete FASEB subtitle have been updated; venue, duration and further title/content changes await discussion.

- [Private Overleaf editor](https://overleaf.quasimorphic.com/project/6af238ebaa6d5b0395871289) — root **slides.tex**, compiler **XeLaTeX**.
- [Private GitHub repository](https://github.com/afermg/2026_11_10_jump_hub).
- [PDF preview](slides.pdf) — all **28 pages**, including three additional slides after the QR slide. The FASEB public PDF contained only pages 1–25.
- Local checkout: `/home/amunoz/Documents/broad/drafts/slides/2026_11_10_jump_hub`.

## Editing and synchronization

`slides.tex` is the Overleaf entry point. `slides.org` retains the editable Org source and extensive presenter notes; keep both aligned when changing content. `main.tex` is a fallback that inputs `slides.tex`.

This deck is **independent** of the original FASEB repository/project and its Org publishing timer. There is **no automatic synchronization** for this new deck. Fetch both remotes before editing and preserve direct author changes. Do not regenerate TeX from stale Org over newer Overleaf wording.

```sh
git fetch origin main
git fetch oppy-overleaf master
git status --short
git log --oneline --left-right HEAD...oppy-overleaf/master
```

Reconcile upstream changes first; stop on substantive conflicts. After reviewing and committing focused changes, publish without force:

```sh
git push origin HEAD:main
git push oppy-overleaf HEAD:master
```

Keep both destinations private unless explicitly approved otherwise. The closing **Slides QR and link intentionally still point to the public FASEB PDF**, not this private draft. Replace them together only after deciding how to distribute the new talk. The inherited demo recording and JUMP Hub links are unchanged.

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

`docs/` is a historical copy of the FASEB provenance, speaker notes, timing, demo instructions and operations records from `/work/users/amunoz/projects/org-overleaf-sync/docs`. These describe the **October deck**, not new November validations or active automation. **Do not follow its old project-binding or publishing commands for this deck.** Use this README for the new workflow.

No scientific analyses or quantitative updates were performed during setup. Existing illustrative-data qualifications, attribution and third-party terms remain; no new blanket license is granted. The inherited cp_measure speed claim and other date-sensitive content can be revisited during revision.

Validation: local XeLaTeX build (28 pages) and QPDF checks; native Overleaf compile is checked separately during setup. Browser preview rendering is not implied by a Git push.
