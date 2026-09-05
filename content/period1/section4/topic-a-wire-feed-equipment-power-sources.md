---
id: p1-s4-a
period: 1
section: 4
section_title: Gas Metal Arc Welding (GMAW), Flux-Cored Arc Welding (FCAW), Metal-Cored Arc Welding (MCAW) and Submerged Arc Welding (SAW)
topic_letter: A
topic_title: Wire Feed Welding Equipment Power Sources
hours: 6
weight_pct: 3
outcome: >
  Upon successful completion, learners will be able to identify and describe wire feed
  welding equipment.
objectives:
  - Describe the principles of operation of wire feed welding equipment.
  - Identify the components of a wire feed welding equipment set-up.
  - Describe wire feed welding equipment power sources and wire feeders.
  - Identify advantages and disadvantages of wire feed processes.
red_seal_mapping:
  - D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables)
  - D-14.02 (Sets up FCAW, MCAW and GMAW equipment)
  - D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW)
citations:
  - source: Miller Electric — GMAW/MIG Welding Guide (public)
    ref: Wire feed equipment components, CV power source characteristics, transfer modes, drive roll types
    url: https://www.millerwelds.com/resources/article-library/mig-gmaw-welding-guide
  - source: Lincoln Electric — GMAW (MIG/MAG Welding) Process Guide (public)
    ref: CV vs CC power sources, wire feeder design, gun assembly, metal transfer modes with voltage/amperage ranges
    url: https://www.lincolnelectric.com/en/education-center/welding-processes/gmaw
  - source: ESAB — Handbook of Arc Welding (public)
    ref: Chapter on GMAW/FCAW equipment — CV output characteristics, transfer mode selection, feeder mechanics
    url: https://www.esab.com/en/us/education/blog/the-esab-handbook
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 14 (GMAW Equipment — power sources, wire feeders, guns, torch anatomy, drive rolls)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 4 Topic A
    ref: pp. 151–165 (wire feed welding equipment)
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Wire Feed Welding Equipment Power Sources

Wire feed processes — GMAW (MIG), FCAW (flux-core), MCAW (metal-core), and SAW (submerged arc) — now account for the majority of weld metal deposited in industrial fabrication worldwide. Understanding why requires understanding what makes these power sources fundamentally different from SMAW: instead of a constant-current machine with a consumable stick, you have a constant-voltage machine with a continuously fed wire. This lesson covers how that system works and why each component matters.

---

## The fundamental difference: CC vs. CV

**SMAW uses a Constant Current (CC) power source.**
The machine tries to maintain a set amperage regardless of arc length changes. The welder controls arc length manually with every hand movement.[^1] [^2]

**Wire feed processes use a Constant Voltage (CV) power source.**
The machine tries to maintain a set voltage regardless of current changes. The wire feed speed (WFS) is set independently. This creates a self-regulating arc.[^1] [^2]

### How the CV self-regulating arc works

This is the most important concept in wire feed welding:

1. You set voltage (V) on the power source and wire feed speed (WFS) on the wire feeder.
2. WFS drives the wire toward the work at a fixed rate.
3. If the wire gets too close to the work (arc shortens):
   - Voltage drops (CV machine senses the short)
   - Current SPIKES instantly — this melts off the wire faster
   - Arc returns to the set length
4. If the wire gets too far from the work (arc lengthens):
   - Voltage rises
   - Current drops
   - Wire doesn't melt off as fast — arc returns to set length

**Result:** The system is self-correcting. If the gun-to-work distance changes slightly (as it does with every hand movement), the arc stabilizes itself. This is why wire feed processes are much more operator-forgiving than SMAW in terms of arc length control.[^1] [^2]

**Key equation (approximate):** In GMAW, the wire burn-off rate equals the wire feed speed. If WFS = 200 in/min and burn-off rate = 200 in/min, the arc length stays constant.[^1]

---

## Complete wire feed welding setup — all components

| Component | Function |
|---|---|
| **Power source (CV machine)** | Converts utility power to constant-voltage DC welding output |
| **Wire feeder** | Motor-driven mechanism that feeds the electrode wire from the spool at set WFS |
| **Welding gun** | The torch held by the welder — guides the wire, carries current, delivers shielding gas |
| **Contact tip** | Copper tip inside the gun nozzle that transfers welding current to the wire |
| **Gas nozzle** | The cup at the end of the gun that directs shielding gas to the weld zone |
| **Shielding gas supply** | Cylinder + regulator + flowmeter + hoses delivering the correct gas at the correct flow rate |
| **Electrode wire spool** | The wire filler metal supply — 2 lb, 10 lb, 33 lb, or bulk drum formats |
| **Work lead (ground cable)** | Return path from the workpiece to the power source negative terminal |
| **Drive rolls** | The rollers inside the wire feeder that push the wire through the liner and gun cable |
| **Welding cable (gun lead)** | The assembly connecting the power source and feeder to the gun — carries current, wire, gas, and often control signals |

---

## Power source types for wire feed welding

### Transformer-rectifier CV

A transformer steps down line voltage; a diode rectifier converts AC to DC. Older design but still common in heavy industrial settings.[^1]

**Output:** DC (typically DCEP for most wire-feed applications)

**Advantages:** durable, simple, relatively easy to repair

**Disadvantages:** heavy, not portable, response time is slower than inverter designs

### Inverter CV

High-frequency electronic switching produces DC output with superior arc response.[^1] [^3]

**Output:** DC (DCEP standard for most wire-feed applications)

**Advantages:** lightweight, efficient, superior arc response (faster reaction to arc length changes = better self-regulation), multi-process capability

**Disadvantages:** more expensive to repair, sensitive to power quality

### Pulsed CV / Pulse GMAW power source

A more sophisticated inverter that alternates between high-current pulses and a lower background current.[^1] [^3]

**Pulse mechanism:**
- During the high-current pulse: one droplet of metal is pinched off and transferred to the weld pool
- During the background current: the arc is maintained but no transfer occurs
- Pulse frequency: typically 1–400 Hz depending on wire diameter and type

**Why pulse matters:** Enables spray transfer characteristics (deep penetration, minimal spatter) at lower average amperages — allowing out-of-position welding that would be impossible with true spray transfer. Standard spray transfer requires flat/horizontal only.[^3]

---

## Metal transfer modes — the most important concept in GMAW

The way electrode wire melts off and transfers to the weld pool determines the arc characteristics, usable positions, penetration profile, spatter level, and shielding gas requirements.[^1] [^2] [^3]

### 1. Short-circuit transfer (short-arc)

**How it works:**
The wire actually touches the weld pool and short-circuits (momentarily, up to 200 times per second). The short causes a current spike that heats the wire and "pinches" it off — the droplet transfers into the pool. Then the arc re-establishes, the cycle repeats.

| Parameter | Typical range |
|---|---|
| **Voltage** | 15–22 V |
| **Wire feed speed / amperage** | Low — typically 75–175 A for 0.035–0.045" wire[^1] |
| **Shielding gas** | 75/25 Ar/CO₂ or 100% CO₂ |
| **Positions** | All positions — including vertical and overhead |
| **Penetration** | Shallow |
| **Spatter** | Moderate to high (especially with 100% CO₂) |
| **Applications** | Thin sheet metal, root passes, out-of-position work |

**Limitation:** The repeated short-circuit creates a "cold" weld zone. If used on thicker material that requires more heat, the result is cold lapping (poor fusion) and porosity.[^1]

---

### 2. Globular transfer

**How it works:**
Voltage is increased above short-circuit range. The wire melts and forms a large irregular droplet (larger than the wire diameter) that falls into the pool under gravity. Erratic, uncontrolled.

| Parameter | Typical range |
|---|---|
| **Voltage** | 22–26 V |
| **Amperage** | 175–200 A (wire-dependent) |
| **Shielding gas** | CO₂ (100%) common for globular |
| **Positions** | Flat and horizontal only — globular cannot be used out of position reliably |
| **Spatter** | VERY HIGH — globular produces the most spatter of all transfer modes |
| **Applications** | Rarely deliberately used — it's the transition zone between short-circuit and spray |

**Practical note:** On the job, you encounter globular when parameters are in the transitional range — typically when running 100% CO₂ with settings that aren't quite at spray. The solution is to either reduce to short-circuit range or increase to spray range. Most welders avoid intentional globular.[^2]

---

### 3. Spray transfer

**How it works:**
Voltage is high enough that the wire melts and transfers as a stream of fine, directed droplets — no shorting, no globules. The droplets are propelled across the arc gap by electromagnetic force. The arc is very stable and quiet.

| Parameter | Typical range |
|---|---|
| **Voltage** | 26–34 V |
| **Amperage** | 175–300+ A (wire and diameter dependent)[^1] |
| **Shielding gas** | Minimum ~80% Argon required for spray — 90/10 or 95/5 Ar/CO₂ |
| **Positions** | Flat and horizontal ONLY — the high heat and fluid pool make spray unsuitable for vertical or overhead without pulse modification |
| **Penetration** | Deep — excellent fusion into the base metal |
| **Spatter** | Very low |
| **Applications** | High-deposition flat/horizontal GMAW on medium and heavy plate |

**Spray transition current:** There is a minimum current level below which spray transfer will NOT occur, even with the correct gas. This threshold current depends on the wire type and diameter — for 0.045" ER70S-6 with 90/10 Ar/CO₂, the spray transition is approximately 230 A.[^1] Running below this current with spray-type gas produces globular, not spray.

---

### 4. Pulsed spray transfer

**How it works:**
The power source alternates between a high peak current (which creates spray transfer — one droplet per pulse) and a lower background current (which maintains the arc without transfer). The average current is below the spray transition threshold, so the heat input is manageable for out-of-position work.

| Parameter | Typical range |
|---|---|
| **Average voltage** | 24–32 V |
| **Average amperage** | 100–250 A |
| **Shielding gas** | 90/10 Ar/CO₂ or similar high-Argon mix |
| **Positions** | All positions — the key advantage over conventional spray |
| **Penetration** | Good — better than short-circuit |
| **Spatter** | Very low |
| **Applications** | Out-of-position GMAW on stainless, aluminum, high-strength steel — anywhere you need spray quality with positional capability |

---

### Transfer mode comparison table

| Mode | Voltage | Amperage | Positions | Spatter | Penetration |
|---|---|---|---|---|---|
| Short-circuit | 15–22 V | Low (75–175 A) | All | Moderate | Shallow |
| Globular | 22–26 V | Medium-low | Flat/horiz only | Very high | Medium |
| Spray | 26–34 V | High (175–300+ A) | Flat/horiz only | Very low | Deep |
| Pulsed spray | 24–32 V avg | Medium (100–250 A) | All | Very low | Good |

---

## Wire feeder — types and design

The wire feeder is the mechanism that pulls wire from the spool and pushes it through the gun cable to the contact tip at a precise, controlled speed.[^1] [^4]

### Feeder types

**Push type (most common):**
The drive rolls push the wire from the feeder through the gun cable (liner) to the gun tip. Works well for most applications. Limitation: difficult to push wire through cable lengths >5 m or through severe bends without feeding problems.

**Pull type (spool gun):**
The wire spool is located AT the gun itself. The feeder motor pulls the wire from a small spool at the gun. Used for soft wires (aluminum) that are difficult to push through long cables. Spool guns are typically limited to 4" spools.

**Push-pull type:**
A push motor at the feeder and a smaller pull motor at the gun work together. Used for longer cable runs with difficult wires (aluminum). The most reliable for long-gun cable applications.

---

## Diagram

*(SVG to be added: `assets/diagrams/p1-s4-a-wire-feed-setup.svg` — fully labeled wire feed welding system showing: CV power source → work lead → workpiece; and separately: power source → feeder (showing drive rolls, wire spool, tension adjustment) → gun cable → welding gun (showing contact tip, gas nozzle, trigger) → arc zone; plus a separate panel showing the 4 metal transfer modes in cross-section diagrams)*

---

## Advantages and disadvantages of wire feed processes

### Advantages (vs. SMAW)

| Advantage | Explanation |
|---|---|
| **Higher deposition rate** | Continuous wire feed = more weld metal per hour than stick (no electrode stub, no stop-and-start for new electrodes) |
| **Higher deposition efficiency** | GMAW solid wire: 90–98%; SMAW E7018: ~65% — wire processes waste far less consumable as slag/stub |
| **No slag removal (GMAW/pulse)** | Solid wire GMAW produces minimal slag — some flux-type inclusions but not a full slag blanket requiring chipping |
| **Longer continuous welds** | No electrode changes mid-bead — welds can run for metres without stopping |
| **Less skill required for arc length** | CV self-regulation reduces the critical dependency on steady hand for arc length (vs. SMAW) |
| **Better for automation** | Wire feed processes are the basis of robotic welding |

### Disadvantages (vs. SMAW)

| Disadvantage | Explanation |
|---|---|
| **Equipment complexity** | More components to set up and maintain (feeder, gas supply, gun, contact tips) |
| **Shielding gas required (GMAW/MCAW)** | Cannot weld in wind without a windscreen — shielding gas is disrupted by drafts above ~5–8 km/h |
| **Less portable** | The gas cylinder, feeder, and power source are a larger setup than a stick welder and a box of electrodes |
| **Contact tip wear** | Contact tips wear out and must be replaced — tip-to-work distance and spatter build-up inside the nozzle require regular maintenance |
| **Wire feed problems** | Bird-nesting, wire tangling, drive roll slip — more troubleshooting scenarios than SMAW |
| **Wind sensitivity** | Self-shielded FCAW is more wind-tolerant, but gas-shielded GMAW/FCAW cannot be used in exposed outdoor work without wind protection |

---

## Numbers you need to memorize

- **CV power source:** constant voltage — used for all wire feed processes (GMAW, FCAW, MCAW, SAW)[^1]
- **CC power source:** constant current — used for SMAW and GTAW[^1]
- **Short-circuit transfer voltage: 15–22 V**[^1]
- **Spray transfer voltage: 26–34 V**[^1]
- **Spray transfer requires minimum ~80% Argon** in shielding gas[^1]
- **Short-circuit: all positions; Spray: flat and horizontal only**[^1]
- **Pulsed spray: all positions with spray-quality characteristics**[^3]
- **GMAW deposition efficiency: 90–98%** (solid wire)[^2]
- **SMAW E7018 deposition efficiency: ~65%**[^2]

---

## What the textbook doesn't tell you

**Wire feed speed controls amperage on a CV machine — not the amperage knob.** On a typical MIG machine, the "voltage" control sets the voltage and the "wire feed speed" control sets the amperage. Turn up the WFS and amperage goes up; turn it down and amperage goes down. This confuses people who come from SMAW where you directly set the amperage. Some machines label one control "voltage" and the other "amperage" — but what that "amperage" control is actually doing is changing the wire feed speed.[^1]

**Short-circuit on thick plate is the #1 cause of hidden cold fusion.** A rookie GMAW welder runs short-circuit parameters on 1/2" plate because the settings are "easier to control." The bead looks fine visually but X-ray shows cold fusion at the sidewalls — the short-circuit mode didn't have enough heat input to fuse the groove faces. Know the mode limits: short-circuit for thin and root passes, spray for heavy plate.[^1]

**The ESAB and Lincoln "synergic" controls simplify setup but don't replace understanding.** Modern synergic wire feeders let you select wire type and diameter, and the machine sets voltage and WFS automatically for a given current. This is helpful for production. But if you don't understand WHY those parameters are set as they are, you can't troubleshoot when the arc isn't right. Know the fundamentals first.[^3]

---

## Key terms

- **CV (Constant Voltage):** power source characteristic — maintains set voltage as current changes; used for wire feed processes
- **CC (Constant Current):** power source characteristic — maintains set amperage as voltage changes; used for SMAW/GTAW
- **Wire feed speed (WFS):** the rate at which electrode wire is fed from the spool to the arc; controls amperage on a CV machine
- **Self-regulating arc:** the automatic feedback mechanism of a CV machine — arc length changes cause current changes that restore the arc to its set state
- **Short-circuit transfer:** wire contacts the pool and short-circuits; current spike melts the wire off; occurs repeatedly (up to 200×/sec); all positions
- **Globular transfer:** large irregular droplets fall into the pool; high spatter; transitional mode; avoid in practice
- **Spray transfer:** fine directed droplets sprayed across the arc; very low spatter; deep penetration; flat/horizontal only
- **Pulsed spray transfer:** controlled pulses of spray transfer at reduced average heat input; all positions
- **Drive rolls:** the rollers in the wire feeder that propel the electrode wire toward the gun
- **Contact tip:** the copper replaceable tip inside the gun nozzle that transfers current to the electrode wire
- **CTWD (Contact Tip to Work Distance):** the distance from the end of the contact tip to the work surface — critical variable controlling amperage

---

## Common exam trap

- **"CV and CC machines are interchangeable for GMAW"** — false. CV is required for GMAW. Using a CC machine with wire feed produces an unstable, uncontrollable arc because there is no self-regulation mechanism.
- **"Increasing voltage always increases amperage"** — false on a CV machine. Increasing voltage with the same WFS increases the arc length and heat; amperage is primarily controlled by WFS.
- **"Spray transfer can be done in all positions with any gas"** — false. Spray transfer requires flat/horizontal positions and a high-Argon shielding gas (minimum ~80% Ar). Without the position and gas requirements, you cannot achieve spray transfer.
- **"Self-shielded FCAW uses the same gas as GMAW"** — false. Self-shielded FCAW uses NO shielding gas — the flux core generates its own shield. Gas-shielded FCAW does use external gas. They are different processes.

---

## Practice question preview

**Q:** A GMAW wire feed welder is set at 28 V and 250 A (via WFS) using ER70S-6 wire and 90/10 Ar/CO₂ shielding gas. What metal transfer mode is most likely occurring?

A) Short-circuit transfer  
B) Globular transfer  
C) Spray transfer  
D) Pulsed spray transfer  

**Correct: C**

**Explanation:** Spray transfer occurs at higher voltages (typically 26–34 V) and higher amperages, with a shielding gas containing at least 80% Argon. At 28 V and 250 A with 90/10 Ar/CO₂, all three conditions for spray transfer are met: voltage in the spray range (28 V > 26 V), amperage at or above the spray transition current (~230 A for this wire/gas combination), and shielding gas with 90% Ar (above the 80% Ar minimum). Option A (short-circuit) requires 15–22 V. Option B (globular) is the 22–26 V transitional range. Option D (pulsed) requires a pulsed power source — the question doesn't indicate pulsed capability.

**Red Seal mapping:** D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW — selects appropriate transfer mode and understands CV power source operation)

---

[^1]: [Miller Electric — GMAW/MIG Welding Guide](https://www.millerwelds.com/resources/article-library/mig-gmaw-welding-guide), CV vs CC power source characteristics, self-regulating arc explanation, metal transfer mode descriptions with voltage/amperage ranges (short-circuit 15–22 V; spray 26–34 V), spray transition current for 0.045" ER70S-6, all-position capability by transfer mode, wire feeder types (push/pull/push-pull)
[^2]: [Lincoln Electric — GMAW Process Guide](https://www.lincolnelectric.com/en/education-center/welding-processes/gmaw), transfer mode selection guide, globular transition zone, spray Argon minimum (80%), GMAW deposition efficiency (90–98% solid wire), SMAW comparison, wire feed speed controls amperage explanation
[^3]: [ESAB — Handbook of Arc Welding](https://www.esab.com/en/us/education/blog/the-esab-handbook), pulsed spray transfer description (peak current/background current), pulse frequency ranges, synergic control description, inverter power source advantages, multi-process capabilities
[^4]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 14 "GMAW Equipment": complete component diagram, wire feeder drive roll types, contact tip function, gun assembly, advantages/disadvantages of wire feed vs SMAW
