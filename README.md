# Longbin Lai — personal website

A custom, responsive HTML5/CSS3 website. No Hugo, theme, JavaScript framework, or client-side content dependency. A small Python build step converts the retained Markdown content into static HTML.

## Local preview

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-site.txt
python scripts/build_site.py
python -m http.server 8000 --directory dist
```

Open http://localhost:8000. Edit `web/site.css` for design, `web/site.js` for publication search, and `scripts/build_site.py` for page composition. Rebuild after changes.

## Content

The original `content/` files, citations, bundled images, and `static/files/` documents remain the source of truth. Publications, projects, posts, talks, courses, and slides get static detail pages. Existing publication/post/project paths are retained. The homepage features NeuG with official links to https://neug.io/ and https://github.com/alibaba/neug. Biography and affiliation are retained from the existing profile; review them and the CV for freshness before launch.

Old Hugo configuration and the Academic submodule remain for reference only and are not used by the build.

## GitHub Pages deployment

1. Use a repository named **longbinlai.github.io** under **longbinlai**. Check whether it already exists before creating or renaming anything.
2. Push this source to that repository's `main` or `master` branch.
3. In Settings → Pages, select **GitHub Actions** as the build source.
4. The included `.github/workflows/pages.yml` builds `dist/` and deploys it to https://longbinlai.github.io/.
5. Keep the Pages custom-domain field empty. No CNAME file is generated; `lai.me` is intentionally separate.
6. Verify the new site, PDF downloads, and old bookmarked paths before changing the existing Netlify custom-domain binding or DNS. The included Netlify configuration supports the new build during transition; it does not change DNS or domain settings.

The build uses root-relative links for the user-site domain, not a `/academic-longbin/` project subdirectory. To deploy under a different base path, adapt URLs first.

## Language and appearance

English pages use the original paths; Chinese pages use `/zh/`. The header switches between corresponding pages and remembers the selected language. Chinese translations cover the interface, homepage, biography, and project summaries. Formal publication titles, abstracts, and downloadable documents retain their source language. Articles use separate translated Markdown bodies. Edit `scripts/translations.py` to maintain Chinese copy.

The appearance button switches between monochrome light and dark palettes. It follows the system until the visitor chooses a mode; the choice persists locally. Portrait images retain their original colors.

## Maintaining talks

The `/talk/` and `/zh/talk/` archives collect real entries from `content/talk/<slug>/index.md` only. The Academic example is excluded. The homepage has no talk cards or slide callout; use the Talks navigation link.

To add a talk, create a Markdown file with YAML front matter containing `title`, optional `date` (actual talk date), `summary`, and `url_slides`, `url_video`, or `url_pdf`. Add details below the front matter. When no date is known, omit it. Publication-linked slides remain in the publication archive and are not included in Talks. Add Chinese interface or summary translations in `scripts/translations.py` as needed.

## Article translations

Place a Chinese translation next to an article as `content/post/<slug>/index.zh.md`, with a `title` field in YAML front matter and the full translated Markdown body. An optional `index.en.md` provides the English version when the original is Chinese. The build automatically translates article headings on the homepage and archive and switches full bodies at the corresponding English and `/zh/` URLs. Relative images continue to use the original shared assets. All three existing posts have bilingual versions; original `index.md` files remain preserved.

## Social contact section

Edit `content/social.json` to update the X profile and Xiaohongshu QR asset. The homepage uses social links instead of a public mailto link. LinkedIn is omitted until a confirmed profile URL is available. The supplied QR image is preserved unchanged; the card displays its code area with CSS, and the dialog lets visitors enlarge or save the original image. Both languages and appearance modes are supported.
