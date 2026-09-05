#!/usr/bin/env python3
"""
Extract the Red Seal Welder Occupational Standard (RSOS) into structured JSON.

Input:  research/red-seal-welder-rsos.txt
Output: content/red-seal-rsos.json

Structure:
{
  "source": "Red Seal Occupational Standard - Welder (2024)",
  "exam": {
    "total_questions": 125,
    "pass_mark_pct": 70,
    "duration_hours": 4,
    "question_types": {
      "knowledge_recall_pct": [40, 50],
      "procedural_application_pct": [35, 45],
      "critical_thinking_pct": [10, 20]
    }
  },
  "mwas": [
    {
      "id": "A",
      "title": "Performs common occupational skills",
      "exam_weight_pct": 16,
      "exam_questions": 20,
      "tasks": [
        {
          "id": "A-1",
          "title": "Maintains tools and equipment",
          "task_weight_pct": 25,
          "exam_questions": 4,
          "sub_tasks": [
            {
              "id": "A-1.01",
              "title": "Maintains hand, power, layout and measuring tools",
              "common_core_jurisdictions": ["NL","NS","PE","NB","ON","MB","SK","AB","BC"],
              "performance_criteria": [
                {"id": "A-1.01.01P", "criterion": "select and use tools and equipment", "evidence": "tools and equipment are selected and used according to task"}
              ],
              "learning_outcomes": [
                {"id": "A-1.01.01L", "outcome": "demonstrate knowledge of hand, power, layout and measuring tools, their characteristics, applications and operation", "objectives": ["identify hand tools, and describe their characteristics and applications", ...]}
              ],
              "range_of_variables": {"striking tools": ["chipping hammers","chisels","punches"]}
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

SRC = Path(__file__).parent.parent / "research" / "red-seal-welder-rsos.txt"
OUT = Path(__file__).parent.parent / "content" / "red-seal-rsos.json"

TEXT = SRC.read_text()

# Static exam blueprint (from Red Seal exam-weightings + Sask apprenticeship 2024 confirmation)
EXAM = {
    "total_questions": 125,
    "pass_mark_pct": 70,
    "duration_hours": 4,
    "format": "multiple-choice",
    "question_types": {
        "knowledge_recall_pct": [40, 50],
        "procedural_application_pct": [35, 45],
        "critical_thinking_pct": [10, 20],
    },
}

MWA_BLUEPRINT = {
    "A": {"title": "Performs common occupational skills", "weight_pct": 16, "questions": 20},
    "B": {"title": "Performs layout and fabrication of components for welding", "weight_pct": 22, "questions": 28},
    "C": {"title": "Performs cutting and gouging", "weight_pct": 18, "questions": 23},
    "D": {"title": "Performs welding processes", "weight_pct": 44, "questions": 54},
}

# Per-task weights + question counts (source: Red Seal exam weightings + Sask 2024)
TASK_BLUEPRINT = {
    "A-1": {"title": "Maintains tools and equipment", "task_weight_pct": 25, "questions": 4},
    "A-2": {"title": "Uses access and material handling equipment", "task_weight_pct": 15, "questions": 3},
    "A-3": {"title": "Performs safety-related activities", "task_weight_pct": 25, "questions": 4},
    "A-4": {"title": "Organizes work", "task_weight_pct": 15, "questions": 3},
    "A-5": {"title": "Performs routine trade activities", "task_weight_pct": 28, "questions": 6},
    "A-6": {"title": "Uses communication and mentoring techniques", "task_weight_pct": 2, "questions": 0},
    "B-7": {"title": "Performs layout", "task_weight_pct": 44, "questions": 12},
    "B-8": {"title": "Fabricates components", "task_weight_pct": 56, "questions": 16},
    "C-9": {"title": "Uses tools and equipment for non-thermal cutting and grinding", "task_weight_pct": 25, "questions": 6},
    "C-10": {"title": "Uses oxy-fuel gas cutting (OFC) process for cutting and gouging", "task_weight_pct": 30, "questions": 7},
    "C-11": {"title": "Uses plasma arc cutting (PAC) process for cutting and gouging", "task_weight_pct": 26, "questions": 6},
    "C-12": {"title": "Uses air carbon arc cutting (CAC-A) process for cutting and gouging", "task_weight_pct": 19, "questions": 4},
    "D-13": {"title": "Welds using shielded metal arc welding (SMAW) process", "task_weight_pct": 33, "questions": 18},
    "D-14": {"title": "Welds using flux cored arc welding (FCAW), metal cored arc welding (MCAW) and gas metal arc welding (GMAW) processes", "task_weight_pct": 34, "questions": 18},
    "D-15": {"title": "Welds using gas tungsten arc welding (GTAW) process", "task_weight_pct": 24, "questions": 13},
    "D-16": {"title": "Welds using submerged arc welding (SAW) process", "task_weight_pct": 9, "questions": 5},
}

# Parse sub-tasks. Each sub-task starts with a pattern like: "A-1.01 Maintains hand, power, layout and measuring tools"
# Followed by a jurisdiction table row: "NL NS PE NB QC ON MB SK AB BC NT YT NU"
# Then "yes yes ..." row indicating common-core status

subtask_pattern = re.compile(
    r"^([ABCD]-\d+\.\d+)\s+([^\n]+?)\s*\n\s*NL NS PE NB QC ON MB SK AB BC NT YT NU\s*\n\s*([a-zNV\s]+?)\n",
    re.MULTILINE,
)

# Find all sub-task blocks
subtask_matches = list(subtask_pattern.finditer(TEXT))

sub_tasks = {}  # id -> parsed data

JURISDICTIONS = ["NL","NS","PE","NB","QC","ON","MB","SK","AB","BC","NT","YT","NU"]

for i, m in enumerate(subtask_matches):
    st_id = m.group(1)
    st_title = m.group(2).strip()
    jurisdiction_row = m.group(3).strip().split()
    common_core = [
        JURISDICTIONS[j] for j, v in enumerate(jurisdiction_row) if v.lower() == "yes"
    ]

    # Content ends at next sub-task or end of file
    start = m.end()
    end = subtask_matches[i + 1].start() if i + 1 < len(subtask_matches) else len(TEXT)
    block = TEXT[start:end]

    # Extract Performance Criteria (P codes)
    # Pattern: "A-1.01.01P criterion text  evidence text"
    # These are hard to split cleanly since PDF text is two-column. Use a regex on the P-code lines.
    p_pattern = re.compile(
        rf"({re.escape(st_id)}\.\d+P)\s+(.+?)(?=(?:{re.escape(st_id)}\.\d+P)|Range of Variables|Knowledge|\Z)",
        re.DOTALL,
    )
    performance_criteria = []
    for pm in p_pattern.finditer(block):
        raw = re.sub(r"\s+", " ", pm.group(2)).strip()
        # Split criterion vs evidence: the evidence usually starts around a natural break.
        # PDF layout means both columns get concatenated. We store as raw for now — cleanup later.
        performance_criteria.append({
            "id": pm.group(1),
            "text": raw,
        })

    # Extract Learning Outcomes (L codes)
    l_pattern = re.compile(
        rf"({re.escape(st_id)}\.\d+L)\s+(.+?)(?=(?:{re.escape(st_id)}\.\d+L)|Range of Variables|Skills|\Z)",
        re.DOTALL,
    )
    learning_outcomes = []
    for lm in l_pattern.finditer(block):
        raw = re.sub(r"\s+", " ", lm.group(2)).strip()
        learning_outcomes.append({
            "id": lm.group(1),
            "text": raw,
        })

    # Extract Range of Variables sections (both — one may follow Skills, one may follow Knowledge)
    rov_pattern = re.compile(
        r"Range of Variables\s*\n(.+?)(?=Knowledge|Skills|Range of Variables|[ABCD]-\d+\.\d+|Task [ABCD]-\d+|\Z)",
        re.DOTALL,
    )
    range_of_variables = {}
    for rm in rov_pattern.finditer(block):
        rov_text = rm.group(1)
        # Each variable line: "striking tools include: chipping hammers, chisels, punches"
        for line in rov_text.split("\n"):
            line = line.strip()
            if " include" in line and ":" in line:
                key_part, val_part = line.split(":", 1)
                key = re.sub(r"\s+include[s]?$", "", key_part.strip())
                vals = [v.strip() for v in val_part.split(",") if v.strip()]
                if key and vals:
                    range_of_variables[key] = vals

    sub_tasks[st_id] = {
        "id": st_id,
        "title": st_title,
        "common_core_jurisdictions": common_core,
        "is_common_core": len(common_core) >= 9,  # 70%+ of 13 jurisdictions
        "performance_criteria": performance_criteria,
        "learning_outcomes": learning_outcomes,
        "range_of_variables": range_of_variables,
    }

# Build final structure: group sub-tasks by task, tasks by MWA
mwas = []
for mwa_id, mwa_info in MWA_BLUEPRINT.items():
    tasks = []
    for task_id, task_info in TASK_BLUEPRINT.items():
        if not task_id.startswith(mwa_id + "-"):
            continue
        task_subtasks = [st for stid, st in sub_tasks.items() if stid.startswith(task_id + ".")]
        task_subtasks.sort(key=lambda x: x["id"])
        tasks.append({
            "id": task_id,
            "title": task_info["title"],
            "task_weight_pct": task_info["task_weight_pct"],
            "exam_questions": task_info["questions"],
            "sub_tasks": task_subtasks,
        })
    mwas.append({
        "id": mwa_id,
        "title": mwa_info["title"],
        "exam_weight_pct": mwa_info["weight_pct"],
        "exam_questions": mwa_info["questions"],
        "tasks": tasks,
    })

result = {
    "source": "Red Seal Occupational Standard - Welder",
    "source_url": "https://red-seal.ca/_conf/assets/custom/docms/welder/rsos-eng.pdf",
    "isbn": "978-0-660-48919-3",
    "published": "2023",
    "extracted": "2026-09-04",
    "exam": EXAM,
    "mwas": mwas,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2))

# Summary
print(f"Extracted to {OUT}")
total_subtasks = sum(len(t["sub_tasks"]) for m in mwas for t in m["tasks"])
total_pcs = sum(len(st["performance_criteria"]) for m in mwas for t in m["tasks"] for st in t["sub_tasks"])
total_los = sum(len(st["learning_outcomes"]) for m in mwas for t in m["tasks"] for st in t["sub_tasks"])
print(f"  Total sub-tasks: {total_subtasks}")
print(f"  Total performance criteria (P codes): {total_pcs}")
print(f"  Total learning outcomes (L codes): {total_los}")
for m in mwas:
    st_count = sum(len(t["sub_tasks"]) for t in m["tasks"])
    print(f"  MWA {m['id']}: {len(m['tasks'])} tasks, {st_count} sub-tasks, {m['exam_questions']} exam Q ({m['exam_weight_pct']}%)")
