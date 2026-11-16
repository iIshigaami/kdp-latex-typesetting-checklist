# Preflight checklist: LaTeX → KDP paperback

Print this or copy it into your notes. Mark items only after you have checked the compiled PDF, not the source.

**Disclosure:** produced as part of a paid BookTemplatesPro campaign on promotedby.ai. Independent checklist; see [DISCLOSURE.md](DISCLOSURE.md). Verify all numeric limits against current KDP help.

## 1. Locked decisions

- [ ] Trim size chosen and written down (e.g. 5.5 × 8.25 in / 13.97 × 20.96 cm).
- [ ] Ink and paper chosen (black & white cream vs. white; color if applicable).
- [ ] Realistic final page count estimated, then re-checked after layout.
- [ ] Cover finish chosen (matte or glossy).
- [ ] Same trim size configured in LaTeX geometry and in the KDP print-options screen.

## 2. Interior PDF (`main.pdf`)

- [ ] `\documentclass[twoside,openright]{book}` (or equivalent two-sided setup).
- [ ] Geometry uses `inner` larger than `outer`; inner margin scaled to the page-count class.
- [ ] No object bounding box — text, image, header, rule — crosses the inner gutter. Check the page *before* visible ink does.
- [ ] PDF page size equals trim size exactly; **no bleed** on interior pages.
- [ ] All fonts embedded; no missing glyphs for punctuation, accents, or italics.
- [ ] Paragraph breaks preserved; no accidental double spaces or hard-wrapped lines from the manuscript.
- [ ] Widows and orphans controlled; no single line stranded at a chapter break.
- [ ] Chapter openings start on the correct page (`openright`); blank verso pages are intentionally blank, not accidental.
- [ ] Running heads and folios consistent; folios on the outer edge.
- [ ] Front matter uses roman numerals, body uses arabic, if that is the chosen convention.
- [ ] Table of contents regenerated after the body is final, then re-checked for pagination shifts.
- [ ] Copyright page, ISBN, and imprint details present and correct — missing details flagged, never invented.
- [ ] Cross-references, notes, index, and bibliography resolve; no `??` placeholders.
- [ ] Chapter order and file assembly order in `main.tex` match the intended book.

## 3. Cover PDF (`cover.pdf`)

- [ ] Spine width recomputed from the **final** page count using the correct paper caliper:
  - cream `pages × 0.0025 in`, white `pages × 0.002252 in`, color `pages × 0.002347 in`.
  - `python3 tools/spine_width.py <pages> --paper cream`
- [ ] Spine text only if the book has at least 79 pages.
- [ ] Full-bleed PDF: 0.125 in / 3.2 mm bleed on all outer edges; bottom bleed no more than 3.2 mm.
- [ ] Cover width = bleed + back + spine + front + bleed; height = bleed + trim height + bleed.
- [ ] Back-cover barcode area left clear, unless supplying a vector barcode yourself.
- [ ] Title, subtitle, author name, and publisher checked against the interior.
- [ ] Fonts embedded in the cover PDF too.

## 4. Export

- [ ] Interior and cover are two separate PDFs.
- [ ] No crop marks, no printer's marks, no annotations.
- [ ] File names are plain (`main.pdf`, `cover.pdf`).
- [ ] Stored copy of source + build script kept outside the upload folder.

## 5. KDP upload and preview

- [ ] Print options match the LaTeX geometry: trim, paper, ink, finish.
- [ ] Bleed set to **No Bleed** for the interior; cover uploaded as a print-ready PDF.
- [ ] Barcode checkbox matches the cover file (own barcode vs. KDP-generated).
- [ ] KDP print previewer walked page by page: gutter text, chapter openings, TOC, copyright, spine.
- [ ] Any preflight rejection message read literally — "text or elements outside the margins" usually means an object bounding box, not just visible glyphs.

## Authoritative references

- [KDP: Format Your Paperback](https://kdp.amazon.com/en_US/help/topic/G201834190)
- [KDP: Paperback Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950)
- [KDP: Create a Paperback Cover](https://kdp.amazon.com/en_US/help/topic/G201953020)
