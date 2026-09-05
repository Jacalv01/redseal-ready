---
id: p3-s4-a
period: 3
section: 4
section_title: Shielded Metal Arc Welding (SMAW)
topic_letter: A
topic_title: SMAW on Mild Steel
hours: 50
weight_pct: 21
outcome: >
  Upon successful completion, learners will be able to perform SMAW groove welds on mild
  steel plate in 2G, 3G, 45° overhead, and 4G positions using E4310 (E6010) for the root
  pass and E4918 (E7018) for fill and cap, including 4GF with backing per CSA W47.1.
objectives:
  - Perform 2G, 3G, 45° overhead and 4G welds using E4310 (E6010) for the root pass and E4918 (E7018) for the fill and cap.
  - Perform 4GF weld using E4918 (E7018) with backing according to CSA Standard W47.1.
red_seal_mapping:
  - D-13.01 (Selects SMAW equipment and consumables)
  - D-13.02 (Sets up SMAW equipment)
  - D-13.03 (Sets operating parameters for SMAW equipment)
  - D-13.04 (Performs weld using SMAW equipment)
citations:
  - source: AWS A5.1 — Carbon Steel Electrodes for SMAW
    ref: E6010 and E7018 classifications, chemistry, mechanical properties, storage requirements
    url: https://pubs.aws.org/p/1085/a51-a51m-2012-specification-for-carbon-steel-electrodes-for-shielded-metal-arc-welding
  - source: CSA W47.1 — Certification of Companies for Fusion Welding of Steel
    ref: Annex B (welder qualification matrix), 4GF with backing, position qualification scope
    url: https://www.csagroup.org/store/product/CSA%20W47%3A1/
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 12 (SMAW groove weld qualification), acceptance criteria, preheat requirements
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: Lincoln Electric — Procedure Handbook of Arc Welding
    ref: E6010 root pass technique, E7018 fill/cap parameters, groove weld parameters by position
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: Miller Electric — SMAW Electrode Selection and Parameters Guide
    ref: E6010 and E7018 amperage ranges, position-specific settings, drag angle
    url: https://www.millerwelds.com/resources/article-library/smaw-electrode-guide
---

# SMAW on Mild Steel — Red Seal Level (2G, 3G, 4G, 4GF)

The E6010 root and E7018 fill/cap combination is the most tested combination in Canadian structural and pressure vessel welding. The 4G overhead plate test and the 4GF (overhead with backing) are the highest-difficulty SMAW plate qualifications. Master these and you carry a credential that most journeypersons don't have.

---

## The Electrode Combination — Why E6010 Root + E7018 Fill/Cap

This isn't an arbitrary pairing — each electrode is best suited for its specific role:[^1][^4]

| Electrode | Root or fill? | Why it's there |
|---|---|---|
| **E4310 / E6010** | Root pass | Penetrating arc, forceful spray-to-globular transfer, digs into the root gap cleanly, works on dirty or tight root openings, tolerates open-root geometry |
| **E4918 / E7018** | Fill and cap passes | Low-hydrogen coating, higher tensile strength (480 MPa / 70 ksi), smooth arc, excellent mechanical properties, reduced spatter, better all-position performance |

**Canadian designation vs AWS:**
- Canadian: **E4310** = AWS **E6010** (4 = 40 ksi × 10 = 60 ksi, roughly; Canadian suffix 10 = same as AWS suffix 10)
- Canadian: **E4918** = AWS **E7018** (same logic; 18 = same low-hydrogen coating, DCEP, all-position)

The AWS classification system is more commonly used on the Red Seal exam and in manufacturer data.[^1]

---

## E6010 — The Root Pass Electrode

**Classification: E6010** — AWS A5.1[^1]

| Property | Value |
|---|---|
| **Coating type** | High-cellulose sodium |
| **Polarity** | DCEP (DC Electrode Positive) |
| **Positions** | All positions (1, 2, 3, 4, 5, 6) |
| **Min tensile strength** | 430 MPa (62,000 psi) deposit |
| **Typical amperage (3/32" / 2.4 mm dia)** | 40–80 A |
| **Typical amperage (1/8" / 3.2 mm dia)** | 75–130 A |
| **Typical amperage (5/32" / 4.0 mm dia)** | 110–165 A |

### E6010 arc characteristics

- **Stiff, penetrating arc:** the cellulose coating produces a hydrogen-rich gas shield that creates a forceful, driving arc — ideal for punching through root gaps and fusing to root faces
- **Fast-freezing slag:** the slag layer is thin and fast-freezing, allowing welding in all positions without the slag running ahead of the puddle
- **Aggressive wash:** the arc wash at the toes is aggressive — good for fusion but requires care to prevent undercut

### Storage and handling — E6010

E6010 is a **cellulosic electrode** — it performs BEST with some moisture in the coating. Unlike E7018, E6010 must NOT be dried in a rod oven before use — excessive drying makes the arc rough and spattery.[^1][^4]

Store in the original sealed container. Use within reasonable time after opening. Do not store on humid jobsites without protection from rain and condensation — but do not put in a rod oven.

---

## E7018 — The Fill and Cap Electrode

**Classification: E7018** — AWS A5.1[^1]

| Property | Value |
|---|---|
| **Coating type** | Low-hydrogen iron powder |
| **Polarity** | DCEP (preferred) or AC |
| **Positions** | All positions |
| **Min tensile strength** | 480 MPa (70,000 psi) deposit |
| **Typical amperage (3/32" / 2.4 mm dia)** | 70–100 A |
| **Typical amperage (1/8" / 3.2 mm dia)** | 100–150 A |
| **Typical amperage (5/32" / 4.0 mm dia)** | 130–190 A |

### E7018 arc characteristics

- **Smooth, stable arc:** the iron-powder low-hydrogen coating produces very low spatter, consistent bead shape, and excellent mechanical properties
- **Thick slag:** the slag is heavier and slower than E6010 — it must be chipped and wire-brushed between every pass
- **Position sensitivity:** at high amperages, the E7018 puddle is fluid and tends to sag in vertical and overhead positions — reduce amperage 15–20% from flat setting for 3G and 4G work

### Storage and handling — E7018 (CRITICAL)

E7018 is a **low-hydrogen electrode** — its entire value comes from the low diffusible hydrogen content of the deposit. Moisture in the coating destroys this.[^1]

- **New, unopened container:** moisture-resistant hermetically-sealed container good for 6 months from manufacture date
- **Once container is opened:** if not in a rod oven, must be used within 4 hours (per AWS A5.1) or per the applicable WPS
- **Rod oven:** maintain at **120–150 °C (250–300 °F)** for E7018[^1]
- **Recondition:** electrodes exposed to humid air for more than 4 hours can be reconditioned at **260–430 °C (500–800 °F)** for 1–2 hours per AWS A5.1 — maximum one reconditioning cycle[^1]

**If E7018 gets wet:** the hydrogen in the moisture diffuses into the weld deposit → hydrogen-induced cracking (HIC) in the HAZ. This is the most common cause of underbead cracking in structural welding. Keep E7018 dry. Always.

---

## Groove Weld Positions — Review for 2G, 3G, 4G

| Position | Plate orientation | Weld axis | Welding direction |
|---|---|---|---|
| **1G** | Flat, weld on top | Horizontal | Along the joint length |
| **2G** | Vertical, weld horizontal | Horizontal | Across the vertical plate |
| **3G** | Vertical, weld vertical | Vertical | Upward (standard) or downward (special cases) |
| **4G** | Overhead, plate above | Horizontal | Along the joint length (under the plate) |
| **45° overhead** | Plate at 45° to horizontal, weld underneath | Diagonal | Combined overhead and inclined |

**Qualification scope (CSA W47.1 Annex B and ASME Section IX):[^2][^3]**
- 2G qualifies: 1G, 2G
- 3G qualifies: 1G, 3G
- 4G qualifies: 1G, 4G
- 3G + 4G together: 1G, 2G, 3G, 4G (all plate positions)

---

## 2G — Horizontal Groove Weld

### Setup
- **Plate:** 3/8" (10 mm) or 1/2" (12.7 mm) mild steel typical for qualification
- **Joint prep:** 30° bevel per side (60° included), 3/32" land, 3/16" root gap
- **Position:** plate stands vertical, weld runs horizontally

### E6010 Root Pass — 2G
- **Electrode size:** 3/32" (2.4 mm) — small electrode gives precise heat control in horizontal
- **Amperage:** 70–90 A
- **Polarity:** DCEP
- **Drag angle:** 10–15° in the direction of travel (backhand), torch slightly upward to counter gravity
- **Technique:** **stringer bead only** — no weaving on the root. Travel at steady speed, watching the keyhole.
- **Arc length:** short — just barely longer than the electrode diameter

### E7018 Fill/Cap — 2G (stringer beads)
- **Electrode size:** 1/8" (3.2 mm) for fill; 5/32" (4 mm) for cap if wider joint
- **Amperage:** 100–125 A (fill), 110–130 A (cap)
- **Stringer beads only** — the 2G position requires multiple horizontal stringer beads to fill the joint. Do NOT weave — the puddle sags under gravity.
- **Bead sequence:** build up from the root, each bead slightly overlapping the previous, working upward in the joint cross-section. The upper bead in each pass ties into the joint sidewall above.

---

## 3G — Vertical-Up Groove Weld

### Setup
- Same joint prep as 2G — 60° included, land, root gap
- Plate stands vertical, weld runs vertically — weld upward

### E6010 Root Pass — 3G uphill
- **Electrode size:** 3/32" (2.4 mm)
- **Amperage:** 60–80 A (lower than 2G to prevent excessive heat buildup climbing upward)
- **Drag angle:** 5–10° upward (torch slightly above horizontal, pointing up in the direction of travel)
- **Technique:** slight side-to-side weave in the root, pausing at each toe — or whip technique (short forward push, brief pause). The keyhole should remain small and consistent.

### E7018 Fill — 3G uphill
- **Electrode size:** 1/8" (3.2 mm)
- **Amperage:** 90–115 A (reduce 15–20% from flat setting)
- **Technique:** triangle weave or C-motion weave — pause at both toes to ensure full fusion. The puddle must freeze slightly between toe pauses. Do not rush.
- **Angle:** torch 5–10° upward (backhand), 10–15° to the plate (perpendicular to bevel face)

### E7018 Cap — 3G uphill
- **Amperage:** 85–110 A (slightly reduced from fill)
- **Technique:** widest weave pass — extend 1/16" to 1/8" past the bevel edge onto base metal at each toe. Pause longer at the toes than the fill passes.
- **Final appearance:** slight convex crown, flush with base metal surface, good tie-in at toes

---

## 4G — Overhead Groove Weld

The overhead position is physically the most demanding SMAW position. Success requires small electrode sizes, reduced amperage, and strict puddle control.[^4][^5]

### Setup
- Same joint prep — 60° included, root gap, land
- Plate positioned above the welder — the joint opens downward
- Welder works below, looking up into the joint

### Safety considerations
- **FR clothing is essential:** spatter and slag fall directly onto the welder. Full leather sleeves, leather bib, neck protection.
- **Head and neck protection:** hot slag on the neck and top of the head is a burn hazard. Use a cloth undercap or leather welding cap.
- **Body position:** stand to the side of the weld axis, not directly below — gravity brings spatter onto your face if you're directly underneath.

### E6010 Root Pass — 4G (overhead)
- **Electrode size:** 3/32" (2.4 mm) — ONLY 3/32" for overhead root. Never 1/8" — too much heat, too much puddle to control overhead.
- **Amperage:** 55–75 A (lowest end of the range)
- **Drag angle:** 5–10° in direction of travel (backhand)
- **Technique:** fast stringer bead. The surface tension of the molten metal holds it against the joint overhead — if the puddle gets too large, it drops out. Short arc. Keep moving.
- **Keyhole:** small, controlled keyhole is essential. More heat = larger keyhole = larger puddle = drips.

### E7018 Fill — 4G (overhead)
- **Electrode size:** 3/32" (2.4 mm) — start with small electrode for the hot pass; upgrade to 1/8" for fill if the joint is large enough
- **Amperage:** 70–90 A (3/32"); 90–110 A (1/8")
- **Technique:** tight stringer beads — NO weaving overhead. Each bead is a narrow stringer. Fill with as many stringers as needed.
- **Between passes:** chip and wire brush aggressively. Overhead slag doesn't fall away — it sticks to the previous bead. Clean thoroughly or the next bead welds over trapped slag.

### E7018 Cap — 4G (overhead)
- **Slightly reduced amperage from fill**
- **Stringer beads across the width of the cap** — two or three narrow stringers overlap to cover the joint width
- **Final check:** with a flashlight and mirror if needed, inspect the full length of each toe for undercut (very common overhead)

---

## 4GF — Overhead with Backing (CSA W47.1 Qualification)

The "F" suffix indicates **with backing** — a steel backing bar is tacked to the back of the joint before welding. No open root is required.[^2]

### What backing does

- The backing plate (typically 6 mm flat bar in full contact with the joint root face) provides a solid surface for the root bead to fuse to
- Eliminates the need to control an open keyhole — simplifies the root pass significantly
- The backing plate is a permanent addition (not removed after welding in most structural applications)

### WPS differences from open root

- **Root gap:** typically 0 to 3/32" with backing (versus 3/16" for open root — the backing closes the tight root)
- **Root pass electrode:** E7018 can be used for the root pass with backing (no need for E6010's penetrating arc). However, E6010 is acceptable and some WPS documents still specify it for the first pass even with backing.
- **First pass amperage:** increase slightly from the open-root setting — the backing conducts heat away from the first bead

### CSA W47.1 Qualification — 4GF

Under CSA W47.1 Annex B, the 4GF (overhead with backing) qualifies the welder for:[^2]
- 4G position with backing
- Does NOT qualify for 4G without backing (that requires a separate open-root overhead test)
- The backing test is explicitly noted as a separate qualification scope

---

## Interpass Temperature Control

For all SMAW groove welds on mild steel:[^3]

- **Maximum interpass temperature:** 260 °C (500 °F)
- **Check method:** contact pyrometer or Tempilstik, measured 75 mm from weld centerline
- **If exceeded:** allow to cool before starting the next pass
- **Minimum interpass = minimum preheat:** do not let the joint cool below the minimum preheat temperature between passes (check WPS)

---

## Numbers you need to memorize

- **E6010 polarity:** DCEP only[^1]
- **E7018 polarity:** DCEP preferred (AC acceptable)[^1]
- **E7018 rod oven temperature:** 120–150 °C (250–300 °F)[^1]
- **E7018 out-of-oven exposure limit:** 4 hours maximum (per AWS A5.1)[^1]
- **E7018 reconditioning temperature:** 260–430 °C for 1–2 hours[^1]
- **Overhead electrode size (4G root):** 3/32" (2.4 mm) maximum[^4]
- **Overhead amperage reduction:** 15–20% from flat position setting[^4]
- **Standard bevel prep:** 60° included angle (30° per side)[^3]
- **3G uphill torch angle:** 5–10° upward drag (backhand)[^4]
- **Max interpass temperature:** 260 °C (500 °F)[^3]
- **3G + 4G qualification scope:** all plate positions (1G, 2G, 3G, 4G)[^2]

---

## What the textbook doesn't tell you

**Your E6010 root tells the story of your whole test.** If the root is cold at the start, shows excessive convexity (not enough speed), or shows incomplete fusion at the toes (too fast), no amount of perfect fill and cap saves you. The bend test reveals every root flaw that visual inspection misses. Practice roots until the sound, the feel, and the look are automatic.[^4]

**Overhead is the great equalizer.** Welders who look effortless on flat plate struggle desperately overhead. The physical position is uncomfortable, the slag falls on you, and the puddle fights gravity. Overhead SMAW is a skill that takes dedicated practice — you cannot shortcut it. Schedule dedicated overhead time at school before your qualification date.[^4]

**E7018 bead restart is a skill in itself.** When you stop and restart on a fill or cap pass (inevitable on long joints), the restart area is the most defect-prone part of the bead. The restart technique: move the arc back onto the still-hot bead crater, establish the arc, wait for the puddle to form, then resume travel. A cold restart without this technique creates a cold lap or porosity at the restart point.[^4]

**Backing plate weld joint prep is different.** With backing, the root face is not critical because there's no open root to control. The bevel angle is the same (60° included) but the land can be zero to minimal. The fit-up tolerance is more forgiving with backing because the first pass fuses to the backing, not through open space.[^2]

**CSA W47.1 and ASME Section IX qualification scopes differ.** Under W47.1, a 3G open-root test with SMAW does not automatically qualify you for 2G. Under ASME Section IX, it does qualify 1G and 3G only. Know which code your employer uses — your qualification cards must match the production work scope.[^2][^3]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s4-a-groove-positions.svg` — four side-by-side diagrams showing plate orientation and weld direction for 2G, 3G, 4G, and 45° overhead — each with welder position indicated and weld axis arrow)*

*(SVG to be added: `assets/diagrams/p3-s4-a-2g-stringer-pattern.svg` — cross-section of 2G groove showing horizontal stringer bead pattern: E6010 root, then 4-6 stringer fill beads, then cap — each bead numbered and labeled with electrode)*

*(SVG to be added: `assets/diagrams/p3-s4-a-4gf-backing.svg` — cross-section of 4GF groove weld with backing: plate above welder, backing bar at root, E7018 root-to-cap sequence shown — gravity direction arrow)*

---

## Key terms

- **E6010 (E4310):** cellulosic SMAW electrode — DCEP, all-position, penetrating arc, ideal for root passes
- **E7018 (E4918):** low-hydrogen iron-powder SMAW electrode — DCEP/AC, all-position, high mechanical properties
- **4G:** overhead plate position — the plate is above the welder, weld runs horizontally underneath
- **4GF:** overhead plate position with backing — backing bar eliminates open root; "F" = with backing per W47.1
- **3G uphill:** vertical groove weld progressing from bottom to top — standard for structural code work
- **Backing plate:** a strip of steel tacked to the root side of the joint, providing a base for the root weld
- **Interpass temperature:** the base metal temperature between weld passes — must be monitored against minimum and maximum limits
- **Rod oven:** an electrically heated storage box maintaining low-hydrogen electrodes at 120–150 °C
- **Reconditioning:** re-drying wet low-hydrogen electrodes at 260–430 °C — maximum one time per AWS A5.1
- **Keyhole:** the small opening visible at the root of an open-root weld — indicates proper penetration

---

## Common exam trap

- **E6010 must NOT be dried in a rod oven** — this is unique to cellulosic electrodes. E7018 MUST be in a rod oven. Students confuse these requirements.
- **E7018 out-of-oven limit is 4 hours** per AWS A5.1 — not 8 hours, not 24 hours.
- **4GF qualification does NOT qualify for 4G open root.** The "F" (with backing) is a different — and easier — test. A separate open-root test is required for 4G without backing.
- **3G + 4G qualifies ALL plate positions including 2G** under ASME Section IX. Under W47.1, verify the annex — qualification scopes differ between codes.
- **Overhead electrode size maximum is 3/32" (2.4 mm)** for the root pass. Students may attempt 1/8" — the puddle is too large to control overhead.
- **Overhead amperage: REDUCE 15–20% from flat.** The distractor always says "increase" — it never does.

---

## Practice question preview

**Q:** A welder is making the root pass on a 4G (overhead) groove weld in 3/8" mild steel plate using E6010. Which electrode size and amperage combination best represents correct practice for this position?

A) 5/32" (4.0 mm) at 140 A — larger electrode for better penetration overhead  
B) 1/8" (3.2 mm) at 130 A — standard flat-position setting applied to overhead  
C) 3/32" (2.4 mm) at 65 A — small electrode, reduced amperage for puddle control  
D) 3/32" (2.4 mm) at 100 A — maximum heat to ensure root fusion overhead

**Correct: C**

**Explanation:** Overhead SMAW root passes require the smallest practical electrode size (3/32" / 2.4 mm) and reduced amperage (55–75 A range). The surface tension of the molten metal holds the puddle against the overhead joint, but only when the puddle is small. Large electrodes (options A and B) produce too much molten metal for surface tension to hold — the puddle drips. Option D uses 3/32" electrode correctly but at 100 A, the puddle is too fluid and will sag or drip. The correct approach is minimum electrode size + minimum effective amperage for the overhead position.

**Red Seal mapping:** D-13.03 (Sets operating parameters for SMAW equipment), D-13.04 (Performs weld using SMAW equipment)

---

[^1]: [AWS A5.1 — Carbon Steel Electrodes for Shielded Metal Arc Welding](https://pubs.aws.org/p/1085/a51-a51m-2012-specification-for-carbon-steel-electrodes-for-shielded-metal-arc-welding); E6010 (cellulosic, DCEP, 430 MPa), E7018 (low-hydrogen iron-powder, DCEP/AC, 480 MPa), storage requirements (E7018: 120–150°C oven; E6010: no oven), reconditioning at 260–430°C
[^2]: [CSA W47.1 — Certification of Companies for Fusion Welding of Steel](https://www.csagroup.org/store/product/CSA%20W47%3A1/); Annex B (welder qualification matrix — positions, scope, backing vs. open root), 4GF with backing qualification
[^3]: [CSA W59 — Welded Steel Construction (2018)](https://www.csagroup.org/store/product/CSA%20W59%3A18/); Clause 12 (SMAW groove weld positions, qualification scope), acceptance criteria, max interpass 260°C, preheat requirements
[^4]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); E6010 root pass technique, E7018 fill/cap parameters, position-specific amperage reduction (15–20% overhead), restart technique, overhead electrode size limitation (3/32")
[^5]: [Miller Electric — SMAW Electrode Selection and Parameters Guide](https://www.millerwelds.com/resources/article-library/smaw-electrode-guide); E6010 and E7018 amperage tables, drag angle recommendations, overhead safety practices
