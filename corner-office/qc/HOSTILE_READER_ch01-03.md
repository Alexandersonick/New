# HOSTILE READER: Chapters 1–3

**Book:** *My CEO Husband Gave Her My Corner Office*
**Pipeline:** v5.0.2, page-craft-standards §2 (O1–O9) and §7 (Hostile Reader Pass and repeat-reader briefing). Ranks are from reader-contract-gates §4.
**Read as:** an independent reader. I had only `qc/ch01-03.md` and `qc/repeat_reader_fingerprints.json`. I saw no architecture, outline, bible or later chapters.
**Text measured:** Ch1 2,137 words, Ch2 2,585 words, Ch3 2,219 words, about 6,940 words in total.

## Bottom line

| Layer | Result |
|---|---|
| Part A: first-time hostile reader | **PASS.** No complaint maps to rank 1, 2, 3, 9, 11 or 13 above low severity. The highest-severity complaint is rank 6 (tone and billionaire signal versus the title), which is not a fail rank. |
| Part B: Opening Pages O1–O8 | O1–O5, O7 and O8 pass. **O6 fails on the letter:** Chapter 1 has about 9 backstory facts against a cap of 3. None of them is a flashback longer than a paragraph, and the hostile read did not experience them as a dump. Either trim to 3 or record a deliberate exception. |
| Part C: repeat reader (O9) | O9's on-page differentiator is present in Chapter 1 and the timeline entry point is new. **`could_write_the_same_book_review: true`, which is a FAIL. File it as `CATALOG_SAMENESS`.** The sameness is not in the inciting act. It is in the hero's error, the heroine's craft authority, the heroine's goal (credit), the tradesman accountability network, the retreat to her own workspace, and about 10 of the 18 voice tags from the earlier books. |

---

## Part A: HOSTILE_READER_REPORT (first-time reader)

```yaml
HOSTILE_READER_REPORT:
  dnf_point: >
    No DNF inside Chapters 1–3. Sentence one ("My office is hanging in the sky") holds the reader
    through Chapter 1. Adam's 4:26 a.m. text ("Where is the room.") is a real hook. Chapter 2's title
    scene pays for the "Twenty hours earlier" rewind within about 300 words ("There's a woman in my room.").
    The highest-risk point is Chapter 3, lines 411–433: plant walk, pallet kick, Joe flashback, LATER folder.
    The reader already knows from Chapter 1 that she calls the crane, so this stretch is waiting rather
    than reading. If Chapter 4 does not go straight back to 4:26 a.m. and Adam, this reader quits at the
    start of Chapter 4.

  skimmed:
    - passage: "Ch1 l.59 (lowboy, cribbing, six-by-sixes, lift points) and the rigging jargon throughout
        (mullion, hook block, tag line, outrigger)"
      reason: "Technical description. Flavor the reader gets after one pass and doesn't need repeated."
    - passage: "Ch1 l.145, Lolo's biography paragraph (line lead, 1994, press brake, bucket, unicorn)"
      reason: "A backstory block landing right after a good exchange. The reader wants to get to the phone call."
    - passage: "Ch2 l.209, floor description (maple boards, 1922 green columns, department layout)"
      reason: "Description placed between 'There's a woman in my room' and the confrontation. It's the
        exact spot where the reader wants the next line of the scene."
    - passage: "Ch2 l.287, explanation of 'That's interesting' (mother, parish council, Marek, referee)"
      reason: "A tangent in the middle of the fight. The joke works, but it stalls the confrontation."
    - passage: "Ch3 l.393–395, the plant soundscape, and l.411, the floor walk and orders"
      reason: "Mood, with no new information except what a Corner is. The divorcing Traverse City
        couple is good but buried."
    - passage: "Ch3 l.417, pallet kick and the Joe/welding-hood flashback"
      reason: "A flashback about a minor character who is never identified ('Joe'). The outcome of the
        chapter is already known."
    - passage: "Ch3 l.437 and l.451, the receipts inventory and the lease re-read ('manor')"
      reason: "The lease itself is the payoff. The inventory around it is padding."
    - passage: "Ch3 l.541–549, Walt's permit, cost and equipment list"
      reason: "Logistics for an operation the reader has already watched happen."

  one_star_review_draft: |
    ★☆☆☆☆ Where is the billionaire??
    The title promised a cold CEO husband handing the heroine's office to his work wife and her getting
    EVEN. What I got was three chapters of cranes. I now know what a hook block, a mullion and a "knee
    frame" are and I did not want to. Every side character is a quirky comedian and there are like
    fifteen of them by chapter 3. The husband shows up for ONE scene, says "you barely
    use it," and leaves for Chicago. That's the big betrayal? An office she admits she doesn't use?
    And the other woman is... nice? She has a daughter at State and squares her napkin. Then right
    after a great cliffhanger it goes "Twenty hours earlier" and I had to watch her kick a pallet and
    read a lease to find out something I already knew from chapter 1. She keeps saying something
    happened "two years ago at seven" and then literally says "I'm just not going to" tell us. Then
    why bring it up! Pretty writing, but everything is "like a" something. Almost DNF'd in chapter 3.

  complaints_mapped:
    - complaint: "'Twenty hours earlier' rewind straight after the Ch1 hook; Ch2–3 answer a question
        Ch1 already answered (does she move it? yes)"
      rank: 1
      severity: low   # Ch2 delivers the title scene quickly; the cost is felt mostly in Ch3
      defect_id: HR-01
    - complaint: "Ch3's first half is low-delta (plant walk, pallet, Joe flashback, LATER, receipts)"
      rank: 1
      severity: low   # about 400–500 words are skimmable; Lolo's arrival (l.453) restores pace
      defect_id: HR-02
    - complaint: "Too many named people for 7k words (about 20: Walt, Lolo, Darnell, Tavi, Elvin,
        Simone, Ruth Baskin, Adam, Bridget, Marek, Marge, Gordon Pyle, Hannah, Irene, Benny, Joe,
        Gina, plus mother and father)"
      rank: 1
      severity: low
      defect_id: HR-03
    - complaint: "Coy withholding of the two-year wound, three times: 'studying the back of his head
        for two' (l.165); 'a long answer, which starts two years ago on a Tuesday morning at seven
        o'clock' (l.497); 'I could tell you the day... I'm just not going to.' (l.567)"
      rank: 13   # narrative tell / device repetition; once is a hook, three times reads as a tease
      severity: low
      defect_id: HR-04
    - complaint: "Without the withheld wound, the heroine's response (a 3 a.m. crane) can read as out
        of proportion to 'he gave away an office I don't use'. Some readers will call her petty."
      rank: 2
      severity: low   # partly pre-empted by the wedding paragraph, the father's brass pull, the
                      # badge change on Friday, and 'Did you ask me?'
      defect_id: HR-05
    - complaint: "The billionaire signal is muted and the register is a blue-collar Michigan craft
        novel, while the title's register is webnovel melodrama. Readers who come from that title
        format expect glitz and a hissable other woman."
      rank: 6
      severity: medium
      defect_id: HR-06
    - complaint: "The work-wife emotional affair is barely visible so far: one glance (l.293), one
        coffee over her shoulder (l.269), and one 'You're the best' (l.373). The other woman is
        sympathetic."
      rank: 6
      severity: low   # it's early, and the seeding is precise ('I used to be the person who got it')
      defect_id: HR-07
    - complaint: "Repetitive constructions: 'the way you'd ___' similes x8; about 35 'like/as if'
        similes in 6.9k words; 'which for him is a confession / which from Irene is a parade /
        Benny's version of a hug'; 'I think about X. I think about Y.' anaphora in 3 passages;
        'speech to N people as if it were 10N' twice (l.349, l.531)"
      rank: 11
      severity: low   # escalates to medium if this rate holds over a full novel; run prose_metrics
      defect_id: HR-08
    - complaint: "Every secondary character speaks in the same deadpan one-liner register (Walt,
        Lolo, Elvin, Darnell, Benny, Tavi, Bridget)"
      rank: 13
      severity: low
      defect_id: HR-09
    - complaint: "About 9 backstory facts in Ch1 (see O6). Not a dump, but several are decoration
        (napkin and First Communion, Elvin's newspaper, 'I used to know everybody's reviews')"
      rank: 9
      severity: low
      defect_id: HR-10
    - complaint: "Editing slips: the oatmeal exchange is out of order; the marketing staff get off on
        three, but marketing sits on four; Ch1 says 'a line' of writing on the door, Ch2 says three
        lines; 'Joe' is never identified (see Continuity)"
      rank: 3
      severity: low
      defect_id: HR-11
    - complaint: "Plausibility: facilities moved the badge access on Friday, so how did Pip and
        Darnell get into the room at night to empty and unbolt it? It isn't addressed."
      rank: 10
      severity: low
      defect_id: HR-12
    - complaint: "Geography (local readers): the room is in the NW corner 'where the two big windows
        meet over the river', yet the crane on Monroe Avenue picks it out, and the NW stairwell window
        looks 'straight down onto Monroe Avenue'. On Monroe Ave NW the river is behind the buildings."
      rank: 17
      severity: low
      defect_id: HR-13

  what_they_could_not_complain_about:
    - "A passive heroine. She is executing her irreversible act in sentence one, and Ch3 shows the
       decision being made, with Lolo pushing and Pip choosing ('The window,' I say)."
    - "Title not delivered. The title scene is literal and public by about word 3,300: a whole sales
       floor watching, the husband handing the rival coffee 'over my shoulder, into my room', and
       'You barely use it.'"
    - "Generic setting. Grand Rapids, Clyde Park Lanes jacket, pierogi, paczki at Marge's, press brake,
       Bob Seger, the asset register 'Line forty-one. Furniture and fixtures, founders' office, one unit.'"
    - "Cheating. Nothing on the page breaches the no-cheating promise. Simone is level and decent ('I
       would have asked you. If I had known it was yours.'), which heads off 'cartoon other woman' reviews."
    - "Thief or unhinged heroine. The dollar-a-year lease, 'Terminable at will by Lessor', is a concrete
       legal footing, set up in a warm flashback with Adam ('Nobody's ever going to read it')."
    - "Strawman husband. Pip's own avoidance is on the page (the LATER folder, skipped Monday meetings,
       'You're here with donuts'), so Adam has a case."
    - "Vague grievance. 'You're telling me now, in front of sales. That's a different verb.' / 'Did you
       ask me?'"
    - "Weak chapter exits. 'Take the longest way you know, Walt.' / 'Plenty of room, I think.' (the
       stairwell window measuring the street is a great seed) / 'I'll bring the bolts.'"
    - "Head-hopping. Single POV throughout."
    - "Plot only about an office. Project North, 'integration', and 'v14' open a second, larger question."

  verdict: PASS
  verdict_note: >
    The rank-6 tone/billionaire complaint (HR-06, medium) is the most likely real one-star driver,
    but it is not a fail rank. Fix list before Phase 12: HR-08 and HR-11 (cheap), HR-04 (cut one
    or two of the three teases), HR-02 (compress Ch3, l.411–437).
```

---

## Part B: Opening Pages Gate O1–O8

| # | Result | Evidence (quote) |
|---|---|---|
| O1: sentence one disturbs | **PASS** | "My office is hanging in the sky over Monroe Avenue, turning a quarter inch at a time, and it has never looked better." This is an anomaly, a precise datum and a judgment in one sentence. |
| O2: non-swappable concrete noun by sentence 3 | **PASS** | Sentence 2: "Walt Kasprzak has it on four chains off the hook of a hundred-ton crane that takes up both lanes and a bus stop." |
| O3: want, disturbance or question by ~300 words, plus a genre signal or strong voice | **PASS (on voice)** | The disturbance and question are there at word 1: why is she removing her office at night? Voice carries it: "Your glass is two inches off my hook block. It's a matter of where you stand." The theme is planted at word ~257: "I am telling everybody it was your idea." / "It was my idea." The romance genre signal is late: the first hint of a husband is "Mr. Kerrigan" at word ~717, and "ADAM" appears at ~1,942. |
| O4: someone speaks by ~400 words, with a status collision or misjudgment | **PASS (weak on misjudgment)** | First dialogue at word ~108: "Lower," I say into the radio. The status collision follows at once: "I'm not kissing anything," Walt says. "I'm forty years married. I don't kiss." The underestimation of the heroine arrives in Ch2 ("Oh my God, Pip" in the voice for "a cousin who flew in for a funeral"; "You barely use it."), not in the first exchange. |
| O5: love interest / genre engine by end of Ch2 | **PASS** | By phone at word ~1,942 ("It says ADAM.") and by text: "*Simone just called me. Pip. Where is the room.*" In person at word ~3,120: "That's when Adam comes around the end of the design studio with two coffees in a cardboard tray". The marriage-crisis engine fires at ~3,400: "You barely use it." |
| O6: ≤3 backstory facts in Ch1; no flashback over one paragraph; no summary prologue | **FAIL on fact count; PASS on flashback and prologue** | Ch1 holds about 9 backstory facts: (1) "In 2018, when we craned the room in, every engineer... told me... it was vanity" (2) "That corner took me three years and a burned eyebrow" (3) "He used to bring me the newspaper some mornings" (4) "I drew those lift points on a napkin at Russo's in 2013... next to my First Communion" (5) Ruth Baskin's "a lovely little indulgence" (6) "I used to know everybody's reviews" (7) Lolo: "line lead at Lindqvist Furniture... My dad trained her on a press brake in 1994" (8) "I've had eleven years to learn them, and I've been studying the back of his head for two" (9) "Adam always uses a question mark." Each is 1–2 sentences, with no flashback paragraph and no prologue. Recommended keep set: (1), (8) and the lease line, "It's on a lease to the company for a dollar a year". Cut or move (3), (4), (6) and compress (7). Note: Ch2–3 as a whole is a 20-hour rewind. That is a timeline structure, not a backstory flashback, so it is not counted here. Ch3's lease flashback (l.439–449) runs one paragraph plus 5 dialogue lines, which is borderline but outside Ch1. |
| O7: no blurb restatement, author's note or cast list | **PASS** | None present. Production note: strip the `<!-- POV: Pip -->` comments, and consider dropping "— Pip" from chapter headings in a single-POV book. Some EPUB converters surface HTML comments. |
| O8: Hostile Reader Pass clean on ranks 1, 2, 9, 13 | **PASS at the caller's severity threshold** | Ranks 1, 2, 9 and 13 appear only at low severity (HR-01–05, HR-09, HR-10). Read literally ("no complaint mapping"), O8 is not clean. Listing those low items as DEFECTs and fixing the cheap ones (HR-04, HR-10) would close it. |

---

## Part C: repeat reader (O9 and the repeat-reader briefing)

### O9: does Ch1–3 differ from PREV-1..3 on the three axes?

| Axis | This book | PREV-1 | PREV-2 | PREV-3 | Differs? |
|---|---|---|---|---|---|
| **Inciting disruption** (core 1) | Husband, in person and in front of the whole floor, has given the room she built, and married him in, to his VP, with the rival standing in it holding his coffee. | Heroine watches, unseen, through a window as her twin impersonates her while the husband pours the wine. | Investor redirects her answer in a client meeting; husband doesn't notice. | A florist on the phone reveals the assistant has ghostwritten every card; heroine alone in her kitchen. | **Partly.** The event, the public audience and the husband as active agent are new. The class, "another woman occupying the heroine's place with the husband's complicity", repeats PREV-1 (twin as Maud) and PREV-3 (assistant as wife's proxy). "Public erasure before colleagues" repeats PREV-2. |
| **First irreversible decision** (core 3) | Ends the lease and cranes her room out of the company building at 3 a.m.; it's on the page in Ch1, decided in Ch3. | Ch3: takes her house key off the ring and moves to a cot in her unheated studio. | Ch4: refuses to finish underwriting unless named. | Ch4: six-page list, calendar access revoked, one-year deadline. | **Partly.** The mode is new (public, physical, legal, spectacle, executed rather than announced, on the page in Ch1). The function, withdrawing herself and her work to her own workspace ("And then I go to work." / "In it?" / "Next to it."), repeats PREV-1's relocation reset. |
| **Timeline entry point** (form 16) | A cold open 20 hours after the crisis, mid-counterstrike, then a rewind to the crisis (Ch2–3); first-person present. | At the crisis, linear. | At the crisis, linear. | At the crisis, linear (retrospective first person). | **Yes, clearly.** |

**The differentiator is on the page in Chapter 1:** "My office is hanging in the sky over Monroe Avenue, turning a quarter inch at a time, and it has never looked better." All three earlier openings meet the heroine as a witness or victim of the disruption. This one meets her as its author's counter-agent, before the reader has seen the disruption at all.

**O9 by the letter: PASS** (an on-page Ch1 differentiator, and a difference on all three axes at the level of event and act). **The briefing test below still fails.**

### Repeat-reader briefing

```yaml
  repeat_reader:
    could_write_the_same_book_review: true
    same_book_review_draft: |
      ★★☆☆☆ Same marriage, new trade.
      I could've written this one from chapter 2. Wife is the
      real talent: last time a restorer, then a builder, now a welder who designs backyard offices.
      Husband is a busy exec whose company ate him, and he makes the big call without asking her
      ("Did you ask me?" is basically the whole book again). Another woman ends up standing in the
      wife's spot while he hands her coffee (before that it was a twin pouring wine, and an assistant
      writing his cards). Wife retreats to her own workshop, where a gruff older woman and a crew of
      salt-of-the-earth tradesmen tell her the truth in one-liners. Exact times, exact measurements,
      a ritual from the early marriage, lots of reading his face. I already know the board finds out
      whose idea it all was and he learns to ask. The crane opening was fun, though.
    axes_they_recognized:
      - hero_error: "unilateral decision ('Did you ask me?' / 'I'm asking you now.') = PREV-2
          unilateral_decision_making; PREV-1 unilateral_carrying"
      - power_configuration: "heroine_craft_authority (weld bead, the post-free corner, 'Nobody else
          reads every order') = PREV-1; PREV-2 heroine holds the systems"
      - heroine_goal: "credit / whose idea (packaging 'boardroom learns whose idea'; Ruth Baskin's
          'lovely little indulgence'; 'It was my idea.') = PREV-2 credited_authority, PREV-1
          reclaim_professional_name"
      - opening_engine_class: "another woman substituted into her place with the husband complicit
          = PREV-1 twin, PREV-3 Fern"
      - setting_function: "husband's company competes for presence ('his calendar went from a
          calendar to a weather system', 'reading every order doesn't scale') = PREV-3; credit
          hierarchy = PREV-2"
      - relocation_reset: "retreats to own workspace (room trucked to the plant yard; 'Next to it.')
          = PREV-1"
      - supporting_cast_function: "blue-collar accountability network with an older-woman truth-teller
          (Lolo, Walt) = PREV-1 (Frances), all three 'accountability_network'"
      - relationship_start: "married and estranged/neglected for two years = PREV-1, PREV-3"
      - ritual_motif: "early-marriage ritual as wound marker ('Coffee at seven' / '(not 7:15)') =
          PREV-1 anniversary, PREV-3 anniversary cards"
      - narrative_voice_tags:
          numeric_time_stamping: "'The bay came out in eleven minutes. I designed it to come out in ten.' / 'It's four twenty-six.'"
          craft_metaphor_precision: "'you're kissing the mullion' / weld bead, knee frame"
          dry_understated_refusals: "'That's interesting.' / 'Okay,' I say."
          emotion_displaced_into_hands: "'I can't work. The file goes back on the bench.' / hand flat on the glass / pallet"
          look_longer_second_reading: "'She looks at the box for a second longer than a person normally looks at donuts.'"
          corrective_negation: "'I couldn't tell you the day it stopped. That's not true.'"
          aphoristic_summation: "'It's easier to know a thing is happening than to see the slide where it happens.'"
          quiet_declarative_chapter_closers: "'Then I go down the rest of the stairs to my truck.'"
          callback_phrase_recurrence: "'That's interesting' x3; 'You barely use it' x3"
          proleptic_foreshadowing: "'That's the thing I'll think about at three in the morning for the next week.'"
    not_recognized_as_repeats:
      - "timeline entry: post-crisis cold open and rewind"
      - "POV form: single first-person present"
      - "spectacle opening act (public night crane lift, filmed by the intern)"
      - "legal-property mechanism (the dollar lease, terminable at will)"
    defect: "CATALOG_SAMENESS (Chapters 1–3). The fresh surface (crane, room, lease) sits on a
      recognizable chassis: hero_error + craft-authority heroine + credit goal + tradesman
      accountability network + workspace retreat + about 10 of the 18 prior voice tags."
```

What would make the review false (for the architect, not the reader): give the hero an error other than "decided without asking". Make the heroine's goal something other than credit or name. Cut the "older working woman tells the truth" function or give it to someone unexpected. Retire 4–5 of the recurring voice tags in this book. "Look longer," corrective negation and aphoristic summation are the most audible.

---

## AI-texture lines (with quotes)

| Pattern | Instances |
|---|---|
| "X, which for [character] is [outsized gesture]" | "he lowers the phone a quarter of an inch, which for him is a confession" (l.95); "lifts her chin at me, which from Irene is a parade" (l.397); "he backs away beeping, which is Benny's version of a hug" (l.409). The near-relative: "she says it with her eyes and then insults you so you don't make a thing of it" (l.145) |
| "the way you'd [verb]" simile, x8 | "the way you'd watch a kid walk out on a stage" (l.29); "the way you'd turn an old woman toward a better chair" (l.63); "the way you'd say the weather in Grand Rapids in January" (l.229); "the way you say it to a waiter" (l.375); plus l.39, l.137, l.265, l.375 |
| Simile density | About 35 "like / as if / as though" similes in about 6,940 words, roughly one every 200 words |
| "I think about X. I think about Y." anaphora | l.109 (x2), l.165 (x2), l.565 (x5): "I think about the ficus. I think about the lighthouse... I think about version fourteen." |
| Stock beats | "That lands somewhere. I see it land." (l.319); "There's a version of me that hears the gentleness... There's another version that..." (l.315); "It's quick. It's nothing. It's the kind of glance..." (l.293); "Nobody is watching me. Ninety people are very busy not watching me." (l.215); "something in his face slows down" (l.265); "like the weather wants to watch too" (l.83); "none of us says anything for a while" (l.271) |
| Explaining the joke / restating the image | "He says it the way you say it to a waiter. He says it the way he used to say it to me." (l.375, where the second sentence glosses the first); "He says it like a fact on a slide. Like the occupancy rate of a conference room. He says it in the same voice he'd use to tell you that the Eight is now oatmeal." (l.283, one image stated three times) |
| Theme statements / aphorisms | "It's easier to know a thing is happening than to see the slide where it happens." (l.431); "Some people have a beach. I have this." (l.395); "LATER is my professional legacy." (l.433); "That's the kind of crew I have." (l.69); "Lolo would've made a terrible poker player and a great priest." (l.453); "Call him before you think about it so long you turn into a person who doesn't do things." (l.511, earned in dialogue, keep) |
| Template reused within 2,300 words | "Adam made a speech to four people as if it were four hundred" (l.349) / "watched Adam give a speech to two hundred people as if it were two thousand" (l.531) |
| Narrator-withholds tease, x3 | l.165, l.497, l.567 (see HR-04) |
| Triple "which" chain | "a short answer, which is *because I'm here*, and a long answer, which starts two years ago... and which I've never said out loud" (l.497); "which means Walt has put his sandwich down..., which means he's going to do it" (l.539) |

---

## Continuity slips

1. **Marketing's floor.** "Two women from marketing get on at two... On three they get off." (l.191, l.205). But floor four holds "Sales on the east side..., marketing in the middle" (l.209), and later "a desk that belongs to somebody in marketing" is on four (l.319).
2. **Oatmeal exchange out of order (l.193–205).** "Oatmeal's a breakfast." and "'Who made it oatmeal?' I ask." are two consecutive Pip lines. Then "They laugh like I'm doing a bit" comes *after* Bridget has gone quiet and been elbowed. The laugh belongs after "Oatmeal's a breakfast."
3. **Door writing.** Ch1 has "a pencil line inside the door... a line of writing on the birch ply in two different hands" (l.81). Ch2 has "Three lines, two different hands" (l.345).
4. **"Joe" is unidentified** (l.417). The text implies a brother, since "my brothers told me" and Joe brings "my father's welding hood", but the only brother named so far is Marek (l.287).
5. **Badge access.** "Facilities moved the badge access Friday" (l.341). Nothing explains how Pip and Darnell got into the room at night to empty it and unbolt it (l.69). Was it Elvin? A key? It needs one line.
6. **Geography.** The room is in "the far northwest corner, where the two big windows meet over the river" (l.209). The crane works from Monroe Avenue, and the "northwest corner" stairwell window looks "straight down onto Monroe Avenue" (l.381–383). Both can be true only if Monroe runs along the north or west face. On Grand Rapids' Monroe Ave NW, the river is generally behind (west of) the street-front buildings. Verify, or drop "over the river".
7. **Timing (soft).** Ch1 puts the elevator at "ten past nine in the morning" (l.137) and the call at 4:26 a.m., which is about 19 hours apart, while Ch2 opens "Twenty hours earlier." That's acceptable as approximate. Ch3: Pip leaves downtown around 9:30 a.m., yet "Today it's afternoon" when she walks the plant (l.411). The gap isn't accounted for, which is fine if she sat in the truck. One clause would cover it.
8. **Consistent, checked:** the room's size (10x12), the post-free corner, the photo of Hannah (MSU sweatshirt = green sweatshirt), the pens and stapler, Adam's Chicago trip (noon flight, Halvard dinner at seven, "til Tues PM"), Adam's question-mark habit against his texts, the dates for the 2013 napkin, 2014 pull, 2015 wedding and 2018 install, and Lolo's second shift.
