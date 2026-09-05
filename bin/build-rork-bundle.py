#!/usr/bin/env python3
"""
Build a single-file bundle for Rork/other content-consuming tools.

Emits welder-app-content-bundle.json in the project root with:
- meta (build timestamp, versions, source repo)
- index (navigable list of every lesson + question bank)
- lessons: period → section → topic → { markdown, sources[] }
- red_seal: full question banks + task blueprint from RSOS

Also emits welder-app-content-bundle.md — a human-readable single-file
version with the same content as Markdown (for tools that prefer text).
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUT_JSON = ROOT / "welder-app-content-bundle.json"
OUT_MD = ROOT / "welder-app-content-bundle.md"


def scan_lessons() -> dict:
    lessons: dict = {}
    for period_dir in sorted(CONTENT.glob("period*")):
        period_key = period_dir.name  # period1, period2, period3
        lessons[period_key] = {}
        for section_dir in sorted(period_dir.glob("section*")):
            section_key = section_dir.name  # section1..sectionN
            lessons[period_key][section_key] = {}
            for md in sorted(section_dir.glob("*.md")):
                topic_key = md.stem  # topic-a-...
                lessons[period_key][section_key][topic_key] = {
                    "path": str(md.relative_to(ROOT)),
                    "markdown": md.read_text(),
                }
    return lessons


def scan_red_seal() -> dict:
    rsos = json.loads((CONTENT / "red-seal-rsos.json").read_text())
    ait = json.loads((CONTENT / "ait-curriculum.json").read_text())
    banks = {}
    for f in [
        "block-a-common-skills.json",
        "block-b-layout-fab.json",
        "block-c-cutting-gouging.json",
        "block-d-welding.json",
    ]:
        data = json.loads((CONTENT / "red-seal" / f).read_text())
        banks[data["block"]] = data
    mock = json.loads((CONTENT / "red-seal" / "mock-exam-sample.json").read_text())
    return {
        "rsos_blueprint": rsos,
        "ait_curriculum": ait,
        "question_banks": banks,
        "sample_mock_exam": mock,
    }


def scan_calculators() -> list[dict]:
    calcs = []
    calc_dir = CONTENT / "calculators"
    if not calc_dir.exists():
        return calcs
    for f in sorted(calc_dir.glob("*.json")):
        calcs.append(json.loads(f.read_text()))
    return calcs


def scan_exam_traps() -> dict:
    trap_file = CONTENT / "exam-traps.json"
    if not trap_file.exists():
        return {}
    return json.loads(trap_file.read_text())


def scan_visuals() -> list[dict]:
    """Return {id, path, filename} for each SVG asset."""
    visual_dir = ROOT / "assets" / "visuals"
    out = []
    if not visual_dir.exists():
        return out
    for f in sorted(visual_dir.glob("*.svg")):
        out.append({
            "id": f.stem,
            "path": str(f.relative_to(ROOT)),
            "bytes": f.stat().st_size,
        })
    return out


def build_index(lessons: dict, red_seal: dict, calculators: list, exam_traps: dict, visuals: list) -> list[dict]:
    idx = []
    for period, sections in lessons.items():
        for section, topics in sections.items():
            for topic, payload in topics.items():
                title = topic.replace("topic-", "").replace("-", " ").strip()
                # first heading is the real title
                m = re.search(r"^# (.+)$", payload["markdown"], re.MULTILINE)
                if m:
                    title = m.group(1).strip()
                idx.append({
                    "kind": "lesson",
                    "period": period,
                    "section": section,
                    "topic": topic,
                    "title": title,
                    "chars": len(payload["markdown"]),
                })
    for block_id, bank in red_seal["question_banks"].items():
        idx.append({
            "kind": "question_bank",
            "block": block_id,
            "title": bank["title"],
            "exam_weight_pct": bank["exam_weight_pct"],
            "exam_questions_on_test": bank["exam_questions_on_test"],
            "questions": len(bank["questions"]),
        })
    for c in calculators:
        idx.append({
            "kind": "calculator",
            "id": c["id"],
            "title": c["title"],
        })
    if exam_traps:
        idx.append({
            "kind": "exam_traps_collection",
            "title": exam_traps.get("meta", {}).get("title", "Exam Traps"),
            "count": len(exam_traps.get("traps", [])),
        })
    for v in visuals:
        idx.append({
            "kind": "visual_asset",
            "id": v["id"],
            "path": v["path"],
        })
    return idx


def build_meta(lessons: dict, red_seal: dict) -> dict:
    lesson_count = sum(
        len(topics)
        for sections in lessons.values()
        for topics in sections.values()
    )
    q_count = sum(len(b["questions"]) for b in red_seal["question_banks"].values())
    return {
        "schema": "redseal-ready.content-bundle.v1",
        "trade": "welder",
        "jurisdiction": "Canada (Alberta AIT + Red Seal)",
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_repo": "github.com/Jacalv01/redseal-ready",
        "lesson_count": lesson_count,
        "question_count": q_count,
        "periods": list(lessons.keys()),
        "red_seal_blocks": list(red_seal["question_banks"].keys()),
        "curriculum_source": "Alberta AIT Welder Curriculum Guide 012 (2026 edition)",
        "exam_source": "Red Seal Occupational Standard for Welder (2023)",
        "content_rules": [
            "Every technical claim cited to allowed sources (RSOS, AIT, CSA W47.1/W59/B51, AWS, CWB, Modern Welding, Miller/Lincoln/ESAB/Hypertherm/ArcAir, TWI, ASME, WHMIS)",
            "No exam questions reconstructed from real Red Seal exam (protected content)",
            "No fabricated specs without cited source",
        ],
    }


def build_bundle() -> dict:
    lessons = scan_lessons()
    red_seal = scan_red_seal()
    calculators = scan_calculators()
    exam_traps = scan_exam_traps()
    visuals = scan_visuals()
    bundle = {
        "meta": build_meta(lessons, red_seal),
        "index": build_index(lessons, red_seal, calculators, exam_traps, visuals),
        "lessons": lessons,
        "red_seal": red_seal,
        "calculators": calculators,
        "exam_traps": exam_traps,
        "visuals": visuals,
    }
    bundle["meta"]["calculator_count"] = len(calculators)
    bundle["meta"]["exam_trap_count"] = len(exam_traps.get("traps", []))
    bundle["meta"]["visual_asset_count"] = len(visuals)
    return bundle


def bundle_to_markdown(bundle: dict) -> str:
    """Render the bundle as one long Markdown document."""
    parts = []
    meta = bundle["meta"]
    parts.append(f"# Welder Apprenticeship & Red Seal — Content Bundle\n")
    parts.append(f"_Generated {meta['generated_at']} from {meta['source_repo']}._\n")
    parts.append(f"- **Trade:** {meta['trade']}")
    parts.append(f"- **Jurisdiction:** {meta['jurisdiction']}")
    parts.append(f"- **Lesson count:** {meta['lesson_count']}")
    parts.append(f"- **Question count:** {meta['question_count']}")
    parts.append(f"- **Curriculum source:** {meta['curriculum_source']}")
    parts.append(f"- **Exam source:** {meta['exam_source']}\n")
    parts.append("## Content rules\n")
    for rule in meta["content_rules"]:
        parts.append(f"- {rule}")
    parts.append("")

    parts.append("---\n\n# Part 1 — Apprenticeship lessons\n")
    for period_key in sorted(bundle["lessons"].keys()):
        period_num = period_key.replace("period", "")
        parts.append(f"\n## Period {period_num}\n")
        for section_key in sorted(bundle["lessons"][period_key].keys()):
            section_num = section_key.replace("section", "")
            parts.append(f"\n### Period {period_num} — Section {section_num}\n")
            for topic_key, payload in sorted(bundle["lessons"][period_key][section_key].items()):
                parts.append(f"\n#### `{payload['path']}`\n")
                parts.append(payload["markdown"])
                parts.append("\n")

    parts.append("---\n\n# Part 2 — Calculators\n")
    if bundle.get("calculators"):
        for c in bundle["calculators"]:
            parts.append(f"\n### `{c['id']}` — {c['title']}\n")
            parts.append(f"_{c.get('subtitle', '')}_\n")
            parts.append(f"**Formula:** `{c.get('formula_display', c.get('formula_expr', ''))}`\n")
            if 'notes' in c:
                parts.append(f"\n{c['notes']}\n")

    parts.append("\n---\n\n# Part 3 — Common exam traps\n")
    if bundle.get("exam_traps"):
        for trap in bundle["exam_traps"].get("traps", []):
            parts.append(f"\n### ⚠ {trap['topic']} — {trap['id']}")
            parts.append(f"\n**When:** {trap['when']}")
            parts.append(f"\n**Wrong assumption:** {trap['wrong_assumption']}")
            parts.append(f"\n**Correct rule:** {trap['correct_rule']}")
            parts.append(f"\n**Memory hook:** {trap['memory_hook']}\n")

    parts.append("\n---\n\n# Part 4 — Visual assets\n")
    if bundle.get("visuals"):
        for v in bundle["visuals"]:
            parts.append(f"- `{v['path']}` ({v['bytes']} bytes)")

    parts.append("\n---\n\n# Part 5 — Red Seal question bank\n")
    parts.append("\n## Blueprint\n")
    rsos = bundle["red_seal"]["rsos_blueprint"]
    parts.append(f"- Exam total: {rsos['exam']['total_questions']} MCQ")
    parts.append(f"- Pass mark: {rsos['exam']['pass_mark_pct']}%")
    parts.append(f"- Duration: {rsos['exam']['duration_hours']}h")
    parts.append("\n### Task weighting\n")
    parts.append("| Block | MWA | Task | Weight % | Exam Q |")
    parts.append("|---|---|---|---|---|")
    for mwa in rsos["mwas"]:
        for task in mwa["tasks"]:
            parts.append(
                f"| {mwa['id']} | {mwa['title']} | {task['id']} {task['title']} "
                f"| {task['task_weight_pct']}% | {task['exam_questions']} |"
            )

    parts.append("\n## Question banks\n")
    for block_id in sorted(bundle["red_seal"]["question_banks"].keys()):
        bank = bundle["red_seal"]["question_banks"][block_id]
        parts.append(f"\n### Block {block_id}: {bank['title']}")
        parts.append(f"({bank['exam_weight_pct']}% of exam · {bank['exam_questions_on_test']} exam Q · {len(bank['questions'])} in bank)\n")
        for q in bank["questions"]:
            parts.append(f"\n#### {q['id']} — [{q['type']} · {q['difficulty']}] — sub-task {q['sub_task']}")
            parts.append(f"\n**Q:** {q['stem']}\n")
            for letter in "ABCD":
                marker = " ← correct" if q["correct"] == letter else ""
                parts.append(f"- **{letter}.** {q['choices'][letter]}{marker}")
            parts.append(f"\n**Explanation:** {q['explanation']}\n")
            src = "; ".join(f"{s['doc']} — {s.get('ref','')}" for s in q["sources"])
            parts.append(f"**Sources:** {src}\n")

    return "\n".join(parts)


def main() -> int:
    bundle = build_bundle()
    OUT_JSON.write_text(json.dumps(bundle, indent=2))
    OUT_MD.write_text(bundle_to_markdown(bundle))
    print(f"Wrote {OUT_JSON.relative_to(ROOT)} ({OUT_JSON.stat().st_size/1024:.0f} KB)")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}   ({OUT_MD.stat().st_size/1024:.0f} KB)")
    print(f"Lessons: {bundle['meta']['lesson_count']}")
    print(f"Questions: {bundle['meta']['question_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
