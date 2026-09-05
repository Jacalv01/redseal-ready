---
id: p3-s1-b
period: 3
section: 1
section_title: Foundational Skills, Safety and Procedures
topic_letter: B
topic_title: Oxyfuel Cutting on Mild Steel
hours: 30
weight_pct: 13
outcome: >
  Upon successful completion, learners will be able to perform oxyfuel cutting procedures
  on mild steel, including bevel cutting, piercing, and coping.
objectives:
  - Perform oxyfuel bevel cutting on mild steel.
  - Perform piercing, cutting, and coping on mild steel.
red_seal_mapping:
  - C-10.01 (Selects oxy-fuel cutting gas and equipment)
  - C-10.02 (Sets up oxy-fuel cutting equipment)
  - C-10.03 (Sets operating parameters for oxy-fuel cutting equipment)
  - C-10.04 (Performs cut and gouge using OFC equipment)
  - A-3.02 (Maintains safe work environment)
citations:
  - source: ESAB — Oxyfuel Cutting Handbook and Equipment Manual
    ref: Torch setup, tip selection, pressure settings, cutting techniques
    url: https://www.esab.com/us/nam_en/education/blog/oxyfuel-cutting-guide/
  - source: Victor Technologies (ESAB) — Oxy-Fuel Equipment Operating Instructions
    ref: Bevel cutting setup, piercing technique, tip sizes and pressure tables
    url: https://www.esab.com/globalassets/products/equipment/cutting/oxyfuel/operating-manual.pdf
  - source: CSA W117.2 — Safety in Welding, Cutting, and Allied Processes
    ref: Clause 9 (gas welding and cutting safety), Clause 10 (fire prevention), PPE requirements
    url: https://www.csagroup.org/store/product/CSA%20W117%3A2/
  - source: NFPA 51B — Standard for Fire Prevention During Welding, Cutting, and Other Hot Work
    ref: Section 5 (hot work permits), Section 6 (fire watch requirements), Section 8 (PPE)
    url: https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=51B
  - source: Lincoln Electric — Oxyfuel Cutting Principles and Practices
    ref: Preheat flame adjustment, cutting speed, plate thickness parameters
    url: https://www.lincolnelectric.com/en/education-center/welding-education
---

# Oxyfuel Cutting on Mild Steel — Advanced Techniques

Every fabrication shop runs an oxyfuel torch. It costs almost nothing per cut on heavy steel, it can reach where plasma cannot, and it's the only process that reliably bevels 4-inch plate for groove weld prep without specialized CNC equipment. Period 3 oxyfuel is not "light it and cut" — it's bevel cutting, piercing holes in plate, and coping structural shapes. These skills separate fabricators from fitters.

---

## How Oxyfuel Cutting Actually Works — The Chemistry

Oxyfuel cutting is not melting. It's **oxidation** (rapid burning).[^1]

The process has two distinct phases:

1. **Preheat:** The preheat flame (acetylene or propane with oxygen) brings the steel to its **kindling temperature** — approximately 870–980 °C (1600–1800 °F) for mild steel. At this temperature, steel glows bright orange.

2. **Cutting:** A high-pressure stream of **pure oxygen** is released through the cutting orifice. At kindling temperature, mild steel burns (oxidizes) in pure oxygen. The iron oxide formed is a liquid that is blown out of the cut by the oxygen jet pressure.

**Why it only works on mild steel and low-alloy steels:**
- The melting point of iron oxide (FeO) is LOWER than the melting point of the steel. The oxide liquefies and gets blown clear.
- In stainless steel, chromium oxide (Cr₂O₃) has a HIGHER melting point than the steel itself — it forms a solid crust that blocks the oxygen stream. Oxyfuel cutting does NOT work on stainless without flux injection.[^1]
- Cast iron has too much carbon — the preheat flame dissolves the carbon into the gas before oxidation can proceed. Plasma cutting is used instead.

---

## Gases and Their Characteristics

| Gas | Max fuel-to-oxygen ratio | Flame temp (°C) | Notes |
|---|---|---|---|
| **Acetylene (C₂H₂)** | 1:1.2–1.5 (cutting) | ~3100 | Hottest, fastest preheat, primary preheat flame. Unstable above 103 kPa (15 psi). [^1] |
| **Propane (C₃H₈)** | 1:4.5 (cutting) | ~2850 | Slower preheat, cooler flame, denser than air (sinks to floor). Cheaper per GJ. |
| **Natural gas (CH₄)** | 1:1.5–2.0 (cutting) | ~2770 | Lowest flame temp, slowest preheat. Used on automated CNC tables. |
| **MAPP Gas (withdrawn)** | Similar to propane | ~2900 | Discontinued commercially; propylene blends used instead |

**Acetylene rule:** NEVER exceed 103 kPa (15 psi) gauge pressure at the torch. Above 103 kPa, acetylene becomes shock-sensitive and can decompose explosively without external ignition.[^3]

**Propane rule:** Propane is heavier than air. In confined spaces, propane leaks pool at floor level and create explosion hazards. Adequate ventilation means air movement at floor level, not just at head height.[^3]

---

## Tip Selection — The Critical Variable

The cutting tip (nozzle) is sized for the material thickness. Using the wrong tip is the most common cause of poor cuts.[^1][^2]

### General acetylene cutting tip size guide (approximate)[^2]

| Steel thickness | Tip size (approx) | O₂ cutting pressure (kPa / psi) | Fuel pressure (kPa / psi) |
|---|---|---|---|
| 3–6 mm (1/8–1/4") | #000 – #0 | 175–241 kPa (25–35 psi) | 7–14 kPa (1–2 psi) |
| 6–12 mm (1/4–1/2") | #0 – #1 | 207–276 kPa (30–40 psi) | 7–21 kPa (1–3 psi) |
| 12–25 mm (1/2–1") | #1 – #2 | 241–310 kPa (35–45 psi) | 14–28 kPa (2–4 psi) |
| 25–50 mm (1–2") | #2 – #3 | 276–345 kPa (40–50 psi) | 21–34 kPa (3–5 psi) |
| 50–100 mm (2–4") | #3 – #4 | 310–414 kPa (45–60 psi) | 28–48 kPa (4–7 psi) |

*Note: Always verify exact pressures with the torch manufacturer's tip chart — different manufacturers have different orifice sizes for the "same" tip number.[^2]*

### Signs of wrong tip or pressure setting

| Problem | Likely cause |
|---|---|
| Cut face has deep drag lines (lag) | Travel too fast OR oxygen pressure too low OR tip too small |
| Cut face is rounded at top, undercut | Too slow OR oxygen pressure too high |
| Preheat cones are too long or luminous | Too much acetylene (rich flame) |
| Cut stops mid-piece | Tip clogging OR plate too thick for tip |
| Excessive slag that won't knock off | Travel speed too slow OR low carbon steel correct, but slag is normal for thick steel |

---

## Flame Adjustment — Getting the Neutral Flame

Before cutting, the preheat flame must be properly adjusted.[^1][^2]

### Acetylene flame types

1. **Carbonizing (rich) flame:** excess acetylene — three-cone structure (luminous inner cone, intermediate feather, outer envelope). Carbon deposits on steel. Wrong for cutting.

2. **Neutral flame:** oxygen-to-acetylene ratio balanced — two-cone structure (sharp inner cone, transparent outer envelope). No carbon deposit. Correct for most steel cutting and welding.

3. **Oxidizing flame:** excess oxygen — single sharp cone, slightly purple tinge. Short inner cone. Burns hotter than neutral. Can be used for cutting but oxidizes the steel surface during preheat, creating mill-scale-like crust.

**For oxyfuel cutting, set a slightly oxidizing to neutral preheat flame.** A true neutral prevents carbon pickup during preheat.[^1]

### Lighting and adjusting procedure
1. Crack the oxygen valve slightly
2. Open the fuel valve, ignite with friction lighter (NEVER a match or lighter — back-flash risk)
3. Adjust fuel until the carbonizing feather disappears (at neutral)
4. For propane: adjust until the inner cone is sharp and blue
5. Test cutting oxygen — flame should increase slightly in size without going out

---

## Straight Cutting Technique (Reviewed from P1/P2)

- **Standoff distance:** 6–10 mm (1/4–3/8") from tip to plate surface (for acetylene tips without a stand-off guide).[^1] Too close = tip clogging. Too far = preheat is diffuse, slow, and cut quality suffers.
- **Torch angle:** typically 0° (perpendicular to plate surface) for a straight cut
- **Travel speed:** found by watching the cut. Proper speed = sparks (slag) blow downward and slightly ahead of the cut. Too fast = sparks blow backward. Too slow = slag stacks up on the bottom edge.
- **Start:** begin at the edge of the plate if possible. If you must start in the middle, pierce first (see below).

---

## Bevel Cutting — The Period 3 Core Skill

Bevel cutting produces an angled face on the plate edge for groove weld preparation. Every structural and pressure vessel groove weld starts with a beveled edge.[^1][^2]

### Setup for bevel cutting

1. **Mark the cut line:** use soapstone on the plate face, or a scribed line on the surface
2. **Determine the bevel angle:** typical groove prep angles are 22.5° per side (45° included) or 30° per side (60° included). For a single-V bevel, one side is cut.
3. **Tilt the torch:** angle the torch away from vertical by the bevel angle. If cutting a 30° bevel, tilt the torch 30° from vertical (60° from the plate surface).
4. **Use a guide:** a bevel cutting guide (a small wheeled jig that clamps on the torch and rides on the plate surface) is highly recommended for straight, consistent bevels. Without a guide, it takes significant practice to hold a consistent angle over 1–3 metre cuts.
5. **Maintain standoff:** with a guide wheel, standoff is set by the guide. Without a guide, maintain a consistent 6–10 mm tip-to-surface distance.

### Bevel angle measurement

The bevel angle is measured from the vertical (90°) of the plate edge:
- **30° bevel:** 30° from vertical = 60° from the plate surface
- **22.5° bevel:** 22.5° from vertical = 67.5° from the plate surface

**Check with a bevel protractor** after cutting. The bevel angle must be within ±2.5° for most code applications.[^2]

### Root face (land)

After bevel cutting, the bottom of the bevel has a small flat area — the root face or land. For oxyfuel-cut bevels, this is typically 1.5–3 mm (1/16–1/8"). If it's too large, it can be ground down. If the bevel cuts all the way to a sharp knife edge, a slight grinding step creates the land.[^1]

### Multi-pass beveling on thick plate

For plate > 50 mm (2 inches), a single-pass bevel cut can be difficult because:
- The oxygen jet has trouble reaching the root of the cut when highly angled
- The preheat may not fully penetrate to the bottom of the cut at high angles

**Two-pass method:** Make a roughing cut first (close to the final angle, leaving 3–5 mm material), then a finishing pass at the exact angle. Or make a straight cut first to remove the bulk of the material, then tilt the torch for the bevel in a second pass.[^2]

---

## Piercing — Starting a Cut in the Middle of a Plate

Piercing is required when you cannot start at the edge — for example, cutting a hole for a pipe nozzle in a vessel shell, or starting a cut-out in the middle of a floor plate.[^1]

### Piercing procedure

1. **Preheat the spot** with the preheat flame at a slight angle (about 5–10° from perpendicular) until the spot glows bright orange (870–980 °C)
2. **Increase standoff** distance to 20–25 mm (3/4–1") before opening the cutting oxygen — this prevents the blow-back of molten iron oxide from clogging the tip
3. **Open the cutting oxygen slowly:** the steel will begin to oxidize. You'll see a shower of sparks below and orange slag blowing upward.
4. **Lower the torch gradually** as the cut penetrates — slowly bring it back to normal standoff once the jet has cut through
5. **Resume normal travel speed** once the pierce is complete

### Pierce hazards[^3]

- **Blow-back:** molten slag is ejected upward during piercing. ALWAYS position your body to the side, NOT directly above or in the path of the ejected slag.
- **Spatter damage:** cover nearby equipment and instrumentation with fire-resistant blankets before piercing
- **Fire watch required:** sparks can travel 10 m (33 ft) or more. A second person as fire watch is required per NFPA 51B Section 6 during confined space or elevated work.[^4]

---

## Coping — Cutting Structural Shapes

Coping is the removal of material from the end of a structural shape (I-beam, channel, angle) so it can fit against another member. A coped W-section looks like a notch cut at the end of the flange and web.[^1]

### Why cope?

- An I-beam connecting to another beam web needs its top and bottom flanges cut back so only the web passes through (or butts against the web)
- Coping prevents flange-to-flange interference in beam connections
- Calculated precisely: the cope depth and length are shown on structural drawings

### Coping procedure

1. **Lay out the cope:** measure and mark with soapstone. Mark both sides of the beam web for reference.
2. **Determine sequence:** typically cut the flange first (straight cut at the cope depth), then cut the web vertical face (to the cope length).
3. **Cut the flange:** straight cut perpendicular to the beam axis, at the cope depth. Cut from the flange edge toward the web.
4. **Stop at the fillet radius:** the junction of the web and flange has a fillet. Do NOT try to cut the fillet sharp — leave a 6–10 mm radius and remove the remnant with an angle grinder. A sharp notch in the cope creates a stress concentration.
5. **Cut the web face:** straight cut parallel to the beam axis, at the cope length. Cut from the preheat flame through the web.
6. **Grind smooth:** all cope cuts should be ground smooth with an angle grinder. Burrs, gouges, and roughness at cope edges concentrate stress.

**Common structural cope dimensions (typical — verify against structural drawings):**
- Cope depth: 1.5× flange thickness, or as drawn
- Cope length: 1.5× d (beam depth), or as drawn
- Corner radius: 25 mm (1") minimum per CISC Handbook practice[^1]

---

## Quality Checks on Oxyfuel Cuts

A well-made oxyfuel cut has these characteristics:[^1][^2]

| Quality indicator | Acceptable | Reject |
|---|---|---|
| **Drag lines** | Nearly vertical (slight rearward lean acceptable) | Steeply angled backward (too fast) |
| **Cut face** | Smooth, consistent | Deep gouges, washout, slag islands |
| **Top edge** | Sharp, slight rounding acceptable | Melted round edge (too slow or too close) |
| **Bottom edge** | Minimal slag | Thick, solidified slag not removable with chipping hammer |
| **Bevel angle** | Within ±2.5° | Varies > 2.5° along cut length |
| **Squareness** | Both faces perpendicular to each other ± 2° | Twisted bevel |

---

## Numbers you need to memorize

- **Acetylene max pressure:** 103 kPa (15 psi) — NEVER exceed[^3]
- **Kindling temperature for mild steel:** 870–980 °C (1600–1800 °F)[^1]
- **Normal standoff distance:** 6–10 mm (1/4–3/8") from tip to plate[^1]
- **Pierce standoff distance:** 20–25 mm (3/4–1") before opening cutting oxygen[^1]
- **Acetylene flame temp:** ~3100 °C (hottest common fuel gas)[^1]
- **Propane flame temp:** ~2850 °C[^1]
- **Bevel angle tolerance:** ±2.5° for most code applications[^2]
- **Cope corner radius minimum:** 25 mm (1") per CISC practice[^1]
- **Fire watch travel distance:** sparks can travel 10 m (33 ft) or more[^4]

---

## What the textbook doesn't tell you

**You CANNOT make a good bevel cut without a guide on long cuts.** Hand-holding a torch at 30° for 3 metres and maintaining a consistent angle is a skill that takes months to develop. Get a guide wheel or a circle cutting attachment. If your company doesn't have one, ask — they cost less than one hour of welder time wasted on a bad bevel.[^2]

**Slag sticking to the bottom is a cut quality indicator, not a cleaning problem.** If your slag is hard to remove with a hammer, you were too slow. Fast cuts produce slag that falls away cleanly or drops with one hammer tap.[^1]

**Propane users: make sure you're adjusting for the different flame chemistry.** Propane requires much more oxygen than acetylene (4.5:1 ratio vs 1.2:1). The torch setup for propane is different from acetylene — the fuel-oxygen mixing is different, the tip orifices are sized differently, and the pressures are different. Never swap an acetylene tip into a propane torch without verifying it's compatible.[^1]

**The pierce blow-back will surprise you the first time.** The shower of orange-hot slag coming back at your face is alarming. Always wear a full-face shield (not just goggles), position your body to the side, and never pierce directly above your head or hands. Shield nearby equipment with a fire blanket.[^3]

**Cut quality on thick plate deteriorates with dirty tips.** Clean tips before EVERY cutting session with tip cleaners (spiral-flute files). Do not use drills — they enlarge the orifice and ruin the tip. A clean tip makes a straight, square cut; a dirty tip makes a wandering, undercut mess.[^2]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s1-b-bevel-cut-setup.svg` — side view showing torch tilted at bevel angle relative to vertical plate, annotated with: tip standoff, bevel angle (from vertical), root face/land, cutting direction)*

*(SVG to be added: `assets/diagrams/p3-s1-b-pierce-sequence.svg` — three-step sequence: step 1 preheat at angle with increased standoff, step 2 open cutting oxygen while tilted, step 3 lower to normal standoff and travel. Arrows showing slag blow-back direction.)*

*(SVG to be added: `assets/diagrams/p3-s1-b-cope-geometry.svg` — end view of W-section beam showing cope cuts: flange cut depth, web face cut length, corner radius, before/after comparison)*

---

## Key terms

- **Kindling temperature:** the temperature at which steel ignites in pure oxygen (~870–980 °C for mild steel)
- **Oxidation:** the chemical reaction between iron and pure oxygen at kindling temperature — this IS the cut
- **Drag lines:** the striations left on the cut face showing the path of the oxygen jet through the steel
- **Standoff distance:** the distance between the torch tip and the plate surface
- **Root face / land:** the flat bottom portion of a beveled edge, retained to control root gap
- **Bevel angle:** the angle of the cut face measured from the vertical of the plate edge
- **Pierce:** starting a cut in the middle of the plate (not from an edge)
- **Cope:** removing material from the end of a structural shape to allow it to fit against another member
- **Fillet radius:** the inside curved transition between the flange and web of a structural shape — must not be notched sharply when coping
- **Drag:** the rearward lean of the cut face — acceptable when slight, indicates too-fast travel when excessive

---

## Common exam trap

- **Acetylene MAX pressure is 103 kPa (15 psi).** Exam questions often offer 207 kPa (30 psi) or 138 kPa (20 psi) as distractors. Always 103 kPa / 15 psi.
- **Oxyfuel cutting = oxidation, NOT melting.** Exam questions may describe it as "melting the steel." The correct term is oxidizing (burning) the steel in a pure oxygen jet.
- **Propane sinks; acetylene is slightly lighter than air.** In confined space, propane pools at floor level. Acetylene diffuses upward. Questions may ask about safe ventilation placement.
- **Pierce position:** stand to the SIDE, not above. Slag blows upward and backward during piercing.
- **Cope corner MUST have a radius** — not a sharp notch. Stress concentration causes fatigue cracking in service.
- **Stainless steel CANNOT be cut with standard oxyfuel.** The chromium oxide film blocks the cut. Use plasma cutting instead.

---

## Practice question preview

**Q:** A welder is piercing a 25 mm (1") hole in the middle of a mild steel plate to start a cut-out. Before opening the cutting oxygen lever, what should the welder do with the torch standoff distance compared to normal cutting?

A) Decrease it to 3 mm to concentrate heat  
B) Keep it at the normal 6–10 mm — no change needed  
C) Increase it to 20–25 mm to prevent slag blow-back onto the tip  
D) Move to 50 mm and use maximum oxygen pressure to force the pierce

**Correct: C**

**Explanation:** During piercing, the molten iron oxide is ejected upward (back toward the torch) when the oxygen jet first breaks through. Increasing standoff to 20–25 mm keeps the tip above the blow-back zone. If you pierce at normal standoff (6–10 mm), the ejected slag will clog the tip orifices immediately, requiring tip cleaning before the cut can continue. D is wrong — 50 mm is too far and the preheat is too diffuse.

**Red Seal mapping:** C-10.04 (Performs cut and gouge using OFC equipment)

---

[^1]: [ESAB — Oxyfuel Cutting Handbook](https://www.esab.com/us/nam_en/education/blog/oxyfuel-cutting-guide/); oxidation chemistry, flame types, tip selection, standoff, bevel cutting setup, coping procedure, cut quality indicators
[^2]: [Victor Technologies (ESAB) — Oxy-Fuel Equipment Operating Instructions](https://www.esab.com/globalassets/products/equipment/cutting/oxyfuel/operating-manual.pdf); tip selection charts, pressure settings, multi-pass bevel technique, tip cleaning procedures
[^3]: [CSA W117.2 — Safety in Welding, Cutting, and Allied Processes](https://www.csagroup.org/store/product/CSA%20W117%3A2/); Clause 9 (gas cutting safety), acetylene pressure limits (15 psi/103 kPa), propane confined space hazards, PPE requirements
[^4]: [NFPA 51B — Standard for Fire Prevention During Welding, Cutting, and Other Hot Work](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=51B); Section 5 (hot work permits), Section 6 (fire watch requirements — 10 m radius, 30-minute post-work watch), Section 8 (PPE)
[^5]: [Lincoln Electric — Oxyfuel Cutting Principles and Practices](https://www.lincolnelectric.com/en/education-center/welding-education); preheat flame adjustment, cutting speed optimization, plate thickness parameters
