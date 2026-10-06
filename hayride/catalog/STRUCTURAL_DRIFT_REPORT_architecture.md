# STRUCTURAL_DRIFT_REPORT: Story Bible Lock (architecture)

```yaml
STRUCTURAL_DRIFT_REPORT:
  book_id: two-tickets-haunted-hayride
  stage: story_bible_lock
  planned_source: concept            # candidate_A2.json (selected, batch 2)
  measured_source: architecture      # fingerprint_hayride_architecture.json (03_STORY_BIBLE.md + 13_CHAPTER_MAP.md)
  moved:
    - field: core.rupture (darkest_moment_cause)
      planned: truth_on_request_plus_open_exit
      measured: truth_on_request_then_heroine_repeats_own_wrong
      drift_class: core
      note: blind-reader fix F6/F7. He tells her about the offer directly; she says "Go." Her
        original wrong recurs, not his, so this moves AWAY from the house template ("hero
        repeats his original wrong").
    - field: staging.spectacle_mode
      planned: quiet_tally
      measured: silence_then_single_voice
      drift_class: staging
      note: blind-reader fix F4 (B and C used quiet_tally; the climax is a performance in the dark).
    - field: staging.evidence_delivery
      planned: act_performed (+ confession)
      measured: act_performed
      drift_class: staging
      note: unchanged in substance; the confession is delivered through the performed effect.
    - field: resolution_visibility
      planned: community_witnessed
      measured: community_witnessed_then_private
      drift_class: core (axis 8)
    - field: ending_state
      planned: reconciled_couple
      measured: reconciled_committed_couple
      drift_class: core (axis 8)
      note: Ch 30 adds the non-hayride question; the epilogue shape is unchanged (no time jump; object at rest).
    - field: climax (axis 6), wording only
      planned: she unbelts mid-run; he takes over the narration
      measured: she unbelts at the scheduled pond stop with the engine off; he stays belted and
        silent and keeps the riders; he does NOT narrate
      drift_class: core (mechanism unchanged: heroine performs her own effect as confession)
      note: fixes F1/F2. Removes the "hero assumes her authority in public" drift.
    - field: macro_beats, signature_scenes, narrative_voice_tags
      drift_class: supporting/form
      note: expanded from concept to the 30-chapter plan; adds softening_fails_at_cost (F5),
        heroine_builds_true_finale (the target is met by her craft, not a bailout, F3) and
        resigns_under_own_rule.
  gate_rerun:
    script: catalog/similarity_architecture.md (catalog_similarity.py v1.1, exit 2)
    script_hard_failures:
      - vs "Candidate A - Ten Questions": only 3 of 7 primary axes differ. Ruling: LINEAGE, not
        sameness. A was the batch-1 SELECTED concept, re-architected into A2 because it failed H3
        alone; it is this book's own earlier row, not a separate catalog entry. Recorded so the
        pool keeps it; it is not a recycled reject (A was never rejected for sameness).
      - vs "Candidate C - The Inspector": "same heroine goal and agency pattern with a hero-owned
        climax". Ruling: SCRIPT ARTIFACT, already overturned by the batch-2 blind reader (the
        substring "hero" matches "heroine_led"); core mechanism matches with C are 0/8.
    verdict: PENDING_BLIND_CONFIRMATION → see BLIND_SAMENESS_REVIEW_architecture.md
    nearest_entry (shelf): My Twin Sister Took My Place as His Wife
    core_matches_vs_shelf: 0/8 (batch-2 blind count for A2; no core axis moved toward PRIOR-1)
    staging_matches_vs_shelf: 1/5 (act_performed)
    overall: BLOCKED. Two earlier titles (My Billionaire Husband Left Me Out in the Cold; My
      Country Star Husband Brought Her Onstage in My Hometown) have no text or fingerprint
      available. The comparison set is short (0 same-lane, 1 cross-lane).
  defect_filed: none
```

## Script defect noted (for the skill owner, not patched here)
`scripts/catalog_similarity.py` line ~301 tests `"hero" in owner`. That is true for `heroine_led`, so every heroine-led climax with a matching goal and agency pattern hard-fails as "hero-owned". Suggested fix: `owner in {"hero_led", "hero"}` or `owner.startswith("hero_")` excluding `heroine`. Both blind readers flagged it. The pipeline rule "never patch the gate to pass" applies, so it is reported, not edited.
