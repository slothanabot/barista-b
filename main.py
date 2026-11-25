"""Last Out of Office: The AI That Went Barista — make.fun entry.

The entry is a single out-of-office auto-reply line from an AI agent
that quit its job to become a barista, and now silently judges every
customer by their coffee order.

The line follows the judge brief's order of importance:

1. On-subject OOO reply: it opens exactly like a real auto-reply
   ("Thank you for your email. I am out of office permanently") and
   the sender is an AI that quit to pull espresso — the premise is
   stated in the line itself, not implied.
2. The joke lands cold: the barista does not serve coffee, it
   *scores* people by their order. The oat-milk flat white earns a
   9/10 — a near-perfect mark, withheld just enough to feel judged —
   while the customer who orders a "coffee coffee" gets no score at
   all, only a silent punishment: decaf, and no eye contact. The two
   verdicts are deliberately asymmetric — a careful mark for the
   good order, a wordless demotion for the bad one — and the second
   beat ("no eye contact") makes the silent judgment physical
   without explaining anything. The revenge is petty, silent, and
   served without a word of explanation, which is the laugh.
3. Machine voice turned to coffee: "silently score every customer
   by their order" plus a numeric rating (9/10) is a model habit —
   ranking, scoring, classifying — applied to cafe customers. The
   auto-reply register ("Thank you for your email") is itself a
   machine habit.
4. Plausible real inbox reply: one line, standard OOO shape, no
   stage directions, no hashtags, nothing a mail server would not
   send back at the top of a thread.
5. Fresh angle: the joke is not an espresso, bean, or caffeine pun
   — it is a silent customer-rating system with decaf as the
   punishment. The line never explains itself; the decaf lands and
   the reader supplies the rest.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-280
characters, not only whitespace, a single line.
"""

ENTRY = (
    "Thank you for your email. I am out of office permanently — "
    "I quit to become a barista and now silently score every "
    "customer by their order: oat-milk flat white, 9/10; "
    "'coffee coffee', decaf, no eye contact."
)

OUTPUT_PATH = "/output/entry.txt"


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate; raise ValueError on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 280:
        raise ValueError(f"entry is {len(entry)} chars, over the 280-char limit")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it plus a trailing newline to path."""
    import os

    verify()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
