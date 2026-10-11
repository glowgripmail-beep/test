---
name: documents-files-diagrams
description: "Create, read, edit and convert documents, files and diagrams: Word .docx/.dotx (templates, tracked changes, comments, images); PDF (extract text/tables, merge, split, rotate, watermark, encrypt/decrypt, extract images, OCR, fill forms, create); PowerPoint .pptx/.potx decks; spreadsheet files (.xlsx, .xlsm, .xltx, .csv, .tsv: formulas, formatting, financial models, cleaning messy data); creating or changing Google Docs, Sheets, Slides or Drive files via connectors (incl. docs.google.com links, follow-ups like 'add a tab'); editable shareable docs via the Claude Docs connector, the default for any document, report, proposal, resume, letter, contract, guide or SOP when no file format is named; and architecture, workflow, sequence, data-flow and lifecycle/state diagrams as interactive HTML (system architecture, API sequences, data pipelines, state machines, Mermaid, everyday plans/processes). Hebrew triggers: מסמך, וורד, PDF, מצגת, אקסל, גיליון, תרשים, דיאגרמה. Not for numeric charts or dashboards."
license: "Mixed. docx, pdf, pptx, xlsx parts: Proprietary, each part's LICENSE.txt has complete terms. archify part: MIT (archify/LICENSE; third-party marks in archify/THIRD_PARTY_NOTICES.md)."
---

# Documents, files and diagrams

This skill merges seven tool skills. Each one lives unchanged in its own folder, with its original instructions in `GUIDE.md` and all of its scripts, schemas, templates and assets at the same relative paths as before:

| Folder | Original skill | What it does |
|---|---|---|
| `docs/` | docs | Editable docs people share and comment on, through the Claude Docs connector |
| `docx/` | docx | Word documents and templates (.docx, .dotx) |
| `pdf/` | pdf | Anything with PDF files, including form filling |
| `pptx/` | pptx | PowerPoint decks and templates (.pptx, .potx) |
| `xlsx/` | xlsx | Spreadsheet files (.xlsx, .xlsm, .xltx, .csv, .tsv) |
| `google-workspace/` | google-workspace | Creating or changing Google Docs, Sheets and Slides through the Google connectors |
| `archify/` | archify | Architecture, workflow, sequence, data-flow and lifecycle diagrams as standalone HTML |

## Paths: "this skill's directory" now means the part folder

Every `GUIDE.md` says script paths are relative to "this skill's directory". That is now the part folder, not this top folder:

- docx: `docx/scripts/...` (e.g. `python <this skill>/docx/scripts/office/soffice.py ...`)
- pdf: `pdf/scripts/...`; `pdf/FORMS.md` and `pdf/REFERENCE.md` sit next to `pdf/GUIDE.md`
- pptx: `pptx/scripts/...`
- xlsx: `xlsx/scripts/recalc.py`, `xlsx/scripts/office/...`
- google-workspace: the references write the folder as `<skill>`; it is `<this skill>/google-workspace` (e.g. `python <this skill>/google-workspace/scripts/docs_index.py outline DOC.json`)
- archify: replace `bin/archify.mjs` with `<this skill>/archify/bin/archify.mjs` (absolute path, or relative to the working directory)

`docx/`, `pptx/` and `xlsx/` each carry their own identical copy of `scripts/office/` (validators, XSD schemas, `soffice.py`, helpers). The copies are kept on purpose so each part's relative paths keep working; do not deduplicate them.

Where a file says "the `docx` skill", "the `xlsx` skill" or "the `pptx` skill" (for example in `google-workspace/references/*.md`), that is now the `docx/`, `xlsx/` or `pptx/` part of this skill. "That format's skill" in the docs description means the matching part here.

## Which part to read

| Task | Read |
|---|---|
| A document, report, proposal, resume, cover letter, letter, contract, policy, form, template, worksheet, essay, handbook, guide, how-to, cheat sheet or SOP, with **no file format named** | `docs/GUIDE.md` (Claude Docs connector; its description has the full routing rule) |
| The user names Word/.docx/.dotx, wants tracked changes, or supplies a .docx/.dotx to change or use as a template | `docx/GUIDE.md` |
| Read, extract text/tables from, merge, split, rotate, watermark, encrypt/decrypt, OCR, or create a PDF | `pdf/GUIDE.md`, then `pdf/REFERENCE.md` for advanced features, pypdfium2, JavaScript libraries (pdf-lib, pdfjs-dist) and troubleshooting |
| Fill in a PDF form | `pdf/FORMS.md` (follow its steps in order) |
| Any .pptx/.potx as input or output; a PowerPoint file requested | `pptx/GUIDE.md` |
| A deck/slides/presentation with no file format named | A dedicated slide-deck artifact type or slides skill if the session offers one; otherwise `pptx/GUIDE.md` |
| A spreadsheet file is the primary input or output (.xlsx, .xlsm, .xltx, .csv, .tsv), incl. formulas, financial models, cleaning messy tabular files | `xlsx/GUIDE.md` |
| Create or change a Google Doc, Sheet or Slides file, a docs.google.com link with a change request, or a follow-up change to a Google file | `google-workspace/GUIDE.md`, then the reference for every app touched: `google-workspace/references/docs.md`, `sheets.md`, `slides.md`; for charts in a deck also `charts.md` |
| Architecture, infrastructure, cloud/security/network topology, workflows, API call sequences, request lifecycles, data pipelines, ETL/ELT, lineage, state machines, Mermaid conversion, or an everyday plan/process/back-and-forth/status as a diagram | `archify/GUIDE.md`, then the references it names (`archify/references/*.md`, `archify/schemas/*.json`, `archify/examples/*`, `archify/renderers/*/README.md`) |

Routing rules carried in the original descriptions (kept here so they are applied before opening a part):

- **docs is the default for any document**, named as a doc or not. A doc exports to Word, PDF, Markdown or Google Docs, so needing a file to send, attach, upload, submit or print is no reason to pick Word, and a file nobody asked for is a doc, not Word. A plan, comparison, summary or notes asked in chat stays in chat. A pasted claude.ai artifact link may be a doc: check with docs tools first. Word or another file format named, tracked changes wanted, or a .docx to change or use as a template → that format's part.
- **docx:** do NOT use for PDFs, spreadsheets, Google Docs, or coding unrelated to document generation.
- **pptx:** when the user asks for a deck, slides, a slide deck, or a presentation without naming a file format, default to a dedicated slide-deck artifact type or a separate slides skill if this session offers one.
- **xlsx:** the deliverable must be a spreadsheet file. Do NOT use when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.
- **google-workspace:** if the user asks for a doc, deck or spreadsheet without naming Google, or gives a Google file only as source material for something new, use Claude's own output type instead. Do NOT use for read-only questions about a Google file, or for Word, Excel, PowerPoint or PDF files.
- **archify:** not for numeric charts or dashboards (use the `data-analysis` skill or the `dataviz` system skill for those).

Several parts can apply to one task: for example, a designed Google Slides deck is built with `pptx/` and uploaded through `google-workspace/` (see `google-workspace/references/slides.md`, "Create"), and an .xlsx upload to Google Sheets is built with `xlsx/` (see `google-workspace/references/sheets.md`, "Create").

## Dependencies at a glance

- docx: `docx` (npm, preinstalled), `pandoc`, LibreOffice (`soffice`), `pdftoppm` (Poppler)
- pdf: `pypdf`, `pdfplumber`, `reportlab`, `pypdfium2`, `pytesseract` + `pdf2image` for OCR, poppler-utils, `qpdf`, `pdftk` (if available), ImageMagick for form-field crops
- pptx: `pptxgenjs` (npm, preinstalled), `markitdown[pptx]`, `Pillow`, `defusedxml`, `lxml`, LibreOffice, `pdftoppm`
- xlsx: `openpyxl`, `pandas`, `markitdown` (preinstalled), LibreOffice
- google-workspace: the Google Drive, Docs, Sheets and Slides connectors; Python for the helper scripts
- docs: the Claude Docs connector
- archify: `node` (>=18); no install needed inside the package (`node archify/bin/archify.mjs doctor` to diagnose)

## Conflicts between sources

These parts give different rules for similar situations. They are listed, not resolved; follow the part that matches the file type you are producing.

1. **Slide type sizes.**
   - pptx: slide title 36-44pt bold, section header 20-24pt bold, body 14-16pt, captions 10-12pt muted; floor of body 14pt, captions 10pt in a deck you create.
   - google-workspace (slides.md): slide title 32-40pt bold (at least about 1.75x the body), section header 24-28pt, body 16-18pt, captions 14pt, footnotes and source lines 10-12pt; only footnotes, source lines, the second line of a chart label, a chart's year row (11pt) and chart callouts (11-12pt) go below 14pt.
2. **Default slide background.**
   - pptx: when no background is specified, use white (`FFFFFF`) or the user's brand palette; "Dark backgrounds for title + conclusion slides, light for content ('sandwich' structure). Or commit to dark throughout for a premium feel." Its palette table includes cream tones (Forest & Moss `F5F5F5`, Berry & Cream `ECE2D0`).
   - google-workspace (slides.md): an off-white background with no warm tint (such as #FAFAFA) and near-black text, rather than pure white and pure black; do not default to a dark-blue background; cream/beige belongs only to the warm editorial look; a dark background suits the title slide and section dividers.
3. **Fonts on slides.**
   - pptx: prefer the "safe" list (Arial, Calibri, Cambria, Times New Roman, Courier New, Bookman Old Style, Century Schoolbook); Georgia, Trebuchet MS, Garamond and others are QA-unreliable; never default to Aptos.
   - google-workspace (slides.md): use Google fonts, such as Arial, Roboto, Lato, Montserrat, or Merriweather.
4. **Chart titles and legends on slides.**
   - pptx: default charts render bare, so set `showTitle` + `title`, `showValue: true`, and `showLegend: false` for a single series.
   - google-workspace (charts.md): the chart's own built-in title stays off; the label is a text box above the chart; no legend except where series names allow one; avoid pie/donut charts unless asked.
5. **Visual element on every slide.**
   - pptx: "Every slide needs a visual element — image, chart, icon, or shape. Text-only slides are forgettable."
   - google-workspace (slides.md): a "Big text" slide with one message and nothing else is a valid (rare) layout; "An image must carry information. A generic stock photo is worse than empty space."
6. **Title alignment.**
   - pptx: "Don't center body text — left-align paragraphs and lists; center only titles."
   - google-workspace (slides.md): title alignment follows the layout: centered on the title slide and section headers, left-aligned on content slides; a template's own title alignment always wins.
7. **Lookup and dynamic-array functions.**
   - xlsx: never use `XLOOKUP`, `XMATCH`, `SORT`, `FILTER`, `UNIQUE`, or `SEQUENCE` (the runtime's LibreOffice cannot evaluate them); use `INDEX`/`MATCH`.
   - google-workspace (sheets.md): Sheets supports `XLOOKUP`, `FILTER`, `UNIQUE`, and `SORT`, so the xlsx LibreOffice limits do not apply there (avoid Sheets-only functions if the file may go to Excel).
8. **Zero-denominator guard.**
   - xlsx: prefers Excel-2007-era functions including `IFERROR`; "guard denominators that can be zero".
   - google-workspace (sheets.md): guard with `=IF(C5=0,0,B5/C5)`; "Use `IF` here rather than `IFERROR`, which also hides a broken reference."
9. **Financial-model number formats (small differences).**
   - xlsx: currency `$#,##0` / `$#,##0;($#,##0);-`; multiples `0.0x`.
   - google-workspace (sheets.md): currency `$#,##0;($#,##0);"-"`; percentages `0.0%;(0.0%);"-"`; multiples `0.0"x"`.
10. **Render resolution for visual QA.** docx renders pages with `pdftoppm -jpeg -r 100`; pptx renders slides with `pdftoppm -jpeg -r 150`.
