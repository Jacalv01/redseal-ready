---
id: p3-s2-a
period: 3
section: 2
section_title: Properties of Metals
topic_letter: A
topic_title: Heat Treatment
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to define and describe heat treatment
  fundamentals including preheat, interpass, postheat, and post-weld heat treatment (PWHT).
objectives:
  - Define heat-affected zones in metals.
  - Describe the difference between heat and temperature.
  - Describe the three forms of heat transfer.
  - Describe the effects of expansion and contraction.
  - Describe the purpose and effects of preheat and postheat.
  - Describe the practices of heat treatment.
  - Describe the principle of temperature-indicating devices.
red_seal_mapping:
  - A-5.03 (Controls temperature of weldments)
  - A-4.01 (Uses documentation and reference material)
  - D-13.04 (Performs weld using SMAW equipment)
citations:
  - source: ASME Boiler and Pressure Vessel Code Section VIII Division 1
    ref: UCS-56 (PWHT requirements for carbon and low-alloy steels), Table UCS-56 (temperature and time)
    url: https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-boiler-pressure-vessel-code-section-viii-division-1
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 4.4 (preheat and interpass temperature requirements by carbon equivalent)
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: Lincoln Electric — Procedure Handbook of Arc Welding
    ref: Chapter on heat treatment — preheat, PWHT, annealing, normalizing, tempering
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: TWI Global — Job Knowledge Article: Post Weld Heat Treatment
    ref: Purpose of PWHT, stress relief temperatures, methods of application
    url: https://www.twi-global.com/technical-knowledge/job-knowledge/post-weld-heat-treatment-pwht-043
  - source: Miller Electric — Welding With Low-Hydrogen Electrodes Guide
    ref: Preheat requirements by thickness, carbon equivalent, interpass temperature limits
    url: https://www.millerwelds.com/resources/article-library/low-hydrogen-welding-guide
---

# Heat Treatment

Welding puts enormous amounts of heat into metal in a very short time and in a very small area. What happens to the steel during and after that thermal cycle determines whether the weld will hold — or crack three months later when the pipeline pressurizes. Heat treatment is how we control those thermal effects before, during, and after welding.

---

## Heat vs Temperature — The Difference Matters

These two terms are confused constantly on the exam:[^3]

| Term | Definition | Example |
|---|---|---|
| **Temperature** | The measure of thermal energy intensity in a material (°C or °F) | A steel plate surface reads 150 °C |
| **Heat** | The total quantity of thermal energy in a material (joules, BTU) | A 50 mm thick plate at 150 °C holds FAR more heat than a 3 mm sheet at 150 °C |

**Why it matters for welding:** A thin plate can read 150 °C on the surface but have very little heat stored — it cools almost instantly after the preheat source is removed. A thick plate at the same temperature holds enormous heat. Preheat for thick plate is not just about surface temperature — you have to soak the heat through the thickness.

**Preheat soak time:** For thick plate (> 50 mm), allow the plate to soak at preheat temperature for at least 1 minute per 25 mm (1") of thickness after the preheat source is removed before welding, to ensure even temperature through the section.[^3]

---

## Three Forms of Heat Transfer

Heat moves from hot to cold by three mechanisms. All three operate simultaneously in welding:[^3]

| Mechanism | Description | Welding example |
|---|---|---|
| **Conduction** | Heat flows through solid material from hot region to cold region | The HAZ is heated by conduction from the weld pool outward into the base metal |
| **Convection** | Heat is carried by a moving fluid (liquid or gas) | Shielding gas carries heat away from the arc zone; water cooling in water-cooled torches |
| **Radiation** | Heat energy is emitted as electromagnetic radiation | The glow from a weld bead — you can feel radiant heat without touching the metal |

**Dominant mechanism in welding:** Conduction dominates heat distribution into the base metal. The rate of conductive heat flow determines HAZ width and temperature gradient.

---

## The Heat-Affected Zone (HAZ)

The HAZ is the region of base metal adjacent to the weld that was heated above room temperature but not melted.[^3][^4]

### HAZ temperature zones

Moving from the fusion line outward:[^3]

| Zone | Peak temperature range | Grain structure effect |
|---|---|---|
| **Partially melted zone** | 1300–1500 °C | Grains partially melted at boundaries — highest brittleness risk |
| **Coarse-grain HAZ** | 900–1300 °C | Rapid grain growth (above Ac₃) — brittleness, reduced toughness |
| **Fine-grain HAZ** | 730–900 °C | Grain refinement — actually improved properties (normalized) |
| **Intercritical zone** | 723–730 °C | Partial transformation — mixed microstructure |
| **Sub-critical HAZ** | Room temp to 723 °C | Overtempered, softened in Q&T steels |

**The coarse-grain HAZ is where cracks originate.** Hydrogen diffuses to the large grain boundaries here, especially in hardenable steels. Preheat slows cooling in this zone, reducing the risk.

---

## Expansion and Contraction

Steel expands when heated and contracts when cooled. Welding creates very localized expansion and contraction, which produces residual stress.[^3]

### Thermal expansion coefficient for mild steel
- Approximately **11.7 × 10⁻⁶ per °C** (or 6.5 × 10⁻⁶ per °F)[^3]
- A 1-metre length of steel heated 100 °C expands approximately 1.17 mm

### Why residual stress develops

1. The weld pool is liquid — no strength
2. Surrounding metal is cool and rigid — it resists the thermal expansion
3. When the weld solidifies and cools, it tries to contract
4. The rigid surrounding metal restrains the contraction
5. Result: **tensile residual stress in the weld and HAZ** — the weld is under tension even before any load is applied

High residual stress + a susceptible microstructure (coarse grain HAZ) + hydrogen = hydrogen-induced cracking (HIC). This is why preheat matters.

---

## Preheat

Preheat is the minimum temperature the base metal must reach before welding begins.[^1][^2]

### Why preheat works

1. **Slows cooling rate:** a slower cooling rate through the martensite transformation temperature (Ms, approximately 300–450 °C for mild steel) produces softer, less brittle martensite — or avoids martensite entirely
2. **Reduces residual stress:** slower cooling means the weld shrinks more gradually, reducing the magnitude of tensile residual stress
3. **Allows hydrogen to diffuse out:** hydrogen diffuses faster at elevated temperature. Preheat keeps the weld warm long enough for hydrogen to escape before it can accumulate at grain boundaries and cause cracking

### Calculating minimum preheat (CSA W59 Annex A)

Preheat is determined from the Carbon Equivalent (CE):[^2]

**CE = C + Mn/6 + (Cr + Mo + V)/5 + (Ni + Cu)/15**

| CE Range | Minimum preheat (CSA W59) |
|---|---|
| CE < 0.35 (t < 25 mm) | None required |
| CE 0.35 – 0.55 | 93 °C (200 °F) minimum |
| CE > 0.55 | 150 °C (300 °F) minimum, or per engineering |

**Source:** mill test report (MTR). The MTR contains the heat chemistry — look for C, Mn, Si, P, S, Ni, Cr, Mo, V, Cu values.

### Applying preheat

- **Heat source:** oxy-acetylene or propane torch (for field work), electric resistance blankets or induction heating (for precision code work)
- **Method:** apply heat to both sides of the joint, 75 mm (3") minimum away from the weld centerline, to ensure even penetration through the section
- **Verify:** with contact pyrometer, infrared temperature gun (calibrated), or temperature-indicating crayons (Tempilstik)
- **Tempilstik (temperature-indicating crayons):** a crayon made of wax that melts at a specific temperature. Apply to the metal 75 mm from the weld centerline — when the crayon smears (melts), the metal has reached that temperature. Available in increments of approximately 10–15 °C.[^3]

### Preheat extent

Heat a band on each side of the joint extending:[^2]
- At least 75 mm (3") from each edge of the weld
- The full thickness of the joint

---

## Interpass Temperature

Interpass temperature is the temperature of the base metal (measured at a specified distance from the weld) between successive weld passes in a multi-pass joint.[^2]

### Maximum interpass temperature

For most mild steel structural applications (CSA W59):[^2]
- **Maximum interpass temperature: 260 °C (500 °F)**

**Why there's a maximum:** excessive interpass temperature produces:
- Coarse grain growth between passes (poor HAZ toughness)
- Loss of strength in heat-treated or normalized steels
- For some alloy steels, risk of temper embrittlement

**Monitoring:** touch the surface 75 mm from the weld with a contact thermometer or calibrated IR gun. If above 260 °C, wait before starting the next pass.

---

## Postheat (Hydrogen Bake-Out)

Postheat is maintaining the weld at a temperature (typically 200–300 °C) for a defined period IMMEDIATELY after welding, before allowing it to cool.[^3]

### Purpose

- Allows hydrogen to diffuse out of the weld and HAZ before the temperature drops below ~150 °C (the temperature below which hydrogen diffusion becomes very slow)
- Required for very thick sections, high-carbon equivalent steels, or high-restraint joints where hydrogen cracking risk is elevated

### Typical postheat parameters (verify per WPS):[^3]

| Condition | Typical postheat |
|---|---|
| Carbon steel, CE 0.35–0.55, thick sections | 200–250 °C for 1–2 hours |
| Carbon steel, CE > 0.55 | 250–300 °C for 2–4 hours |

---

## Post-Weld Heat Treatment (PWHT) — Stress Relief

PWHT is a controlled thermal cycle applied to the entire weld joint (or entire vessel) after welding is complete.[^1][^4]

### Purpose of PWHT

1. **Stress relief:** high temperature reduces the yield strength of steel, allowing the residual stresses to redistribute (relax) below yield. After cooling, the steel is in a much lower residual stress state.
2. **Tempering of martensite:** the brittle martensite in the coarse-grain HAZ is tempered (softened and toughened) at PWHT temperatures
3. **Hydrogen diffusion:** extended time at temperature allows any remaining hydrogen to diffuse out
4. **Dimensional stability:** stress-relieved welds are more dimensionally stable in service (less distortion under load)

### PWHT requirements (ASME BPVC Section VIII Div 1, UCS-56)[^1]

| Base metal thickness (t) | PWHT required? |
|---|---|
| Carbon steel, t ≤ 19 mm (3/4") | Not required (unless design specifies) |
| Carbon steel, t > 19 mm | Required: 595–665 °C, 1 hr per 25 mm of thickness, 15 min minimum |
| Low-alloy steel (Cr-Mo) | Required at all thicknesses: 675–760 °C |

### PWHT temperature for carbon steel (ASME VIII)[^1]

- **Temperature:** 595–665 °C (1100–1225 °F)
- **Soak time:** 1 hour per 25 mm (1") of thickness, minimum 15 minutes
- **Heating rate:** max 55–220 °C/hr depending on thickness and code
- **Cooling rate:** max 260 °C/hr in the temperature range above 315 °C (to prevent thermal shock)

### PWHT methods

- **Furnace PWHT:** entire vessel placed in a controlled furnace — most uniform, required for pressure vessels per ASME VIII
- **Local PWHT:** electric resistance heating bands wrapped around a pipe joint — acceptable for piping under ASME B31.3 with specific requirements
- **Induction PWHT:** electromagnetic induction heats the metal — very precise temperature control, used in field and shop

---

## Other Heat Treatment Types

| Treatment | Description | Effect on steel |
|---|---|---|
| **Annealing (full)** | Heat to above Ac₃ (~900 °C), hold, cool in furnace | Maximum softening, stress relief, grain refinement — used on castings, forgings |
| **Normalizing** | Heat to above Ac₃, air cool | Refined, uniform grain structure — moderate hardness, good toughness |
| **Tempering** | Heat quench-hardened steel to 150–700 °C, hold, air cool | Increases toughness, reduces brittleness of martensite — part of quench-and-temper (Q&T) cycle |
| **Quench and Temper (Q&T)** | Austenitize, quench in water/oil, then temper | High strength and toughness — structural steels like A514/CSA G40.21 Grade 100W |
| **Stress Relief** | Heat to 595–650 °C for carbon steel, hold, slow cool | Reduces residual stress without changing microstructure significantly |

**Welding on Q&T steels:** maximum interpass temperature is typically 230 °C (450 °F) — lower than for normalized steel — because excess heat erases the temper and permanently softens the HAZ. Check the WPS.[^3]

---

## Temperature-Indicating Devices

| Device | Operating principle | Accuracy |
|---|---|---|
| **Tempilstik crayon** | Wax/salt melts at calibrated temperature when applied to metal surface | ±1% of rated temperature — good for precheck |
| **Contact pyrometer** | Thermocouple tip touches surface, reads millivolts converted to temperature | ±1–2°C — very accurate, required for PWHT monitoring |
| **Infrared (IR) thermometer** | Measures emitted infrared radiation — non-contact | ±1–2% — affected by surface emissivity (shiny steel reads low) |
| **Thermocouples (bonded)** | Welded or attached directly to the vessel — used for continuous monitoring during PWHT | ±0.5°C — required for ASME PWHT compliance |

**IR thermometer trap:** shiny, polished, or freshly sandblasted steel surfaces have lower emissivity than oxidized or painted surfaces. An IR gun calibrated for emissivity 0.95 (dull oxidized steel) will read too low on shiny steel. Use a contact pyrometer on shiny surfaces, or blacken the spot with a marker.[^3]

---

## Numbers you need to memorize

- **CE threshold for preheat (W59):** CE > 0.35 → preheat required for t > 25 mm[^2]
- **Minimum preheat, CE 0.35–0.55:** 93 °C (200 °F)[^2]
- **Minimum preheat, CE > 0.55:** 150 °C (300 °F)[^2]
- **Maximum interpass temperature (mild steel, W59):** 260 °C (500 °F)[^2]
- **PWHT temperature, carbon steel (ASME VIII UCS-56):** 595–665 °C (1100–1225 °F)[^1]
- **PWHT soak time:** 1 hour per 25 mm, 15 min minimum[^1]
- **PWHT threshold (carbon steel, ASME VIII):** required for t > 19 mm (3/4")[^1]
- **Stress relief temperature (general carbon steel):** 595–650 °C[^4]
- **Hydrogen diffusion temperature:** Below ~150 °C, hydrogen diffusion becomes very slow[^3]
- **Thermal expansion coefficient of steel:** ~11.7 × 10⁻⁶ per °C[^3]
- **Preheat extent:** 75 mm (3") from weld centerline, both sides[^2]

---

## What the textbook doesn't tell you

**Preheat does not fix bad technique.** Preheat reduces hydrogen cracking risk in the HAZ — it doesn't fix slag inclusions, undercut, or lack of fusion. Preheat is metallurgical protection, not a substitute for correct welding practice.[^3]

**The interpass temperature limit is frequently exceeded on busy jobsites.** When production pressure is high, the temptation is to keep welding without stopping to check temperature. The consequence — coarse-grain growth and potential HAZ toughness failures — doesn't show up until impact testing or in service under shock loads. Check the temperature. It's in the WPS for a reason.[^2]

**PWHT is permanent.** Once you stress-relieve a vessel, the residual stress is gone — but so is the microstructural hardness from cold work or previous heat treatment. If the vessel was designed to be PWHT'd, this is correct. If someone PWHT's a Q&T component by mistake, they've permanently softened it below spec.[^1]

**On field-welded pipe, thermocouples must be located correctly.** ASME B31.3 specifies exactly where thermocouples must be attached relative to the weld for local PWHT to qualify. If the thermocouple is in the wrong position, the weld doesn't meet the code requirement regardless of what temperature it showed.[^4]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s2-a-haz-zones.svg` — cross-section of a groove weld showing: fusion zone, partially melted zone, coarse-grain HAZ, fine-grain HAZ, intercritical zone, sub-critical HAZ, and base metal — each zone labeled with peak temperature range)*

*(SVG to be added: `assets/diagrams/p3-s2-a-pwht-cycle.svg` — temperature vs. time graph showing: heating ramp to soak temperature, hold time (1 hr/25mm), controlled cooling rate, with ASME temperature limits annotated)*

---

## Key terms

- **HAZ (Heat-Affected Zone):** the region of base metal that was heated but not melted by the welding process
- **Preheat:** the minimum temperature of the base metal before welding begins
- **Interpass temperature:** the temperature of the base metal between successive weld passes
- **Postheat:** heating applied immediately after welding to allow hydrogen to diffuse before cooling
- **PWHT (Post-Weld Heat Treatment):** a controlled thermal cycle applied after welding to relieve residual stress and temper the HAZ
- **Carbon Equivalent (CE):** a formula that relates steel chemistry to hardenability and preheat requirement
- **Stress relief:** PWHT at temperatures below the transformation range (Ac₁) to reduce residual stresses
- **Martensite:** a hard, brittle steel microstructure formed by rapid cooling from the austenite range — the main cracking risk in the coarse-grain HAZ
- **Tempilstik:** a temperature-indicating crayon that melts at a calibrated temperature
- **Soak time:** the duration at PWHT temperature — determines how completely the residual stress redistributes

---

## Common exam trap

- **PWHT temperature for carbon steel under ASME VIII is 595–665 °C (1100–1225 °F)** — NOT 700 °C or 900 °C. Distractors will offer temperatures outside this range.
- **Interpass MAX (not min) is 260 °C.** The exam may ask "what is the maximum interpass temperature for mild steel?" The answer is 260 °C / 500 °F.
- **Preheat is measured 75 mm FROM the weld centerline** — not right at the joint edge and not 100 mm away.
- **Stress relief ≠ full anneal.** Stress relief is below Ac₁ (no phase transformation). Full anneal is above Ac₃ (full transformation). They produce very different microstructures.
- **CE formula denominators: 6, 5, 15.** They will give you wrong denominators (3, 7, 10) in the options. Memorize: Mn/6, (Cr+Mo+V)/5, (Ni+Cu)/15.

---

## Practice question preview

**Q:** A carbon steel pressure vessel shell is 32 mm thick. According to ASME BPVC Section VIII Division 1, which statement about PWHT is correct?

A) PWHT is not required because the thickness is less than 38 mm  
B) PWHT is required at 595–665 °C for a minimum of 1.5 hours  
C) PWHT is required at 595–665 °C; soak time = 1 hour per 25 mm of thickness  
D) PWHT is optional if the welder has a 6G qualification

**Correct: C**

**Explanation:** ASME BPVC Section VIII UCS-56 requires PWHT for carbon steel exceeding 19 mm (3/4") thickness. 32 mm exceeds this threshold. The required temperature range is 595–665 °C and soak time is 1 hour per 25 mm of thickness — for 32 mm, that is approximately 1.28 hours (rounded up in practice). Option A is wrong — the threshold is 19 mm, not 38 mm. Option B states 1.5 hours as a fixed time, which is not how the code works. Option D is wrong — welder qualification does not exempt the joint from PWHT requirements.

**Red Seal mapping:** A-5.03 (Controls temperature of weldments)

---

[^1]: [ASME BPVC Section VIII Division 1](https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-boiler-pressure-vessel-code-section-viii-division-1); UCS-56 (PWHT requirements for carbon and low-alloy steels), Table UCS-56 (temperature 595–665°C, 1 hr/25 mm, 19 mm threshold)
[^2]: [CSA W59 — Welded Steel Construction (2018)](https://www.csagroup.org/store/product/CSA%20W59%3A18/); Clause 4.4 (preheat and interpass temperature by CE), Annex A (CE formula), maximum interpass 260°C, preheat extent 75 mm
[^3]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); heat vs. temperature, HAZ zone descriptions, soak time for thick plate, postheat for hydrogen removal, Tempilstik use, Q&T steel cautions
[^4]: [TWI Global — Job Knowledge: Post Weld Heat Treatment (PWHT)](https://www.twi-global.com/technical-knowledge/job-knowledge/post-weld-heat-treatment-pwht-043); purpose of PWHT, stress relief effect, furnace vs. local PWHT, thermocouple placement requirements
[^5]: [Miller Electric — Welding With Low-Hydrogen Electrodes Guide](https://www.millerwelds.com/resources/article-library/low-hydrogen-welding-guide); preheat requirements by thickness and CE, interpass temperature limits, hydrogen cracking prevention
