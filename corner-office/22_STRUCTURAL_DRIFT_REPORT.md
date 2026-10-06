# 22 — STRUCTURAL_DRIFT_REPORT

## Stage: Story Bible Lock (concept Z1 → architecture)

```yaml
STRUCTURAL_DRIFT_REPORT:
  book_id: E2-corner-office
  stage: story_bible_lock
  planned_source: concept (candidate_Z1.json)
  measured_source: architecture (architecture_row.json, 13_CHAPTER_MAP.md)
  moved:
    - {field: form.timeline_entry_point, planned: "in medias res (implicit)", measured: in_medias_res_at_retaliation, drift_class: form}
    - {field: supporting.first_attraction_device, planned: unset, measured: mirror_line, drift_class: supporting}
    - {field: supporting.first_care_device, planned: unset, measured: narrator_wrong_once, drift_class: supporting}
  core_axes_moved: none
  staging_moved: none
  shape_moved: none
  gate_rerun:
    verdict: PASS (script AMBER, short set; no hard failures against shelf or reject pool)
    nearest_entry: P12 (published), 3/8; nearest reject Z2 (score 0.218)
    core_matches: 3/8 vs P12 (axis 1 declared constant; axis 5 adversarial; axis 8 constant)
    staging_matches: 0/5 vs every published row that has staging fields
    review_ref: catalog/BLIND_SAMENESS_REVIEW_concept_batch2.md (shelf numbers); catalog/GATE_RECORD_concept.md (ruling)
  defect_filed: none
```

No core, shape or staging field moved between the concept and the architecture. The
architecture adds only supporting devices and form, which were blank at concept. The
blind reader's concept-stage numbers therefore carry to this row unchanged. The
architecture-stage verdict is still issued on this row, not inherited (Never-list 25).
The next measurement is the **manuscript** row at the Continuity Audit.

## Stage: Continuity Audit (architecture → finished manuscript)

```yaml
STRUCTURAL_DRIFT_REPORT:
  book_id: E2-corner-office
  stage: continuity_audit
  planned_source: architecture (catalog/architecture_row.json)
  measured_source: manuscript (catalog/manuscript_row.json, measured from 17_MANUSCRIPT.md, 68,499 words)
  moved:
    - {field: resolution.epilogue_design, planned: no_epilogue_final_scene_days_after_climax, measured: no_epilogue_final_chapter_same_week_test_day, drift_class: form}
    - {field: form.ending_image, planned: "two desks pushed together (months later)", measured: "his chair left pushed back from the radiator; she doesn't straighten it", drift_class: form (class unchanged: object at rest)}
    - {field: supporting.intimacy_function, planned: marks_return_of_asking, measured: marks_return_of_telling, drift_class: supporting}
    - {field: supporting.relocation_reset, planned: room moves, heroine doesn't, measured: room moves and the hero sleeps in it after the rupture, drift_class: supporting}
    - {field: supporting.signature_scenes, planned: "boardroom demand", measured: "boardroom diligence answer + her on-record correction + cash reveal; hero ends the late calls and signs the guarantee unwatched", drift_class: supporting}
    - {field: supporting.concealment_motive, planned: unset, measured: "pride: telling her meant saying she'd been right", drift_class: supporting}
    - {field: form.narrative_voice_tags, planned: low_numeric, measured: dual_pov_salesman_self_correction, drift_class: form}
  core_axes_moved: none (axes 1–8 carry the same mechanisms; axis 6 gained the hero's costly amendment, which the architecture already had as "argument as equals")
  staging_moved: none (workplace floor / workforce / no evidence / a vote / a quiet tally)
  shape_moved: none (commission · accepting a consequence he could avoid · object at rest)
  gate_rerun:
    verdict: PASS (blind read); script AMBER (short set, 8 rows without staging fields, 3 of 5 cross-lane)
    nearest_published: P05, 1/8 core (4/8 counting partial echoes); staging max 1/5
    nearest_any: R-Z2 (rejected concept), 3/8; not a recycled reject (its two rejection reasons are absent)
    one_beat_sheet: fits no comparison book
    house_template: repeats are the declared packaging constant or lane-inherent; flags F1–F4 recorded, none failing
    review_ref: catalog/BLIND_SAMENESS_REVIEW_measured_v2.md (supersedes _measured.md, which failed on H7 before the fixes in 18_REVISION_LOG.md)
    open_items:
      - "H7 technique-bank rotation not blind-scorable: the earlier books have no devices_used field. Author-scored (provisional): this book's primary chemistry device is the mirror line; the concept-stage house-template list names the care object and the involuntary symptom as catalog-primary, and neither is primary here."
      - "H6 text coverage: series_diff ran against excerpts of P09–P14 only; P01–P08 text was not available."
      - "Short set: 3 of 5 cross-lane rows; P01–P08 lack staging fields."
  defect_filed: none
```

The first measured re-score (`BLIND_SAMENESS_REVIEW_measured.md`) failed on H7. The book
balanced fault between the spouses, had a secret devotion discovered later, and ended on a "don't
decide alone" lesson. The fixes are logged in `18_REVISION_LOG.md` (M-01 to M-06). The second
blind read is on the fixed manuscript and passes. The verdict above is issued on the measured
row, not inherited from the concept or the architecture.
