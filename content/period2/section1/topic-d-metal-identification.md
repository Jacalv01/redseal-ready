---
id: p2-s1-d
period: 2
section: 1
section_title: Foundational Skills, Safety, Procedures and Properties of Metals
topic_letter: D
topic_title: Metal Identification
hours: 3
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to identify and describe metals by their physical and mechanical properties.
objectives:
  - Identify metals by physical and mechanical properties.
  - Describe chip, spark, file hardness and flame tests.
  - Describe the mechanical properties of metals.
  - Describe the physical properties of metals.
red_seal_mapping:
  - A-4.04 (Organizes materials)
  - A-5.05 (Selects welding processes and power source)
  - B-8.01 (Prepares materials)
citations:
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 19 — Properties of Metals; physical properties, mechanical properties, identification methods
    url: https://www.g-w.com/modern-welding
  - source: Lincoln Electric — Metals & Their Weldability
    ref: Steel classification, AISI/SAE numbering, spark test guide, identification of ferrous and non-ferrous metals
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: TWI Global — Metal Properties and Identification
    ref: Mechanical property definitions (tensile, yield, elongation, impact toughness), testing methods
    url: https://www.twi-global.com/technical-knowledge/faqs
  - source: CWB Group — Welder Certification Study Guide
    ref: Carbon steel classification, identification tests, weldability
    url: https://www.cwbgroup.org/education/learning-resources
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic D
    ref: pp. 29–30
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Metal Identification

You will spend your career welding metals that aren't always labelled. Scrap yards. Repair jobs. Unknown stock in a shop corner. Getting it wrong — welding a high-carbon steel with the wrong procedure, or fusing a non-weldable alloy — produces failures. Worse, you can waste a day's work on a weld that cracks the next morning in the heat-affected zone. Metal identification is a diagnostic skill, and it starts with understanding *what properties distinguish metals from each other*.

---

## Physical properties vs mechanical properties

These are two different categories, and exam questions frequently test whether you can tell them apart.[^1]

### Physical properties — what the metal *is*

Physical properties are intrinsic characteristics — they don't depend on what you do to the metal.

| Property | Definition | Example values |
|---|---|---|
| **Density** | Mass per unit volume (kg/m³ or g/cm³) | Steel ~7.85 g/cm³; Aluminum ~2.7 g/cm³; Lead ~11.3 g/cm³ |
| **Melting point** | Temperature at which solid becomes liquid | Mild steel ~1510°C; Aluminum ~660°C; Copper ~1085°C |
| **Thermal conductivity** | Rate of heat transfer through the material | Copper (high); Aluminum (high); Steel (medium); Stainless (low) |
| **Electrical conductivity** | Rate of electrical current transfer | Copper > aluminum >> steel |
| **Colour and lustre** | Surface appearance of fresh, clean metal | Copper = reddish; Aluminum = silver-grey; Brass = yellow |
| **Thermal expansion coefficient** | How much material expands per °C | Steel ~12 × 10⁻⁶/°C; Aluminum ~23 × 10⁻⁶/°C — aluminum expands ~twice as much as steel[^1] |
| **Magnetism** | Whether the metal is attracted to a magnet | Carbon steel/ferritic stainless = magnetic; Austenitic stainless (304, 316) = non-magnetic; Aluminum = non-magnetic |

### Mechanical properties — how the metal *behaves under load*

Mechanical properties describe response to applied forces. These are determined by tensile testing (ASTM/CSA standards).[^3]

| Property | Definition | How measured |
|---|---|---|
| **Tensile strength (UTS)** | Maximum stress before fracture (MPa or psi) | Tensile test — pulled to failure |
| **Yield strength** | Stress at which permanent deformation begins (MPa or psi) | Tensile test — 0.2% offset method |
| **Elongation** | % increase in gauge length at fracture — measures ductility | Tensile test — compare original vs final gauge length |
| **Hardness** | Resistance to surface indentation | Brinell (BHN), Rockwell (HRC/HRB), Vickers (HV) tests |
| **Impact toughness** | Energy absorbed before fracture at low temperature — measures notch toughness | Charpy V-notch test (in Joules) |
| **Fatigue strength** | Stress level that can be sustained for infinite load cycles without cracking | Cyclic loading tests |

**Critical relationship for welders:** High tensile strength metals typically have higher carbon content → lower ductility → **harder to weld**. Ductility (elongation %) is what allows the weld and HAZ to flex and deform when stressed — a brittle material cracks instead.

---

## The AISI/SAE steel numbering system

The most important classification system in a North American shop.[^2]

**Format:** 4-digit number — first two digits = alloy series, last two (sometimes three) digits = carbon content in hundredths of 1%.

### Common series:

| AISI/SAE Series | Main alloying element(s) | Examples |
|---|---|---|
| **10xx** | Carbon only (plain carbon steel) | 1010 (low C), 1045 (medium C), 1095 (high C) |
| **11xx** | Carbon + sulfur (free-machining) | 1141, 1144 |
| **13xx** | Manganese | 1340 |
| **41xx** | Chromium + molybdenum | 4130, 4140 (Cr-Mo, common in oil & gas) |
| **43xx** | Nickel + chromium + molybdenum | 4340 (high-strength alloy) |
| **51xx** | Chromium | 5160 (spring steel) |
| **86xx** | Nickel + chromium + molybdenum | 8620 (low-alloy case-hardening) |

### Reading the carbon content:
- **10**18 → 1018 = plain carbon, 0.18% carbon → **low carbon steel (weldable, no preheat usually needed)**[^2]
- **10**45 → 1045 = plain carbon, 0.45% carbon → **medium carbon steel (preheat required)**[^2]
- **10**95 → 1095 = plain carbon, 0.95% carbon → **high carbon steel (very hard to weld, may crack)**[^2]

**Carbon Equivalent (CE) formula:** Determines preheat need for alloy steels.[^4]
> CE = C + Mn/6 + (Cr + Mo + V)/5 + (Ni + Cu)/15
>
> CE < 0.35 → generally no preheat required for mild steel thicknesses
> CE 0.35–0.60 → preheat required, amount depends on thickness and restraint
> CE > 0.60 → high preheat required; specialized procedure

---

## Metal identification tests (field methods)

When there's no label, use these tests in combination. No single test gives a definitive answer.[^1][^2]

### 1. Magnet test
**Procedure:** Hold a magnet to the clean metal surface.
- **Strongly attracted:** Plain carbon steel, cast iron, low-alloy steel, ferritic stainless steel
- **Not attracted (non-magnetic):** Austenitic stainless steel (304, 316), aluminum, copper, brass, bronze, most non-ferrous
- **Weakly attracted:** Some duplex stainless steels (partially ferritic)

**Limitation:** Tells you it's ferrous OR that it's austenitic SS/non-ferrous. Doesn't distinguish between carbon steel and alloy steel.

### 2. Spark test
**Procedure:** Hold the metal to a bench grinder and observe the spark stream.

| Metal | Spark characteristics |
|---|---|
| **Low carbon steel (1010–1025)** | Long, straight orange streams, few bursts |
| **Medium carbon steel (1040–1060)** | Shorter streams, more white bursts near the end |
| **High carbon steel (1080–1095)** | Very short streams, many bright white star-shaped bursts |
| **Cast iron** | Short, dull red streams; dense, close to wheel |
| **Stainless steel (304)** | Long orange streams, very few bursts (different from plain carbon) |
| **Wrought iron** | Long streaks, few bursts, characteristic "tail" at end |
| **Manganese steel** | Similar to high-carbon but with gold-coloured bursts |

**Use spark testing to distinguish carbon content in plain steels.** More bursts = more carbon.[^1][^2]

### 3. File hardness test
**Procedure:** Draw a new, sharp file firmly across the metal surface.
- **File cuts freely (leaves a groove):** Soft metal — annealed steel, aluminum, copper
- **File skips and skates with little cutting:** Hard metal — hardened high-carbon steel, chrome hard-face, tool steel (HRC 60+)
- **File bites slightly but with effort:** Medium hardness — normalized medium carbon steel

**Limitation:** Only gives relative hardness; can't distinguish between alloy types of similar hardness.

### 4. Chip test
**Procedure:** Strike the edge of the metal with a cold chisel.
- **Long, curled chip:** Ductile metal — mild steel, aluminum, copper, soft brass
- **Short, brittle chip or no chip (shatters):** Brittle material — cast iron, hardened steel
- **Powdery chip:** Cast iron typically — carbon comes off as graphite flakes

**Cast iron is the key material the chip test identifies:** The chip (or rather the shatter) is distinctive and immediate.[^2]

### 5. Flame test
**Procedure:** Apply an oxyfuel flame to a small area and observe the colour, oxide formation, and melting characteristics.
- **Steel (low/med carbon):** Red-orange glow before melting; melts to a liquid pool; no white oxides
- **Stainless steel:** Forms black/dark oxide coating quickly; does not cut cleanly with oxyfuel
- **Aluminum:** Appears to "suddenly melt" without glowing red (melts at 660°C but does not oxidize red); surface forms a thin white oxide skin first — you won't see it coming
- **Copper:** Orange-red glow, easily melted, green tinged flame from copper vapour
- **Cast iron:** Glows but won't flow or cut cleanly; produces black oxide

---

## Non-ferrous metals: quick ID guide

| Metal | Colour (clean) | Magnet | Weight | Key welding notes |
|---|---|---|---|---|
| **Aluminum** | Silver-grey | No | Light (2.7 g/cm³) | Oxide melts at 2050°C (base metal at 660°C) — must remove oxide first |
| **Copper** | Reddish-orange | No | Heavy (8.9 g/cm³) | High thermal conductivity; needs high preheat |
| **Brass (Cu-Zn)** | Yellow | No | Heavy | Zinc fumes when welded — ventilation mandatory |
| **Bronze (Cu-Sn)** | Golden-brown | No | Heavy | Can be welded; usually brazed instead |
| **Lead** | Blue-grey, dull | No | Very heavy (11.3 g/cm³) | Extremely toxic fumes; avoid welding |
| **Titanium** | Silver-grey | No | Light-medium (4.5 g/cm³) | Extremely reactive; requires inert-gas back-purging |

---

## Numbers you need to memorize

- **Thermal expansion (mild steel):** ~12 × 10⁻⁶/°C[^1]
- **Thermal expansion (aluminum):** ~23 × 10⁻⁶/°C — nearly twice steel[^1]
- **Melting point (mild steel):** ~1510°C[^1]
- **Melting point (aluminum):** ~660°C[^1]
- **Melting point (aluminum oxide / Al₂O₃):** ~2050°C — much higher than base metal[^1]
- **Carbon content — low carbon steel:** 0.05–0.25%[^2]
- **Carbon content — medium carbon steel:** 0.25–0.60%[^2]
- **Carbon content — high carbon steel:** 0.60–1.4%[^2]
- **CE < 0.35:** typically no preheat; CE > 0.60: high preheat required[^4]
- **Density comparison:** Lead (11.3) > Copper (8.9) > Steel (7.85) > Titanium (4.5) > Aluminum (2.7) g/cm³[^1]

---

## What the textbook doesn't tell you

**The magnet test tells you the metallurgical condition, not just the alloy.** Work-hardened (cold-worked) austenitic stainless (304) can become slightly magnetic — the deformation changes the crystal structure from austenite to martensite. If a stainless part tests weakly magnetic, it might be a heavily cold-worked 304, not ferritic stainless. Check with a chemical spot test or spectrometer to be sure.

**Spark testing requires a consistent grinding technique.** Apply the same pressure each time. Too light = long, low-energy sparks. Too heavy = you're seeing friction heat, not the steel's own carbon-related bursts. Practice on known samples (1020, 1040, 1080) so you have a reference baseline in your muscle memory.

**Aluminum's oxide problem is unique.** Every time you grind, file, or scratch aluminum, a new oxide layer forms within seconds. This isn't a defect — it's why aluminum doesn't rust. But for GTAW on aluminum (AC current, cathodic cleaning), the arc breaks up the oxide continuously. For GMAW on aluminum, you must brush with a stainless steel brush dedicated only to aluminum, immediately before welding, every time.[^1]

---

## Key terms

- **Physical property:** intrinsic characteristic of a material (density, melting point, conductivity, thermal expansion, colour)
- **Mechanical property:** response to applied force (tensile strength, yield strength, elongation, hardness, impact toughness)
- **Tensile strength (UTS):** stress at failure — the maximum the material can handle
- **Yield strength:** stress at which permanent (plastic) deformation begins
- **Elongation:** ductility measurement — % increase in length at fracture; higher = more ductile
- **Impact toughness:** energy absorbed before fracture (Charpy V-notch, in Joules) — especially important at low temperatures
- **Hardness:** resistance to surface indentation (Brinell, Rockwell, Vickers scales)
- **AISI/SAE number:** 4-digit classification for steels; first two digits = alloy type, last two = carbon content × 100
- **Carbon equivalent (CE):** formula combining carbon and alloying elements to predict preheat requirement and weldability
- **Spark test:** identification method using a grinder to produce characteristic spark patterns indicating carbon content
- **Chip test:** identification method using a chisel to observe chip character (ductile vs brittle)
- **Ferrous:** iron-based metals (steel, cast iron)
- **Non-ferrous:** non-iron-based metals (aluminum, copper, titanium, etc.)

---

## Common exam trap

- **Physical vs mechanical properties — know the difference.** Tensile strength, hardness, elongation are MECHANICAL. Density, melting point, conductivity, colour are PHYSICAL. Exam questions frequently misplace one or two on a list.
- **Higher carbon = more spark bursts = LESS weldable, NOT more.** High-carbon steel is harder and stronger, but harder to weld without cracking. The burst-rich spark pattern means preheat.
- **Aluminum does not glow red before melting.** Students expect steel behaviour. Aluminum melts suddenly and silently — this is why overheating aluminum is easy and dangerous. Watch for this in questions about aluminum welding hazards.
- **Austenitic stainless (304, 316) is NON-MAGNETIC.** Ferritic and martensitic stainless are magnetic. This is a critical distinction for identification and for welding procedures.
- **Carbon Equivalent formula — if given on exam** — remember Mn/6 not Mn/4, and Ni+Cu combined in the denominator 15, not separately.

---

## Practice question preview

**Q:** A welder receives unmarked steel stock for a repair job. The spark test shows very short, dense streams with many bright white star-shaped bursts close to the grinding wheel. What does this indicate about the steel?

A) The steel is low-carbon (approximately 0.15% C) — no preheat needed
B) The steel is medium-carbon (approximately 0.40% C) — light preheat
C) The steel is high-carbon (approximately 0.80% C or more) — preheat and post-weld controlled cooling required
D) The steel is an austenitic stainless — non-magnetic and non-hardenable

**Correct: C**

**Explanation:** Dense, short spark streams with many star-shaped (exploding) bursts near the grinding wheel indicate high carbon content. High-carbon steels (above 0.60% C) have low weldability — they are very susceptible to hydrogen-induced cracking (HIC) in the HAZ. Preheat (often 200–300°C or higher depending on carbon equivalent) and controlled interpass and post-weld cooling are required. (A) Low carbon = long, straight streams with few bursts. (B) Medium carbon = moderate stream length, moderate bursting. (D) Stainless 304 shows long orange streams without carbon bursts — and a magnet test would show non-magnetic, which should be done first.

**Red Seal mapping:** A-4.04 (Organizes materials); B-8.01 (Prepares materials)

---

[^1]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 19 — Properties of Metals; density table, melting points, thermal expansion values, physical vs mechanical property definitions, identification tests
[^2]: [Lincoln Electric — Metals and Their Weldability, Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); AISI/SAE numbering system, spark test guide, carbon content ranges, identification of ferrous metals
[^3]: [TWI Global — Mechanical Properties and Testing](https://www.twi-global.com/technical-knowledge/faqs); tensile/yield/elongation/impact toughness definitions and test methods
[^4]: [CWB Group — Welder Certification Study Guide](https://www.cwbgroup.org/education/learning-resources); carbon equivalent formula, preheat requirements by CE level, weldability classification
[^5]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic D](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 29–30
