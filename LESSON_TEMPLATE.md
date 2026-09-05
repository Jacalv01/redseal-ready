# Lesson template (LOCKED 2026-09-04)

**Goal:** Every lesson must be *better than the corresponding ILM module* on the same topic.

## Required front-matter

```yaml
---
id: p{period}-s{section}-{letter}
period: 1|2|3
section: 1-5
section_title: <verbatim from AIT curriculum guide>
topic_letter: A-Z
topic_title: <verbatim from AIT curriculum guide>
hours: <from AIT>
weight_pct: <from AIT>
outcome: >
  <verbatim from AIT curriculum guide>
objectives:
  - <verbatim from AIT curriculum guide, one per bullet>
red_seal_mapping:
  - <Red Seal sub-task code(s) this lesson supports, e.g. A-3.01, A-3.02>
citations:
  - source: <name>
    ref: <chapter/section/page>
    url: <link>
  # MINIMUM 3 sources per lesson
---
```

## Required sections (in order)

### 1. `# <topic title>` — H1 header

### 2. Opening hook (1-2 sentences)
Why this matters on the job. Not "in this lesson we will learn..." — the actual real-world consequence.

### 3. Core content (H2 sections as needed)
Plain-English explanation, tables, bullets. Every technical claim gets an inline footnote citation.

### 4. `## Numbers you need to memorize`
Bulleted list of specific figures Red Seal tests: temperatures, amperages, gas flow rates, distances, percentages, tolerances. Each with citation.

### 5. `## What the textbook doesn't tell you`
Journeyperson wisdom / practical tips beyond the curriculum guide. Sourced from CWB, TWI, Miller/Lincoln/ESAB training materials, Modern Welding textbook. NO unsourced opinions.

### 6. `## Diagram` (when applicable)
Reference to an SVG in `assets/diagrams/`. If the topic is visual (joint types, weld positions, torch anatomy, defect patterns), a diagram is REQUIRED.

### 7. `## Key terms`
Bulleted glossary of jargon introduced in the lesson.

### 8. `## Common exam trap`
Specific ways multiple-choice writers try to trick students on this topic. Real distractors, real gotchas.

### 9. `## Practice question preview`
One sample Red Seal-style multiple-choice question with all 4 options + correct answer + explanation + Red Seal sub-task code mapping.

Example:
```
**Q:** Under Alberta OHS legislation, a worker has the right to refuse dangerous work. Which of the following is NOT a required step in the refusal process?

A) Report the refusal to the supervisor
B) Wait for the investigation to be completed
C) Immediately leave the worksite
D) If unresolved, contact an OHS officer

**Correct: C**
**Explanation:** The right to refuse dangerous work in Alberta requires the worker to REMAIN at the worksite (though away from the danger) until the formal investigation completes. Immediately leaving can void the protection. See OHS Act s.17.
**Red Seal mapping:** A-3.01 (Performs hazard assessments)
```

### 10. Footnote citations
Full URL and reference for each inline `[^n]` marker. MINIMUM 3 unique sources per lesson.

---

## Allowed source list (LOCKED)

- Alberta AIT Welder Curriculum Guide 012 (2026)
- Red Seal Occupational Standard — Welder (2024)
- Alberta OHS Act, Regulation, Code
- Health Canada — WHMIS 2015
- CSA W47.1 (Certification of Companies for Fusion Welding of Steel)
- CSA W59 (Welded Steel Construction)
- CSA B51 (Boiler, Pressure Vessel & Pressure Piping Code)
- CSA W117.2 (Safety in welding, cutting, and allied processes)
- CSA Z94.3 (Eye and face protectors)
- CSA Z195 (Protective footwear)
- CWB Group public learning materials (cwbgroup.org)
- Modern Welding textbook (Bowditch, Goodheart-Willcox)
- Miller Electric manufacturer manuals & Weld Setting Calculators
- Lincoln Electric manufacturer manuals & Consumables catalogs
- ESAB manufacturer manuals & Handbook of Arc Welding
- TWI Global public knowledge base (twi-global.com)
- AWS (American Welding Society) public standards (D1.1, A5.x series filler classifications)
- NFPA 51B (Fire Prevention in Hot Work)

If a fact can't be cited from the above list, it does NOT ship.
