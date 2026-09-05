# RedSeal Ready

iOS app that helps Alberta welder apprentices pass their Period 1, 2, 3 exams and the national Red Seal (Interprovincial) exam.

## Structure

- `CURRICULUM_SPINE.md` — the master spec (source of truth for scope and content rules)
- `research/` — authoritative source PDFs (AIT, Red Seal, CWB, etc.) and extracted text
- `pipeline/` — content extraction and generation scripts
- `content/` — structured curriculum data (JSON) + written lessons (Markdown)
  - `ait-curriculum.json` — full Alberta AIT Welder curriculum (P1/P2/P3, 68 topics, 263 objectives)
  - `red-seal-rsos.json` — full Red Seal Occupational Standard (16 tasks, 60 sub-tasks, 585 criteria)
- `assets/` — diagrams (SVG), images, etc.
- `app/` — iOS Swift/SwiftUI app source (starts Phase 3)

## Content rules (locked)

Every technical claim in the app MUST have an inline citation from one of the allowed sources listed in `CURRICULUM_SPINE.md` §9.

## Status

- ✅ Phase 1: Research + curriculum spine
- 🚧 Phase 2: Content generation (in progress)
- ⏸️  Phase 3: iOS app build
- ⏸️  Phase 4: App Store submission
