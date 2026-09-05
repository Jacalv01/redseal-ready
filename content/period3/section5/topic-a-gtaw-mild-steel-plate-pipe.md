---
id: p3-s5-a
period: 3
section: 5
section_title: Gas Tungsten Arc Welding (GTAW)
topic_letter: A
topic_title: GTAW on Mild Steel Plate and Pipe
hours: 40
weight_pct: 17
outcome: >
  Upon successful completion, learners will be able to prepare, fit-up, and weld using
  GTAW and SMAW on mild steel plate and pipe in all positions, including GTAW root with
  SMAW E7018 fill/cap, 2G, 5G, and 6G pipe.
objectives:
  - Demonstrate preparation and fit-up for GTAW.
  - Perform 1G and 2G welds on mild steel plate.
  - Perform 3G weld on mild steel plate using GTAW root and SMAW E4918 (E7018) fill and cap, uphill for all passes.
  - Perform 2G, 5G and 6G welds on mild steel pipe.
red_seal_mapping:
  - D-15.01 (Selects GTAW gas, equipment and consumables)
  - D-15.02 (Sets up GTAW equipment)
  - D-15.03 (Sets operating parameters for GTAW)
  - D-15.04 (Performs weld using GTAW equipment)
  - D-13.04 (Performs weld using SMAW equipment)
citations:
  - source: CSA W47.1 — Certification of Companies for Fusion Welding of Steel
    ref: Annex B (GTAW qualification scope, 6G qualifying all positions)
    url: https://www.csagroup.org/store/product/CSA%20W47%3A1/
  - source: ASME Boiler and Pressure Vessel Code Section IX — Welding Qualifications
    ref: QW-350 to QW-399 (GTAW performance qualification, 6G scope)
    url: https://www.asme.org/codes-standards/find-codes-standards/bpvc-ix-boiler-pressure-vessel-code-section-ix-welding-brazing
  - source: Lincoln Electric — GTAW Welding Guide
    ref: GTAW setup, tungsten selection, shielding gas flow rates, mild steel GTAW procedure
    url: https://www.lincolnelectric.com/en/education-center/welding-education/gtaw-welding-guide
  - source: Miller Electric — TIG Welding Fundamentals and Advanced Pipe Welding
    ref: 6G pipe technique, GTAW root parameters, SMAW fill/cap combination, foot pedal control
    url: https://www.millerwelds.com/resources/article-library/tig-welding-fundamentals
  - source: ESAB — GTAW Handbook and Process Guide
    ref: Shielding gas selection for mild steel, backing gas purge for pipe interiors, tungsten grind angle
    url: https://www.esab.com/us/nam_en/education/blog/gtaw-tig-welding-guide/
  - source: AWS A5.18 — Carbon Steel Electrodes and Rods for GTAW
    ref: ER70S-2 and ER70S-6 filler classifications for mild steel GTAW
    url: https://pubs.aws.org/p/1141/a518a518m2005-specification-for-carbon-steel-electrodes-and-rods-for-gas-shielded-arc-welding
---

# GTAW on Mild Steel Plate and Pipe — All Positions Including 6G

The 6G pipe qualification is the highest credential in the welding trade. A welder with a 6G GTAW+SMAW combination qualification card can walk into almost any pressure vessel shop, refinery, nuclear facility, or power plant in Canada and be hired on the spot. It takes years of deliberate practice to get there — this lesson covers what you need to know to begin that journey.

---

## Why GTAW Root + SMAW Fill/Cap Is the Standard

In pressure piping and high-quality structural fabrication, the combination of GTAW root and SMAW fill/cap is used for several reasons:[^1][^3]

| Advantage | GTAW root | SMAW fill/cap |
|---|---|---|
| **Penetration quality** | Superior — GTAW provides precise fusion at the root with full control over the puddle | Less precise at root — SMAW arc is harder to control in tight root gaps |
| **Root appearance** | Smooth, consistent crown on back side — ideal for quality-critical piping | Coarser root surface; more susceptible to incomplete penetration |
| **Productivity** | Slow — GTAW deposition rate is very low | Fast — SMAW deposition rate is much higher than GTAW |
| **Hydrogen risk** | Near-zero diffusible hydrogen (argon shielded, no flux) | Low with E7018 (2 mL/100g max diffusible H per AWS A5.1) |

**The strategy:** use GTAW where quality is non-negotiable (the root — the highest-stress location and the least accessible for repair) and switch to SMAW to fill the joint efficiently and economically.

---

## GTAW Setup Review — Mild Steel Specifics

### Tungsten selection for DCEN mild steel GTAW[^3][^5]

For mild steel GTAW on DC:

| Tungsten type | Color code | Best for | Notes |
|---|---|---|---|
| **2% Thoriated (EWTh-2)** | Red | DCEN — steel, stainless, titanium | Excellent arc starts, long life, BUT: thorium is mildly radioactive — must not be ground dry (inhale dust) |
| **2% Ceriated (EWCe-2)** | Gray | DCEN — preferred replacement for thoriated | Non-radioactive, excellent arc starts, similar performance to EWTh-2 |
| **Pure tungsten (EWP)** | Green | AC only — aluminum/magnesium | NOT for DC/steel — does not form a stable arc on DC |
| **Lanthanated (EWLa-1.5)** | Gold | AC and DC | Versatile, non-radioactive, good arc starts |

**Polarity for mild steel GTAW:** DCEN (DC Electrode Negative — also written DCSP, Direct Current Straight Polarity).[^3]

### Tungsten preparation for DCEN

- **Grind to a point:** for DCEN mild steel GTAW, the tungsten should be ground to a **tapered point** (15–30° included angle)
- **Grind parallel to the tungsten axis** — not circumferentially, which leaves ridges that cause arc wander
- **Point length:** approximately 2–2.5× the tungsten diameter
- At the tip of a well-ground tungsten, a very small flat (1/10 to 1/5 of the tungsten diameter) is acceptable — a perfect needle tip is fragile[^3][^5]

### Shielding gas for mild steel GTAW[^5]

- **Standard:** 100% argon (Ar) — the most common and cleanest choice
- **Flow rate:** 10–15 L/min (20–30 CFH) for most mild steel applications — adjust for cup size and joint geometry
- **Higher flow ≠ better:** excess flow creates turbulence that draws air in at the cup edge (Venturi effect) — results in contamination. Set the minimum flow that provides adequate coverage.
- **Shielding gas purity:** 99.99% minimum purity. Moisture or air contamination in the gas causes porosity and tungsten contamination.

### Filler rod for mild steel GTAW — AWS A5.18[^6]

| Filler | Application |
|---|---|
| **ER70S-2** | All-purpose mild steel GTAW — triple-deoxidized (contains Ti, Zr, Al) — good for out-of-position, excellent on oxidized or contaminated steel |
| **ER70S-6** | General mild steel GTAW — higher Mn + Si deoxidizers — better for scale and mill residue, slightly higher spatter in GMAW mode |

**Most code shops specify ER70S-2 for GTAW root passes** on pressure pipe because of its superior deoxidation and root-pass appearance.[^6]

---

## 1G and 2G Plate Welds — GTAW

### 1G (flat) plate — technique overview

For 1G groove welds with GTAW:

- **Body position:** forearms rested on the bench — maximize stability
- **TORCH angle:** 15–20° drag (backhand), slight work angle toward the torch travel direction
- **FILLER addition:** add filler with the non-dominant hand at the leading edge of the puddle — dip the rod in and out of the puddle in a regular cadence (dip technique)
- **Arc length:** 2–3 mm (roughly one tungsten diameter) — too long = oxidation and contamination. Too short = contamination of tungsten by touching the filler or puddle.
- **Travel speed:** steady, slow — GTAW is a slow process. Quality over speed.

### 2G (horizontal) plate — technique differences

In 2G horizontal GTAW:

- **Stringer beads only** — the GTAW puddle is fluid and sags in horizontal position
- **Torch angle tilted upward:** 5–10° above horizontal to counter sag — the arc force pushes the puddle slightly upward
- **Filler addition:** add at the top of the puddle — let the puddle flow slightly downward after the addition to keep the bead centered
- **Multiple passes:** more passes are required than 1G to fill the joint without puddle sag

---

## 3G Plate — GTAW Root + SMAW E7018 Fill/Cap (All Uphill)

This combination is the AIT Period 3 plate procedure. All passes are uphill.[^1][^2]

### Joint preparation

- **Plate:** 3/8" (10 mm) minimum mild steel
- **Bevel:** 30° per side (60° included)
- **Root face:** 3/32" (2.4 mm) — slightly larger than for SMAW, because GTAW generates more precise heat at the root
- **Root gap:** 3/32" (2.4 mm) — same as root face width
- **Fit-up:** tack at each end and optionally in the middle; tack with GTAW

### GTAW Root Pass — 3G Uphill

- **Electrode:** 2% ceriated tungsten, 3/32" (2.4 mm) diameter, ground to a point
- **Filler:** ER70S-2, 1/16" (1.6 mm) diameter
- **Shielding gas:** 100% Ar, 10–12 L/min
- **Amperage:** 80–110 A DCEN — use a foot pedal (current control pedal) for uphill work to adjust amperage as the joint heats up
- **Technique:**
  - Establish a puddle at the start; wait until you can see through to the back of the joint (keyhole forms)
  - Add filler at the leading edge of the puddle in a consistent rhythm
  - Travel UPHILL — torch angled upward (10–15° drag)
  - The keyhole should remain constant in size — adjust travel speed and amperage via pedal to maintain it

### SMAW E7018 Fill and Cap — 3G Uphill

After the GTAW root is complete:
- **Slag check:** GTAW produces no slag, but inspect the root surface for color (gold = good shielding, blue = marginal, black = poor shielding — grind and re-pass)
- **Switch to SMAW:** pick up E7018, 1/8" (3.2 mm)
- **Hot pass (E7018):** 100–115 A uphill — first E7018 pass over the GTAW root
- **Fill passes:** 105–120 A, triangle weave, pause at toes
- **Cap:** 100–115 A, wider weave, extend past toes slightly
- **All passes uphill** — the AIT/W47.1 procedure specifies uphill for all SMAW passes in 3G

---

## 2G and 5G Pipe — GTAW Root

For pipe welds, the GTAW root pass is the most technically demanding application of the process.[^4][^5]

### Pipe joint preparation — GTAW root

| Parameter | Value |
|---|---|
| **Pipe size** | 150 mm (6") NPS for qualification |
| **Wall thickness (Sch 80)** | 10.97 mm |
| **Bevel** | 30° per side (60° included) |
| **Root face (land)** | 1/16" to 3/32" (1.6–2.4 mm) |
| **Root gap** | 1/16" to 3/32" (1.6–2.4 mm) — tighter than SMAW, because GTAW heat is more precisely controlled |
| **Filler rod** | ER70S-2, 1/16" (1.6 mm) |

### Backing gas purge — when and how

For code pressure piping, the inside of the pipe at the root weld zone must be purged with inert gas during GTAW:[^5]

- **Purpose:** the GTAW root bead is exposed to both the outside (shielded by the torch cup) and the inside (open to atmosphere). Without purge, the inside of the root bead oxidizes heavily — "sugaring" occurs (a gray, rough, granular oxide layer forms on the back side).
- **Purge gas:** 100% argon
- **How:** block the pipe 300–600 mm from the weld with pipe end caps, foam dams, or commercial purge systems. Flow argon into the blockade and let it displace air. Check oxygen content at the outlet — purge is complete when O₂ < 0.5% (use an oxygen monitor).[^5]
- **Flow rate:** 5–10 L/min during welding — just enough to maintain positive pressure
- **Verify:** after the root pass, inspect the inside (with a flashlight and mirror through the pipe end) — the back bead should be smooth silver-gold, not gray-sugared

**For the AIT qualification coupon (short spool sections):** purge is typically not required at school — the short open ends allow adequate argon fill. Verify with your instructor.

---

## 2G Pipe — GTAW Root

2G pipe is a vertical pipe, weld runs horizontally around the circumference.

- **Work around the pipe:** the welder walks around the fixed pipe, maintaining consistent torch and filler angle throughout
- **Torch angle:** 15° in direction of travel (horizontal, backhand), 5–10° tilt pointing inward toward the pipe center
- **Filler:** add at the leading edge of the horizontal puddle; gravity pulls the puddle slightly downward — add filler at the top of the puddle to compensate
- **Travel speed:** consistent — watching the keyhole and the bead shape constantly

---

## 5G Pipe — GTAW Root

5G pipe is fixed horizontal — the welder welds all positions in one pass around the pipe.[^4]

**Two-half method (same as SMAW 5G):**

### Lower half — 6 o'clock to 9 o'clock (right side going up) and 6 o'clock to 3 o'clock (left side going up)

Many experienced GTAW pipe welders use a **walking the cup** technique:

**Walking the cup:** the GTAW cup (ceramic nozzle) rests on the bevel face or root land. The welder "walks" the cup along the joint, keeping it in contact with the pipe surface. This provides automatic standoff control — the cup physically maintains arc length. It's especially effective in horizontal (2G) and 5G positions.[^4]

- **Cup size:** 6 to 8 (3/8" to 1/2") cup diameter — large enough to maintain gas coverage while walking
- **Tungsten stick-out:** extended to 10–15 mm beyond the cup face for the walking technique
- **Technique:** the cup contacts the bevel face and "rocks" or "walks" along the joint as the welder moves. Filler is added continuously.

**Walking the cup is NOT permitted in all welding positions** — it requires the cup to contact the pipe. In the overhead zone (6 o'clock), the cup may be awkward to contact — some welders switch to a free-hand technique at the overhead portion.

### Overhead zone (at 6 o'clock in 5G)

- **Freehand technique:** hold the cup slightly away from the pipe surface
- **Foot pedal:** reduce amperage as the puddle heats up in the overhead zone — gravity and heat buildup combine to create overflow risk
- **Short arc:** critical overhead — longer arc = more heat and less precise control

---

## 6G Pipe — GTAW Root + SMAW Fill/Cap

The 6G position is a pipe inclined at 45° to horizontal, fixed — no rotation.[^1][^2]

**Why 6G is the master test:**
- The pipe is inclined, so every position around the circumference is a combination of overhead, vertical, and horizontal — no position is "pure"
- The inclined position requires the welder to constantly adjust technique as the joint angle changes
- Gravity effects are constant but changing throughout the joint

**6G qualification scope (ASME Section IX, CSA W47.1 Annex B):**
- A 6G GTAW+SMAW qualification covers: ALL pipe positions (1G, 2G, 5G, 6G) AND all plate positions (1G, 2G, 3G, 4G)[^1][^2]
- This is why the 6G is the gold standard — one test qualifies everything

### 6G joint preparation

Same as 5G — 60° included bevel, 1/16"–3/32" land, same root gap.

### 6G GTAW root technique

The inclined position means different zones of the joint present as follows:[^4]

| Zone | Clock position on 6G pipe | Welding condition |
|---|---|---|
| **Top** | 12 o'clock | Flat-like — easiest zone |
| **Downhill side (low side)** | 3 o'clock | Combination downhill and horizontal — filler runs downhill |
| **Bottom** | 6 o'clock | Overhead-like — hardest zone |
| **Uphill side (high side)** | 9 o'clock | Combination uphill and horizontal — best fusion side |

**Filler management in 6G:** on the low-slope side (3 o'clock), the filler rod and puddle tend to flow downhill. Add filler at the upper portion of the puddle; let the puddle flow upward-rearward slightly before the next dip. On the uphill side (9 o'clock), add filler at the leading edge — puddle stays where it's placed.

### Amperage management in 6G

Foot pedal is essential for 6G quality:[^3][^4]

- **12 o'clock (flat-ish):** set amperage — 90–110 A
- **3 o'clock (low side):** reduce 5–10% as heat builds
- **6 o'clock (overhead):** reduce 10–15% — maximum control needed
- **9 o'clock (high side):** return toward original amperage — the uphill side dissipates heat faster

---

## Weld Defects Specific to GTAW Pipe

| Defect | Cause | Prevention |
|---|---|---|
| **Tungsten inclusion** | Tungsten touched the puddle or filler rod | Maintain arc length; keep filler at the puddle edge, not in the arc |
| **Porosity** | Contamination (moisture, oil), poor shielding, gas purity | Clean the joint; verify gas purity; adequate flow rate; check for drafts |
| **Sugared root (inside)** | No backing gas purge — oxide forms on back side | Use backing gas purge when specified; inspect inside before next pass |
| **Cold root (incomplete penetration)** | Travel too fast; arc too long; root face too large | Slow down; shorten arc; verify keyhole is maintained |
| **Suck-back** | Excess heat at root; too slow travel | Increase speed; reduce amperage via pedal |
| **Undercut at toes** | Arc too long; travel too slow for amperage | Shorten arc; maintain consistent travel |

---

## GTAW + SMAW Combination — Pass Inspection Between Process Switch

When switching from GTAW root to SMAW fill:[^3]

1. **Inspect the GTAW root:** check for color (gold to straw = acceptable; blue = marginal; gray/black = poor shielding, reject and re-pass)
2. **Inspect for defects:** check for porosity, suck-back, cold lap, or tungsten inclusions (bright shiny spots in the bead = tungsten)
3. **Clean:** wire brush with stainless wire brush (dedicated — not used on carbon steel)
4. **Grind if needed:** grind out any defects before SMAW fills over them
5. **Switch electrodes:** SMAW E7018, 1/8" — verify rod oven temperature before taking electrodes out

---

## Numbers you need to memorize

- **6G qualification scope:** all pipe AND plate positions[^1][^2]
- **Tungsten for DCEN mild steel:** 2% ceriated (gray) or 2% thoriated (red)[^3]
- **Tungsten grind:** tapered point, 15–30° included angle, ground parallel to axis[^3]
- **Shielding gas:** 100% argon, 10–15 L/min[^5]
- **ER70S-2 filler for GTAW root:** preferred — triple-deoxidized[^6]
- **Root face for GTAW pipe:** 1/16"–3/32" (1.6–2.4 mm)[^3]
- **Root gap for GTAW pipe:** 1/16"–3/32" (1.6–2.4 mm)[^3]
- **GTAW amperage (3/32" tungsten, DCEN mild steel):** 80–110 A[^3]
- **Walking the cup:** cup contacts the bevel face — automatic standoff control technique[^4]
- **Backing gas purge O₂ limit:** < 0.5% O₂ before welding root[^5]
- **6G pipe inclination angle:** 45° to horizontal[^1]

---

## What the textbook doesn't tell you

**The 6G is as much mental as physical.** The moment you sit down to start the 6G qualification test, there's a mental dimension that no amount of textbook reading addresses. You're tracking arc length, filler rhythm, puddle shape, keyhole size, travel speed, amperage via pedal, torch angle, AND body position — simultaneously — for an extended period. The welders who pass 6G on the first try are not superhuman; they have practiced until each of those variables is automatic, freeing their conscious attention to monitor overall quality.[^4]

**Walking the cup changes everything.** A welder who has never used the walking-the-cup technique and then learns it often says: "Where has this been my whole career?" The automatic arc length from the cup contact dramatically reduces one dimension of the cognitive load. If your school has instructors who know this technique, learn it. It is widely used in pressure piping GTAW.[^4]

**Backing gas is non-negotiable on code pressure pipe.** On a real 6G qualification test for a pressure vessel or B31.3 piping company, you will use backing gas. Practice it before the test. Discovering that your root has "sugared" on the inside surface during visual inspection of the completed coupon is a heart-sinking moment that happens to unprepared welders.[^5]

**The SMAW switch requires a re-calibration of your hands.** GTAW is a two-handed, fine-motor-control process. SMAW is a one-handed, higher-energy process. When you switch from GTAW root to SMAW E7018 for the hot pass, give yourself a few seconds to re-establish grip, verify rod angle, and find your amperage setting. Rushing the hot pass produces an overheated root.[^3]

**ER70S-2 for code work; ER70S-6 when the base is dirty.** On the exam, both are acceptable for mild steel GTAW — but ER70S-2 is the code preference for pressure piping root passes because its triple-deoxidization handles any residual surface contamination better. If the exam asks "which filler is preferred for code quality GTAW root passes on mild steel pipe?" — ER70S-2.[^6]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s5-a-6g-pipe-position.svg` — side view of 6G pipe position: pipe at 45° to horizontal, fixed, with weld position zones labeled (12 o'clock = top, 6 o'clock = bottom, 3 and 9 o'clock on sides) — showing the compound angles each zone presents)*

*(SVG to be added: `assets/diagrams/p3-s5-a-walking-cup.svg` — cross-section of GTAW cup walking on bevel face: cup contact point on bevel, tungsten stick-out, arc gap, puddle, keyhole — showing the mechanical standoff control)*

*(SVG to be added: `assets/diagrams/p3-s5-a-tungsten-grind.svg` — three tungsten tip profiles: correctly pointed (15–30° taper, parallel grinding marks), over-ground (needle tip), contaminated (balled, smeared) — each with the recommended and unacceptable label)*

*(SVG to be added: `assets/diagrams/p3-s5-a-gtaw-smaw-combination.svg` — cross-section of 3G groove weld showing: GTAW root pass (labeled), SMAW E7018 hot pass (labeled), SMAW E7018 fill passes (labeled), SMAW E7018 cap (labeled) — each pass in a different color/pattern)*

---

## Key terms

- **GTAW (Gas Tungsten Arc Welding):** the TIG process — non-consumable tungsten electrode, shielded by inert gas, filler added manually
- **6G:** inclined pipe position (45°) — fixed, no rotation — the highest-level pipe qualification
- **5G:** horizontal pipe — fixed, no rotation — all positions in one joint
- **2G (pipe):** vertical pipe — fixed — weld progresses horizontally around the circumference
- **DCEN (Direct Current Electrode Negative):** the polarity for mild steel and stainless steel GTAW — the electrode is negative
- **Ceriated tungsten (EWCe-2):** the preferred non-radioactive tungsten for DCEN GTAW — gray color code
- **ER70S-2:** triple-deoxidized mild steel GTAW filler — the code-preferred choice for pressure pipe root passes
- **Walking the cup:** GTAW technique where the ceramic cup contacts the bevel face, providing automatic arc length control
- **Backing gas purge:** inert gas (argon) flowing inside the pipe at the weld zone to protect the root bead from atmospheric oxidation
- **Sugaring:** the granular, gray oxide that forms on the inside of a stainless or mild steel GTAW root weld when backing gas is inadequate
- **Keyhole:** the through-opening at the leading edge of the GTAW root puddle — indicates proper penetration
- **Foot pedal:** the amperage control pedal on a GTAW power source — essential for position welding
- **Tungsten inclusion:** a fragment of tungsten electrode embedded in the weld — a rejectable defect, visible as a bright spot on radiograph

---

## Common exam trap

- **6G = 45° inclined pipe — fixed, no rotation.** Not 45° to horizontal on a flat plate. Not a variation of 5G. A specific position that qualifies ALL other positions.
- **GTAW polarity for mild steel = DCEN** (electrode negative). AC is ONLY for aluminum/magnesium (cleaning action required). Wrong polarity on mild steel GTAW = balled, contaminated tungsten and bad weld.
- **Pure tungsten (green) = AC ONLY** — never use pure tungsten on DCEN. It balls up immediately.
- **ER70S-2 vs ER70S-6:** both are for mild steel. ER70S-2 is triple-deoxidized (preferred for code root passes on pressure pipe). ER70S-6 is higher-silicon, preferred for surface-contaminated base metal. The exam may ask "which is preferred for GTAW root on pressure pipe?" — ER70S-2.
- **Walking the cup provides automatic arc length control** — NOT automatic filler control. The welder still controls filler addition rate manually.
- **Backing gas purge limit: O₂ < 0.5%** — not < 5%, not just "until gas flows." Monitor with an O₂ meter.
- **6G qualification covers everything: all pipe AND plate positions** under both ASME IX and CSA W47.1. This is the key fact about 6G — it is the universal qualification.

---

## Practice question preview

**Q:** A welder completes a GTAW root pass on 6" Schedule 80 pipe in the 6G position. Upon inspection of the back side (inside the pipe), the root bead shows a gray, granular, rough texture. What caused this and what is the correct remedy?

A) The tungsten was contaminated — the bead must be ground out and re-welded with a fresh tungsten  
B) The shielding gas flow rate was too high — reduce to 8 L/min and re-inspect  
C) Backing gas was insufficient or absent, causing atmospheric oxidation of the root bead — the affected area must be ground out completely and re-welded with proper backing gas purge  
D) The filler metal (ER70S-6) was incorrect — re-weld using ER70S-2

**Correct: C**

**Explanation:** The gray, granular, rough texture on the back side of a GTAW root bead is called "sugaring" — it is chromium oxide (in stainless) or iron oxide (in mild steel) formed by the root bead being exposed to atmospheric oxygen during welding. The cause is absent or inadequate backing gas purge. The remedy is to grind out the affected area completely (the oxidized zone cannot be fused over — it will become a slag inclusion or lack of fusion) and re-weld with proper backing gas purge, confirmed to < 0.5% O₂ before welding. Tungsten contamination (Option A) appears as bright metallic inclusions, not surface roughness. Excess shielding flow (B) causes turbulence and drawing-in of air, but the primary symptom is not the specific "sugaring" appearance. Wrong filler rod (D) does not cause this specific appearance.

**Red Seal mapping:** D-15.04 (Performs weld using GTAW equipment), A-5.01 (Performs quality inspection)

---

[^1]: [CSA W47.1 — Certification of Companies for Fusion Welding of Steel](https://www.csagroup.org/store/product/CSA%20W47%3A1/); Annex B (GTAW qualification matrix: 6G covers all pipe and plate positions), GTAW+SMAW combination procedures
[^2]: [ASME BPVC Section IX — Welding Qualifications](https://www.asme.org/codes-standards/find-codes-standards/bpvc-ix-boiler-pressure-vessel-code-section-ix-welding-brazing); QW-350 to QW-399 (GTAW performance qualification), 6G scope (covers all pipe: 1G/2G/5G/6G and all plate: 1G/2G/3G/4G)
[^3]: [Lincoln Electric — GTAW Welding Guide](https://www.lincolnelectric.com/en/education-center/welding-education/gtaw-welding-guide); DCEN polarity for mild steel, tungsten grind (15–30° taper, parallel), 100% Ar shielding, amperage ranges, dip technique, 3G uphill procedure
[^4]: [Miller Electric — TIG Welding Fundamentals and Advanced Pipe Welding](https://www.millerwelds.com/resources/article-library/tig-welding-fundamentals); walking the cup technique, 6G position zone analysis, foot pedal management, 5G two-half method for GTAW
[^5]: [ESAB — GTAW Handbook and Process Guide](https://www.esab.com/us/nam_en/education/blog/gtaw-tig-welding-guide/); shielding gas flow rates (10–15 L/min), backing gas purge for pipe (O₂ < 0.5%), sugaring definition, gas purity requirements (99.99%)
[^6]: [AWS A5.18 — Carbon Steel Electrodes and Rods for GTAW](https://pubs.aws.org/p/1141/a518a518m2005-specification-for-carbon-steel-electrodes-and-rods-for-gas-shielded-arc-welding); ER70S-2 (triple-deoxidized — preferred for code pressure pipe GTAW root) vs ER70S-6 (higher Si, preferred for contaminated base metal)
