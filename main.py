#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — glow-in-the-dark petunias.

Writes a single sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell, to
/output/entry.txt.

The pitch: petunias bred to glow in the dark, so a garden lights itself at
night. Ridiculous at first glance — a plant as a lamp — yet real by the
second: homeowners already spend a fortune on outdoor lighting that rusts,
shorts and dies in the rain, and a self-lighting plant replaces it. The
sentence names the odd thing being sold (glowing petunias), who pays for it
(homeowners) and why it holds together (it replaces the lamps they already
buy).

Standard library only. Deterministic: the same bytes on every run.
"""

import os

# Sentence parts, joined by build_sentence(). Keeping the claim, the
# audience and the reason as separate clauses makes the pitch easy to
# audit: each part maps to one requirement of the brief.
CLAIM = "We breed petunias that glow in the dark"
PROMISE = "so your garden lights itself at night"
REASON = (
    "because homeowners already spend a fortune on outdoor lamps "
    "that rust, short and die in the rain"
)


def build_sentence() -> str:
    """Assemble the pitch from its three clauses."""
    parts = [CLAIM, PROMISE + ",", REASON + "."]
    return " ".join(parts)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(build_sentence() + "\n")


if __name__ == "__main__":
    main()
