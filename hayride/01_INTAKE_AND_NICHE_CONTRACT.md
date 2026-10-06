# Two Tickets to the Haunted Hayride: Intake and Niche Contract

Pipeline: Master Fiction Pipeline v5.0.2 · Mode 1 (BUILD) → Mode 2 (DRAFT) · Status: `NICHE_CALIBRATION`
Project identity: new title. The user supplied the title, subtitle, logline, three categories and seven backend keywords (6 Oct 2026). It is not the twin-sister project in `manuscript/` and `revision/`.

## PROJECT_INPUT (Phase 0)

| Field | Locked value | Source |
|---|---|---|
| Title | *Two Tickets to the Haunted Hayride* | user |
| Subtitle | *A Sweet Halloween Second-Chance Romance* | user |
| Logline | The town's haunted hayride assigns seats by raffle, and she draws the ex who left for the city — back for good, apologetic, and belted in beside her for every bumpy mile of October. The scares are fake; the second look he keeps giving her is not. | user |
| Wave / slot | S1 — Halloween (first book of a seasonal wave) | user |
| Categories | Second Chances Romance · Holiday Romance · Small Town Romance | user |
| Backend keywords | corn maze old flames · fall carnival meet cute · cozy spooky season charm · closed door gentle read · hometown harvest feel good · pumpkin spice warmth · happily ever after | user |
| Fiction format | Full-length novel | derived |
| Target word count | **70,000** | user |
| Standalone / series | Standalone novel. "S1" is read as the first entry in a seasonal wave with **no recurring cast**, so the cross-book FACTS check is out of scope unless a later wave entry reuses this cast. | assumption A1 |
| Pen name | **Shawn J Dean** (provisional) | assumption A2 |
| Primary genre | Contemporary romance: sweet, small-town, holiday (Halloween/autumn), second chance | user (subtitle and categories) |
| Secondary engine | Community-event plot: the hayride season, which runs 10 nights | derived from logline |
| POV / tense | Set at Story Bible Lock (see the candidates). Default: dual POV, close third person, past tense. This differs on purpose from the catalog's dual first person. | assumption A3 |
| Heat | **Sweet.** Kisses on the page. No sex on or off the page. No implied overnight intimacy. Matches the "closed door gentle read" keyword. | user keyword + A4 |
| Language | No profanity. Mild exclamations only ("good grief", "heck"). | A4 |
| Darkness | Low. Grief and regret are allowed. No abuse, no violence, no peril beyond comic or weather scares. | A4 |
| Violence | None | A4 |
| Spookiness | Cozy and staged. Every scare is fake: costumed volunteers, a town legend performed for riders. No real supernatural events. | logline ("the scares are fake") |
| Humor | Yes. Situational and character-logic comedy from the hayride's staged scares, volunteers and town business. Front-loaded, withdrawn at the rupture. | A5 |
| Ending | **HEA on the page in this book.** No cliffhanger. | category + keyword "happily ever after" |
| Required tropes (Promise Audit nouns) | second chance with an ex; small town; Halloween/October; haunted hayride; raffle and two tickets; forced proximity (seated together every ride); he left for the city and is back for good; apology; corn maze; fall carnival; pumpkins/harvest; cozy spooky season | user packaging |
| Forbidden (Breach list) | cheating; surprise love triangle; on-page or implied sex; profanity; real supernatural horror; gore; abuse framed as love; surprise pregnancy or baby epilogue; miscommunication as the only conflict; a passive heroine; a third-act breakup over a misunderstanding | reader-contract-gates.md §1 + sweet contract |
| Reader age | Adult (also safe for a teen reader) | A4 |
| Platform | Amazon KDP (ebook + paperback) | inherited from catalog |
| Trim | 6 × 9 in | default, catalog-consistent |
| TOC | Yes. The previous Shawn J Dean title carries one. | catalog lock |
| Content note | None needed | sweet contract |
| Market evidence | None supplied. Market Research Boundary: research may constrain, never drive. | — |

### Target-Length Contract (locked)

```
TARGET_WORD_COUNT   70,000
ACCEPTABLE_RANGE    66,500 – 73,500
SOFT_CHECKPOINTS    17,500 (25%) · 35,000 (50%) · 52,500 (75%)
FINAL_LENGTH_GATE   63,175 (95% of the range minimum)
```

### ASSUMPTION_LEDGER (each can be overridden by the user; overriding one propagates)

| ID | Assumption | Why | Impact if wrong |
|---|---|---|---|
| A1 | Standalone; "S1" means seasonal wave slot 1 with no shared cast | the user's table header reads "Book / wave", and the S1 row is self-contained | a shared-cast wave opens SERIES_LEDGER.FACTS for this book |
| A2 | Pen name is Shawn J Dean | the only pen name on record in this repo | a different pen name changes the comparison set (Catalog Novelty Gate) |
| A3 | Dual close third person, past tense | the sweet small-town holiday shelf runs heavily dual-POV. Third person moves the narrator mind away from the catalog's two first-person narrators (form field 18). | first person would require the blind voice test |
| A4 | Sweet heat; no profanity; low darkness | subtitle "Sweet", keyword "closed door gentle read" | promise mismatch (Promise Audit) |
| A5 | Comic register present | "cozy spooky season charm", "feel good" | tone drift |

## NICHE_CONTRACT (Phase 1, fresh for this project)

```yaml
NICHE_CONTRACT:
  primary_reader: adult readers of sweet/clean small-town holiday romance; many binge seasonal
    titles in Kindle Unlimited in September–October; also read Hallmark-adjacent fiction.
  dominant_reader_pleasure: watching two people who already loved and lost each other earn
    a second, better-built chance, with cozy autumn atmosphere and a community around them.
  secondary_pleasures: [seasonal texture (October nights, hay, cider, cold hands), comic town
    ensemble, staged scares that turn into real nerves, nostalgia that is tested rather than
    indulged]
  primary_story_engine: romance (trust axis; second-chance variant: the old reason must be
    answered, not forgotten)
  secondary_story_engines: [community-event engine: the hayride season has a schedule, a
    budget, a failure condition and a final night that must work]
  emotional_promise: warmth with an ache; the reader never doubts the HEA but doubts how it
    can be built; the ending feels earned by changed behaviour, not by October magic.
  core_conventions: [HEA on page, sweet heat, small town as an active force, Halloween season
    clock that ends on Oct 31, the ex's return is permanent and that permanence is tested]
  expected_conventions: [forced proximity, a festival set piece, a kiss withheld until it
    matters, a town of opinionated helpers, a grand-but-proportionate final gesture or
    choice, an epilogue or coda]
  optional_conventions: [pet, grandparent figure, best-friend sidekick, a rival bidder,
    snow or storm night, a costume reveal]
  conventions_to_avoid: [real ghosts, city-is-evil / small-town-is-pure moralizing, a hero
    who must give up his whole career as penance, a heroine whose only goal is the hero,
    a villain developer cliché used only as a mustache-twirl]
  likely_tropes: [second chance, forced proximity, small town, holiday, he-came-back,
    grumpy/sunshine optional, fake scares]
  pacing_profile: one scene per chapter mostly; 10 ride nights provide a hard weekly rhythm
    (Fri/Sat × 5 weekends); midweek chapters carry the off-wagon plot.
  narrative_distance_profile: close third, both leads; low-to-moderate interiority;
    reflection ≤3 sentences before an act or line.
  information_profile:
    resolution_mode: FULL_DISCLOSURE
    note: the reason he left is a known fact to her but its true shape is not; one withheld
      item max, and it must pass the Relational Conflict Check.
  expected_scene_types: [wagon rides (banter under staged scares), community meetings and
    volunteer work, corn maze, fall carnival, kitchen/porch scenes, a weather night, the
    Oct 31 final ride]
  escalation_model:
    intensity_register: COZY
    cost_types: [relational, reputational (small town), financial (the hayride's survival /
      her livelihood), emotional]
  magic_certainty_level: N/A
  ending_contract: HEA on page by Oct 31 (or a short coda after); couple question closed;
    no cliffhanger; no sequel bait as last line.
  common_failure_modes: [hangout middle with nothing at stake ("nothing happens", rank 1),
    instant forgiveness, hero's apology substituting for changed behaviour, a third-act
    breakup over a misunderstanding, saccharine town with no friction, seasonal decor
    standing in for plot]
  subversion_opportunities: [the raffle rule is hers, so she is trapped by her own
    integrity; the staged scares become the means of telling the truth; the ex's return
    costs him something visible rather than being a free homecoming]
  chapter_band: {target_words: 2500, min: 1500, max: 3600, scenes_per_chapter_default: 1,
    length_cv_min: 0.15}
  dialogue_floor_chapter: 25%   # romance
  file_weighting: {06_WORLD_BIBLE: LIGHT, 10_INFORMATION_LEDGER: LIGHT,
    09_GENRE_ENGINE_MAPS: SKIP, 13_CHAPTER_MAP: HEAVY}
```

### Genre-promise revision checklist (romance + sweet holiday)
1. Does the relationship state change in every ride-night chapter, with a visible act or line?
2. Is the old reason he left answered by behaviour, not just explained?
3. Does she want something non-romantic that the romance threatens and helps?
4. Does the season clock (10 rides, Oct 31) generate decisions, not only decor?
5. Is the HEA on the page, sweet-heat clean, and earned before the last ride ends?
6. Are the scares fake every time, and still doing story work (truth told in costume, nerve tested)?

### Niche Anti-Sameness extension (sweet small-town holiday)
- No "big-city executive learns the true meaning of [holiday]" arc.
- No saving the town festival from a developer whose only trait is greed.
- No "accidental" snowed/stormed-in cabin that resolves the conflict for them.
- The town is countable: named businesses, named volunteers, with competing agendas.
- Pumpkin spice, flannel and cider appear as specific objects with jobs, never as mood wallpaper.

## Comparison set (Catalog Novelty Gate scope)

Pen name: Shawn J Dean (A2). Lane of this title: `sweet_small_town_holiday_second_chance`.
- Same-lane titles under the pen name: none known. That is a short set: 0 of the 10 rows the gate wants.
- Cross-lane titles: *My Twin Sister Took My Place as His Wife* (full text in repo). *My Billionaire Husband Left Me Out in the Cold* and *My Country Star Husband Brought Her Onstage in My Hometown* are known by title only; their text has not been supplied.
- So the gate can FAIL, or report BLOCKED (missing texts) and AMBER (short set). It cannot return a clean PASS. Every delivery will say so.
