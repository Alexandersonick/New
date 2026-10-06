# BLIND_SAMENESS_REVIEW (concept stage, Catalog Novelty Gate)

```yaml
BLIND_SAMENESS_REVIEW:
  comparison_set:
    candidates: [A, B, C]
    shelf:
      - PRIOR-1: available (stripped full-text fingerprint, cross-lane: marriage crisis)
      - PRIOR-2: BLOCKED (content unavailable)
      - PRIOR-3: BLOCKED (content unavailable)
    inputs_read_only:
      - scratchpad/catalog/stripped_candidates.md
      - scratchpad/catalog/stripped_shelf.md
  stripped: true
  reviewer: "independent subagent (blind)"
  gate_status: BLOCKED   # two of three prior titles unscored; shelf is short. Verdicts below are against PRIOR-1 plus the batch only.
  scoring_note: >
    "Match" = same mechanism (what kind of thing happens, who causes it). Full matches count 1.
    Partials (same function family, different mechanism) are listed but NOT counted toward H1.
    The logline-fixed premise (exes, he returned, the draw seats them for all ten runs, staged scares)
    is excluded from matching between candidates.

  axis_fingerprints:            # mechanism class per axis, used for every pairwise row
    A:
      1_inciting: chance pairing, locked by a no-swap rule she wrote herself (external blow / self-authored trap)
      2_bind: breaking her own rule hands her leadership to a rival who would shut the event down (credibility cost)
      3_first_irreversible: she imposes a transactional bargain (one truthful question per run; he gets one back)
      4_midpoint: concealed truth exposed, her own share of the breakup, so blame moves off him
      5_rupture: her own truth device backfires; his honest answer ("no, I would not have come back") wounds
      6_climax: she drops the script and publicly confesses their true story, her fault included, to a full load of riders; she causes it
      7_repair: sustained unglamorous unwitnessed presence plus risking real loss (turns down a rehire)
      8_resolution: engaged; coda one year later; last image = spoken line
    B:
      1_inciting: discovery (he is the rival bidder)
      2_bind: a third party's contractual condition (walking out = withdrawal)
      3_first_irreversible: she stakes her home on a signed pledge (collateral)
      4_midpoint: an external threat (land sale) forces enemies into allies
      5_rupture: hero repeats his original error (decides for both of them); she walks
      6_climax: she produces an alternative plan, backed by community money, that meets the gatekeeper's terms; the contract decides
      7_repair: he cedes control formally in front of witnesses (signs away his votes before her family)
      8_resolution: relationship re-founded on formal new terms (partnership); last image = document
    C:
      1_inciting: commission by him (his official act restricts her event)
      2_bind: an external rule makes him indispensable (he is the required officer on her vehicle)
      3_first_irreversible: she signs personal responsibility for a deadline rebuild
      4_midpoint: concealed truth about the past exposed (his false guilt over the fire; true cause = her grandfather), so blame moves off him
      5_rupture: hero repeats his original error (duty over her, again), in public
      6_climax: she produces an alternative plan that meets the gatekeeper's terms, carried out by the community; his sign-off plus the weather decide
      7_repair: he lets her be right in public by reversing his own closure (he cedes his authority to her plan in front of witnesses)
      8_resolution: engaged; next-season flash-forward; last image = act in motion
    PRIOR-1:
      1_inciting: discovery of a betrayal
      2_bind: she depends on him to finish her skilled job before a fixed deadline; she sets the terms ("pay the weeks back in evenings")
      3_first_irreversible: she leaves her house key and moves out
      4_midpoint: concealed deception (forgery) exposed; stakes reframe; one-chance terms
      5_rupture: hero repeats the core harm (acts alone without her); second trough
      6_climax: joint; her expertise directs his hands; an official watches and signs off
      7_repair: being taught by her, on her terms (fail, then succeed)
      8_resolution: marriage rebuilt on renegotiated terms ("lists of asks"); time-jump epilogue; last image = spoken one-word callback

  pairwise_core_matches:
    A-B:
      count: 0
      matching_axes: []
      partials: [6_climax (her final-act move also lands community money: word of mouth vs pre-sales)]
    A-C:
      count: 1
      matching_axes: [4_midpoint (hidden truth about the original breakup comes out and takes the blame off him)]
      partials:
        - 6_climax (on the final night she breaks the event's normal format in front of the community: drops the script vs re-routes)
        - 8_resolution (engaged, with a one-year / next-season time jump; last-image class differs)
    B-C:
      count: 4
      matching_axes:
        - 3_first_irreversible (she signs personal liability: pledges her house vs signs as responsible party)
        - 5_rupture (hero repeats his original error and the relationship breaks)
        - 6_climax (her alternative plan meets the gatekeeper's terms and is carried by the community; a formal authority decides)
        - 7_repair (he publicly cedes his decision power to her in front of the people who matter. The taxonomy labels differ, "relinquishing control" vs "letting her be right", but the mechanism is the same: the hero signs or overrules away his own authority before witnesses)
      partials: [2_bind (an outside party's rule makes leaving the pairing cost her the goal)]
      note: 4/8 full plus 1 partial. One axis short of H1 ≥5.
    A-P1:
      count: 2
      matching_axes:
        - 4_midpoint (concealed truth or deception exposed at midpoint; secret-then-discovered)
        - 8_resolution (reconciliation + time-jump epilogue + spoken-line last image)
      partials: [heroine-imposed transactional terms device (A axis 3 / P1 axis 2, so it sits on different axes)]
    B-P1:
      count: 2
      matching_axes:
        - 1_inciting (discovery, by function class)
        - 5_rupture (hero repeats the core harm by acting or deciding without her; she ends the arrangement)
      partials:
        - 8_resolution (relationship re-founded on formal renegotiated terms; last-image class differs)
        - 6_climax (outcome decided by paper authority: contract vs certifier signature)
        - 3_first_irreversible (her house is the stake vs her house is abandoned; surface echo)
    C-P1:
      count: 3
      matching_axes:
        - 2_bind (she cannot complete her work without him; skilled job, deadline, external requirement)
        - 4_midpoint (concealed truth exposed, reframing)
        - 5_rupture (hero repeats the core harm)
      partials:
        - 6_climax (her expertise is proven in a physical act before an official whose sign-off decides)
        - 7_repair (the hero submits his judgment to her expertise in front of witnesses: taught by her vs reverses his closure on her plan's merits)
      structural_echo: >
        C rebuilds P1's skeleton: her skilled hand job with a fixed deadline, an official who must certify it,
        a hero who repeats the harm, and a hero who finally puts his own judgment under hers. The regulator and
        rebuild surface hides this.

  max_core_overlap:
    A: {vs_shelf: 2 (P1), vs_any_row: 2 (P1)}
    B: {vs_shelf: 2 (P1, +3 partials), vs_any_row: 4 (C)}
    C: {vs_shelf: 3 (P1, +2 partials), vs_any_row: 4 (B)}

  shape_matches:               # inciting kind / repair shape / ending-image class
    triples:
      A: [external blow (chance, self-locked), sustained unglamorous presence + risking real loss, spoken line]
      B: [discovery, relinquishing power or control, document or record]
      C: [commission, letting her be right in front of the people who mattered, act in motion]
      P1: [discovery, being taught by her on her terms, spoken line (callback)]
    pairs:
      A-P1: 1/3 (ending: spoken line)
      B-P1: 1/3 (inciting: discovery)
      C-P1: 0/3
      A-B: 0/3
      A-C: 0/3
      B-C: 0/3 by taxonomy label. At the mechanism-family level the repair matches (he cedes authority before witnesses), so 1/3.
    full_triple_repeat: none

  staging_matches:             # venue / audience / evidence / authority / spectacle
    A-P1: 1/5 (spectacle: private line)
    B-P1: 0/5 full (authority partial: contract vs official signature)
    C-P1: 2/5 (evidence: act performed; authority: official sign-off, though C adds weather)
    A-B: 0/5
    A-C: 1/5 (audience: the community; A's riders are a mixed slice of it)
    B-C: 1/5 (spectacle: quiet tally)

  hard_fail_checks:
    H1 (≥5/8 core vs any one book):
      A: PASS (max 2)
      B: PASS (max 4 vs C; at the edge)
      C: PASS (max 4 vs B; 3 vs P1)
    H2 (four consecutive macro-beats in same order as an earlier book):
      A: PASS (no run longer than 1 against P1)
      B: FAIL (strict) vs P1 beats 5-8: hero repeats the harm, then a formal authority ratifies her outcome, then the hero cedes his agency to her formally, then the relationship is re-founded on renegotiated terms
      C: FAIL (strict) vs P1 beats 4-7: concealed truth exposed, then the hero repeats the harm, then an official certifies her competence in a physical demonstration, then the hero submits his judgment to her expertise
    H3 (occupation swap):
      A: FAIL. Inciting (the draw plus her rule), midpoint (she sent him away) and climax (she drops the script and tells the true story) survive any profession swap. Her scare-building craft drives none of the three. Fixable without touching any other axis.
      B: FAIL. A business-acquisition rivalry, a land-sale midpoint and a pre-sales counter-deal transplant onto any shop, farm or inn unchanged. "Knows the books" is generic.
      C: PASS. Inciting needs his regulatory power; the climax needs her rebuild skill and his conditions; the midpoint's fire investigation leans on both.
    H4 (surface-only difference from nearest earlier book, <3 mechanism diffs):
      A: PASS (6 differences vs P1)
      B: PASS (6 vs P1)
      C: PASS (5 vs P1, though see H2 and structural_echo)
    H5 (climax + repair both repeat; or triple; or 2 shape axes + climax/repair pair):
      A: PASS
      B: PASS vs shelf. Intra-batch: climax AND repair both repeat C's, so B and C cannot both advance.
      C: PASS vs shelf by taxonomy (climax and repair are partial matches with P1, a near miss). Intra-batch: same collision with B.
    H7 (house template): see house_template. A breaks the dominant template. B and C both follow it.
    H8 (≥4/5 staging, or climax+repair match + ≥3 staging):
      A: PASS (max 1/5)
      B: PASS (max 1/5)
      C: PASS (2/5 vs P1)

  occupation_swap:
    A: FAIL. Profession is decorative. Required fix: route the truth bargain, the midpoint or the climax through a scare she built (for example, the final-run confession is delivered through, or instead of, a staged effect only she can rig or disarm), so swapping her craft breaks the beat.
    B: FAIL. Rivals bidding on a business is profession- and setting-agnostic.
    C: PASS.

  recognizability_line:
    A: "She makes her ex answer one true question a night, and when her own rule forces the answer that guts her, she ends the season by telling a full ride that she was the one who sent him away."
    B: "Two exes bidding for the same failing business are forced into partnership by a land sale, until he decides for both of them again and she outbids his money with the town's."
    C: "The ex who comes home and shuts down her grandfather's attraction learns the fire he ran from was never his fault, and on the storm-night finale she builds a route that meets his own safety terms so he has to overrule himself in public."
    assessment: >
      All three have a line (no (c) fail). A's line is the most distinctive: it rests on a device and a heroine
      self-indictment the shelf does not have. C's is distinctive at the surface but sits on P1's skeleton.
      B's line reads as stock rivals-to-partners and is the weakest.

  house_template:
    recurring_across_set:
      - midpoint = concealed truth exposed (secret-then-discovered): P1, A, C (3 of 4)
      - rupture = hero repeats his original wrong: P1, B, C (3 of 4)
      - climax adjudicated by formal or paper authority (signature, contract, official sign-off): P1, B, C (3 of 4)
      - climax = her competence or plan vindicated, with the community or an institution as witness: P1, B, C
      - repair = hero publicly subordinates his authority or judgment to hers, staged before witnesses (witness pattern): P1, B, C (3 of 4)
      - heroine imposes transactional terms to structure the forced proximity: P1 ("pay the weeks back in evenings"), A (one question per run)
      - time-jump epilogue: P1 (months), A (one year), C (next season)
      - spoken-line last image: P1, A
      - her house as a plot stake: P1 (leaves the key), B (pledges as collateral)
      - fail-then-succeed rhythm at the repair or climax: P1 (apprenticeship), C (closes, then reverses), B (partnership breaks, then is re-founded)
    verdict: >
      There is a house template, and it is a back half: hero repeats the wrong, her plan or craft is ratified by
      an official or document, then the hero cedes authority to her before witnesses. B and C run it and A does not.
      A inherits three smaller house habits from P1: a midpoint reveal, the heroine-imposed bargain device, and a
      time-jump plus spoken-line ending. Change A's last-image class (an object at rest or a third party's gesture,
      not a spoken line) to cut the ending echo.

  one_beat_sheet_test:
    result: FAIL for {B, C}. One sheet fits both at 7/8.
    sheet:
      1: His return puts him directly against her goal (rival bidder / regulator). [B true, C true]
      2: An outside party's rule chains them together for the season; leaving costs her the goal. [B, C]
      3: She signs her personal stake onto the outcome. [B, C]
      4: Midpoint turns him from obstacle to ally. [B true; C false: C's midpoint is a past-guilt reveal]
      5: He repeats his old error, putting his priority over her, and it breaks. [B, C]
      6: She answers with her own alternative plan, carried by the community, that meets the gatekeeper's terms. [B, C]
      7: He publicly gives up his power to her plan in front of the people who matter. [B, C]
      8: They re-found a joint future. [B, C]
    other_combinations:
      A+P1: about 4/8 (terms device, midpoint reveal, time-jump, spoken line)
      C+P1: about 5/8
      B+P1: about 5/8
      A+B, A+C: 4/8 or fewer
    implication: >
      The batch holds two distinct concepts, not three: B and C are one book. The gate's ≥3-candidate
      requirement is not genuinely met. Replace B or C with a concept that differs in back-half mechanism.

  hostile_reader_flags:
    A:
      - The climax is a speech. A public confession over a microphone or to a wagonload is "talk, not act". Pair it with a costly physical act she performs, or a consequence she accepts on the spot.
      - The inciting is the logline itself. A adds only the self-written rule, so chapter 1 risks feeling pre-sold.
      - Her backstory fault (she sent him away and let the town blame him for years) risks unlikeability. It must be paid off in the open, which the climax does, but early chapters must hint at it fairly.
      - His honest "no, I would not have come back" can sink him unless the rehire refusal happens on the page and costs him visibly. It must not be reported offstage.
      - The one-question-per-run device can turn mechanical over ten runs. Vary what each question costs.
      - The rival leader risks being a cardboard antagonist.
    B:
      - Romance resolved by paperwork. The contract decides the climax and a vote-signing is the repair, which reads as transactional.
      - The land-sale midpoint is a deus ex machina from a third party.
      - Stock rivals-to-partners trope. The Halloween event is incidental; this could be any business.
      - Money and power imbalance: he out-funds her. "He decides for both" is fair conflict, but the repair is a legal instrument, not a sacrifice.
    C:
      - The climax is really his. The decisive act is his sign-off reversal, so climax and repair collapse into one hero beat.
      - Miscommunication backstory. He left for years over a false belief one conversation would have cleared.
      - Credibility: a safety regulator reversing a weather closure because his ex re-routed the walk reads as compromised judgment, and a community walk in wind is a risky image for a sweet romance.
      - Weather as co-authority makes the outcome partly external.
      - Posthumously blaming the beloved grandfather may sour the legacy goal.

  verdicts:   # overall gate status remains BLOCKED (two prior titles unavailable; shelf short)
    A: FAIL (H3 occupation swap only). The failure is not sameness, and it can be fixed by wiring her scare-building craft into inciting, midpoint or climax. Lowest sameness in the set.
    B: FAIL (H3; H2 strict vs PRIOR-1 beats 5-8; one-beat-sheet collision with C; intra-batch H5 collision with C)
    C: FAIL (H2 strict vs PRIOR-1 beats 4-7; one-beat-sheet collision with B; intra-batch H5 collision with B). PASS on H1/H3/H4/H5(shelf)/H8, but its back half is PRIOR-1's back half.

  selection:
    lowest_maximum_core_overlap_vs_shelf: A (2/8 vs PRIOR-1; B = 2 with 3 partials; C = 3 with 2 partials)
    lowest_maximum_core_overlap_vs_any_row: A (2; B and C = 4)
    tie_break: >
      A and B tie at 2 full vs the shelf. A wins on partials (1 vs 3) and on the recognizability line
      (A's line is device-plus-confession specific; B's is stock).
    selected: A
    conditions_before_concept_kill_test:
      - Fix H3: make her scare-building skill load-bearing in at least one of inciting, midpoint or climax.
      - Change the last-image class away from a spoken line (PRIOR-1 used one) to cut the house ending.
      - Give the climax a physical or costly act beyond the confession so it is not just a speech.
      - Put the hero's rehire refusal on the page, at visible cost.
      - Regenerate a third candidate to replace B or C (they are one concept) so the batch meets ≥3 distinct.
      - Re-run the gate once PRIOR-2 and PRIOR-3 are available. Until then status = BLOCKED.

  strongest_reasons:
    - A is the only candidate off the house back-half (hero repeats the wrong, official or document ratifies her, hero cedes authority before witnesses). B and C both run it, and so does PRIOR-1.
    - C reads as new but is PRIOR-1's skeleton re-skinned: her deadline skilled job, an official who certifies it, the hero repeating the harm, the hero deferring to her expertise. Four consecutive macro-beats line up.
    - B and C share 4/8 core axes and pass a single 7/8 beat sheet. Climax and repair both repeat between them, so the batch is effectively two concepts.
    - A's only hard fail is a decorative profession (H3), not sameness. It is the cheapest failure in the set to fix.
```
