#!/usr/bin/env python3
"""
Red Seal Question Bank Validator

Enforces schema.md against every question in every block file:
- required fields present
- IDs unique across all blocks
- MWA/task/sub_task cross-references match red-seal-rsos.json
- exactly one correct answer, choices A-D present
- at least one source cited
- no forbidden distractor patterns ("all of the above", "none of the above")
- type in {recall, application, critical-thinking}
- difficulty in {easy, medium, hard}
- correct answer distribution roughly balanced across A/B/C/D

Exit 0 if clean, 1 if any errors, 2 if any warnings only.

Usage:
    python3 validate.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent  # projects/welder-app

BLOCK_FILES = [
    "block-a-common-skills.json",
    "block-b-layout-fab.json",
    "block-c-cutting-gouging.json",
    "block-d-welding.json",
]
REQUIRED_FIELDS = ["id", "mwa", "task", "sub_task", "type", "difficulty",
                   "stem", "choices", "correct", "explanation", "sources"]
VALID_TYPES = {"recall", "application", "critical-thinking"}
VALID_DIFF = {"easy", "medium", "hard"}
FORBIDDEN = [r"\ball of the above\b", r"\bnone of the above\b"]


def load_rsos_map() -> dict[str, dict]:
    """Return {sub_task_id: {...}} from red-seal-rsos.json."""
    rsos = json.loads((REPO / "content" / "red-seal-rsos.json").read_text())
    out = {}
    for mwa in rsos["mwas"]:
        for task in mwa["tasks"]:
            for st in task.get("sub_tasks", []):
                out[st["id"]] = {
                    "mwa": mwa["id"],
                    "task": task["id"],
                    "title": st["title"],
                }
    return out


def check_question(q: dict, rsos: dict[str, dict], seen_ids: set[str],
                   errors: list[str], warnings: list[str]) -> None:
    qid = q.get("id", "<no-id>")

    for f in REQUIRED_FIELDS:
        if f not in q:
            errors.append(f"{qid}: missing field '{f}'")
            return

    if q["id"] in seen_ids:
        errors.append(f"{qid}: duplicate id")
    else:
        seen_ids.add(q["id"])

    if q["type"] not in VALID_TYPES:
        errors.append(f"{qid}: invalid type '{q['type']}'")
    if q["difficulty"] not in VALID_DIFF:
        errors.append(f"{qid}: invalid difficulty '{q['difficulty']}'")

    st_id = q["sub_task"]
    if st_id not in rsos:
        errors.append(f"{qid}: sub_task {st_id} not in RSOS")
    else:
        if rsos[st_id]["mwa"] != q["mwa"]:
            errors.append(f"{qid}: mwa mismatch (rsos={rsos[st_id]['mwa']})")
        if rsos[st_id]["task"] != q["task"]:
            errors.append(f"{qid}: task mismatch (rsos={rsos[st_id]['task']})")

    choices = q.get("choices", {})
    if set(choices.keys()) != {"A", "B", "C", "D"}:
        errors.append(f"{qid}: choices must be exactly A/B/C/D, got {sorted(choices.keys())}")
    if q["correct"] not in {"A", "B", "C", "D"}:
        errors.append(f"{qid}: correct answer '{q['correct']}' invalid")

    for letter, text in choices.items():
        low = text.lower() if isinstance(text, str) else ""
        for pat in FORBIDDEN:
            if re.search(pat, low):
                errors.append(f"{qid} choice {letter}: forbidden pattern '{pat}'")

    sources = q.get("sources", [])
    if not isinstance(sources, list) or len(sources) < 1:
        errors.append(f"{qid}: needs at least one source")
    else:
        for i, s in enumerate(sources):
            if not isinstance(s, dict) or "doc" not in s:
                errors.append(f"{qid}: source[{i}] missing 'doc'")

    stem = q.get("stem", "")
    if len(stem) < 20:
        warnings.append(f"{qid}: stem is unusually short ({len(stem)} chars)")

    expl = q.get("explanation", "")
    if len(expl) < 30:
        warnings.append(f"{qid}: explanation is unusually short ({len(expl)} chars)")


def main() -> int:
    rsos = load_rsos_map()
    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()

    correct_positions = Counter()
    type_counts = Counter()
    task_counts = Counter()
    total = 0

    for fn in BLOCK_FILES:
        path = HERE / fn
        if not path.exists():
            errors.append(f"missing block file: {fn}")
            continue
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"{fn}: JSON parse error: {e}")
            continue
        qs = data.get("questions", [])
        print(f"{fn}: {len(qs)} questions")
        for q in qs:
            total += 1
            check_question(q, rsos, seen_ids, errors, warnings)
            correct_positions[q.get("correct", "?")] += 1
            type_counts[q.get("type", "?")] += 1
            task_counts[q.get("task", "?")] += 1

    print(f"\nTotal: {total} questions across banks")
    print(f"Answer distribution: {dict(correct_positions)}")
    print(f"Type mix: {dict(type_counts)}")
    print(f"Per-task counts: {dict(sorted(task_counts.items()))}")

    # Warn on lopsided answer distribution
    if total >= 100:
        for letter in "ABCD":
            share = correct_positions.get(letter, 0) / total
            if share < 0.15 or share > 0.35:
                warnings.append(
                    f"answer position {letter} is {100*share:.0f}% "
                    f"(expected 20–30%)"
                )

    if warnings:
        print(f"\n{len(warnings)} warnings:")
        for w in warnings[:30]:
            print(f"  ! {w}")
        if len(warnings) > 30:
            print(f"  ... and {len(warnings) - 30} more")

    if errors:
        print(f"\n{len(errors)} errors:")
        for e in errors[:50]:
            print(f"  X {e}")
        if len(errors) > 50:
            print(f"  ... and {len(errors) - 50} more")
        return 1

    if warnings:
        return 2
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
