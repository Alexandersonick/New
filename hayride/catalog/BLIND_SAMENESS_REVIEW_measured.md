# BLIND_SAMENESS_REVIEW — MEASURED row (Continuity Audit re-run)

- **Title under review:** MEASURED-H (finished manuscript, surface-stripped fingerprint)
- **Gate stage:** Catalog Novelty Gate, Continuity Audit re-run (measured, not planned; the concept PASS is not inherited)
- **Reader:** independent blind reader (did not write the concept, architecture or manuscript; did not open the architecture fingerprint, the measured JSON, or any earlier review)
- **Inputs read:** `stripped_measured.md`, `stripped_shelf.md` (PRIOR-1), `stripped_candidates.md` (A, B, C), `stripped_batch2.md` (A2, D, E), `similarity_measured.md`, SKILL.md section "Catalog & Series Layer"
- **Comparison set available:** PRIOR-1 (published, cross-lane). The pool rows: A (superseded parent of A2), B, C, D, E (rejected), and A2 (the selected concept, used only for the drift comparison). Two earlier titles under the pen name are **unavailable**.
- **Mechanical triage (attached):** `catalog_similarity.py` 1.1.0 returned **AMBER**. Nearest were A 0.227, E 0.161 and C 0.147, all in the PASS band with no hard failures. The AMBER comes from the short set: 0 same-lane rows and 1 cross-lane row. PRIOR-1 is not among the three nearest.

## Verdict

| Scope | Verdict |
|---|---|
| Against the available set (PRIOR-1 + pool) | **FAIL, on H7 house template only.** The core structure passes: H1, H2, H3, H4, H5 and H8 all pass against PRIOR-1 and every rejected row. |
| Overall gate | **BLOCKED.** Two earlier titles are unavailable. The set is short (0 of 10 same-lane, 1 of 5 cross-lane). The H7 rotation clause cannot be tested with only one prior. |
| Defect to file | `CATALOG_SAMENESS` (device and staging level), routed to the Revision Stack. It is cheap to fix and needs no re-architecture. See "Required actions". |

In plain terms, this is not the same book as PRIOR-1. It is a different plot (0 of 8 core axes match) built from PRIOR-1's devices. A repeat reader would recognise the same hero and the same signature payoff before noticing the plot is new. The rubric's H7 house-template clause fails when the reader can name such recurrences, and I can name several.

---

## 1. Core axes: measured row vs PRIOR-1 (scored by mechanism)

| # | Axis | MEASURED | PRIOR-1 | Match? |
|---|---|---|---|---|
| 1 | Inciting | Public lottery under her own rules; she refuses an offered redraw by citing the rule (choice under pressure) | Discovers that her twin has been impersonating her with his ratification (discovery/betrayal) | **No** |
| 2 | Bind | Her self-authored rules (a chair who breaks one steps down) plus a cash/insurance deadline. On-page cost: she tells the slander story nightly beside him, and a 4–1 formal warning leaves her one more breach | A forgery cancels her contract and she has an injured hand on a fixed deadline. She makes him her hands. | **No.** Partial family: both have a deadline project, and both have an authority issuing one-chance terms (see drift D3) |
| 3 | First irreversible decision | Ch 11/30: withdraws her own story under an author-may-withdraw clause. Price: refunds, revenue drop, ally's hurt | Ch 3: leaves her house key and moves to her unheated workplace | **No** |
| 4 | Midpoint | Ch 14/30: the lie is retired and a true communal story replaces it. Committee adopts 4–3, the pair co-build it in his workspace, ally breaks, press gets the old story | Forgery exposed. Stakes reframe from the marriage to her professional name, and a mentor sets one-chance terms | **No** (constructive replacement vs exposure plus reframe) |
| 5 | Rupture | Her flaw recurs on a goal collision: his true "wouldn't have come back" plus a city offer, and she says "Go" again | His harm recurs: he "helps" alone and causes permanent damage, then reports it himself | **No** by mechanism (her send-away vs his unilateral damage). Same family: an old pattern recurs. **Flag:** in both books the hero self-discloses the damaging fact |
| 6 | Climax | She leads. She breaks the belt rule and publicly retells the true story, indicting herself. He answers one rider's question from the bench. She enforces the penalty on herself | Joint. On her spoken count with the certifier watching, he performs the delicate work and stops where she says "leave it" | **No** |
| 7 | Repair | Inverted grovel. His side: sustained truthful presence plus a declined offer. Her side: a staged public correction ladder ending in "Stay." | Being taught by her, on her terms: an apprenticeship that fails, then succeeds | **No** by shape. **Flag:** her ladder opens with a failed attempt (fail-first rhythm) |
| 8 | Resolution | Full reconciliation, "I love you", proposal promised with the yes given in advance. No time skip; next-morning teardown; object at rest | Renegotiated reconciliation built on lists of asks. Epilogue months later; one-word spoken last line | **No** |

**Count:** 0 of 8 strict. The most lenient reading counts the axis 2 and axis 5 families as half-matches, giving 1 of 8. **H1 PASS.**

## 2. Core axes and staging vs every pool row

| Row (status) | Core-axis matches | Staging matches (of 5) | Notes |
|---|---|---|---|
| **A** (superseded parent of A2) | **5/8**: inciting, bind, rupture (same question, same "no"), climax (she tells the true story incl. her fault to riders), repair (sustained presence plus a declined rehire) | **3 firm + venue partial** (riders, confession, her own choice; wagon/dock vs moving vehicle) | **Lineage, not a catalog collision.** A2 itself scores 5/8 vs A on the same axes, so the pipeline accepted A as this title's ancestor. **But** the measured staging re-converged on A: A2 vs A was about 2.5/5, and the measured row vs A is 3–3.5/5. H5 (climax plus repair) and H8 clause 2 would trip if A counted as an earlier book. See drift D9 and residual risk R1. |
| B (rejected) | 0/8 | 0/5 | Inverse of B's rupture: B's hero decides for both; here she decides for him |
| C (rejected) | 0/8 | 0/5 | — |
| D (rejected) | 0/8 (rupture is a half-family match) | 1/5 (her own choice) | Rupture echo: in D he refuses to be the reason she stays; here he refuses to let her decide for him |
| **E** (rejected) | 2/8: inciting (chance pairing), bind (pairing lock plus money deadline). Half-family matches on rupture (goal collision read as "leaving again") and repair (public confession, inverted actor) | **2 firm + spectacle partial** (stage, confession; "room turns" silently vs audibly) | Nearest rejected row. Two of three shape axes repeat E's (choice under pressure, public confession). E's climax plus repair pair does **not** repeat (E: he withdraws and confesses; here: she confesses), so H5 is not tripped. E's midpoint mechanism (a third party spreads the old wedding story) migrated into the measured midpoint cost and rupture (old story to the press; the paper prints the ally's version). |

## 3. Hard-fail conditions

| # | Result | Basis |
|---|---|---|
| H1 | **PASS** | PRIOR-1 0/8, B 0, C 0, D 0, E 2. A is 5/8, but A is lineage (see above) |
| H2 | **PASS** | No shared run of four ordered macro-beats with PRIOR-1 or with any rejected row |
| H3 | **PASS** (with a note) | Swap away her authorship of the story and her effects-building, and axes 1 (the rules and story she owns), 3 (author-may-withdraw), 4 (withdraw and replace) and 6 (lifting her own lantern, retelling her own story) all change. **Note:** his trade is causal only at the midpoint co-build. The rupture offer and his climax line survive any job swap |
| H4 | **PASS** | Nearest shelf book PRIOR-1: 8 core differences, all mechanisms (well over the 3 required) |
| H5 | **PASS** (flags) | Against PRIOR-1, climax plus repair does not repeat and the shape triple matches 0 of 3. Against E, two shape axes match but E's climax plus repair does not. A is not counted (lineage). **Flag:** the measured repair shape moved from sustained presence (A2) to public confession, E's shape |
| H6 | *Out of scope (mechanical).* **Referral** | "He didn't…" restraint at 52× matches PRIOR-1's signature clipped "he did not" restraint. Both narrators are numerically precise, with exact times and money. Both have near-zero em dashes. Run `series_diff.py`; expect VOICE CONVERGENCE. The **1,000-word blind voice test is recommended now** and becomes mandatory on any flag |
| H7 | **FAIL (house template)**. Rotation clause **BLOCKED** | See §5. Rotation clause: care-object-and-service is PRIOR-1's primary device and the measured book's dominant device from the second care beat onward. With the two other priors unavailable, three in a row cannot be ruled out |
| H8 | **PASS** | PRIOR-1 0/5 (venue is only adjacent: both climaxes sit on the heroine's own work site). E 2/5, with spectacle partial. A is excluded as lineage: 3–3.5/5, and clause 2 would trip |

## 4. One-beat-sheet test

Sheet written for the measured book:
1. A public draw under her own rules seats her beside the ex she has publicly maligned in a story she wrote, and she refuses a redraw.
2. Her rules and a revenue deadline keep her telling the slander nightly beside him, and a committee warning makes the next breach her last.
3. She withdraws her own story at a visible cost.
4. A true communal story replaces the lie and is co-built with him. The ally breaks with her and the old story reaches the press.
5. His truthful "no" plus a city offer trigger her repeat send-away, and the paper prints the lie.
6. On the final ride she breaks the safety rule and publicly retells the story against herself. He answers from the bench.
7. His sustained truthful presence and declined offer meet her self-imposed step-down and "Stay."
8. Full reconciliation, a promised proposal, and the next-morning teardown with the lantern at rest.

The sheet fits PRIOR-1 at 0/8, A2 at about 4/8, A at about 3/8, E at about 1/8, and B, C and D at 0/8. **It fits no comparison book: PASS.**

## 5. House-template question (H7): what a repeat reader clocks before the plot

**What does not recur:**
- Inciting kind (choice under pressure vs discovery)
- Midpoint shape (constructive replacement vs exposure plus reframe)
- Last-image class (object at rest vs spoken line)

**What does recur** (the PRIOR-1 habit checklist):

| PRIOR-1 habit | In the measured book? | Evidence |
|---|---|---|
| Heroine-imposed terms | **Echo (moderate)** | Her laminated rules govern everyone, he included, and she cites them against the redraw. These are self-binding rules, not terms imposed on him. *Unverifiable from the row:* who proposed the nightly question engine. A2 locked it as his offer specifically to avoid this habit (R2) |
| Hero as silent hands on her deadline build | **Echo (moderate)** | He co-builds the deadline finale (in his workspace, with his trade making it possible). In repair, "holding the light" is literally silent hands on her work |
| Apprenticeship on her terms | Absent | Inverted: she enters his shop |
| Climax on her spoken cue with an official watching | **Migrated, not removed** | The climax itself is clean: she speaks and he answers a rider. But the bind has him "cue his own villain role **on the exact word**" nightly, which is the same precise compliance as PRIOR-1's "stops exactly where she says 'leave it'". The vice-chair ally watches the climax and ratifies it ("I was wrong") |
| Reconciliation built on lists of asks | Weak echo | He "asks for nothing". The nightly one-true-answer ledger and the pre-answered proposal are an itemised-exchange grammar, but not lists of asks |
| One-word spoken payoff | **Present (strong)** | "Go" → "Stay." is the heroine's capstone line and a one-word spoken mirror callback, PRIOR-1's signature ending device. It is no longer the last line, but it is the emotional payoff |
| Numerically precise heroine | **Present (strong)** | "Exact times and money figures"; vote tallies 4–1 and 4–3; 32 riders; her attention goes to timing |
| "He did not" restraint | **Present (strong)** | "He didn't…" 52×. Restraint is also promoted to the first care beat ("restraint as care"), so PRIOR-1's hero signature moved from voice into a device slot |

**Repair staging rhythm:** partial recurrence. PRIOR-1's repair is fail-then-succeed. The measured heroine-side ladder opens with a failed softened line, then escalates to success. The hero side is steady, with no fail step. The witness pattern also recurs: in both books the hero self-reports the costly fact (PRIOR-1: he reports the damage; measured: he discloses the offer, then reports the decline's cost), so neither book uses secret-then-discovered.

**Devices:** care-object-and-service is primary in PRIOR-1 and dominant in the back half of this book. "Mending her porch light unasked" is the same act as PRIOR-1's rupture (unasked help on her property), now signed as care. It also contradicts the row's own "care without fixing" label.

**Answer:** a repeat reader of PRIOR-1 would clock four things:
1. The same restrained hero (the "he didn't" cadence plus quiet object service).
2. His exact-word compliance to her cue.
3. The one-word spoken callback payoff.
4. The numerically precise narration.

Under H7's house-template clause, naming any one recurring device fails the gate. **H7 FAIL.**

## 6. Structural drift: A2 (selected concept) → MEASURED

Direction key: **→P1** means toward PRIOR-1. **→HT** means toward the house template or genre default. →A, →E and →D mean toward that pool row. "Away" means away from PRIOR-1.

| # | Field | A2 (planned) | MEASURED | Direction |
|---|---|---|---|---|
| D1 | Axis 2 bind consequence | Breaking her rule hands leadership to a rival who would fold the event | The chair who breaks a rule steps down. The rival is removed | Neutral |
| D2 | Opposition (field 11) | A rival leader pushes the story as "official history" | A loving vice-chair ally, a voting committee, and the press | →E (votes, third-party spread of the old story) |
| D3 | Bind on-page cost | Not specified beyond the revenue pressure | A **4–1 formal warning: one more breach and she steps down** | **→P1.** This is PRIOR-1's midpoint "mentor sets one-chance terms", moved into the bind |
| D4 | Axis 3 FID | Run 1: she tells the unfair story as written and profits ("the groom is riding") | Ch 11/30: she withdraws her own story at a cost. A2's run-1 telling became the bind's nightly cost | Moved later (agency becomes irreversible about 8 chapters later); →HT (passive-endurance stretch risk, ch 1–10). Not →P1 |
| D5 | Axis 4 midpoint | Run 5: costly change of plan; she cuts her own finale effect and sales drop | Ch 14: the true communal story (from the landowner) is co-built **in his workspace** and adopted 4–3; ally breaks; press | **→P1** (hero's hands on the deadline build, venue inverted); →E (committee vote; old story weaponised) |
| D6 | Axis 5 rupture | Truth "no" plus the old employer's higher rehire: truth meets open exit | Truth "no" plus a city offer. She says **"Go" again**; brother names her pattern; he refuses to be decided for; paper prints the lie | **→P1 / →HT** (rupture became "core flaw recurs", PRIOR-1's repeated-core-harm family); →D (he refuses her unilateral decision); →E (public spread of the old story) |
| D7 | Axis 6 climax (who and what) | She unbelts and goes to the effect site to **play her own lantern ghost** while telling the truth. **He keeps the riders seated and takes over the narration** | She walks the dock, lifts the lantern and retells. **He gives one line from the bench** in answer to a rider. She self-enforces the step-down. Ally says "I was wrong" | →A (hero's act shrinks to a line); **→P1** (official-ish witness ratifies); mirror-line payoff →P1 device |
| D8 | Axis 7 repair | Sustained unglamorous presence (early-morning grunt work), unwitnessed, then declines the rehire and tells her the same day | **Inverted grovel.** His side: one true answer a night, plus **care-object-and-service (held light, porch light mended unasked, note)**, plus the declined offer. Her side: a **ladder that opens with a failed attempt**, ending in **"Stay."** | **→P1** (P1's primary device; fail-first rhythm; one-word spoken payoff; the unasked-mending act from PRIOR-1's rupture); →E (public confession shape) |
| D9 | Climax staging: venue | Effect site on the trail | Stage of a live performance (dock and wagon at the finale stop) | →E ("stage"); →A (the wagon is back in the frame) |
| D10 | Staging: evidence | Act performed + confession | Confession only | →A, →E. **Away** from P1 (P1 = act performed) |
| D11 | Staging: spectacle | Quiet tally | Silent room-turn; lanterns lifted toward the bench | →E ("room turns", with the volume knob turned down) |
| D12 | Staging: audience | Riders | 32 paying riders plus the ally (an official) plus a child | Mild →P1 (an official watching) |
| D13 | Shape triple: repair | Sustained unglamorous presence | Public confession (inverted), with the hero side as sustained presence | →E (two of three shape axes now equal E's) |
| D14 | Axis 8 resolution | Reconciled; teardown morning; unlit lantern on a nail **beside two raffle stubs** | Full reconciliation plus "I love you" plus a **proposal promised with the yes given in advance**; lantern alone on the nail | Mild →P1 (terms settled in advance); →HT (proposal) |
| D15 | Question engine origin | **His offer** ("ask me one thing every run") | Who offered is not recorded in the row | Unknown. If it is hers, →A and →P1 (heroine-imposed terms) |
| D16 | Heroine goal payoff | The cost includes "the story that funded her season" | The cash or insurance outcome is not recorded | Unknown (dangling external goal, or A's word-of-mouth fix: →A) |
| D17 | Voice (form field 18) | Not specified at concept | "He didn't" 52×; exact times and money; near-zero em dashes; filter words at threshold | **→P1** voice signature |

**Stable fields:** inciting kind and mechanism; her craft and authorship functions; heroine goal (revenue/insurance); climax authority (her own choice); no time skip; object-at-rest last image.

**Net drift:** structurally the book stayed far from PRIOR-1 (0 of 8). Every change at the device, staging and voice level moved **toward PRIOR-1's habits** (D3, D5, D6, D7, D8, D14, D17), **toward rejected E** (D2, D5, D9, D11, D13), or **back toward superseded A** (D7, D9, D10). No change moved toward a new, unclaimed shape.

## 7. Repeat-reader question

**`could_write_the_same_book_review` (vs PRIOR-1): false.**

- **Why false:**
  - The lane differs (second-chance holiday vs marriage crisis).
  - The inciting kind differs (her own rule under public pressure vs a twin's impersonation).
  - The engine differs (a public slander she authored vs forgery and injury dependence).
  - The climax differs (her public self-indictment vs his performed act on her count).
  - The repair shape and the ending class differ.
  - The epilogue timing differs (next morning vs months later).
  - No beat of the one-beat sheet transfers.
- **What can still be written:** a "same hero, same voice" review: *"He's the same quiet guy who 'didn't' do things and silently fixes her stuff, she counts everything to the minute and the dollar, and it lands on one word again."* That is a narrower complaint, but it is the half of the trigger review ("same old book… characters' names and occupations changed") that a voice-level reader produces. It is why H7 fails and why the H6 voice test is recommended.

## 8. Recognizability lines (no names, jobs or places)

- **MEASURED:** *The one where she has to tell, every night beside him, the ghost story she wrote making him the groom who abandoned her, and ends it by telling the crowd she was the one who sent him away.*
- **PRIOR-1:** *The one where her twin has been living her life with her husband's blessing, and she makes him her injured hands to finish the job a forgery cost her.*

These lines need no help to tell the books apart. **PASS.**

## 9. Residual risks

- **R1 (lineage re-convergence):** the measured row is 5/8 against superseded A. Its climax staging re-converged on A (wagon in frame, confession only, hero's act reduced to a line). That is acceptable only if A was superseded for reasons unrelated to PRIOR-1 or house-template proximity. The caller should check A's supersession note. If A was dropped for heroine-imposed terms or P1 proximity, D7, D9, D10 and D15 are material.
- **R2:** the origin of the question engine is not recorded. If the manuscript has **her** proposing "one true answer a night", PRIOR-1's heroine-imposed terms are fully back. Check this in the manuscript.
- **R3:** the revenue/insurance outcome is unrecorded. It is either a dangling goal or A's word-of-mouth resolution.
- **R4:** irreversible agency arrives at ch 11/30, later than A2's run 1. Chapters 1–10 risk reading as endurance. The redraw refusal and the softened line mitigate this only partly.
- **R5:** his trade is causal only at the midpoint (H3 note). The rupture offer and climax line are job-agnostic.
- **R6:** the row contradicts itself: "care without fixing" vs "mending her porch light unasked". The unasked mending is PRIOR-1's rupture act, re-signed as care.
- **R7:** shape-axis flag against rejected E (two of three). E's staging (stage, confession, room turns) is also two to three of five from this climax.
- **R8 (short set):** with two titles unavailable, every PASS line above is provisional. The H7 rotation clause is untestable. Care-object-and-service, primary in PRIOR-1 and dominant here, fails rotation outright if either missing title also used it as primary.
- **R9:** mechanical triage ranked A at only 0.227 although the blind read finds 5/8. Tag wording hides function-level matches, which is the "never collide by string" problem. Do not read the low triage scores as distance.

## 10. Required actions (to clear the measured-row FAIL)

All of these are revision-level, not re-architecture:

1. **Payoff:** replace the "Stay." one-word mirror capstone with an act, or with a line that is not a one-word callback. Alternatively, keep the word but let the act carry the payoff and keep "Go/Stay" out of final position in both the chapter and the scene.
2. **Exact-word compliance:** cut or re-own the "cues his villain role on the exact word" beat. Make his timing his own initiative, not precision to her word.
3. **Care device:** reduce care-object-and-service dominance in the back half. Convert the unasked porch-light mending (PRIOR-1's rupture act) into a non-object care device, or make it something she asked for.
4. **Voice:** cut "He didn't…" from 52 to a low count, and vary restraint forms. Then run `series_diff.py` and the 1,000-word blind voice test against PRIOR-1's hero POV.
5. **Fail-first opener (optional):** consider dropping the failed softened line that opens her correction ladder, to break the fail-then-succeed rhythm echo.
6. **Verify R2 and R3** in the manuscript, then re-score.
7. **Overall gate stays BLOCKED** until the two unavailable earlier titles (text or filed fingerprints) are back-filled and the H7 rotation clause can be tested.

---

## 11. Remediation applied (author side, after this review) and re-measurement

*Written by the pipeline author, not by the blind reader. It records what changed in the text and what was re-measured. Under the blind-scoring rule, the H7 clearance is the blind voice test below plus the mechanical re-run. It is not a self-scored count.*

| Required action | Applied | Where |
|---|---|---|
| Replace the one-word "Stay." payoff | Done. Danny's "say the other thing, it's shorter than *go*" [25, 29] is now a setup that she **refuses**. She names her own terms instead: *"When you ask, ask on a Tuesday... I'd like one thing in my life that doesn't come with a crowd and a cue. And the answer's yes."* He writes TUES in the frost on the dock board and says "Noted," the way he'd answer a cue on a headset. | ch30 |
| Cut the exact-word cue beat | Done. Her ch3 praise "You hit it on the word" is now a craft observation: he works the toggle with his thumb and keeps four fingers on the rail ("You never let go of anything to take a cue"). "On the word" was cut at ch28, and "He didn't flip it early" was cut at ch27. The ch17 "Don't flip it early" exchange stays, because it belongs to this book's own Woodlot pull-early motif, which pays off at ch19. | ch3, ch27, ch28 |
| Cut back object-and-service care in the back half | Done. **The porch-light repair (PRIOR-1's rupture act) is removed.** On the old wedding date, Roz fixes her own porch light in eleven minutes ("It had taken her two and a half years to find eleven minutes"), and Lorna reports that Clyde lost money betting Gus would do it. From ch20 on, his only object act is the shop door [26], which is his own building, not her house. | ch20, ch21 (timestamp) |
| "He didn't" well below 52 | Done. Sentence-initial "He didn't / He did not" in narration went from 52 to **11**. Gus's restraint chains became stage-manager cue-calling ("Standby whistle... Whistle. Hold." [2]; "Bark, go" [17]; "Blackout" [12]), object-talk and self-mocking asides set in parentheses, which is the Voice Contract device. The two near-identical "He didn't ask her why. Not between the 8:20..." paragraphs [6, 11] were rewritten so they no longer share a template. | ch2, 4, 6, 7, 8, 9, 11, 12, 15, 17, 18, 19, 21, 24, 26, 27, 28, 29 |
| Fail-first repair ladder (optional) | **Kept, by decision.** The failed softening [5–6] is the setup that makes the withdrawal [11] cost something. It is recorded here as a SAMENESS_VERDICT item so that the next title under the pen name rotates it out. | none |
| Check question-engine origin | **His offer**, on the page at ch3 ("every ride, you can ask me one thing"). This matches A2 (D15 resolved, away from heroine-imposed terms). | ch3 |
| Check revenue outcome | On the page. The goal is met at $29,350 [23], with FINAL $36,410 [29], and the new wagon's DOT specifications are due to Great Lakes Mutual [30] (D16 resolved, external goal paid off by her craft). | ch23, 29, 30 |
| Back-fill the two missing titles | **Not possible in this session.** No text or fingerprint exists for either title. The overall gate stays **BLOCKED**. | none |

### Blind voice test (H6 / H7 voice clause), `blind_voice_test`

- **Round 1 (INVALID).** All three readers paired the samples correctly. Anonymization had leaked recurring names (single letters reused across samples, plus Cora, Greta, Kessler, Hal Ostrowski and Hale), so the pairing proved nothing. All three also judged Gus and PRIOR-1's hero to be **the same stoic mind**: feeling sent into the hands, "He did X. He didn't Y.", "because" justification clauses, women who hang up first, scenes that close on a gesture. This finding drove the Gus revision above.
- **Round 2 (PASS).** Samples: revised ch21 and ch12 (Gus), plus PRIOR-1 ch8 and ch24 mid-chapter (Declan, numbered-plan openers excluded). Names were replaced independently per sample and the order shuffled. Files: `voice_test/round2_samples.md` and `round2_key.txt`. Three independent readers, each reading only that file.
  - **Reader 1:** paired 1+2 and 3+4 with high confidence. Same man? *Partly*, with "low to medium" confidence that it is one narrator. Perceptual differences cited: time stance (memory vs. the clock), certainty (reads people confidently vs. admits what he can't tell), humor density, syntax, and feeling (B states it as negation).
  - **Reader 2:** paired 1+2 and 3+4 at about 85%. Same man? *Partly*: "a repeat reader would sense two men, though clearly by the same author." Differences cited: time stance, certainty, humor, rhythm (all PERCEPTUAL) and simile source (VOCABULARY).
  - **Reader 3:** paired 1+2 at about 85% and 3+4 at about 95%, and called A and B different narrators at about 80%. Differences cited: attention (object history vs. procedure), time, certainty, and restraint (comic deflection vs. restraint as a moral act), all PERCEPTUAL. Their summary: "two different men inside."
  - **Rule check:** at least 2 of 3 must identify the candidate's samples correctly **and** cite a perceptual difference. 3 of 3 met it. **PASS.**
- **Mechanical re-run** (`reports/series_diff_post_voice_revision.md`): 0 shared tics with PRIOR-1, no house habits, no VOICE CONVERGENCE flag. Sentence-opener Jaccard is 0.290 against the 0.30 threshold; the top openers are pronouns, which close third person shares by default. Narration "because" in Gus chapters went from about 2.5 to about 0.6 per 1,000 words (PRIOR-1 is 2.15). Gus's "hung up" phone-call exits went from 2 to 0 (Mitch's one survives at ch9 as a character trait). Ruth's call now closes warmly, on him.

### SAMENESS_VERDICT items (author-level habits; the test passed but a repeat reader may still notice these)

1. Faces given a will of their own ("her mouth tried something", "the face where she'd put it"). Thinned (ch12, ch23). "Where she'd put it" is kept as this book's own motif for Roz's face (4×).
2. "Looked at X and not at him." Down to 0 in narration.
3. Echo-repeat replies ("Most of it." / "Most of it"). Kept; they are dialogue rhythm. Rotate in the next title.
4. Offstage sound cutting into a tense beat (the tractor through the wall, the heater ticking). Kept. Rotate.
5. "Without looking up / turning around": 16 → 14. Monitor.
6. Similes drawn from the narrator's own trade. This is an intended Voice Contract device. Flag it for rotation so the next hero's similes come from somewhere other than his job.
7. Fail-first repair ladder, kept (see above). Rotate.

### Verdict after remediation

| Scope | Verdict |
|---|---|
| Against the available set | **H7 REMEDIATED, blind re-score not run.** The author cannot self-certify a PASS. A fresh blind H7 read of the revised text is still owed before this row can read PASS. H1–H5 and H8 were unchanged at PASS. H6: blind voice test PASS, mechanical clean. H7: the named recurrences (one-word callback payoff, exact-word cue, unasked mending, "He didn't" restraint, object-and-service as the dominant back-half care) were removed or reduced in the text. The fail-first ladder is kept and logged. The rotation clause still cannot be tested with only one prior. |
| Overall gate | **BLOCKED.** Two earlier titles are unavailable, and the comparison set is short. |
