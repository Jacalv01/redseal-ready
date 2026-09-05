---
id: p2-s1-c
period: 2
section: 1
section_title: Foundational Skills, Safety, Procedures and Properties of Metals
topic_letter: C
topic_title: Other Processes
hours: 2
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to describe other welding-related processes and their applications.
objectives:
  - Describe robotics, handheld laser beam welding, resistance spot welding, thermite, friction stir welding, and 3D metal printing.
red_seal_mapping:
  - A-5.05 (Selects welding processes and power source)
  - A-4.03 (Plans job tasks)
citations:
  - source: AWS Welding Handbook Vol. 3 — Welding Processes, Part 2 (9th ed.)
    ref: Chapters on LBW, RSW, thermite, FSW — process descriptions and applications
    url: https://pubs.aws.org/p/365/welding-handbook-volume-3-welding-processes-part-2
  - source: TWI Global — Process Knowledge Base
    ref: Friction stir welding overview, laser beam welding overview, resistance spot welding overview
    url: https://www.twi-global.com/technical-knowledge/job-knowledge
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 26 — Other Welding Processes; robotics, RSW, FSW, thermite
    url: https://www.g-w.com/modern-welding
  - source: Miller Electric — Robotic Welding Guide
    ref: Robotic MIG/GMAW cells, MTBF concepts, joint repeatability requirements
    url: https://www.millerwelds.com/resources/article-library/robotic-welding
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic C
    ref: pp. 28–29
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Other Processes

Six processes. None of them require you to pull a trigger or strike an arc the traditional way. Most of them exist because they do something better, faster, or safer than SMAW/GMAW for specific applications. Knowing *what* they're for — and critically, *what they can't do* — is what the Red Seal exam tests on this topic.

---

## 1. Robotic welding

### What it is
A robotic welding cell consists of an articulated robot arm fitted with a welding gun (typically GMAW or FCAW), a positioner or fixture to hold the workpiece, and a controller that runs pre-programmed weld paths.[^4]

### How it works
The robot is programmed (taught) by moving the arm through the weld path and recording positions — called **teach-pendant programming** — or by offline programming software. Once programmed, it repeats the path with consistent speed, angle, and contact-tip-to-work distance for every part.[^4]

### Applications
- Automotive body welding (billions of resistance spot welds per year, worldwide)
- Structural component repetitive fillet welds (gussets, brackets)
- High-volume pipe assembly welding
- Any application where joints are identical and repeatability matters more than flexibility

### Limitations — where robotic welding fails
- **Part-to-part variation.** If each part has slightly different fit-up, the programmed path misses the joint. Robots need tight fit-up tolerances — often ±0.5 mm vs the 1–3 mm acceptable for hand welding.[^4]
- **Complex geometry.** Robot arms have reach and rotation limits.
- **Low-volume or one-off work.** Programming cost isn't justified for a single part.
- **Repair welding.** A defective robot weld still needs a human to fix it.

### Your role as a welder near robots
Robotic cells still need human welders to: program/teach the robot, inspect weld quality, clean wire liners and contact tips, fit up parts into fixtures, and perform repair welds. Robots don't replace welders in most shops — they change *what* the welder does.

---

## 2. Handheld Laser Beam Welding (LBW)

### What it is
Laser Beam Welding uses a high-power laser focused to a tiny spot to melt and fuse metal. Traditional LBW is automated (CNC positioning); **handheld LBW** is a newer tool (2015–present) that brings a laser in a hand-held gun format to the shop floor.[^1][^2]

### How it works
A fiber-optic cable delivers laser energy from a generator to a handheld head. The operator moves the laser spot along the joint. Shielding gas (typically argon or nitrogen) protects the molten pool. Filler wire may or may not be added.[^2]

### Key characteristics
- **Extremely fast** — travel speeds 3–10× faster than GMAW on thin material
- **Very low distortion** — because the heat zone is extremely narrow
- **No spatter** — cleaner than GMAW/FCAW
- **Works on thin, coated, dissimilar metals** — can join galvanized, aluminum to steel, etc.
- **High capital cost** — equipment costs are substantial
- **Eye hazard — Class 4 laser** — requires specialized laser safety eyewear (not standard welding shade). Reflected beams can permanently blind anyone in the area.[^3]

### Applications
- Automotive: door frames, battery enclosures, galvanized body panels
- HVAC: thin-gauge ductwork
- Electronics: precision assemblies

### What it can't do
- Deep, thick section welds (limited penetration without high-power equipment)
- Dirty or rusty material — laser is sensitive to surface condition
- Field welding — power and cooling requirements are significant

---

## 3. Resistance Spot Welding (RSW)

### What it is
Two copper electrodes clamp the workpiece, force is applied, and a very high current (up to 10,000 A or more) flows through the contact area for milliseconds.[^1] The resistance of the steel to current flow generates heat exactly at the interface — creating a molten **nugget** that solidifies under pressure into a weld spot.

### How it works
**Weld cycle:**
1. **Squeeze** — electrodes clamp the sheets together
2. **Weld** — current flows; nugget forms at interface
3. **Hold** — current stops; electrodes maintain pressure while nugget solidifies
4. **Release** — electrodes retract; part advances to next spot location

### Key characteristics
- **Fast** — a single spot weld takes 0.1–0.5 seconds[^1]
- **No filler metal** — the base metal itself is fused
- **No shielding gas** — the short weld time prevents significant atmospheric contamination
- **Limited to lap joints** — only joins overlapping sheets; cannot weld butt joints or groove welds
- **Joint must be accessible from both sides** — both electrodes need contact

### Applications
- Auto body assembly (each car has ~4,000–6,000 spot welds[^1])
- Sheet metal ductwork
- Appliance manufacturing

### Electrode wear
Copper electrodes erode and mushroom with use. Electrodes must be dressed (trimmed back to their cone geometry) or replaced at intervals. A worn electrode makes a larger contact area → lower current density → weaker or no nugget.[^1]

---

## 4. Thermite Welding

### What it is
A chemical reaction between aluminum powder and iron oxide (rust/Fe₂O₃) generates enough heat — approximately **2500°C (4500°F)**[^1] — to melt and fuse steel without any arc or external power source.

### The reaction
> Fe₂O₃ + 2 Al → Al₂O₃ + 2 Fe + heat

The products are liquid iron (the weld metal) and aluminum oxide slag. The liquid iron pours into a mold prepared around the joint.[^1]

### Applications
- **Railway track welding** — the primary industrial application. Joining rails in the field where no power is available and the joint must have load-bearing capacity identical to the parent rail.
- **Electrical grounding connections** — joining copper conductors to earth rods (sold as "Cadweld" systems)
- **Large cross-section joints** in remote locations

### Key characteristics
- **No power source required** — the reaction is initiated with a small igniter or magnesium strip
- **Single-shot process** — each use requires a complete new thermite kit
- **High heat** — extreme fire and burn hazard; must be performed in a designated area with fire protection
- **Cannot be stopped once started** — the reaction runs to completion

### Limitations
- Cannot be used on thin material — minimum ~25 mm rail cross-section
- No parameter control — chemistry is fixed
- Not a general fabrication process; specialist application only

---

## 5. Friction Stir Welding (FSW)

### What it is
A non-consumable rotating tool is plunged into the joint and traversed along it. Frictional heat softens (but does not melt) the metal. The tool's shoulder mixes the softened metal across the joint, creating a solid-state bond.[^2]

### Key characteristics
- **No melting** — FSW occurs below the melting point. The metal is plasticized, not liquid. This is called a **solid-state joining process**.[^2]
- **No filler metal, no shielding gas** — self-contained process
- **Exceptional joint quality** — no solidification defects (porosity, hot cracking), because the metal never melts
- **Low distortion** — lower heat than fusion welding
- **Works on aluminum alloys that can't be fusion-welded** — some 7xxx (aerospace) alloys that crack when fusion-welded join fine by FSW

### Applications
- Aerospace: fuselage panels, fuel tanks (aluminum)
- Shipbuilding: aluminum deck panels
- Rail cars: aluminum extrusions
- Automotive: aluminum body components

### Limitations
- **High tooling force** — the machine must push the rotating tool with significant downforce. Requires a robust machine; not portable for field use.
- **Joint access** — tool must be able to plunge into the joint from one side with backing support on the other
- **Cannot weld vertical or overhead** — gravity-sensitive process (requires rigid fixturing)
- **Exit hole** — when the tool retracts, it leaves a hole at the end of the weld that must be drilled out or run off onto runoff tabs

---

## 6. 3D Metal Printing (Additive Manufacturing)

### What it is
Metal is deposited layer by layer to build a 3D part from a digital model. The most relevant variants for welders are:

**Wire Arc Additive Manufacturing (WAAM):**
Uses a GMAW or GTAW torch as the deposition head, depositing weld beads layer-by-layer on a substrate to build up a part. Essentially robotic welding that builds shape instead of joining two pieces.[^2]

**Powder Bed Fusion (Selective Laser Melting / SLM):**
Fine metal powder is spread in layers; a laser selectively melts each layer pattern. Used for titanium, Inconel, and tool steel aerospace parts. High precision, high cost.

### Applications (WAAM — most relevant to welders)
- Large structural titanium aerospace components
- Near-net-shape forgings replaced by deposited billets
- Repair of worn surfaces (overlaying bearing journals, turbine blade tips)

### Limitations
- Complex parameters — each pass must be carefully controlled for consistent mechanical properties
- As-deposited structure may require heat treatment (stress relief, HIP) before use in critical applications
- Not yet a mainstream shop process for most Alberta fabricators — awareness is the goal at Period 2 level

---

## Process comparison table

| Process | Power source needed | Filler | Fusion welding? | Best for |
|---|---|---|---|---|
| Robotic GMAW | Yes (welding machine + controller) | Wire | Yes | Repetitive production |
| Handheld LBW | Yes (high-power laser generator) | Optional | Yes | Thin/coated metals, clean shop |
| Resistance Spot | Yes (high-current transformer) | No | Yes | Lap joints on sheet metal |
| Thermite | No | No (base metal) | Yes | Rail, remote large joints |
| Friction Stir | Yes (motor, machine frame) | No | **No (solid-state)** | Aluminum, aerospace |
| WAAM (3D print) | Yes (robot + welding machine) | Wire | Yes | Complex shape fabrication |

---

## Numbers you need to memorize

- **RSW spot weld current:** up to 10,000+ A[^1]
- **RSW weld cycle time:** 0.1–0.5 seconds per spot[^1]
- **Thermite reaction temperature:** ~2500°C (4500°F)[^1]
- **Thermite reaction products:** liquid iron + aluminum oxide slag[^1]
- **FSW is a solid-state process** — metal never melts[^2]
- **Handheld LBW hazard:** Class 4 laser — requires laser safety eyewear, not standard welding shade[^3]
- **Robot fit-up tolerance:** typically ±0.5 mm (tighter than hand welding)[^4]

---

## What the textbook doesn't tell you

**Friction stir welding is why the Space Shuttle External Tank looks the way it does.** The massive aluminum fuel tanks are FSW-joined — it was the first major aerospace adoption of the process (early 1990s). The joints are stronger and more reliable than any fusion-welded alternative on that alloy. Knowing *why* a process was developed gives you better intuition for when to reach for it.

**Thermite welding on railroad tracks is incredibly dangerous when done wrong.** The preheating step is critical — if the rail is wet or cold, the poured liquid iron can cause a steam explosion inside the mold. Rail thermite welders are certified specialists. Don't approach a thermite weld in progress unless it's your job.

**Robotic welding is your employer's efficiency tool, not your job replacement.** Understanding robot cells makes you more valuable — someone has to program them, fixture the parts, inspect the output, and repair the defects they produce. Shops increasingly want welders who can program and troubleshoot robots, not just weld.

---

## Key terms

- **Robotic welding cell:** integrated system of robot arm, positioner, controller, and welding power source for automated, repeatable welds
- **Teach pendant:** handheld controller used to manually move a robot arm and record weld path positions
- **Laser Beam Welding (LBW):** fusion welding using focused laser energy; extremely fast, low distortion
- **Resistance Spot Welding (RSW):** fusion welding using electrical resistance heating between copper electrodes; makes nugget-shaped fusion bonds in lap-joint sheet metal
- **Nugget:** the lens-shaped fusion zone created by a resistance spot weld
- **Thermite welding:** exothermic chemical reaction (Al + Fe₂O₃) producing liquid iron that fills a joint mold; no external power
- **Friction Stir Welding (FSW):** solid-state joining process using a rotating tool to plasticize metal below its melting point
- **Solid-state welding:** joining without melting — the material is in plastic/solid state throughout
- **WAAM:** Wire Arc Additive Manufacturing — layer-by-layer deposition using a welding arc to build 3D parts
- **Additive manufacturing:** building parts by adding material layer-by-layer (opposite of machining, which removes material)

---

## Common exam trap

- **Friction stir welding is the only process that does NOT melt the base metal.** Any answer describing FSW as a "fusion process" is wrong. The question will try to lump it with the others.
- **RSW cannot make butt joints** — only lap joints where both electrodes can contact the outer surfaces. Exam questions may describe a butt joint scenario and ask which process to use — RSW is always the wrong answer for butt joints.
- **Thermite welding needs no power source** — the energy comes from the chemical reaction. Exam distractors often include "high-current transformer required."
- **Handheld LBW requires laser-specific eye protection, NOT welding shades** — standard auto-darkening helmets do NOT protect against Class 4 laser reflections. This is a safety question target.
- **Robotic GMAW still requires a shielding gas** — robots use wire-feed processes that have all the same gas requirements as hand GMAW. "Robots don't need shielding gas" is a false statement.

---

## Practice question preview

**Q:** A railway maintenance crew needs to join two rail sections in a remote field location with no electrical power available. Which welding process is MOST appropriate?

A) Resistance spot welding (RSW)
B) Submerged arc welding (SAW)
C) Thermite welding
D) Friction stir welding (FSW)

**Correct: C**

**Explanation:** Thermite welding is specifically designed for field joining of railroad rails. It requires no external power source — the exothermic reaction between aluminum powder and iron oxide generates the ~2500°C heat needed to produce liquid weld metal. (A) RSW requires a high-current transformer — not field-portable, and cannot join the cross-sectional area of a rail. (B) SAW requires a welding power source, wire feeder, and flux hopper — not practical in remote field conditions. (D) FSW requires a large, rigid machine frame and motor — not portable.

**Red Seal mapping:** A-5.05 (Selects welding processes and power source)

---

[^1]: [AWS Welding Handbook Vol. 3 — Welding Processes, Part 2, 9th ed.](https://pubs.aws.org/p/365/welding-handbook-volume-3-welding-processes-part-2); Chapters on RSW (nugget formation, electrode wear), thermite welding (reaction chemistry, rail applications), LBW process principles
[^2]: [TWI Global — Process Knowledge Base](https://www.twi-global.com/technical-knowledge/job-knowledge); Friction Stir Welding overview, WAAM (Wire Arc Additive Manufacturing), Laser Beam Welding
[^3]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 26 — Other Welding Processes; process descriptions, laser safety hazards, comparisons
[^4]: [Miller Electric — Robotic Welding Guide](https://www.millerwelds.com/resources/article-library/robotic-welding); robotic cell design, fit-up tolerances, programming approaches, maintenance requirements
[^5]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic C](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 28–29
