#!/usr/bin/env python3
"""
Extract structured AIT Welder curriculum from the extracted PDF text.

Input:  research/ait-course-content-extracted.txt
Output: content/ait-curriculum.json

Structure:
{
  "source": "AIT Welder Curriculum Guide 012 (2026)",
  "periods": [
    {
      "number": 1,
      "total_hours": 240,
      "sections": [
        {
          "number": 1,
          "title": "Foundational Skills, Safety and Procedures",
          "hours": 70,
          "weight_pct": 29,
          "topics": [
            {
              "letter": "A",
              "title": "Welder Apprenticeship Training Program Orientation",
              "hours": 2,
              "weight_pct": 1,
              "outcome": "...",
              "objectives": ["...", "..."]
            }
          ]
        }
      ]
    }
  ]
}
"""
import re
import json
from pathlib import Path

SRC = Path(__file__).parent.parent / "research" / "ait-course-content-extracted.txt"
OUT = Path(__file__).parent.parent / "content" / "ait-curriculum.json"

TEXT = SRC.read_text()

# Split by period
period_pattern = re.compile(r"Period (One|Two|Three)\s*\nCourse Content", re.MULTILINE)
period_names = {"One": 1, "Two": 2, "Three": 3}

# Find period start positions
period_starts = [(m.group(1), m.start()) for m in period_pattern.finditer(TEXT)]

periods = []

for i, (name, start) in enumerate(period_starts):
    end = period_starts[i + 1][1] if i + 1 < len(period_starts) else len(TEXT)
    block = TEXT[start:end]
    period_num = period_names[name]

    # Split into sections. Section headers look like:
    # "Section One: Foundational Skills, Safety and Procedures"
    section_pattern = re.compile(
        r"Section (One|Two|Three|Four|Five):\s*([^\n]+)", re.MULTILINE
    )
    section_names = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    section_matches = list(section_pattern.finditer(block))
    # First match is often in the summary table; the real section header appears again later.
    # We want the SECOND occurrence of each section as the actual content start.
    seen = {}
    real_starts = []
    for m in section_matches:
        num = section_names[m.group(1)]
        seen.setdefault(num, []).append(m)
    for num in sorted(seen):
        matches = seen[num]
        # Use the last occurrence (the actual section content start, not the TOC entry)
        real_starts.append((num, matches[-1]))

    sections = []
    for idx, (num, sm) in enumerate(real_starts):
        sec_start = sm.start()
        sec_end = real_starts[idx + 1][1].start() if idx + 1 < len(real_starts) else len(block)
        sec_block = block[sec_start:sec_end]
        title_raw = sm.group(2).strip()
        # Clean multi-line titles (some wrap)
        title = re.sub(r"\s+", " ", title_raw).strip()

        # Look up section hours/weight from the summary table earlier in the period block
        # Pattern: "Section One: Foundational Skills, Safety and Procedures 70 hrs 29%"
        summary_match = re.search(
            rf"Section {['','One','Two','Three','Four','Five'][num]}:\s*[^\n]*?(\d+)\s*hrs\s*(\d+)%",
            block[: sm.start()],
            re.MULTILINE,
        )
        sec_hours = int(summary_match.group(1)) if summary_match else None
        sec_weight = int(summary_match.group(2)) if summary_match else None

        # Extract topics. Topic headers look like: "Topic A. Some Title"
        topic_pattern = re.compile(
            r"Topic ([A-Z])\.\s+([^\n]+?)\s*\nWeighting\s*\n(\d+)\s*Hours?\s*(\d+)%",
            re.MULTILINE,
        )
        topics = []
        topic_matches = list(topic_pattern.finditer(sec_block))
        for ti, tm in enumerate(topic_matches):
            t_start = tm.end()
            t_end = topic_matches[ti + 1].start() if ti + 1 < len(topic_matches) else len(sec_block)
            t_block = sec_block[t_start:t_end]

            # Outcome (optional): "Outcome: Upon successful completion..."
            outcome_match = re.search(
                r"Outcome:\s*(.+?)(?=\n\s*Objectives:|\n\s*Topic |\Z)",
                t_block,
                re.DOTALL,
            )
            outcome = None
            if outcome_match:
                outcome = re.sub(r"\s+", " ", outcome_match.group(1)).strip()

            # Objectives: numbered list
            obj_section_match = re.search(
                r"Objectives:\s*(.+?)(?=\n\s*Topic |\n\s*Section |\Z)",
                t_block,
                re.DOTALL,
            )
            objectives = []
            if obj_section_match:
                obj_text = obj_section_match.group(1)
                # Match numbered items: "1. foo bar\n2. baz"
                obj_items = re.split(r"\n\s*(\d+)\.\s+", "\n" + obj_text)
                # obj_items structure: ['', '1', 'text', '2', 'text', ...]
                for j in range(1, len(obj_items) - 1, 2):
                    obj = re.sub(r"\s+", " ", obj_items[j + 1]).strip()
                    # Trim trailing noise like page headers
                    obj = re.sub(r"===\s*PAGE.*", "", obj).strip()
                    obj = re.sub(r"PERIOD (ONE|TWO|THREE).*", "", obj).strip()
                    obj = re.sub(r"Classification: Public.*", "", obj).strip()
                    if obj:
                        objectives.append(obj)

            topics.append({
                "letter": tm.group(1),
                "title": tm.group(2).strip(),
                "hours": int(tm.group(3)),
                "weight_pct": int(tm.group(4)),
                "outcome": outcome,
                "objectives": objectives,
            })

        sections.append({
            "number": num,
            "title": title,
            "hours": sec_hours,
            "weight_pct": sec_weight,
            "topics": topics,
        })

    periods.append({
        "number": period_num,
        "total_hours": 240,
        "sections": sections,
    })

result = {
    "source": "Alberta AIT Welder Curriculum Guide 012 (2026)",
    "source_url": "https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF",
    "isbn": "978-1-4601-6513-3",
    "extracted": "2026-09-04",
    "periods": periods,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2))

# Print summary
print(f"Extracted to {OUT}")
for p in periods:
    total_topics = sum(len(s["topics"]) for s in p["sections"])
    total_objectives = sum(
        len(t["objectives"]) for s in p["sections"] for t in s["topics"]
    )
    print(f"  Period {p['number']}: {len(p['sections'])} sections, {total_topics} topics, {total_objectives} objectives")
