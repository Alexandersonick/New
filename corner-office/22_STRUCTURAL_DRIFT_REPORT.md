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
