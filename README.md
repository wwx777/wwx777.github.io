# Wanxing Wu — personal homepage

A standalone, original static website for Wanxing Wu. Built with semantic HTML, CSS and locally hosted assets. No framework, build step, analytics, or external font requests. A small progressive-enhancement script adds navigation state and restrained scroll reveals, with reduced-motion support.

## Files

- `index.html`: homepage content
- `assets/style.css`: responsive design
- `assets/site.js`: scroll navigation and motion
- `assets/portrait.jpg`: personal graduation portrait
- `cv.pdf` / `cv_cn.pdf`: current English / Chinese CV

Serve this directory with any static HTTP server for local preview. GitHub Pages serves the `main` branch from the repository root.

The seven original homepage sections retain their pre-redesign wording and links; the redesign changes presentation. Under-review venues are not named on the homepage.

This repository was initialized independently; it does not inherit another homepage's source or Git history.

## Blog status

The three research posts are in preparation. The Blog section and publication Blog placeholders are hidden, and the Blog navigation link is omitted until posts are ready. No earlier blog drafts are published. Reveal the section and add article links only after reviewing and publishing each post.

## CV editing and publishing

The canonical bilingual CV sources now live in this repository:

- `cv/Wanxing_Wu_CV_EN.tex` → `cv.pdf`
- `cv/Wanxing_Wu_CV_CN.tex` → `cv_cn.pdf`
- `cv/assets/` contains the required school logos.

On this Mac, the repository's pre-commit hook is enabled. When staged CV sources
change, it builds both PDFs and stages them in the same commit. A compilation
failure blocks the commit, so the website keeps the last successful PDFs.
Stage all CV source edits before committing. Website-only commits skip compilation.

```sh
# After cloning elsewhere, enable the hook once (requires Python 3 + MacTeX).
git config core.hooksPath .githooks
# Optional explicit build before previewing:
python3 scripts/build_cv.py
# Edit sources, then publish:
git add cv/
git commit -m "Update CV"
git push
```

Chinese typesetting uses the existing macOS Heiti SC font. The build requires
MacTeX and that font. GitHub Pages publishes the committed PDFs; it does not
compile LaTeX. Editing only a `.tex` file through GitHub's web editor bypasses
local hooks, so use the local checkout above or upload both generated PDFs.
Older Documents/resume files are retained as history; edit the sources here
for future updates. Existing `/cv.pdf` and `/cv_cn.pdf` URLs stay stable.

The footer displays the last publishing commit date. The local pre-commit hook
runs `scripts/update_date.py`, using Europe/Paris, and stages the updated date.
