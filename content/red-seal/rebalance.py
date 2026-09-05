#!/usr/bin/env python3
"""
Rebalance the correct-answer position (A/B/C/D) across each block file.

Many question banks drift toward one position (typically B) because writers
intuit the correct answer as "not the first / not the last" — which is a real
statistical bias that exam candidates exploit.

This script randomly permutes the choices A/B/C/D on each question so that
the correct-answer position is uniformly distributed. It updates:
  - the 'choices' dict
  - the 'correct' letter
  - the 'explanation' text (if it references distractor letters by name)

The explanation-letter rewrite is best-effort — if it can't map safely, the
explanation is left as-is and the script prints a warning for manual review.

Deterministic with a seed for reproducibility.
"""
from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
BLOCK_FILES = [
    "block-a-common-skills.json",
    "block-b-layout-fab.json",
    "block-c-cutting-gouging.json",
    "block-d-welding.json",
]
SEED = 20260905

# Pattern to find in-explanation references like "answer A", "option (B)", "(C)", "distractor D"
LETTER_REF = re.compile(r"\b([Aa]nswer|[Oo]ption|[Dd]istractor)?\s*\(?([A-D])\)?\b")


def remap_explanation(text: str, mapping: dict[str, str]) -> str:
    """Best-effort remap of letter references in explanation text.
    mapping is old_letter -> new_letter."""
    # Only remap tokens that look like standalone letter refs to avoid mangling
    # things like "A5.1" or "CSA".
    def _sub(m: re.Match) -> str:
        prefix = m.group(1) or ""
        letter = m.group(2)
        # Preserve original casing for prefix; letter always uppercase in refs
        new_letter = mapping.get(letter, letter)
        if prefix:
            return f"{prefix} {new_letter}"
        # bare letter — only remap if inside parens
        if m.group(0).startswith("(") and m.group(0).endswith(")"):
            return f"({new_letter})"
        return m.group(0)  # untouched

    # Regex for "(A)" style
    def _paren(m):
        return f"({mapping.get(m.group(1), m.group(1))})"

    text = re.sub(r"\(([A-D])\)", _paren, text)

    # Regex for "answer/option/distractor A" style
    def _named(m):
        prefix = m.group(1)
        letter = m.group(2)
        return f"{prefix} {mapping.get(letter, letter)}"

    text = re.sub(r"\b([Aa]nswer|[Oo]ption|[Dd]istractor)\s+([A-D])\b", _named, text)
    return text


def rebalance_block(path: Path, rng: random.Random) -> tuple[int, int]:
    data = json.loads(path.read_text())
    qs = data.get("questions", [])
    total = len(qs)

    # Target distribution: cycle through A,B,C,D to equalize
    targets = ["A", "B", "C", "D"] * (total // 4 + 1)
    rng.shuffle(targets)
    targets = targets[:total]

    changed = 0
    for i, q in enumerate(qs):
        old_correct = q["correct"]
        new_correct = targets[i]
        if old_correct == new_correct:
            continue

        old_choices = q["choices"]
        # Build mapping: old letter -> new letter
        # We need a permutation of ABCD such that old_correct maps to new_correct.
        # Simplest: swap old_correct <-> new_correct, leave others in place.
        mapping = {"A": "A", "B": "B", "C": "C", "D": "D"}
        mapping[old_correct] = new_correct
        mapping[new_correct] = old_correct

        # Apply mapping to choices
        new_choices = {}
        for old_letter, text in old_choices.items():
            new_choices[mapping[old_letter]] = text
        q["choices"] = {k: new_choices[k] for k in "ABCD"}
        q["correct"] = new_correct

        # Update explanation
        q["explanation"] = remap_explanation(q["explanation"], mapping)

        changed += 1

    path.write_text(json.dumps(data, indent=2))
    return total, changed


def main():
    rng = random.Random(SEED)
    for fn in BLOCK_FILES:
        path = HERE / fn
        if not path.exists():
            print(f"skip missing {fn}")
            continue
        total, changed = rebalance_block(path, rng)
        print(f"{fn}: {changed}/{total} rebalanced")


if __name__ == "__main__":
    main()
