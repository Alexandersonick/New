# BLIND_SAMENESS_REVIEW — concept batch (X1, X2, X3)

Catalog Novelty Gate, pipeline v5.0.2, concept stage (before Concept Validation).
Scored as one batch: every candidate against every prior row and against its siblings.

```yaml
BLIND_SAMENESS_REVIEW:
  batch: [X1, X2, X3]
  stage: concept
  reviewer: independent-subagent-blind-1
  stripped: true
  inputs_read:
    - catalog/BLIND_BATCH_STRIPPED.md          # candidates, surface-stripped
    - catalog/CATALOG_STRIPPED.json            # P01–P14, all evidence_level FULL_TEXT
    - catalog/triage_A.md, triage_B.md, triage_C.md   # catalog_similarity.py v1.1, all AMBER
    - master-fiction-pipeline SKILL.md "The Catalog Novelty Gate" (H1–H8, blind-scoring rule)
    - references/schemas.md BLIND_SAMENESS_REVIEW schema
  inputs_deliberately_not_opened: [CATALOG.json, candidate_A.json, candidate_B.json, candidate_C.json,
                                   project files outside catalog/]   # kept the read blind
  blindness_note: >
    The triage files print unstripped prior titles and candidate working titles. I saw them but
    did not score on them. Surface leaks in the stripped catalog (a town name, the apiary, character
    names in core_axes prose) are surface variables and were ignored, as the file's note says.
  comparison_set: [P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13, P14, X1, X2, X3]
  reject_pool_checked: true
  reject_pool_note: >
    The pen name has no earlier rejected, planned, or CONCEPT/OUTLINE rows. All 14 catalog rows are
    published FULL_TEXT books. The pool is the 14 shelf books plus the batch's own siblings.
  recycled_reject_of: none
  lanes: >
    Same lane (marriage_crisis_grovel): P01–P07, P09, P11, P12, P14 (11 rows). Cross lane: P08, P10, P13
    (3 rows). That is why all three triage runs are AMBER ("3 cross-lane, target 5").
  shape_and_staging_data: >
    P09–P14 have recorded inciting_kind, repair_shape, ending_image_class and five climax-staging
    fields. P01–P08 have none. Their shapes below are INFERRED from tags and signature_scenes and are
    marked (inf). No staging is inferred for P01–P08: H8 can only be scored against P09–P14.
  scoring_method: >
    Each of the 8 core axes is scored by function, after consolidating synonyms. FIRM means the same
    mechanism. PARTIAL means the same function with a materially different mechanism, or a match on
    one of two components. The H1 count uses FIRM. "Weighted" (FIRM + 0.5 × PARTIAL) is reported as
    an adversarial ceiling, because a concept-stage row is prose and will move at architecture.
```

---

## 0. A finding about the whole batch, before any per-candidate score

The packaging-fixed hook (axis 1) is the shelf's dominant hook. In P01–P07 the husband erases
the wife's work at a public career moment, often centring another woman: an award dedication, a TV
"muse", a wedding toast, a retrospective. P12 has a public credit erasure inside the shared family
company. That is **8 of 14 priors.** All three candidates therefore start with axis 1 = FIRM
against P01–P07 and P12. The hook's other half, the husband leaning emotionally on another woman
with no affair, is P09's hero error (delegating intimacy to a female assistant) and is adjacent to
P13 (the hero defers to his female agent).

- This puts all three candidates into the H7 house template on the **inciting mechanism**. No
  choice between candidates can clear it. It is a packaging decision.
- The gate gives only one exit: a **`declared_constants`** entry in `SERIES_LEDGER`. That is a
  user-level, dated series decision, and I cannot make it. Without it, the hook is a recorded
  H7 item for every candidate, and the other seven axes have to carry all of the novelty.
- The inciting **kind** (commission) collides only with the inferred P01–P07 rows. Recorded kinds
  for P09–P14 are discovery, external_blow ×3, omission and betrayal. By the v5.0.2 pigeonhole rule
  this is a single-axis flag, not a fail.

---

## 1. Pairwise core-axis matches (8 axes, by function)

Axis key: 1 inciting · 2 bind · 3 first irreversible decision · 4 midpoint · 5 lowest point · 6 climax action · 7 repair · 8 resolution/ending.

### 1a. Summary grid: FIRM count (weighted ceiling)

| Prior | X1 | X2 | X3 |
|---|---|---|---|
| P01 | 2 (3.5) | 1 (2.5) | 3 (4.5) |
| P02 | 2 (3.0) | 1 (2.5) | **4 (5.5)** |
| P03 | 2 (3.0) | 1 (2.0) | 3 (5.0) |
| P04 | 2 (3.0) | 1 (2.0) | **4 (5.5)** |
| P05 | 2 (3.5) | 1 (3.5) | 3 (4.5) |
| P06 | 2 (2.5) | 1 (2.0) | 3 (4.5) |
| P07 | 2 (3.0) | 1 (2.0) | **4 (5.5)** |
| P08 | 0 (0.5) | 0 (0.0) | 0 (0.5) |
| P09 | 1 (2.0) | 0 (1.0) | 0 (1.0) |
| P10 | 0 (0.0) | 0 (0.5) | 1 (1.5) |
| P11 | 0 (1.5) | 0 (0.5) | 0 (1.0) |
| **P12** | **3 (4.5)** | **3 (5.0)** | 1 (3.0) |
| P13 | 0 (1.5) | 0 (0.5) | 1 (2.0) |
| P14 | 1 (3.0) | 0 (1.0) | 0 (1.5) |
| **Max** | **3 vs P12 (4.5)** | **3 vs P12 (5.0)** | **4 vs P02/P04/P07 (5.5)** |

### 1b. Detailed pairs (≥3 FIRM, or weighted ≥4.5)

```yaml
pairwise_core_matches:
  - candidate: X1
    book_id: P12
    count: 3            # weighted 4.5
    firm: [1_inciting, 2_bind, 5_lowest]
    partial: [3_first_decision, 4_midpoint, 7_repair]
    differ: [6_climax, 8_resolution]
    notes:
      1: Public erasure of the wife's standing inside the shared company (P12 omission by a partner, husband silent; X1 commission by husband). Same function, different shape.
      2: "Her legal/financial stake in the husband-run company and her duty to its workforce make walking away impossible." P12 = loan guarantee + 11 employees' jobs on her systems; X1 = undissolvable third-share veto + workforce her late father trained. FIRM.
      3: Both are an early, costly act of defiance inside the company. P12 withholds work until named (conditional strike); X1 seizes the office overnight (spectacle seizure). Different mechanism, same slot → PARTIAL.
      4: X1's midpoint adds a third party publicly crediting her (P12's client does this on a recorded call), plus a husband's secret share/equity move that reframes the problem (P12 Ch14–16). The core mechanism differs (X1 = leverage inversion, P12 = gift rejected) → PARTIAL.
      5: Husband's secret, unilateral business deal about the company, made without her, comes out = repeated core harm. FIRM.
      7: Hero restraint (P12 silent at walkthrough, asks before acting; X1 "does not pitch, only answers") plus giving up a control lever (P12 tiebreaker struck; X1 fallback withdrawn). Dominant shapes differ (relinquishing control vs accepting a consequence) → PARTIAL.
      6/8: Workforce vote vs private dictated terms. Object at rest at home vs renamed sign and act in motion. DIFFER.
  - candidate: X2
    book_id: P12
    count: 3            # weighted 5.0. This is the H1 threshold on the adversarial reading.
    firm: [1_inciting, 6_climax, 7_repair]
    partial: [2_bind, 3_first_decision, 4_midpoint, 5_lowest]
    differ: [8_resolution]
    notes:
      6: Heroine privately sets or rewrites the terms of the ownership deal while he accepts them (P12 site-trailer terms dictated, he writes them down; X2 closing-table rewrite). FIRM.
      7: Ownership is restructured so that he holds capital without control (P12 co-negotiated equity, his tiebreaker struck; X2 proceeds wired back with no control rights). FIRM.
      3: A financial/contractual ultimatum over her standing (P12 "name on it or I don't finish"; X2 shotgun trigger) → PARTIAL.
      4: The hero's unilateral surprise move turns her win into a new problem (P12 title/raise/bracelet; X2 elects to sell) → PARTIAL.
      5: A secret deal made without her surfaces; both books include a secret competing partnership in another city (P12's rival offer and Seattle visit; X2's co-founding offer from the executive) → PARTIAL.
  - candidate: X3
    book_id: P02            # identical result vs P04 and P07; P03 at 3 firm
    count: 4            # weighted 5.5
    firm: [1_inciting, 5_lowest, 6_climax, 7_repair]
    partial: [2_bind, 3_first_decision, 8_resolution]
    differ: [4_midpoint]
    notes:
      3: Early exit from the husband's sphere to reclaim her vocation (P0x to a family asset; X3 to the rival). Destination differs, function is the same → PARTIAL.
      5: The husband falls back into the core harm under pressure (sides with the other woman's judgment against the wife's authorship) → FIRM.
      6: Her authorship is proved with original records before a deciding body: P02 public credit correction + legal transfer; P04 counter-film screening + husband confession; P07 provenance correction by the institution. X3 = testimony + design records in mediation. FIRM.
      7: Public accountability before the people who matter: he says on the record that the work is hers. P0x repair = public accountability (+ redistribution). FIRM.
      8: Reconciled, with her standing publicly corrected → PARTIAL.
  - candidate: X3
    book_id: P10
    count: 1
    firm: [6_climax]     # heroine's public evidence reveal, ruled on by officials (see H8)
```

The remaining pairs are listed here so the record is complete. X1 vs P01–P07: FIRM 1 and 5 (husband repeats the core avoidance under pressure); PARTIAL 2 or 7 (company ties; public-accountability component), and P01 also PARTIAL 8 (structural relocation lands in X1's ending). X1 vs P14: FIRM 5 (secret "carrying it alone" = P14 hero error `unilateral_carrying_as_avoidance`); PARTIAL 1, 4, 6, 7. X1 vs P09: FIRM 5; PARTIAL 3 (she strips the other woman of what was handed over) and 7 (he does himself "a job he would always have delegated").

**Max overlap per candidate:** X1 = 3 (P12) · X2 = 3 (P12) · X3 = 4 (P02 / P04 / P07).
Ties on FIRM go to the weighted ceiling: X1 4.5 < X2 5.0 < X3 5.5.

---

## 2. Shape matches vs every prior (H5)

Candidate triples: **X1** commission · accepting a consequence he could avoid · object at rest.
**X2** commission · restitution · spoken line. **X3** commission · letting her be right · third party's gesture.

```yaml
shape_matches:
  X1:
    P01-P07(inf): {inciting_kind: same(inf), repair_shape: different, ending_image_class: different(inf), triple_repeats: false, climax_repair_pair_repeats: false}
    P08(inf):     {inciting_kind: different, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    P09:          {inciting_kind: different, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    P10:          {all: different, triple_repeats: false, climax_repair_pair_repeats: false}
    P11:          {all: different, triple_repeats: false, climax_repair_pair_repeats: false}
    P12:          {all: different, triple_repeats: false, climax_repair_pair_repeats: false}
    P13:          {all: different, triple_repeats: false, climax_repair_pair_repeats: false}
    P14:          {inciting_kind: different, repair_shape: "different (primary) — FLAG: X1's primary = P14's SECONDARY", ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: false}
    H5: CLEAR. Flags: commission vs inferred P01–P07, and accepting-a-consequence vs P14's secondary repair.
  X2:
    P02/P05(inf): {inciting_kind: same(inf), repair_shape: "same(inf) — legal transfer / ownership transfer read as restitution", ending_image_class: different(inf), triple_repeats: false, climax_repair_pair_repeats: "partial (P05: ownership-transfer climax; redistribution repair)"}
    P12:          {inciting_kind: different, repair_shape: different, ending_image_class: different, triple_repeats: false, climax_repair_pair_repeats: TRUE}
    others:       {triple_repeats: false, climax_repair_pair_repeats: false}
    H5: FAIL. Clause 1: climax (private terms-setting on the ownership deal) and repair (ownership restructured, he cedes control) both repeat P12. Clause 3 is at risk vs P05 on inferred shapes.
  X3:
    P02/P04/P07(inf): {inciting_kind: same(inf), repair_shape: "same(inf) — public status correction = letting her be right before the people who mattered", ending_image_class: "unknown(inf); P07 ends on the institution correcting the record, a third party's act", triple_repeats: "possible(inf)", climax_repair_pair_repeats: TRUE}
    P13:          {repair_shape: "FLAG: X3 primary = P13 secondary", climax_repair_pair_repeats: false}
    H5: FAIL. Clause 1: climax + repair both repeat P02, P04 and P07 (firm). Clause 3: two of three shapes plus the pair, on inferred shapes.
```

---

## 3. Climax staging vs P09–P14 (H8)

Fields: venue / audience / evidence delivery / decisive authority / spectacle mode.

| Cand. | Staging | P09 | P10 | P11 | P12 | P13 | P14 | H8 |
|---|---|---|---|---|---|---|---|---|
| X1 | workplace floor / workforce / no evidence / vote / quiet tally | 0 | 0 | 0 | 0 | 0 + 2 partial (audience = a collective; authority = the collective decides) | 1 (spectacle) + 1 partial (venue = her workplace) | **CLEAR** (max 1) |
| X2 | document exchange / two + counsel / documents / contract / private line | 2 (audience two + professional third; spectacle) + 1 partial venue | 0 + 1 partial (documents) | 1 + 1 partial | 1 (spectacle) + 3 partial (private room; two of them; her own choice instantiated as contract) | 0 | 0 | **Borderline.** Clause 2 vs P12: climax + repair both match; staging is 1 firm + 3 partial against a threshold of ≥3. Not called on its own; H5 carries the fail |
| X3 | mediation room / institution / documents read out / official's decision / room turns audibly | 0 | **3 firm (evidence, authority, spectacle) + 1 partial (audience = the deciding institution in the room)** | 0 | 0 | 1 (spectacle) | 0 + 3 partial (log read, expert certifies) | **Borderline FAIL vs P10.** Clause 1 = 3.5/5. If the audience counts, it is 4/5 |

Spectacle mode is itself a house distribution: private_line ×3 (P09, P11, P12), room_turns_audibly ×2
(P10, P13), quiet_tally ×1 (P14). Each candidate takes an existing value. X1 takes the least-used
one, and its decisive authority (a vote) and evidence (none) are new to the set.

---

## 4. Candidates vs each other (must differ on ≥5 core axes)

| Pair | Same | Partial | Differ (firm) | Verdict |
|---|---|---|---|---|
| X1–X2 | 1 (fixed) | 5 (hero's secret deal tied to the executive comes out) | 2, 3, 4, 6, 7, 8 = **6** | OK |
| X1–X3 | 1 (fixed) | 5 (husband acts against her under the executive's influence), 7 (public accountability before a board) | 2, 3, 4, 6, 8 = **5** | OK (at minimum) |
| X2–X3 | 1 (fixed) | 3 (she forces separation from the shared company in ch 3–4), 5 (husband aligns with the executive against her), 6 (document-based legal-room climax) | 2, 4, 7, 8 = **4** | **Short by one.** A batch-design defect. It does not change the outcome because both fail elsewhere. |

All three triples differ, as required. All share "commission" only because of the fixed hook.
Siblings converge on axis 5: in all three the lowest point is "the husband sides with or confides
in the executive against the wife." That is the hook leaking into the rupture. See house template.

---

## 5. One-beat-sheet test

```yaml
one_beat_sheet_test:
  X1:
    sheet: [public reassignment of her founding space to another woman, dismissing her;
            her ownership stake is a veto she cannot shed, so she stays in daily proximity;
            she seizes the space back overnight in a public spectacle that costs her standing;
            at her censure the rival credits her, then a hidden cash crisis turns her veto against the workforce;
            his secret fallback deal, and what he confided to the rival, come out; she sends him from the house;
            she puts her own rescue plan, paid for in her own equity, to a workforce vote, and he will not pitch it;
            he takes consequences he could avoid, in person;
            days later the founding space stands at home, at rest]
    fits: [none]          # best fit P12 = 3/8 (beats 1, 2, 5); P01–P07 = 2/8
    beats_that_break_it: [3 (seizure, not exit or strike), 4 (leverage inversion), 6 (collective vote), 8 (object at rest, no epilogue)]
    result: PASS
  X2:
    sheet: [public erasure; a binding ownership instrument; she fires an ultimatum over ownership;
            his surprise move turns her win into a risk; his secret deal surfaces;
            she sets the terms privately at the table; he restructures money and ownership, ceding control;
            the arrangement is renegotiated]
    fits: [P12 at 6/8 (beat 2 needs the exception "no clock"; beat 8 "he leaves the company" vs shared renamed company)]
    result: PASS on the letter (fits 1 book at <7/8), but this is the closest single-book fit in the batch
  X3:
    sheet: [public erasure; marriage and shared life hold her; she leaves to reclaim her work elsewhere;
            mid-book complication; husband turns against her under pressure, repeating the harm;
            she proves authorship with original records before a deciding body;
            husband affirms on the record that the work is hers; reconciled with standing publicly restored]
    fits: [P02 7/8, P04 7/8, P07 7/8]      # only beat 4 (bait reveal vs paper trail) breaks it
    result: FAIL (fits ≥2 priors)
```

---

## 6. House-template question

```yaml
house_template:
  found: true
  items:
    - item: Inciting = husband's public erasure of the wife's labour at a career moment, often centring another woman
      recurs_in: [P01, P02, P03, P04, P05, P06, P07, P12]   # 8/14
      candidates: [X1, X2, X3]      # packaging-fixed; see §0
    - item: Hero error = intimacy or confidence routed through another woman, no affair
      recurs_in: [P09, P13 (defers to female agent), P03/P07 (other woman as muse/centre), P14 (twin in her place)]
      candidates: [X1 (confided the funeral reason to the executive), X2 (career elopement), X3 (sues on her advice)]
    - item: Lowest point = the husband relapses into the core fault under pressure
      recurs_in: [P01–P07, P09, P11, P12, P14]   # 11/14; P13 = defers to agent
      candidates: [X1, X2 (variant: chooses the other woman), X3]
    - item: Repair staging rhythm = witness pattern (named onlookers attest to the changed behaviour)
      recurs_in: [P01–P07 community-witnessed, P09, P11, P12, P13, P14]   # 13/14
      candidates: [X1 ("the witnesses are the crew, her family and the board"), X3 (testifies before the board)]
      note: X2's restitution is private. This is the one house rhythm X2 avoids.
    - item: Hero submits to her authority at the climax or in the repair ("Ask Maud", silent at walkthrough, writes her terms down, confirms her account)
      recurs_in: [P11, P12, P13, P14]
      candidates: [X1 ("It's her plan. I'm in."; "does not pitch, only answers"), X2 (capital without control rights)]
      note: The skill names "his submission to her authority" as one shape, not a default.
    - item: Heroine sets terms (early or at the climax)
      recurs_in: [P09, P11, P12, P13, P14]   # 5 of the 6 recorded
      candidates: [X2 (names the price; rewrites the deal)]
      note: X1 inverts it. At the climax she hands the decision to others.
    - item: Documentary / paper-trail midpoint, or third party publicly restoring her credit
      recurs_in: [P01–P07, P10, P14 (forged resignation read aloud), P12 (client credits her on a recorded call)]
      candidates: [X1 midpoint (rival tells the board every idea is hers), X3 climax (records produced)]
    - item: Public reckoning climax before a community or institution
      recurs_in: [P01–P07, P10, P13]
      candidates: [X3 (fully), X1 (adjacent: public and collective, but no evidence and no reckoning, a vote on a plan)]
    - item: Early exit / relocation to a family asset or own space
      recurs_in: [P01–P07, P14, P11 (house inherited jointly)]
      candidates: [X3 (exit to rival), X1 (inverted: the husband moves into the removed office, and the founding object holding her father's desk is relocated home at the end)]
    - item: Dead or dying parent's legacy object or wound as the emotional key
      recurs_in: [P09 (father's box of cards), P10 (father's murder), P11 (dying father figure, ring, recipe box), P13 (father confession)]
      candidates: [X1 (late father, missed funeral confided to rival, father's desk in the final image)]
    - item: Repair beat = the hero endures a family meal
      recurs_in: [P09 (burnt chicken at his mother's, Thanksgiving), P11 (harvest supper)]
      candidates: [X1 (Sunday dinner with her hostile brothers)]
    - item: Repair beat = he personally does the task he always delegated
      recurs_in: [P09 (the whole repair)]
      candidates: [X1 (tells sixty workers himself)]
    - item: Care object = coffee / tea / food
      recurs_in: [P09 Thai food, P10 coffee, P13 proof box, P14 thermos tea]
      candidates: [X1 final image "two mugs"]
    - item: Ending = act in motion + months-later epilogue
      recurs_in: [act in motion P09, P12, P13, P14; months-later epilogue in 12/14]
      candidates: none. X1 (object at rest, no epilogue), X2 (spoken line) and X3 (third party's gesture) all step out.
    - item: Macro sequence shared verbatim by P01–P07 (erasure → exit to family asset → revive asset → paper trail → repair fails → public accountability → conditional reconciliation → months later)
      recurs_in: [P01–P07]
      candidates: [X3 runs beats 1–3 (partial on 3) and the accountability→reconciliation tail]
```

Who falls in, in short. **X3** is the P01–P07 template with a lawsuit attached. **X2** reruns
P12's back half. **X1** avoids the house *spine*: no exit, no paper-trail midpoint, no
evidence-reckoning climax, no terms-setting, no months-later epilogue. But it collects six or
seven house *devices* in its repair and ending: the witness pattern, hero submission, the family
meal, the do-it-yourself delegated task, the dead father's legacy, the mugs, and the
relocated founding object.

---

## 7. Occupation-swap test (H3), axes 1, 4, 6

```yaml
occupation_swap:
  X1:
    swap_product_only: >
      Swap the craneable factory-built room for any product with a factory workforce (bakeries, a
      boatyard). Axis 1 survives (packaging hook). Axis 4 survives: board censure, cash crisis and the
      veto inversion are generic governance. Axis 6 survives: a staff vote on deferral-for-equity works
      in any workforce company. The product is load-bearing only at 3 (overnight removal), 7 (he lives
      in the removed unit) and 8 (unit lifted into the garden).
    swap_role: >
      Swap "co-founding one-third owner of the company" for a non-ownership job. The veto, the 75% sale,
      the payroll inversion and the equity-funded vote all vanish. Axes 4 and 6 collapse.
    survives_unchanged: false   # on the role; the ownership position is causal
    reasoning: >
      PASS, marginal. The ownership role is causal. The industry and product are colour at exactly the
      three axes H3 tests. Architecture must make the product's defining property (built in a factory,
      liftable in one night) causal at the midpoint or the climax, or the Story Bible Lock re-run is at
      risk.
  X2:
    survives_unchanged: true-ish
    reasoning: >
      A shotgun buy-sell clause works in any two-owner partnership (law firm, restaurant, clinic).
      Axes 1, 4 and 6 survive any industry swap. The product never touches the plot. H3 FAIL-risk,
      recorded as a flag because H5/H2 already fail.
  X3:
    survives_unchanged: true
    reasoning: >
      "She defects to the rival, he sues, records prove the designs are hers" works for any
      authored IP: songs, films, recipes, code. P02, P03, P04 and P07 already ran it with four
      different professions. H3 FAIL.
```

---

## 8. Recognizability lines (no names, jobs, places)

- **X1:** "She keeps the one vote that can stop the sale of what she built, then spends it: she hands part of her own share to the people who build the thing and lets them decide by a show of hands." Clear; needs no help.
- **X2:** "She pulls a forced buy-or-sell trigger on her husband, and he chooses to sell to her because he plans to leave with the other woman." Clear, but on the shelf it reads as "the P12 one where she sets the terms at the table."
- **X3:** "She defects to the rival, her own husband sues her, and she wins by proving in a hearing that the work was always hers." Clear as a sentence, but its second half is the shelf's line for P02, P04 and P07.

---

## 9. H-condition table and verdicts

| | H1 (≥5 firm) | H2 (4-beat run) | H3 | H4 (nearest; ≥3 core/supporting diffs) | H5 | H6 | H7 | H8 | One-sheet | Recog. |
|---|---|---|---|---|---|---|---|---|---|---|
| **X1** | clear (3 vs P12; 4.5 weighted) | clear (longest run 2) | marginal pass | clear vs P12: climax, first decision, midpoint mechanism, repair shape, ending class, plus ally-turn | clear | n/a at concept (no text) | **FIRES** (staging and device level: witness-pattern repair; hero-submission climax line). Hook-level item shared by the batch, §0 | clear (max 1) | pass | pass |
| **X2** | clear on firm (3); **at threshold weighted (5.0)** | **FAIL vs P12**: midpoint (surprise hero move turns her win) → lowest (secret deal surfaces) → climax (she sets terms privately) → repair (ownership restructured, he cedes control) in the same order | flag | weak: vs P12, only 1st decision, bind clock and ending differ firmly | **FAIL** (clause 1 vs P12) | n/a | FIRES (heroine sets terms; hero submits) | borderline vs P12 | pass (P12 6/8) | weak |
| **X3** | clear on firm (4), **5.5 weighted** vs P02, P04 and P07 | 3-beat runs only | **FAIL** | fail: vs P02/P07, only the midpoint and the destination of the exit differ | **FAIL** (clause 1 firm vs P02, P04, P07; clause 3 inferred) | n/a | FIRES (documentary authorship climax; witness repair; exit) | **borderline FAIL vs P10** (3.5/5) | **FAIL** (fits 3) | weak |

```yaml
verdicts:
  X1:
    verdict: FAIL (as submitted). H7 only: staging and device level; no core-axis or combination fail
    strongest_reasons:
      - Lowest maximum overlap in the batch, 3/8 vs P12 (weighted ceiling 4.5); clear of H1, H2, H4, H5 and H8.
      - Breaks the house spine. The heroine stays and does not exit; the midpoint is a leverage inversion, not a paper trail; the climax is a collective vote with no evidence; it ends on an object at rest with no epilogue.
      - H7 fires because the repair is staged as the house witness pattern and the climax gives the hero the house's "submits to her authority" line. Both can be fixed without changing any of X1's eight core-axis mechanisms.
  X2:
    verdict: FAIL
    rejected_for: H5 (climax + repair repeat P12) and H2 (ordered 4-beat run with P12); H1 at threshold on the weighted reading; H7 (terms-setting, submission)
  X3:
    verdict: FAIL
    rejected_for: H5 (climax + repair repeat P02, P04 and P07), one-beat-sheet test (fits P02, P04 and P07), H3, H7 (it is the P01–P07 template), H8 borderline vs P10

batch_outcome: >
  No candidate passes as submitted. The rule says a batch in which every candidate fails is a
  re-concept, not a pick-the-least-bad. X1 is the only candidate whose failures are confined to
  staging and devices: all 8 of its core mechanisms clear H1, H2, H5 and H8, and the H7 items sit
  in the repair's staging and in two lines of the climax and ending. The smallest legal path is
  therefore a revised X1 (X1-r) carrying the fixes below. X1-r must go back to a fresh blind read
  with two newly built siblings, and X2 and X3 are filed in SERIES_LEDGER.FINGERPRINTS with
  source: concept and the rejected_for notes above. The owner must also decide the §0 hook question
  (re-cut, or dated declared_constants entry). No candidate can resolve it.

selection:
  selected_candidate: X1 (to be revised as X1-r; not a PASS yet)
  basis: lowest maximum core-axis overlap against any shelf book
  nearest_prior: P12
  count: 3/8 firm (axes 1 inciting, 2 bind, 5 lowest point); partial 3, 4, 7; weighted ceiling 4.5
  runner_up: X2. It ties at 3 firm vs P12 but has a weighted 5.0 and hard fails on H5 and H2.
```

---

## 10. X1 weak spots for architecture to fix before drafting (and before the Story Bible Lock re-run)

1. **Repair staging = the house witness pattern (H7, must fix).** Remove the chorus of named
   witnesses (crew, family, board). Make the consequence-taking land unseen: she learns of it late
   and second-hand, or never, or it happens while she is away and nobody reports it. The repair
   *shape* (accepting a consequence he could avoid) is fresh on the shelf as a primary; keep it,
   change its rhythm.
2. **Climax line "It's her plan. I'm in." plus the "does not pitch, only answers" rule (H7, must fix).**
   This is the hero's submission to her authority, as in P11, P12, P13 and P14. Give him a
   non-deferential, costly position in the vote that is not leadership. For example, his own pledged
   shares or his prized second factory go on the same ballot and he loses something by the count, or
   he is absent from the floor as a consequence he accepted. Do not let the climax become hero-led.
3. **Axis 5 lowest point = "husband relapses into concealment under business pressure"** (11/14
   priors, FIRM vs P12 and P14 — P14's hero error is literally "unilateral carrying as avoidance").
   It also repeats across the siblings (the executive involved). Re-engineer the rupture so its cause
   is not his relapse. One option is a cost of her own crane stunt or veto falling on the workforce.
   Another is a reveal that is not a repeat of his core fault. Cut "what he confided to the executive
   and never to her" (P09's delegated-intimacy wound).
4. **Axis 2 bind drifts to P12** ("her stake plus employees depending on her"). Keep the veto as
   the engine, but drop "a workforce her late father helped train" as a reason to stay. Make the bind
   about the veto itself: once she uses it, she owns the outcome either way.
5. **Midpoint first half = a third party publicly restoring her credit** (P12 recorded call, P14
   resignation read aloud, P07 institution). This also pre-pays the house's credit-correction payoff.
   Cut the rival's "every core idea is hers" testimony, or make it private. Keep the payroll /
   pledged-shares / veto-inversion as the sole midpoint mechanism. It is X1's most original axis.
6. **H3 marginal: the product is colour at axes 4 and 6.** Make "built in a factory, liftable in one
   night" causal at the midpoint or the climax. Examples: the rescue plan depends on the factory
   building something only it can; the acquirer's cheapening is visible in the unit; the vote is held
   inside the moved prototype and its fate is on the ballot.
7. **Device pile-up in the repair and the ending.** Cut or replace: the family-dinner gauntlet (P09,
   P11), the task he always delegated (P09), the late-father legacy object and the funeral secret
   (P09, P10, P11, P13), and the "two mugs" (the house's coffee/tea care object). Keep the object-at-rest
   class but choose an object with no drink, food or dead-parent load. Moving the founding object
   home at the end echoes P01–P07's family-asset relocation, so give the move a cost or drop it.
8. **Husband moves into the cold removed office** reverses P14 (heroine to a cot in her unheated
   studio) and echoes P01's "husband takes leave and moves." If kept, it must not be the repair's
   centrepiece.
9. **Ally turn with the rival** (no prior has it) and **the in-medias-res crane opening** (no prior
   uses a flash-forward entry; P09, P12, P13 and P14 are at_crisis linear) are X1's assets. Protect
   them through architecture.
10. **Staging fields must be recorded on the architected row.** X1's climax staging (workplace
    floor / workforce / none / vote / quiet tally) is currently the most novel in the batch. Its
    only house value is the spectacle mode `quiet_tally` (P14). If the vote turns into a speech that
    "turns the room", it drifts into P13's staging (civic meeting / whole town / room turns audibly),
    and H8 must be re-checked.

```yaml
  voice_signature: not run (concept stage; no text)
  blind_voice_test: {run: false, reason: "no prose at concept stage; required at the draft stage if narrative_voice_tags overlap ≥60% with two same-POV priors — X1's first-person present tense is new to the set"}
  repeat_reader_review_draft (X3 only, since one could be written): >
    "Same book as her songwriter, filmmaker and painter ones. Husband takes credit in public, she
    walks, he makes it worse, she pulls out the original files in front of the people in charge,
    he admits it's hers, they make up. This time it's design drawings and a mediator. I could have
    written the last third myself after chapter three."
```
