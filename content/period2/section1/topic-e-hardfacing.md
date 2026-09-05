---
id: p2-s1-e
period: 2
section: 1
section_title: Foundational Skills, Safety, Procedures and Properties of Metals
topic_letter: E
topic_title: Hardfacing
hours: 2
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to describe and identify hardfacing applications, procedures, and consumables.
objectives:
  - Describe the hardfacing process and applications.
  - Identify the types of wear.
  - Identify filler metals for hardfacing.
  - Identify the problems associated with hardfacing and how to avoid them.
  - Describe the procedures for applying hardfacing materials with filler wires.
red_seal_mapping:
  - A-5.05 (Selects welding processes and power source)
  - D-13.04 (Performs weld using SMAW equipment)
  - A-5.03 (Controls temperature of weldments)
citations:
  - source: Lincoln Electric — Hardfacing Product and Procedures Selection
    ref: Wear types, electrode selection guide, overlay procedures, chrome carbide, tungsten carbide, austenitic Mn classifications
    url: https://www.lincolnelectric.com/assets/global/products/consumable_hardfacingelectrodes-lincore/c4100.pdf
  - source: ESAB — Hardfacing and Overlay Welding Guide
    ref: Wear mechanism identification, filler metal selection by application, FCAW hardfacing procedure
    url: https://www.esab.com/us/nam_en/education/hardfacing.cfm
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 27 — Hardfacing; wear types, consumable families, application techniques
    url: https://www.g-w.com/modern-welding
  - source: AWS A5.21 — Specification for Bare Electrodes and Rods for Surfacing
    ref: Classification of hardfacing electrodes/rods (Fe-based, Co-based, carbide composites)
    url: https://pubs.aws.org/p/1152/a521a5-21m2011-specification-for-bare-electrodes-and-rods-for-surfacing
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic E
    ref: pp. 30–31
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Hardfacing

A bucket tooth on a bulldozer working in Alberta oil sands gravel will wear out in days if made from plain mild steel. Apply a hardfacing overlay — a weld deposit of ultra-hard alloy — and the same tooth lasts weeks. Hardfacing is a specialty that keeps heavy equipment alive in Canada's most abrasive environments: mining, oil sands, agriculture, and aggregate processing. It's one of the few welding skills where *understanding metallurgy pays off every day*.

---

## What is hardfacing?

Hardfacing (also called **surfacing** or **overlay welding**) is the application of wear-resistant filler metal to a base material surface using a welding process. The goal is NOT a structural weld — it's to deposit a hard, wear-resistant layer on the surface of a part that otherwise wouldn't last in service.[^1][^3]

**Hardfacing is applied:**
- To new parts before first service (preventive hardfacing)
- To worn parts to restore dimension and add wear resistance (rebuilding + hardfacing)

**It is NOT intended to:**
- Join two pieces together
- Replace base metal in a structural load-carrying capacity
- Be machined flat (most hardfacing alloys are too hard to machine — they're ground only or used as-deposited)

---

## Types of wear — match the hardfacing to the enemy

This is the central skill of hardfacing selection. Wrong wear type → wrong hardfacing → short life.[^1][^2]

### 1. Abrasive wear (most common in Alberta)
The surface is scratched, ground, or gouged by harder particles.

- **Low-stress abrasion (scratching abrasion):** Fine particles (sand, dirt) slide across the surface. Think: the outside of a screw conveyor handling dry grain.
  - **Hardfacing choice:** Chrome carbide or complex carbide overlay (very high hardness, ~60–70 HRC)
- **High-stress abrasion (grinding abrasion):** Coarse particles are crushed between two surfaces. Think: crusher rolls, jaw liners, ball mill liners.
  - **Hardfacing choice:** Complex carbide, tungsten carbide composite
- **Gouging abrasion:** Large rocks or hard objects hit and dig into the surface. Think: bucket teeth, dipper lips, drilling bits.
  - **Hardfacing choice:** Austenitic manganese steel (Hadfield steel) OR complex carbide — the material must be tough enough to resist impact AND hard enough to resist gouging

### 2. Impact wear
Repeated blows absorb energy. The surface must be tough, not just hard. Hard-but-brittle hardfacing cracks and spalls under impact.
- **Hardfacing choice:** Austenitic manganese steel (work-hardens under impact → gets harder in service!), or pearlitic/martensitic steel overlays with moderate hardness

### 3. Metal-to-metal wear (friction and galling)
Two metal surfaces sliding against each other. Think: rail/wheel interface, gear teeth.
- **Hardfacing choice:** Cobalt-chromium alloys (Stellite-type), austenitic stainless overlay for corrosion-wear combination

### 4. Erosion
High-velocity particles or fluid stream removes surface material. Think: pump impellers, slurry pipelines.
- **Hardfacing choice:** Chrome carbide for abrasive slurry; stainless or cobalt for corrosive fluid erosion

### 5. Corrosion + wear combined
- **Hardfacing choice:** Cobalt-base (Stellite) or nickel-chrome overlays

---

## Hardfacing filler metal families

### Chrome carbide (Cr₇C₃ / Cr₂₃C₆ composite)[^1][^2]
- **Hardness:** 55–65 HRC as-deposited
- **Best for:** Low-stress abrasion, fine particle abrasion (grain elevators, agricultural equipment)
- **Characteristics:** Brittle under impact; check pattern cracking is *normal* and expected in the overlay — it relieves thermal stress. Do NOT try to eliminate check cracking.
- **Process:** SMAW, FCAW, GMAW

### Tungsten carbide (WC) composite[^1]
- **Hardness:** 60–70 HRC composite; carbide particles ~2000 HV
- **Best for:** Extreme abrasion (drill bits, PDC cutter pads, mixer paddles)
- **Characteristics:** The hardest commercially available hardfacing; expensive; applied in thin layers because thick overlays crack

### Austenitic manganese steel (Hadfield steel, ~12% Mn)[^1][^2]
- **Hardness:** 15–25 HRC as-deposited; work-hardens to ~50 HRC in service
- **Best for:** High-impact gouging abrasion; crusher parts, railway track crossings, bucket teeth on rocky ground
- **Characteristics:** The base metal MUST be austenitic manganese steel (cannot be applied to carbon steel without intermediate layers); work-hardens under repeated impact — this is its superpower
- **Critical:** Do NOT preheat austenitic Mn steel! Preheat above 260°C causes carbide precipitation at grain boundaries → embrittlement and catastrophic cracking.[^1] Weld with LOW amperage, short beads, allow to cool between passes.

### Martensitic steel overlay[^1]
- **Hardness:** 35–55 HRC
- **Best for:** Metal-to-metal wear, cam surfaces, moderate abrasion with some impact
- **Characteristics:** Moderate toughness and hardness; can be used on carbon steel base

### Cobalt-base (Stellite-type)[^1][^2]
- **Hardness:** 25–55 HRC depending on grade
- **Best for:** High-temperature wear, corrosion + wear, metal-to-metal in chemical environments
- **Characteristics:** Expensive; used in valves, pump impellers, cutting edges in chemical plants

---

## Application procedures: SMAW hardfacing

Most field hardfacing is done with SMAW (stick) because of portability and the wide range of hardfacing electrodes available.[^1]

### General procedure:[^1][^3]

1. **Identify the wear type** — this determines the electrode
2. **Inspect the base metal** — if rebuilding a worn part, determine if a build-up layer (usually with a tough low-alloy filler like E7018) is needed before the hardfacing overlay
3. **Clean the surface** — remove grease, oil, rust, paint, and old hardfacing to bare metal
4. **Preheat if required** — carbon steel base metals often need preheat (see CE formula). Austenitic Mn base: NO preheat.
5. **Apply in thin layers** — typically 2–3 mm per pass for chrome carbide; thicker layers increase risk of spalling
6. **Inter-pass temperature control** — for carbide overlays, keep cool; for Mn steel, keep cool (no preheat); for martensitic overlays, control to avoid hydrogen cracking
7. **Pattern the overlay beads** — stringer beads side-by-side (for flat wear surfaces) OR cross-hatch (50% overlap) pattern to ensure full coverage without low spots
8. **Allow to cool** — in still air; do NOT quench. Quenching causes rapid thermal shock cracking in carbide overlays.

### Application with FCAW wire (production hardfacing):[^2]
FCAW allows much faster deposition rates than SMAW. Chrome carbide FCAW wires (e.g., Lincoln Lincore series, ESAB Stoody series) are common in equipment rebuild shops.
- Maintain CTWD per manufacturer's wire data sheet
- DCEP polarity for most FCAW hardfacing wires
- Use same cooling/interpass rules as SMAW

---

## Common hardfacing problems and how to avoid them

| Problem | Cause | Prevention |
|---|---|---|
| **Spalling (chunks breaking off)** | Too many overlay layers; brittle hardfacing under impact load; base metal contamination | Limit overlay to 2–3 layers max; match hardfacing type to wear type; clean base metal thoroughly |
| **Cracking of base metal HAZ** | No preheat on carbon steel base; high carbon equivalent | Preheat per CE formula; use build-up layer before hardfacing |
| **Austenitic Mn steel embrittlement** | Preheat above 260°C or slow interpass cooling | NO preheat; cool between passes; fast travel speed |
| **Poor adhesion / delamination** | Contaminated base metal; wrong electrode for base metal | Wire brush, grind, or blast to bare metal; verify electrode compatibility |
| **Rapid re-wear after hardfacing** | Wrong hardfacing for wear type | Re-identify wear mechanism; select correct family |
| **Check cracks in chrome carbide** | Normal thermal relief — NOT a defect | Accept as normal; do not attempt to fill or repair |

---

## Numbers you need to memorize

- **Chrome carbide hardness:** 55–65 HRC as-deposited[^1]
- **Tungsten carbide hardness:** 60–70 HRC composite[^1]
- **Austenitic Mn steel: NO preheat above 260°C** — critical rule[^1]
- **Austenitic Mn in-service hardness:** up to ~50 HRC after work-hardening (starts ~15–25 HRC)[^1]
- **Check cracking in chrome carbide = normal** — do not repair[^1]
- **Maximum overlay layers (general):** 2–3 (more increases spalling risk)[^1]
- **Build-up layer before hardfacing:** typically E7018 or equivalent low-alloy to restore dimension[^1]

---

## What the textbook doesn't tell you

**Check cracking is the number one thing apprentices get wrong on hardfacing.** They see cracks in a finished overlay and try to grind them out or fill them. Don't. Chrome carbide overlays crack in a regular check pattern as the hard deposit relieves its own internal stress. This is designed-in behaviour. The cracks are shallow and do not propagate into the base metal. Filling them just restarts the cycle.

**Rebuilding first, hardfacing second.** A worn tooth that's 20 mm undersize needs 15 mm of build-up with a tough low-alloy electrode (E7018 family) to get close to size, then 2–3 mm of hardfacing for wear resistance. Applying hardfacing directly to a severely worn surface wastes expensive hardfacing material and leaves the wrong hardness profile where it matters (near the substrate interface).

**Austenitic manganese preheat is a genuine safety issue.** A crusher jaw that's been hardfaced with preheat can fail catastrophically in service. The carbide precipitation at grain boundaries makes the part brittle in a way that's invisible until it shatters under load. This is not a theoretical risk — it happens in the field.

---

## Key terms

- **Hardfacing:** weld deposit applied to a surface to resist wear, not to join parts
- **Surfacing:** general term for applying one metal to another surface (includes hardfacing, build-up, cladding)
- **Build-up:** applying filler metal to restore a worn surface to size before hardfacing
- **Chrome carbide:** Cr₇C₃ / Cr₂₃C₆ hard phases; extreme abrasion resistance; brittle under impact
- **Tungsten carbide:** WC particles in a metal matrix; highest available hardness
- **Austenitic manganese steel (Hadfield steel):** ~12% Mn steel that work-hardens under impact; not preheated
- **Work-hardening:** increase in hardness caused by plastic deformation under service load — austenitic Mn's superpower
- **Check cracking:** regular crack pattern in chrome carbide overlays — normal thermal stress relief; not a defect
- **Spalling:** chunks of overlay breaking away from the base metal — caused by too many layers or wrong filler choice
- **Cobalt-base (Stellite-type):** cobalt-chrome overlay for high-temperature, corrosion + wear applications
- **Abrasive wear:** surface removal by hard particles (most common wear type in Alberta industries)

---

## Common exam trap

- **Check cracks in chrome carbide are NORMAL** — not a defect requiring repair. Exam writers love asking if check cracks are acceptable. Answer: yes, they are normal and expected.
- **Austenitic manganese steel: NO preheat, and that is correct procedure** — not an oversight. The question will phrase this as a "correct procedure" vs "incorrect procedure" choice.
- **Build-up layer ≠ hardfacing** — they use different filler metals. Build-up uses tough filler (like E7018 family); hardfacing uses wear-resistant alloys. Using a hardfacing electrode for build-up wastes expensive material and creates a brittle transition.
- **Hardfacing is matched to wear TYPE, not severity** — the question will describe a high-impact scenario and list chrome carbide as an option. Chrome carbide is for abrasion, not impact; it spalls under high impact. The right choice is Mn steel or martensitic overlay.
- **FCAW hardfacing uses DCEP** for most chrome carbide wires — same as all FCAW-G. Don't confuse with FCAW-S (DCEN).

---

## Practice question preview

**Q:** A crusher jaw liner made of austenitic manganese steel (12% Mn) is being rebuilt with a hardfacing overlay. The welder preheats the base metal to 250°C before welding to prevent hydrogen cracking. Is this correct procedure?

A) Yes — preheat above 150°C is always required for alloy steel hardfacing
B) Yes — 250°C is within the safe preheat range for Mn steel
C) No — austenitic manganese steel must NOT be preheated; heat above 260°C causes carbide precipitation and embrittlement
D) No — austenitic Mn steel must be preheated to at least 350°C for proper fusion

**Correct: C**

**Explanation:** Austenitic manganese (Hadfield) steel is uniquely sensitive to heat. Holding it above 260°C or allowing slow cooling through that range causes carbides to precipitate at grain boundaries, destroying the toughness that makes the material valuable. Preheated Mn steel can shatter in service without warning. The correct approach is NO preheat, short beads, allow to cool between passes, and use low amperage.

**Red Seal mapping:** A-5.03 (Controls temperature of weldments); D-13.04 (Performs weld using SMAW equipment)

---

[^1]: [Lincoln Electric — Hardfacing Product and Procedures Selection (C4100)](https://www.lincolnelectric.com/assets/global/products/consumable_hardfacingelectrodes-lincore/c4100.pdf); wear type identification, electrode selection guide, Mn steel precautions, check cracking explanation, overlay layer limits
[^2]: [ESAB — Hardfacing and Overlay Welding Guide](https://www.esab.com/us/nam_en/education/hardfacing.cfm); wear mechanism classification, chrome carbide and tungsten carbide properties, FCAW hardfacing procedures
[^3]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 27 — Hardfacing; process description, application technique, consumable families
[^4]: [AWS A5.21 — Specification for Bare Electrodes and Rods for Surfacing](https://pubs.aws.org/p/1152/a521a5-21m2011-specification-for-bare-electrodes-and-rods-for-surfacing); hardfacing electrode/rod classification system (Fe-base, Co-base, carbide composites)
[^5]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic E](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 30–31
