---
id: p1-s1-f
period: 1
section: 1
section_title: Foundational Skills, Safety and Procedures
topic_letter: F
topic_title: Oxyfuel Equipment and Cutting
hours: 37
weight_pct: 15
outcome: >
  Upon successful completion, learners will be able to assemble, adjust, operate,
  shut down, and maintain oxyfuel equipment; perform hand-held and machine oxyfuel
  cuts on mild steel plate, pipe, and structural shapes.
objectives:
  - Identify causes and preventive measures for backfires, flashbacks and burn backs.
  - Describe how to operate a hand-held oxyfuel cutting torch on mild steel plate and structural shapes.
  - Describe the characteristics and handling procedures for oxygen and fuel gases.
  - Describe the functions of oxyfuel equipment components.
  - Explain the procedure for placement, set-up and shutting down of oxyfuel equipment.
  - Demonstrate the use, care and maintenance of oxyfuel equipment components.
  - Describe pressure and flame adjustments.
  - Perform straight line, bevel, and shape cutting on mild steel.
  - Pierce and cut holes in mild steel plate.
  - Cope 3/8 in. mild steel to fit a 100 mm (4 in.) C shape.
  - Perform cuts on structural shapes.
  - Operate a machine oxyfuel cutting torch on mild steel plate and pipe.
red_seal_mapping:
  - C-10.01 (Sets up oxy-fuel gas cutting equipment)
  - C-10.02 (Performs oxy-fuel gas cutting)
  - C-10.03 (Performs oxy-fuel gas shape cutting)
citations:
  - source: CSA W117.2 — Safety in Welding, Cutting, and Allied Processes (2019)
    ref: Clause 8 (compressed gas cylinders, storage, handling); Clause 9 (oxyfuel cutting and welding safety)
    url: https://www.csagroup.org/store/product/CSA%20W117.2%3A19/
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapters 11–13 (Oxyfuel Gas Welding and Cutting — equipment, flame types, cutting technique)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: Victor Technologies / ESAB — Oxyfuel Equipment Operator Manual (public)
    ref: Section 3 (regulator setup), Section 5 (torch lighting, flame adjustment), Section 7 (troubleshooting backfire/flashback)
    url: https://www.esabna.com/us/en/education/blog/oxy-fuel-cutting-guide.cfm
  - source: Lincoln Electric — Oxy-Fuel Cutting Guide (public)
    ref: Cutting tip selection chart, working pressures by tip size and material thickness
    url: https://www.lincolnelectric.com/en/education-center/welding-education/cutting
  - source: Red Seal Occupational Standard — Welder (2024), Block C, Task C-10
    ref: Sub-tasks C-10.01–C-10.03 performance criteria (OFC setup, operation, shape cutting)
    url: https://red-seal.ca/_conf/assets/custom/docms/welder/rsos-eng.pdf
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 1 Topic F
    ref: pp. 22–32
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Oxyfuel Equipment and Cutting

Oxyfuel cutting (OFC) is the oldest and still one of the most practical cutting processes in the trade. No power outlet needed, cuts steel up to 300 mm thick, and travels anywhere a cylinder cart can go. At 37 hours, this is the largest block in Period 1 — and every hour of it is hands-on.

---

## Oxygen and fuel gases — what you're actually working with

### Oxygen (O₂)

Stored in black cylinders in Canada (grey internationally). Oxygen supports combustion — it doesn't burn itself. The characteristics that matter for safety:[^1]

- **High-pressure storage:** industrial oxygen cylinders are filled to approximately **20 700 kPa (3 000 PSI)** at 21°C. That's not a pressure a regulator or connection failure tolerates gracefully.
- **Oil and grease prohibition:** oil contact with high-pressure oxygen causes spontaneous combustion and violent explosion. No petroleum-based lubricants, no grease-contaminated gloves, nothing oily near oxygen equipment — ever.[^1]
- **Oxygen enrichment:** even a slightly enriched atmosphere (above 23–25% O₂) makes ordinary materials catch fire far more easily. Welding clothing, cardboard, sawdust — all ignite at lower temperatures in enriched air.

### Acetylene (C₂H₂)

The most common fuel gas for OFC and oxyfuel welding (OFW). Dissolved in acetone inside porous media in maroon cylinders (Canada).[^2]

- **Cylinder pressure:** at 21°C, acetylene cylinders contain gas at approximately **1 700–1 900 kPa (250–275 PSI)**.
- **Acetylene instability:** acetylene becomes **chemically unstable and can self-detonate** at pressures above **103 kPa gauge (15 PSI gauge)**. This is not a regulatory preference — it's a chemistry limit. Never use acetylene above 15 PSI working pressure.
- **Withdrawal rate:** acetylene maximum withdrawal rate is **1/7 of cylinder capacity per hour** — exceeding this rate draws liquid acetone out of the cylinder, contaminating the process and damaging the torch.
- **Store and use upright.** If stored on its side, acetone settles to one end; if then used, acetone is drawn into the regulator. A cylinder stored on its side must stand upright for **at least 2 hours** before use.
- **Open valve max 1.5 turns** — so the cylinder can be quickly shut in an emergency. A cylinder fully opened can take many turns to shut.

### Propane and propylene

Alternatives to acetylene for cutting only (not suitable for OFW without special torches). Stored in liquid form in cylinders, heavier than air — vapour sinks to floor level.

- Propane cylinders: do not invert — liquid propane would flow into the regulator.
- Lower flame temperature than acetylene (~2 500°C vs ~3 100°C), requiring slightly longer preheating time to reach ignition temperature on thick steel.
- Better for machine cutting applications where preheat time is less critical.[^2]

---

## Equipment components and their functions

## Diagram
*(SVG to be added: `assets/diagrams/p1-s1-f-oxyfuel-system.svg` — labelled schematic of a complete oxyfuel setup: O₂ cylinder with valve cap, O₂ regulator with two gauges (cylinder pressure and working pressure), green O₂ hose, cutting torch body, mixing head, cutting attachment, cutting tip; and separately: acetylene cylinder with fusible plugs labeled, acetylene regulator, red hose, same torch body)*

### Cylinders

- **O₂ cylinder:** two gauges on regulator — left gauge shows cylinder contents pressure (high pressure gauge); right shows working pressure (line pressure gauge). Green hose. Right-hand (standard) threads on connections.
- **Acetylene cylinder:** same two-gauge principle, but cylinder pressure is lower. Red hose. **Left-hand thread** on regulator connection (acetylene and all fuel gases in Canada) — prevents accidentally connecting fuel to oxygen side.

**Why fuel gas fittings have left-hand threads:** a simple mechanical safety feature — you can't accidentally connect an acetylene regulator to an oxygen cylinder because the threads won't match. Always assume the notched hex nut on a hose fitting = fuel gas (left-hand thread). Standard hex nut = oxygen (right-hand thread).[^1]

### Regulators

Two-stage regulators are standard for industrial use:[^2]

- **First stage:** reduces cylinder pressure down to an intermediate pressure (typically 300–500 kPa).
- **Second stage:** reduces further to working pressure, controlled by the adjusting screw.

**Adjusting regulator pressure:**
1. Turn the adjusting screw counter-clockwise until free (no spring tension) before connecting.
2. Open the cylinder valve **slowly** — allow the high-pressure side to equalize before fully opening. Then open fully (O₂) or a maximum of 1.5 turns (acetylene).
3. Turn the adjusting screw clockwise to increase working pressure; counterclockwise to decrease.
4. Set working pressure with the gas flowing (blow-down method) — pressure set with gas flowing is more accurate than static pressure setting.

**Oxygen working pressure (cutting):** typically **270–415 kPa (40–60 PSI)** for common plate thicknesses, but always consult the tip manufacturer's chart.[^4]

**Acetylene working pressure:** set between **7–69 kPa (1–10 PSI)** — never above **103 kPa (15 PSI)**.[^1]

### Hoses

- **Oxygen hose:** green, right-hand thread fittings.
- **Fuel gas hose:** red, left-hand thread fittings.
- Twin-hose assemblies (joined) are common — easier to manage, less tangling.
- **Check condition before use:** cracks, cuts, oil contamination, or evidence of burning disqualify a hose from service.
- **Minimum hose length:** avoid coiling up excess hose on the cylinder — heat from the work area conducts back. Keep at least 2–3 m of hose extended.

### Check valves and flashback arrestors

Two critical safety devices:

- **Check valves (non-return valves):** prevent reverse gas flow — installed at the torch inlets. Stop gas from backing up into the hoses if a pressure imbalance occurs. Cheap insurance.
- **Flashback arrestors:** contain a temperature-sensitive shutoff that triggers if a flashback (burning flame front traveling back through the hose) reaches the arrestor. Should be installed at **both the regulator outlets AND the torch inlets** on all industrial setups.[^1]

### Cutting torches and tips

**Cutting torch construction:**
- **Body:** contains the mixing chamber for O₂ and fuel gas, control valves for each gas, and the cutting oxygen lever.
- **Cutting attachment/head:** connects to the body, holds the tip, and routes the high-pressure cutting oxygen through a separate channel.
- **Cutting tip:** the business end. Two types:
  - **One-piece tip (Prest-O-Lite/Harris style):** drilled all-in-one — preheat orifices ring the central cutting oxygen hole.
  - **Two-piece tip:** outer shell + inner copper insert — easier to clean.

**Tip selection by material thickness:**[^4]

| Plate thickness | Tip number (approximate) | O₂ cutting pressure |
|---|---|---|
| 3–6 mm (1/8–1/4 in) | 000–0 | 205–275 kPa (30–40 PSI) |
| 6–12 mm (1/4–1/2 in) | 0–1 | 275–345 kPa (40–50 PSI) |
| 12–25 mm (1/2–1 in) | 1–2 | 310–415 kPa (45–60 PSI) |
| 25–50 mm (1–2 in) | 2–3 | 345–480 kPa (50–70 PSI) |
| 50–100 mm (2–4 in) | 3–4 | 415–550 kPa (60–80 PSI) |

*Always verify with the specific tip manufacturer chart — numbers vary by brand.[^4]*

---

## Flame types

The flame is set by adjusting the ratio of oxygen to fuel gas. Three distinct flame types result:[^2]

### Neutral flame (the correct starting point for cutting)

Equal ratio of O₂ and C₂H₂ (approximately 1:1). Recognizable by:
- A bright, well-defined inner cone
- No feather beyond the inner cone
- Soft, rounded tip to the inner cone

The neutral flame is used as the reference — cut from it by opening the cutting oxygen lever. Do not start from a carburizing or oxidizing flame for cutting.

### Carburizing flame (excess acetylene / reducing flame)

More acetylene than oxygen. Recognizable by:
- An acetylene feather extending beyond the inner cone
- The feather length indicates how much excess acetylene there is
- Slightly lower temperature than neutral

Rarely used for cutting. Used for some OFW applications (e.g., high-carbon steel, silver brazing, some bronze welding).

### Oxidizing flame (excess oxygen)

More oxygen than acetylene. Recognizable by:
- A shorter, pointed inner cone
- Hissing sound
- Higher temperature than neutral — but oxidizes the steel surface

**Do not use an oxidizing flame for cutting mild steel** — it oxidizes the cut kerf excessively, creating rough, spattered edges and excessive dross.

## Diagram
*(SVG to be added: `assets/diagrams/p1-s1-f-flame-types.svg` — three side-by-side flame profiles showing carburizing (long feather), neutral (clean inner cone, no feather), and oxidizing (short sharp inner cone) with labels)*

---

## Lighting, adjusting, and shutting down — the correct sequence

### Lighting the torch (acetylene-fuelled)

1. **Check hose, tip, and connections** — no damage, no leaks.
2. **Open O₂ cylinder valve fully** (seat the packing). Set oxygen working pressure.
3. **Open acetylene cylinder valve 1.5 turns maximum**. Set acetylene working pressure.
4. **Bleed hoses** — briefly crack each valve on the torch to purge air; close.
5. **Open fuel gas valve on torch** slightly (approximately 1/4 turn).
6. **Ignite with a friction lighter** (sparker, striker). Never a lighter or match — your hand is in the gas stream.
7. Flame ignites with a yellow/orange smoky character (excess fuel, no O₂ yet).
8. **Gradually open oxygen valve** until the flame transitions from carburizing → neutral → set to the desired flame type.
9. **Depress cutting oxygen lever** to verify the cutting oxygen stream is clean (no rust, water, or spatter in the stream).

### Shutting down the torch

Correct shutdown order prevents internal flashback and acetylene accumulation in the oxygen lines:[^1]

1. **Close fuel gas valve first** — extinguishes the flame, eliminates fuel source.
2. **Close oxygen valve** — purges residual gas from the torch body.
3. **Close both cylinder valves.**
4. **Open torch valves** to bleed off residual pressure in the lines.
5. **Back off regulator adjusting screws** (counterclockwise until free).
6. **Close torch valves.**

**Mnemonic: "Fuel off first, oxygen second, then cylinder, bleed, back off."**

---

## Backfires, flashbacks, and burnbacks

These three events are the most common emergencies in oxyfuel operations. Know the difference:[^1] [^3]

### Backfire

**What it is:** a momentary extinguishing and reignition of the flame at the tip — a "pop" or "squeal" followed by re-lighting.

**Causes:**
- Tip touching the work (briefly obstructing gas flow)
- Tip overheated
- Working pressure too low
- Contaminated or clogged tip

**Response:**
1. Release the cutting oxygen lever
2. Close the torch valves if the flame doesn't re-ignite cleanly
3. Allow the tip to cool
4. Clean or replace the tip
5. Re-light

### Flashback

**What it is:** the flame front travels back into the torch, hoses, or even the cylinders — accompanied by a squealing or hissing sound, the torch may get extremely hot.

**Causes:**
- Both gas pressures set too low
- Severely clogged tip
- Blocked gas flow (tip pressed against work, kinked hose)
- Inadequate flashback arrestors

**Response:**
1. **Close both torch valves immediately.**
2. If the hoses are burning — **close the cylinder valves at the cylinders.**
3. Do not attempt to re-light until root cause is identified and corrected.
4. Inspect all equipment before returning to service — flashback can damage regulators, hoses, and torch internals.
5. If flashback arrestors are not installed — install them before reuse.

### Burnback (GMAW-specific)

Note: "burnback" in oxyfuel cutting refers to a tip that has been burning at reduced flow — distinct from the GMAW definition. In OFC context, a sustained backfire that doesn't self-extinguish and burns back toward the torch.

---

## Cutting technique — hand torch

### Preparing the cut

1. Mark the cut line with a soapstone or chalk scriber.
2. Position the tip **perpendicular to the plate surface** for a square cut, or at the desired bevel angle for bevel cuts.
3. Tip-to-work distance: **3–6 mm** between the tip face and the plate surface — the inner cone tip should just clear the plate surface. Too far = slow, ragged cut. Too close = tip overheats, backfires.[^2]

### Starting the cut

- **Edge start:** position the tip at the edge of the plate. Preheat the start point until it reaches **ignition temperature** — a bright cherry-red (~870°C for mild steel). Then depress the cutting oxygen lever smoothly and begin travel.
- **Pierce start:** for holes and internal cuts. Tilt the tip slightly (15–20°) away from yourself to direct initial blow-out of slag away from you. Preheat the pierce point to cherry-red. Depress cutting oxygen lever — a momentary puddle of molten metal forms; as oxygen purges it, straighten the torch and begin travel. Pierce in 6 mm plate takes ~3–5 seconds of preheat; 25 mm plate takes 15–20 seconds.

### Travel speed

Correct travel speed produces a clean kerf with a drag line that trails nearly vertically. Signs of incorrect speed:[^2]

| Symptom | Cause | Fix |
|---|---|---|
| Dross clings heavily to the bottom of the kerf | Travel too fast | Slow down |
| Kerf is excessively wide, eroded edges | Travel too slow | Speed up |
| Cut stops mid-plate | Travel too fast / O₂ pressure too low / tip too small for thickness | Reduce speed, check settings |
| Wavy, irregular kerf | Unsteady hand/movement | Practice smooth travel (use a guide rail for machine-quality cuts) |
| Concave kerf (undercut on bottom) | Too much cutting oxygen pressure | Reduce O₂ pressure |

### Bevel cutting

Set the torch at the desired bevel angle (e.g., 30° to the plate for a 30° bevel). Use a guide rail or straightedge. Travel the same direction as square cuts — the tip faces the direction of travel.

### Structural shapes (angle, channel, I-beam)

- Cut flanges as separate passes before the web — don't try to cut across the full profile in one pass.
- For angle iron: cut one leg first, then rotate 90° and cut the second.
- For I-beams and channels: cut each flange separately, then the web. The web is thinner and preheats faster — adjust travel speed accordingly.

### Coping (fitting pipe to structural shapes)

Coping is cutting a curved profile into pipe or structural steel so it fits against (rather than over) another member. For a 100 mm (4 in.) C-channel cope:

1. Mark the cope profile by tracing the actual C-channel section onto the workpiece.
2. Use a template (cut from sheet metal or cardboard) for consistency across repeated copes.
3. Cut the cope with the hand torch, keeping the tip aligned to the marked line and maintaining perpendicularity to the cut surface.
4. File and grind the cut edge for a good fit-up. Weld quality starts with cut quality — a poorly coped joint creates gaps that must be bridged with weld metal, leading to stress concentrations and potential code rejection.

### Machine oxyfuel cutting

Machine (track) cutting produces straight cuts of higher quality and consistency than hand cutting. The torch is mounted on a carriage running on a straight rail or template:[^2]

- **Set cutting speed** on the machine drive — starting point from the manufacturer's chart, then adjusted to produce a clean drag line.
- Machine can't feel the torch getting too close to the work — maintain consistent set height, and check tip clearance after each pass as warping can raise or lower the plate.
- **Multiple torch machines** (pantographs, CNC plasma tables used for OFC) can cut complex shapes with excellent repeatability. The same setup, flame, and pressure principles apply.

---

## Care and maintenance of oxyfuel equipment

### Tip cleaning

Tip orifices clog with slag and spatter. Clean with a **tip cleaner set** — round files sized to match the tip orifices.

- Insert the tip cleaner in the direction of gas flow (in from the tip face).
- Use a straight in-and-out motion — do not ream in circles, which enlarges the orifice.
- A worn or oversized orifice produces a noisy, ragged flame and poor cutting quality.
- Replace tips that cannot be cleaned to produce a round, symmetric flame.[^1]

### Regulator maintenance

- Do not attempt to disassemble or rebuild a regulator in the field — send to a certified shop.
- Store with adjusting screw backed off (no spring tension).
- Keep inlet filters clean.

### Hose inspection and storage

- After each use, coil hoses loosely — don't tightly coil (damages inner lining over time).
- Wipe down with a clean dry cloth.
- Store away from sunlight and heat.
- Any hose that fails a leak test (soap solution applied to connections with gas flowing — watch for bubbles) gets replaced, not repaired with tape.

---

## Numbers you need to memorize

- **O₂ cylinder storage pressure:** ~20 700 kPa (3 000 PSI) at 21°C[^1]
- **Acetylene cylinder pressure:** ~1 700–1 900 kPa (250–275 PSI) at 21°C[^1]
- **Acetylene maximum working pressure:** **103 kPa gauge (15 PSI gauge)** — above this, risk of self-detonation[^1]
- **Acetylene max withdrawal rate:** 1/7 of cylinder capacity per hour[^1]
- **Acetylene valve opening:** max **1.5 turns** from closed[^1]
- **O₂/fuel cylinder separation (storage):** 6 m open space OR 1.5 m non-combustible barrier[^1]
- **Steel ignition temperature for OFC:** approximately **870°C (cherry-red)**[^2]
- **Tip-to-work distance (hand cutting):** **3–6 mm** (inner cone clears surface)[^2]
- **Oxygen working pressure for cutting (general range):** 205–550 kPa (30–80 PSI) depending on thickness and tip[^4]
- **Preheat time — 6 mm plate:** ~3–5 seconds; **25 mm plate:** ~15–20 seconds[^2]
- **Flame type for cutting:** **neutral flame** as starting point[^2]
- **Pierce start tip angle:** 15–20° tilt away from operator[^2]

---

## What the textbook doesn't tell you

**Don't use worn tips and call it "good enough."** An out-of-round cutting tip orifice produces an asymmetric oxygen stream. On a machine cut, the kerf drifts. On a pipe cut, the bevel is uneven. When that joint fails a fit-up check, the foreman will ask who cut it — and everyone in the shop knows who the welder was who skipped tip maintenance.[^1]

**Oxygen cylinder valves are opened fully — acetylene is not.** Journeypersons will correct a first-day apprentice on this immediately. The oxygen valve should be opened **all the way** (the packing is seated at the full-open position). Acetylene max 1.5 turns. This isn't preference — it's physics and chemistry safety.[^1]

**The drag lines tell you everything.** If you can read the cut face (the wall of the kerf), you can diagnose what went wrong: vertical drag lines = correct speed; lines drag forward at the bottom = too fast; lines curve backward = too slow. Senior welders can look at a cut and tell you exactly what the operator did wrong.[^2]

**Soapstone is the correct marking tool for plate to be cut.** Markers with organic inks leave hydrocarbon deposits that interfere with the cut start and produce small pops. Scribed metal lines are finer but harder to see without chalk. Soapstone is the right tool.[^2]

**Machine cuts are not maintenance-free.** Track-mounted cutting machines must have their rail cleaned and checked for burrs — a machine that jerks on debris in the track produces a cut that looks like hand-cut garbage.

---

## Key terms

- **Oxyfuel cutting (OFC):** chemical cutting process that uses a preheat flame and a high-pressure oxygen stream to oxidize (burn) iron — works only on metals that oxidize more readily than the iron itself (mild steel, low-alloy steel; NOT stainless, aluminum, or copper)
- **Kerf:** the slot cut by the torch — width is slightly larger than the tip orifice
- **Drag line:** the pattern of marks on the cut face, produced by the oxygen stream — used to diagnose cutting quality
- **Neutral flame:** 1:1 oxygen-to-acetylene ratio — the standard reference flame
- **Carburizing (reducing) flame:** excess acetylene; feather beyond inner cone
- **Oxidizing flame:** excess oxygen; short pointed inner cone; hissing sound
- **Backfire:** momentary pop-and-reignition at the tip — usually minor
- **Flashback:** flame travels back through hoses toward cylinder — serious hazard
- **Flashback arrestor:** spring-loaded or temperature-activated check valve that stops flashback propagation
- **Pierce:** starting a cut from inside the plate (not from the edge)
- **Cope:** a curved cut fitting one member to the profile of another (e.g., pipe to a C-channel)
- **Open circuit voltage:** not applicable to OFC — the process uses no electricity
- **Working pressure:** the regulated gas pressure delivered to the torch — distinct from cylinder storage pressure

---

## Common exam trap

- **Acetylene pressure limit:** the number is **15 PSI / 103 kPa gauge**. Distractors give 30, 25, or 20 PSI. 15 PSI is a hard rule, not a guideline.
- **Shutdown order:** fuel off first, then oxygen. Distractors reverse this. Correct order: close fuel valve → close oxygen valve → close cylinders → bleed → back off adjusters.
- **Oxygen cylinder valve:** open **fully** (all the way). Acetylene: max **1.5 turns**. A question that asks which is opened "1.5 turns" — that's acetylene, not oxygen.
- **Neutral flame for cutting:** the correct starting point. An oxidizing flame is sometimes called "better for cutting" by distractors — it's not; it oxidizes the kerf excessively.
- **Left-hand threads = fuel gas:** the notched hex nut on any fuel gas fitting indicates left-hand thread. Distractors may claim this means "oxygen side."
- **Machine cutting vs hand cutting:** the set pressures and tip selection charts are the same — the difference is the carriage controls travel speed, not gas pressure.
- **Dross (clinker, slag) on bottom of cut:** if dross clings and is difficult to remove, **travel speed is too fast** OR **preheat is insufficient**. Not "too much oxygen."

---

## Practice question preview

**Q:** A welder is performing an oxyfuel cut on 25 mm mild steel plate using acetylene. After igniting the torch and setting the flame to neutral, they depress the cutting oxygen lever but the cut stops 50 mm into the plate. Which combination of issues is most likely?

A) Travel speed too fast and oxygen working pressure too high  
B) Travel speed too fast and tip size too small for the plate thickness  
C) Travel speed too slow and cutting oxygen pressure too low  
D) Backfire caused by tip contacting the work surface  

**Correct: B**

**Explanation:** A cut that starts but stops mid-plate on 25 mm steel typically indicates either insufficient oxygen pressure or a tip too small for the plate thickness (the oxygen jet cannot maintain the oxidizing reaction through the full plate thickness at adequate volume). Too fast of a travel speed compounds this — the preheat zone ahead of the oxygen jet isn't sufficient to maintain ignition temperature through the cut. Option A is internally inconsistent (high O₂ pressure would not cause the cut to stop). Option C is partially correct (low O₂ pressure) but slow speed would make the cut more likely to succeed, not stop. Option D (backfire) produces a momentary pop and re-ignition, not a persistent failure to cut. Verify tip selection against the manufacturer's chart for 25 mm plate and increase O₂ working pressure.

**Red Seal mapping:** C-10.01 (Sets up oxy-fuel gas cutting equipment — tip selection, pressure setting); C-10.02 (Performs oxy-fuel gas cutting — diagnoses cutting failures)

---

[^1]: [CSA W117.2 — Safety in Welding, Cutting, and Allied Processes (2019)](https://www.csagroup.org/store/product/CSA%20W117.2%3A19/), Clause 8 (compressed gas handling: O₂ cylinder storage pressure, acetylene instability above 103 kPa gauge, cylinder valve procedure, oil prohibition, cylinder separation rules, flashback arrestor requirement)
[^2]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapters 11–13: flame types and adjustment, lighting/shutdown sequence, tip-to-work distance, travel speed diagnostics, pierce technique, structural shape cutting procedure, drag line interpretation, soapstone marking
[^3]: [Victor Technologies / ESAB — Oxyfuel Equipment Operator Manual](https://www.esabna.com/us/en/education/blog/oxy-fuel-cutting-guide.cfm), Section 7: backfire causes and response, flashback definition and emergency procedure, flashback arrestor types and placement
[^4]: [Lincoln Electric — Oxy-Fuel Cutting Guide](https://www.lincolnelectric.com/en/education-center/welding-education/cutting), Tip selection chart by plate thickness, cutting oxygen working pressure ranges by tip number
[^5]: [Red Seal Occupational Standard — Welder (2024)](https://red-seal.ca/_conf/assets/custom/docms/welder/rsos-eng.pdf), Block C Task C-10 sub-tasks C-10.01–C-10.03 performance criteria (machine cutting, shape cutting, cope cutting techniques)
