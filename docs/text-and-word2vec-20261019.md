# Shorter slides and a word2vec bridge — 2026-10-19

Requested: reduce on-screen text, then add a word2vec example immediately before
the cell-vector comparison. The new deck has **25 pages: 22 main-talk pages and
three additional slides**. Main timing stays 1,380 seconds within a 25-minute slot.
The end sequence is Thank you 20 → References 21 → QR 22 → Nahual 23 → word2vec
24 → cell vectors 25. The detailed Nahual explanation remains hidden.

## Text reduction

Extractable alphabetic-word counts on main content pages 2–19 fall from **782 to
526 (32.7%)**. This includes headings, excludes numbers and unchanged raster or
outlined figure text, and does not claim that every visible word in the deck
was counted. Per-page counts and scope: `text-reduction-word-counts.json`.
The AI slide drops 81→34 words and the take-home slide 63→37; repeated clauses
and long procedural bullets are shortened. Main scientific caveats and fuller
spoken explanations remain in presenter notes.

The exact talk title/date/affiliation, numerical counts, collaborator credits,
five conclusions, existing scientific images, edited Mac workflow, live
JUMP-lite wording and presenter-authored Fastest/>2x CellProfiler bullet are
preserved. That speed comparison remains independently unvalidated. The nuclear
area recipe now separates feature-value ranking from checking perturbation
activity, avoiding a suggestion that the latter is per-feature significance.
Demo pages remain 13/14 and both QR payloads remain unchanged.

The user's follow-up on ORF biology prompted a methods check of Chandrasekaran
et al. (2025), DOI 10.1038/s41592-025-02753-9. The imaging experiment used
lentiviral ORF delivery, a 48-hour readout and no blasticidin selection. The
shortened card says gene overexpression (ORF); notes no longer imply transient
expression from assay duration. Overexpression does not guarantee increased
normal protein activity or uniform delivery. Earlier transient wording in
historical documents describes an imprecise prior revision, not this protocol.

## Word2vec and cell vectors

The new original vector schematic uses a country-capital analogy:
`v(Paris) − v(France) + v(Italy) ≈ v(Rome)`. It explicitly labels its invented
2D positions as **not a trained model output**. Individual learned coordinates
are not predefined concepts such as age/gender. Analogy behavior is approximate,
model-dependent and can reflect training-corpus biases. The linked method
reference is Mikolov et al. (2013), <https://arxiv.org/abs/1301.3781>.

The next slide is renamed **From words to cells: vectors for comparison** and
its figure subtitles are shorter. Cell positions, colors, cartoon geometry,
mitochondrial patterns and scientific limitations are unchanged. The transition
is numerical representation, not a claim that word2vec was used on these cells.
Both examples are additional slides, not new measured results or main narration.
SVGs/generators are retained; PDFs are vector figure assets with no raster images.
The France label was moved above its point to avoid a crossing vector line.

## Validation and publication boundaries

Use an isolated preview, inspect the dense main slides and both vector examples,
check 25 pages/1,380 seconds, QR destinations, demo links and zero final-pass
compile/box/glyph warnings. Verify original image bytes and the edited Mac SVG
are unchanged. Existing title, closing frames, References, short JUMP-lite and
Nahual frame remain unchanged; intended main text reductions are documented.

Re-fetch live Overleaf immediately before guarded integration. Preserve newer
author edits, unowned `main.tex`, hidden slides and comment state. Use the
established publisher without force pushes or baseline changes. Add only a
specific source-artwork PDF exception in the private mirror. The presentation
PDF remains local and the repository stays private pending separate approvals.

The concurrent manuscript-bibliography review is a separate local reading pack;
no private manuscript content or announcements changes belong to this revision.
