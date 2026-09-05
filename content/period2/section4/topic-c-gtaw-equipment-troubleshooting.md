---
id: p2-s4-c
period: 2
section: 4
section_title: Gas Tungsten Arc Welding (GTAW)
topic_letter: C
topic_title: GTAW Equipment Maintenance and Troubleshooting
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to troubleshoot and maintain GTAW equipment.
objectives:
  - Describe the set up and maintenance of GTAW equipment.
  - Determine and solve power source output current problems.
  - Determine and solve GTAW torch and cable assembly problems.
  - Determine and solve shielding gas coverage problems.
red_seal_mapping:
  - A-1.04 (Maintains welding equipment)
  - D-15.02 (Sets up GTAW equipment)
  - D-15.03 (Sets operating parameters for GTAW)
citations:
  - source: Miller Electric — GTAW Troubleshooting Guide
    ref: Contaminated tungsten causes, arc instability, gas coverage troubleshooting, torch component maintenance
    url: https://www.millerwelds.com/resources/article-library/tig-welding-troubleshooting
  - source: Lincoln Electric — GTAW Equipment Setup and Maintenance
    ref: Power source output current, HF settings, torch cable inspection, gas line leak check
    url: https://www.lincolnelectric.com/en/education-center/welding-education/tig-welding
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 13 — GTAW troubleshooting; defect causes, torch maintenance, gas system checks
    url: https://www.g-w.com/modern-welding
  - source: CSA W117.2 — Safety in Welding, Cutting, and Allied Processes (2019)
    ref: Electrical safety for GTAW, HF interference precautions, torch cable insulation inspection
    url: https://www.csagroup.org/store/product/CSA%20W117.2/
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 4 Topic C
    ref: pp. 58–60
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# GTAW Equipment Maintenance and Troubleshooting

GTAW is the most contamination-sensitive arc process. A dirty tungsten, a cracked gas cup, a kinked torch cable, or an air leak in the gas line will kill the weld quality immediately. Unlike SMAW or FCAW where problems often reveal themselves gradually, GTAW quality problems are instant and obvious — porosity, black smoke, tungsten inclusions. The payoff: when GTAW troubleshooting logic is applied systematically, you can diagnose and fix any problem in under five minutes.

---

## GTAW workstation setup checklist

A systematic setup prevents 90% of GTAW problems.[^1][^2]

### Pre-weld checklist:

1. **Power source:**
   - Confirm output type (DCEN for steel/stainless; AC for aluminum)
   - Confirm amperage range appropriate for material thickness
   - For AC: confirm balance control is set (more EN for penetration; more EP for cleaning)
   - HF: confirm HF is set to "Start" (not "Continuous") for DC; "Continuous" for AC aluminum
2. **Gas system:**
   - Verify cylinder has sufficient gas (not expired)
   - Open cylinder valve fully (all the way) — back off ¼ turn to reseat for regulator seal
   - Set flow rate at regulator/flow meter: 8–15 L/min for most steel; 10–18 L/min for aluminum (larger cup)
   - Purge the gas hose briefly before welding — condensation in cold hose can contaminate
3. **Torch assembly:**
   - Select correct tungsten type and diameter for the current type and amperage
   - Verify collet is correct size for tungsten diameter (a collet one size too large = loose tungsten = arc wander)
   - Inspect gas cup for cracks — a cracked cup causes turbulent gas and porosity
   - Ensure gas lens is installed if using (recommended for critical work)
   - Confirm tungsten stick-out: 3–6 mm beyond cup
   - Check torch body for cracked insulation or damaged o-rings — replace if found
4. **Work clamp:**
   - Attach close to the weld zone — long work leads increase resistance and arc instability
   - Ensure clean metal contact — paint, rust, or oxide at the clamp causes arc instability
5. **Filler rod:**
   - Select correct classification and diameter
   - Wipe end with acetone or clean cloth — do NOT touch the end with bare fingers

---

## Power source troubleshooting

### Problem: Arc won't start or starts erratically

| Symptom | Likely cause | Fix |
|---|---|---|
| No arc at all | Machine not powered; gas pressure zero; bad work lead connection | Check power switch, gas cylinder, clamp connection |
| Arc starts but immediately extinguishes | Amperage set too low; tungsten contaminated | Increase amps; regrind tungsten |
| HF sparks but no arc established | Tungsten-to-work gap too large (HF spark can't bridge it) | Reduce gap to 2–4 mm; ensure tungsten is properly positioned |
| Arc unstable, wandering | Contaminated tungsten; wrong tungsten type for current; work clamp on paint or oxide | Regrind tungsten; verify tungsten type; move clamp to clean metal |

### Problem: Incorrect or unstable output current

| Symptom | Likely cause | Fix |
|---|---|---|
| Amperage doesn't match dial setting | Worn foot pedal potentiometer; loose connection inside pedal | Test pedal range with ammeter; service or replace pedal |
| No response from foot pedal | Cable connector not fully seated at machine; broken pedal cable | Check connector; inspect cable for damage |
| Machine trips breaker at high amperage | Overloaded circuit; duty cycle exceeded; cooling fan failure | Reduce amperage or rest duration; check fan rotation; verify circuit breaker amperage |
| AC output unbalanced (weld not cleaning aluminum) | AC balance control set too far toward EN | Increase EP percentage (more cleaning); test arc on scrap aluminum and observe cleaning action |

---

## Torch and cable troubleshooting

### Problem: Tungsten contamination

**What it looks like:** Tungsten tip darkens, oxidizes, or develops irregular shape. Weld pool shows black smoke, sparks, or a black deposit on the weld surface. If tungsten contacts the pool, a tungsten inclusion is produced.

| Cause | Fix |
|---|---|
| Arc length too short → tungsten dips into puddle | Increase arc length; practice maintaining consistent distance |
| Tungsten contacts filler rod end | Keep filler angle low (15°) and dip smoothly at puddle edge only |
| Shielding gas not flowing when arc starts → tungsten oxidizes instantly | Check post-flow delay; purge gas line before welding |
| Wrong tungsten type for current (e.g., EWP on DCEN) | Select correct tungsten type; replace and regrind |
| Contaminated filler rod touches tungsten | Clean filler rod end; maintain proper rod angle |

**Once contaminated:** Stop welding. Remove tungsten. If contamination is at the tip only, break off the tip (snap off with pliers) or re-grind. If contamination extends into the tungsten body, replace it.

### Problem: Tungsten inclusions in the weld

**Cause:** Tungsten entered the molten pool (from tungsten contact with the puddle, or tungsten ball falling off during AC operation)[^1]

**Detection:** Radiographic testing (X-ray) shows bright white irregular inclusions (tungsten is very dense, absorbs more X-ray). Not detectable visually.

**Repair:** Grind out the affected area completely. Verify tungsten condition and proper technique before re-welding. Document per your WPS.

### Problem: Torch overheating

**Cause:** Amperage exceeding torch rating; torch duty cycle exceeded; blocked cooling (water-cooled torch with insufficient water flow)

**Fix:** 
- For air-cooled torches: verify amperage is within torch's continuous rating
- For water-cooled torches: verify water cooler is running and flow is adequate; check for kinked hose
- Allow torch to rest between runs to stay within duty cycle

### Problem: Loose tungsten in collet

**Symptom:** Tungsten slips into the cup during welding; inconsistent arc starting

**Cause:** Wrong collet size for tungsten; collet worn or corroded; back cap not tightened

**Fix:** Match collet size exactly to tungsten diameter. Replace worn collet (collets are consumables). Ensure back cap is finger-tight + ¼ turn.

---

## Shielding gas coverage troubleshooting

Gas coverage problems produce immediate, visible porosity — the gas is not protecting the pool from atmosphere.

### Problem: Porosity in weld (small surface pores, or subsurface pores on X-ray)

| Cause | Diagnosis | Fix |
|---|---|---|
| **Air leak in gas line** | Listen for hiss; soapstone-water leak test on fittings | Re-torque fittings; replace o-ring; inspect hose for cracks |
| **Gas cup cracked** | Visible crack or chip on ceramic cup | Replace cup |
| **Flow rate too low** | Less than 8 L/min for steel | Increase to 8–15 L/min; verify rotameter reading |
| **Flow rate too high (turbulence)** | Greater than 25 L/min (argon) — induces turbulence, draws air in | Reduce to 15 L/min; install gas lens for smoother flow |
| **Contaminated gas (moisture or oxygen)** | Porosity appears even with proper flow | Replace gas cylinder; verify grade (must be ≥99.995% purity) |
| **Drafts/wind** | Arc visible; weld pool disturbed by air movement | Shield the weld area; use windscreen |
| **No post-flow protection** | Weld discolors (straw, blue, black) as it cools | Set post-flow time 8–15 seconds to protect cooling tungsten and weld |
| **Gas hose too cold (condensation)** | First welds of cold morning show porosity, then improve | Purge gas hose for 15–30 seconds before first weld; allow machine to warm up |

### Problem: Excessive tungsten oxidation (darkening) at startup

**Cause:** Shielding gas not flowing at arc start — a delay between gas valve opening and arc start

**Fix:** 
- Use a pre-flow delay: modern GTAW machines have a pre-flow setting (typically 0.2–0.5 seconds) — gas flows before the arc starts
- After a long pause, purge the torch by pressing the torch switch briefly (without striking arc) to clear the hose
- Never try to strike the arc immediately after a long stop — the line may have air in it

### Straw vs blue vs black discoloration on stainless steel

Stainless steel GTAW passes show heat tint colours that indicate atmospheric contamination levels:

| Colour | Severity | Cause | Acceptability |
|---|---|---|---|
| **Silver/bright** | None | Full argon coverage during cooling | Acceptable |
| **Golden/straw** | Minimal | Slight air infiltration at edge of shield | Acceptable per some codes (verify) |
| **Light blue** | Moderate | Reduced gas coverage | May be rejected — verify with code |
| **Dark blue/purple** | Significant | Poor coverage | Typically rejected; clean and assess |
| **Black** | Severe | No gas coverage | Always rejected; grind back and re-weld |

---

## Numbers you need to memorize

- **GTAW gas flow rate (standard):** 8–15 L/min argon[^1][^2]
- **Post-flow time:** 8–15 seconds after arc extinction[^1]
- **Pre-flow time:** 0.2–0.5 seconds before arc starts[^1]
- **Tungsten stick-out:** 3–6 mm beyond cup end[^1]
- **Collet must match tungsten diameter** exactly — loose collet = arc wander[^1]
- **Gas purity minimum:** 99.995% argon (Grade 4.5)[^1]
- **Contaminated tungsten:** stop, remove, regrind or replace — never continue through a contamination event[^1]
- **Black discoloration on stainless:** always rejected — indicates zero gas coverage during cooling[^1]

---

## What the textbook doesn't tell you

**Post-flow is as important as pre-flow.** When the arc extinguishes, the tungsten is still at ~2000°C and the weld pool is still liquid. The shielding gas must continue flowing until the tungsten is below ~300°C (8–15 seconds depending on amperage and tungsten diameter). Stopping gas immediately on arc stop produces a blue-black oxidized tungsten that must be re-ground before the next arc start. This is the most commonly skipped step in routine TIG work.

**The gas lens turns a good welder into an excellent one.** Standard collet bodies produce a turbulent annular gas stream that's adequate at short cup-to-work distances. Extend your arc slightly (for better puddle visibility) and the coverage breaks down. With a gas lens, the flow is laminar and extends predictably 2–3× farther. On aluminum, where you need to see the puddle clearly and work with a larger arc gap for AC cathodic cleaning, a gas lens isn't optional — it's essential.

**Cracked collet bodies cause air aspiration.** A collet body with a hairline crack — common in shops where torches are dropped regularly — allows air to be pulled in by the venturi effect of the gas flowing past the crack. The weld produces porosity that looks exactly like a low-flow-rate problem, except increasing flow makes it worse (more aspiration). If you've checked everything else, replace the collet body.

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s4-c-gtaw-setup.svg` — schematic of complete GTAW workstation showing: power source → torch cable → torch body → collet body → collet → gas lens (optional) → cup → tungsten; work lead from power source to workpiece; gas cylinder → regulator → hose → torch gas inlet; foot pedal connection to power source.)*

*(SVG to be added: `assets/diagrams/p2-s4-c-stainless-discoloration.svg` — stainless steel weld strip showing colour bands from centre outward: silver/bright → straw → light blue → dark blue/purple → black; each band labeled with acceptability.)*

---

## Key terms

- **Pre-flow:** gas flow before arc strike — purges air from torch and protects tungsten at arc start
- **Post-flow:** gas flow continuing after arc extinction — protects tungsten and hot weld pool during cooling
- **Tungsten inclusion:** fragment of tungsten electrode that entered the molten weld pool; a subsurface defect detectable by X-ray
- **Air aspiration:** drawing of air into the shielding gas stream through cracks, loose fittings, or turbulence; causes porosity
- **Gas lens:** screen insert in torch collet body that converts turbulent to laminar argon flow; extends effective shielding zone
- **Duty cycle:** percentage of a 10-minute period that the torch/machine can operate at rated amperage without overheating
- **Collet:** precision-machined split tube that grips tungsten; must match tungsten diameter exactly
- **Heat tint:** oxidation colour on stainless steel surface indicating temperature and atmospheric exposure during cooling
- **Porosity:** gas pores (holes) in the weld metal caused by atmospheric contamination (nitrogen, oxygen, moisture)
- **Arc wander:** unstable arc that shifts position during welding; caused by contaminated or improperly ground tungsten, or loose collet
- **HF (High Frequency):** high-voltage, high-frequency spark used to start the GTAW arc without contact; can interfere with electronics

---

## Common exam trap

- **Post-flow is required — stopping gas at arc extinction overheats and oxidizes the tungsten**. Exam may describe stopping gas immediately as "correct procedure to save gas."
- **Porosity from too-HIGH gas flow is possible** — turbulent flow aspirates air. Not just too-low flow. This counterintuitive point is tested.
- **Tungsten inclusions are NOT visible on the surface** — they are subsurface. Only X-ray or UT can reliably detect them. Exam may suggest visual inspection detects tungsten inclusions. It doesn't.
- **A cracked collet body causes porosity** — not just loose tungsten. The mechanism (air aspiration through the crack) is the specific exam point.
- **Black stainless discoloration = always rejected**. Straw may be accepted by some codes. Know the spectrum and that black is never OK.

---

## Practice question preview

**Q:** A welder performing GTAW on stainless steel notices porosity on the first few welds of the morning but the welds improve as the session continues. What is the MOST likely cause?

A) The tungsten is contaminated from the previous session
B) The amperage is too high, evaporating the shielding gas
C) Moisture condensation in the cold gas hose is being driven out as the line warms up
D) The gas pressure regulator needs to be recalibrated

**Correct: C**

**Explanation:** Moisture condensing in a cold gas hose during overnight shutdown is a classic cause of porosity at the start of a welding session. As the gas flows and the hose warms up, the condensation is swept through and out of the system — porosity disappears once the hose is clear and warm. The fix is to purge the hose for 15–30 seconds before beginning the first weld of the day. (A) Contaminated tungsten would produce consistent problems throughout the session, not just at the beginning. (B) High amperage doesn't evaporate shielding gas. (D) Regulator calibration doesn't affect in-session moisture in the hose.

**Red Seal mapping:** A-1.04 (Maintains welding equipment); D-15.02 (Sets up GTAW equipment)

---

[^1]: [Miller Electric — GTAW Troubleshooting Guide](https://www.millerwelds.com/resources/article-library/tig-welding-troubleshooting); contaminated tungsten causes, arc instability, gas coverage troubleshooting, torch component maintenance, post-flow requirements, gas lens benefits
[^2]: [Lincoln Electric — GTAW Equipment Setup and Maintenance](https://www.lincolnelectric.com/en/education-center/welding-education/tig-welding); power source output troubleshooting, HF settings, torch cable inspection, gas line leak check, pre-flow and post-flow settings
[^3]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 13 — GTAW troubleshooting; defect causes and solutions, torch maintenance, gas system checks
[^4]: [CSA W117.2:19 — Safety in Welding, Cutting, and Allied Processes](https://www.csagroup.org/store/product/CSA%20W117.2/); torch cable insulation inspection requirements, HF interference precautions
[^5]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 4 Topic C](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 58–60
