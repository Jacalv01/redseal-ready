# Question Object Schema

```json
{
  "id": "D-13.02-Q001",
  "mwa": "D",
  "task": "D-13",
  "sub_task": "D-13.02",
  "type": "application",
  "difficulty": "medium",
  "stem": "A welder needs to deposit a 6 mm fillet weld on 12 mm mild steel plate in the vertical-up (3F) position using SMAW with E7018 electrodes. Which electrode diameter is most appropriate for the root pass?",
  "choices": {
    "A": "2.5 mm (3/32\")",
    "B": "3.2 mm (1/8\")",
    "C": "4.0 mm (5/32\")",
    "D": "5.0 mm (3/16\")"
  },
  "correct": "B",
  "explanation": "For vertical-up SMAW on mild steel plate, 3.2 mm (1/8\") is the standard electrode diameter — small enough to control the molten pool against gravity, large enough to deposit adequate metal per pass. 2.5 mm burns too fast; 4.0 mm and 5.0 mm cause pool sag in vertical-up on plate up to ~12 mm.",
  "sources": [
    {"doc": "CSA W47.1", "ref": "Table 11.2 electrode diameter vs plate thickness"},
    {"doc": "Modern Welding (Bowditch)", "ref": "Ch. 12 SMAW out-of-position technique"}
  ],
  "tags": ["smaw", "electrode-selection", "position-3f", "mild-steel"]
}
```

## Fields

| Field | Required | Notes |
|---|---|---|
| `id` | ✓ | `{SUB_TASK}-Q{NNN}` zero-padded to 3 digits |
| `mwa` | ✓ | A/B/C/D |
| `task` | ✓ | e.g. `D-13` |
| `sub_task` | ✓ | e.g. `D-13.02`; must exist in `red-seal-rsos.json` |
| `type` | ✓ | `recall` \| `application` \| `critical-thinking` |
| `difficulty` | ✓ | `easy` \| `medium` \| `hard` |
| `stem` | ✓ | Question text; single unambiguous question |
| `choices` | ✓ | Object A–D; no "all of the above" |
| `correct` | ✓ | Single letter A/B/C/D |
| `explanation` | ✓ | Why correct + why others wrong (brief) |
| `sources` | ✓ | Array of `{doc, ref}` — at least one allowed source |
| `tags` | optional | Free-form for search/filtering |

## MCQ writing rules

1. **Stem** poses one clear question — no double negatives, no compound questions
2. **All 4 choices** are grammatically parallel and roughly the same length
3. **Distractors** are plausible errors an under-prepared apprentice might actually make (not obviously wrong)
4. **Correct answer position** distributed roughly evenly across A/B/C/D across the bank
5. **No trick wording** — the exam tests knowledge, not reading comprehension
6. **Numeric answers**: distractors should reflect common miscalculations (unit swap, factor-of-2 error, wrong formula), not random numbers
