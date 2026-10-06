# Line Revision Brief: *My CEO Husband Gave Her My Corner Office* (draft 1 → draft 2)

You are revising **your assigned chapters only**, in place, in
`/home/user/New/corner-office/chapters/chNN.md`. This is a **line and depth** pass. The
structure, the plot facts and the order of events are locked. Read these before touching
anything:
- `/home/user/New/corner-office/14_VOICE_GUIDE.md` (Voice Contract and idiolects)
- `/home/user/New/corner-office/06_WORLD_BIBLE.md` (locked facts)
- `/home/user/New/corner-office/04_CHARACTER_BIBLE.md`
- `/home/user/New/corner-office/qc/HOSTILE_READER_full_draft1.md` (if present): its findings for your chapters
- Your chapters, plus one chapter on either side for continuity.

## Hard rules (never break)
1. Keep: the heading line `## Chapter N — Name`, the `<!-- POV: Name -->` line, present tense, first person, and the chapter's POV.
2. Do not change plot facts, numbers, names, dates, who knows what when, or chapter endings' *content*. You may tighten an ending's wording, but the final paragraph must stay ≤25 words and stay the same kind (image, line, decision and so on).
3. Never add: "attracted/attraction", Tier-1 phrases (ai-texture-audit §1, e.g. *testament to, tapestry, delve, a wave of X washed over, couldn't help but, the silence stretched, heart hammered*), "never once", "I'm not going to", "for the first time", "for what it's worth", "I want to be honest", or "not X, but Y" / "It wasn't X. It was Y." constructions. Em dashes ≤2 per 1,000 words (use them only for cut-off speech).
4. No narrator glossing a joke or explaining a beat's meaning. Theme stays in characters' mouths.
5. No new characters with names. No new subplots.
6. Keep the Polish/West Side texture, the humour, and each character's idiolect (tag-strip test ≥80%).

## Targets (measure with the script; see the bottom of this brief)
- **Fragment share (sentences ≤4 words) ≤30% per chapter.** This is the biggest problem. The draft uses punch fragments as a habit ("Not much." "It's Adam." "Hi." "Hi."). Fix it by merging: attach the short line to the sentence before or after, give a one-word reply an action or a tag of ≥4 words, and turn narration fragments into full sentences. Keep fragments only at real turns.
- **Tricolon proxy:** the script counts every run of three consecutive sentences of ≤3 words, plus any sentence ending "X, Y, and Z." Break every such run unless it is the single sharpest beat in the chapter (at most one per chapter).
- **Dialogue share ≥25% per chapter** (confrontation scenes ≥45%). Do not cut dialogue to fix fragments; merge it instead.
- **Filter words ≤6/1k** (felt, saw, heard, noticed, realized, watched, wondered, seemed, could see/hear).
- **Emotion words anchored** to a body part, gesture or object in the same or the previous sentence.

## Repetition to break (book-wide counts in draft 1; your share must drop by at least half)
"for a long time" ×25 · "for a long moment" ×11 · "at one in the morning" ×21 (a motif; keep it where it's a plot fact, cut it elsewhere) · "the chair by the radiator" ×15 (call it "his chair" or "the radiator chair" sometimes, or drop the noun) · "through the glass corner" ×11 · "end of the counter" ×11 · "I look at him" ×10 · "in front of everybody" ×10 · "I put the phone" ×9 · "he doesn't say anything" / "I don't say anything" ×16 · "takes her glasses off" ×8 (Lolo's tic; keep ≤1 per chapter) · "something happens at the corner of her/his mouth" (keep ≤1 in the book; use specific faces instead) · "I want you to know" ×6 · "the way you'd [verb]" simile construction (cap 1 per chapter) · "which for X is Y" construction (cut) · "like a man [doing X]" similes (cap 2 per chapter).

## Depth expansion (only where your assignment says so)
The book is short: 61,167 words measured against a 67,000-word minimum. Some chapters have an
**expansion quota**. Every expansion must:
- add a **visible act, line, or object change** (Felt-delta). No interior summary, no recap.
- add ≥1 new concrete problem, joke, or turn.
- keep or raise dialogue share; no new backstory dumps; no restating what an earlier chapter showed.

Good expansion material: a short extra exchange in an existing scene that complicates it; a
workplace beat with the crew that shows the plant's stakes; a specific obstacle in a task
already underway; a moment of humour between two characters already in the scene.

## Process
1. Read your chapters and their neighbours.
2. Revise each chapter by rewriting the file in full (Write) or with targeted edits.
3. Measure after each chapter:
   `python3 /root/.claude/skills/synced/bd2694d4-4c02-48e4-b638-527ccb841fad_be25934a-7495-42ed-b478-ac156b97130e/master-fiction-pipeline/scripts/prose_metrics.py /tmp/YOURNAME_check.md --niche romance`
   Build the check file by concatenating `# T` + your chapters. Iterate until fragment ≤30%,
   dialogue ≥25%, and the exit is ≤25 words. Then run
   `python3 /home/user/New/corner-office/tools/tric.py /tmp/YOURNAME_check.md` and break the runs it lists.
4. Report: per chapter, words before → after, fragment % before → after, dialogue % after, tricolon hits before → after, and anything you could not fix.
