# BLIND_SAMENESS_REVIEW (measured): Continuity Audit re-run

Date: 2026-10-06 · Pipeline v5.0.2 · Catalog Novelty Gate, measured row (the concept PASS is not inherited)

Inputs read: `BLIND_MEASURED_STRIPPED.md` (finished-manuscript fingerprint, surface-stripped),
`CATALOG_STRIPPED_v2.json` (P01–P14 full text; R-B, R-C, R-Z2, R-Z3 reject pool),
`triage_manuscript.md` (script AMBER; nearest R-Z2 0.216, R-C 0.191, R-Z3 0.185, no hard failures).
I did **not** read any earlier review, the gate record, the unstripped catalog, or the
architecture/manuscript rows. Following the Declared-constants note, the packaging hook (husband
publicly gives her founding office to another woman executive, no physical affair, "barely uses it";
she owns a third; the boardroom learns whose idea it was; he begs; they reconcile) is **reported, not
counted under H7**. It still counts on core axis 1 under H1, because that axis is part of the book's
structure.

```yaml
BLIND_SAMENESS_REVIEW:
  candidate: E2-manuscript-measured        # "My CEO Husband Gave Her My Corner Office", finished manuscript
  comparison_set: [P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13, P14, R-B, R-C, R-Z2, R-Z3]
  stripped: true
  reviewer: independent-subagent-blind-3
  reject_pool_checked: true                # R-B, R-C, R-Z2, R-Z3 all scored below
  recycled_reject_of: none                 # max 3/8 strict vs R-Z2; but R-Z2's disqualifying device has migrated in (see house_template)
  one_beat_sheet_test:
    single_sheet_fits_all: false
    sheet_if_true: n/a
    beats_that_break_it:
      - "P01–P07: fit 1/8 (inciting only). Bind, first decision (she stays and strikes, not exits), midpoint, lowest point, climax, repair and ending all break."
      - "P09: fits 1–2/8 (beat 8 no-epilogue private reconciliation; beat 1 only by generalising 'another woman doing wife-work')."
      - "P12: fits 1/8 (beat 5 only if the actor of the unilateral public announcement is ignored, which is an exception clause)."
      - "P14: fits 0–1/8. P10, P11, P13, P08: 0/8."
      - "R-Z2: fits 3/8 (inciting, equity-deadlock bind, no-epilogue private reconciliation). R-Z3: 1 strict, 3 with partials (inciting, room-claim first act, collective-vote climax). R-B: 2/8. R-C: 1/8."
      - "No book reaches 7/8. Sheet fits zero comparison books: PASS on this test."
  pairwise_core_matches:     # strict = same mechanism; adv = strict + partials (adversarial ceiling)
    - {book_id: P01, count: "1 strict / 1 adv", axes: [1]}
    - {book_id: P02, count: "1 / 1", axes: [1]}
    - {book_id: P03, count: "1 / 1", axes: [1]}
    - {book_id: P04, count: "1 / 1", axes: [1]}
    - {book_id: P05, count: "1 / 2", axes: [1, "6 partial"]}
    - {book_id: P06, count: "1 / 1", axes: [1]}
    - {book_id: P07, count: "1 / 1", axes: [1]}
    - {book_id: P08, count: "0 / 0", axes: []}
    - {book_id: P09, count: "1 / 3", axes: ["1 partial", "4 partial", 8]}
    - {book_id: P10, count: "0 / 1", axes: ["7 partial"]}
    - {book_id: P11, count: "0 / 1", axes: ["4 partial"]}
    - {book_id: P12, count: "0 / 3", axes: ["1 partial", "2 partial", "5 partial (actor inverted)"]}
    - {book_id: P13, count: "0 / 0", axes: []}
    - {book_id: P14, count: "0 / 2", axes: ["1 partial", "7 partial"]}
    - {book_id: R-B, count: "2 / 2", axes: [1, 2]}
    - {book_id: R-C, count: "1 / 2", axes: [1, "2 partial"]}
    - {book_id: R-Z2, count: "3 / 4", axes: [1, 2, "4 partial", 8]}
    - {book_id: R-Z3, count: "1 / 3", axes: [1, "3 partial", "6 partial"]}
  shape_matches:   # candidate triple: commission · accepting_a_consequence_he_could_avoid · object_at_rest
    - P01-P07: {inciting_kind: "same (inferred: husband's public erasure = commission; rows lack shape fields)", repair_shape: different, ending_image_class: "unknown (not filed); epilogue months-later, not object at rest", triple_repeats: false, climax_repair_pair_repeats: false}
    - P08: {inciting_kind: different, repair_shape: different, ending_image_class: "unknown", triple_repeats: false, climax_repair_pair_repeats: false}
    - P09: {inciting_kind: different, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - P10: {inciting_kind: different, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - P11: {inciting_kind: different, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - P12: {inciting_kind: different, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - P13: {inciting_kind: different, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - P14: {inciting_kind: different, repair_shape: "different primary; SAME as P14's secondary (FLAG; P14 is one of the previous three entries)", ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - R-B: {inciting_kind: same, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - R-C: {inciting_kind: same, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - R-Z2: {inciting_kind: same, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    - R-Z3: {inciting_kind: same, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
  staging_matches:   # candidate: workplace_floor / workforce / no_evidence / vote / quiet_tally
    - P01-P07: {count: "0 strict / 2 adv (inferred: public assembly venue + whole-community audience)", fields: ["venue~", "audience~"], mechanism_pair_also_matches: false, note: "no filed staging (schema 1.0); inferred from climax_mechanism + signature scenes; back-fill required"}
    - P08: {count: 0, fields: [], mechanism_pair_also_matches: false, note: "inferred"}
    - P09: {count: "0 / 1", fields: ["authority~ (heroine's own choice)"], mechanism_pair_also_matches: false}
    - P10: {count: 0, fields: [], mechanism_pair_also_matches: false}
    - P11: {count: "0 / 1", fields: ["authority~"], mechanism_pair_also_matches: false}
    - P12: {count: "0 / 1", fields: ["authority~"], mechanism_pair_also_matches: false}
    - P13: {count: "0 / 2", fields: ["venue~ (mass assembly)", "audience~ (whole community)"], mechanism_pair_also_matches: false}
    - P14: {count: "1 / 2", fields: [spectacle_mode, "venue~ (her workplace, but private, at night)"], mechanism_pair_also_matches: false}
    - R-B: {count: 0, fields: [], mechanism_pair_also_matches: false}
    - R-C: {count: "0 / 1", fields: ["audience~"], mechanism_pair_also_matches: false}
    - R-Z2: {count: "1 / 2", fields: [evidence_delivery, "authority~"], mechanism_pair_also_matches: false}
    - R-Z3: {count: "1 / 3", fields: [decisive_authority, "venue~", "audience~"], mechanism_pair_also_matches: false}
  occupation_swap:
    survives_unchanged: false
    reasoning: >
      Swap the company that makes factory-built, crane-set rooms for (say) a software firm or a
      restaurant group. Axis 1 survives (any company has an office to give away), but that axis is
      the declared packaging. Axis 4 does not: the midpoint depends on the office being the first
      unit the company ever built, craneable, so that a video of it lifting creates deposits for
      her original design, which sit in escrow until steel is cut under her own founding rule. A
      non-manufacturer has no prototype to lift, no steel-cut escrow and no cash clock tied to
      production. Axis 6 does not survive either: a 6 a.m. shift-change vote on Saturdays versus
      closing his second plant, with a crew trust, needs crews, shifts and plants. The abstract
      shape "put a plan to an employee vote" carries over, but its content and its stakes do not.
      Two of the three tested axes change, so the profession is causal, not colour.
  recognizability_line: >
    The wife takes the disputed room away overnight, in public, then watches the demand her stunt
    created get starved by her own veto. The book ends on a quiet counted vote, where she adopts her
    husband's offer to sacrifice his own project, not on a public reckoning.
  house_template:
    found: true
    items:
      - "HIT. Mutual-fault rebalancing device. The heroine is shown committing the hero's own sin, and the past is revealed to make her the one who broke the shared rule first. In the manuscript it appears twice: (i) at the lowest point she makes a unilateral public announcement without telling anyone first, his exact hero-error, and it is named back at her ('Now you know what it's like to be scared and alone with it'); (ii) in the Ch 25 narrator-wrong reversal, she believed he stopped the ritual first, but he kept coming alone for three weeks. Recurs in P09 (midpoint: her overfunctioning), P11 (midpoint: the elder names the same pattern in both), P14 (midpoint: both were relieved by the absence) and R-Z2 (past reveals the heroine broke the rule first; R-Z2 was REJECTED under H7 for exactly this). The manuscript moves it off the midpoint, but a repeat reader clocks it regardless of chapter."
      - "HIT. Secret-then-discovered devotion. He did the loving thing unseen and she learns of it later, which recasts her grievance (Ch 25: 'he came alone for three weeks and she never knew', told once, to her). Recurs in P09 (rides arranged and told to no one, learned by accident) and P11 (bed and gutters done without telling her, then reported back to her). The manuscript's REPAIR rhythm deliberately avoids this (told beforehand, unwatched, unverified), but the reversal reinstates the same emotional key through the backstory."
      - "HIT (moderate). 'Deciding alone' is the sin and asking or consulting is the cure. The father's rule is 'nobody finds out alone'; her unilateral act is the lowest point; the climax is her putting the plan to a vote; the resolution has her asking him into the room. Recurs in P14 (the heroine asks instead of commanding, which triggers the climax), P11 and P12 (the hero learns to ask before deciding), and R-Z2 (hero error: decides alone, confides elsewhere). This is the heroine-learns-to-ask template spread across both spouses."
      - "FLAG. An elder parent supplies the book's moral rule. P09 (inherited warning) and P11 (the dying father-figure names the pattern) do this; here a LIVING father does. Dead to living is a surface inversion of the same device."
      - "FLAG. The final configuration gives the hero a place in the heroine's workspace: his chair in her original room every morning at seven. Echoes P14 (shared bench, months later) and P12 (shared name and office). This book avoids the months-later jump and the shared desk, and its ending-image class (object at rest) is new to the set, so it is a flag, not a hit."
      - "FLAG. Climax at a public assembly (pen-name pattern: P01–P07, P10, P13, R-Z3). Here the staging changes four of five fields (no evidence, a vote, a quiet tally, and no accountability for the marital wrong), so it is not the house's 'public reckoning'."
      - "FLAG. A benign secret unilateral act by the hero is revealed (the secret share pledge at the midpoint). Echoes P11's midpoint and P12's secret equity negotiation. It is one strand of a three-strand midpoint, so it is a flag."
      - "REPORTED, NOT COUNTED (declared constants). The inciting kind is commission, the husband publicly putting another woman in the wife's place without an affair (P01–P07, P03/P07 explicitly; P09 and P14 by function; all four rejects). The public credit correction ('hers') is moved from climax (P01–P07) to midpoint. The hero begs."
      - "CLEAR: fail-then-succeed repair (none; his acts work first time); witness-pattern repair (guarantee, apology and ending the calls are all unwitnessed); heroine sets terms (explicitly never); relocation to a family asset (none); dead-parent legacy (father is living; see the flag above); documentary midpoint (the midpoint is a financial disclosure that reverses her leverage, not documents converting harm into a claim); hero submission (they argue as equals and she adopts HIS idea); months-later shared-workspace epilogue (no epilogue, no time jump); last-image class (object at rest appears in no other row)."
  voice_signature:
    convergence_flags: "not assessed by this reader (no series_diff.py §6 output in the stripped inputs)"
    house_habits: "not assessed"
    per_pov_coverage: "not assessed"
  blind_voice_test:
    run: false
    readers: 3
    correct_identifications: null
    evidence_type: null
  repeat_reader_review_draft: >
    "Different job, different hook, and honestly the crane opening and the floor vote were fresh.
    But I've read this author's marriages before, and I saw the turn coming. Halfway through, the
    wife does the exact thing she's furious at him for, someone tells her so, and then a late
    chapter reveals he'd been quietly showing up all along and she was the one who stopped first. It
    happened with the cards, it happened with the dying father-in-law, it happened with the twin. Every
    time the author has to make it 'both their faults' before the kiss, and every time there's a
    secret good deed she finds out about. The ending was quieter than usual, which I liked."
  verdict: FAIL
  strongest_reasons:
    - "H7 (house template): the mutual-fault rebalancing device and the secret-then-discovered devotion beat recur across P09, P11 and P14 (and caused R-Z2's rejection). They converge in the manuscript at the lowest-point mirror line and the Ch 25 narrator-wrong reversal. A rejected concept's disqualifying device has migrated into the finished book."
    - "H1 PASS: max 3/8 strict, 4/8 adversarial (R-Z2, reject pool); max published 1/8 strict, 3/8 adversarial (P09, P12)."
    - "H2 PASS: no shared run of four ordered macro-beats with any row. R-Z3 shares room-given, then heroine claims the room, then alliance with the rival, then a collective vote, but not consecutively."
    - "H3 PASS: midpoint and climax are manufacturing-bound."
    - "H4 PASS: vs nearest P09, nine or more core/supporting differences."
    - "H5 PASS with flags: no triple, no climax+repair pair. Single collisions: commission (rejects; declared) and accepting-a-consequence (P14 secondary)."
    - "H8 PASS: max 1/5 strict, 3/5 adversarial (R-Z3), with the mechanism pair not matching. Caveat: P01–P08 staging is inferred, not filed."
```

---

## Core-axis detail for pairs at 3 or more (by function, adversarial)

Candidate axes (my compression): **1** the husband publicly installs another woman (an executive he
leans on emotionally) in the wife's founding office. **2** A sale needs 75%, so her third is a veto,
and a lock-up stops her selling: neither of them can exit. **3** She removes the office overnight and
self-publishes the video, at the cost of censure, a founder-risk flag, a fine and public humiliation.
**4** In the boardroom, her stunt's demand is starved by her own veto and escrow rule, he credits her
("hers"), a cash cliff appears, his secret share pledge is revealed, and he votes against her censure.
**5** She makes a unilateral live-TV "no sale"; the acquirer walks, the covenant test accelerates and
her ally resigns. **6** Heroine-caused workforce vote: he publicly counter-proposes sacrificing his
plant, she adopts it and writes it in herself, and the tally is 97–41–3. **7** He accepts consequences
he could avoid (an unlimited personal guarantee, ending the calls, one kneeling private apology,
proposing his own plant's closure), told beforehand and unwatched. **8** Full reconciliation in the
same week through the restored seven o'clock ritual; no epilogue.

| Axis | R-Z2 (3 strict / 4 adv) | P09 (1 / 3) | P12 (0 / 3) | R-Z3 (1 / 3) |
|---|---|---|---|---|
| 1 Inciting | **match** (identical hook) | partial: another woman does wife-work, no affair; but a private *discovery* | partial: public workplace credit erasure, but by a third party (omission) | **match** |
| 2 Bind | **match**: founder-equity deadlock over a forced sale; neither can exit | different (self-set deadline) | partial: entangled in the company through a personal guarantee and dependence (liability, not veto) | different (shared room) |
| 3 First decision | different (formal trigger vs physical stunt) | different (written terms) | different (withholding labour) | partial: physically claims the room (moves in vs removes) |
| 4 Midpoint | partial: her own founding rule turns on her ≈ "heroine broke the rule first" | partial: her own tactic becomes part of the problem (overfunctioning) | different (surprise fix rejected) | different (women compare notes) |
| 5 Lowest | different (his testimony sinks her) | different (his relapse) | partial: a unilateral public announcement about company ownership without the spouse (actor inverted: his in P12, hers here) | different (hero scapegoats) |
| 6 Climax | different (private settlement on the road) | different (hero-led speakerphone) | different (she declines an offer and sets terms) | partial: her plan is put to a collective body's vote |
| 7 Repair | different (rewrite agreement, move HQ) | different (sustained self-performed care, witnessed) | different (co-negotiated equity, restraint) | different (public confession) |
| 8 Resolution | **match**: reconciled, private, no epilogue | **match**: reconciled, private, no epilogue, same-days close | different (months-later sign) | different (months-later launch) |

Nearest **published** book: **P09** (1/8 strict, 3/8 adversarial), tied on the adversarial count
with **P12** (0/8 strict, 3/8 adversarial). Nearest row overall: **R-Z2** (reject pool), at 3/8
strict and 4/8 adversarial. That is below the H1 threshold and is not a recycled reject, but it shares
the equity-deadlock bind, the private no-epilogue close and (see house template) the "she broke it
first" reveal that got R-Z2 rejected.

**H4 vs P09 (differences):** inciting (public installation vs private discovery: core); bind
(veto/lock-up vs self-set deadline: core); first decision (public stunt vs written terms: core);
lowest point (her own act vs his relapse: core); climax (heroine-caused vote vs hero-led call: core);
repair shape and rhythm (accepting consequence, unwatched, told beforehand vs sustained care, witnessed:
core); staging 0/5 (core); she never sets terms vs timed written terms (supporting); dual first-person
present, in medias res vs single first-person retrospective, at crisis (form). That is nine
differences, at least six of them core, so H4 passes.

**H2 scan:** the candidate's beats are erasure, room removed, boardroom trap and pledge, alliance with
the rival, her unilateral act, his unwatched repairs, the Ch 25 reversal, the floor vote, then the
ritual restored. P01–P07 diverge at beat 2 (exit to a family asset). P12 shares only erasure and the
unilateral announcement. R-Z3 shares four items in order (room given, room claimed, rival becomes ally,
collective vote), but the candidate's boardroom midpoint and R-Z3's forced-proximity beat break
consecutiveness, and R-Z3's failure and confession beats differ. No run of four, so H2 passes.

## Why FAIL (H7), and the narrowest fix

The structural surface of this manuscript is genuinely new to the shelf. It has a stunt-driven first
act, a midpoint where the heroine's own leverage turns on her, a heroine-caused rupture, an
unwitnessed repair told in advance, a quiet-tally vote climax staged differently from every filed row,
no epilogue, and an object-at-rest last image. What a repeat reader of P09, P11 and P14 will clock
before the plot is the **emotional rebalancing key**: she turns out to have done his sin, and he turns
out to have been secretly faithful. That key was the reason R-Z2 was rejected, and it has resurfaced
here at the lowest point and in Ch 25.

Narrowest revision that would clear H7 without touching the core architecture:
1. **Cut or recast the Ch 25 narrator-wrong reversal.** Either drop "he came alone for three weeks
   and she never knew", or make the reversal cost *him* (a fact that worsens his account) or reveal
   something neither of them knew, so it neither exonerates him nor makes her the one who broke the
   ritual first.
2. **Remove the mirror line at the lowest point** ("Now you know what it's like to be scared and
   alone with it") and let the TV announcement stand as a strategic error under pressure, with its
   own logic, not as "now you are him."
3. Optionally decouple the father's rule from an explicit "ask, don't decide alone" moral, or give
   the climax a reason other than consultation (for example, the vote is legally required), so the
   learn-to-ask template is not the book's thesis.

After those edits, re-run this blind read on the revised measured row. On the evidence here, H1–H5
and H8 would hold, and H6 (voice and 4-grams, via `series_diff.py`) still needs its own run.
