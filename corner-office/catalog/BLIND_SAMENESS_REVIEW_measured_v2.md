# BLIND_SAMENESS_REVIEW: Continuity Audit re-run (measured manuscript, v2)

Gate: Catalog Novelty Gate, measured row (fiction pipeline v5.0.2). This is a re-run, so no concept PASS carries over.
Inputs used: `catalog/BLIND_MEASURED_STRIPPED.md` (candidate), `catalog/CATALOG_STRIPPED_v2.json` (P01–P14 + R-B, R-C, R-Z2, R-Z3), `catalog/triage_manuscript.md`, `qc/series_diff_final.md`. The reviewer saw no architecture, no earlier review and no unstripped catalog.

```yaml
BLIND_SAMENESS_REVIEW:
  candidate: E2-M   # finished manuscript, measured fingerprint, surface-stripped
  comparison_set: [P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12, P13, P14, R-B, R-C, R-Z2, R-Z3]
  stripped: true
  reviewer: independent-subagent-blind-4
  reject_pool_checked: true      # R-B, R-C, R-Z2, R-Z3 scored on every axis below
  recycled_reject_of: none       # nearest reject R-Z2 at 3/8; its reject reasons (mutual-fault midpoint, job-agnostic climax) are absent here
  mechanical_triage: {tool: catalog_similarity 1.1.0, band: AMBER, hard_failures: none,
                      nearest: [R-Z2 0.216, R-C 0.191, R-Z3 0.185],
                      amber_cause: "short cross-lane set (3 of 5); 8 rows (P01–P08) lack staging fields; 4 reject rows compared but not counted toward coverage"}
  verdict: PASS
```

## 1. Core-axis counts, scored by function (H1)

Candidate axes as read from the measured row:
1. **Inciting.** The husband publicly gives her founding room to another woman and says she barely uses it. This is a commission, and it is the declared constant.
2. **Bind.** Her equity is a veto over a pending sale, and a lock-up stops her selling. She can't exit, and the sale can't close without her.
3. **First irreversible decision.** Overnight she has the room lifted out of the building and broadcasts it herself. The visible cost is censure, a fine, a buyer risk-flag and his humiliation.
4. **Midpoint.** In the boardroom, the demand her stunt created is locked behind her own founding rule. His one-line credit to her and her own on-record list come next. Then the cash cliff and his secret share pledge surface, and her veto now starves her own demand.
5. **Lowest point.** It is caused by her own unilateral public act (announcing no sale, telling no one). The buyer walks, the lender accelerates and the ally quits.
6. **Climax.** It is heroine-caused. She puts a plan to a workforce vote. He dissents and offers to close his own project. She adopts his offer, writes it in and calls the vote, which passes with open dissent.
7. **Repair.** Its shape is accepting a consequence he could avoid. He announces each act beforehand, does it unwatched, and she never verifies. He ends the outside intimacy himself, signs a personal guarantee alone, apologises once privately, and proposes closing his own project.
8. **Resolution.** Full reconciliation in the same week through a resumed daily ritual. There is no epilogue and no time jump, and the last image is an object at rest.

"Strict" counts a match only when the mechanism is the same. "Ceiling" also counts every partial, meaning an echo of the same function where the mechanism differs. **H1 needs 5. No row reaches 5 even at ceiling.**

| Row | Strict | Matching axes (strict) | Partials | Ceiling |
|---|---:|---|---|---:|
| P01 | 1 | 1 | 4 (credit put on the record), 7 (one public act + risk moved off her) | 3 |
| P02 | 1 | 1 | 4, 7 | 3 |
| P03 | 1 | 1 | 4, 7 | 3 |
| P04 | 1 | 1 | 4, 7 | 3 |
| **P05** | **1** | 1 | 4, 6 (public room, equity moved, husband's costly public admission), 7 | **4** |
| P06 | 1 | 1 | 4, 7 | 3 |
| P07 | 1 | 1 | 4, 7 | 3 |
| P08 | 0 | none | none | 0 |
| P09 | 1 | 8 (full reconciliation, no epilogue) | 7 (self-performed changed acts) | 2 |
| P10 | 0 | none | 7 (taking real loss for her) | 1 |
| P11 | 0 | none | 6 (his offered sacrifice is ruled on by her; there she refuses it, here she adopts it) | 1 |
| P12 | 0 | none | 1 (public erasure of her work, but by omission and by a third party), 2 (financially tied to the company), 3 (costly self-assertion at work) | 3 |
| P13 | 0 | none | 7 (private acts, then public backing) | 1 |
| P14 | 0 | none | 7 (his secondary shape is the same) | 1 |
| R-B | 2 | 1, 4 (midpoint turns it into a money race she must fund) | 2 (contractual ownership clock) | 3 |
| R-C | 1 | 1 | none | 1 |
| **R-Z2** | **3** | 1, 2 (ownership deadlock or veto over a company sale), 8 (no epilogue, settlement-type close) | 7 (a contract structure) | **4** |
| R-Z3 | 2 | 1, 3 (immediate physical repossession of the room) | 6 (vote decides) | 3 |

Axis-1 matches with P01–P07 and the four rejects are the declared constant (public erasure by commission). They count under H1 but not under H7.

### Detail pairs (≥3 at strict or ceiling)

- **R-Z2 (3 strict / 4 ceiling): the nearest row overall.**
  - Shared: the constant inciting; a bind built on an ownership veto over a sale (R-Z2's goal "stop forced sale" echoes the candidate's veto); a no-epilogue close.
  - Different: the first decision (public physical stunt here, formal legal trigger there); the midpoint (his concealed pledge and her trap here, a past-timeline reveal that she broke the rule first there); the lowest point (her own public act here, his truthful testimony there); the climax (workforce vote on the floor here, private settlement on a stranded road there); the repair shape (accepting a consequence here, changing a structure there); the ending class (object here, document there).
  - Form differs too: dual first-person present, opening in medias res, versus single first-person past with dual timeline.
  - Not a recycled reject: the two things R-Z2 was rejected for (a mutual-fault midpoint and a climax that works in any job) are both absent.
- **P05 (1 strict / 4 ceiling): the nearest published book.**
  - Shared: the constant inciting. The partials are an on-record credit claim (axis 4); a public room where equity moves and the husband makes a costly public admission (axis 6); and one public accountability act within the repair (axis 7).
  - Different: the bind (no exit possible here, exit to a hometown asset there); the first decision (stunt versus exit); the lowest point (her act versus his repeated avoidance); the climax mechanism (a vote on an operating plan that adopts his plant closure, versus a microphone confession transferring equity to her); the repair rhythm (unwatched and unverified versus community-witnessed); the resolution (same week, no epilogue, versus a months-later thriving epilogue).
  - The strongest differences: her equity moves to the crew, not from him to her, and authorship is not the climax's question because it was settled at the midpoint in one line.
- **P01–P04, P06, P07 (1 strict / 3 ceiling).** Same analysis as P05, without the axis-6 echo.
- **P12 (0 strict / 3 ceiling): the nearest by supporting fields.** It shares the company-finance engine, a personal guarantee as an instrument (she signs one in P12; he signs one here as repair), a husband's secret unilateral equity transaction surfacing at a company meeting (P12 at the rupture, here at the midpoint), and her name on the company. Core mechanisms differ on all 8. The secret-equity-deal-surfaces echo is the one P12 detail a repeat reader could notice. It is recorded here as a pairwise supporting overlap, not a house item, because it occurs in only one prior book.
- **R-B (2 strict / 3 ceiling).** Shared: the constant, and a midpoint that turns into a money race she must fund. Different: no buy-sell trigger; her own act causes the lowest point, where R-B's is his exit-with-confidante; climax is a vote rather than a closing-table rewrite; repair is accepting a consequence rather than restitution; the ending is an object rather than a spoken line.
- **R-Z3 (2 strict / 3 ceiling).** Shared: the constant, and immediate repossession of the room. Different: the other woman is a short-lived ally who resigns for her own reasons, with no forced proximity and no joint presentation; there is no public confession as repair, and the staging differs (see §3).

## 2. Shape triple and H5

Candidate triple: **commission · accepting a consequence he could avoid · object at rest.**

| Row | inciting_kind | repair_shape | ending_image_class | triple repeats | climax+repair pair repeats |
|---|---|---|---|---|---|
| P01–P07 | not filed (by function, commission = the constant) | not filed (public accountability + redistribution: closest to public confession or changing a structure) | not filed | false (repair shape cannot match) | false |
| P08 | not filed (external blow by function) | not filed (relinquishing power) | not filed | false | false |
| P09 | different (discovery) | different (sustained presence) | different (act in motion) | false | false |
| P10 | different (external blow) | different (risking loss) | different (callback) | false | false |
| P11 | different (external blow) | different (sustained presence) | different (callback) | false | false |
| P12 | different (omission) | different (relinquishing) | different (act in motion) | false | false |
| P13 | different (external blow) | different (sustained presence) | different (act in motion) | false | false |
| P14 | different (betrayal) | different (primary is being taught by her; **secondary = same**) | different (act in motion) | false | false |
| R-B | **same** | different (restitution) | different (spoken line) | false | false |
| R-C | **same** | different (letting her be right) | different (third-party gesture) | false | false |
| R-Z2 | **same** | different (changing a structure) | different (document) | false | false |
| R-Z3 | **same** | different (public confession) | different (spoken line) | false | false |

- **H5: clear.** No row repeats the triple. No row shares two shape values plus the climax+repair pair. No row repeats both the climax action and the repair mechanism.
- **The verdict holds whatever P01–P08 filed.** Their filed repair mechanism (community-witnessed public accountability) cannot be "accepting a consequence he could avoid," so the triple cannot repeat for them.
- **Single-value flags, none of which fails on its own:**
  - Commission recurs in all four rejects and, by function, in P01–P07. This is the declared constant.
  - The repair shape matches P14's secondary shape.
  - The ending class could be read as a weak callback, since the chair stands in the room the book opens on. Even under that reading no row repeats the triple: P10 and P11 share only the callback value.
- **Previous three published entries (P12, P13, P14).** The candidate differs from all three on every primary shape axis.

## 3. Climax staging and H8

Candidate staging: **workplace floor · workforce · no evidence · a vote · quiet tally.**

| Row | Matching fields | n/5 | Mechanism pair also matches |
|---|---|---:|---|
| P09 | none | 0 | false |
| P10 | none | 0 | false |
| P11 | none | 0 | false |
| P12 | none (private room, the two of them, confession, her choice, private line) | 0 | false |
| P13 | none | 0 | false |
| P14 | spectacle (quiet tally) | 1 | false |
| R-B | none | 0 | false |
| R-C | none | 0 | false |
| R-Z2 | evidence (no evidence) | 1 | false |
| R-Z3 | authority (vote); venue (civic meeting) and audience (institution/board) differ | 1 | false |
| P01–P08 | not filed. Inferred from climax and resolution tags: community-witnessed stage, screening or microphone; documents or performance; public opinion or official decision; room turns audibly | 0 inferred | false |

**H8: clear.** The maximum is 1 of 5. The P01–P08 staging fields still need back-filling, as triage notes.

## 4. H2: macro-beat order

Candidate run: room given away → physical repossession and broadcast → demand created and trapped → board-room exposure of his pledge and the cash cliff → independent plan with the ally → her unilateral announcement collapses the deal → his announced, unwatched consequence acts → workforce vote adopting his sacrifice → same-week ritual resumed.

- P01–P07 share "erasure … public accountability … reconciliation," but not as four consecutive beats. The candidate has no exit, no revival of a hometown asset and no failed first repair.
- The best run against R-B is 2 (room given → heroine acts).
- Against R-Z3 it is 2.

**H2: clear.**

## 5. Occupation swap (H3)

Swap the product (rooms factory-built and lifted into place, plus a multi-plant crew) for a non-manufacturing firm such as a law or ad agency. Taking the axes in turn:

- **Axis 1 (inciting).** It survives the swap. That is expected, because it is the declared constant.
- **Axis 3 (first decision).** It does not survive. Lifting the room out overnight needs a modular room.
- **Axis 4 (midpoint).** It does not survive. Deposits are held in escrow "until steel is cut" under her founding rule, and her veto starves build-to-order demand. Both need made-to-order manufacturing with pre-orders.
- **Axis 6 (climax).** It does not survive. A shift-change vote on Saturday shifts versus closing his second plant needs a multi-site production crew.

Residual: another manufacturer with pre-orders would keep the mechanism. That is the profession acting as cause, not colour. **`survives_unchanged: false`. H3: clear.**

## 6. H4: nearest published book

Nearest published book: **P05, 1/8 strict, 4/8 at ceiling.** Differences:

| # | Difference | Label |
|---|---|---|
| 1 | Bind: she cannot leave, and holds a veto; P05's heroine exits | core |
| 2 | First decision: public physical stunt versus exit | core |
| 3 | Midpoint: her stunt's demand is trapped by her own rule, and his concealed pledge surfaces | core |
| 4 | Lowest point caused by her own unilateral public act | core |
| 5 | Climax: a vote on an operating plan that adopts his self-sacrifice; authorship is not at stake | core |
| 6 | Repair rhythm: announced beforehand, unwatched, unverified, self-originated | core |
| 7 | Resolution: same week, no epilogue, object at rest | core |
| 8 | Opposition: buyer, lender covenant and cash clock | supporting |
| 9 | Supporting cast: the crew's lead dissents and votes against her | supporting |
| 10 | Form: dual first-person present, opening in medias res | form |

That is 7 core differences against a threshold of 3. **H4: clear.**

## 7. H6: mechanical sameness (from `qc/series_diff_final.md`)

- **Result:** AXIS_11_MECHANICAL PASS.
  - The 4-gram FAIL set and WATCH set are both empty.
  - Opening Jaccard ranges 0.197–0.255, below the 0.35 flag; the baseline among the priors is 0.253.
  - Ending Jaccard is 0.000 for every prior.
  - Exit-rhythm L1 distance is at least 0.632 for every prior, above the 0.30 flag.
  - Voice signature: 0 shared tics with any prior, opener Jaccard at most 0.026, no VOICE CONVERGENCE, no house habits.
  - So the blind voice test is not triggered, and **H6: clear.**
- **Coverage caveat (recorded, not a fail):**
  - The priors in that run are excerpts (chapters 1–3 plus the last chapter or epilogue) of P09–P14 only.
  - P01–P08 are not in the text-level diff.
  - The target's repeated-4-gram list was capped at 200.
  - The opening and ending checks are fully covered by the excerpts. The 4-gram intersection is partial.

## 8. One-beat-sheet test

The candidate's sheet:
1. In public, he gives her founding room to another woman and belittles her use of it.
2. She can't sell or leave: her equity is a veto on a pending sale, and she is locked up.
3. Overnight she has the room physically removed and broadcasts it, paying in censure, a fine and his humiliation before the buyer.
4. At the board, the demand she created is trapped by her own rule, then his secret pledge and the cash cliff surface; her veto now starves what she built.
5. Her own unilateral public announcement collapses the buyer, accelerates the lender and drives him out.
6. He accepts consequences he could dodge. He announces each act, does it unwatched, and she never checks.
7. At a workforce vote she adopts his counter-proposal to sacrifice his own project, and the crew passes it over open dissent.
8. In the same week he comes home into a resumed daily ritual, the numbers pass, and the book ends on his chair left at an angle.

How many beats fit each row:
- P01–P07: 1–2 of 8 (beat 1, and a partial on beat 6).
- P09: at most 2.
- P12: at most 2 (partials on beats 1–2).
- R-Z2: 2 strict plus 1 partial (beats 1, 2, partial 8).
- R-B: 2.
- R-Z3: 2.
- All other rows: at most 1.

`single_sheet_fits_all: false`. The sheet fits no book at 7 of 8, let alone two.

## 9. House-template question

These items recur across the set. For each one, the candidate is checked by mechanism.

**(a) Declared packaging constants or items inherent to the lane (reported, not counted under H7):**
- Public erasure of the wife's work by the husband, which is a commission: P01–P07 and all four rejects. This is the constant.
- "Another woman" with no physical affair: P03, P07, P09, R-B, R-Z3. Constant.
- A public credit correction ("whose idea it was"): the P01–P07 status correction, P02, P12. Constant. Here it is placed at the midpoint and runs to one line plus her own list.
- A grovel, an apology and reconciliation. Lane-inherent. The apology here is private, given once, and was never withheld by her terms (unlike P11 and P14).
- A heroine-caused climax: P01–P07, P10–P13. This is the lane's reader promise (the erased wife acts). Its force is reduced here: the deciding authority is a vote, not "her own choice," and his alternative is the one adopted.

**(b) Distinctive house devices the catalog repeats. Each was checked, and the candidate falls into none:**

| House item | Recurs in | Candidate |
|---|---|---|
| Repair ends in his submission to her terms | P09, P11, P12, P13, P14 | Absent. He originates the practice; she never sets terms; at the climax they argue as equals. |
| Repair staged as a witness pattern (community- or institution-witnessed accountability) | P01–P07, P10, P12, P13, P14 | Not dominant. Three of four acts are unwatched; one is public. |
| Repair staged as secret-then-discovered (good deeds she learns of by accident or report) | P09, P11, P13 | Inverted. He announces beforehand and she does not verify. |
| Mutual-fault midpoint that rebalances blame | P09, P11, P14, R-Z2 (P12 by the reject note) | Absent at the midpoint, which exposes his concealment. See flag F1. |
| Inciting kind "external blow" | P10, P11, P13 | No. |
| Last image "act in motion" (walking out together) | P09, P12, P13, P14 | No. |
| Last image "callback to the opening" | P10, P11 | No as primary class. See §2. |
| Months-later or multi-year epilogue | P01–P08, P10–P14 | No. |
| "Her own choice" as the climax's deciding authority, staged as a private line | P09, P11, P12, R-Z2 | No. It is a vote, with a quiet tally. |

**Flags (recorded so a repeat reader's possible notices are on file; not counted as recurrences):**
- **F1: heroine's mirror flaw.** Her unilateral, tell-no-one announcement at the lowest point parallels his tell-no-one pledge, and the father's rule "nobody finds out alone" covers both. Her climax-eve text ("won't cut him off") shows her changing. This is a cousin of the house "heroine has his flaw too" turn (P09, P11, P14). Here it is moved to the lowest point, no one names it, and blame is explicitly not rebalanced. It is a different mechanism, but the page should keep the parallel unspoken, as the row says it does.
- **F2: an elder figure supplies the book's rule.** The living father gives the rule its meaning. P09 (inherited warning) and P11 (dying arbiter names the pattern) are similar. Here it is supporting texture, not an arbiter at a structural turn.
- **F3: the other woman turns ally.** Compare R-Z3 (women compare notes) and P09 (the sympathetic assistant). Here she is a short ally who resigns for her own reasons.
- **F4: P12 detail.** A secret equity transaction surfaces at a company meeting. Pairwise only.

`house_template.found: false` for counted items. The technique-bank rotation clause of H7 (primary device in this book and the previous two) cannot be scored from the stripped rows, because `devices_used` is not supplied. That is a mechanical check the pipeline owes; it was not done in this read.

## 10. Recognizability line

The wife has the disputed room lifted out of the building overnight and broadcasts it. Her own veto then starves the demand her stunt created, and her lone announcement sinks the sale. He takes the consequences unwatched and unchecked. The crew votes to sacrifice his project rather than their weekends, and the book ends on a chair she leaves crooked.

```yaml
  one_beat_sheet_test:
    single_sheet_fits_all: false
    beats_that_break_it:
      P01-P07: [2 exit, 3 exit, 4 paper-trail, 5 his relapse, 7 witnessed, 8 months-later]
      P09: [1 private discovery, 2 self-imposed deadline, 5 his relapse, 6 hero-led]
      P12: [3 work withheld, 4 rejected gift, 5 secret deal is his, 6 private terms, 8 four-months sign]
      R-Z2: [3 legal trigger, 4 her old fault, 5 his testimony, 6 stranded settlement]
  pairwise_core_matches:
    - {book_id: R-Z2, count: 3, axes: [inciting(constant), bind, resolution]}
    - {book_id: R-B, count: 2, axes: [inciting(constant), midpoint]}
    - {book_id: R-Z3, count: 2, axes: [inciting(constant), first_irreversible_decision]}
    - {book_id: P01, count: 1, axes: [inciting(constant)]}
    - {book_id: P02, count: 1, axes: [inciting(constant)]}
    - {book_id: P03, count: 1, axes: [inciting(constant)]}
    - {book_id: P04, count: 1, axes: [inciting(constant)]}
    - {book_id: P05, count: 1, axes: [inciting(constant)]}    # ceiling 4 with partials 4,6,7
    - {book_id: P06, count: 1, axes: [inciting(constant)]}
    - {book_id: P07, count: 1, axes: [inciting(constant)]}
    - {book_id: P09, count: 1, axes: [resolution]}
    - {book_id: R-C, count: 1, axes: [inciting(constant)]}
    - {book_id: P08, count: 0, axes: []}
    - {book_id: P10, count: 0, axes: []}
    - {book_id: P11, count: 0, axes: []}
    - {book_id: P12, count: 0, axes: []}                    # ceiling 3 with partials 1,2,3
    - {book_id: P13, count: 0, axes: []}
    - {book_id: P14, count: 0, axes: []}
  shape_matches: "see §2 — no triple repeat; no two-of-three + climax/repair pair; flags: commission (constant), P14 secondary repair shape"
  staging_matches: "see §3 — max 1/5 (P14 spectacle, R-Z2 evidence, R-Z3 authority); P01-P08 unfiled, inferred 0"
  occupation_swap:
    survives_unchanged: false
    reasoning: "Axes 3, 4 and 6 depend on a craneable modular product, build-to-order deposits held in escrow until steel is cut, and a multi-plant shift crew; only the declared-constant inciting survives a swap."
  recognizability_line: "The wife has the disputed room lifted out of the building overnight and broadcasts it; her own veto then starves the demand her stunt created, and her lone announcement sinks the sale. He takes the consequences unwatched and unchecked. The crew votes to sacrifice his project rather than their weekends, and the book ends on a chair she leaves crooked."
  house_template:
    found: false
    items:
      - "CONSTANT (not counted): public erasure by husband, a commission (P01-P07, all rejects)"
      - "CONSTANT (not counted): the other woman with no affair (P03, P07, P09, R-B, R-Z3)"
      - "CONSTANT (not counted): public credit correction, here placed at the midpoint"
      - "LANE (not counted): apology and reconciliation; heroine-caused climax (reduced here: vote decides, his option adopted)"
      - "ABSENT: submission-to-her-terms repair; witness-pattern repair rhythm; secret-then-discovered rhythm; mutual-fault midpoint; act-in-motion or callback last image; months-later epilogue; 'her own choice' private-line climax"
      - "FLAG F1: heroine's tell-no-one act mirrors his concealment at the lowest point; blame not rebalanced; keep it unspoken on the page"
      - "FLAG F2: elder figure supplies the rule (cf. P09, P11); supporting texture only"
      - "FLAG F3: the other woman as a short-lived ally (cf. R-Z3, P09)"
      - "FLAG F4: secret equity transaction surfacing at a company meeting (P12 only, pairwise)"
      - "UNSCORED: technique-bank rotation clause; devices_used not in the stripped rows"
  voice_signature:
    convergence_flags: []
    house_habits: []
    per_pov_coverage: {heroine: 32082, hero: 13459}
  blind_voice_test:
    run: false     # not triggered: no convergence flags, no house habits
  repeat_reader_review_draft: null   # the reviewer could not honestly write the "same book again" review
  verdict: PASS
  strongest_reasons:
    - "H1: max strict 3/8 (R-Z2, a reject); max published strict 1/8 (P01-P07, P09, mostly the declared constant); no row reaches 5 even counting every partial (max ceiling 4)"
    - "H5/H8: triple commission · accepting a consequence · object at rest repeats no entry; max staging 1/5"
    - "One-beat sheet fits no comparison book; the occupation swap breaks axes 3, 4 and 6"
    - "House template: the candidate avoids every distinctive house repair rhythm, midpoint shape and last-image class; recurrences are the declared constant or lane-inherent"
    - "H6: series_diff_final shows a clean AXIS_11, no voice convergence, no house habits"
  open_conditions:
    - "H7 technique-bank rotation: confirm from the Chemistry Ledgers (devices_used for P13, P14 and this book); not scorable blind"
    - "H6 coverage: text diff ran on excerpts of P09-P14 only; add P01-P08 texts if they exist"
    - "Short set: cross-lane 3/5; must be disclosed at delivery"
    - "Back-fill staging and shape fields for P01-P08"
```

## Verdict

**PASS.**
- H1–H5, the house-template clause of H7, and H8 are clear on the blind read.
- H6 is clear on the supplied measurement.
- Nearest published book: **P05, 1/8 strict, 4/8 counting partials.**
- Nearest row overall: **R-Z2 (reject), 3/8**. It is not a recycled reject.
- The open conditions are those listed at the end of the YAML block above.
