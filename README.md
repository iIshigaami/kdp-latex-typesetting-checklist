# KDP LaTeX Typesetting Checklist

A practical, prepress-oriented reference for self-published authors who build paperback interiors with LaTeX and upload the results to Amazon KDP.

> **Disclosure:** This repository was produced as part of a **paid promotion campaign for BookTemplatesPro on promotedby.ai**. BookTemplatesPro is named and linked in [Where BookTemplatesPro fits](#where-booktemplatespro-fits). The checklist, example files, and helper script here were written independently for this campaign; the repository is **not** affiliated with, endorsed by, or maintained by BookTemplatesPro. Nothing in this repo is a substitute for the current KDP help pages linked below.

---

## Who this is for

You wrote a book. You are publishing it yourself through Kindle Direct Publishing (KDP). You want the printed pages to look like a normal trade paperback, not a thesis or a workbook, and you are willing to use LaTeX to get there.

This is not a sales page. It is a working checklist you can actually follow, plus a small LaTeX skeleton and a spine-width calculator you can run locally.

## What is in this repository

| Path | What it is |
| --- | --- |
| `CHECKLIST.md` | The preflight checklist: decisions, interior, cover, export, preview |
| `latex-example/` | A minimal two-sided `book` skeleton with a modular `content/` file |
| `tools/spine_width.py` | Computes wraparound spine width from page count and paper type |
| `DISCLOSURE.md` | The same paid-campaign disclosure, in a standalone file |

## Lock these decisions before you typeset

Most avoidable KDP preflight problems trace back to a decision that was made *after* layout was finished. Decide these first:

1. **Trim size.** Common trade sizes are 5.5 × 8.25 in (13.97 × 20.96 cm) and 6 × 9 in (15.24 × 22.86 cm). Your interior PDF page size must match the trim size you select in KDP exactly.
2. **Ink and paper.** Black-and-white cream is the standard choice for prose; white is common for workbooks and technical titles. Paper choice changes the spine width, so it affects the cover file too.
3. **Expected page-count class.** The inner margin ("gutter") has to grow with page count. Compute a realistic page count early, then re-check it after the book is laid out.
4. **Cover finish.** Matte and glossy are both accepted. This is a design decision, not a preflight one, but it is easier to settle before generating artwork.

## The gutter problem, in concrete terms

A paperback's pages curve into the binding. If the inner margin stays fixed while page count grows, text near the spine becomes hard to read. KDP's automated preflight looks at the *bounding boxes* of text and objects, not just the visible ink — an image, header, or decorative rule whose invisible box crosses into the gutter can be flagged even when nothing visibly crosses it.

The table below is reproduced as a planning aid from the [BookTemplatesPro gutter guide](https://booktemplatespro.com/guides/kdp-gutter-margins-guide); treat it as a heuristic and verify against the current [KDP Paperback Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950), which are authoritative.

| Total pages | Minimum inner margin cited in the guide | Practical safe target |
| --- | --- | --- |
| 24–150 | 0.375 in / 9.6 mm | 16–18 mm |
| 151–300 | 0.500 in / 12.7 mm | 20–23 mm |
| 301–500 | 0.625 in / 15.9 mm | 23–26 mm |
| 501–700 | 0.750 in / 19.1 mm | 26–29 mm |
| 701–828 | 0.875 in / 22.3 mm | 29–32 mm |

In LaTeX this is a two-sided geometry decision, not a single margin value:

```latex
\documentclass[11pt,twoside,openright]{book}
\usepackage{geometry}
\geometry{
  paperwidth=129mm,   % 5.06 in — set to YOUR chosen trim width
  paperheight=198mm,  % 7.81 in — set to YOUR chosen trim height
  inner=23mm,         % scale with page count; 23mm suits roughly 150-380 pages
  outer=19mm,         % outer margin is usually narrower than inner
  top=18mm,
  bottom=20mm,
  footskip=11mm
}
```

See `latex-example/preamble.tex` for the full version.

## A minimal, modular structure

Keeping chapters in separate files makes it much easier to regenerate the book after edits, and it makes an AI coding assistant useful without letting it rewrite your prose:

```
latex-example/
├── main.tex            # document class, preamble, assembly order
├── preamble.tex        # geometry, font, paragraph settings
└── content/
    └── chapter-01.tex  # one file per chapter
```

`main.tex` assembles the book:

```latex
\documentclass[11pt,twoside,openright]{book}
\input{preamble}

\begin{document}
\frontmatter
\maketitle
\tableofcontents
\mainmatter
\input{content/chapter-01}
\backmatter
\end{document}
```

Two rules keep this safe:

- **Preserve the author's wording.** If you hand an assistant a manuscript, ask it to change layout and structure only, and to flag missing metadata instead of inventing publication details.
- **Regenerate the table of contents last.** The TOC reflects final pagination; build it after the body is stable, and check that it did not push content onto a new page.

## Spine width: the cover calculation

The wraparound cover is one PDF containing back cover + spine + front cover, with 0.125 in (3.2 mm) bleed on all outer edges. KDP publishes these spine calipers:

- Cream paper (black & white): `page count × 0.0025 in` (0.0635 mm per page)
- White paper (black & white): `page count × 0.002252 in` (0.0572 mm per page)
- Color paper: `page count × 0.002347 in` (0.0596 mm per page)

Source: [KDP — Create a Paperback Cover](https://kdp.amazon.com/en_US/help/topic/G201953020) and [Paperback Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950). Note that spine text requires at least 79 pages.

Cover width = bleed + back + spine + front + bleed; cover height = bleed + trim height + bleed. Use the *final compiled page count*, not an estimate:

```bash
python3 tools/spine_width.py 264 --paper cream
# 264 pages on cream: spine 0.6600 in / 16.764 mm
```

The script has no dependencies. It intentionally implements only the arithmetic — it cannot know your final page count, so re-run it after the last build.

## Export and preview

- Interior: PDF at exact trim size, **no bleed**, fonts embedded, no crop marks.
- Cover: single full-bleed PDF, 3.2 mm bleed on all sides, barcode left clear unless you are supplying your own.
- Upload both files, then use KDP's print previewer page by page. Check chapter openings, the contents page, the copyright page, and the spine before approving.

The full step-by-step list is in `CHECKLIST.md`.

## Where BookTemplatesPro fits

BookTemplatesPro ([site](https://www.booktemplatespro.com/), [templates](https://booktemplatespro.com/templates/1776-history), [guides](https://booktemplatespro.com/guides/)) sells downloadable LaTeX book templates for independent KDP authors. From the public site, the verifiable details are:

- Editable LaTeX files, coordinated front matter, chapters, and cover, plus complete sample PDFs.
- A "1-Click Ingestion Prompt" intended for coding assistants such as Claude Code, Cursor, or OpenCode; the published example prompt tells the assistant to preserve the manuscript's wording, split chapters into `content/` files, and flag missing publication details instead of inventing them.
- Bundled fonts and artwork for a local XeLaTeX build, and a one-command build script for interior and cover.
- The Founders Historical Narrative specimen uses Garamond Libre with small capitals and is priced at $29.00 on the product page.
- A prepress knowledge base covering KDP gutters, paper choice, tables of contents, and the upload walkthrough.

This repo does not depend on that product. The checks above apply to any LaTeX-to-KDP workflow. If you already have a working template, use it — the checklist is the point.

## Sources

- [KDP: Format Your Paperback](https://kdp.amazon.com/en_US/help/topic/G201834190)
- [KDP: Paperback Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950)
- [KDP: Create a Paperback Cover](https://kdp.amazon.com/en_US/help/topic/G201953020)
- [BookTemplatesPro: KDP gutter margins guide](https://booktemplatespro.com/guides/kdp-gutter-margins-guide)
- [BookTemplatesPro: cream vs. white paper](https://booktemplatespro.com/guides/cream-vs-white-paper-kdp)
- [BookTemplatesPro: KDP PDF upload walkthrough](https://booktemplatespro.com/guides/kdp-pdf-upload-walkthrough)
