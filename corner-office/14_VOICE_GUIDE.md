# 14 — Voice Contract (locks at Story Bible Lock)

Set against the measured catalog. The earlier narrators across all three pen names share
these traits: forensic, retrospective, numerically precise, metaphors from the heroine's own
trade, explanatory or therapeutic dialogue, and an opening sentence of the form "X was
wrong" (3 of 6 sampled books). This narrator is deliberately set outside all of them.

```yaml
VOICE_CONTRACT:
  narrator_signature_device:
    Pip: >
      The wrong-question answer. She answers the question under the question, out loud or in
      narration, with a joke or an object, and moves on without explaining it. Narration
      never glosses its own joke.
    Adam: >
      The struck pitch. He narrates like a man in a room he is trying to win, catches himself,
      and says "Strike that." It appears at most twice a chapter and drops out of his last
      three chapters (the register shift is the repair).
  three_sentences_only_this_narrator_could_say:
    Pip:
      - "My mother's love language is telling you what you did wrong at a funeral you weren't at."
      - "I don't cry at work. I go out to the yard and kick a pallet until it's the pallet's fault."
      - "He has the face of a man who has never once been told no by a woman holding a drill."
    Adam:
      - "I can sell anything to anybody, which is how I know the exact sound of a room deciding not to buy."
      - "Strike that. I'm not sorry the way you say it in a deck. I'm sorry the way you are at three a.m."
      - "There are two things I know how to do with a silence, fill it or bill it."
  sentence_one_claim:
    book: an anomaly stated as fact, in the present tense; never "X was wrong"; never weather or waking
    adam_ch4: a spoken line
  self_comment_density_target: "Pip Ch 1: ≥1 aside or fragment per ~150 words; Adam: ≤1 per 200"
  register_shift_plan:
    - "Jokes per 1,000 words: about 6 in Ch 1–8, about 3 in Ch 15–20, 0–1 in Ch 21–22 (rupture), back to about 3 in Ch 29–30"
    - "Rupture (Ch 21–22): sentence mean drops to ≤60% of the setup chapters; dialogue share falls in the grief beats"
    - "Adam: 'Strike that' disappears after Ch 23. He stops correcting himself because he stops pitching."
    - "Climax (Ch 28): short sentences, crowd noise as objects (boots, a thermos lid, the time clock)"
  forbidden_in_narration:
    - the Tier-1 list (ai-texture-audit.md §1)
    - attracted / attraction
    - "load-bearing" or "load path" as a metaphor for feeling (trade-metaphor house habit; literal use only)
    - exact clock times and counts as voice texture (numbers only where the plot needs them)
    - "for the first time"; "I want to be honest"; "for what it's worth"; "[name] understood"
  narrative_voice_tags:
    Pip: [present_tense_immediate, people_reader_not_object_reader, comic_deflection, withholds_interpretation,
          metaphor_source_family_parish_kitchen_bowling, certainty_high_self_deception_about_own_silence]
    Adam: [present_tense_immediate, performative_self_correction, short_declaratives,
           metaphor_source_selling_and_sports_radio, attention_bias_to_faces_and_rooms]
  voice_vector_targets:            # series_diff.py §6, narration only, per 1k words
    em_dash: "≤2.0  (priors 0–11.3; Briar Salvano titles run 5.7–11.3)"
    neg_par: "0"
    not_exactly: "0"
    understood: "0"
    hedge: "0"
    first_time: "0  (priors up to 0.56)"
    filter: "≤2.5  (priors 3.4–5.4 → deliberately below every prior)"
    theme: "≤0.1"
```

## IDIOLECT_CARDs

| Character | Sentence habit | Register | Deflection | Tic (max one) | Never says | First line in book |
|---|---|---|---|---|---|---|
| Pip | short, then one long run-on when angry | West Side plain, mild swearing, Polish kitchen words | a joke that answers a different question | "That's interesting." (means: you are about to lose) | "I'm hurt." | "Lower. Lower. Okay, stop, you're kissing the mullion." |
| Adam | pitch cadence: claim, proof, ask | polished, sports radio, "listen" | reframing the question | "Strike that." (narration only) | "I don't know." | "You barely use it." |
| Simone | complete sentences, no contractions under pressure | corporate-precise, dry | literalism | none | flattery | "I asked for it. He said yes before I finished the sentence." |
| Lolo | fragments, profanity as punctuation | shop floor, bowling alley | insult as affection | "Hon." | "sorry" | "You want it out the window or out the door, hon? 'Cause the door's a no." |
| Halina | questions that are verdicts | Polish-inflected English, saints' days | changes the subject to food | "Eat." | "I was wrong." | "So. He sends flowers, he doesn't come." |
| Ruth | investor plural, "we" | fund-speak, cheerful | "Let's take that offline." | none | a number she can't defend | "We love the energy. We'd love it more in a different building." |

Tag-strip test target: ≥80% attribution on every exchange of six lines or more.
