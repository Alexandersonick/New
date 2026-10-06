# CATALOG_STORY_FINGERPRINT (measured): *Two Tickets to the Haunted Hayride*

| | |
|---|---|
| book_id | standalone / *Two Tickets to the Haunted Hayride* |
| source | manuscript (measured row) |
| filled_by | read of the full text, all 30 chapters (scratchpad `hr/draft_v2.md`, 68,788 parsed words), plus `series_diff.py` measurements (prior: `twin_sister.md`) on this file |
| not consulted | story bible, chapter map, concept candidates, architecture fingerprint. This row measures what the text does. It does not check drift against the plan. |
| date | 2026-10-06 (revised the same day after BLIND_SAMENESS_REVIEW_measured H7: rows marked *rev* reflect the post-review text; *rev P15* rows reflect the Phase 15 hostile-reader revisions: recycled names renamed (Teague→Ambrose, Joan→Marlys, Mitch→Vince, Teo→Nico, Lou→Gil); "sitting face" charm-witness cut [4]; explicit answer-length ladder cut [18]; "You said flashlight" obedience line replaced [8]; Gus refuses her direct order at the hitch pin and is logged into the Grange minutes for it [13–14]; Roz's off-the-record correction to the reporter [16]) |
| machine row | `fingerprint_hayride_measured.json` (schema 1.1, evidence_level FULL_TEXT, lane `sweet_small_town_holiday_second_chance`) |
| exact sub-lane | second chance with an ex-fiancé, under forced public proximity at a seasonal small-town event |
| triage | `catalog_similarity.py` against the twin-sister row: score 0.080, PASS band, no hard failures (AMBER only because the comparison set is short) |

Chapter numbers are in brackets. Quotes are verbatim from the manuscript.

---

## Core structural axes (8)

### 1. Inciting disruption
**What happens:** at the town's Harvest Supper, about 90 people watch the hayride chair draw the guide pairs from a jar on stage. She wrote the rules herself and laminated them:
- rule 7: no swaps, and "a guide who leaves her draw leaves the season"
- rule 12: "a chair who breaks a rule steps down"

She draws her own name, then the man she was engaged to seven years ago. For six seasons he has been the villain of the ghost story she wrote for the hayride's finale [1]. The vice-chair comes up and puts her palm on the jar: *"Put it back. Draw again. Nobody will say a word."* The heroine answers: *"Rule seven."* [1]

**Who causes it:**
- **Chance.** The draw.
- **The heroine, by choice under pressure.** She enforces her own rule against a public offer to redraw: *"If I put it back, the Seat War was for nothing."*
- **The hero, by a prior yes.** He agreed to guide in the summer, "before I thought about what that meant" [2]. He offers her an exit twice: *"I could say I've got a conflict"* [1], and he gives her a second to pull the ticket back.

**Medium and audience:** in person, read into a microphone in front of most of the town. The ticket halves are pinned inside each other's coats.

**What turns it into a disruption** is the first ride [3]. He hits the whistle cue for "the 6:10" on the word, a rider stage-whispers *"That's him. That's the guy,"* and *"thirty-two people turned their heads."* After that, every ride performs her published version of their breakup with him sitting in it.

**Inciting kind (shape):** `choice_under_pressure`. The draw is chance. What breaks the equilibrium is her public choice to honour it.

Function class for scoring: **forced proximity by lottery, made binding by her own rule**.

### 2. The bind
**Stated reason:**
- Her own rules (7, 12, and rule 3: the finale is told as approved; the committee votes on changes) [1, 6].
- The money. The hayride needs **$29,000 by January 1** for a new wagon or the insurer drops it, and the ghost story is what sells: *"If we don't make it, Great Lakes drops us and there is no hayride"* [5].

**On-page cost:**
- She tells the story that casts him as the man "still choosing the city" seven times a night, beside him, while the wagon turns to stare [3–6].
- Popcorn is thrown at him [4], the line on the road chants *"SIX-TEN!"* [4], fans arrive with signs [4].
- When she softens the last line, she gets a refund demand and an emergency committee vote: a formal warning, 4–1. One more breach means rule twelve [6].

**His side of the bind:** rule 7 holds him too. He chooses to stay: *"Tell it like it's written... I'll sit there and hit the whistle"* [3].

### 3. First irreversible decision
**The act:** [11]. Mid-season, on the third Friday, she withdraws the Lantern Bride at the pond under the author clause of rule three ("An author may withdraw her story"): *"I wrote her. I'm the author. And tonight I'm withdrawing her... She's not out there. It's just a pond."*

**Price:**
- 12 refunds ($180) from the busiest group [11].
- About $2,800–3,000 lost that night. The vice-chair rubs the number off the chalkboard [12].
- The vice-chair's hurt: *"Is this for him?"* / *"No. It's for me."* [11]
- A season she can no longer return to. Restoring the old ending would be "just the story with the ending changed" [12].

**Chapter:** 11.

The softened line in [5–6] ("Maybe still deciding") was a probe. She reversed it under the warning ("As approved."), so it does not count as irreversible.

### 4. Midpoint reversal
**[14] (of 30), carried through [15–17].**
- The 81-year-old landowner tells the true story of the October 1958 night her late husband, then six, was lost in the corn. Forty neighbours searched with lanterns in lines until dawn, and he waited by the pond for "the parade" [14].
- The heroine asks the owner before she asks the committee: *"It's yours. It's not mine."* The committee adopts it 4–3. One member switches because he gets a new line ("Take one. We're looking for somebody.").
- The couple co-build it in his barn [15]. He shows her kerfing to hide the reeds rig; she teaches him "touch, flow, off" soldering.
- The first lantern ride works [17]: *"That's finished,"* says the fan who demanded a refund.

**What flips:**
- the lie is removed and replaced with a true story
- bench adversaries become co-builders
- revenue goes from loss to recovery (by [23] the target is passed)

**Cost:**
- the vice-chair's open break: *"I'm not putting my hand up for the next one. Don't ask me to cry at it."* [14]
- the old story is still alive in public. The vice-chair gives it to the newspaper [16], and it runs on the front page [22].

### 5. Rupture / lowest point (mechanism)
**Mechanism:** her core flaw recurs on a goal collision. Repeated core harm, done by the heroine.
1. **[21]** The hero is offered head of a new big-city scene shop: $84k, crew of eight, answer by Monday.
2. **[23]** She asks the question she has held back all season: *"Would you have come back if the job hadn't ended?"* He answers true: *"No."* She ends the question ritual: *"That's the last one. I'm done asking."*
3. **[24]** He tells her about the offer in person and says he has not decided. She says ***"Go."*** He names it: *"That's what you said last time... You don't get to make it easy for me this time."* He walks home and leaves his truck in the field.
4. **[25]** She sits at the kitchen table with the rooster salt shaker from the original breakup. Her brother names the pattern: *"You say go first. You say it before anybody can leave, so it's your idea and not theirs."* He traces it to their mother and to his own college plans. Then: *"Stay. It's one word. It's shorter than go."*

**External pressure:** the newspaper prints the vice-chair's version on the front page, "CARROW'S FAVORITE GHOST HAS A GROOM. HE'S BACK." [22]

### 6. Climax action
**What:** [28], the last ride on Halloween.
- She tells the true search story first. She has already told the tractor driver to leave the engine off "however long it takes".
- When a rider demands the bride, she unbuckles (breaking rule one, "guides stay belted from barn to barn"), walks the dock, lifts the unveiled lantern off its line and switches it on.
- She retells the original story truthfully: the price-tagged veil, his offer to take her and her brother, his offer to wait and drive home every weekend, her "Go. Don't call."
- *"She was never waiting. She sent him."*
- A nine-year-old asks *"Is that true?"* She answers: *"It's true. I'm the one who sent him."*
- A rider asks where the groom is. The hero, still belted on the bench, answers in five words: ***"Right here. Choosing this one."*** It mirrors the ghost story's "Still choosing the city."
- The riders lift their lanterns toward the bench, not the pond.

**Caused by:** the heroine (`heroine_led`). His one line completes it. He does not reach for her: *"He just held his hand down to her from the bench, palm up... and waited for her to decide."*

**Coda [29]:** in the shed she reads rule one and rule twelve aloud and steps down as chair. The vice-chair says *"I was wrong"* and takes the handbook.

### Climax staging (5, scored as a set)

| Field | Value | Evidence |
|---|---|---|
| `climax_venue` | `stage_or_broadcast` | The finale stop of a performed attraction: the dock and the wagon at the pond, mid-show [28] |
| `climax_audience` | `paying_public_strangers` (other) | 32 riders who paid, mostly out-of-towners in costume (one has driven from Sturgis "for a bride"), plus the vice-chair, a child and the tractor driver. Not the whole town and not an institution [28] |
| `evidence_delivery` | `confession` | Her own retelling. No documents and no witness [28] |
| `decisive_authority` | `heroines_own_choice` | She breaks the rule, makes the confession, and later enforces the penalty on herself [28, 29] |
| `spectacle_mode` | `room_turns_silently_collective_gesture` (other) | *"It wasn't a sound, exactly. It was the thing a room does when it turns... only this time nobody looked at him."* Then lanterns are lifted row by row toward the bench. The driver: *"that's the best one anybody ever told here."* [28] |

### 7. Repair / grovel mechanism
**Inverted grovel.** The founding harm is hers: she sent him away, then defamed him for six years in a public story. So the staged repair is her public confession. His repair, for obeying "go" because it was easy, is sustained truthful presence.

**His changed-behaviour acts:**

| # | Act | Witnesses | Chapter |
|---|---|---|---|
| 1 | Apologises "for how I left", asks nothing: *"I'm not asking for anything for it"* | Her | 3 |
| 2 | Offers one true answer a night, "Not nice. True." He answers against his own interest: the ring was sold for rent [4]; not calling was "the easiest thing I ever did... And I've hated that ever since" [6]; "I hated the whistle" [11]; the ex who said he kept a room shut [13]; his want [17]; the diner vigil [18]; "No" [23] | Her, with the wagon in earshot | 3–23 |
| 3 | Cues his own villain role every ride and never defends himself. To the newspaper: *"It's her story. I don't have anything to add to it."* | Riders, town, press | 3–11, 22 |
| 4 | Keeps her secret from her brother: *"If you want the rest, it's hers. Ask her."* | Brother | 9 |
| 5 | Sits in the dunk tank for the wagon fund | Town | 7 |
| 6 | Holds the light for eighty minutes and never offers to fix, for his own reason: *"Because it's your rig... Everybody hates that guy."* (*rev P15*: was "You said flashlight") | Her | 8 |
| 7 | *rev:* removed. He tells her in the truck that he knows what tomorrow is ("I just know"); the porch light is now fixed by her, alone, on the old wedding date [20] | Her | 20 |
| 8 | Discloses the offer in person and refuses to let her "go" decide for him | Her | 24 |
| 9 | Declines the offer for his own reasons, hangs the door with his shop's name, and reports the real cost from the doorway (the lost overflow work, $20–30k a year): *"Not for you... Well. Not only."* | Her; old boss; mother | 26 |
| 10 | Stays belted and answers *"Right here. Choosing this one."* | 32 riders | 28 |
| 11 | *"Sit with me next year."* He says it as a statement, not a question | Her | 29 |

**Her changed-behaviour acts:**

| # | Act | Witnesses | Chapter |
|---|---|---|---|
| 1 | Softens the line. It fails: refund, warning, and she reverts | Riders, committee | 5–6 |
| 2 | Withdraws the story | Riders, vice-chair | 11 |
| 3 | Gives the true finale to its owner before the committee | Elder | 14 |
| 4 | Says *"I'm sorry"* in public, in the hardware store: "For six years of the pond." | Store owner, two old men | 22 |
| 5 | Makes the dock confession | 32 riders | 28 |
| 6 | Enforces rule twelve on herself and steps down | Committee, volunteers | 29 |
| 7 | *rev:* Names her own terms instead of the word her brother handed her: *"When you ask, ask on a Tuesday... And the answer's yes."* He writes TUES in the frost | Him | 30 |
| 8 | Changes how she says go: tells her brother "go. And come home Sundays. And call." | Him (reported) | 30 |

**Repair shape:** `public_confession`, by the heroine. Hero side: `sustained_presence`.

**Staging rhythm:** incremental self-correction, and the first attempt fails [6]. The truth moves from a pencil note [5] to a withdrawal [11], a substitution [14], a private apology in public [22], and finally a public confession [28].

### 8. Resolution & epilogue shape
**Resolution shape:** `full_reconciliation`.
- *"I love you... I have the whole time."* / *"I love you too. I've never once said it out loud in this town."* [29]
- He announces that a proposal is coming, "here, on purpose, because I decided to". *rev:* She answers with her own terms: ask on a Tuesday, the answer's yes; he writes TUES in the frost on the dock board [30].
- The ring was sold [4]. None is replaced.

**Side resolutions:**
- The vice-chair concedes [29], becomes chair, writes "rule thirteen" appointing the heroine effects lead, and invites both mothers to Thanksgiving [30].
- The brother applies to a four-year school [30].
- The target is exceeded: $36,410 FINAL [29].

**Epilogue device:** no time skip. [30] is the next morning, when the town strikes the hayride.
- Off the clipboard, she does not know where to stand.
- She takes down the fog rig and the pond line ("That's the whole ghost." / "It always was. That's the trick.").
- "Hold the flashlight." / "It's daytime." / "I know." This calls back to [8].
- The silent volunteer gives her an empty cigar box: "Starts with one." Both ticket halves go in together.
- The Bride's lantern is hung on the empty hook where the dog collar used to hang.

---

## Shape classifications

| Shape axis | Value |
|---|---|
| Inciting kind | `choice_under_pressure` (she honours a chance draw against a public offer to redraw, under her own rule) |
| Repair shape | `public_confession` (inverted: the heroine confesses; hero side `sustained_presence`) |
| Ending-image class | `object_at_rest` (callback: the lantern is first lit at [3], about 10% in, and the collar's hook is set up in [1], [14]) |

**Final paragraphs, verbatim:**

> It hung on the old iron nail on the barn wall in a bar of November sun from the high window, with no veil and no light, a two-dollar hurricane lantern from a Goodwill in Kalamazoo.
>
> Its glass held the light from the window, and it was still.

**Shape triple:** choice_under_pressure / public_confession / object_at_rest.

---

## Macro beats (story order)
1. `public_lottery_pairs_exes` [1]
2. `heroine_tells_maligning_story_beside_him_nightly` [3–6]
3. `heroine_withdraws_own_story_at_cost` [11–12]
4. `true_communal_story_co_built_replaces_lie` [14–17]
5. `heroine_initiates_first_kiss` [18]
6. `job_offer_triggers_heroine_repeat_send_away` [21–25]
7. `hero_declines_offer_on_own_terms` [24, 26]
8. `heroine_public_self_indicting_retelling` [28]
9. `heroine_steps_down_and_names_her_own_terms` [29–30] (*rev*; was `says_stay`)

---

## Supporting structural fields (9–15)

### 9. Central relationship problem
**The question the book asks:** *who left whom, and will the person who wrote the story tell the true one?*

The child's question frames it in [5]: *"Did he leave? Or did you tell him to?"* / *"My grandpa says it's always both."*

The deeper question is how the two of them parted:
- She says "go" first, so leaving is her idea.
- He obeyed "go" because obeying was easy.
- The book resolves it by inverting both: she stops saying *go* and, refusing the one-word fix her brother offers, says what she wants in her own terms [30], and he decides for himself ("for once in his life easy wasn't the same as obedient", [24]).

### 10. Protagonist's dominant strategy
`building`. She manages feeling the way she builds scares: control the wait, keep the face "exactly where it was", rig the room.
- Toward the plot, she revises her own story incrementally and procedurally (rules, votes, withdrawal clause).
- Her reflex in the relationship is `exit`, the pre-emptive "go".

### 11. Primary opposition mechanism
1. **Her own published story, institutionalised by a loving ally.** The vice-chair:
   - moves to make it official heritage with a bronze-look plaque (passed 4–3) [10]
   - gives it to the press [16, 22]
   - has repeated it "for seven years... I'm not sorry for taking your side" [12]

   She believes it is true until [28]: *"I didn't know they weren't true."* [29]
2. **The money that rewards the lie.** Fans want refunds when it changes [6, 11]; paper readers ask "Where's the bride?" [23, 27].
3. **The heroine's own reflex**, which produces the lowest point [24].

No villain. The antagonist is affection plus procedure.

### 12. Secret / information architecture
**The core secret:** she sent him. He asked her to come with her brother ("an apartment with two bedrooms"), then asked to wait and drive home every weekend; she said no and "Go. Don't call." He cried in her kitchen.

| Ch | Who learns | What surfaces |
|---|---|---|
| 1–3 | Reader | Only the public version (the ghost story). Hints: the hero refuses to argue about 2019 [4]; the vice-chair's pound-cake visit [1, 9] |
| 5 | Reader | Roz's interior: *"he had asked her to come, and she had said go."* The line is "only true-ish" [3, 5] |
| 9 | Brother (refused) | The hero won't tell: *"it's hers. Ask her."* |
| 16 | Heroine | The friend's half: the night before he left, he sat three hours at the diner over a pie he hates, waiting for her to walk in |
| 16 | Heroine | The brother's half: he heard the whole breakup from the fourth stair and was told "Gus is gone," "like he'd done it to us" |
| 18 | Heroine ↔ hero | She knew about the diner that night and did not go: *"I sat in the kitchen with the phone on the table and I didn't go."* / *"I knew. When the bell didn't go."* |
| 22 | Public | The newspaper prints the false version. The hero declines to correct it |
| 28 | Public | The truth, from the dock |
| 29 | Vice-chair | Concedes she was deceived |

**Hero's secrets, all surfaced by the truth ritual or in person:**
- the ring was sold [4]
- he would not have come back if the job hadn't ended [23]
- the offer: the reader learns it at [21], she learns it at [24]

**Private objects:**
- the quarter-inch model of the pond in his barn. He slides the bead lantern off its line [12] and sets it upright again [24].
- the box "AUGUST, DON'T THROW OUT" with the proposal Polaroid and the veil photo [15, 24]
- her pencil copy of the script in a junk drawer [5, 6]

### 13. Secondary plot engine and collision
**Engine:** the fundraising tally on the shed chalkboard. Each night's number is a verdict on the story choice:
- $2,300 → $6,100 → $9,800 → $13,900 [3–8]
- a smudged-out number and $16,200 after the withdrawal [12]
- $17,400 → $21,900 → $29,350 with the true story [17–23]
- $36,410 FINAL [29]

**Collisions:**
- The lie sells, so truth costs money [6, 11–12].
- The true story beats the lie's numbers, which removes the financial excuse and leaves only the confession [23, 27].

**Tertiary engines:**
- **His one-contract start-up against the Chicago offer** [9, 21, 26]. It produces the rupture, and declining it has a stated cost [26].
- **The newspaper feature** (announced [9], voted [10], interviewed [16], printed [22]). It hardens the lie and brings in the paper-readers who demand the bride [23, 27].
- **The brother's college choice** mirrors her "go" [18, 25, 30].
- **His mother's move** turns her packing into the scene where the heroine labels his boxes [15].

### 14. Signature scenes and technique-bank devices
**Signature scenes:**
- the jar draw and "Rule seven" [1]
- the binder's back page: *"(Front-bench guide: WHISTLE on 'that's the 6:10.')"* [2]
- the whistle hit, and the wagon turns to stare [3]
- the truth-a-night deal [3]
- "Do you still have the ring?" / "No. I sold it." [4]
- the popcorn and the stopped ride [4]
- Owen's "always both" and the pencil revision [5]
- the softened line and the 4–1 warning [6]
- the dunk tank, where she takes his place: *"The groom's closed. The chair's open."* [7]
- the 79-minute flashlight and the kitchen-sink hose [8]
- the plaque vote and Clyde's "It's mean" [10]
- the ghost withdrawn: *"She's not out there. It's just a pond."* [11]
- folding blankets with "That's a byline." [12]
- the mud-hitch repair as a radio show [13]
- the 1958 search told over pie [14]
- forty lanterns wired in his barn, and Rufus's bark recorded on moving day [15]
- the brother on the stairs, and the father's toolbox [16]
- the first lantern ride: *"That's finished."* [17]
- the corn-maze kiss and the raccoon [18]
- Dot lifts the last lantern: *"That's about where he was."* [19]
- the porch light she fixes herself, in eleven minutes, two and a half years late [20] (*rev*)
- the empty Pullman warehouse floor, where a quarter stands on edge [21]
- *"I'm sorry"* in the hardware store [22]
- *"No."* / *"I'm done asking."* [23]
- "Go." again in the parking field [24]
- the rooster and Danny's "say the other thing" [25], refused and replaced at [30] (*rev*)
- the bride brought home at dawn [25, 27]
- the door hung with the name and the hours [26]
- the dock confession, *"Right here. Choosing this one,"* and the lanterns lifted to the bench [28]
- the self-enforced step-down and *"I was wrong"* [29]
- the strike and the two tickets in the cigar box [30]

**Technique-bank devices (`page-craft-standards.md` §4.1):**

| Device | Where it appears | Role |
|---|---|---|
| First-inspection line (true, not misjudged) | [1], her POV: *"He was taller than she remembered, or he stood straighter, or her memory had been leaning on him... He looks like somebody let him out of a coat... Like he'd hung on a hook a long time."* Confirmed by the closed-room line in [13]. Capped by an object-act: *"He'd brought a pin."* | **PRIMARY. Carries the first attraction beat.** |
| Restraint as care (offered exit plus stillness), not a bank device | [1]: *"giving her one more second to pull it back, standing very still so that if she took her hand away, nobody would see"*; *"I could say I've got a conflict... nobody would have to watch you do this."* | **Carries the first care beat.** The bank does not cover it; record it as `other` |
| Care-object-and-service | [6] hand flat on the bench, then removed "before she could notice" (service, no object); [8] the Maglite held 79 minutes; [26] the door (*rev:* the [20] porch-light repair was cut; the light is now her own act) | First *bank* care device. It dominates the care beats from [8] |
| Others'-talk introduction | [1]: whispers under the ham buns (*"Chicago let him go, is what I heard. Bought her house off her"*) before he is seen. He is also pre-cast as the villain of her story | Introduction mode |
| Answer-length ladder | *rev P15:* explicit ladder cut; only a one-line callback remains ("the only thing you said to me was 'Belt.'" [18]). Previously explicit in [18]: *"The first night you said 'Belt.' One word... You just said a paragraph."* / *"I'm a carpenter. I measure."* | Secondary, structural |
| Mirror line | "Still choosing the city" [3] becomes "Choosing this one" [28]; "Go" [4, 16, 24] is answered not by "Stay" but by her own terms ("ask on a Tuesday") [30] (*rev:* the one-word callback payoff was removed); *"You still pull early?"* [1] becomes *"Do you still pull early?" / "Only when I'm scared."* [19]; his ex's "whole room... kept the door shut on" [13] becomes the door he hangs [26] | Secondary, load-bearing at the climax |
| Charm-witness | Clyde (*"That story's mean."* [5, 10]); Lorna (*"He's giving you the answers that'll make you believe him"* [5]); Mateo (*"That's my friend. That's the train guy."* [13]); Dot (*"That's the right answer."* [19]); Ruth (*"She labels like me."* [15]) | Secondary, frequent |
| Comic undercut at chapter exit | [4] "Trains are cool."; [7] pie poll; [13] "That's the train guy."; [18] "Ain't nobody comes back out of that corn." | Secondary |
| Narrator-wrong-once | [18]: *"it had never been nothing. It had been the effort of holding still."* Also "Still choosing the city" was hers and wrong [5] | Secondary |
| Involuntary symptom | Weak: *"She looked at it for one second and it felt like a week"* [1]; *"her jaw did something small"* [2]; *"the flashlight beam jumped a half inch and came back"* [8, his]; *"her hand was steady too, which it had not been all night"* [18] | Secondary only |
| Contraband object (variant) | The ticket halves pinned inside the coats, left side, over the heart. "Which side of the coat?" [2, 7, 26]. Boxed together at the end [30] | Secondary token. Not a secret relationship |
| Non-bank structural device | One true answer a night, asked "to the corn" on the dark stretch home [3, 4, 6, 8, 11, 13, 17, 19, 23] | The book's question engine |

**Not used:** mistake-based introduction, endorsement-before-encounter, name-by-mistake, competence-before-greeting (competence beats come after the greeting: [3] the cue, [13] the hitch), cold-hero puncture (the hero is restrained, not cold).

**Rotation note for H7:** the first attraction beat is carried by a first-inspection line, not by an involuntary symptom. The first care beat is carried by restraint/offered exit, not by care-object-and-service. Care-object-and-service is the dominant care device from [8]. If the two previous pen-name titles used it as primary, flag it as a texture recurring, not a primary.

### 15. What the job and the setting make possible
**The heroine:**
- **Effects builder and author of the event's story.** This makes the plot possible:
  - She owns the narrative that defames him, and only she can withdraw it (author clause).
  - Her craft logic ("A scare is just a promise you keep two seconds late"; "find where they're looking, then put the thing somewhere else") is how she hides her feeling.
  - The climax is a re-staging of her own effect: the same lantern and line, unveiled.
- **Chair.** Her own bylaws bind her (rules 1, 3, 7, 12). The climax transgression has a pre-written price, which she pays [29].
- **Day job, middle-school science teacher:**
  - a classroom chorus asks the true question [5, 22]
  - dry-ice fog ties in [5, 20]
  - she teaches probability, which makes the jar ironic [1]
  - she reads a room and uses "the voice" on riders

**The hero, theatre scenic carpenter turned one-man shop:**
- He works the toggle the stagehand's way, four fingers on the rail and thumb on the cue [3] (*rev:* was "hits the cue on the word").
- He reads the room as a stage manager ("Standby humiliation. Humiliation, go." [4]).
- He kerfs the reeds hummock that makes the true finale technically possible [15].
- His model of the pond carries his private decision [12, 24].
- The shop folding is why he came home [2], and that produces the truthful "No" [23].
- The big-city offer is the goal collision [21].
- His want is a door with his name and hours: "things that travel and come home" [17, 26].

**The setting, a ten-night volunteer hayride on a farm:**
- The two-seat belted bench is the containment.
- The pond stop is the stage where the public story is performed.
- The chalkboard is the scoreboard.
- The committee is a voting jury.
- The farm's own 1958 history supplies the true replacement story.

**Occupation-swap test (H3):**
- Axis 1 (the lottery pairing) depends on the volunteer institution, not on either day job.
- Axes 4 and 6 depend on her being the author and builder of the event's story. Swap that role and the withdrawal, the substitution and the dock confession lose their mechanism.
- His trade is causal for the co-build and the rupture (the offer), not for the climax.
- **Verdict:** her authorship role is causal. Both day jobs are partly colour.

---

## Form fields (16–18)

### 16. Structure, POV, tense, entry point

**Structure:** 30 chapters, 68,788 parsed words. Mean chapter length 2,293 words, CV 0.15. Dialogue is 28.5% of the book and 25.7% of Ch1–3; Ch1 runs 184 words before the first dialogue.

**POV:** dual close third person, past tense, one POV per chapter.

| Narrator | Person / tense | Chapters | Narration words |
|---|---|---|---|
| Roz | Close third, past | 18: 1, 3, 5, 6, 8, 10, 11, 13, 14, 16, 18, 20, 22, 23, 25, 27, 28, 30 | 29.2k |
| Gus | Close third, past | 12: 2, 4, 7, 9, 12, 15, 17, 19, 21, 24, 26, 29 | 20.0k |

The pattern alternates, with Roz runs at 5–6, 10–11, 13–14, 22–23 and 27–28.

**Timeline:**
- Linear, about five weeks: the Harvest Supper (late September), ten Friday/Saturday nights in October, then the strike on November 1.
- Anchored dates: Oct 6 (the breakup anniversary [5]), Oct 26 (the would-have-been wedding [20]), Halloween (the climax).
- Embedded retrospectives come as told stories: the 1958 search [14], the 2019 breakup from the stairs [16], the ring [4], the diner vigil [16, 18].

**Timeline entry point:** `after_departure`. The book opens seven years after the breakup, once he is back.

### 17. Ending image
- **Object:** the Bride's lantern, unveiled and with a dead battery, hung on the iron nail in the barn where the dog collar used to hang (the collar is now in her pocket, waiting for a dog "not born yet"). *"Its glass held the light from the window, and it was still."*
- **Class:** `object_at_rest`.
- **Callbacks:**
  - the lantern's first lighting at [3]
  - the collar/hook at [1, 14]
  - "small and ordinary and hers" [25]
- The penultimate beat is the two ticket halves boxed together.

### 18. Narrator signature

**Voice-contract devices:**
- **Roz's chapters often open on an aphoristic scare-craft or situation verdict:**
  - [3] "A scare is just a promise you keep two seconds late"
  - [5] "Eighth graders could smell a story the way sharks could smell a paper cut"
  - [6] "The trouble with changing a last line was that somebody always knew the old one by heart"
- **She keeps her face "exactly where it was."** It is a recurring motif, and the climax undoes it: "Her face was nowhere near where she'd put it" [29].
- **Her exits often end on her own writing on the script or call sheet:**
  - "FINALE: AS APPROVED." [3]
  - "*Maybe still deciding.*" [5]
  - "*Finale: author's choice.*" [27]
- **Gus's chapters use a stage-manager lens:**
  - "Standby humiliation. Humiliation, go." [4]
  - "A flat is a lie you can carry under one arm." [9]
  - "Everything in a theater's lying about its weight" [15]
  - "Standby... nothing left to cue" [29]
- **He holds still on purpose:** "He rested it there and didn't push." [2]
- **"Okay."** He says it and she replies "Don't say okay," a running gag (5×) that ends with her "Okay" at [26] and "I'm borrowing it" [27].

**Measured voice vector** (`series_diff.py` §6, narration only, per 1,000 words):

| Tic | Book | Roz | Gus |
|---|---|---|---|
| Em dash | 0.06 | 0.10 | 0.00 |
| Negative parallelism | 0.02 | 0.00 | 0.05 |
| "Not X, exactly" | 0 | 0 | 0 |
| "[name] understood" | 0 | 0 | 0 |
| Hedge before disclosure | 0.02 | 0.03 | 0.00 |
| "For the first time" | 0.02 | 0.03 | 0.00 |
| Theme statement | 0 | 0 | 0 |
| Filter words | 4.98 | 4.28 | **6.02** (at the 6.0 threshold) |

No tic is above threshold at book level. Gus's filter-word rate sits on the threshold and is worth watching. Against the twin-sister prior: no shared tics, top-opener Jaccard 0.29 (under 0.30), AXIS_11_MECHANICAL PASS. The WATCH set holds 6 shared 4-grams: "i'm not going to", "she looked at him", "at the far end", "he could see the", "in front of him", "said without looking up".

**Top repeated 4-grams:**

| 4-gram | Count |
|---|---|
| i'm not going to | 13 |
| in the front row | 12 |
| end of the dock | 11 |
| on the far bank | 11 |
| on the way back | 10 |
| back to the barn | 9 |
| in the third row | 9 |
| we're looking for somebody | 9 |
| on the 8:20 | 8 |
| on the right side | 8 |

**Recurring phrase habits (counted):**

| Phrase | Count | Note |
|---|---|---|
| "She didn't" / "He didn't" | 55 / 52 → *rev* 30 / 11 (sentence-initial, narration only) | Restraint rendered as actions not taken; Gus's chains converted to stage-manager cue-calling and object-talk |
| "didn't say anything" | 27 | |
| "the way he" / "the way she" | 27 / 27 | Similes and characterising comparisons |
| "the way you…" / "the way a…" | 18 / 15 | |
| "Okay" | 59 | Includes Lorna's "Okay, so" (13) and "Don't say okay" (5) |
| "very still" | 13 | |
| "Bro" | 14 | Danny |
| "Now," | 10 | Bev's opener |
| "Yup" | 9 | Hank's whole vocabulary |
| "Huh" | 9 | |
| "Well, now" | 8 | Dot |
| "to the corn" | 7 | Where she asks her questions |
| "As a performer" | 5 | Ed |
| "face where" | 5 | |
| "on record" | 4 | |

Exact times and dollar figures appear throughout ("six-thirty-eight", "$13,900", "seventy-nine minutes", "five-ten for it").

**Chapter-exit kinds (hand tally, 30 chapters):**

| Exit kind | Count | Chapters |
|---|---|---|
| Side-character line | 10 | [1, 4, 7, 9, 13, 14, 15, 18, 19, 28]. Four or five are comic undercuts: [4, 7, 13, 18, 19] |
| Lead's spoken line | 5 | [11, 16, 17 (question), 22, 26] |
| Written annotation on the script or call sheet | 3 | [3, 5, 27] |
| Physical act | 5 | [2, 10, 12, 20, 24] |
| Image or object at rest | 7 | [6, 8, 21, 23, 25, 29, 30] |

The script's coarse labels are dialogue 50%, image/quiet 50%, decision 6.7%, named-feeling 3.3%. Exit-rhythm L1 against the twin-sister prior is 0.224, which the script flags as "same exit rhythm". That is a heuristic flag; read it against the distinct exit content above, where side-character punchlines and script annotations do not appear in the prior.

### narrative_voice_tags per narrator

| Dimension | Roz (close 3rd past) | Gus (close 3rd past) |
|---|---|---|
| Attention bias | Rooms and where they're looking; rigs, cues, batteries, timing of a scare; who is watching | Lines, plumb and level, weight; what a thing is pretending to be; where she is in his peripheral vision ("the exit sign in a dark theater") |
| Certainty | Procedural certainty ("It's handled"), emotional evasion; truths arrive "before she could put it down" | Plain declaratives about himself, self-indicting ("Arguing was for people who believed they had a case") |
| Time stance | Scene-immediate, with embedded memory flashes (veil, funeral luncheon) | Scene-immediate; decisions made at named times and places ("He had made himself a promise in the Ranger in August") |
| Syntax | Medium sentences, comic triads, aphoristic first lines, clipped "the voice" commands | Short plain sentences; "He didn't X. He didn't Y." restraint chains; stage-manager imperatives |
| Humour | Deadpan teacher wit (*"It's cocoa with a felony in it."*), room management | Self-deprecating, situational (*"Under the Wagon"*, *"It's a candle flavor"*). Straight man to the ensemble |
| Sensory priority | Cold, fog, light in the dark, sound of the wagon's silence | Sawdust, materials, stillness of hands, a marble rolling on a sloped floor |
| Metaphor source | Haunt and effects craft: scares, rigs, cues, lines, "a promise you keep two seconds late" | Theatre scene shop: flats, strike, standby/go, "lying about its weight" |
| Self-deception | High early ("It's handled"; the story is "true-ish"); taken apart by [5], [16], [25] | Low to moderate: he knows his error is ease and names it [6, 24] |
| Explains-meaning frequency | Low to moderate. An occasional summary line ("Because it isn't true and it's the best thing I ever wrote and those are the same sentence") | Low. Lets acts stand ("He'd brought a pin.") |

**Shared across both narrators:**
- an ensemble with fixed catchphrase tags (Lorna "Okay, so", Dot "Well, now", Bev "Now", Hank "Yup", Danny "Bro", Ed "As a performer", Clyde one word)
- heavy callback density
- warm small-town comedy
- near-zero em dashes
- little glossing

**Machine tags:** `dual_close_third_past`, `ensemble_catchphrase_comedy`, `callback_dense_running_gags`, `scare_rigging_vs_stagecraft_metaphor_split`, `restraint_rendered_as_stillness`, `the_way_you_simile_habit`, `time_and_dollar_precision`, `aphoristic_chapter_openers`, `script_annotation_chapter_exits`, `side_character_punchline_exits`, `low_gloss_rendered_meaning`, `near_zero_em_dash`, `warm_deadpan_small_town_humor`.

**Voice note for the gate:**
- `restraint_rendered_as_stillness` overlaps in function with the twin-sister book's `negated_action_restraint`. Both books use "He didn't" chains: 52 here against 63 "he did not" there.
- `low_gloss_rendered_meaning` and `near_zero_em_dash` also recur.
- Treat these as possible house habits. A blind voice test on a passage from each Gus/Declan chapter is advised.

---

## Surface variables (recorded to prove they are NOT the differentiator)

- **Names:**
  - Leads: Rosalind "Roz" Pietrowski and August "Gus/Augie" VanderWal.
  - Her family: brother Danny (19); late father Walt; absent mother.
  - His family: mother Ruth; late father Pete; Aunt Marlys and Rufus the beagle mix.
  - The farm: Dot Ambrose (81), late husband Arlo, the dogs (all named Pepper).
  - The committee: vice-chair Bev Oosterhouse, Arlene Doornbos (late husband Herm), Marv Kuiper, Ed Brinks, Clyde Mulder.
  - The hayride crew: friend Lorna Bakker; tractor driver Hank Ruiter and the tractor Marguerite; Kenny and Brielle Hoekstra.
  - Riders and fans: Mateo and Inés Salas; Joyce from Battle Creek and Sharon; Mason Kuiper; Tyler; Jaxon.
  - Press: Kenzie Vos and Brody.
  - His work world: Vince Ferrante, Nico, Gil, Bettina; ex Kate.
  - Students: Owen Sterk and Kaylee Dykstra.
  - Town: Mr Haverkamp and Lyle; Mr Bosma.
  - Grandfathers: Stan Pietrowski and Hendrik VanderWal.
  - The truck Delores.
- **Occupations (labels only):**
  - heroine: 8th-grade science teacher, volunteer hayride chair and effects builder
  - hero: theatre scenic carpenter / former scene-shop foreman, now a one-man scenic shop
  - brother: community-college student and parking volunteer
  - friend: diner owner
  - vice-chair: church/Grange volunteer
  - Hank: farmer
  - Kenzie: local reporter
  - Vince: production manager
- **Locations:** fictional Carrow, Michigan (Kalamazoo/Paw Paw area): Grange Hall, Ambrose farm and pond, Hollins Road, Ambrose Road, Bakker's Diner, Carrow Hardware, room 114. Also Tractor Supply in Paw Paw, a Lawton cider mill, the Marathon station on M-40; Chicago (Lakefront Stage Company, Calumet Repertory, the Pullman warehouse on 95th St, a Clark Street jeweler, Pilsen); Grand Rapids; Battle Creek; Allegan; Sturgis.
- **Species:** human (`monster_difference: not_applicable`).
- **Wealth level:** working and lower-middle class, rural. $15 tickets, a $510 ring sale, an $84k offer turned down, a $29k community target.
- **Cover trope:** second chance with an ex-fiancé / forced proximity / small-town fall festival / haunted hayride / Halloween.
- **Heat level:** closed door. Two kisses [18, 29]; no profanity on the page.
- **Title pattern:** "Two Tickets to the [Seasonal Event]". It is not a first-person grievance title.

---

## Recognizability line

A woman who has spent six years telling paying crowds a ghost story in which the man she sent away is the villain is bound by her own rules to sit beside him while she tells it every night. She softens it, withdraws it, and replaces it with a true story of a community searching for a lost child. In the end she leaves her seat mid-finale to tell the crowd that she was never the one waiting: she sent him.
