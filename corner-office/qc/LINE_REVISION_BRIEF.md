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

---

## ADDENDUM after the full-draft hostile read (`qc/HOSTILE_READER_full_draft1.md`)
Structural fixes are **already made** in the chapter files: the fifteen-mornings retellings were
cut from Ch 10 and Ch 22, Pip's terms were removed (Ch 16; Adam adopts telling-before on his
own), the countdown was fixed (test = **Friday 12 Feb**, close of business; Nashville's line stops
Monday 8 Feb), Gil's and Margaret's yeses are business, the "nobody claps" beat and the
pocket speech were cut, the Ch 30 ending was rewritten (same week, radiator chair), and
billionaire markers were added. **Do not undo any of these.**

### Additional book-wide repetition targets (cut your share by the amount shown)
- "two years" (53×): cut by half; use "since Nashville", "since the spring before last", or nothing.
- "looks at me" / "I look at him" / "looks at her" (~65×): cut by half. Use an action instead, or nothing.
- "a long time" / "a long moment" (~43×): cut by two-thirds.
- "before" as a chant ("I'm telling you before", "before, not after", "Before."): cut by a third in Ch 18–30. Keep it where it carries a plot act.
- "like a person", "I'm learning", "I'm asking (you)", "the bad part first": cut each to at most one per chapter, and none in most chapters. These phrases are recognised from earlier books under the pen name.
- **Clock times as voice texture** (6:52, 11:58, 4:40, "at 10:12"): keep a clock time only where the plot needs it, at most two per chapter. Write the rest as "just before seven", "near midnight", or cut.
- **Weld and craft similes** for feelings ("like a weld that held", "like a sheet of glass"): at most one per chapter.
- Glasses-off gestures: Lolo only, at most one per chapter. Remove them from Simone, Stan and Gordon (give each another tell or none).
- Benny's unlit cigarette: at most two mentions in the whole book (Ch 3 and Ch 15). Cut it elsewhere.
- Counting motifs ("that's three", "that's two things I'll give her", "four times"): at most one per chapter.
- Corrective negation in narration ("That's not true." / "Not X. Y."): at most one per chapter.
- "phone face down": at most one per chapter.

### Assignments (expansion quota = words to ADD net, after cuts; measured by prose_metrics)
| Agent | Chapters | Quotas (net words) | Specific tasks |
|---|---|---|---|
| A | 1–5 | Ch1 +100 · Ch2 +400 · Ch3 +400 · Ch4 +250 · Ch5 +250 | **Ch1:** cut backstory facts to about 4 (D-02): drop the napkin/First Communion frame line, the 2018-engineers anecdote, Elvin's newspaper, and Lolo's Lindqvist history, or move it to Ch3; record Ch1's dialogue below 25% as the action-set-piece exception. **Ch2:** raise dialogue to ≥25% with a sharper exchange on the floor (Bridget, the sales man, or Simone); add one line naming *a* wound ("Nashville, decided without me") without the coffee detail (D-06). **Ch3:** raise dialogue to ≥25% (Lolo, Benny, Walt). Ch4–5: line pass. |
| B | 6–10 | Ch6 +700 · Ch7 +250 · Ch8 +450 · Ch9 +200 · Ch10 +450 | **Ch6:** expand the kitchen scene with a real exchange that changes something visible (dialogue ≥25%). **Ch8:** dialogue scene with the crew or Stan. **Ch10:** the fifteen-mornings memory has been cut; do NOT reintroduce it. Add depth to the Kurt dinner (Kurt's pressure made concrete) or the kitchen. |
| C | 11–15 | Ch11 +500 · Ch12 +450 · Ch13 +300 · Ch14 +350 · Ch15 +200 | **Ch12:** dialogue ≥25%. **Ch13:** dialogue ≥25% (Odell or Gordon); convert Adam's numbered legal-pad list into prose or cut it (procedural-numbered-plan house habit). Keep the Ch 15 boardroom beats exactly. |
| D | 16–20 | Ch16 +250 · Ch17 +200 · Ch18 +150 · Ch19 +350 · Ch20 +500 | **Ch20:** dialogue ≥25%; expand the break-room panic as a scene with the crew pushing Pip, so the pressure that makes her go on TV is on the page. Keep Ch16's new no-terms ending. |
| E | 21–25 | Ch21 +150 · Ch22 +350 · Ch23 +200 · Ch24 +200 · Ch25 +250 | **Ch22:** it is a REFLECTIVE_SEQUEL (Adam alone), so low dialogue is allowed, but add the Simone call depth rather than interior. Do not reintroduce the fifteen-mornings detail anywhere before Ch 25. **Ch25** is the only full telling; make it land. |
| F | 26–30 | Ch26 +200 · Ch27 +400 · Ch28 +150 · Ch29 +300 · Ch30 +150 | **Ch28:** keep the vote exactly (the amendment, Pip writes NASH, the tally 97–41–3, Benny's press brake). **Ch30:** the final two paragraphs must stay as written (the radiator-chair ending). Ch 29–30: thin the "before" and "like a person" chant hard. |
