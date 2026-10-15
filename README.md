# Sam Cheng's academic website

Live site: https://samcheng123.github.io/Cam/

A lightweight, responsive academic website inspired by the layout of
[Mayank Mittal's website](https://mayankm96.github.io/). The HTML, CSS and
JavaScript in this redesign are original; no theme runtime is required.

## Update content

- `_data/publications.json`: publications, authors, status, and verified links.
- `_data/activities.html`: education, experience, teaching, service, talks, mentorship, and honors.
- `scripts/build_site.py`: biography, news, selected papers, and shared page layout.
- `site-assets/CV_Sam_Cheng.pdf`: downloadable CV (October 2026 edition).
- `_data/figure-sources.json`: provenance for the six publication figures.
- `site-assets/site.css` and `site-assets/site.js`: styling and progressive enhancement.

After editing content, regenerate the committed pages:

```sh
python3 scripts/build_site.py
```

Commit source and generated HTML together. Publications remain readable without
JavaScript, which adds search, category filters, and the mobile menu. There are
no third-party fonts, analytics, or JavaScript dependencies.

## Preview

URLs include the GitHub project prefix `/Cam/`. From the directory containing
this `Cam` checkout, run:

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765/Cam/`.

## GitHub Pages

The Pages deployment serves the generated pages from `main`. `_config.yml` sets
the project URL and excludes the legacy Academic Pages template, example posts,
and unrelated example publications from deployment. Original files remain in
Git for recovery. No new build workflow or hosting provider is needed.

## Content provenance

The October 2026 refresh uses the owner's supplied CV. Publication venues and
review status follow that CV. Public records were used to repair incorrectly
mapped links and reconcile author lists. Manuscripts without a public link remain
listed without an invented link or date. The original portrait is preserved in
full. Figures come from the author's papers/project pages; website versions are
resized proportionally and compressed to WebP without cropping.
