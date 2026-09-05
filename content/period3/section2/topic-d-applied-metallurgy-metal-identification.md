---
id: p3-s2-d
period: 3
section: 2
section_title: Properties of Metals
topic_letter: D
topic_title: Applied Metallurgy and Metal Identification
hours: 6
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to identify space-lattice types,
  describe dendritic grain growth, interpret grain structure changes from welding,
  and read mill test reports.
objectives:
  - Identify space-lattice types in metals.
  - Describe dendritic grain growth.
  - Describe grain structure differences in metals.
  - Identify changes in grain structure that result from welding.
  - Interpret information supplied on mill test reports.
red_seal_mapping:
  - A-4.01 (Uses documentation and reference material)
  - A-5.01 (Performs quality inspection)
  - A-5.03 (Controls temperature of weldments)
  - B-8.01 (Prepares materials)
citations:
  - source: TWI Global — Job Knowledge: Introduction to the Metallurgy of Welding
    ref: Space lattice types, dendritic solidification, HAZ grain structure, iron-carbon diagram
    url: https://www.twi-global.com/technical-knowledge/job-knowledge/metallurgy-of-welding-part-1-041
  - source: Lincoln Electric — Procedure Handbook of Arc Welding
    ref: Iron-carbon phase diagram, transformation temperatures, grain growth in HAZ, MTR interpretation
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: Modern Welding (Bowditch et al., Goodheart-Willcox)
    ref: Chapter on metallurgy — space lattice, BCC/FCC, dendritic solidification, heat treatment effects
    url: https://www.g-w.com/modern-welding
  - source: CWB Group — Understanding Mill Test Reports for Welders
    ref: Reading MTR/MTC documents, chemistry fields, mechanical property fields, heat numbers
    url: https://www.cwbgroup.org/education
  - source: ESAB — Welding Metallurgy Fundamentals
    ref: Grain growth, recrystallization, HAZ zones, cooling rate effects on microstructure
    url: https://www.esab.com/us/nam_en/education/blog/welding-metallurgy/
---

# Applied Metallurgy and Metal Identification

Metallurgy is the language that connects what welders do (put heat into metal) to what engineers need (welds that don't crack or fail). You don't need a metallurgist's degree — but you need to understand why your welding procedure says what it says, and what happens at the grain level when you ignore it.

---

## Space Lattice Types — The Crystal Structure of Metals

All crystalline metals are made of atoms arranged in repeating three-dimensional patterns called space lattices (or crystal structures).[^1][^3]

### The three most important for welders

| Structure | Full name | Example metals | Properties |
|---|---|---|---|
| **BCC** | Body-Centered Cubic | Iron (below 912°C), ferritic steel, chromium, molybdenum, tungsten | Moderate ductility, magnetic, allows interstitial carbon |
| **FCC** | Face-Centered Cubic | Austenite (iron above 912°C), aluminum, copper, nickel, austenitic stainless | High ductility, often non-magnetic, better toughness at low temperature |
| **HCP** | Hexagonal Close-Packed | Titanium, magnesium, zinc, cobalt | Limited slip systems, lower ductility, directional properties |

### BCC structure (Body-Centered Cubic)

- One atom at each corner of a cube + one atom at the center of the cube
- **8 atoms at corners × 1/8 each + 1 center atom = 2 atoms per unit cell**
- Iron in the BCC form is called **alpha-iron (α-Fe) or ferrite**
- BCC iron exists at room temperature and below 912 °C
- **Carbon solubility in BCC iron:** very low — maximum 0.022% C at 727 °C. Carbon does not fit easily in the BCC lattice.

### FCC structure (Face-Centered Cubic)

- One atom at each corner + one atom at the center of each face
- **8 corners × 1/8 + 6 faces × 1/2 = 4 atoms per unit cell**
- Iron in the FCC form is called **gamma-iron (γ-Fe) or austenite**
- FCC iron exists between 912 °C and 1394 °C
- **Carbon solubility in FCC iron:** high — maximum 2.14% C at 1147 °C. The FCC lattice has large interstitial spaces that accommodate carbon atoms.

### Why this matters for welding

When steel is heated above 912 °C (Ac₃), the iron transforms from BCC ferrite to FCC austenite — carbon dissolves into solution. When it cools:

- **Slow cooling (below about 0.77% C):** austenite transforms to ferrite + pearlite (a mix of ferrite and iron carbide layers). Good ductility.
- **Faster cooling:** some bainite forms. Moderate strength and toughness.
- **Rapid cooling (quenching):** austenite transforms to martensite — a highly distorted BCT (body-centered tetragonal) structure. Very hard, very brittle.

**The HAZ of every carbon steel weld goes through this transformation cycle.** The cooling rate in the HAZ determines whether you get tough pearlitic steel or brittle martensite. Preheat slows cooling. That is its function.

---

## Iron-Carbon Phase Diagram — Key Temperatures

| Temperature | Transformation |
|---|---|
| **727 °C (A₁ or Ac₁)** | Lower critical temperature — austenite starts forming on heating; pearlite transforms to austenite |
| **912 °C (Ac₃)** | Upper critical temperature for low-carbon steel — steel is fully austenitic above this |
| **1147 °C** | Eutectic temperature — austenite + liquid + cementite coexist |
| **1394 °C** | Delta iron to liquid transformation |
| **0.77% C** | Eutectoid composition — fully pearlitic steel at slow cooling |
| **2.14% C** | Maximum carbon solubility in austenite (FCC iron) |

**In the HAZ of a weld**, peak temperatures are highest at the fusion line and decrease with distance from the weld. The zones (from hot to cold): partial melting → grain coarsening → grain refinement → intercritical → subcritical HAZ → base metal.[^1]

---

## Dendritic Grain Growth — How Weld Metal Solidifies

When liquid weld metal solidifies, it doesn't form round grains immediately. It solidifies through a process called **dendritic solidification**.[^1][^3]

### The solidification sequence

1. **Nucleation:** tiny solid crystals form at the fusion line (on the existing grain boundaries of the base metal — heterogeneous nucleation)

2. **Dendrite growth:** each nucleus grows outward into the liquid, forming a tree-like branching structure (dendrite = Greek for "tree"). The main trunk grows in the direction of maximum heat extraction (toward the coolest zone — away from the heat source).

3. **Dendrite branches fill the space:** as the dendrites grow, they reject alloying elements to the liquid around them. The last liquid to solidify is enriched in segregated elements.

4. **Solidification complete:** the liquid is fully consumed. The result is columnar grains elongated toward the weld centerline, with solute-enriched boundaries between dendrites.

### What dendritic solidification means for weld quality

- **Centerline segregation:** the last liquid (at the centerline, farthest from the fusion boundary) is enriched in sulfur, phosphorus, and carbon — the elements with lowest melting points. This is the zone most susceptible to **hot cracking (solidification cracking)**.
- **Columnar grain structure:** columnar grains are weaker in the direction perpendicular to their growth axis — transverse to the weld axis. This is why through-thickness tensile loading of weld metal is tested differently from longitudinal loading.
- **Coarse grain size:** rapid solidification in a weld produces finer dendrites (faster cooling = finer solidification structure). Slow cooling = coarser dendrites = larger effective grain size = lower toughness.

### Weld metal grain refinement

Multi-pass welds benefit from **grain refinement:** each subsequent pass reheats the previous pass into the grain-growth range, and the thermal cycle of the new pass refines the coarse solidification grains of the previous pass. The LAST pass (cap) has no subsequent refinement — it retains the coarse solidification structure. This is why cap pass toughness is generally lower than fill pass toughness.[^2]

---

## HAZ Grain Structure Changes — What the Weld Does to Base Metal

The HAZ is a permanently altered zone. The peak temperature gradient creates distinct microstructural zones:[^1][^5]

| Zone (from fusion line outward) | Peak temp range | Structure after cooling | Effect on properties |
|---|---|---|---|
| **Partially melted zone (PMZ)** | 1400–1500 °C | Liquid films at grain boundaries — solidified into mixed structure | Very high cracking risk; starting point for HAZ cracks |
| **Coarse-grain HAZ (CGHAZ)** | 1100–1400 °C | Large austenite grains form; on cooling → coarse-grained martensite or bainite | Lowest toughness zone, highest hardness; hydrogen cracking risk |
| **Fine-grain HAZ (FGHAZ)** | 900–1100 °C | Grain refinement from complete transformation — normalized condition | Best toughness in the HAZ; actually improved over base metal in some cases |
| **Intercritical HAZ** | 727–900 °C | Partial transformation — mixed ferrite and austenite zones | Lower toughness than FGHAZ; some austenite pockets may transform to martensite |
| **Subcritical HAZ** | < 727 °C | No phase transformation; carbides may coarsen | Softening in Q&T steels; stress relief in normalized steel |

**The coarse-grain HAZ is always the weakest link.** It is the prime target for hydrogen-induced cracking in hardenable steels and the zone that fails first in impact testing of substandard welds. Controlling this zone requires preheat, interpass temperature control, and low-hydrogen process selection.[^1]

---

## Grain Coarsening and Refinement

### Why grains grow at high temperature

Grain boundaries have higher energy than grain interiors. At elevated temperature, atoms have sufficient thermal energy to migrate across boundaries — large grains grow at the expense of small ones (Ostwald ripening). This is driven thermodynamically: fewer boundaries = lower total boundary energy.[^3]

**Above 912 °C**, grain growth in the austenite is rapid. The longer the time above 912 °C, the coarser the grains.

### Grain size effects on mechanical properties

| Finer grain size | Coarser grain size |
|---|---|
| Higher yield strength | Lower yield strength |
| Higher tensile strength | Lower tensile strength |
| Higher toughness (Charpy V-notch) | Lower toughness |
| Better fatigue resistance | Worse fatigue resistance |

**Hall-Petch relationship:** yield strength ∝ 1/√(grain size). Finer grains = stronger. This is why controlled rolling, normalizing, and fine-grained practices exist in steel production.[^3]

### Grain refinement in practice

- **Normalizing** (heat to above Ac₃, air cool) refines coarse grains — gives a uniform, fine-grained microstructure
- **Multi-pass welding** partially refines the previous pass
- **Addition of Ti, Nb, Al to steel** pins grain boundaries (grain boundary pinning) — these microalloyed steels resist grain growth and are tougher after welding (ASTM A517, CSA G40.21 Grade 350W)

---

## Mill Test Report (MTR / MTC) — Reading What the Steel Mill Sends You

Every piece of structural or pressure vessel steel arrives with a Mill Test Certificate (MTC) or Mill Test Report (MTR) — the official record of what came out of the mill.[^4]

### Key fields on an MTR

| Field | What it means |
|---|---|
| **Heat number** | Unique identifier for the batch of liquid steel (the "heat") from which the plate/pipe was poured — traceable to specific chemistry |
| **Grade/specification** | e.g., A36, A516 Gr. 70, CSA G40.21 350W — defines the minimum mechanical requirements |
| **Thickness** | Mill-measured actual thickness (may differ from nominal within tolerance) |
| **Chemistry (%) C, Mn, Si, P, S, Ni, Cr, Mo, V, Cu** | Actual analyzed chemistry of the heat — use this to calculate CE for preheat determination |
| **Tensile strength (MPa)** | Actual measured tensile strength from a coupon cut from the plate |
| **Yield strength (MPa)** | Actual measured yield strength |
| **Elongation (%)** | Measure of ductility — how much the specimen stretched before fracture |
| **Charpy impact (J at specified temp)** | Toughness at a given temperature — relevant for low-temperature service |
| **Certification signature** | Mill quality department signature and date |

### How welders use MTRs

1. **Calculate CE for preheat determination:** Pull C, Mn, Cr, Mo, V, Ni, Cu from the chemistry section. Apply the formula. Compare to W59 or applicable code requirements.

2. **Verify material is as specified:** if the drawing calls for A516 Gr. 70 and the MTR shows A516 Gr. 60, that's an engineering issue to escalate — don't weld it and hope for the best.

3. **Document the heat number on weld records:** many code jobs require traceability from the finished weld back to the heat number on the MTR — so the engineer can verify material properties for the as-built record.

4. **Check for exotic chemistry:** high Cr, high Mn, or significant alloy additions may indicate a higher CE than a standard grade — preheat requirements can be very different from the nominal grade would suggest.

---

## Spark Test for Metal Identification

A quick field method for identifying carbon content and approximate steel type:[^3]

| Spark appearance | Approximate material |
|---|---|
| Long, straight, orange sparks — few forks | Low-carbon steel (mild steel) |
| Long sparks with prominent star bursts | Medium-carbon steel |
| Short, dense, white sparks with many forks | High-carbon steel or tool steel |
| Long, dull orange sparks, minimal forks | Wrought iron or very low carbon |
| Dark red to orange, short, few sparks | Cast iron |
| No spark (or very faint) | Stainless steel (Cr suppresses spark) |

**Caution:** Spark testing is a rough identification method — it does NOT replace chemical analysis or MTR review for code welding. Use it for sorting unknown material in a fabrication shop, not for determining preheat on a pressure vessel.[^3]

---

## Numbers you need to memorize

- **BCC iron (ferrite):** exists at room temperature to 912 °C[^1]
- **FCC iron (austenite):** exists from 912 °C to 1394 °C[^1]
- **Ac₁ (lower critical temp):** 727 °C — austenite starts forming on heating[^1]
- **Ac₃ (upper critical temp for low-C steel):** 912 °C — fully austenitic above this[^1]
- **Max C in BCC (ferrite):** 0.022% C[^1]
- **Max C in FCC (austenite):** 2.14% C at 1147 °C[^1]
- **Eutectoid composition:** 0.77% C (fully pearlitic at slow cooling)[^1]
- **CE formula:** C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15[^4]
- **Hall-Petch relationship:** finer grain = higher yield strength[^3]

---

## What the textbook doesn't tell you

**The MTR is a legal document.** On code jobs, losing the MTR creates a verification crisis — the inspector may require plate sampling and chemical analysis (costly and slow) to re-establish traceability. File MTRs immediately, organized by heat number and plate ID. Every journeyperson should know where the MTRs are on the job.[^4]

**The carbon equivalent formula gives you a MINIMUM preheat requirement.** It doesn't account for: joint restraint (high restraint = crack risk, use higher preheat), diffusible hydrogen level of the electrode (E7018 is low-H, E6010 is not), or section thickness (thicker = faster cooling in the interior). Professional welding engineers add safety margin.[^1]

**Dendritic grain boundaries are where the problems hide.** Segregated sulfur at the centerline of a weld bead is what causes solidification cracking in nickel alloys and high-sulfur steels. The only way to see it is metallographic sectioning and etching — or it shows up as a crack on radiograph. Correct technique (stringer beads, appropriate heat input) minimizes segregation by increasing the solidification rate and reducing the segregation path length.[^1]

**You can't judge steel quality by color or feel.** A36 and A514 (Grade 100 quench and temper) look identical from the outside. Their weld preheat requirements are vastly different: A36 may need no preheat for thin sections; A514 requires minimum 10 °C (50 °F) preheat even at thin sections and much more for thicker material, per the steel producer's data sheet. Always check the MTR.[^4]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s2-d-space-lattice.svg` — three side-by-side 3D cube diagrams: BCC (atom at center + corners), FCC (atoms at faces + corners), HCP (hexagonal prism with atoms) — each labeled with example metals and temperature range for steel)*

*(SVG to be added: `assets/diagrams/p3-s2-d-dendritic-solidification.svg` — cross-section of weld pool showing: fusion line at left, liquid pool, dendrites growing from fusion line toward centerline, last liquid at centerline (segregation zone), final columnar grain structure)*

*(SVG to be added: `assets/diagrams/p3-s2-d-iron-carbon-diagram.svg` — simplified iron-carbon phase diagram showing: ferrite region, austenite region, two-phase regions, key temperatures Ac₁ (727°C) and Ac₃ (912°C), eutectoid point (0.77% C), maximum carbon in austenite (2.14% C))*

---

## Key terms

- **Space lattice:** the repeating three-dimensional atomic arrangement in a crystalline metal
- **BCC (Body-Centered Cubic):** cubic lattice with one atom at center — the structure of iron (ferrite) at room temperature
- **FCC (Face-Centered Cubic):** cubic lattice with atoms at face centers — the structure of austenite
- **Austenite (γ-iron):** FCC iron phase, stable 912–1394 °C, high carbon solubility
- **Ferrite (α-iron):** BCC iron phase, room temperature to 912 °C, low carbon solubility
- **Martensite:** highly strained BCT structure formed by rapid quenching of austenite — hard and brittle
- **Dendritic solidification:** tree-like growth pattern of solid grains forming from liquid weld metal
- **Segregation:** concentration of certain alloying elements at dendrite boundaries or grain boundaries during solidification
- **HAZ (Heat-Affected Zone):** base metal region heated but not melted by the weld — microstructure permanently altered
- **Coarse-grain HAZ (CGHAZ):** the highest-temperature HAZ zone — prone to brittleness and cracking
- **MTR / MTC (Mill Test Report / Certificate):** the official document from the steel mill certifying chemistry and mechanical properties of a specific heat of steel
- **Heat number:** the traceable ID for a specific batch of steel from the mill
- **Carbon equivalent (CE):** calculated value from steel chemistry used to assess hardenability and preheat requirement

---

## Common exam trap

- **BCC iron is ferrite, NOT austenite.** FCC is austenite. They will be reversed in distractors.
- **Ac₁ = 727 °C; Ac₃ ≈ 912 °C for low-carbon steel.** Exam questions love to place these at the wrong temperatures (800 °C, 1000 °C).
- **Martensite is NOT the same as austenite.** Martensite forms when austenite is rapidly quenched. It is NOT the stable equilibrium structure at any temperature.
- **Fine grain size = STRONGER than coarse grain** (Hall-Petch). This is counterintuitive — students think large crystals = strong. The grain boundary network impedes dislocation motion, so more boundaries (finer grain) = stronger.
- **CE formula denominators:** Mn/6, (Cr+Mo+V)/5, (Ni+Cu)/15 — not 3, not 10, not 8. Memorize these.
- **Spark test is rough identification only** — not suitable for code welding material verification.

---

## Practice question preview

**Q:** A welder receives a plate labeled "A516 Gr. 70" but no Mill Test Report is provided. The foreman says "just go ahead, it's standard carbon steel." What is the correct course of action?

A) Proceed without preheat — A516 Gr. 70 is always low-carbon equivalent  
B) Request the Mill Test Report before welding; carbon equivalent must be verified before determining preheat  
C) Use the standard preheat for any carbon steel (93°C / 200°F) and proceed  
D) Perform a spark test to verify the carbon content and proceed if the sparks look correct

**Correct: B**

**Explanation:** A516 Gr. 70 has minimum mechanical property requirements but the actual chemistry of any given heat may have CE significantly above 0.35 (requiring preheat) or below (not requiring it). Without the MTR, the CE cannot be calculated. Welding without verifying the CE is a code violation under CSA W59. Option A is wrong — grade alone doesn't guarantee CE. Option C applies an arbitrary preheat without basis. Option D — spark testing is a rough identification method not suitable for code welding material verification.

**Red Seal mapping:** A-4.01 (Uses documentation and reference material), A-5.03 (Controls temperature of weldments)

---

[^1]: [TWI Global — Job Knowledge: Metallurgy of Welding](https://www.twi-global.com/technical-knowledge/job-knowledge/metallurgy-of-welding-part-1-041); space lattice types, Ac₁/Ac₃ temperatures, dendritic solidification, HAZ zones and peak temperatures, columnar grain growth
[^2]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); iron-carbon diagram, transformation temperatures, grain refinement in multi-pass welds, cap pass toughness
[^3]: [Modern Welding (Bowditch et al., Goodheart-Willcox)](https://www.g-w.com/modern-welding); BCC/FCC/HCP diagrams, Hall-Petch relationship, grain growth mechanisms, spark test identification
[^4]: [CWB Group — Understanding Mill Test Reports for Welders](https://www.cwbgroup.org/education); MTR fields (heat number, chemistry, mechanical properties), CE calculation from MTR, traceability requirements
[^5]: [ESAB — Welding Metallurgy Fundamentals](https://www.esab.com/us/nam_en/education/blog/welding-metallurgy/); HAZ microstructure zones, coarse-grain HAZ cracking risk, grain refinement mechanisms, multi-pass refinement effect
