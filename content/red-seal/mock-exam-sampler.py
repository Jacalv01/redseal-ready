#!/usr/bin/env python3
"""
Red Seal Welder Mock Exam Sampler

Draws a 125-question mock exam from the block banks using the exact
task weighting specified in the RSOS 2023 blueprint.

Usage:
    python3 mock-exam-sampler.py [--seed N] [--out mock-exam-NNN.json]

The output is a shuffled 125-Q exam ready for delivery in the iOS app.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Task-level exam weighting (must match red-seal-rsos.json exactly)
TASK_WEIGHTS = {
    "A-1": 4, "A-2": 3, "A-3": 4, "A-4": 3, "A-5": 6,  # A-6 = 0
    "B-7": 12, "B-8": 16,
    "C-9": 6, "C-10": 7, "C-11": 6, "C-12": 4,
    "D-13": 18, "D-14": 18, "D-15": 13, "D-16": 5,
}
BLOCK_FILES = {
    "A": "block-a-common-skills.json",
    "B": "block-b-layout-fab.json",
    "C": "block-c-cutting-gouging.json",
    "D": "block-d-welding.json",
}


def load_bank() -> dict[str, list[dict]]:
    """Return {task_id: [questions...]} grouped from all block files."""
    by_task: dict[str, list[dict]] = {t: [] for t in TASK_WEIGHTS}
    for block_id, filename in BLOCK_FILES.items():
        path = HERE / filename
        if not path.exists():
            print(f"[warn] missing bank file: {path}", file=sys.stderr)
            continue
        data = json.loads(path.read_text())
        for q in data.get("questions", []):
            task = q.get("task")
            if task in by_task:
                by_task[task].append(q)
            else:
                print(f"[warn] question {q.get('id')} has unknown task {task}", file=sys.stderr)
    return by_task


def build_exam(by_task: dict[str, list[dict]], rng: random.Random) -> list[dict]:
    """Draw a weighted 125-Q exam. Raises if any task is under-supplied."""
    exam = []
    for task_id, count in TASK_WEIGHTS.items():
        pool = by_task[task_id]
        if len(pool) < count:
            raise ValueError(
                f"Task {task_id}: need {count} questions, bank has only {len(pool)}"
            )
        exam.extend(rng.sample(pool, count))
    rng.shuffle(exam)
    assert len(exam) == 125, f"Exam length {len(exam)} != 125"
    return exam


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--out", type=str, default=None,
                    help="Write exam JSON to this path (default: stdout summary only)")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    by_task = load_bank()

    # Coverage report
    print("Bank coverage:")
    total_bank = 0
    short = False
    for task_id, count in TASK_WEIGHTS.items():
        have = len(by_task[task_id])
        total_bank += have
        marker = "OK " if have >= count * 3 else ("min" if have >= count else "SHORT")
        if marker == "SHORT":
            short = True
        print(f"  {task_id:6s} need {count:2d}  have {have:3d}  [{marker}]")
    print(f"  TOTAL         have {total_bank}")
    if short:
        print("\n[error] Bank is under-supplied for one or more tasks; cannot build exam.",
              file=sys.stderr)
        return 1

    exam = build_exam(by_task, rng)

    # Type mix report
    type_counts: dict[str, int] = {}
    for q in exam:
        type_counts[q.get("type", "unknown")] = type_counts.get(q.get("type", "unknown"), 0) + 1
    print("\nSampled exam type mix:")
    for t, n in sorted(type_counts.items()):
        print(f"  {t:20s} {n:3d} ({100*n/125:.0f}%)")

    if args.out:
        out_path = Path(args.out)
        out_path.write_text(json.dumps({
            "exam_type": "red-seal-mock",
            "trade": "welder",
            "total_questions": 125,
            "pass_mark_pct": 70,
            "duration_hours": 4,
            "seed": args.seed,
            "questions": exam,
        }, indent=2))
        print(f"\nWrote exam to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
