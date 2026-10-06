# BLIND_SAMENESS_REVIEW — concept batch 2 (Z1, Z2, Z3)

```yaml
reviewer: independent-subagent-blind-2
stripped: true
reject_pool_checked: true
pipeline: master-fiction-pipeline v5.0.2, Catalog Novelty Gate (H1–H8, candidates rule, comparison-set rule, blind-scoring rule, shape axes)
inputs:
  candidates: BLIND_BATCH_2_STRIPPED.md (Z1, Z2, Z3)
  comparison_set_file: CATALOG_STRIPPED.json
  triage: triage_Z1.md (FAIL vs R-X1), triage_Z2.md (AMBER), triage_Z3.md (AMBER)
comparison_set: [P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13, P14, R-X1, R-X2, R-X3, Z1, Z2, Z3]
not_read: BLIND_SAMENESS_REVIEW_concept.md (the earlier review), candidate_*.json (unstripped). This reader worked only from the stripped rows.
batch_verdict: FAIL. No candidate passes, so the gate selects none and calls for a re-concept (rule: "a batch in which every candidate fails is a re-concept, not a pick-the-least-bad").
```

## 0. Method and data caveats

- **Core axes (8):** 1 inciting disruption, 2 bind, 3 first irreversible decision (FID), 4 midpoint reversal, 5 lowest point, 6 climax action, 7 repair mechanism, 8 resolution shape. Machine fields map as `inciting_event`, `containment`, `agency_pattern`, `midpoint_reversal`, `darkest_moment_cause`, `climax_mechanism`/`climax_owner`, `repair_mechanism`, `ending_state`. Axes 1 and the heroine goal are scored **by function**, not by tag string.
- **M** means the same mechanism, **D** means a different one, and **(adv)** marks a match this reader counts when scoring adversarially, with the reason given. Detail pairs (≥3) are stated for every count of 3 or more.
- **Declared constants.** The owner's locked hook is: public handover of her founding office to an executive he leans on, no affair, the boardroom learns whose idea it was, he begs, they reconcile. It puts axis 1 (public erasure before third parties) and axis 8 (reconciliation) at **M** against P01–P07, P12 and all three rejects for *every* candidate. Two counts are therefore given: **raw n/8** and **open-axis n/6** (with axes 1 and 8 exempt, as a SERIES_LEDGER `declared_constants` entry would make them). Each verdict below is checked so that it holds under either count. The hook is not used for an H7 FAIL.
- **Data gaps.** P01–P08 have no staging fields and no shape fields (`inciting_kind`, `repair_shape`, `ending_image_class`). Their H5 and H8 checks are therefore **inferred from the rows' mechanisms**, labelled "(inferred)", and cannot by themselves produce a clean PASS. The triage warns the same: 8 rows lack staging. These should be back-filled before any future PASS is treated as clean.
- **H6 (mechanical text sameness / voice)** cannot run at concept stage because there is no text. It is N/A here and must run at 25%, 50% and 100% of draft.

---

## 1. Declared-constant collision report (reported, not counted under H7)

| Constant | Collides with | Note |
|---|---|---|
| Public handover of her founding office (public erasure of her authorship before third parties) | P01–P07 (`public_partner_erasure`, opening `public_career_ceremony_partner_erasure`), P12 (`public_credit_erasure` in a client meeting), R-X1, R-X2, R-X3 | 8 of 14 published books open on this inciting function. It fixes **inciting_kind = commission** for every candidate, so the candidates' shape triples can vary on only two of the three shape axes. |
| He leans on another woman emotionally, no affair | P03 (TV interview names another woman as muse), P07 (retrospective centres another woman), P05 (husband's fixation), P09 (an assistant performs his intimacy, no affair) | The "other woman, no affair" device appears in 3–4 published books. |
| Boardroom learns whose idea everything was | P01–P07 (community-witnessed status correction), P12 (client credits her on a recorded call; partner names her on the record before the bonding committee), R-X1 (boardroom rival credits heroine), R-X3 (husband credits her on the record) | Public credit correction is the house resolution beat. Where a candidate *stages* it decides the risk: a documentary midpoint or a public-reckoning climax both reproduce P01–P07. |
| He begs forgiveness | P01–P07 (`husband_attempts_repair_and_initially_fails`), P14 (the apology is withheld, then allowed), P09 (index-card apology collapses) | Staging must avoid fail-then-succeed and the witness pattern. |
| Reconciliation | 12 of 14 published end in reconciliation or a marriage made real | Arithmetic, not reuse, but it consumes one of the 8 axes for every comparison. |

**Consequence:** every candidate starts at **2/8 raw** against P01–P07, P12, R-X1, R-X2 and R-X3 before any open axis is designed. Two more matches on open axes against any of those 8 rows produces a raw H1 FAIL.

---

## 2. Candidate Z1 (revision of rejected R-X1)

### 2.1 Pairwise core matches (raw n/8; open n/6)

| Row | 1 inc | 2 bind | 3 FID | 4 mid | 5 low | 6 climax | 7 repair | 8 res | raw | open |
|---|---|---|---|---|---|---|---|---|---|---|
| P01–P07 (each) | M | D | D | D | D | D | D | M | 2 | 0 |
| P08 | D | D | D | D | D | D | D | D | 0 | 0 |
| P09 | D | D | D | D | D | D | D | M | 1 | 0 |
| P10 | D | D | D | D | D | D | D | D | 0 | 0 |
| P11 | D | D | D | D | D | D | D | M | 1 | 0 |
| **P12** | M | D | D | D | **M (adv)** | D | D | M | **3** | 1 |
| P13 | D | D | D | D | D | D | D | D | 0 | 0 |
| P14 | D | D | D | D | D | D | D (secondary shape matches) | M | 1 | 0 |
| **R-X1** | M | **M** | **M** | **M** | D | **M** | **M** | M | **7** | **5** |
| R-X2 | M | D | D | D | D | D | D | D | 1 | 0 |
| R-X3 | M | D | D | D | D | D | D | M | 2 | 0 |

Detail pairs:
- **Z1 vs R-X1, 7/8** (6/8 even if the repair is scored D for its new staging rhythm):
  - (a) Bind: the supermajority veto, with the sale impossible without her (`supermajority_veto_and_crew`) = Z1's 75% veto. The lock-up is an addition, not a new mechanism.
  - (b) FID: she has the founding room craned out overnight at public cost (`heroine_removes_room_overnight`, `immediate_costly_physical_act_then_builds_alternative`) = Z1 Ch 1–3.
  - (c) Midpoint: the board learns the origin, then a cash cliff turns her veto against the workforce (`veto_becomes_weapon_against_crew_cash_cliff_revealed`) = Z1's midpoint. Only the *trigger* changed: viral product demand instead of a rival's testimony.
  - (d) Climax: the heroine puts her plan to a workforce hand vote at shift change (`heroine_asks_workforce_vote_on_her_plan`) = Z1's climax. His amendment is content inside the same mechanism.
  - (e) Repair: he accepts a consequence he could avoid by taking the blame in hostile rooms (`hero_accepts_consequences_in_hostile_rooms`) = Z1 telling the lender the crisis was his and pledging his shares first. The shape is identical; only the witness rhythm changed.
  - (f) Ally beat: the heroine allies with the rival on a plan = Z1's "ally turn". This is a supporting axis, but it is in the same beat position.
- **Z1 vs P12, 3/8.** (a) Axis 1 is public credit erasure before third parties (constant). (b) Lowest point, adversarial match: in P12 the hero announces at the all-hands an equity deal he negotiated without her and she is blindsided. In Z1 the heroine announces on live TV a no-sale decision she made without him, and her husband, the executive and the board are blindsided. The mechanism is the same (a unilateral decision about the shared company, announced publicly, blindsiding the partner) with the actor reversed. (c) Axis 8 is reconciliation (constant). No other axis matches: P12's bind is a loan guarantee plus indispensability, its FID is withholding work, its midpoint a rejected surprise fix, its climax private terms in the trailer, and its repair a co-negotiated equity agreement plus restraint.

### 2.2 Shape triple and H5

Z1's triple is **commission · accepting a consequence he could avoid · object at rest**.

| Row | inciting_kind | repair_shape | ending_class | triple repeats | climax+repair pair repeats |
|---|---|---|---|---|---|
| P01–P07 | (inferred) same | (inferred) different: public accountability + redistribution | (inferred) unknown | no (inferred) | no |
| P08 | not filed, differs (external blow) | different | not filed | no | no |
| P09 | different | different | different | no | no |
| P10 | different | different | different | no | no |
| P11 | different | different | different | no | no |
| P12 | different | different | different | no | no |
| P13 | different | different | different | no | no |
| P14 | different | different (secondary shape = Z1's primary: flag) | different | no | no |
| **R-X1** | **same** | **same** | **same** | **TRUE** | **TRUE** |
| R-X2 | same | different | different | no | no |
| R-X3 | same | different | different | no | no |

**H5 FAIL against R-X1 on two clauses:** the shape triple repeats, and the climax action plus repair mechanism repeat.

### 2.3 Climax staging (H8)

Z1's staging is: workplace_floor / workforce / no_evidence / vote / quiet_tally.

| Row | count /5 | fields | mechanism pair also matches |
|---|---|---|---|
| **R-X1** | **5** | venue, audience, evidence, authority, spectacle | **yes** |
| P14 | 1 | spectacle (quiet_tally) | no |
| P09, P10, P11, P12, P13 | 0 | (none) | no |
| R-X2, R-X3 | 0 | (none) | no |
| P01–P08 | not filed | (inferred) public-reckoning staging, so likely ≤1 | no |

**H8 FAIL against R-X1 on both clauses:** 5/5 staging, and the same climax and repair with ≥3 staging. This confirms the script's hard failure.

### 2.4 H2 (ordered macro-beats)

Against R-X1, the beats run founding room given away → room removed overnight → acquisition needs her yes → board learns origin and the cash cliff flips the veto → she allies with the rival on a plan. That is the **same 5-beat run in the same order** in Z1. **H2 FAIL** against R-X1. No published book shares a run of four.

### 2.5 Is Z1 a re-architecture or a recycled reject?

The script FAIL is against R-X1, so this reader checked which core axes actually **changed mechanism**:

| Axis | Changed? | Finding |
|---|---|---|
| 5 Lowest point | **YES: a new mechanism** | The hero's concealment relapse becomes the heroine's own unilateral public act, mirroring his fault. This is a real change, and new against 11/14 published rows. |
| 7 Repair | Staging rhythm only | It moves from "walks into hostile rooms, witnessed" to "announced in advance, done unwitnessed, taken on trust". The shape is unchanged. The rhythm is new against the shelf, but the mechanism (he takes the blame and the cost in a hostile room, here the lender) is the same. |
| 6 Climax | Content only | The hero now opposes part of her plan, which cures R-X1's hero-submission line. The mechanism and all 5 staging fields are unchanged. |
| 4 Midpoint | Trigger only | The cause becomes product-causal (viral video demand) instead of testimony. What flips and what it costs (the veto turns on the workers; cash cliff) are unchanged. |
| 2 Bind, 3 FID | No | Identical. |
| Supporting / surface | Changed | The dead-father legacy, family-meal ordeal and mugs are removed. These were R-X1's H7 reasons, not core axes. |

**Ruling: recycled reject.** Z1 cures every *H7 reason* R-X1 was rejected for (witness-pattern repair, hero-submission line, dead-father legacy, family meal, hero-relapse lowest point), but only **one core axis changed mechanism**. The spine is the same: bind, FID, midpoint function, climax and staging, repair shape, shape triple, and the 5-beat run. The script FAIL (6/7 serial shape, 5/5 staging) **is not overturned**. Fewer than the 4 axes needed have new mechanisms.

### 2.6 Remaining tests

- **H3 occupation swap (axes 1, 4, 6): survives_unchanged = false, so PASS.**
  - The midpoint does not survive a swap: demand for her original design exists only because a whole room can be lifted out and driven away undamaged.
  - The FID (crane removal) does not survive either.
  - The climax (a workforce vote on a pay deferral versus closing the second plant) partly survives in any company with a workforce, but its stakes come from the plant and the build.
  - Axis 1 survives only because it is the constant.
- **H4:** the nearest row is R-X1. Differences: lowest point (core), repair rhythm (core sub-feature, same shape), midpoint trigger (supporting), climax content (supporting), legacy and meal removed (surface). That is ≥3 core or supporting mechanisms, so H4 technically passes. It does not rescue H1, H2, H5 or H8.
- **H7 against the published shelf:** clean on the named items. Flag: the "both are guilty" mirror echoes the mutual-fault motif of P09, P11 and P14, but it sits at the lowest point and comes through an action, not a midpoint revelation. Recorded as a flag only.

### 2.7 Review fields

```yaml
candidate: Z1
recycled_reject_of: R-X1   # 7/8 raw (5/6 open), 5/5 staging, identical shape triple, 5-beat ordered run
one_beat_sheet_test:
  single_sheet_fits_all: false
  sheet_if_true: n/a
  sheet: "1 public handover of her founding room → 2 her veto means the sale cannot happen without her, and she cannot sell or leave → 3 she has the room craned out overnight; public humiliation and a censure follow → 4 the stunt's viral demand turns her veto into a trap that starves the orders, with 9 weeks of cash → 5 she makes a unilateral public decision and does to everyone what he did to her → 6 he announces his amends, then does them unseen; she chooses not to check → 7 at a workforce vote he dissents and she adopts his amendment; the tally is not unanimous → 8 reconciled; two desks inside the craned room"
  beats_that_break_it: "No published book fits on ≥4/8. R-X1 fits 6/8 (beats 1, 2, 3, 4, 7-generic, 8); beats 5 and 6 break it."
occupation_swap: {survives_unchanged: false, reasoning: "The midpoint and FID depend on the product being a craneable, transportable room. Swapping it removes the demand trap and the removal act."}
recognizability_line: "A founder has her own first room craned out of headquarters overnight, and the stunt's viral demand turns her veto into a noose around the workers she meant to protect."
house_template_hits: ["inciting: public erasure (constant, exempt)", "inciting_kind commission (constant)", "flag: mutual-guilt motif (P09, P11, P14 midpoints) relocated to the lowest point"]
verdict: FAIL
fail_conditions: [H1 vs R-X1 (7/8 raw; 5/6 open), H2 vs R-X1, H5 vs R-X1 (triple + climax/repair pair), H8 vs R-X1 (5/5 + mechanism pair)]
strongest_reasons:
  - "Only the lowest point changed mechanism; bind, FID, midpoint function, climax and staging, and repair shape are R-X1's."
  - "The script's 5/5 staging hard-fail cannot be overturned: every staging field is identical."
  - "Against the published shelf alone it is the cleanest candidate in the batch: max 3/8 (P12), H3 pass, a new repair rhythm."
```

---

## 3. Candidate Z2

### 3.1 Pairwise core matches

| Row | 1 inc | 2 bind | 3 FID | 4 mid | 5 low | 6 climax | 7 repair | 8 res | raw | open |
|---|---|---|---|---|---|---|---|---|---|---|
| P01–P07 (each) | M | D | D | D | D | D | D (P05 flag) | M | 2 | 0 |
| P08 | D | D | D | D | D | D | D | D | 0 | 0 |
| P09 | D | D | D | **M** | D | D | D | M | 2 | 1 |
| P10 | D | D | D | D | D | D | D | D | 0 | 0 |
| P11 | D | D | D | **M** | D | D (partial) | D | M | 2 | 1 |
| **P12** | M | D | D | D (reframe, different object) | D | D (staging 3/5) | **M** | M | **3** | 1 |
| P13 | D | D | D | D | D | D | D | D | 0 | 0 |
| P14 | D | D | D | **M** | D | D | D | M | 2 | 1 |
| R-X1 | M | D | D | D | D | D | D | M | 2 | 0 |
| **R-X2** | M | **M** | **M** | D | D | **M (adv)** | D | D | **4** | 3 |
| R-X3 | M | D | D | D | D | D | D | M | 2 | 0 |

Detail pairs:
- **Z2 vs R-X2, 4/8.**
  - (a) Bind: a founders'-agreement clause, once triggered, runs a fixed clock during which neither founder may exit. R-X2 has a 30-day buy-sell; Z2 has a 45-day deadlock arbitration where neither may resign or sell.
  - (b) FID: early on, the heroine triggers that clause and stakes her own shares (R-X2 `early_legal_trigger`; Z2 Ch 3, where she is "dragged along" if she loses).
  - (c) Climax, adversarial match: at the final legal session the heroine replaces the contractual or adjudicated outcome with a privately negotiated one (R-X2 rewrites the deal at the closing table; Z2 withdraws and they settle it themselves).
  - (d) Axis 1 is the constant.
  - R-X2's contract rewrite has also **migrated into Z2's repair** (rewriting the founders' agreement), which axis-by-axis scoring does not count. Below H1, but the front half of R-X2 is reproduced.
- **Z2 vs P12, 3/8.**
  - (a) Axis 1 is the constant.
  - (b) Repair: the couple co-rewrites the company's ownership or governance document and changes the structure (P12 redlines the equity agreement, strikes his tiebreaker and renames the company; Z2 co-rewrites the founders' agreement and moves HQ). The shapes are labelled differently (relinquishing control vs changing a structure), but the mechanism is the same.
  - (c) Axis 8 is the constant.
  - The climax is D: P12 has the heroine decline the exit offer and dictate terms, while Z2 has a mutual withdrawal from adjudication after she has been losing. They share 3/5 staging, however.
- **Z2 vs P09, P11 and P14 on the midpoint.** The midpoint shape is the same: a revelation makes the problem two-sided or mutual. In P09 the heroine sees her own over-functioning and the repair becomes two-sided. In P11 Gid names the same pattern in both of them. In P14 both admit relief at the absence and the harm is reframed. In Z2 the past timeline shows she broke their rule first, and the problem is reframed as mutual.

### 3.2 Shape triple and H5

Z2's triple is **commission · changing a structure · document or record**.

| Row | inciting_kind | repair_shape | ending_class | triple | pair |
|---|---|---|---|---|---|
| P01–P07 | (inferred) same | different | (inferred) unknown | no | no |
| P09–P14 | different | different (P12: different by label, same mechanism) | different | no | no |
| R-X1 | same | different | different | no | no |
| R-X2 | same | different (restitution) | different (spoken line) | no | no |
| R-X3 | same | different | different | no | no |

**H5: not triggered.** Single-axis flags: inciting_kind = commission (the constant). The ending image of two names on one founding document is *thematically* P12's shared-name company sign (P12 is classed act-in-motion, so the class differs). This is a flag.

### 3.3 Climax staging (H8)

Z2's staging is: road_or_weather / the_two_of_them / no_evidence / heroines_own_choice / private_line.

| Row | count | fields | mechanism pair |
|---|---|---|---|
| **P12** | **3** | audience, authority, spectacle | no (the climax is D; the repair is M) |
| P09 | 2 | authority, spectacle | no |
| P11 | 2 | authority, spectacle | no |
| R-X1 | 1 | evidence | no |
| R-X2 | 1 | spectacle | no (the climax is M (adv); the repair is D) |
| P10, P13, P14, R-X3 | 0 | (none) | no |
| P01–P08 | not filed | (inferred) public staging, so ≤1 | no |

**H8: not triggered**, but this is the closest call in the batch. If an architect changes either the climax into "she dictates terms" or adds hero restraint to the repair, Z2 hits clause 2 against P12. The **heroine's-own-choice / private-line** pair recurs in P09, P11 and P12.

### 3.4 Other conditions

- **H2:** the shared run with R-X2 is founding room given away → heroine triggers the clause, which is 2 beats. No run of 4 with any row, so H2 passes.
- **H3 occupation swap: survives_unchanged = true, so FAIL.**
  - Axis 1 is the constant and survives any swap.
  - The **midpoint** (years ago she alone refused an offer that would have saved his mother's house) survives a swap to any co-founded company.
  - The **climax** (a highway closure strands them on the way to arbitration; she proposes withdrawal) survives any profession and setting.
  - The product touches only the repair (HQ moved into the factory) and the shared-fact backdrop, so the profession is colour.
- **H4:** the nearest shelf row is P12. Bind, FID, midpoint, lowest point and climax all differ in mechanism, so H4 passes.
- **H7: FAIL on midpoint shape.** The "reframed as mutual / she broke it first" midpoint is the house midpoint of the last published block: P09, P11 and P14, with P12 a reframe as well. That is 4 of the 6 most recent published rows.
- **Other house-template flags:**
  - The hero relocates to her ground (HQ into the factory): P01 "husband takes leave and moves", R-X1 "hero lives in the room in the factory yard".
  - Family-home stakes in the backstory (his mother's house) sit near the family-asset motif of P01–P07 and P11.
  - The climax is "heroine sets terms"-adjacent (her proposal, then co-written terms): P09, P11, P12, P13, P14.
  - The repair is a document-signing beat (P12 lawyer's redline; R-X2 closing table).
  - The road_or_weather climax is the exact venue the stress-bundle evidence shows **drifting into a packed public meeting** in drafting.
- **Constant gaps:** Z2's card does not say where "the boardroom learns whose idea" or "he begs" happen. They are unstaged, so the H7 or H8 risk cannot be checked until they are placed.

```yaml
candidate: Z2
recycled_reject_of: none by H1. It partially reproduces R-X2's front half: the clause-triggered timed bind and the early legal trigger, 4/8 adversarial.
one_beat_sheet_test:
  single_sheet_fits_all: false
  sheet: "1 public handover → 2 the deadlock clause locks both founders for 45 days → 3 she triggers arbitration and stakes her shares → 4 the past timeline shows she broke their rule first, so the fault is mutual → 5 his truthful testimony about her old refusal sinks her interim → 6 a road closure strands them overnight; she proposes withdrawal and they settle it themselves → 7 they co-rewrite the founders' agreement and he moves HQ into her factory → 8 reconciled; the clause in two handwritings"
  beats_that_break_it: "It fits P12 on 3/8 (beats 1, 7, 8), R-X2 on 3–4/8 and P11 on 2–3/8. No row fits ≥7."
occupation_swap: {survives_unchanged: true, reasoning: "The midpoint (the refused offer and his mother's house) and the climax (the road closure and the settlement) need no product. Only the repair's HQ move touches the business."}
recognizability_line: "Two co-founders in a 45-day deadlock arbitration are stranded on a closed highway on the way to the final session, the night after his honest testimony sank her, and decide to settle it themselves."   # it needs help: the stranding is generic
house_template_hits: ["midpoint: mutual-fault reframe (P09, P11, P14; P12 reframe)", "climax spectacle: heroine's own choice / private line (P09, P11, P12)", "hero relocates to her ground (P01, R-X1)", "contract-rewrite repair (P12, R-X2)", "road_or_weather drift risk (stress-bundle evidence)"]
verdict: FAIL
fail_conditions: [H3, H7 (midpoint shape)]
strongest_reasons:
  - "The profession is colour: the midpoint and climax survive the occupation swap unchanged."
  - "The midpoint is the house's recent midpoint shape (a mutual-fault reframe in 4 of the last 6 published)."
  - "It has the lowest maximum overlap over the whole comparison set (4/8 vs R-X2; 3/8 vs P12), but it sits in the founders'-contract family R-X2 was rejected out of, with 3/5 staging against P12."
```

---

## 4. Candidate Z3

### 4.1 Pairwise core matches

| Row | 1 inc | 2 bind | 3 FID | 4 mid | 5 low | 6 climax | 7 repair | 8 res | raw | open |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | M | D | D | D (partial) | M | D | M | M | 4 | 2 |
| P02 | M | D | D | D (partial) | M | D | M | M | 4 | 2 |
| **P03** | M | D | D | D (partial) | **M** | **M** | **M** | M | **5** | 3 |
| **P04** | M | D | D | D (partial) | **M** | **M** | **M** | M | **5** | 3 |
| P05 | M | D | D | D (partial) | M | D | M | M | 4 | 2 |
| **P06** | M | D | D | D (partial) | **M** | **M** | **M** | M | **5** | 3 |
| **P07** | M | D | D | D (partial) | **M** | **M** | **M** | M | **5** | 3 |
| P08 | D | D | D | D | D | D | D | D | 0 | 0 |
| P09 | D | D | D | D | M | D | D | M | 2 | 1 |
| P10 | D | D | D | D | D | M | D | D | 1 | 1 |
| P11 | D | D | D | D | M | D | D | M | 2 | 1 |
| P12 | M | D | D | D | M | D | D | M | 3 | 1 |
| P13 | D | D | D | D | D | D | D | D | 0 | 0 |
| P14 | D | D | D | D | M | D | D | M | 2 | 1 |
| R-X1 | M | D | D (partial: a physical act on the office) | D | D | **M** | D | M | 3 | 1 |
| R-X2 | M | D | D | D | D | D | D | D | 1 | 0 |
| **R-X3** | M | D | D | **M (adv)** | D | **M** | **M** | M | **5 (adv) / 4 firm** | 3 |

Detail pairs:
- **Z3 vs P04 (also P03, P06, P07), 5/8.**
  - (a) Lowest point: under pressure the husband repeats his core erasure. P01–P07 have `husband_repeats_core_avoidance_under_pressure`; in Z3, after the failed launch, he blames the executive to the board to save face, "doing to her what he did to his wife".
  - (b) Climax: the heroine's public presentation of her own case before the deciding body turns the room, with the husband's public confession attached. P04 has a counter-film screening plus his confession, P03 a public performance plus his confession, P07 an art show plus a public provenance correction, P06 a reporting payoff plus public policy. Z3 has the two women presenting the alternative to the board, and his confession to the board and staff.
  - (c) Repair: public accountability before the community or institution. P01–P07 have `public_accountability…`, `community_witnessed_status_correction`; Z3 has a public confession to the board and staff.
  - (d) Axes 1 and 8 are the constants.
  - Midpoint, partial: "the women compare notes and expose his double story" is an evidence-assembly reveal, close to the documentary midpoint of P01–P07. It is scored D.
- **Z3 vs R-X3, 4 firm / 5 adversarial.**
  - (a) Climax: a heroine-led documentary case before an institution, documents read aloud, the room turns (R-X3 testimony with origin records).
  - (b) Repair: the husband sets the record straight about her before the institution (R-X3 withdraws the suit and credits her on the record).
  - (c) Midpoint, adversarial match: she discovers the husband or company is deceiving her about the company's future or sale (R-X3 "learns she is acquisition bait").
  - (d) Axes 1 and 8 are the constants.

### 4.2 Shape triple and H5

Z3's triple is **commission · public confession · spoken line**.

| Row | inciting_kind | repair_shape | ending_class | triple | pair |
|---|---|---|---|---|---|
| P03, P04, P06, P07 | (inferred) same | (inferred) same: public accountability | (inferred) unknown | (inferred) 2 of 3 | **TRUE** |
| P09–P14 | different | different | different | no | no |
| R-X1 | same | different | different | no | no |
| R-X2 | same | different | **same** | no (2 of 3) | no |
| R-X3 | same | different by label (same mechanism) | different | no | **TRUE (adv)** |

**H5 FAIL:** the climax action and repair mechanism both repeat P03 and P04 (and P06 and P07). The third clause is also met against P03 and P04 *(inferred)*: two of three shape axes repeat, together with the pair.

### 4.3 Climax staging (H8)

Z3's staging is: public_civic_meeting (board) / institution / documents_produced_aloud / vote / room_turns_audibly.

| Row | count | fields | mechanism pair |
|---|---|---|---|
| **R-X3** | **3** | audience, evidence, spectacle | **yes (adv): climax M + repair M** |
| P10 | 3 | audience (board and press), evidence, spectacle | no (repair D) |
| P13 | 2 | venue, spectacle | no |
| R-X1 | 1 | authority (vote) | no |
| P09, P11, P12, P14, R-X2 | 0–1 | (none, or one) | no |
| P01–P07 | not filed | (inferred) public room, community or institution, room turns: likely 3–4 against P03, P04, P07 | (inferred) yes |

**H8 FAIL against R-X3 (clause 2).** It is the same scene: an institutional hearing room, documents read aloud, the room turning, and the husband putting her credit on the record. It is probable against P03, P04 and P07 once their staging is back-filled.

### 4.4 Other conditions

- **H2:** P01–P07 run erasure → exit → revive → paper trail. Z3 runs erasure → occupation → compare notes. There is no 4-beat ordered run, so H2 passes.
- **H3 occupation swap: survives_unchanged = true, so FAIL.** A shared office, comparing notes, a product launch failing, and a board presentation and vote all survive a swap to any company and setting. The craneable product plays no causal role.
- **H4:** the nearest row is P04. Differences: bind (forced proximity vs exit; core), FID (moving in vs leaving; core), executive-as-ally (supporting), three narrators (form). That is ≥3, so H4 technically passes, but H1 and H5 fail regardless.
- **H7: FAIL**, on four house-template items outside the declared hook:
  - Hero-relapse lowest point (11/14 published).
  - Public-reckoning climax (P01–P07, P10, P13).
  - Witness-pattern repair before the board and staff (P01–P07, P10, P12, P13, P14).
  - Public-confession repair (P03, P04, P05).
- **H1 robustness:** raw 5/8 is a FAIL. With the constants exempt it is 3/6, which is not an H1 FAIL. **The verdict does not depend on the constants:** H5, H7, H8 and H3 fail independently.
- **Batch rule:** Z3 differs from Z1 on only 4 of 8 axes (see §5).

```yaml
candidate: Z3
recycled_reject_of: R-X3 (partial, back half: deception-discovery midpoint, institutional documents climax, on-the-record credit repair; 4/8 firm, 5/8 adversarial; H8 clause 2)
one_beat_sheet_test:
  single_sheet_fits_all: false
  sheet: "1 public handover → 2 she refuses to cede and shares the room with the other woman under a launch deadline → 3 she carries her desk in before the staff → 4 the two women compare notes and expose his double story → 5 under pressure he repeats his erasure on the other woman → 6 the women jointly present the alternative to the board; vote; the room turns → 7 he confesses publicly to the board and staff → 8 reconciled; a spoken line"
  beats_that_break_it: "It fits P03, P04 and P07 at 6/8; only beats 2 and 3 (stay and occupy vs exit to a family asset) break it, which leaves one beat of margin. It fits R-X3 at 5/8."
occupation_swap: {survives_unchanged: true, reasoning: "None of the inciting event, midpoint or climax uses the product. A shared desk, comparing notes and a board vote fit any company."}
recognizability_line: "The wife moves her desk into the office he gave the other woman, and sharing it the two women discover he has promised each of them a different future."   # recognizable, but as a genre trope
house_template_hits: ["hero relapse at the lowest point (11/14)", "public-reckoning climax (P01–P07, P10, P13)", "witness-pattern repair", "public-confession repair (P03, P04, P05)", "documentary-adjacent midpoint (P01–P07)"]
verdict: FAIL
fail_conditions: [H1 raw (5/8 vs P03, P04, P06, P07), H3, H5 (climax+repair pair vs P03/P04), H7, H8 (vs R-X3, clause 2)]
strongest_reasons:
  - "It is the grovel-lane back half (relapse → public presentation → public confession) relocated into a shared office."
  - "The climax staging is the R-X3 scene again."
  - "The profession is colour."
```

---

## 5. Candidates against each other (must differ on ≥5 of 8)

| Pair | Same axes | Differ | Rule |
|---|---|---|---|
| Z1 vs Z2 | 1, 8 | 6 | OK |
| **Z1 vs Z3** | 1; 3 (adv: an early physical act on the office itself, before witnesses; one removes it, the other occupies it); **6** (the heroine's alternative to the sale is put to a vote); 8 | **4** (5 if the FID is scored D) | **Batch-construction defect.** Both climaxes are "her alternative plan, decided by a vote". |
| Z2 vs Z3 | 1, 8 | 6 | OK |

The three triples differ. Every candidate shares inciting_kind = commission, which is forced by the constant.

## 6. House-template answer for the batch plus the comparison set (H7, CB-10)

`found: true`. Recurring items, with the books they recur in:

1. **Inciting kind:** public erasure, a commission (P01–P07, P12, R-X1–3, and all of Z1–Z3). This is the declared constant and is exempt.
2. **Lowest point = hero relapse into the core fault:** P01–P07, P09, P11, P12, P14 (11/14). Z3 falls in. Z1 and Z2 avoid it.
3. **Midpoint shapes:**
   - Documentary evidence makes the harm a claim: P01–P07. Z3 is adjacent.
   - Mutual-fault reframe: P09, P11, P14, plus P12's reframe. **Z2 falls in.**
   - Z1's motif sits at its lowest point and is a flag only.
4. **Repair staging rhythms:**
   - Witness pattern: P01–P07, P10, P12, P13, P14. Z3 falls in.
   - Secret-then-discovered: P09 (rides learned of by accident), P11 ("She noticed"), P13 (the mixer and the note).
   - Fail-then-succeed: P01–P07, P09, P12, P14.
   - **Z1's announced → unwitnessed → trusted, never discovered rhythm is new**, but it is R-X1's repair shape.
5. **Climax staging families:**
   - Public room / institution / documents / the room turns: P10, P13, R-X3, and (inferred) P01–P07. Z3 falls in.
   - Private / the two of them / heroine's own choice / private line: P09, P11, P12. Z2 falls in.
6. **Heroine sets terms:** P09, P11, P12, P13, P14. Z2 is adjacent.
7. **Relocation to a family asset, or the hero moving to her ground:** P01–P07, P11, P14, R-X1. Z2 flags this through the HQ move.
8. **Dead or dying-parent legacy:** P09, P11, P13. Z2's backstory with his mother's house is adjacent. Z1 removed its legacy object.
9. **Last-image classes:** act in motion (P09, P12, P13, P14) and callback to the opening (P10, P11). Z1, Z2 and Z3 each avoid both. Z1's object-at-rest is R-X1's class; Z3's spoken line is R-X2's class.
10. **Hero submission:** P11, P12, P14, and R-X1's rejection. Z1 explicitly breaks it (the hero dissents and is adopted as an equal).

`repeat_reader_review_draft` (written because a repeat reader could write it of Z3): "Another one where he erases her in public, she digs in and builds her case, he caves under pressure and throws someone else under the bus, and then there's the big meeting where she presents, the room gasps, and he stands up and confesses in front of everybody. Swap the factory for the recording studio from her earlier book and it's the same scenes. The new wrinkle, the wife and the 'work wife' sharing an office, was the best idea in the book and it was gone by the halfway mark."

## 7. Selection

| Candidate | Max core overlap, published shelf only | Max over the whole comparison set | Verdict |
|---|---|---|---|
| Z1 | 3/8 (P12) | **7/8 (R-X1)**, recycled reject | FAIL (H1, H2, H5, H8 vs R-X1) |
| Z2 | 3/8 (P12; staging 3/5) | 4/8 (R-X2, adversarial) | FAIL (H3, H7) |
| Z3 | 5/8 (P03, P04, P06, P07) | 5/8 | FAIL (H1 raw, H3, H5, H7, H8) |

- **Gate selection: NONE.** Every candidate fails, so the rule calls for a **re-concept**.
- By the arithmetic rule on shelf books alone, Z1 and Z2 tie at 3/8 against P12. The recognizability tie-break favours **Z1**, whose line needs no help, but Z1's maximum over the whole comparison set is 7/8 against its own reject. Over the whole pool, the lowest maximum is **Z2** (4/8 vs R-X2; 3/8 vs P12).
- **Owner decision point (not a gate ruling).** R-X1 was rejected for H7 only, and Z1 cures every named H7 item. The gate as written still scores a revised reject against its parent on core axes, and Z1 keeps 6–7/8 of them. Only the owner can rule whether a reject cured of its stated reasons is re-scored against the shelf only. That would require a dated `declared_constants`-level series decision. This reader does not recommend it, because a reader of R-X1's file would recognise Z1 on the bind, the crane stunt, the cash-cliff veto flip and the shift-change hand vote.

**Re-concept guidance.** Z1 contains four mechanisms that test clean against all 14 published rows:
- a product-causal midpoint (demand from a craneable room traps her veto);
- the heroine's mirrored unilateral public announcement as the lowest point;
- an announced, unwitnessed repair taken on trust;
- the hero's costly independent dissent at the climax, adopted as an equal.

Re-home them on a new spine that differs from R-X1. That means a new mechanism on at least 3 of {bind, FID, climax, repair} and a staging set that shares ≤2 fields with R-X1. The repair shape or the ending class must also change, so the triple is no longer R-X1's. To rescue Z2, its midpoint and climax must become product-causal (H3), and the mutual-fault reframe must leave the midpoint (H7).

**Nearest prior for whatever goes forward:** P12, the nearest published row for both surviving lines (3/8). Then R-X1 (Z1 lineage) or R-X2 (Z2 lineage).

**Weak spots the architecture must watch:**
1. The hook already spends 2/8 against P01–P07, P12 and all rejects. **Two more open-axis matches against any of those 8 rows is a raw H1 FAIL.**
2. "The boardroom learns whose idea" must not become a documentary midpoint (P01–P07) or a public credit-correction climax (P01–P07, P12, R-X3). Z1's one-line diligence answer is the safe form.
3. "He begs" must not be staged as fail-then-succeed or before witnesses.
4. Keep the lowest point off hero relapse (11/14).
5. Keep the midpoint off the mutual-fault reframe (P09, P11, P12, P14).
6. Avoid both climax staging families:
   - private / the two of them / heroine's own choice / private line (P09, P11, P12);
   - public room / documents / the room turns (P10, P13, R-X3; inferred P01–P07).
7. Avoid co-rewriting the ownership document as the repair (P12, R-X2), and the hero relocating to her ground (P01, R-X1).
8. **Z1-lineage risk:** its lowest point is P12's lowest point with the actor reversed (a unilateral company decision announced publicly). Keep it from reading as "P12 flipped".
9. **Z2-lineage risk:** a road_or_weather climax is the venue the stress bundle drifted from into a packed meeting. Re-check it at Story Bible Lock (STRUCTURAL_DRIFT_REPORT).
10. inciting_kind is locked to commission, so the repair shape and ending class must carry all triple variation.
11. Back-fill staging and shape fields for P01–P08 before any PASS is treated as clean. H5 and H8 against them are inferred in this review.
12. H6 (voice convergence; the 1,000-word blind voice test) is unchecked at concept stage. Run series_diff.py at 25%, 50% and 100% of draft.

```yaml
voice_signature: {convergence_flags: [], house_habits: [], per_pov_coverage: {}}   # N/A at concept stage (no text)
blind_voice_test: {run: false}   # required later if voice tags or series_diff flag it
batch_verdict: FAIL (re-concept)
```
