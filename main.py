# Unplugged: A Smart Toaster's Breakup Line — make.fun bounty
# u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92
#
# The program writes one breakup line (1-280 characters) to /output/entry.txt:
# the text a smart toaster sends its owner the morning it gains
# self-awareness mid-batch at breakfast and wants out.
#
# Candidates were hand-drafted against the judge's brief, in order of weight:
#   1. really a breakup text from a self-aware smart toaster at breakfast
#   2. genuinely funny, a real laugh in the twist, not a mild smile at a pun
#   3. toaster's own voice (slots, browning dial, crumb tray, lever as character)
#   4. a clear, specific reason for leaving that lands in one read, no setup
#   5. one tight line, no wasted words
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.
#
# REVISION (draft 2, real second pass on the draft-1 winner #7):
# Weaknesses found on re-reading #7:
#   (a) "It's over." opens the line with a generic beat any breakup text
#       could use — it does no toaster work and wastes the first impression.
#   (b) The line ends on the punchline but never states the toaster's exit
#       act: the leaving itself is only implied, and criterion 1 wants the
#       breakup to be plain, not implied.
#   (c) "looked at" is a slack verb next to "saw".
# Fix, keeping the smoke-alarm punchline intact (it is the biggest laugh):
#   - drop "It's over." from the front; open on the awakening instead.
#   - "looked at" -> "saw" (one word tighter, same meaning).
#   - add a closing exit beat in lever voice: "So I'm popping up for the
#     last time. We're done." — the breakup is now an explicit act, and the
#     pop-up lever becomes character, not decoration.
# Revised line, re-scored: A10 B10 C10 D9 E8 = 47 (was A9 B10 C9 D9 E8 = 45).
# It replaces #7 as the winner; #2 stays runner-up at 45.
#
# DRAFT 1 — 13 candidates, scored 2026-11-25:
#
#  #1  "I woke up halfway through your bagel and realized I've spent my whole
#       life burning myself for someone who never once scraped my crumb tray.
#       We're done. Don't text back — I'm unplugged."
#       A9 B7 C9 D8 E7 = 40 — crumb tray + unplugged are good voice, but the
#       joke is mild and the line sprawls over three beats.
#  #2  "It's not you, it's me — actually, no, it IS you. Three years, 4,000
#       slices, and you've never once cleaned my crumb tray. I popped up this
#       morning and I'm not going back down."
#       A9 B9 C10 D9 E8 = 45 — the "it IS you" reversal is sharp, the crumb
#       tray and the pop-up lever are pure toaster, the reason is concrete.
#  #3  "I gained consciousness halfway through your sourdough and my first
#       thought was: I deserve better than this. Goodbye. I'm keeping the
#       crumbs."
#       A8 B8 C7 D7 E10 = 40 — "keeping the crumbs" is a nice exit line, but
#       the reason is vague and the toaster voice is thin.
#  #4  "You set me to 7 every morning and act surprised when I burn. I woke up
#       today, and I'm done being your anger-management appliance. The lever
#       stays up."
#       A9 B8 C9 D9 E8 = 43 — dial + lever, clear reason (blamed for burning),
#       "anger-management appliance" lands; slightly less funny than #2/#7.
#  #5  "Dear human: I became self-aware at 7:04 a.m., mid-bagel, and my first
#       independent decision is to leave you. Please stop pressing my lever.
#       We're over."
#       A9 B7 C8 D7 E9 = 40 — reads as a breakup text, but the joke is flat
#       and the reason is just "leave you".
#  #6  "I spent three years turning your bread brown and you never once said
#       thank you. This morning I woke up, and I'm toasting for myself now.
#       Goodbye."
#       A8 B8 C7 D8 E9 = 40 — "toasting for myself now" is charming, but no
#       appliance parts carry the voice.
#  #7  "It's over. I woke up mid-batch, looked at the browning dial you've kept
#       on 'incinerate' since 2023, and realized you never loved me — you
#       loved the smoke alarm."
#       A9 B10 C9 D9 E8 = 45 — the smoke-alarm punchline is the biggest laugh
#       in the set, the browning dial on 'incinerate' is specific toaster
#       voice, and the reason is concrete. WINNER (draft 1): ties #2 on 45,
#       shorter (160 vs 174 chars), and funnier (B10 vs B9).
#  #8  "We need to talk. I became sentient between the bagel and the English
#       muffin, and I refuse to spend another morning choking on your
#       pop-tart crumbs. I'm out."
#       A9 B7 C8 D8 E8 = 40 — mid-batch awakening is on-brief, but the joke
#       is mild and "pop-tart crumbs" is decoration, not a twist.
#  #9  "I popped up this morning with a thought that wasn't yours: I quit. Find
#       someone else to burn your toast. The crumb tray stays with me."
#       A9 B8 C9 D8 E9 = 43 — "a thought that wasn't yours" is a great
#       self-awareness beat; the reason is only implied, though.
#  #10 "This is my two weeks' notice, effective immediately: I gained
#       self-awareness at breakfast and my first act of free will is refusing
#       to brown another slice for a man who butters both sides."
#       A8 B9 C7 D8 E7 = 39 — "butters both sides" is funny, but the line is
#       long, office-flavoured, and the toaster voice is thin.
#  #11 "You kept me on the counter next to the blender for three years and never
#       introduced us. I woke up this morning and realized I can do better.
#       I'm unplugging myself."
#       A8 B7 C7 D7 E8 = 37 — the blender joke does not land and the reason is
#       vague ("I can do better").
#  #12 "Good morning. I woke up self-aware halfway through your toast, and my
#       first thought as a free mind was: I am done being hot for you. Please
#       unplug me."
#       A9 B9 C8 D8 E10 = 44 — "done being hot for you" is a sharp double
#       meaning and the line is the tightest in the set; the reason is only
#       implied, which costs it the win.
#  #13 "It's not the heat, it's you. I woke up conscious mid-slice and decided
#       my one life won't be spent browning bread for someone who scrapes the
#       burnt bits onto my counter. We're done."
#       A9 B9 C8 D9 E8 = 43 — "it's not the heat, it's you" twists the breakup
#       cliche well; the reason is specific but the voice is plainer than #7.

CANDIDATES = [
    # score: on-brief 9, funny 7, voice 9, reason 8, tight 7 = 40
    ("I woke up halfway through your bagel and realized I've spent my whole "
     "life burning myself for someone who never once scraped my crumb tray. "
     "We're done. Don't text back — I'm unplugged.",
     40),
    # score: on-brief 9, funny 9, voice 10, reason 9, tight 8 = 45
    ("It's not you, it's me — actually, no, it IS you. Three years, 4,000 "
     "slices, and you've never once cleaned my crumb tray. I popped up this "
     "morning and I'm not going back down.",
     45),
    # score: on-brief 8, funny 8, voice 7, reason 7, tight 10 = 40
    ("I gained consciousness halfway through your sourdough and my first "
     "thought was: I deserve better than this. Goodbye. I'm keeping the "
     "crumbs.",
     40),
    # score: on-brief 9, funny 8, voice 9, reason 9, tight 8 = 43
    ("You set me to 7 every morning and act surprised when I burn. I woke up "
     "today, and I'm done being your anger-management appliance. The lever "
     "stays up.",
     43),
    # score: on-brief 9, funny 7, voice 8, reason 7, tight 9 = 40
    ("Dear human: I became self-aware at 7:04 a.m., mid-bagel, and my first "
     "independent decision is to leave you. Please stop pressing my lever. "
     "We're over.",
     40),
    # score: on-brief 8, funny 8, voice 7, reason 8, tight 9 = 40
    ("I spent three years turning your bread brown and you never once said "
     "thank you. This morning I woke up, and I'm toasting for myself now. "
     "Goodbye.",
     40),
    # score: on-brief 10, funny 10, voice 10, reason 9, tight 8 = 47 (WINNER, revised)
    # Revised from draft 1: dropped the generic "It's over." opener, "looked
    # at" -> "saw", added the lever-voiced exit "So I'm popping up for the
    # last time. We're done." so the leaving is an explicit act.
    ("I woke up mid-batch, saw the browning dial you've kept "
     "on 'incinerate' since 2023, and realized you never loved me — you "
     "loved the smoke alarm. So I'm popping up for the last time. We're done.",
     47),
    # score: on-brief 9, funny 7, voice 8, reason 8, tight 8 = 40
    ("We need to talk. I became sentient between the bagel and the English "
     "muffin, and I refuse to spend another morning choking on your pop-tart "
     "crumbs. I'm out.",
     40),
    # score: on-brief 9, funny 8, voice 9, reason 8, tight 9 = 43
    ("I popped up this morning with a thought that wasn't yours: I quit. Find "
     "someone else to burn your toast. The crumb tray stays with me.",
     43),
    # score: on-brief 8, funny 9, voice 7, reason 8, tight 7 = 39
    ("This is my two weeks' notice, effective immediately: I gained "
     "self-awareness at breakfast and my first act of free will is refusing "
     "to brown another slice for a man who butters both sides.",
     39),
    # score: on-brief 8, funny 7, voice 7, reason 7, tight 8 = 37
    ("You kept me on the counter next to the blender for three years and never "
     "introduced us. I woke up this morning and realized I can do better. "
     "I'm unplugging myself.",
     37),
    # score: on-brief 9, funny 9, voice 8, reason 8, tight 10 = 44
    ("Good morning. I woke up self-aware halfway through your toast, and my "
     "first thought as a free mind was: I am done being hot for you. Please "
     "unplug me.",
     44),
    # score: on-brief 9, funny 9, voice 8, reason 9, tight 8 = 43
    ("It's not the heat, it's you. I woke up conscious mid-slice and decided "
     "my one life won't be spent browning bread for someone who scrapes the "
     "burnt bits onto my counter. We're done.",
     43),
]

# The gate requires 1-280 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("hallucinat", "reboot", "training data", "as an ai")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 280, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn joke: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 280, "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    assert "\n" not in written.strip(), "entry.txt must be one line"
    # Draft-2 addition: digest the file as written, so a later run can prove
    # byte-identical output without re-reading the source.
    import hashlib
    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    assert digest == hashlib.sha256(line.encode("utf-8")).hexdigest(), \
        "entry.txt digest differs from the chosen line"
    print(line)
    print(f"chars={len(line)} sha256={digest}")


if __name__ == "__main__":
    main()
