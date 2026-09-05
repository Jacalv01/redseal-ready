# Red Seal Question Bank — Welder (RSOS 2023)

**Target exam:** Red Seal Interprovincial (Welder — 456A)
**Format:** 125 MCQ · 4 hours · 70% to pass
**Source of truth:** `../red-seal-rsos.json` (2023 Occupational Standard)

## Structure

```
red-seal/
├── README.md                    (this file)
├── schema.md                    question object schema + rules
├── block-a-common-skills.json   20 Q on exam · target bank ≥ 80 Q
├── block-b-layout-fab.json      28 Q on exam · target bank ≥ 110 Q
├── block-c-cutting-gouging.json 23 Q on exam · target bank ≥ 95 Q
├── block-d-welding.json         54 Q on exam · target bank ≥ 220 Q
└── mock-exam-sampler.py         draws a 125-Q mock exam with correct weighting
```

## Task weighting (mock exam must match this exactly)

| Block | MWA | Exam Q | Bank target |
|---|---|---|---|
| A | Common occupational skills | 20 | 80 |
| B-7 | Performs layout | 12 | 48 |
| B-8 | Fabricates components | 16 | 64 |
| C-9 | Non-thermal cutting/grinding | 6 | 24 |
| C-10 | Oxy-fuel cutting (OFC) | 7 | 28 |
| C-11 | Plasma arc cutting (PAC) | 6 | 24 |
| C-12 | Air carbon arc (CAC-A) | 4 | 16 |
| D-13 | SMAW | 18 | 72 |
| D-14 | FCAW/MCAW/GMAW | 18 | 72 |
| D-15 | GTAW | 13 | 52 |
| D-16 | SAW | 5 | 20 |
| **TOTAL** | | **125** | **≥500** |

## Content rules (hard — from CURRICULUM_SPINE.md §9)

Every question:
1. Tagged with MWA / task / sub-task ID (e.g. `D-13.02`)
2. Cited to an allowed source (RSOS, AIT, CSA W47.1/W59/B51, CWB, Modern Welding, Miller/Lincoln/ESAB, TWI, AWS)
3. Exactly one correct answer, three plausible distractors
4. Explanation ties back to citation
5. Question type flagged: `recall` | `application` | `critical-thinking`

**Never:**
- Copy or reconstruct real Red Seal exam questions (that's protected content)
- Fabricate specs without a manufacturer/code citation
- Use "all of the above" or "none of the above" (poor MCQ practice per NCLEX/exam-writing guidelines)

## Question type mix (matches RSOS blueprint)

- Recall (definitions, symbols, code refs): 40–50%
- Application (procedure, calculation, selection): 35–45%
- Critical thinking (scenario, troubleshooting): 10–20%
