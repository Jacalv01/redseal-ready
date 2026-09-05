---
id: p1-s4-b
period: 1
section: 4
section_title: Gas Metal Arc Welding (GMAW), Flux-Cored Arc Welding (FCAW), Metal-Cored Arc Welding (MCAW) and Submerged Arc Welding (SAW)
topic_letter: B
topic_title: Wire Feed Welding Filler Metals and Feeders
hours: 6
weight_pct: 3
outcome: >
  Upon successful completion, learners will be able to identify and describe wire feed
  consumables and feeder components.
objectives:
  - Identify wire feed welding equipment filler metals.
  - Describe the modes of metal transfer.
  - Describe wire feed drive systems and gun and cable accessories.
  - Describe wire feed operating variables.
red_seal_mapping:
  - D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables)
  - D-14.02 (Sets up FCAW, MCAW and GMAW equipment)
  - D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW)
citations:
  - source: AWS A5.18 — Specification for Carbon Steel Electrodes and Rods for Gas Shielded Arc Welding (2021)
    ref: ER70S-6 classification, ER70S-2, ER70S-3 — composition, tensile properties, wire characteristics
    url: https://www.aws.org/standards/page/aws-a518
  - source: AWS A5.20 — Specification for Carbon Steel Electrodes for Flux Cored Arc Welding (2015)
    ref: E71T-1, E71T-11 classifications — gas-shielded and self-shielded FCAW electrodes
    url: https://www.aws.org/standards/page/aws-a520
  - source: AWS A5.36 — Specification for Carbon and Low-Alloy Steel Flux Cored and Metal Cored Welding Electrodes (2016)
    ref: E70C-6M (MCAW) and updated FCAW classifications
    url: https://www.aws.org/standards/page/aws-a536
  - source: Lincoln Electric — Consumables Catalog (public)
    ref: ER70S-6, E71T-1, E71T-11, E70C-6M data sheets — diameter ranges, applications, drive roll requirements
    url: https://www.lincolnelectric.com/en/products/consumables
  - source: Miller Electric — Wire Welding Process and Product Guide (public)
    ref: Drive roll types (V-groove, U-groove, knurled), GMAW/FCAW/MCAW wire selection, CTWD effects
    url: https://www.millerwelds.com/resources/article-library/mig-gmaw-welding-guide
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 14–15 (wire feed filler metals, feeder drive rolls, gun assembly, operating variables)
    url: https://www.goodheartwillcox.com/products/modern-welding
---

# Wire Feed Welding Filler Metals and Feeders

The wire you put in the machine determines the mechanical properties of the weld, the process you can use, the gas you need, and the drive roll setup. Getting this wrong — using the wrong wire or wrong drive rolls — produces either a bad weld or equipment damage. This lesson covers the classification systems for GMAW, FCAW, and MCAW wires, plus the feeder hardware that makes them work.

---

## Wire classification systems

### GMAW (solid wire) — AWS A5.18

The AWS A5.18 standard classifies solid carbon steel electrodes used for GMAW and GTAW (filler rods). The classification format:[^1]

**Format: ER-XX-S-X**

| Segment | Meaning | Example (ER70S-6) |
|---|---|---|
| **E** | Electrode (usable energized in the arc) | E |
| **R** | Rod (usable as cold-filler rod for GTAW) | R |
| **ER** | Can be used as either electrode or rod | ER |
| **70** | Minimum tensile strength of weld deposit in ksi | 70,000 psi (480 MPa) |
| **S** | Solid wire (as opposed to cored wire) | S |
| **6** | Chemical composition designation (deoxidizer level) | 6 = highest Mn+Si content |

**Common ER70S designations:**

| Designation | Si content | Mn content | Key characteristic |
|---|---|---|---|
| ER70S-2 | Low | Low | Triple-deoxidized for rusty/oily surfaces; used on some pipe applications |
| ER70S-3 | Medium | Medium | General purpose; minimal deoxidizers |
| **ER70S-6** | **High** | **High** | **Most common industrial wire**; highest deoxidizer content; works best on mill-scale, slightly rusty steel |

**ER70S-6 is the standard GMAW wire for mild steel.** Its high manganese and silicon content provides excellent deoxidation, allowing it to be used on less-than-perfectly-clean base metal. The resulting weld metal also has good mechanical properties.[^1] [^4]

---

### FCAW (flux-cored wire) — AWS A5.20 and A5.36

Flux-cored wire has a steel outer sheath surrounding a powdered flux core. The classification system:[^2] [^3]

**Format (A5.20): E-X-XT-X**

| Segment | Meaning | Example (E71T-1) |
|---|---|---|
| **E** | Electrode |  |
| **7** | Tensile strength designation | 7 = 70 ksi (480 MPa) |
| **1** | Welding position | 0 = flat/horiz; 1 = all positions |
| **T** | Tubular (cored) wire | T |
| **-1** | Usability characteristics — flux type, polarity, shielding gas | -1 = gas-shielded, DCEP, CO₂ or Ar/CO₂ |

**Key FCAW wire types:**

| Wire | Standard | Polarity | Gas | Positions | Key characteristic |
|---|---|---|---|---|---|
| **E71T-1C** | A5.20 | DCEP | 100% CO₂ | All | Gas-shielded; smooth arc, low spatter |
| **E71T-1M** | A5.20 | DCEP | 75/25 Ar/CO₂ | All | Gas-shielded; M = mixed gas designation |
| **E71T-11** | A5.20 | DCEN | None (self-shielded) | All (limited) | Self-shielded; no external gas needed |
| **E71T-8** | A5.20 | DCEN | None (self-shielded) | All | Self-shielded; low-hydrogen rating |

**The critical difference between gas-shielded and self-shielded FCAW:**

- **Gas-shielded (E71T-1, E71T-9, etc.):** requires external shielding gas to protect the weld. Cannot be used outdoors in wind without windscreening. Produces high-quality, clean welds.
- **Self-shielded (E71T-11, E71T-8, etc.):** the flux core generates its own shielding gas when it burns — no external gas required. More wind-tolerant. Used for outdoor structural steel erection and field work.[^2]

**Important:** E71T-11 is a self-shielded wire — do NOT hook up shielding gas to it. Using external gas on a self-shielded wire actually makes the shielding WORSE because the external gas can disrupt the self-generated shield.[^2]

---

### MCAW (metal-cored wire) — AWS A5.36

Metal-cored wire looks similar to flux-cored wire (tubular/sheath design) but the core contains metal powders rather than flux. This gives MCAW characteristics somewhere between solid GMAW wire and FCAW:[^3]

- **Like GMAW:** produces very little slag (no heavy flux slag blanket)
- **Like FCAW:** higher deposition rate than solid wire; better tolerance for mill scale

**Common MCAW classification:**

**E70C-6M** (per AWS A5.36)

| Segment | Meaning |
|---|---|
| E | Electrode |
| 70 | 70 ksi minimum tensile |
| C | Composite (cored) electrode |
| -6 | Composition designation (like S-6 for solid wire) |
| M | Mixed gas (Ar/CO₂) required |

**E70C-6M requires 75/25 or 90/10 Ar/CO₂** shielding gas. Do NOT use 100% CO₂ — the arc becomes unstable and the weld quality degrades.[^3]

**Applications for MCAW:**
- High-deposition structural fillet welds where post-weld slag removal is an issue (MCAW produces little slag → less cleanup)
- Code-quality welds where GMAW solid wire productivity isn't sufficient but FCAW slag is a problem
- Pipe fit-up and structural multi-pass welds

---

## Wire filler metals reference table

| Wire | AWS Spec | Polarity | Shielding | Positions | Diameter range | Primary use |
|---|---|---|---|---|---|---|
| **ER70S-6** | A5.18 | DCEP | CO₂ or Ar/CO₂ | All | 0.023–1/16" (0.6–1.6 mm) | General GMAW mild steel |
| **E71T-1C** | A5.20 | DCEP | 100% CO₂ | All | 0.035–7/64" (0.9–2.8 mm) | Gas-shielded FCAW |
| **E71T-1M** | A5.20 | DCEP | 75/25 Ar/CO₂ | All | 0.035–7/64" (0.9–2.8 mm) | Gas-shielded FCAW (mixed gas) |
| **E71T-11** | A5.20 | DCEN | None (self-shielded) | All (flat/horiz preferred) | 0.035–5/64" (0.9–2.0 mm) | Self-shielded FCAW — field/outdoor |
| **E70C-6M** | A5.36 | DCEP | 75/25 or 90/10 Ar/CO₂ | All | 0.035–3/32" (0.9–2.4 mm) | MCAW — high deposition, low slag |

---

## Drive systems — drive rolls and liner

The wire feeder's job is to push wire from the spool to the contact tip at a precise, consistent speed. The drive rolls are the critical components that make this happen.[^5] [^6]

### Drive roll types — match the wire type

| Drive roll groove shape | Wire type | Reason |
|---|---|---|
| **V-groove (knurled)** | Flux-cored wire, metal-cored wire | The knurled (serrated) groove grips the harder cored wire without crushing the tubular sheath |
| **V-groove (smooth)** | Solid hard wire (ER70S-6) | Smooth V-groove feeds solid wire without marring the surface; won't crack the wire |
| **U-groove (smooth)** | Aluminum (soft wire) | The U-groove is rounded and smooth — grips aluminum gently without cutting into the soft wire surface |
| **Serrated/knurled** | Flux-cored and metal-cored wire only | Same as V-groove knurled — grips the harder sheath |

**CRITICAL:** Never use a knurled/serrated drive roll on aluminum. The serrations cut into the soft aluminum wire surface, creating shavings that clog the liner. Never use a smooth V-groove on cored wire — it may slip or crush the tubular sheath.[^5]

### Drive roll tension (pressure)

Drive roll tension (the force pressing the rolls against the wire) must be set correctly:[^5]

- **Too little tension:** the drive rolls slip on the wire — inconsistent wire feed speed — erratic arc
- **Too much tension:** the rolls crush the wire (especially problematic for cored wires — crushing collapses the flux core); for solid wire, excess tension creates shavings that clog the liner

**Test for correct tension:** Grip the wire coming out of the gun tip. If the drive rolls slip without bending the wire into a tight coil, tension is approximately correct. If the rolls immediately start buckling wire, tension is too high.

### Liner

The wire travels from the feeder to the gun through a **liner** — a spiral steel coil (or plastic for some applications) inside the gun cable.[^5]

- **Match liner inner diameter to wire diameter** — too tight and the wire binds; too loose and the wire wanders and kinks
- **Keep the liner as straight as possible** — kinks in the gun cable cause the liner to bind and produce inconsistent WFS
- **Replace liners regularly** — worn liners accumulate wire shavings and develop rough spots that cause bird-nesting

---

## Gun assembly components

The GMAW/FCAW gun delivers the wire, current, and gas to the weld zone. Know all components and their maintenance requirements.[^5] [^6]

| Component | Function | Common maintenance issue |
|---|---|---|
| **Trigger** | Starts wire feed, current, and gas flow simultaneously | Trigger switch failure; spatter in trigger housing |
| **Contact tip** | Transfers current to the wire; copper alloy; consumable | Must be matched to wire diameter exactly; replace when worn oval/plugged |
| **Contact tip holder** | Threads the contact tip to the gun body; sometimes includes a diffuser | Spatter build-up; heat damage |
| **Gas diffuser** | Distributes shielding gas evenly around the contact tip | Spatter plugging the gas holes |
| **Gas nozzle (cup)** | Directs shielding gas flow around the arc zone | Spatter build-up inside (insulate nozzle from the arc to prevent shorting); replace when heavily fouled |
| **Insulator** | Prevents electrical contact between the gas nozzle and the contact tip holder | Must be intact to prevent short-circuit through the gun body |
| **Gun handle/body** | Ergonomic housing; contains the liner connection, gas line, and trigger wiring | |

**Contact tip sizing:** Contact tips are stamped with the wire diameter they accept. A 0.035" tip for 0.035" wire. If the wire is too tight in the tip, the tip overheats and welds itself to the wire (burnback). If the tip hole is too large, the wire wanders and arc characteristics suffer.[^5]

---

## Operating variables — what controls what

Understanding which variable controls which result is essential for setup and troubleshooting.[^1] [^5]

| Variable | Primary effect | Secondary effect |
|---|---|---|
| **Voltage (arc voltage setting)** | Arc length; bead width; weld appearance | Heat input; fusion zone width |
| **Wire feed speed (WFS)** | Amperage; burn-off rate; deposition rate | Heat input; penetration depth |
| **Travel speed** | Bead width; heat input per unit length | Weld profile; penetration |
| **CTWD (Contact Tip to Work Distance)** | Arc length; effective amperage (longer CTWD = more wire stickout = more resistance heating = effectively lower amperage at the arc) | Deposition rate |
| **Electrode extension (stickout)** | Wire resistance preheat between tip and arc | Affects burn-off without changing WFS |
| **Travel angle (gun angle)** | Bead profile; penetration direction; spatter direction | Shielding gas coverage |
| **Shielding gas flow rate** | Atmospheric protection of the weld pool | Arc stability |

**CTWD (Contact Tip to Work Distance)** is the distance from the end of the contact tip to the work surface. It includes:[^5]
- The electrode extension (the length of free wire from the contact tip to the arc)
- The arc length itself

Typical CTWD values:
- GMAW short-circuit: 3/8–3/4 in (10–20 mm)
- GMAW spray: 3/4–1 in (19–25 mm)
- FCAW gas-shielded: 3/4–1 in (19–25 mm)
- FCAW self-shielded: 1–2 in (25–50 mm) — longer CTWD required for preheating the self-shielded wire core before the arc

---

## Numbers you need to memorize

- **ER70S-6: most common GMAW mild steel wire — high Si + Mn deoxidizers**[^1]
- **E71T-1: gas-shielded FCAW — DCEP, CO₂ or Ar/CO₂**[^2]
- **E71T-11: self-shielded FCAW — DCEN, NO external gas**[^2]
- **E70C-6M: MCAW — DCEP, 75/25 or 90/10 Ar/CO₂ required**[^3]
- **V-groove smooth drive rolls: solid wire; U-groove: aluminum; V-groove knurled: cored wire**[^5]
- **Self-shielded FCAW polarity: DCEN** (opposite of most other wire processes)[^2]
- **Gas-shielded FCAW polarity: DCEP**[^2]
- **GMAW solid wire polarity: DCEP**[^1]
- **Typical GMAW CTWD (spray): 3/4–1 in (19–25 mm)**[^5]
- **Self-shielded FCAW CTWD: 1–2 in (25–50 mm) — longer than gas-shielded**[^5]

---

## What the textbook doesn't tell you

**E71T-11 polarity catches people out constantly.** Almost every other wire-feed process uses DCEP. E71T-11 self-shielded FCAW uses DCEN. If you hook up your machine for DCEP and run E71T-11, you'll get poor arc stability, porosity, and erratic arc characteristics. Check polarity first every time you change wire types.[^2]

**Contact tips are cheap. Don't nurse a worn one.** A worn contact tip (hole has gone oval from wire wear) produces a wandering arc, erratic feeding, and increased spatter. The cost of replacing a contact tip is trivial compared to a second of poor weld quality. Replace contact tips at the first sign of wear or build-up — experienced welders carry spares in their apron.

**Never use anti-spatter spray inside the gas nozzle on FCAW self-shielded.** Some welders spray anti-spatter inside the gas nozzle on GMAW to prevent spatter build-up. On self-shielded FCAW, there's no gas nozzle in most configurations — the nozzle tip geometry is different. Using gas-shield anti-spatter on SS-FCAW equipment or spraying into the wrong area can contaminate the electrode and cause porosity.[^4]

**MCAW produces almost no slag — this is both an advantage AND a trap.** Because slag holds the pool shape and slows cooling in FCAW, the absence of slag with MCAW means the pool is more fluid and weld profile control requires more attention. On vertical and overhead, MCAW can be harder to control than FCAW because you have less slag support. Know your wire type and adjust your technique accordingly.[^3]

---

## Key terms

- **ER70S-6:** solid GMAW wire for mild steel — high deoxidizer content; AWS A5.18
- **E71T-1:** gas-shielded FCAW wire (C or M suffix for CO₂ or mixed gas); DCEP; all positions; AWS A5.20
- **E71T-11:** self-shielded FCAW wire; DCEN; no external gas; all positions (flat/horiz preferred for best quality); AWS A5.20
- **E70C-6M:** metal-cored wire (MCAW); DCEP; requires Ar/CO₂ mixed gas; AWS A5.36
- **Cored wire:** wire with a tubular steel sheath surrounding a powder core (flux for FCAW, metal powder for MCAW)
- **Solid wire:** completely solid metal wire (ER70S-6) — no core
- **Drive rolls:** the motor-driven rollers in the wire feeder that push wire to the gun
- **V-groove (smooth):** drive roll type for solid wire
- **U-groove:** drive roll type for soft aluminum wire
- **Knurled/serrated groove:** drive roll type for cored (FCAW/MCAW) wire
- **CTWD:** Contact Tip to Work Distance — tip-to-surface measurement that determines stickout and effective amperage
- **Electrode extension (stickout):** length of free wire between contact tip and arc — part of CTWD
- **Liner:** the coiled-wire tube inside the gun cable through which the electrode wire travels

---

## Common exam trap

- **"E71T-11 requires CO₂ shielding gas"** — completely wrong. E71T-11 is self-shielded. Using external gas with SS-FCAW interferes with the wire's self-generated shield and degrades weld quality.
- **"Use knurled drive rolls for aluminum"** — false and harmful. Knurled rolls cut into aluminum and create shavings that clog the liner. Use smooth U-groove rolls for aluminum.
- **"ER70S-6 and ER70S-3 are interchangeable"** — they are both solid GMAW wires but not identical. ER70S-6 has higher deoxidizer content and works better on marginally clean steel. ER70S-3 is appropriate for very clean steel. Using ER70S-3 on mill-scale or slightly rusty steel produces porosity.
- **"The -C and -M suffix on FCAW wire just means the manufacturer"** — false. The -C means 100% CO₂ shielding gas; the -M means mixed gas (Ar/CO₂). You must use the correct gas for the electrode suffix — using CO₂ on an -M electrode or mixed gas on a -C electrode is a WPS deviation.

---

## Practice question preview

**Q:** A welder is setting up to run E71T-11 self-shielded FCAW wire on an outdoor structural fillet weld. Which combination of polarity and gas is correct?

A) DCEP, 100% CO₂ shielding gas  
B) DCEN, no external shielding gas  
C) DCEP, 75/25 Ar/CO₂ shielding gas  
D) DCEN, 75/25 Ar/CO₂ shielding gas  

**Correct: B**

**Explanation:** E71T-11 is a self-shielded FCAW wire (per AWS A5.20). It operates on DCEN (DC Electrode Negative) — the opposite polarity from most other wire-feed processes. It generates its own shielding from the flux core burning in the arc — external gas is NOT required and would actually interfere with the self-shielding mechanism. Options A and C use DCEP (wrong polarity) and also add external gas (wrong for SS-FCAW). Option D has the correct DCEN polarity but still incorrectly adds shielding gas.

**Red Seal mapping:** D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables — correctly identifies wire type, polarity, shielding gas requirements)

---

[^1]: [AWS A5.18 — Specification for Carbon Steel Electrodes and Rods for Gas Shielded Arc Welding (2021)](https://www.aws.org/standards/page/aws-a518), ER70S-6 classification (high Mn+Si deoxidizers), ER70S-2 and ER70S-3 comparison, tensile strength requirements (70 ksi), all-position capability, DCEP polarity
[^2]: [AWS A5.20 — Specification for Carbon Steel Electrodes for Flux Cored Arc Welding (2015)](https://www.aws.org/standards/page/aws-a520), E71T-1C (DCEP, 100% CO₂), E71T-1M (DCEP, mixed gas), E71T-11 (DCEN, self-shielded, no gas), E71T-8 (DCEN self-shielded low-hydrogen), classification format, position designations (0 = flat/horiz, 1 = all positions)
[^3]: [AWS A5.36 — Specification for Carbon and Low-Alloy Steel Flux Cored and Metal Cored Welding Electrodes (2016)](https://www.aws.org/standards/page/aws-a536), E70C-6M (MCAW) classification, mixed gas requirement for MCAW, metal-core characteristics vs FCAW flux core
[^4]: [Lincoln Electric — Consumables Catalog](https://www.lincolnelectric.com/en/products/consumables), ER70S-6 vs ER70S-3 deoxidizer comparison, E71T-1 gas shielded FCAW, E71T-11 self-shielded FCAW, E70C-6M MCAW product specifications, diameter ranges, applications
[^5]: [Miller Electric — Wire Welding Process and Product Guide](https://www.millerwelds.com/resources/article-library/mig-gmaw-welding-guide), drive roll types (V-groove smooth for solid, V-groove knurled for cored, U-groove for aluminum), drive roll tension setting procedure, liner maintenance, contact tip sizing and replacement, CTWD definitions (3/4–1" spray GMAW; 1–2" SS-FCAW)
[^6]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 14–15 "Wire Feed Filler Metals and Feeders": gun assembly components (contact tip, gas diffuser, nozzle, insulator), operating variables (voltage, WFS, travel speed, CTWD, stickout)
