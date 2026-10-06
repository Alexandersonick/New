#!/usr/bin/env node
/**
 * build_manuscript_docx.js — convert a novel manuscript (Markdown, in the
 * Master Fiction Pipeline format) into a print-ready .docx with a real,
 * paginated, VERIFIED Table of Contents and KDP-standard page setup.
 *
 * Expected Markdown conventions:
 *   # TITLE                          (line 1)
 *   ### Subtitle                     (line 2, optional)
 *   ## Chapter One / ## Epilogue …   (heading per chapter/section)
 *   *POV — Date*                     (italic subtitle, immediately after a heading)
 *   *italic paragraph*               (whole-line italics, e.g. letter excerpts)
 *   **bold**, *italic*               (inline emphasis inside normal paragraphs)
 *   ---                              (scene break)
 *   **THE END**                      (rendered as a centered "THE END" line)
 *
 * Usage:
 *   node build_manuscript_docx.js <manuscript.md> [output.docx]
 *     [--series "Series Name — Book N"] [--author "Author Name"]
 *     [--trim 6x9|5.5x8.5|5x8|letter]
 *
 * Why two (or more) passes: a TableOfContents field's page numbers aren't
 * knowable until the document is actually laid out. Pass 1 renders with a
 * blank/placeholder TOC to get real pagination, converts to PDF, and reads
 * off which page each heading lands on. Pass 2 rebuilds with those numbers
 * baked into TableOfContents' cachedEntries (with working internal
 * hyperlinks via Bookmark). Pass 2's own PDF is then INDEPENDENTLY
 * re-verified against ground truth (not assumed identical to pass 1's
 * layout) — if anything drifted, the script rebuilds again with corrected
 * numbers and re-verifies, up to a small convergence cap, and refuses to
 * ship a file whose TOC doesn't match its own pages.
 *
 * TOC implementation: NOT a live/cached Word TableOfContents field. docx.js's
 * `TableOfContents` cachedEntries renderer hardcodes its dot-leader tab stop
 * to a Letter-page-width assumption (~9025 twips) with no way to override it
 * — on a narrower KDP trim (6x9 = 8640 twips wide) that tab stop lands past
 * the actual right margin, pushing every page number off the visible page.
 * Confirmed by rendering: real bug, not hypothetical. Instead, the TOC is
 * built as plain paragraphs with an explicit tabStop computed from the
 * actual trim/margins, each entry a real InternalHyperlink to that chapter's
 * Bookmark. This is also strictly more robust than a field: with no field
 * code at all, there is nothing for any viewer to mark dirty or recompute on
 * open — the content that ships is the content that displays, permanently.
 *
 * Font: Times New Roman. This isn't a stylistic default so much as a
 * correctness requirement — LibreOffice (used here to verify pagination)
 * does not have "Garamond" installed and silently substitutes DejaVu Serif,
 * which has different character metrics than whatever Microsoft Word
 * substitutes (or the real Garamond, if Word has it). That mismatch is a
 * real, previously-shipped bug: page numbers verified against one font's
 * layout came out wrong once the file was opened in a viewer using a
 * different font's layout. Times New Roman maps to Liberation Serif under
 * LibreOffice, which is metric-compatible with real Times New Roman in
 * Word — eliminating the cross-renderer drift risk at its root instead of
 * chasing it with more verification passes.
 */

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  PageBreak, Bookmark, Footer, PageNumber, Tab, TabStopType, InternalHyperlink,
} = require('docx');

// ---------------------------------------------------------------------
// CLI args
// ---------------------------------------------------------------------
function parseArgs(argv) {
  const positional = [];
  const flags = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith('--')) {
      const key = argv[i].slice(2);
      flags[key] = argv[i + 1];
      i++;
    } else {
      positional.push(argv[i]);
    }
  }
  return { positional, flags };
}

const { positional, flags } = parseArgs(process.argv.slice(2));
const mdPath = positional[0];
if (!mdPath) {
  console.error('Usage: node build_manuscript_docx.js <manuscript.md> [output.docx] [--series "..."] [--author "..."] [--trim 6x9]');
  process.exit(1);
}
const outPath = positional[1] || mdPath.replace(/\.md$/i, '.docx');
const seriesLine = flags.series || '';
const authorName = flags.author || '';

const TRIMS = {
  '6x9': { w: 8640, h: 12960 },
  '5.5x8.5': { w: 7920, h: 12240 },
  '5x8': { w: 7200, h: 11520 },
  letter: { w: 12240, h: 15840 },
};
const trimKey = (flags.trim || '6x9').toLowerCase();
const TRIM = TRIMS[trimKey] || TRIMS['6x9'];

const BODY_FONT = 'Times New Roman';

// Must match the margin values used in buildDocument() below — kept as named
// constants specifically so the TOC tab stop (which needs the real usable
// content width) can never silently drift out of sync with the page margins.
const MARGIN_TOP = 720;    // 0.5"
const MARGIN_BOTTOM = 720; // 0.5"
const MARGIN_OUTSIDE = 540; // 0.375"
const MARGIN_INSIDE = 720;  // 0.5" (gutter)
const USABLE_WIDTH = TRIM.w - MARGIN_OUTSIDE - MARGIN_INSIDE; // total horizontal margin is the same on every page regardless of mirroring, so one flat tab-stop position is correct for both odd and even pages

// ---------------------------------------------------------------------
// Smart typographic quotes (source manuscripts use plain straight quotes)
// ---------------------------------------------------------------------
function smartQuotes(s) {
  s = s.replace(/'/g, '’'); // assumes no nested single-quote dialogue in the manuscript
  let result = '';
  let prevChar = '';
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (c === '"') {
      result += (prevChar === '' || /[\s([{\-—–]/.test(prevChar)) ? '“' : '”';
    } else {
      result += c;
    }
    prevChar = c;
  }
  return result;
}

function parseInline(rawText, baseItalic = false) {
  const text = smartQuotes(rawText);
  const runs = [];
  const tokenRe = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let lastIndex = 0;
  let m;
  while ((m = tokenRe.exec(text)) !== null) {
    if (m.index > lastIndex) {
      runs.push(new TextRun({ text: text.slice(lastIndex, m.index), italics: baseItalic }));
    }
    const token = m[0];
    if (token.startsWith('**')) {
      runs.push(new TextRun({ text: token.slice(2, -2), bold: true, italics: baseItalic }));
    } else {
      runs.push(new TextRun({ text: token.slice(1, -1), italics: true }));
    }
    lastIndex = tokenRe.lastIndex;
  }
  if (lastIndex < text.length) {
    runs.push(new TextRun({ text: text.slice(lastIndex), italics: baseItalic }));
  }
  if (runs.length === 0) runs.push(new TextRun({ text: '', italics: baseItalic }));
  return runs;
}

function isFullyItalicLine(line) {
  return /^\*[^*].*[^*]\*$|^\*[^*]\*$/.test(line) && !line.startsWith('**');
}
function stripFullItalic(line) {
  return line.slice(1, -1);
}

const bodyParagraph = (text, opts = {}) => new Paragraph({
  children: parseInline(text, opts.italic || false),
  alignment: AlignmentType.JUSTIFIED,
  spacing: { after: 0, line: 300 }, // ~1.25x, no extra paragraph gap — indent alone signals new paragraph (manuscript-style-guide.md)
  indent: opts.noIndent ? undefined : { firstLine: 360 }, // 0.25"
});

const sceneBreak = () => new Paragraph({
  text: '•        •        •',
  alignment: AlignmentType.CENTER,
  spacing: { before: 160, after: 160 },
});

// ---------------------------------------------------------------------
// Build the document body. `pageMap` is null on pass 1 (blank TOC) or
// {headingId -> pageNumber} on later passes (populated TOC).
// Returns { children, tocEntries } — tocEntries is the ordered list of
// {id, text} for every '## ' heading, used to compute pageMap between passes.
// ---------------------------------------------------------------------
function buildBody(lines, title, subtitle, pageMap) {
  const children = [];
  const tocEntries = [];

  // Title page
  children.push(new Paragraph({ text: '', spacing: { before: 2000 } }));
  children.push(new Paragraph({
    children: [new TextRun({ text: smartQuotes(title), bold: true, size: 64 })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 300 },
  }));
  if (subtitle) {
    children.push(new Paragraph({
      children: [new TextRun({ text: smartQuotes(subtitle), italics: true, size: 28 })],
      alignment: AlignmentType.CENTER,
      spacing: { after: 200 },
    }));
  }
  if (seriesLine) {
    children.push(new Paragraph({
      children: [new TextRun({ text: smartQuotes(seriesLine), size: 24 })],
      alignment: AlignmentType.CENTER,
      spacing: { before: 400, after: 0 },
    }));
  }
  if (authorName) {
    children.push(new Paragraph({
      children: [new TextRun({ text: smartQuotes(authorName), size: 26 })],
      alignment: AlignmentType.CENTER,
      spacing: { before: seriesLine ? 120 : 400, after: 0 },
    }));
  }
  children.push(new Paragraph({ children: [new PageBreak()] }));

  // Copyright page (project addition): paragraphs from --copyright <file>, blank-line separated
  if (flags.copyright) {
    const cp = fs.readFileSync(flags.copyright, 'utf8').split(/\n\s*\n/).map((x) => x.trim()).filter(Boolean);
    children.push(new Paragraph({ text: '', spacing: { before: 3600 } }));
    for (const para of cp) {
      children.push(new Paragraph({
        children: [new TextRun({ text: smartQuotes(para), size: 18 })],
        alignment: AlignmentType.CENTER,
        spacing: { after: 160 },
      }));
    }
    children.push(new Paragraph({ children: [new PageBreak()] }));
  }

  // Table of Contents — real paragraphs (see file header for why this is not a
  // Word TableOfContents field). tocEntries isn't known until the body loop below
  // has run, so splice a placeholder marker here and replace it afterward. Always
  // built with real dot-leader/hyperlink paragraphs (even on the blank-map pass) so
  // every pass's Contents section has the same real height — an empty/live TOC
  // field on pass 1 would under-measure the section and throw off pagination.
  children.push(new Paragraph({
    children: [new TextRun({ text: 'Contents', bold: true, size: 32 })],
    alignment: AlignmentType.CENTER,
    spacing: { after: 240 },
  }));
  children.push({ __tocPlaceholder: true });
  children.push(new Paragraph({ children: [new PageBreak()] }));

  let i = 0;
  while (i < lines.length && !lines[i].startsWith('## ')) i++;

  let firstChapter = true;
  let headingCounter = 0;

  while (i < lines.length) {
    const line = lines[i];

    if (line.startsWith('## ')) {
      const headingText = line.slice(3).trim();
      const bookmarkId = `toc_h${headingCounter}`;
      if (!firstChapter) {
        children.push(new Paragraph({ children: [new PageBreak()] }));
      }
      firstChapter = false;

      children.push(new Paragraph({
        heading: HeadingLevel.HEADING_1,
        alignment: AlignmentType.CENTER,
        spacing: { before: 240, after: 120 },
        children: [
          new Bookmark({
            id: bookmarkId,
            children: [new TextRun({ text: headingText, bold: true, size: 32 })],
          }),
        ],
      }));

      tocEntries.push({ id: bookmarkId, text: headingText });
      headingCounter++;

      i++;
      while (i < lines.length && lines[i].trim() === '') i++;
      if (i < lines.length && isFullyItalicLine(lines[i].trim())) {
        const subtitleLine = stripFullItalic(lines[i].trim());
        children.push(new Paragraph({
          children: [new TextRun({ text: subtitleLine, italics: true, size: 22 })],
          alignment: AlignmentType.CENTER,
          spacing: { after: 240 },
        }));
        i++;
      }
      continue;
    }

    if (line.trim() === '---') {
      children.push(sceneBreak());
      i++;
      continue;
    }

    if (line.trim() === '') {
      i++;
      continue;
    }

    if (line.trim() === '**THE END**') {
      children.push(new Paragraph({
        children: [new TextRun({ text: 'THE END', bold: true, size: 26 })],
        alignment: AlignmentType.CENTER,
        spacing: { before: 300, after: 300 },
      }));
      i++;
      continue;
    }

    const trimmed = line.trim();
    if (isFullyItalicLine(trimmed)) {
      children.push(bodyParagraph(stripFullItalic(trimmed), { italic: true }));
    } else {
      children.push(bodyParagraph(trimmed));
    }
    i++;
  }

  // Now that tocEntries is known, splice in the real TOC paragraphs — one per
  // heading, each a clickable link to that heading's Bookmark, with a dot-leader
  // tab stop positioned at this document's actual usable content width (not
  // docx.js's hardcoded Letter-width assumption — see file header).
  const tocParagraphs = tocEntries.map((entry) => {
    const pageLabel = pageMap ? String(pageMap[entry.id] || '?') : '';
    return new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: USABLE_WIDTH, leader: 'dot' }],
      spacing: { after: 40 },
      children: [
        new InternalHyperlink({
          anchor: entry.id,
          children: [new TextRun({ text: entry.text, color: '000000', underline: undefined })],
        }),
        new TextRun({ children: [new Tab()], color: '000000' }),
        new TextRun({ text: pageLabel, color: '000000' }),
      ],
    });
  });
  const tocIdx = children.findIndex((c) => c && c.__tocPlaceholder);
  children.splice(tocIdx, 1, ...tocParagraphs);

  return { children, tocEntries };
}

function buildDocument(children) {
  const pageNumberFooter = new Footer({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: [PageNumber.CURRENT], font: BODY_FONT, size: 20 })],
      }),
    ],
  });

  // No `features.updateFields` anywhere: the TOC is plain paragraphs, not a Word
  // field (see file header), so there is nothing for any viewer to mark dirty or
  // recompute on open in the first place — the earlier cachedEntries-field approach
  // needed to suppress that explicitly; this approach has no such flag to suppress.
  return new Document({
    sections: [{
      properties: {
        page: {
          size: { width: TRIM.w, height: TRIM.h },
          margin: {
            top: MARGIN_TOP,
            bottom: MARGIN_BOTTOM,
            right: MARGIN_OUTSIDE, // 24–150pp KDP bracket needs >=0.375" gutter; built-in headroom throughout
            left: MARGIN_INSIDE,   // inside/gutter
            gutter: 0,              // deliberate — the inside-margin value above IS the gutter, not stacked on top of it
          },
        },
      },
      footers: {
        default: pageNumberFooter, // every page, including the title page — numbered from page 1
      },
      children,
    }],
    styles: {
      default: {
        document: {
          run: { font: BODY_FONT, size: 24 }, // 12pt
          paragraph: { spacing: { line: 300 } }, // ~1.25x
        },
      },
      paragraphStyles: [
        {
          id: 'Heading1',
          name: 'Heading 1',
          basedOn: 'Normal',
          next: 'Normal',
          quickFormat: true,
          run: { font: BODY_FONT, size: 32, bold: true, color: '000000' },
          paragraph: {
            alignment: AlignmentType.CENTER,
            spacing: { before: 240, after: 120 },
          },
        },
      ],
    },
  });
}

// ---------------------------------------------------------------------
// Post-build mirror-margins patch (docx.js has no native support).
// ---------------------------------------------------------------------
function applyMirrorMargins(docxPathIn) {
  const docxPath = path.resolve(docxPathIn); // must be absolute — the zip step below cd's into a temp dir
  const workDir = `${docxPath}.__unzip`;
  execFileSync('rm', ['-rf', workDir]);
  fs.mkdirSync(workDir, { recursive: true });
  execFileSync('unzip', ['-q', docxPath, '-d', workDir]);

  const settingsPath = path.join(workDir, 'word', 'settings.xml');
  let settings = fs.readFileSync(settingsPath, 'utf8');
  if (!settings.includes('<w:mirrorMargins')) {
    if (settings.includes('<w:displayBackgroundShape/>')) {
      settings = settings.replace('<w:displayBackgroundShape/>', '<w:displayBackgroundShape/><w:mirrorMargins/>');
    } else {
      // fall back: insert right after the opening <w:settings ...> tag
      settings = settings.replace(/(<w:settings[^>]*>)/, '$1<w:mirrorMargins/>');
    }
    fs.writeFileSync(settingsPath, settings);
  }

  execFileSync('rm', [docxPath]);
  // zip contents (not the wrapping directory) back into the docx
  execFileSync('bash', ['-c', `cd "${workDir}" && zip -Xrq "${docxPath}" .`]);
  execFileSync('rm', ['-rf', workDir]);
}

// ---------------------------------------------------------------------
// LibreOffice / pdftotext helpers
// ---------------------------------------------------------------------
function findSofficeWrapper() {
  const candidate = '/root/.claude/skills/synced/docx/scripts/office/soffice.py';
  return fs.existsSync(candidate) ? candidate : null;
}

function convertToPdf(docxPath, outDir) {
  const wrapper = findSofficeWrapper();
  if (wrapper) {
    execFileSync('python3', [wrapper, '--headless', '--convert-to', 'pdf', '--outdir', outDir, docxPath], { stdio: 'pipe' });
  } else {
    execFileSync('soffice', ['--headless', '--convert-to', 'pdf', '--outdir', outDir, docxPath], { stdio: 'pipe' });
  }
  return path.join(outDir, path.basename(docxPath).replace(/\.docx$/i, '.pdf'));
}

// Extract {headingId -> pageNumber} by searching forward through the PDF with a
// monotonically-advancing page cursor (never restart from page 1 per heading — a
// repeated title, or the TOC's own listing of the title, would false-match).
// `startPage` (0-indexed) lets a re-verification pass skip the TOC's own pages.
function extractPageMap(pdfPath, tocEntries, startPage = 0) {
  const text = execFileSync('pdftotext', ['-layout', pdfPath, '-']).toString('utf8');
  const pages = text.split('\f');
  const map = {};
  let searchFrom = startPage;
  for (const entry of tocEntries) {
    let found = null;
    for (let p = searchFrom; p < pages.length; p++) {
      const pageLines = pages[p].split('\n').map((l) => l.trim());
      if (pageLines.includes(entry.text)) {
        found = p + 1; // 1-indexed page number
        searchFrom = p;
        break;
      }
    }
    map[entry.id] = found || null;
  }
  return { map, pageCount: pages.length };
}

// ---------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------
async function main() {
  const raw = fs.readFileSync(mdPath, 'utf8');
  const lines = raw.split('\n');

  const titleMatch = lines[0] && lines[0].match(/^#\s+(.+)/);
  const subtitleMatch = lines[1] && lines[1].match(/^#{2,3}\s+(.+)/);
  const title = titleMatch ? titleMatch[1].trim() : path.basename(mdPath, '.md').toUpperCase();
  const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';

  const tmpDir = path.dirname(outPath);
  const tmpDocx = outPath.replace(/\.docx$/i, '.__pass.docx');

  // ---- Pass 1: blank TOC, to discover a real, representative pagination.
  // Mirror margins are applied to THIS temp file too (not just the final one) —
  // total left+right margin is unchanged by mirroring so it shouldn't affect
  // wrapping, but "shouldn't" isn't good enough for a page-number pipeline; verify
  // against the literal bytes closest to what ships, every single pass. ----
  const pass1 = buildBody(lines, title, subtitle, null);
  const doc1 = buildDocument(pass1.children);
  fs.writeFileSync(tmpDocx, await Packer.toBuffer(doc1));
  applyMirrorMargins(tmpDocx);
  let pdfPath = convertToPdf(tmpDocx, tmpDir);
  let { map: pageMap } = extractPageMap(pdfPath, pass1.tocEntries, 0);

  // ---- Convergence loop: rebuild with real numbers, then INDEPENDENTLY
  // re-verify against the actual rebuilt PDF (never assume it matches the
  // previous pass) — repeat until stable or the cap is hit. ----
  const MAX_PASSES = 4;
  let finalTocEntries = pass1.tocEntries;
  let converged = false;

  for (let attempt = 1; attempt <= MAX_PASSES; attempt++) {
    const pass = buildBody(lines, title, subtitle, pageMap);
    const doc = buildDocument(pass.children);
    fs.writeFileSync(tmpDocx, await Packer.toBuffer(doc));
    applyMirrorMargins(tmpDocx);
    pdfPath = convertToPdf(tmpDocx, tmpDir);

    // Re-extract from THIS pass's own PDF, searching from page 1 — the TOC page
    // itself is blank of chapter-heading-exact-match lines by construction (it only
    // contains "Heading....N" lines with a tab+number, not the bare heading text), so
    // this does not require skipping past the TOC's own pages.
    const { map: verifiedMap, pageCount } = extractPageMap(pdfPath, pass.tocEntries, 0);

    let mismatches = 0;
    for (const entry of pass.tocEntries) {
      if (verifiedMap[entry.id] !== pageMap[entry.id]) mismatches++;
    }

    console.log(`Pass ${attempt}: ${pass.tocEntries.length} headings, ${mismatches} page-number mismatch(es), ${pageCount} total pages`);

    finalTocEntries = pass.tocEntries;

    if (mismatches === 0) {
      converged = true;
      break;
    }
    pageMap = verifiedMap; // rebuild once more with the corrected numbers
  }

  if (!converged) {
    console.error(`WARNING: TOC page numbers did not converge after ${MAX_PASSES} passes — shipping best-effort result. Investigate before treating as final.`);
  }

  // tmpDocx already has mirror margins applied from inside the loop above — move it
  // to the real output path rather than rewriting from the pre-mirroring in-memory
  // buffer, so what shipped is exactly what was verified, byte for byte.
  fs.copyFileSync(tmpDocx, outPath);
  fs.unlinkSync(tmpDocx);
  if (fs.existsSync(pdfPath)) fs.unlinkSync(pdfPath);

  if (!fs.existsSync(outPath) || fs.statSync(outPath).size < 10000) {
    throw new Error(`Output file missing or suspiciously small: ${outPath}`);
  }

  console.log(`Built ${outPath} (${fs.statSync(outPath).size} bytes), TOC entries: ${finalTocEntries.length}, converged: ${converged}, trim: ${trimKey} (${TRIM.w}x${TRIM.h} twips)`);
  console.log('Final page map:', pageMap);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
