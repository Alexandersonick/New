# Catalog & Series Layer cross-book Report — target: Two Tickets to the Haunted Hayride
Priors: My Twin Sister Took My Place as His Wife · n=4 · min-count=3 · min-books=2

Mechanical measurement only. AXIS_11_MECHANICAL is the one PASS/FAIL; the Jaccard numbers are heuristics that tell you where to READ, not verdicts. Nothing here rewrites a manuscript.

## 1. Book profiles

| Metric | My Twin Sister Took My Place as His Wife | Two Tickets to the Haunted Hayride (TARGET) |
|---|---|---|
| Words (parsed) | 72,926 | 69,590 |
| Parse coverage (parsed / raw) | 100% | 100% |
| Chapters | 30 | 30 |
| Mean chapter words | 2431 | 2320 |
| Chapter-length CV | 0.15 | 0.15 |
| Dialogue % (book) | 36.7 | 28.6 |
| Dialogue % (ch 1–3) | 29.8 | 25.7 |
| Ch1 words before first dialogue | 203 | 184 |
| First-person hits /1k narration words | 30.4 | 0.7 |
| First-person share of pronoun hits | 29% | 1% |
| Narration mode (derived) | third-person | third-person |
| POV marker lines | 30 | 30 |
| Quote style | double | double |

**My Twin Sister Took My Place as His Wife** — `/tmp/claude-0/-home-user-New/ee1766d4-8f58-5f44-b6ce-ba0c0d35d499/scratchpad/catalog/twin_sister.md`
- Ch1 first sentence: The first wrong thing was my coat, because I had left it on the third hook in the front hall on August 3 and it had just walked out of my front door without me.
- Ch1 first 60 words: The first wrong thing was my coat because I had left it on the third hook in the front hall on August 3 and it had just walked out of my front door without me Camel wool a man's cut 11 at a thrift shop in Wilmington worn through at the right cuff where my wrist used to rest on
- Last paragraph: "Again."

**Two Tickets to the Haunted Hayride** — `manuscript/draft.md`
- Ch1 first sentence: Roz Pietrowski had written the rule herself, which was the worst part.
- Ch1 first 60 words: Roz Pietrowski had written the rule herself which was the worst part She had written it on the back of a Bakker's Diner placemat last October in the middle of the Seat War while two grown women argued over a wagon bench as if it were the last lifeboat off the Titanic She had laminated it on the teachers' lounge
- Last paragraph: Its glass held the window. It was still.

## 2. Cross-book repeated 4-grams (axis 11, mechanical half)

FAIL = 4-gram used ≥3× in the target AND ≥3× in each of ≥2 prior books. WATCH = same, but in fewer than 2 prior book(s).

- WARNING: My Twin Sister Took My Place as His Wife has ≥200 repeated 4-grams at min-count; prose_metrics caps the list at 200, so the intersection for this book may be incomplete.
- WARNING: Two Tickets to the Haunted Hayride has ≥200 repeated 4-grams at min-count; prose_metrics caps the list at 200, so the intersection for this book may be incomplete.
### FAIL set (0)

- none

### WATCH set (7)

| 4-gram | TARGET × | My Twin Sister Took My Place as His Wife |
|---|---|---|
| i'm not going to | 13 | 5 |
| she looked at him | 7 | 5 |
| at the far end | 6 | 4 |
| he could see the | 5 | 3 |
| for a long time | 4 | 3 |
| in front of him | 4 | 4 |
| said without looking up | 4 | 4 |

### Target signature — top repeated 4-grams (≥3×)

'i'm not going to' ×13; 'in the front row' ×12; 'end of the dock' ×11; 'on the far bank' ×11; 'on the way back' ×10; 'back to the barn' ×9; 'in the third row' ×9; 'side of the bench' ×9; 'we're looking for somebody' ×9; 'on the 8 20' ×8

## 3. Opening similarity — HEURISTIC

Jaccard overlap of lowercase content-word sets (chapters 1–3), target vs each prior. ≥0.35 is flagged HIGH (heuristic). A high number means shared vocabulary/template, not proof of reuse — read both passages.

| Prior | Jaccard | Flag |
|---|---|---|
| My Twin Sister Took My Place as His Wife | 0.271 | — |

## 4. Ending similarity — HEURISTIC

Jaccard overlap of lowercase content-word sets (last paragraph of the final chapter), target vs each prior. ≥0.30 is flagged HIGH (heuristic). A high number means shared vocabulary/template, not proof of reuse — read both passages.

| Prior | Jaccard | Flag |
|---|---|---|
| My Twin Sister Took My Place as His Wife | 0.000 | — |

## 5. Chapter-exit rhythm — HEURISTIC

How chapters end, using prose_metrics' exit-kind labels on each chapter's final paragraph (a chapter can carry several labels). Cells = % of chapters carrying the kind. Distance = L1 between the kind-share vectors after normalising each to sum 1 (0 = identical, 2 = disjoint); ≤0.30 is flagged.

| Exit kind (% of chapters) | My Twin Sister Took My Place as His Wife | Two Tickets to the Haunted Hayride (TARGET) |
|---|---|---|
| dialogue | 57% | 50% |
| question | 0% | 0% |
| decision | 0% | 7% |
| cliffhanger-ish | 0% | 0% |
| image/quiet | 43% | 47% |
| SUMMARY? | 0% | 0% |
| NAMED-FEELING? | 0% | 7% |
| STOCK-ENDING! | 0% | 0% |

| Prior | L1 distance | Flag |
|---|---|---|
| My Twin Sister Took My Place as His Wife | 0.242 | SAME EXIT RHYTHM (heuristic) |

## 6. Voice signature — HEURISTIC (v5.0.2)

Sentence-level habits measured on NARRATION ONLY (dialogue stripped), per 1,000 narration words. The structural fingerprint cannot see these; the stress test showed seven narrators sharing one set. A tic is SHARED with a prior when both books sit at or above its threshold and within 2× of each other. ≥3 shared tics, or top-sentence-opener Jaccard ≥0.30, flags VOICE CONVERGENCE — which means: run the blind voice test (page-craft-standards.md §7) on these two books. A flag is not a verdict.

| Tic (per 1k narration words) | threshold | My Twin Sister Took My Place as His Wife | Two Tickets to the Haunted Hayride (TARGET) |
|---|---|---|---|
| em dashes | ≥5.0 | 0.02 | 0.06 |
| negative parallelism ('not X, but Y') | ≥0.5 | 0.02 | 0.02 |
| 'not X, exactly' / 'not quite X' reframes | ≥0.3 | 0.02 | 0.00 |
| '[name] understood' cognitive summaries | ≥0.4 | 0.00 | 0.00 |
| hedges before disclosure ('for what it's worth', 'I want to be honest') | ≥0.3 | 0.00 | 0.02 |
| 'for the first time' epiphany markers | ≥0.25 | 0.00 | 0.00 |
| filter words (felt/saw/noticed/realized…) | ≥6.0 | 3.64 | 5.05 |
| theme statements ('that was the thing about…') | ≥0.5 | 0.00 | 0.00 |

| Prior | Shared tics | Which | Opener Jaccard | Flag |
|---|---|---|---|---|
| My Twin Sister Took My Place as His Wife | 0 | — | 0.290 | — |

Per-POV vectors were computed where a POV label covers ≥1,000 narration words (chapter POV line, `## Name` section marker kept by the parser, or `<!-- POV: Name -->` comments):

- My Twin Sister Took My Place as His Wife: Maud (28,639 w), Declan (17,516 w)
- Two Tickets to the Haunted Hayride: Roz (29,569 w), Gus (20,136 w)

## 7. Twelve-axis table (skeleton)

Pre-filled only where derivable (axis 3, 10, 11; hint on 2). Everything else: read the books and fill.

| Axis | My Twin Sister Took My Place as His Wife | Two Tickets to the Haunted Hayride (TARGET) |
|---|---|---|
| 1 Inciting disruption (+ kind) | [fill from text] (hint — Ch1 opens: "The first wrong thing was my coat, because I had left it on the third hook in the front hall on Augu") | [fill from text] (hint — Ch1 opens: "Roz Pietrowski had written the rule herself, which was the worst part.") |
| 2 The bind | [fill from text] | [fill from text] |
| 3 First irreversible decision (chapter) | [fill from text] | [fill from text] |
| 4 Midpoint reversal | [fill from text] | [fill from text] |
| 5 Rupture / lowest point | [fill from text] | [fill from text] |
| 6 Climax action (+ who causes it) | [fill from text] | [fill from text] |
| 7 Repair mechanism (+ shape) | [fill from text] | [fill from text] |
| 8 Resolution & epilogue shape | [fill from text] | [fill from text] |
| 9 Form: structure / POV / timeline entry | third-person + 30 POV markers | third-person + 30 POV markers |
| 10 Form: ending image (+ class) | "Again." | Its glass held the window. It was still. |
| 11 Form: narrator signature | 'end of the bench' ×8; 'okay he said and' ×7; 'phone in the bowl' ×7; 'and put it back' ×6; 'clock over the sink' ×5 | 'i'm not going to' ×13; 'in the front row' ×12; 'end of the dock' ×11; 'on the far bank' ×11; 'on the way back' ×10 |

## 8. Verdict

AXIS_11_MECHANICAL: PASS
VOICE_CONVERGENCE (heuristic): —

- FAIL list: empty
- HIGH-similarity flags: none
- SAME EXIT RHYTHM (heuristic) vs: My Twin Sister Took My Place as His Wife (L1 0.24)
- VOICE CONVERGENCE (heuristic) vs: none
- HOUSE HABITS (target + ≥2 priors above threshold): none

Reminder: Core axes 1–8 are filled by reading the earlier books' actual text — never blurbs or summaries — and scored BLIND from surface-stripped rows by a reader who did not write the concept. Gate (SKILL.md, Catalog & Series Layer): FAIL if ≥5 of 8 core axes match any one earlier book; the shape-axis COMBINATION (inciting kind + repair shape + ending-image class) and the climax staging set are never reused series-wide; this script's flags are heuristics — a flag plus a confirming read is the finding.
