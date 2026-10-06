# Tic-thinning pass (final line pass before production)

You edit ONLY your assigned chapter files in `/home/user/New/corner-office/chapters/`. This is a
**phrase-level pass only**. Do not change plot, dialogue meaning, chapter openings, final
paragraphs, headings, or `<!-- POV -->` lines. Keep word count within ±3% per chapter. Keep
present tense, first person, and each character's voice. All the hard rules in
`qc/LINE_REVISION_BRIEF.md` still apply: no Tier-1 phrases, no "not X, but Y", em dashes only
for cut-off speech, no runs of three ≤3-word sentences.

## Per-chapter caps
- "the way …" (any use, including similes) **≤3** per chapter.
- "like a …" similes **≤3** per chapter. "like a man …" **≤1** per chapter.
- "the way you'd …": at most one in the book per agent group (cut or rephrase the rest).
- Craft or weld similes for feelings ("like a weld", "like a sheet of glass", "like checking a weld"): **≤1** per chapter.

Replace with a plain statement, a concrete action, or nothing. A simile that is genuinely funny
and character-specific can stay inside the caps. Cut the generic ones first.

## Book-wide caps, split by group (counts as of now)
| Phrase | Book now | Book cap | Group A (ch01–10) | Group B (ch11–20) | Group C (ch21–30) |
|---|---|---|---|---|---|
| "the real one" (laugh) | 8 | 4 | keep ≤2 | keep ≤1 | keep ≤1 |
| "nose voice" / "Rotary" | 15 | 6 | keep ≤3 | keep ≤2 | keep ≤1 |
| "two years" | 19 | 10 | keep ≤4 | keep ≤3 | keep ≤3 |
| "since Nashville" | 14 | 10 | keep ≤3 | keep ≤4 | keep ≤3 |
| "temperature of a bath" | 2 | 1 | — | — | keep ≤1 |
| "X-ray" simile | 2 | 1 | keep ≤1 | keep ≤0 if A kept one | — |
| "um" as a joke about Adam | — | 3 | — | keep ≤2 | keep ≤1 |

## Check
Count with `grep -o -i "PHRASE" FILE | wc -l`. Run `python3 /home/user/New/corner-office/tools/tric.py`
on a file built as `# T` plus your chapters. Report a per-chapter before → after table for "the way"
and "like a", plus the book-wide phrase counts for your group, in under 150 words.
