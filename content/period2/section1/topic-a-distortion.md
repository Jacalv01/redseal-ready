---
id: p2-s1-a
period: 2
section: 1
section_title: Foundational Skills, Safety, Procedures and Properties of Metals
topic_letter: A
topic_title: Distortion
hours: 2
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to identify the types, causes, and control methods of welding distortion.
objectives:
  - Identify how heat and temperature relate to distortion.
  - Identify the three types of distortion, their causes and control of each type.
red_seal_mapping:
  - A-5.03 (Controls temperature of weldments)
  - B-8.02 (Fits components for welding)
  - B-8.03 (Assembles components)
citations:
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 22 — Distortion and Stress Relief
    url: https://www.g-w.com/modern-welding
  - source: TWI Global — Distortion in Welding — Causes and Prevention
    ref: TWI Knowledge Summary, types of distortion, control methods
    url: https://www.twi-global.com/technical-knowledge/faqs/what-is-distortion-in-welding
  - source: Lincoln Electric — Controlling Distortion in Welding
    ref: Lincoln Procedure Handbook of Arc Welding, Section 3.4
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 5 — Fit-up and assembly tolerances, dimensional control
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic A
    ref: pp. 26–27
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Distortion

Every time you lay a bead, you're fighting thermodynamics. Hot metal wants to expand; cold metal won't let it. The weld cools; hot metal wants to contract; now your joint is pulling against itself. The result is a part that is no longer flat, square, or the right shape. Distortion costs Alberta fabricators money every day — in straightening, rework, scrap, and delays. Understanding *why* it happens puts you in control.

---

## Heat and temperature: not the same thing

Apprentices confuse these constantly.[^1]

- **Temperature** = how hot something is (measured in °C or °F). A small bead and a large bead can be at the same temperature.
- **Heat (heat input)** = the total energy delivered to the joint, measured in joules per millimetre (J/mm) or kJ/in.

**Heat input formula:**[^1]
> Heat Input (J/mm) = (Amps × Volts × 60) ÷ Travel Speed (mm/min)

**Why it matters for distortion:**
- Higher heat input → larger heat-affected zone (HAZ) → more metal undergoes thermal expansion and contraction → **more distortion**
- Same amperage, faster travel speed → lower heat input → less distortion
- Same amperage, multiple small passes → less total distortion than one large pass per side

**Thermal expansion of mild steel:** approximately 12 × 10⁻⁶ mm/mm·°C[^1] — meaning a 1000 mm piece at 500°C above ambient will try to be ~6 mm longer. The surrounding cold metal resists. Something has to give — either plastic deformation in the HAZ, or distortion of the overall part.

---

## Why distortion happens: the expansion-contraction cycle

This three-stage cycle explains every type of distortion:[^2]

**Stage 1 — Heating:**
The arc heats the weld zone to above 1500°C locally. The surrounding base metal is cool. The hot metal tries to expand but is constrained by the cooler surrounding metal. Since it can't expand freely, it **plastically deforms** (upsets) — the hot metal is effectively squeezed short.

**Stage 2 — Cooling:**
As the weld cools, it tries to shrink back. But it's now shorter (upset) than it was to begin with. This means it pulls on the surrounding base metal as it contracts.

**Stage 3 — Residual stress + distortion:**
If the joint is rigidly restrained (clamped, tacked), the contraction builds **residual tensile stress** in the weld and compressive stress in the HAZ. If the joint is free to move, the contraction causes **distortion**. In practice, most real fabrications experience some of both.

---

## The three types of distortion

### 1. Transverse shrinkage (shrinkage across the joint)[^1][^2]

The weld metal contracts perpendicular to the weld bead — pulling the two plates together. This is visible as narrowing of the joint gap after welding.

**How much:** Approximately 1–3 mm per pass depending on joint geometry, amperage, and preheat.

**Control methods:**
- Pre-set the joint slightly wider ("springback allowance") — for a butt joint, 2–3° presetting of each plate outward before welding
- Use strong-backs welded to each side to resist transverse movement
- Fit-up tack welds at intervals (never skip tacks on long seams)
- Complete multiple joints simultaneously on a symmetric structure

### 2. Longitudinal shrinkage (shrinkage along the weld)[^1][^2]

The weld contracts along its length. A single long bead on one side of a plate will cause that plate to bow (camber) — the welded side becomes convex (bows toward the weld).

**Visible on:** long beams, structural columns, large fabrications with single-sided welds.

**Control methods:**
- **Back-step welding:** Weld short segments in the direction *opposite* to overall travel direction. Each segment's shrinkage partially offsets the cumulative bow. Example: for a 1200 mm seam, weld 200 mm segments, starting at the end and working back to the start.
- **Balanced welding sequences:** alternating passes on opposite sides of the joint cancels longitudinal shrinkage.
- **Presetting (cambering):** pre-bend the assembly opposite to the expected distortion direction. After welding, it springs back approximately flat.

### 3. Angular distortion (rotation about the weld line)[^1][^2]

The most common type in shop fabrication. The bottom of the weld is constrained by the root and the base metal. The top of the weld has more freedom. When the top shrinks more than the bottom, the plates rotate — pulling the far edges upward (fillet weld on a T-joint → legs want to lift). A butt weld with more fill on one side → that plate rotates toward the weld.

**Visible on:** T-joints (legs pull inward), butt joints with asymmetric passes, multiple-pass groove welds.

**Control methods:**
- **Presetting the joint angle:** For a T-joint, set the fillet at 95–100° instead of 90°. After welding and cooling, angular distortion pulls it back to 90°. Requires knowing how much distortion to expect — experience + calculation.[^3]
- **Balanced welding:** Alternate between both sides of a T-joint or butt joint. Weld one pass on the right side, then one pass on the left side.
- **Clamps and fixtures:** Jigs with strongbacks hold the part in position while the weld solidifies and cools below the yield point.
- **Intermittent welding:** Use intermittent (skip) welds instead of continuous where design allows. Less total heat input → less angular pull.
- **Peening:** For inter-pass passes only (NEVER on root or cap). Light peening with a ball-peen hammer while the weld is still warm stretches the weld metal slightly, offsetting some contraction. Check welding procedure — peening may not be allowed by your WPS.

---

## Distortion control: full toolkit summary

| Control method | Best for | Notes |
|---|---|---|
| **Back-step welding** | Longitudinal shrinkage on long seams | Short segments opposite to travel direction; requires planning |
| **Balanced welding** | Angular distortion, longitudinal shrinkage | Alternate passes left/right or top/bottom |
| **Presetting (cambering)** | Angular distortion, longitudinal bowing | Requires experience; trial-and-error first piece |
| **Tack weld sequence** | Transverse shrinkage | Tack from centre out (odd-numbered tacks) — never one end to the other |
| **Strong-backs / fixtures** | All types | Best control; adds cost; residual stress trade-off |
| **Intermittent welding** | Angular on large assemblies | Reduces heat input; only where design allows per WPS |
| **Low heat input** | All types | Fastest travel, lowest amperage that still achieves fusion — check WPS limits |
| **Peening (interpass)** | All types | Inter-pass only; verify WPS allows it |
| **Proper joint prep** | All types | Minimize root opening and bevel angle to reduce filler volume |

---

## Numbers you need to memorize

- **Thermal expansion of mild steel:** ~12 × 10⁻⁶ mm/mm·°C[^1]
- **Heat Input formula:** (A × V × 60) ÷ travel speed (mm/min) = J/mm[^1]
- **Transverse shrinkage per pass (typical butt joint):** 1–3 mm[^1]
- **Preheat reduces distortion** — higher preheat makes the temperature gradient shallower, reducing differential expansion[^2]
- **More passes, lower heat per pass** = less distortion per pass (multiple-pass vs. single-pass)[^1]
- **Angular distortion increases with bevel angle** — a 60° groove will distort more than a 45° groove (more filler metal, more shrinkage volume)[^2]

---

## What the textbook doesn't tell you

**Tack weld sequence is not optional.** Tacking one end of a long seam, then the other end, then the middle, guarantees the seam gaps change between tacks. Start from the middle, alternate outward in equal jumps. This distributes shrinkage incrementally rather than letting it accumulate.[^3]

**Fixtures trap stress.** Clamping or jigging completely locks out distortion during welding. But the residual stress left in the part when you unclamp can cause problems later — stress corrosion cracking in some environments, fatigue failure in cyclic loading. For pressure vessels and critical structural welds, post-weld heat treatment (PWHT) is used to relieve this stress. Know what your WPS says.[^4]

**Back-stepping does NOT reverse the direction of each weld.** Each short segment is still welded start-to-finish in the normal sense; it's the *order* of the segments that reverses. Each segment still fuses properly. Don't reverse the direction of the arc — just start your next segment 200 mm back from where you finished.[^1]

**Angular distortion from fillet welds is often accepted on code work** — CSA W59 specifies dimensional tolerance limits (typically ±3 mm over the length of a member). If you're within tolerance, the part ships. If you're outside tolerance, you need to straighten it — and straightening a welded fabrication is expensive.[^4]

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s1-a-distortion-types.svg` — three panel diagram: (1) transverse shrinkage on a butt joint showing plates pulling together; (2) longitudinal shrinkage on a long beam showing upward bow toward the weld; (3) angular distortion on a T-joint showing legs rotating inward. Each panel labels the shrinkage direction with arrows.)*

*(SVG to be added: `assets/diagrams/p2-s1-a-back-step.svg` — plan view of a long seam showing numbered weld segment order: segments 5→4→3→2→1 with arrows showing individual segment direction left-to-right, but sequence starting at right end and working left.)*

---

## Key terms

- **Distortion:** dimensional change caused by non-uniform thermal expansion and contraction during welding
- **Transverse shrinkage:** weld metal contracts across (perpendicular to) the joint
- **Longitudinal shrinkage:** weld metal contracts along (parallel to) the joint
- **Angular distortion:** plates rotate about the weld line due to differential shrinkage top-to-bottom
- **Heat input (J/mm):** total energy per unit length delivered to the weld — the key driver of distortion magnitude
- **Residual stress:** internal stress remaining in the part after welding and cooling
- **Presetting:** intentionally angling or positioning parts before welding to counteract expected distortion
- **Back-step welding:** welding short segments in a sequence opposite to the overall direction of progress
- **Balanced welding:** alternating weld passes on opposite sides of a joint to cancel angular distortion
- **Intermittent weld:** a series of short weld segments with un-welded gaps between, reducing total heat input
- **Strong-back:** temporary restraint bar tacked to the outside of a joint to prevent movement during welding
- **PWHT:** Post-Weld Heat Treatment — thermal stress relief after welding

---

## Common exam trap

- **"Distortion is caused by heat" is incomplete.** The correct answer is differential *thermal expansion and contraction* — the temperature gradient between the hot weld zone and cold surrounding metal. Uniform heating would expand everything equally and cause no distortion.
- **Back-step welding reduces *longitudinal* shrinkage specifically** — it doesn't eliminate angular distortion. Exam questions often ask which type is controlled by back-stepping.
- **Peening is NOT permitted on the root pass or cap pass** — only on inter-pass passes. Root: peening introduces cracks. Cap: peening damages the final surface appearance and can't be inspected. Always check your WPS.
- **Tacking from one end to the other = bad.** The correct sequence is centre-outward. Exam distractors will describe end-to-end tacking as correct procedure.
- **Presetting corrects distortion BEFORE welding; straightening corrects it AFTER** — two entirely different approaches. Know which one is applied when.

---

## Practice question preview

**Q:** A welder is fabricating a 3-metre steel beam with continuous fillet welds on one side only. After welding, the beam has bowed significantly toward the weld side. Which technique, if applied BEFORE welding, would have MOST effectively prevented this?

A) Peening each bead while still red-hot
B) Pre-setting the beam with a camber (bow) opposite to the expected distortion
C) Using back-step welding sequence
D) Reducing amperage by 20% and increasing travel speed

**Correct: B**

**Explanation:** Longitudinal shrinkage on a single-sided weld causes the welded side to shorten, bowing the beam toward the weld. Pre-setting (cambering) the beam with an upward bow opposite to the expected direction allows the weld shrinkage to pull it back toward flat. (A) Peening is an interpass technique and can't be applied to the completed weld without violating WPS restrictions. (C) Back-step welding reduces but does not eliminate longitudinal shrinkage — and it wasn't applied here. (D) Lower amperage and higher speed reduces heat input, which helps, but presetting directly counteracts the specific directional distortion.

**Red Seal mapping:** A-5.03 (Controls temperature of weldments); B-8.02 (Fits components for welding)

---

[^1]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 22 — Distortion and Stress Relief; heat input formula, thermal expansion coefficient, types and control methods
[^2]: [TWI Global — Distortion in Welding: Causes and Prevention](https://www.twi-global.com/technical-knowledge/faqs/what-is-distortion-in-welding); expansion-contraction cycle, angular and transverse distortion mechanisms
[^3]: [Lincoln Electric — Controlling Distortion in Welding, Procedure Handbook of Arc Welding §3.4](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); tack sequence, back-step welding, presetting techniques
[^4]: [CSA W59:18 — Welded Steel Construction](https://www.csagroup.org/store/product/CSA%20W59%3A18/), Clause 5 — dimensional tolerances, fit-up requirements, PWHT provisions
[^5]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic A](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 26–27; learning outcome and objectives
