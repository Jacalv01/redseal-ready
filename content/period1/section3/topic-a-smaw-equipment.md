---
id: p1-s3-a
period: 1
section: 3
section_title: Shielded Metal Arc Welding (SMAW)
topic_letter: A
topic_title: SMAW Equipment
hours: 8
weight_pct: 3
outcome: >
  Upon successful completion, learners will be able to identify SMAW equipment and
  power sources and explain key concepts.
objectives:
  - Define SMAW related terms.
  - Identify welding cables and accessories for welding power sources.
  - Identify the effect of arc length on amperage and voltage.
  - Describe AC and AC-DC rectified power sources.
  - Describe AC and DC generator power sources.
  - Describe multi-process inverter power sources.
red_seal_mapping:
  - D-13.01 (Selects SMAW equipment and consumables)
  - D-13.02 (Sets up SMAW equipment)
  - D-13.03 (Sets operating parameters for SMAW equipment)
citations:
  - source: Miller Electric — Stick (SMAW) Welding Guide (public)
    ref: Power source types (transformer, rectifier, inverter), OCV, duty cycle, DCEP/DCEN/AC polarity
    url: https://www.millerwelds.com/resources/article-library/stick-smaw-welding-guide
  - source: Lincoln Electric — Procedure Handbook of Arc Welding (public)
    ref: Section 3 (SMAW process, power sources, OCV, arc characteristics, equipment setup)
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 10 (SMAW Equipment — power sources, cables, electrode holders, ground clamps)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 3 Topic A
    ref: pp. 95–108 (SMAW equipment and power sources)
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
  - source: CSA W117.2 — Safety in Welding, Cutting and Allied Processes (2019)
    ref: Clause 8 (electrical safety — OCV limits, grounding, electrode holder requirements)
    url: https://www.csagroup.org/store/product/CSA%20W117.2%3A19/
---

# SMAW Equipment

Shielded Metal Arc Welding is the oldest continuously-used arc welding process. It's also the most versatile — you can SMAW in the field with a generator, underwater with specialized equipment, in all positions, and on materials that other processes struggle with. Understanding the power source is what separates a welder who "knows how to strike an arc" from a welder who can diagnose a bad weld and fix the setup.

---

## What SMAW is — process overview

SMAW (Shielded Metal Arc Welding), called "stick welding" on the job, uses a consumable coated electrode (the "stick") clamped in an electrode holder.[^1] [^2]

The arc is struck between the electrode tip and the base metal. The arc generates heat (~6,500°C at the arc core) that melts both the electrode and the base metal, forming the weld pool. As the electrode melts, the coating burns and decomposes, producing:[^2]

1. **Shielding gases** — CO₂, CO, and other gases that displace atmospheric oxygen and nitrogen from the arc zone
2. **Slag** — a molten flux layer that floats over the weld pool, shields it from atmosphere, and controls cooling rate

The slag must be completely chipped and wire-brushed from each pass before depositing the next pass.

---

## SMAW equipment components

| Component | Function |
|---|---|
| **Power source** | Converts utility power (or generates DC/AC) to the correct voltage and amperage for welding |
| **Electrode holder (stinger)** | Insulated clamp that holds the electrode and conducts welding current to it |
| **Work clamp (ground clamp)** | Connects the work lead to the base metal or welding table to complete the circuit |
| **Welding cables (leads)** | Heavy copper or aluminum conductors that carry current between power source and work |
| **Electrode** | The consumable stick — base metal + coating — that forms the arc and deposits weld metal |

---

## Power source types — the three designs

### 1. Transformer (AC output only)

The simplest and oldest design. Steps down the utility supply voltage (230 V or 480 V) to welding voltage (typically 17–40 V arc voltage), while stepping up the current.[^1] [^3]

**Output:** AC (alternating current) only.

**Advantages:**
- Simple, durable, low maintenance
- Lower initial cost
- Works well with AC-compatible electrodes (E6011, E6013)

**Disadvantages:**
- AC only — limits electrode selection (can't run E6010 well; E7018 runs poorly on AC at lower amperages)
- Arc tends to be less stable than DC
- Heavier than inverter designs

**Typical shop use:** light fabrication, training environments, general maintenance welding.

---

### 2. Rectifier (AC-DC) — transformer-rectifier

An AC transformer with a **rectifier** (diode bank) added to convert AC to DC.[^1] [^3]

**Output:** AC or DC, selectable. When producing DC, the diode bank converts the AC sine wave to pulsating DC (which is then smoothed by capacitors/inductors into more stable DC).

**Advantages:**
- Selectable AC or DC — compatible with all SMAW electrode types
- DC arc is more stable than AC arc
- Good for E7018, E6010, E6013, all major electrodes

**Disadvantages:**
- Heavier and more complex than a pure transformer
- Less portable than an inverter

**Typical shop use:** general SMAW in a fixed shop or construction site with utility power.

---

### 3. Inverter (multi-process)

The modern design. Uses high-frequency electronic switching (typically 20,000–100,000 Hz switching frequency) to transform power far more efficiently than a traditional transformer, which operates at line frequency (60 Hz in North America).[^1] [^3]

**Why inverters are smaller and lighter:** at higher frequency, the transformer core can be much smaller. An inverter machine at 300 A can weigh as little as 10–15 kg vs. 150+ kg for an equivalent transformer-rectifier.

**Output:** DC (DCEP or DCEN), or AC, depending on the machine model.

**Advantages:**
- Extremely portable
- High efficiency (>85% vs. 40–60% for transformers)
- Arc starting is superior — especially for E6010 and E7018
- Precise output control — amperage adjustable in fine increments
- Multi-process capability (SMAW + GMAW + GTAW on one machine)
- Better arc stability under varying arc length

**Disadvantages:**
- More expensive to repair (electronic components vs. simple transformer)
- Sensitive to voltage fluctuations and poor extension cord sizing
- Not all inverters handle all electrode types equally — verify the machine spec

**Typical shop use:** field work, maintenance, any application requiring portability or multi-process capability.

---

### 4. Generator and engine-driven welder

A gasoline, diesel, or propane engine turns an alternator or generator to produce welding current. Used wherever utility power is not available.[^1]

**Output:** AC (older generator designs) or DC (modern inverter-generators and alternator designs).

**Advantages:**
- Fully portable — works anywhere
- Also provides auxiliary AC power for tools and lights
- Diesel units are common on pipeline and heavy construction

**Disadvantages:**
- Noise, exhaust, fuel logistics
- Engine maintenance requirements (oil, fuel, air filters)
- Not suitable for indoor use without ventilation (CO exhaust)

**Important:** When running an engine-driven welder on a job site, ensure exhaust is vented away from the work area and any enclosed spaces. Carbon monoxide from engine exhaust is a serious hazard.[^5]

---

## Polarity — DCEP, DCEN, and AC

**Polarity** determines the direction of current flow in a DC welding circuit, which affects heat distribution and penetration characteristics.[^1] [^2]

### DC terminology

**Conventional current** flows from (+) to (−). In a DC welding circuit:

| Polarity | Electrode connection | Work connection | Also called |
|---|---|---|---|
| **DCEP** | Positive (+) | Negative (−) | DC Electrode Positive; Reverse Polarity (RP) |
| **DCEN** | Negative (−) | Positive (+) | DC Electrode Negative; Straight Polarity (SP) |

**Heat distribution rule:** approximately **2/3 of the arc heat goes to the (+) terminal.** This is a fundamental arc physics fact.[^2]

**DCEP (electrode positive):**
- 2/3 of heat at the electrode → deeper penetration into the base metal
- Electrode melts faster → higher deposition rate in some cases
- Most SMAW electrodes are designed for DCEP: E7018, E6010, E6012

**DCEN (electrode negative):**
- 2/3 of heat at the work → shallower penetration
- Electrode melts more slowly → used for thin material or certain processes where lower penetration is needed
- Some electrodes specify DCEN: E6012 can run DCEN; some hardfacing electrodes

### AC (alternating current)

Current direction alternates at line frequency (60 Hz = reverses 120 times per second). Heat distributes roughly equally between electrode and work (averaging out over the cycle).[^1]

**AC advantages:**
- No arc blow (magnetic arc deflection) — a major problem on large DC welds
- Good for electrodes with self-ionizing coatings (E6011, E6013)

**AC disadvantages:**
- The arc extinguishes and re-ignites 120 times per second — less stable than DC
- Low-hydrogen electrodes (E7018) are harder to maintain with AC at lower amperages
- Not compatible with E6010 (requires DC+ for proper arc ionization)

---

## Open Circuit Voltage (OCV)

**OCV** is the voltage measured at the welding terminals when **no arc is established** (no current flowing).[^1] [^3]

| Machine type | Typical OCV range |
|---|---|
| AC transformer | 50–80 V |
| DC rectifier | 60–90 V |
| Engine-driven DC | 60–90 V |
| Inverter DC | 60–100 V |

**Why OCV matters:**
- OCV must be high enough to initiate and maintain the arc. AC requires higher OCV than DC because the arc re-ignites every half-cycle.
- CSA W117.2 sets a maximum OCV for safety: **80 V (AC) and 100 V (DC)** in general work environments. Exceeding these values increases the electric shock risk to the welder.[^5]
- When the arc is established, voltage drops to **arc voltage** (typically 17–28 V for SMAW) and current rises to the set welding amperage.

---

## Arc length and its effect on voltage and amperage

The relationship between arc length, voltage, and amperage is governed by the **volt-ampere characteristic** (V-A curve) of the power source.[^1] [^2]

For a constant-current (CC) power source (which SMAW uses):

| Change | Effect on voltage | Effect on amperage |
|---|---|---|
| Increase arc length | Voltage increases | Amperage decreases slightly |
| Decrease arc length | Voltage decreases | Amperage increases slightly |
| Very short arc (drag) | Very low voltage | Current spike → can cause electrode to stick |
| Very long arc | High voltage | Low amperage → poor fusion, excessive spatter |

**Practical meaning:** A CC power source is "self-regulating" in current — it tries to maintain the set amperage even if the arc length changes. This is why SMAW is forgiving of slight arc length variation. However, excessive arc length still causes problems (spatter, porosity, poor penetration) even if the current is held approximately constant.[^2]

**Ideal SMAW arc length:** approximately equal to the electrode diameter (e.g., 1/8 in arc length for a 1/8 in electrode).[^1]

---

## Duty cycle — how long you can weld

**Duty cycle** is the percentage of a 10-minute period that a machine can weld at its rated amperage without overheating.[^1] [^3]

**Standard rating:** Most SMAW machines are rated at **60% duty cycle** at their rated amperage.

**Example — 60% duty cycle calculation:**
- At 300 A: weld for 6 minutes, rest 4 minutes, repeat
- At 200 A: duty cycle improves — the machine can weld longer before overheating
- At 400 A (if the machine is only rated 300 A): pushing over the rating overheats the machine

**Duty cycle formula:**
(I₁)² × D₁ = (I₂)² × D₂

Where I = amperage, D = duty cycle as a decimal.

**Example:** A 300 A machine at 60% duty cycle. Duty cycle at 250 A?

(300)² × 0.60 = (250)² × D₂
90,000 × 0.60 = 62,500 × D₂
54,000 = 62,500 × D₂
D₂ = 0.864 = **86.4% duty cycle at 250 A**[^3]

---

## Welding cables — sizing and connections

Welding cables carry the full welding current. Undersized cables create voltage drop, overheating, and arc instability.[^1] [^2]

**Cable sizing guidelines (check manufacturer tables — this is general guidance):**[^2]

| Welding current | Cable length (approx.) | Minimum cable size |
|---|---|---|
| Up to 200 A | Up to 50 ft | 2 AWG |
| 200–300 A | Up to 50 ft | 1/0 AWG |
| 300–400 A | Up to 50 ft | 2/0 AWG |
| 300–400 A | 50–100 ft | 3/0 AWG |

**Note:** Always check the machine manufacturer's cable sizing table and local electrical code requirements. Longer cables = more resistance = need for larger cable. The work lead must also be sized the same as the electrode lead — it carries the same current.

**Work clamp placement:**
- Clamp as close to the weld as practical to minimize voltage drop in the work circuit
- Never use the workpiece as the only conductor for several metres — the resistance adds up and arc characteristics suffer
- Clamping to a painted or corroded surface increases contact resistance — use a clean metal connection point

---

## Diagram

*(SVG to be added: `assets/diagrams/p1-s3-a-smaw-equipment.svg` — labelled diagram of a complete SMAW setup showing: power source, electrode cable, electrode holder, electrode, work cable, work clamp, workpiece, with current path arrows; separate panel showing DCEP vs DCEN polarity with heat distribution (2/3 at + terminal marked); voltage characteristic curve showing OCV, arc voltage, short-circuit current)*

---

## Numbers you need to memorize

- **OCV maximum (AC): 80 V per CSA W117.2**[^5]
- **OCV maximum (DC): 100 V per CSA W117.2**[^5]
- **SMAW arc voltage (typical): 17–28 V**[^1]
- **Standard duty cycle for SMAW machines: 60% at rated amperage** (10-minute cycle basis)[^1] [^3]
- **Heat distribution in DC arc: 2/3 at the positive (+) terminal**[^2]
- **DCEP (electrode positive) = deeper penetration** into base metal[^2]
- **DCEN (electrode negative) = shallower penetration**, higher deposition rate in some cases[^2]
- **Ideal arc length ≈ electrode diameter** (e.g., 1/8 in arc for 1/8 in electrode)[^1]
- **Inverter switching frequency: ~20,000–100,000 Hz** (vs. 60 Hz for transformer)[^3]
- **AC arc re-ignition: 120 times per second at 60 Hz line frequency**[^1]

---

## What the textbook doesn't tell you

**Arc blow is real and it will ruin your weld if you don't know what it is.** On DC, magnetic fields from the welding current can deflect the arc backward or forward — making it impossible to direct the arc into the joint. This is called arc blow. It's most severe near the ends of a joint or near the work clamp. The fix: switch to AC (eliminates arc blow), reposition the work clamp, change electrode angle to compensate, or use shorter arc length. E6011 (AC-rated) is specifically chosen for jobs where arc blow on DC is a persistent problem.[^2]

**The work clamp is called a "ground" clamp but it's NOT an electrical earth ground.** In welding, "ground" means the return path of the welding circuit — not a connection to earth. Electricians use "ground" to mean earth ground. Don't confuse these. The work clamp completes the welding circuit. A separate earth ground is a safety ground on the machine chassis. Both are needed, but they are different things.[^5]

**Inverters require proper extension cords.** Running a 200 A inverter welder through a standard 14-gauge extension cord will starve the machine of voltage, cause the inverter's protection circuits to trip, and result in an unstable or non-functional arc. Use proper welding leads on the output side and sized supply cables on the input side. Check the machine's input amperage requirement (not the output rating) when sizing the supply circuit.[^3]

---

## Key terms

- **SMAW:** Shielded Metal Arc Welding — arc welding with a consumable coated electrode
- **OCV (Open Circuit Voltage):** voltage at the welding terminals with no arc established
- **Arc voltage:** voltage across the arc when welding (typically 17–28 V for SMAW)
- **CC (Constant Current):** power source characteristic — maintains approximately constant amperage despite arc length variation. SMAW uses CC machines.
- **DCEP (DC Electrode Positive):** electrode connected to positive terminal; 2/3 heat at electrode side → deeper base metal penetration
- **DCEN (DC Electrode Negative):** electrode connected to negative terminal; 2/3 heat at work
- **AC (Alternating Current):** current reverses direction 120 times/second (at 60 Hz) — used for arc blow-prone situations and with self-ionizing electrode coatings
- **Duty cycle:** percentage of a 10-minute period the machine can weld at rated amperage without overheating
- **Transformer:** simple power source, AC output only — steps down voltage, steps up current
- **Rectifier:** transformer + diode bank = selectable AC or DC output
- **Inverter:** high-frequency electronic switching power source — lightweight, efficient, superior arc control
- **Arc blow:** deflection of the welding arc by magnetic fields — occurs on DC; corrected by switching to AC or repositioning work clamp
- **Work clamp:** the return path conductor — connects the workpiece to the power source return terminal (not an earth ground)

---

## Common exam trap

- **"DCEP means the work is positive"** — false. DCEP = DC Electrode Positive. The electrode is positive, the work is negative.
- **"Higher OCV = more welding amperage"** — false. OCV is the open-circuit (no arc) voltage. Once the arc is established, the voltage drops to arc voltage (17–28 V) and the current rises to the set amperage. OCV doesn't directly determine welding amperage.
- **"Increasing arc length increases amperage"** — false. On a CC machine, increasing arc length increases voltage and slightly decreases amperage.
- **"AC transformers are safer because OCV is lower than DC machines"** — partially true (AC OCV is typically lower) but AC OCV is still lethal. All welding voltages above 50 V are potentially fatal — this is not a "safe" voltage. CSA W117.2 requires proper PPE and electrical safety regardless of process.
- **"Duty cycle is based on an 8-hour workday"** — false. Duty cycle is based on a 10-minute cycle, not an 8-hour day.

---

## Practice question preview

**Q:** A SMAW power source is set up with the electrode holder connected to the positive terminal and the work clamp connected to the negative terminal. Which polarity is this, and what is the primary effect on the weld?

A) DCEN — the electrode receives 2/3 of the arc heat, producing shallow penetration  
B) DCEP — the work receives 2/3 of the arc heat, producing deep penetration into the base metal  
C) DCEP — the electrode receives 2/3 of the arc heat, producing deep penetration into the base metal  
D) DCEN — the work receives 2/3 of the arc heat, producing deep penetration  

**Correct: C**

**Explanation:** Electrode connected to the positive (+) terminal = DCEP (DC Electrode Positive). With 2/3 of arc heat concentrated at the positive terminal (which is the electrode), this does NOT mean the base metal gets deeper penetration from direct heat — rather, the hotter electrode side drives more ionization, and the arc digs deeper into the base metal due to the plasma force and arc dynamics. DCEP produces deeper penetration and is the standard polarity for most SMAW electrodes (E7018, E6010). Option B incorrectly says the work receives 2/3 heat — that would be DCEN. Option A describes DCEN but incorrectly labels it DCEP. Option D is backwards on both polarity and heat distribution.

**Red Seal mapping:** D-13.01 (Selects SMAW equipment and consumables — identifies power source type, polarity requirements, and arc characteristics)

---

[^1]: [Miller Electric — Stick (SMAW) Welding Guide](https://www.millerwelds.com/resources/article-library/stick-smaw-welding-guide), power source types (transformer, rectifier, inverter, engine-driven), OCV, arc voltage, duty cycle, arc length effects on voltage and current, polarity selection
[^2]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook), Section 3 "The SMAW Process": heat distribution (2/3 at positive terminal), DCEP vs DCEN effects on penetration and deposition, arc blow causes and correction, ideal arc length = electrode diameter, CC volt-ampere characteristic
[^3]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 10 "SMAW Equipment": transformer design and operation, transformer-rectifier design, inverter technology and high-frequency switching, duty cycle calculation formula (I₁²×D₁ = I₂²×D₂), cable sizing guidelines
[^4]: [AIT Welder Curriculum Guide 012 (2026)](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), Period 1 Section 3 Topic A: SMAW equipment and power sources, welding cables and accessories, OCV, polarity, duty cycle
[^5]: [CSA W117.2 — Safety in Welding, Cutting and Allied Processes (2019)](https://www.csagroup.org/store/product/CSA%20W117.2%3A19/), Clause 8 "Electrical Safety": OCV maximum limits (80 V AC, 100 V DC), grounding requirements, electrode holder specifications, electrical shock prevention, work clamp vs. earth ground distinction
