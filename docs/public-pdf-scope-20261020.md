# Public PDF ends at the QR slide

The presenter requested removing the UMAP reference link and excluding all slides after the QR from the published PDF,while keeping them in Overleaf.

- Remove only the UMAP References entry;retain all UMAP figures,methodological notes and other links.
- Keep the full Overleaf deck at28pages,including the three additional slides26–28.
- Derive the public25-page PDF from the validated full build,ending at the unchanged QR page25. Do not truncate or hide the additional slides in the canonical Org/Overleaf source.
- Preserve every retained page's rendering,text and hyperlink annotations exactly. Remove excluded-page bookmarks and unreferenced objects when saving the derived PDF.
- The repository's root slides.pdf is the public/main version. Source files retain the full deck for reproducibility;this is not a Git-history removal request. Prior public PDF versions remain in history.
- The local delivery retains slides.pdf (public,25pages) and slides-full.pdf (full,28pages). page-map.json describes the full deck;public-page-map.json describes the public PDF.
- References24 now has39distinct URLs;UMAP is intentionally excluded at the presenter's request. All retained URL targets were checked in the preceding release;verify their annotations remain in the new PDF.

No scientific analysis,figure edits,repository visibility change,comment-state modification or Mac transfer. Main narration remains1380seconds. The Slides QR URL remains unchanged.
