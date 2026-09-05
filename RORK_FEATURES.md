# RedSeal Ready — Feature Specifications for Rork

**Audience:** Rork build agent. Everything below is a build spec. Cite this file when asking Rork to implement any feature.

**Sources of truth this app already ships with:**
- 64 lessons (`content/period[1-3]/section*/topic-*.md`) — each with YAML frontmatter tagging it to Red Seal MWAs via `red_seal_mapping`
- 169 questions in 4 blocks (`content/red-seal/block-{a,b,c,d}-*.json`) — each tagged to an RSOS `sub_task` (e.g. `D-13.02`)
- RSOS 2023 blueprint (`content/red-seal-rsos.json`) — task weightings, exam format
- AIT curriculum (`content/ait-curriculum.json`) — official Alberta outline
- Mock exam sampler (`content/red-seal/mock-exam-sampler.py`) — reference weighting algorithm

**Data-model connection Rork must preserve:**
```
lesson.red_seal_mapping[] ← contains sub_task IDs like "D-13.02"
question.sub_task          ← identical format
```
This is the join key between lessons and questions. Everything below uses it.

---

## Feature 1 — Spaced Repetition (SRS)

**Why:** Highest-impact learning feature ever built. Anki-style SRS gives 2–3× retention vs re-reading. All 169 questions are already tagged; we just need the scheduling layer.

### Data model (local device only, no auth)
```typescript
interface UserQuestionState {
  question_id: string;            // e.g. "D-13.02-Q003"
  ease_factor: number;             // default 2.5 (SM-2)
  interval_days: number;           // days until next review
  repetitions: number;             // consecutive correct answers
  last_reviewed_at: number;        // unix ms
  next_due_at: number;             // unix ms
  history: Array<{ ts: number; grade: 0|1|2|3|4|5 }>;
}
```

Store in AsyncStorage (React Native) or Core Data (Swift). Keyed by `question_id`.

### Algorithm: SM-2 (SuperMemo 2)
On answer, user picks grade:
- **Grade 0–2 (wrong):** reset repetitions to 0, interval to 1 day
- **Grade 3–5 (correct):**
  - If repetitions == 0: interval = 1 day
  - If repetitions == 1: interval = 6 days
  - Else: interval = prev_interval × ease_factor (rounded up)
  - repetitions += 1
- Update ease_factor:
  ```
  EF_new = EF_old + (0.1 - (5 - grade) × (0.08 + (5 - grade) × 0.02))
  EF_new = max(1.3, EF_new)
  ```

### UI
- **Home screen:** "Review" card at top showing `X due today`, tap → Review session
- **Review session:** shows one question at a time; user answers; after each answer, three buttons:
  - "Again" (grade 1) — got it wrong
  - "Hard" (grade 3) — got it but struggled
  - "Good" (grade 4) — got it comfortably
  - "Easy" (grade 5) — trivial
- After the queue empties, show streak + retention stats

### Simplification for MVP
If SM-2 feels complex, use a simplified version: wrong → review tomorrow, right → double the interval (1, 2, 4, 8, 16, 32 days), cap at 6 months. Retain the correct/wrong log for future upgrade.

---

## Feature 2 — Weak-Area Diagnostic Dashboard

**Why:** Students waste hours re-studying material they already know. Show them exactly where their gaps are.

### Data model
```typescript
interface SubTaskStats {
  sub_task_id: string;        // e.g. "D-13.02"
  attempts: number;
  correct: number;
  last_attempt_at: number;
  mastery: 'weak' | 'developing' | 'strong'; // <60% / 60-85% / >85%
}
```

Derive from `UserQuestionState.history[]` by joining on `question.sub_task`.

### UI

**After every quiz/mock exam** — replace generic "You got 84/100" with a diagnostic breakdown:

```
Mock Exam Results
─────────────────
Score: 87 / 125 (70% — PASS)

By Block:
  A Common Skills          16/20  ✅ strong
  B Layout & Fabrication   19/28  🟡 developing
  C Cutting & Gouging      17/23  ✅ strong
  D Welding Processes      35/54  🔴 weak — focus here

Weakest sub-tasks:
  ⚠ D-14.02 GMAW technique     2/6   → Review lesson
  ⚠ D-15.03 GTAW technique     3/7   → Review lesson
  ⚠ B-8.02 Estimating          4/9   → Review lesson

[Practice weak areas] [Retake mock] [Full breakdown]
```

**"Review lesson"** tap → open the lesson whose `red_seal_mapping[]` contains this sub-task. If multiple lessons match, prefer the one from the highest period number.

**Full breakdown** = table of every sub-task with attempts, % correct, mastery band, and lesson link.

### Home-screen mastery ring
Show three rings on home: **Study** (lessons opened), **Practice** (questions attempted), **Master** (sub-tasks at >85%). Motivating without being cringe.

---

## Feature 3 — Visual Explainers

**Why:** Some welding concepts are impossible to learn from text. See `assets/visuals/README.md` for the list of 20 assets. Rork should embed these inline in the corresponding lessons where the frontmatter has a `visuals:` field.

### Integration
Each lesson markdown file will get a frontmatter field:
```yaml
visuals:
  - id: smaw-arc-anatomy
    src: assets/visuals/smaw-arc-anatomy.svg
    caption: "SMAW arc showing electrode core, coating, gas shield, molten pool, and slag."
    embed_after_heading: "What SMAW is — process overview"
```

Rork renders each `visual` as a full-width image after the specified H2 heading, with a caption below.

### SVG format
All visuals are vector SVG so they scale on any screen. Include ARIA labels for accessibility.

---

## Feature 4 — Voice Narration

**Why:** Welders study on commutes, breaks, and in shops with dirty hands. Audio unlocks 2 hours/day of previously unusable time.

### Pipeline (build-time, not runtime)
1. `bin/generate-narration.py` iterates every lesson markdown
2. Strips markdown, extracts prose (skips code blocks, tables, YAML)
3. Sends to TTS (options: ElevenLabs API, Coqui TTS local, or Kokoro-82M local — Coqui/Kokoro is free)
4. Writes MP3 to `assets/audio/period{N}/section{M}/topic-{letter}.mp3`
5. Emits `assets/audio/manifest.json` mapping lesson ID → audio path + duration

### Runtime UI
- Play button in lesson header
- Persistent mini-player at bottom of screen when audio is active (like Spotify)
- Speed control (0.8× / 1× / 1.25× / 1.5× / 2×)
- Auto-advance to next lesson at end (opt-in)
- Sleep timer
- Downloadable per-lesson for offline

### Voice choice
- **Preferred:** Neutral North-American male (relatable to trades demographic — but survey later)
- **Alt:** Female voice option to counter homogeneity
- **Never:** Robotic / obviously synthetic voices — kills engagement

**Do NOT** stream on-demand from a cloud TTS at runtime — expensive, requires internet, adds latency.

---

## Feature 5 — Interactive Calculators

**Why:** The formulas students learn once and use forever. Also doubles as a job-site tool that keeps the app installed post-cert.

### Calculators (all bundled offline)

Each stored as a JSON spec `content/calculators/{id}.json` and rendered by a generic calculator component.

#### 5.1 — Heat Input Calculator
```json
{
  "id": "heat-input",
  "title": "Weld Heat Input",
  "formula": "HI = (V × A × 60) / (mm/min × 1000)",
  "inputs": [
    { "id": "V", "label": "Arc voltage (V)", "type": "number", "min": 10, "max": 40, "default": 24 },
    { "id": "A", "label": "Amperage (A)", "type": "number", "min": 30, "max": 500, "default": 150 },
    { "id": "S", "label": "Travel speed (mm/min)", "type": "number", "min": 50, "max": 800, "default": 200 }
  ],
  "output": {
    "expr": "(V * A * 60) / (S * 1000)",
    "units": "kJ/mm",
    "decimals": 2
  },
  "notes_ref": "CSA W59 Clause 5.7 · AWS D1.1 Annex heat input formula",
  "linked_lesson": "period1/section3/topic-a-smaw-equipment"
}
```

#### 5.2 — Bend Allowance
Inputs: material thickness T, inside bend radius R, bend angle θ (deg), K-factor (default 0.44 for mild steel, adjustable per material)
Output: bend allowance in mm and inches

#### 5.3 — Filler Metal Consumption
Inputs: joint length, weld cross-section area (or leg for fillet), deposition efficiency (dropdown: SMAW 60% / FCAW 80% / GMAW 90% / SAW 98%), density (default 7.85 g/cm³ steel, 2.70 aluminum)
Output: filler mass to purchase (kg)

#### 5.4 — Sling Load per Leg
Inputs: total load (kg), number of legs (2 or 4), included angle between legs (deg)
Output: load per leg (kg) with warning if > 60° angle
Cite ASME B30.9 in output.

#### 5.5 — Deposit Rate & Arc Time
Inputs: deposit weight required (kg), deposition rate (kg/hr — dropdown with typical values for each process)
Output: arc-on hours; also show typical labour hours assuming 30% operator factor (adjustable).

#### 5.6 — Hex Across Flats ↔ Across Corners
Input: one value (F or C), toggle unit (mm / inch)
Output: the other value using C = F / cos(30°).

#### 5.7 — Mitre Angle for Pipe Elbows
Inputs: total angle (default 90°), number of pieces (2, 3, 4, 6)
Output: mitre angle per cut = total ÷ (2 × pieces)

#### 5.8 — Preheat Lookup (Simplified)
Inputs: base metal group (P-number dropdown), thickness (mm), process (SMAW low-H / non-low-H / other)
Output: minimum preheat per CSA W59 Annex E table (bundle the table as JSON reference data).
Disclaimer: always verify with the actual WPS/code.

### UI pattern
- Calculator lives on a "Tools" tab (fourth tab beside Study, Practice, Progress)
- Each calculator = inputs at top, big result number in center, formula + citation at bottom
- Result updates live as inputs change
- "Copy result" button (long-press) — copies formatted result to clipboard for field notes

---

## Feature 6 — Photo Defect Scanner (v2 — plan now, ship later)

**Why:** Enormous coolness factor + genuine learning tool. Ties the app to real shop work.

### v2 architecture
1. User taps camera icon on Home
2. Take photo of a weld (any process)
3. Photo → Gemini 2.0 Flash / Claude Sonnet vision API with structured prompt:
   ```
   You are a welding inspector. Analyze this weld photo. Return JSON:
   {
     "process": "SMAW|GMAW|FCAW|GTAW|SAW|unknown",
     "defects": [{ "type": "<name>", "confidence": 0-1, "location": "<description>" }],
     "notes": "<what the welder should look at>"
   }
   Defect types allowed: undercut, porosity, incomplete_fusion, incomplete_penetration,
   cold_lap, overlap, crater_crack, longitudinal_crack, transverse_crack, spatter,
   convexity, concavity, arc_strike, sugaring, tungsten_inclusion, slag_inclusion, none
   ```
4. Match returned defect(s) to lesson(s) via a lookup table:
   ```json
   {
     "undercut": ["period1/section1/topic-g-weld-faults", "period3/section2/topic-e-non-destructive-testing"],
     "porosity": [...],
     ...
   }
   ```
5. Show defect(s) + confidence + one-tap link to remedy lesson + question bank of related MCQs

### Cost management
- Cap at 5 scans/day free tier, unlimited on Pro
- Cache identical photos (hash-based) so retries are free

### Safety
- Add disclaimer: "This is a study tool, not a certified inspection. Always follow your WPS and QA procedure for production work."

**Do NOT ship v6 until v1-5 are stable.** Vision APIs cost money; make sure users are engaged first.

---

## Feature 7 — "Common Exam Traps" callouts

**Why:** The Red Seal exam has known trick patterns (units, polarity direction, position designation off-by-one). Explicit callouts train students to spot them.

**Implementation:** every lesson gets a `⚠ Exam trap` box appended (I'll add these in content directly — Rork just needs to render them). Frontmatter will add:
```yaml
exam_traps:
  - trap: "Confusing DCEP with DCEN"
    when: "Any question naming an electrode by classification"
    counter: "E7018 = AC or DCEP only. E6010 = DCEP only. If you see DCEN in the answer, it's almost always wrong for these two."
```

Render style: yellow-tinted callout box, ⚠ icon, at end of lesson before quiz.

---

## Feature 8 — Progress & Streaks (light gamification)

Show but don't over-do:
- **Study streak:** consecutive days with any activity. Reset if 24h+ gap.
- **Total XP:** 10 per lesson opened, 5 per question answered correctly (once — not repeat farming).
- **Milestones:** first 100 questions, 500 questions, all lessons in a period, first mock exam passed, etc. Simple badges. No pop-up spam.

Never lock content behind streaks. Don't send daily push notifications more than once. Don't guilt-trip users.

---

## Feature 9 — Offline mode (already almost free)

All content is bundled at install. Requirements:
- Question banks + lessons ship in-app (already true)
- SRS state persists in local storage (Feature 1 spec above)
- Audio narration downloaded per-lesson on-demand + cached; user can "Download all" for a period
- Calculators run entirely offline (Feature 5)
- Photo scanner is the ONLY feature requiring network — degrade gracefully with clear "requires internet" message

---

## Feature 10 — Instructor mode (v2)

For selling to trade schools:
- Instructor account creates a "class" with a join code
- Students join via code → progress visible to instructor dashboard
- Instructor sees: per-student mastery, weakest sub-tasks class-wide, mock exam average, engagement time

**Punt** until we have paying B2C users. Selling B2B costs sales cycles; B2C validates the product first.

---

## Build order recommendation for Rork

Ship in this order — each is standalone-shippable:

1. **v1.0 (current):** Lessons + quizzes + mock exam sampler (already in the repo)
2. **v1.1:** SRS + Diagnostic dashboard (Features 1 + 2) — biggest learning impact, uses existing data
3. **v1.2:** Calculators (Feature 5) — differentiator, low complexity, no ML dependency
4. **v1.3:** Visual explainers (Feature 3) — content-heavy but self-contained
5. **v1.4:** Voice narration (Feature 4) — big TAM expansion (audio-first users)
6. **v1.5:** Exam traps + streaks polish (Features 7 + 8)
7. **v2.0:** Photo defect scanner (Feature 6) — flagship differentiator, needs external API
8. **v2.1:** Instructor mode (Feature 10) — B2B expansion after B2C validated

---

## Data contracts summary (for Rork)

```typescript
// Lesson (parsed from markdown frontmatter)
interface Lesson {
  id: string;                 // "p1-s3-a"
  period: 1 | 2 | 3;
  section: number;
  topic: string;
  title: string;
  hours: number;
  weight_pct: number;
  outcome: string;
  objectives: string[];
  red_seal_mapping: string[]; // ["D-13.01", "D-13.02"]
  citations: Array<{ source: string; ref: string; url?: string }>;
  visuals?: Array<{ id: string; src: string; caption: string; embed_after_heading: string }>;
  exam_traps?: Array<{ trap: string; when: string; counter: string }>;
  narration_audio?: string;   // path to mp3
  body_markdown: string;      // everything after frontmatter
}

// Question (already in the JSON banks)
interface Question {
  id: string;                 // "D-13.02-Q003"
  mwa: 'A'|'B'|'C'|'D';
  task: string;               // "D-13"
  sub_task: string;           // "D-13.02"
  type: 'recall'|'application'|'critical-thinking';
  difficulty: 'easy'|'medium'|'hard';
  stem: string;
  choices: { A: string; B: string; C: string; D: string };
  correct: 'A'|'B'|'C'|'D';
  explanation: string;
  sources: Array<{ doc: string; ref: string }>;
  tags?: string[];
}

// Mock exam (output of sampler)
interface MockExam {
  exam_type: 'red-seal-mock';
  trade: 'welder';
  total_questions: 125;
  pass_mark_pct: 70;
  duration_hours: 4;
  seed?: number;
  questions: Question[];
}
```

---

## Non-negotiables

- **All content offline-first.** Every lesson, every question, every calculator works with airplane mode on.
- **Every question shows its citations after answering.** No unsourced answers.
- **No dark patterns.** No fake urgency, no manipulative streaks, no attention-hijacking notifications.
- **Accessibility from day 1.** VoiceOver labels, dynamic type, high contrast mode, captions on any video.
- **No user auth for v1.** Everything local. Auth only when Instructor Mode (v2.1) demands it.

---

**End of feature spec.** Point Rork at this file (`RORK_FEATURES.md` in repo root) and it has everything needed to build v1.1 through v2.1.
