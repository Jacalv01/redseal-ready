---
id: p3-s2-b
period: 3
section: 2
section_title: Properties of Metals
topic_letter: B
topic_title: Stainless Steel
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to identify and describe stainless
  steels, the AISI numbering system, carbide precipitation, sensitization, and welding
  filler materials.
objectives:
  - Describe stainless steel.
  - Identify types of stainless steel and their properties.
  - Identify the AISI numbering system of stainless steel.
  - Identify carbide precipitation and ways of overcoming this problem.
  - Identify the major types of stainless steel filler materials and AWS specifications.
  - Describe handling and storage of stainless steel electrodes and filler materials.
  - Describe the handling procedures and preparation for welding stainless steel.
red_seal_mapping:
  - D-13.01 (Selects SMAW equipment and consumables)
  - D-15.01 (Selects GTAW gas, equipment and consumables)
  - A-4.01 (Uses documentation and reference material)
  - A-5.03 (Controls temperature of weldments)
citations:
  - source: Lincoln Electric — Stainless Steel Welding Guide
    ref: Types of stainless steel, filler selection, sensitization, interpass temperature
    url: https://www.lincolnelectric.com/en/education-center/welding-education/stainless-steel-welding-guide
  - source: ESAB — Stainless Steel Welding Manual
    ref: AISI numbering system, austenitic/ferritic/martensitic/duplex properties, AWS classifications
    url: https://www.esab.com/us/nam_en/education/blog/stainless-steel-welding-overview/
  - source: TWI Global — Stainless Steel Welding Knowledge Base
    ref: Carbide precipitation, sensitization, L-grade and stabilized grades, duplex metallurgy
    url: https://www.twi-global.com/technical-knowledge/job-knowledge/welding-stainless-steels-part-1-039
  - source: AWS A5.4 — Stainless Steel Electrodes for SMAW
    ref: E308L, E309, E316L electrode classifications and chemistry requirements
    url: https://pubs.aws.org/p/1086/a54-a54m-2006-specification-for-stainless-steel-electrodes-for-shielded-metal-arc-welding
  - source: AWS A5.9 — Stainless Steel Bare Electrodes and Rods
    ref: ER308L, ER309L, ER316L filler rod classifications
    url: https://pubs.aws.org/p/1097/a59-a59m2012-specification-for-bare-stainless-steel-welding-electrodes-and-rods
---

# Stainless Steel — Metallurgy and Welding

Stainless steel shows up in every industrial sector: food processing, chemical plants, refineries, pulp and paper, offshore platforms. The reason is corrosion resistance — but that resistance comes at a cost. Stainless steel behaves very differently from mild steel in the heat of a weld. Ignore those differences and the weld fails in service despite looking perfect from the outside.

---

## What Makes Steel "Stainless"

A steel is classified as stainless when it contains at least **10.5% chromium** by weight.[^1][^2]

Chromium reacts with oxygen to form a thin, dense chromium oxide layer (Cr₂O₃) on the surface — typically 1–5 nm thick. This layer is:
- **Self-healing:** if scratched or abraded, it reforms in the presence of air or water
- **Impermeable:** prevents oxygen and moisture from reaching the steel beneath
- **Invisible:** colorless and transparent — the steel still looks metallic

**Above 12% Cr:** strongly corrosion-resistant to atmospheric conditions. Higher Cr contents extend resistance to acids, chlorides, and high-temperature oxidation.

**Other alloying elements in stainless steel:**
- **Nickel (Ni):** stabilizes the austenite structure, improves toughness and corrosion resistance
- **Molybdenum (Mo):** improves resistance to pitting (especially chloride attack) — 316 has 2% Mo
- **Carbon (C):** can cause sensitization (the main welding problem — see below)
- **Titanium (Ti) and Niobium (Nb):** added in stabilized grades to prevent sensitization

---

## The Four Main Types of Stainless Steel

### 1. Austenitic (300 Series)

- **AISI range:** 301–321 (common: 304, 304L, 316, 316L, 321, 347)
- **Structure:** FCC (face-centered cubic) — austenite at all temperatures
- **Key properties:** non-magnetic (in annealed state), excellent ductility, excellent corrosion resistance, good weldability, work hardens rapidly
- **Main alloy:** 18% Cr, 8–10% Ni (hence "18-8" stainless)
- **The most common type in welding**

### 2. Ferritic (400 Series — low carbon)

- **AISI range:** 405, 409, 430, 439, 444
- **Structure:** BCC (body-centered cubic) — ferrite, similar to mild steel
- **Key properties:** magnetic, lower ductility than austenitic, limited weldability (grain coarsening in HAZ is severe), less corrosion resistant than austenitic
- **Applications:** automotive exhaust, appliances, some vessels

### 3. Martensitic (400 Series — higher carbon)

- **AISI range:** 410, 416, 420, 431, 440A/B/C
- **Structure:** BCT (body-centered tetragonal) martensite when quenched from austenite
- **Key properties:** hardenable (can be heat-treated to high hardness), magnetic, lower corrosion resistance, poor weldability (high cracking risk without preheat)
- **Applications:** cutlery, shafts, pump components, turbine blades
- **Welding precaution:** preheat and controlled interpass temperature essential to avoid HAZ cracking

### 4. Duplex (e.g., 2205, 2507)

- **Structure:** approximately 50% austenite + 50% ferrite
- **Key properties:** higher strength than austenitic, excellent resistance to stress corrosion cracking (SCC) and pitting, more difficult to weld than austenitic
- **Applications:** offshore, subsea piping, chemical vessels under chloride service
- **Welding precaution:** interpass temperature max 150 °C (much lower than austenitic), controlled heat input to maintain proper ferrite/austenite ratio in the weld

---

## AISI Numbering System

| Series | Type | Examples |
|---|---|---|
| **2xx** | Austenitic (Cr-Mn, low Ni) | 201, 202 |
| **3xx** | Austenitic (Cr-Ni) | 304, 304L, 316, 316L, 321, 347 |
| **4xx** | Ferritic or Martensitic | 409 (ferritic), 410 (martensitic), 430 (ferritic) |
| **Duplex** | No standard AISI number — use trade designation | 2205 (22% Cr, 5% Ni), 2507 |

### Reading a 3xx designation[^2]

- **304:** Standard austenitic. 18% Cr, 8% Ni. The most common stainless in general industry.
- **304L:** Low-carbon (max 0.03% C). Better sensitization resistance. Use when welding.
- **316:** 18% Cr, 10% Ni, 2% Mo. Better pitting resistance for chloride environments.
- **316L:** Low-carbon 316. Standard for marine, chemical, and food service where welding is involved.
- **321:** Ti-stabilized. Carbon is tied up by Ti rather than Cr — prevents sensitization.
- **347:** Nb-stabilized. Similar function to 321 but with Nb (columbium) as the stabilizer.

---

## Carbide Precipitation and Sensitization

This is the most important metallurgical concept in stainless steel welding.[^1][^3]

### What happens during welding

When austenitic stainless steel is heated to the **sensitization temperature range: 427–816 °C (800–1500 °F)**, chromium combines preferentially with carbon to form chromium carbides (Cr₂₃C₆) at the grain boundaries.[^3]

The chromium carbides precipitate at the grain boundaries because that's where diffusion is fastest. The result:
- **Chromium is depleted** at the grain boundary regions (below the 10.5% threshold)
- **The grain boundaries become susceptible to corrosion** — specifically intergranular corrosion (IGC) and stress corrosion cracking (SCC)
- This sensitized steel corrodes at the grain boundaries in service, even though the grain interiors remain stainless

**The weld HAZ passes through the sensitization temperature range.** This is unavoidable — it happens in every austenitic stainless steel weld that isn't of a "low-carbon" or "stabilized" grade.

### Solutions to sensitization

| Solution | How it works | Notes |
|---|---|---|
| **Use L-grade (304L, 316L)** | Max 0.03% C — so little carbon that insufficient chromium carbides can form to cause sensitization | The go-to solution for most austenitic stainless welding |
| **Use stabilized grades (321, 347)** | Ti or Nb has greater affinity for carbon than Cr does — the carbides form with Ti or Nb instead of Cr | Good for service at sensitization temperatures (e.g., furnace applications) |
| **Solution annealing** | Heat the entire part to 1040–1150 °C, then quench — dissolves the carbides back into solution | Re-homogenizes the microstructure; not always practical post-welding |
| **Minimize heat input** | Lower amperage, faster travel, smaller passes — reduces time in the sensitization range | Combined with L-grade for best results |
| **Control interpass temperature** | Maximum 177 °C (350 °F) for austenitic stainless — limits cumulative time in sensitization range[^1] | Critical for multi-pass welds |

---

## Filler Metal Selection for Stainless Steel

### AWS A5.4 — SMAW electrodes for stainless[^4]

| Electrode | Base metal matched | Notes |
|---|---|---|
| **E308L-16** | 304L (and 304) | Most common austenitic stainless SMAW electrode |
| **E308L-15** | 304L | DC+ only (15 suffix), slightly different flux system |
| **E309L-16** | Dissimilar: stainless to carbon steel, or 309 stainless | "Buffer layer" electrode when welding stainless to carbon steel |
| **E316L-16** | 316L (and 316) | For chloride service applications |
| **E347-16** | 347 (stabilized) | Nb-stabilized electrode, for high-temperature service |
| **E410-15** | 410 martensitic | Requires preheat and PWHT — DC+ only |

**Classification system:** E (electrode) + chemistry number + flux code (15 = DC+, 16 = AC or DC+, 17 = AC or DC+, special flux)[^4]

### AWS A5.9 — GTAW/GMAW filler rods for stainless[^5]

| Filler | Use |
|---|---|
| **ER308L** | 304L base — most common GTAW stainless filler |
| **ER309L** | Dissimilar (stainless to carbon), overlay on carbon steel |
| **ER316L** | 316L base — chloride environments |
| **ER347** | 347 base — high temperature, Nb-stabilized |

**Rule of thumb:** For 304L base metal, use ER308L filler. For 316L base metal, use ER316L filler. For stainless-to-carbon steel dissimilar joints, use ER309L.[^1][^3]

---

## Handling and Preparation for Welding Stainless Steel

Stainless steel requires cleaner preparation than mild steel because any contamination risks:[^1][^2]

1. **Iron contamination:** carbon steel particles embedded in stainless surface will rust and stain — creating a "rust bleed" that mimics the HAZ damage of sensitization
2. **Oil and grease:** causes porosity and carbon pickup in the weld
3. **Chloride contamination:** any chloride (including fingerprints with salt) can initiate pitting corrosion at the weld surface

### Preparation rules

- **Dedicated tools:** stainless steel grinding discs, wire wheels, and sanding products must NEVER be used on carbon steel before use on stainless. Contamination from carbon steel embeds iron particles. Label tools.
- **Stainless wire brush only:** never use a carbon steel wire brush on stainless — iron contamination
- **Clean with acetone or dedicated stainless cleaner:** wipe the joint area before welding; do not touch with bare hands after cleaning
- **No galvanized or zinc-coated fixtures:** zinc fumes from coated steel near a stainless weld cause liquid metal embrittlement in some alloys
- **Passivation after welding:** for food-grade or corrosive service, the completed weld is acid-cleaned (passivated) with nitric acid or citric acid solution to restore the chromium oxide layer damaged by heat and oxidation[^3]

### Electrode storage

Low-hydrogen electrodes for stainless (AWS A5.4) should be stored in sealed containers or a rod oven at 120–150 °C when not in use — similar to E7018 storage. Moisture pickup in the coating causes porosity and increases diffusible hydrogen.[^4]

---

## Numbers you need to memorize

- **Minimum Cr for stainless:** 10.5% chromium[^2]
- **Sensitization temperature range:** 427–816 °C (800–1500 °F)[^3]
- **Maximum interpass temperature for austenitic stainless:** 177 °C (350 °F)[^1]
- **Maximum interpass temperature for duplex stainless:** 150 °C[^3]
- **L-grade max carbon:** 0.03% C (304L, 316L)[^2]
- **Standard 304 composition:** 18% Cr, 8% Ni[^2]
- **316 addition:** 2% Mo (for chloride pitting resistance)[^2]
- **E308L-16:** most common SMAW electrode for 304/304L base[^4]
- **ER308L:** most common GTAW filler for 304/304L base[^5]
- **E309L-16 / ER309L:** used for stainless-to-carbon-steel dissimilar joints[^4][^5]

---

## What the textbook doesn't tell you

**The "L" in 304L saves welds every day.** Specifying standard 304 (max 0.08% C) for welded construction is technically an error in many codes — it should be 304L (max 0.03% C). On a real job, verify the base metal heat number and compare to the mill cert. If the cert shows C > 0.03%, that's standard 304, not 304L — escalate to engineering before welding.[^3]

**Austenitic stainless doesn't need preheat — but heat input still matters.** Unlike carbon steel, austenitic stainless is not hardenable (no martensite). You don't preheat to prevent martensite. But you DO control heat input to minimize time in the sensitization range and to control distortion (stainless distorts much more than mild steel — about 50% more thermal expansion).[^1]

**Color matters after welding.** A properly shielded stainless GTAW weld should show a light gold or straw-colored oxide — maximum acceptable. A blue oxide means more heat than ideal. A gray or black oxide means inadequate shielding or torch contamination. Black oxide = clean and grind before the next pass — otherwise you're welding over contaminated metal.[^2]

**Duplex stainless is a different animal.** Its higher strength tempts welders to use it at higher heat inputs, but the ferrite/austenite ratio in the weld is very sensitive to heat input and cooling rate. Too high = excessive ferrite (brittle). Too low = excessive austenite (susceptible to SCC). Always follow the WPS for duplex — this is not a "feel it out" material.[^3]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s2-b-sensitization.svg` — grain boundary diagram showing: before welding (uniform Cr distribution), during sensitization (Cr₂₃C₆ carbides precipitating at boundaries, Cr-depleted zones), and intergranular corrosion path in service — three sequential images)*

*(SVG to be added: `assets/diagrams/p3-s2-b-stainless-types.svg` — comparison table diagram showing: 4 stainless types, their crystal structure (FCC/BCC/BCT), magnetic property, weldability rating, and main AISI numbers)*

---

## Key terms

- **Austenitic:** FCC stainless steel (300 series) — non-magnetic, excellent ductility, most weldable type
- **Ferritic:** BCC stainless steel (400 series, low C) — magnetic, limited weldability, HAZ grain coarsening
- **Martensitic:** hardenable stainless (400 series, higher C) — high hardness potential, poor weldability, requires preheat
- **Duplex:** mixed austenite/ferrite structure — high strength, SCC resistant, controlled heat input essential
- **Sensitization:** chromium depletion at grain boundaries due to carbide precipitation — makes the steel susceptible to intergranular corrosion
- **Chromium carbide (Cr₂₃C₆):** the carbide that precipitates at grain boundaries in the sensitization range
- **L-grade:** low-carbon stainless (304L, 316L) — max 0.03% C — the primary solution to sensitization
- **Stabilized grade:** stainless containing Ti (321) or Nb (347) — the stabilizer ties up carbon, preventing Cr carbide formation
- **Passivation:** acid treatment of welded stainless surface to restore the chromium oxide passive layer
- **Intergranular corrosion (IGC):** corrosion that propagates along grain boundaries in sensitized stainless

---

## Common exam trap

- **Sensitization temperature range is 427–816 °C (800–1500 °F)** — not 500–900 °C or 600–1000 °C. The exact range matters.
- **304L = max 0.03% C; 304 = max 0.08% C.** Both are "18-8 austenitic." Only 304L is suitable for welded fabrication in corrosive service.
- **E309L is for DISSIMILAR welds** (stainless to carbon steel) — not for welding 309 stainless to itself. If the question asks "which electrode for joining 304L to A36?" — E309L.
- **Stainless does NOT need preheat to prevent martensite.** Austenitic stainless doesn't transform to martensite. If the question asks "why do you preheat austenitic stainless?" — you generally don't. Preheat is for martensitic and some ferritic grades only.
- **Maximum interpass for stainless is 177 °C — much lower than for mild steel (260 °C).** This is a frequent exam distinguisher.
- **Dedicated tools — never share with carbon steel.** A stainless-contaminated grinding disc from a carbon steel job will fail every stainless inspection.

---

## Practice question preview

**Q:** A welder is making a multi-pass GTAW weld on 316L stainless steel pipe. After several passes, the weld surface shows a dark blue-gray oxide coloration. What does this indicate and what should be done?

A) Dark blue coloration is normal for GTAW stainless — continue welding  
B) The shielding gas coverage was inadequate; clean and grind the affected area before the next pass  
C) The interpass temperature is too low; increase preheat before continuing  
D) The filler metal needs to be changed from ER316L to ER308L

**Correct: B**

**Explanation:** On properly shielded GTAW stainless welds, the acceptable oxide color is light gold or straw. Blue oxide indicates more heat than ideal (acceptable in some cases). Dark blue-gray or black oxide indicates significant contamination from poor shielding gas coverage — oxygen reacted with the hot weld surface, destroying the passive layer and oxidizing the metal. This contaminated surface must be cleaned and ground before the next pass, otherwise you are welding into contaminated metal which causes porosity and loss of corrosion resistance. C is wrong — stainless austenitic does not require preheat. D is wrong — ER316L is the correct filler for 316L base.

**Red Seal mapping:** D-15.04 (Performs weld using GTAW equipment)

---

[^1]: [Lincoln Electric — Stainless Steel Welding Guide](https://www.lincolnelectric.com/en/education-center/welding-education/stainless-steel-welding-guide); types of stainless, sensitization explanation, interpass temperature (177°C max for austenitic), filler metal selection guide, weld color significance
[^2]: [ESAB — Stainless Steel Welding Manual](https://www.esab.com/us/nam_en/education/blog/stainless-steel-welding-overview/); AISI numbering system, minimum Cr (10.5%), 304/316 compositions, handling procedures, dedicated tooling requirements
[^3]: [TWI Global — Welding Stainless Steels (Job Knowledge Series)](https://www.twi-global.com/technical-knowledge/job-knowledge/welding-stainless-steels-part-1-039); sensitization temperature range (427–816°C), L-grade and stabilized grade solutions, duplex interpass temperature (150°C), passivation
[^4]: [AWS A5.4 — Stainless Steel Electrodes for SMAW](https://pubs.aws.org/p/1086/a54-a54m-2006-specification-for-stainless-steel-electrodes-for-shielded-metal-arc-welding); E308L-16, E309L-16, E316L-16 classifications, flux code suffix meanings, storage requirements
[^5]: [AWS A5.9 — Stainless Steel Bare Electrodes and Rods](https://pubs.aws.org/p/1097/a59-a59m2012-specification-for-bare-stainless-steel-welding-electrodes-and-rods); ER308L, ER309L, ER316L, ER347 classifications and chemistry
