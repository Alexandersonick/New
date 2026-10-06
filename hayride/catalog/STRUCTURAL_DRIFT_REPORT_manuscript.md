# STRUCTURAL_DRIFT_REPORT: Continuity Audit (manuscript, measured)

```yaml
STRUCTURAL_DRIFT_REPORT:
  book_id: two-tickets-haunted-hayride
  stage: continuity_audit
  planned_source: architecture       # fingerprint_hayride_architecture.json (Story Bible Lock)
  measured_source: manuscript        # fingerprint_hayride_measured.json (read from full text, revised after H7)
  moved:
    - field: bind on-page cost
      planned: breaking her own rule hands the event to a rival
      measured: 4–1 formal warning, one more breach and she steps down
      drift_class: supporting
      direction: toward PRIOR-1 (one-chance terms)
      action: kept; logged. It is the mechanism behind the climax step-down (rule twelve), so
        removing it would break axis 6/8 causality.
    - field: axis 4 midpoint (venue)
      planned: true story co-built for her finale
      measured: co-built in HIS barn workspace; adopted 4–3 by committee
      drift_class: supporting (venue)
      direction: mild toward PRIOR-1 (hero's workspace on her deadline)
      action: kept. Her craft carries the effect (circuits, bark); his contribution is one kerfed
        hummock. The H3 occupation-swap test still changes the midpoint.
    - field: axis 5 rupture
      planned: truth "no" meets an open exit; her original wrong recurs ("Go")
      measured: same
      drift_class: none (planned at Story Bible Lock, fix F6/F7)
    - field: axis 7 repair, hero side
      planned: sustained truthful presence, unglamorous
      measured_before_revision: presence + care-object-and-service (porch light mended unasked)
      measured_after_revision: presence; the porch light is now HER act (ch20). Object acts
        remaining are the held Maglite (ch8) and his own shop door (ch26).
      drift_class: core (axis 7 detail)
      direction: corrected back to plan
    - field: axis 7 repair, heroine side, and ending payoff
      planned: public confession, then reconciliation
      measured_before_revision: ladder ending in the one-word "Stay." (PRIOR-1 device)
      measured_after_revision: ladder ending in her own terms ("ask on a Tuesday... the answer's
        yes"); the brother's one-word suggestion is set up and refused
      drift_class: core (axis 8 detail) / device
      direction: corrected away from PRIOR-1
    - field: climax staging (venue / evidence / spectacle / authority / audience)
      planned: performance stop at the pond / act_performed / silence_then_single_voice /
        heroine_own_choice / riders
      measured: dock at the finale stop / confession + act / silence then one line from the bench;
        lanterns lifted / her own choice, ratified by her own rule / 32 riders + vice-chair
      drift_class: staging
      matches_vs_PRIOR-1: 0/5 (blind count, BLIND_SAMENESS_REVIEW_measured §3)
    - field: form 18 narrator signature (Gus)
      planned: stage-manager cue-calling, object-talk, self-mocking hyperbole, parentheses
      measured_before_revision: device in 3 chapters; "He didn't" chains (52) and "because"
        rationales converged on PRIOR-1's hero (blind voice test round 1)
      measured_after_revision: device in ch2, 4, 7, 12, 15, 17, 19 (ending), 21, 29; "He didn't"
        11; blind voice test round 2 PASS 3/3
      drift_class: form
      direction: corrected back to the Voice Contract
  gate_rerun:
    script: catalog/similarity_measured.md (catalog_similarity.py v1.1); reports/series_diff_post_voice_revision.md
    triage: PRIOR-1 0.080 (PASS band); nearest pool row A 0.227 (own lineage), E 0.161, C 0.147
    blind_review: catalog/BLIND_SAMENESS_REVIEW_measured.md
    verdict_on_measured_row: >
      H1–H5, H8 PASS against the available set (0/8 core axes and 0/5 staging fields vs PRIOR-1).
      H6 PASS (blind voice test round 2, 3/3; series_diff shows 0 shared tics, no house habits).
      H7 FAIL at review, then REMEDIATED in text. A blind re-score of H7 on the revised text is
      outstanding.
    nearest_entry (shelf): My Twin Sister Took My Place as His Wife
    core_matches_vs_shelf: 0/8
    staging_matches_vs_shelf: 0/5
    overall: BLOCKED. Two earlier titles (My Billionaire Husband Left Me Out in the Cold; My
      Country Star Husband Brought Her Onstage in My Hometown) have no text or fingerprint
      available. The comparison set is short (0 same-lane, 1 cross-lane).
  defect_filed: CATALOG_SAMENESS (H7, device level) → Revision Stack → remediated (see review §11)
```
