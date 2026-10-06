#!/usr/bin/env node
/**
 * build_epub_source.js — preprocess a Master Fiction Pipeline manuscript
 * (the same Markdown convention build_manuscript_docx.js consumes) into a
 * pandoc-ready Markdown file for EPUB conversion.
 *
 * Unlike the .docx path, this does NOT hand-parse bold/italic markup — pandoc's
 * own markdown reader (with +smart) does that natively, including straight-
 * to-curly quote conversion. Only three fiction-specific constructs need
 * conversion to raw HTML, because they need visual treatment plain Markdown
 * has no clean way to express: the POV/date subtitle line under each chapter
 * heading, the scene-break glyph, and the "THE END" mark.
 *
 * Usage:
 *   node build_epub_source.js <manuscript.md> <output.md> [--series "..."] [--author "..."] [--seriesIndex N]
 */

const fs = require('fs');
const path = require('path');

function parseArgs(argv) {
  const positional = [];
  const flags = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith('--')) {
      flags[argv[i].slice(2)] = argv[i + 1];
      i++;
    } else {
      positional.push(argv[i]);
    }
  }
  return { positional, flags };
}

const { positional, flags } = parseArgs(process.argv.slice(2));
const [mdPath, outPath] = positional;
if (!mdPath || !outPath) {
  console.error('Usage: node build_epub_source.js <manuscript.md> <output.md> [--series "..."] [--author "..."]');
  process.exit(1);
}

function isFullyItalicLine(line) {
  return /^\*[^*].*[^*]\*$|^\*[^*]\*$/.test(line) && !line.startsWith('**');
}
function stripFullItalic(line) {
  return line.slice(1, -1);
}
function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

const raw = fs.readFileSync(mdPath, 'utf8');
const lines = raw.split('\n');

const titleMatch = lines[0] && lines[0].match(/^#\s+(.+)/);
const subtitleMatch = lines[1] && lines[1].match(/^#{2,3}\s+(.+)/);
const title = titleMatch ? titleMatch[1].trim() : path.basename(mdPath, '.md');
const subtitle = subtitleMatch ? subtitleMatch[1].trim() : '';
const seriesLine = flags.series || '';
const authorName = flags.author || '';

const out = [];

// Custom title page (pandoc's auto title page is disabled via --epub-title-page=false).
//
// This MUST be its own real, non-empty H1 section, a sibling of every chapter's H1 —
// not raw content floating before the first heading. Two failure modes were found and
// rejected before this one: (a) no heading at all around the title-page div → pandoc's
// epub3 writer still synthesizes an implicit level-1 section from the doc title to hold
// it, and since that's the only level-1 heading in the document, every chapter heading
// nests underneath it as a false child in the nav outline (chapters end up one level
// deep, all listed under a single "COUNTDOWN" parent entry) — and if the doc title is
// left empty to avoid an unwanted label, that synthesized H1 has no text at all, which
// epubcheck flags outright ("Anchors within nav elements must contain text"). (b) giving
// the title page its own H1 while chapters stayed at H2 hit the same nesting bug, just
// with a real label instead of an empty one — chapters still ended up nested under it,
// since H2 always nests under whatever H1 precedes it in document order. The fix used
// here: title page AND every chapter are H1, so they're siblings in the outline, not
// parent/child — hidden via CSS (`.visually-hidden`) so the "Title Page" label itself
// isn't shown to the reader, but it still carries real text so the nav entry is valid.
out.push('# Title Page {.visually-hidden}');
out.push('');
out.push('<div class="titlepage">');
out.push(`<p class="booktitle">${escapeHtml(title)}</p>`);
if (subtitle) out.push(`<p class="booksubtitle"><em>${escapeHtml(subtitle)}</em></p>`);
if (seriesLine) out.push(`<p class="seriesline">${escapeHtml(seriesLine)}</p>`);
if (authorName) out.push(`<p class="authorline">${escapeHtml(authorName)}</p>`);
out.push('</div>');
out.push('');

let i = 0;
while (i < lines.length && !lines[i].startsWith('## ')) i++;

while (i < lines.length) {
  const line = lines[i];

  if (line.startsWith('## ')) {
    out.push(`# ${line.slice(3)}`); // promoted to H1 — see the title-page comment above for why
    i++;
    while (i < lines.length && lines[i].trim() === '') { out.push(''); i++; }
    if (i < lines.length && isFullyItalicLine(lines[i].trim())) {
      const povLine = stripFullItalic(lines[i].trim());
      out.push(`<p class="povline"><em>${escapeHtml(povLine)}</em></p>`);
      i++;
    }
    continue;
  }

  if (line.trim() === '---') {
    out.push('<p class="scenebreak">&#8226;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;&nbsp;&nbsp;&nbsp;&nbsp;&#8226;</p>');
    i++;
    continue;
  }

  if (line.trim() === '**THE END**') {
    out.push('<p class="theend">THE END</p>');
    i++;
    continue;
  }

  out.push(line); // everything else — regular paragraphs, letter blocks (*...*), **bold** — pandoc handles natively
  i++;
}

fs.writeFileSync(outPath, out.join('\n'));
console.log(`Wrote ${outPath} (${out.length} lines). Title: "${title}" / Subtitle: "${subtitle}" / Series: "${seriesLine}" / Author: "${authorName}"`);
