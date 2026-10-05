# Revision edits for "My Twin Sister Took My Place as His Wife" (Mode 4, against the 5 Oct 2026 audit).
# Each edit: (op, para_index, expect_prefix, finding, text)
#   op: "replace" | "delete" | "insert_after"
#   para_index: absolute DOCX body paragraph index in the supplied _2 manuscript
#   expect_prefix: the original paragraph must start with this (guards against mis-targeting)
#   text: *...* marks italic runs
EDITS = [
# ---------------- R04: a visible obstacle to verification (Ch 5, live scene, before any confession) --------
("replace", 486, "“That’s what bothered me.”", "R04",
 "“That’s what bothered me. So the second week of October I called your mother, because you weren’t picking up and she was.” She did the voice before I could stop her, soft and level, the front desk of an elementary school. “‘Maudie’s sleeping sixteen hours a day on those pills, dear, and the doctors want no telephone calls. She asked me specially to keep you from flying over. She’d hate to be seen like this. You know how private she is.’” Odalys dropped the voice. “And you are. So the first time I had a ticket open, I closed it.”"),
("insert_after", 486, None, "R04",
 "“My mother has never once in her life called me private,” I said. “She calls me difficult.”"),
("insert_after", 486, None, "R04",
 "She took her phone out and held it, locked. “I screenshot everything when something smells wrong, it’s a sickness, I have a whole folder. You want to see?”"),
("replace", 1420, "“I had a ticket open on my laptop,”", "R04 (consistency)",
 "“I had a ticket open on my laptop,” she said. “Twice. The second time I didn’t call your mother first. Philadelphia to Bologna, $900, and my finger on the button. And then you sent me a picture.” She leaned over and turned two pages and put her finger on it. “View from my window. A road with all those skinny trees. And I thought, fine, she’s alive, she’s being weird, she hit her head, leave her alone.”"),

# ---------------- R05: make the five-week scope explicit (Ch 6) ----------------
("replace", 607, "I looked down at my window.", "R05",
 "I looked down at my window. Five weeks and three days, for work I had given eight months in May. Eight months had a lining in it and a full campaign of retouching. Five weeks could hold only what had to happen before she went back on a wall: the lifting paint laid down, the dirt and the brown varnish off, Wrobel off her face. The rest could come back to my studio in the summer. My right hand was going in its brace, very fine, a moth against a window."),
("replace", 623, "“Same scope as May,”", "R05",
 "“The May plan, first phase,” I said. “Consolidation, cleaning, the overpaint off the face. Lining and retouching next summer, on a separate letter.”"),
("replace", 624, "“Same scope of work,”", "R05",
 "“First phase,” Walter said, writing, and read it back."),
("replace", 625, "“The same fee as before.”", "R05",
 "“The fee for that phase, as it stood in May.”"),

# ---------------- R01: compress repeated instruction ----------------
# Ch 8 (first apprenticeship): keep tails, vise, yellow rule, log origin, craquelure; cut the unchanged recaps
("replace", 911, "“It’s low-tack tape, so it won’t lift anything", "R01",
 "“What you’re taking off is surface dirt,” she said. “A century of candles and coal smoke and people breathing. It sits on top of the varnish, and it comes off first, or everything after drags it around.”"),
("replace", 919, "“Like that, but lighter on the stick.", "R01",
 "“Lighter on the stick. Now turn it to a clean face and do it again.”"),
("delete", 923, "“How many passes before I change the swab?”", "R01", None),
("delete", 924, "“Until it’s gray, then a clean face.", "R01", None),
("delete", 951, "At ten past nine she dictated again,", "R01", None),
("delete", 952, "“No yellow,” he said, writing it.", "R01", None),
# Ch 9: the full operator formula again
("replace", 1079, "I sat back and dictated.", "R01",
 "I sat back and dictated the entry, the time and the area and the six applications of sixty seconds and the operator line, and then the only line I cared about. “Result: varnish fully reduced. Original paint layer intact.”"),
# Ch 12: the wine replay (already dramatized in Ch 2 and Ch 3); the Valley Forge reveal now lands once, in the scene with Maud
("replace", 1323, "September eleventh.", "R01",
 "September eleventh he had been through so many times, in bed, with the box fan going on the floor above him, that the three seconds with the corkscrew had worn smooth. The rest was a Thursday in October: the Turnpike at twenty to seven, the Valley Forge exit, and his own hand reaching over to turn up the radio."),
("delete", 1324, "One: Joan’s face, falling,", "R01", None),
("delete", 1325, "He had taken the corkscrew out of Cora’s hand.", "R01", None),
("delete", 1326, "That was the part he had told.", "R01", None),
("delete", 1327, "He had slept seven hours a night that week.", "R01", None),
("delete", 1328, "He had reached over and turned up the radio.", "R01", None),
# Ch 15: log and rule recap
("replace", 1747, "“Six-forty p.m.,” she read.", "R01",
 "“Six-forty p.m.,” she read. “Surface cleaning, area one, lower right, adjacent to the July test window. Operator D. Hale, under direct supervision of M. Alder, conservator, present throughout.” She went on through the pages without reading any more of it aloud, her finger stopping at each set of initials, and at the end of the gel tests she stopped altogether. “Who taught you to keep a log like this?”"),
("replace", 1763, "“He doesn’t fix anything", "R01",
 "“He stops when I say stop. When his hand’s tired he says so, and he stops. On the first Saturday he asked me what it looks like when it’s right.”"),
("replace", 1771, "“Six to ten on weeknights.", "R01",
 "“Four hours a night, ten on Saturdays, until the twenty-fourth.”"),
# Ch 17: dictation
("replace", 1918, "“Seven fifty-two p.m.,” I dictated.", "R01",
 "“Seven fifty-two p.m.,” I dictated. “Solvent tests, overpaint, Virgin’s left jaw at the edge of the veil. Four sites, three millimeters each. Site four, 1957 overpaint reduced. Original flesh tone present beneath. No loss.” Then the operator line, which he could have written by now without me."),
# Ch 19: mixing lesson -- drop the restated 'why it darkens' exchange (already said in 2228)
("delete", 2239, "“Why does it go darker when it dries?”", "R01/R02", None),
("delete", 2240, "“The resin sinks in", "R01/R02", None),
# Ch 26: section list already given in Ch 25's Mylar scene
("replace", 2942, "“There are six sections.”", "R01",
 "“There are six sections.” She turned a clear plastic sheet on the bench toward him with her left hand. Under it lay a photograph of the Virgin’s face, and over the face a map in black marker, the lines wandering a little, six shapes numbered in her capitals. “The jaw first, because I know it. The left brow last of all.”"),
# Ch 27: Frances's log recital before the hinge; one unchanged count
("replace", 2997, "She read with the glasses on the end of her nose", "R01",
 "She read with the glasses on the end of her nose, her finger down every margin. It took eleven minutes, and she read nothing aloud until the hinge."),
("delete", 2998, "“Three-ten p.m. Operator rest", "R01", None),
("delete", 2999, "“Yes.”", "R01", None),
("delete", 3000, "She turned on. “Seven fifty-two p.m.", "R01", None),
("delete", 3001, "“The third.”", "R01", None),
("replace", 3088, "He wiped the brush between sections", "R01",
 "He wiped the brush between sections and changed his swab before it was spent, and I counted him through it."),
("delete", 3089, "“Eighty, ninety. Clear.”", "R01", None),

# ---------------- R02: leave the image room; stop explaining it twice ----------------
# Ch 17: loosen the exact brow-to-scar correspondence (primary hypothetical DNF point)
("replace", 1989, "The 1957 brow was a perfect arch.", "R02",
 "The 1957 brow was a perfect arch. Wrobel had drawn it in one confident stroke, a sign painter’s line, the brow you put on a woman on a billboard for cold cream. Under raking light it should have been smooth, and it was smooth, but it wasn’t flat. At the outer end, where the brow ran in under the edge of the veil, the surface stepped down and up again over something, a small ragged break about six millimeters long, with the edge of older paint catching the light on either side. A knock from a candlestick, perhaps, or a flake that had come away in the first fifty years. Somebody had filled it, and Leon Wrobel had painted his perfect arch straight across the top as if it had never been there."),
("replace", 1990, "I wrote it down before I moved the lamp.", "R02",
 "I wrote it down before I moved the lamp. *Left brow, outer end at veil: old loss beneath 1957 fill, approx. 6 mm.*"),
("replace", 2866, "I laid the clear sheet over the photograph", "R02 (consistency)",
 "I laid the clear sheet over the photograph of the face I had taken on the third, under the raking light, and drew the sections in fine marker left-handed, the lines wandering where the hand wandered. There were six of them, the jaw first, where the test was, because it was the part of her I already knew. Then the right cheek, then the nose and the mouth together, because a mouth can’t be done in halves. Then the right eye and its brow. Then the left eye and cheek. Last, the left brow, from the arch to the edge of the veil, with the old scrape at its outer end in dotted line. Beside it I wrote in my leaning capitals, LEAVE."),
("replace", 2953, "He bent over the sheet.", "R02 (consistency)",
 "He bent over the sheet. At the outer end of the left brow, where it ran under the veil, there was a short dotted line, and beside it, in the same capitals, one word."),
("replace", 3140, "He was coming to it now.", "R02 (consistency)",
 "He was coming to it now, the old scrape at the end of the brow where it ran under the veil, where something had struck her between 1886 and 1957. Someone after that had filled it with a small brush and left it a little low, mended and left showing, and then Wrobel had covered all of it."),
("replace", 3156, "Across her left brow, under the veil,", "R02 (consistency)",
 "At the end of her left brow, under the edge of the veil, was an old break, mended and a little low."),
# Ch 23: the useful-hands diagnosis is narrated and then said aloud; keep it aloud (it changes the relationship)
("replace", 2645, "On the seventeenth of November I had stood at this bench", "R02",
 "On the seventeenth of November I had stood at this bench and told him the terms. I had called it payment and I had called it a schedule, and both of those were true. Under them, if you stayed on it, there was a third thing, and it had been there since the first night, when he took off his watch without being told. He was easy. He stood where I put him and asked me for nothing, and I came to the bench every evening at six to a pair of hands that wanted nothing from me but the next instruction."),
("delete", 2646, "*He never asked me for anything,*", "R02", None),
("delete", 2647, "I had built one.", "R02", None),
# Ch 25: Atlanta read as the same pattern, not an endorsed sacrifice; cut the restated self-diagnosis
("replace", 2860, "He had turned down Atlanta and not told me,", "R02",
 "He had turned down Atlanta and not told me. He had looked at what it would cost me, decided it for both of us, and paid it himself before I could see the bill. It was the corner again, done kindly. I would tell him so, to his face, and not today."),
("replace", 2861, "I had ended it on the thirteenth", "R02",
 "I need his hands, and I need him, and I am never going to get the two apart. I stopped trying on the floor of that corridor with a butter cookie in my good hand."),
# Ch 27: Frances's catechism answered the image the climax had already dramatized
("delete", 3177, "“Whose voice?”", "R02", None),
("delete", 3178, "“Mine.”", "R02", None),
("delete", 3180, "“Then it’s yours,” Frances said.", "R02", None),

# ---------------- R06: the absolute in Ch 23 ----------------
("replace", 2642, "His hands could do it.", "R06",
 "His hands could do it. I had watched them do the heel. On my voice, with my count, he could do all six sections and lift at every stop and leave the brow where it was. For four weeks he has done exactly what I said, except for one night I hinged into the book, and since that night he has done it better."),

# ---------------- R01/R03 timetable: the release is a deliberate professional risk ----------------
("insert_after", 2648, None, "R01 (timetable)",
 "That left me ten days. The face was one night’s work if the night was planned to the minute, and I could plan it with one hand. What I couldn’t do with one hand was the work, and I would not ask for his until I knew which I was asking for. If I didn’t know by the twenty-third, I would telephone Frances that morning and tell her not to come, and the parish would hang Helen Wrobel for one more Christmas, and I would sign my name to that as well."),
("replace", 2863, "I would ask him when I could count", "R01 (timetable)",
 "I would ask him when I could count her whole face aloud without a stumble, and not an hour before, and no later than the evening of the twenty-third, which left three and a half hours for him to learn it on the lighthouse before Frances came up in the cage. If I asked for his hands, they were not going to stand at that table waiting on my voice."),

# ---------------- R03: reciprocal adult choice ----------------
("replace", 3267, "“Next time I’ll tell you, and you decide.”", "R03",
 "“Next time I’ll tell you, and we decide it.”"),
("replace", 3268, "“Yes,” she said, as if she were writing it in the book.", "R03",
 "“We,” she said, as if she were writing it in the book."),
("replace", 3327, "“Whatever you tell me. A square inch. Slower.”", "R03",
 "“Learn it. Not to be your hands. I’d like to be good at something slow, and I’d like it to be this.”"),
("replace", 3337, "“I know you do. I knew in the chapel,", "R03",
 "“I know you do. I knew in the chapel, with my head on the bricks. That was never the part I couldn’t tell.” She drew a breath and let it go. “The evenings were never going to pay for the nine weeks. I’ve stopped wanting them to.”"),
# Ch 30: a non-work preference from him, a real difference, a negotiated choice
("replace", 3599, "“You tell her, she likes it better from you.”", "R03",
 "“You tell her, she likes it better from you.”"),
("insert_after", 3599, None, "R03",
 "“Easter is Grandfather,” I said. “I told Mrs. Tsang he’d be home by Easter.”"),
("insert_after", 3599, None, "R03",
 "“I know you did.” He turned the cup a quarter turn on his knee. “I want to go anyway. Both days, Saturday and Sunday, not up and back in an afternoon. I haven’t been home for Easter since I was running nights in Allentown. She does a ham with cloves in it, and I’d like to be there when she does it.”"),
("insert_after", 3599, None, "R03",
 "I had promised the Saturday before Easter to Grandfather, and he knew it, and he had asked anyway."),
("insert_after", 3599, None, "R03",
 "“Then I’ll ask Mrs. Tsang for one more week,” I said. “If she says no, I finish him on the Friday, and you drive me up after, and I sleep in the car.”"),
("insert_after", 3599, None, "R03",
 "“She’ll say yes.”"),
("insert_after", 3599, None, "R03",
 "“She’ll make me ask in person.”"),
("insert_after", 3599, None, "R03",
 "“Then ask her in person,” he said. “What time is your sister coming?”"),
]
