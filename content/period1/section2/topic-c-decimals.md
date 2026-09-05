---
id: p1-s2-c
period: 1
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: C
topic_title: Decimals
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to convert fractions to decimals,
  and decimals to fractions to solve practical problems.
objectives:
  - Round decimal fractions to specified place values.
  - Add, subtract, multiply and divide decimal fractions.
  - Convert fractions to decimals.
  - Convert decimal inches and decimal feet, to feet and inch fractions with a practical denominator.
  - Solve decimal fraction calculations.
red_seal_mapping:
  - B-7.02 (Transfers dimensions from drawings to materials)
  - B-8.01 (Prepares materials)
citations:
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 2 Topic C
    ref: pp. 51–56 (trades math — decimals and conversions)
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Appendix A (Math for Welders — decimals, conversions, rounding)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: Miller Electric — Weld Setting Calculators and Reference Tables (public)
    ref: Travel speed, wire feed speed, and heat input calculations use decimal arithmetic
    url: https://www.millerwelds.com/resources/welding-calculators
  - source: Lincoln Electric — Procedure Handbook of Arc Welding (public)
    ref: Section on welding variables — current, voltage, travel speed as decimal values
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
---

# Decimals

Digital calipers read in decimals. Welding calculators give you decimals. CNC plasma tables cut to decimal coordinates. Wire feed speed is in inches-per-minute as a decimal. The world of precision welding and fabrication runs on decimals — but drawings and tape measures often use fractions. You need to translate fluently between both.

---

## Decimal place values — the basics

Decimals extend the number system to the right of the decimal point, with each position representing a power of ten.[^2]

| Position | Name | Value | Example (3.1416) |
|---|---|---|---|
| Ones | 1s | 1 | **3**.1416 |
| Tenths | 0.1 | 1/10 | 3.**1**416 |
| Hundredths | 0.01 | 1/100 | 3.1**4**16 |
| Thousandths | 0.001 | 1/1000 | 3.14**1**6 |
| Ten-thousandths | 0.0001 | 1/10,000 | 3.141**6** |

**Reading decimals correctly:**
- 0.375 = "three hundred seventy-five thousandths"
- 1.25 = "one and twenty-five hundredths"
- NOT "point three seven five" (that's informal — fine in the shop, wrong on an exam that tests terminology)

---

## Rounding decimals

Rounding reduces the precision of a number to a specified place value. The rule:[^2]

- Look at the digit **one place to the RIGHT** of where you're rounding
- If it's **5 or greater:** round UP the digit at your target place
- If it's **4 or less:** keep the digit at your target place (round DOWN = truncate)

**Welding examples:**

| Original value | Round to... | Result | Context |
|---|---|---|---|
| 3.4167 A/mm | Hundredths | 3.42 A/mm | Heat input calculation |
| 0.3125 in | Thousandths | 0.313 in | Caliper reading |
| 12.666... in | Nearest 1/8 in | 12 5/8 in (see conversion below) | Tape measure layout |
| 7.1428 in | Tenths | 7.1 in | Rough cut measurement |

---

## Adding and subtracting decimals

Line up the decimal points, then add or subtract as with whole numbers.[^2]

**Example — travel speed calculation:**
A WPS specifies a travel speed range of 8.5 to 12.0 inches per minute. Your actual measured speed is 10.35 in/min. How far above the minimum are you?

10.35 − 8.50 = **1.85 in/min above the minimum**

**Example — total weld gap:**
Root opening: 0.250 in. Root face: 0.125 in. Land (plate thickness minus prep): 0.375 in. Total plate thickness to confirm: 0.250 + 0.125 + 0.375 = **0.750 in (3/4 in)**

---

## Multiplying decimals

Multiply as whole numbers, then count total decimal places in both factors and insert the decimal in the result.[^2]

**Welding example — wire feed speed and deposition:**
A GMAW setup uses 0.045 in diameter wire at a wire feed speed of 350 in/min. If you increase the wire feed speed by 1.5×, what is the new WFS?

350 × 1.5 = 525.0 in/min

Decimal check: 350 has 0 decimal places; 1.5 has 1 decimal place. Total = 1 place → 5250 → insert 1 decimal place → 525.0 ✓

**New WFS: 525 in/min**[^3]

---

## Dividing decimals

Move the decimal point in the divisor until it becomes a whole number, then move the decimal in the dividend the same number of places.[^2]

**Welding example — cutting speed:**
A plasma cutter is set to cut at 62.5 inches per minute. You need to cut a 500 inch total length of cuts. How many minutes of arc-on time is required?

500 ÷ 62.5 = ?

Move decimal in divisor 1 place right → 625. Move decimal in dividend 1 place right → 5000.

5000 ÷ 625 = **8 minutes** of arc-on time.

---

## Converting fractions to decimals

Divide the numerator by the denominator.[^2]

**The welder's fraction-to-decimal table (memorize these):**

| Fraction | Decimal |
|---|---|
| 1/16 | 0.0625 |
| 1/8 | 0.125 |
| 3/16 | 0.1875 |
| 1/4 | 0.250 |
| 5/16 | 0.3125 |
| 3/8 | 0.375 |
| 7/16 | 0.4375 |
| 1/2 | 0.500 |
| 9/16 | 0.5625 |
| 5/8 | 0.625 |
| 11/16 | 0.6875 |
| 3/4 | 0.750 |
| 7/8 | 0.875 |
| 1 | 1.000 |

**Why you need this table:** A digital caliper reads 0.4375 inches. Your drawing shows 7/16. Are they the same? 7 ÷ 16 = **0.4375 ✓** — yes.[^2]

---

## Converting decimals to fractions (with a practical denominator)

For welding and layout work, "practical denominator" means the denominator you can actually measure on a tape: 2, 4, 8, 16, or 32.

**Method:**

1. Multiply the decimal by the desired denominator (typically 16 or 32)
2. Round the result to the nearest whole number
3. That rounded number is your numerator
4. Simplify if possible

**Example:** Convert 0.625 inches to a fraction with 16ths denominator.

Step 1: 0.625 × 16 = 10.0 (exact)
Step 2: Numerator = 10
Step 3: 10/16
Step 4: Simplify: GCF of 10 and 16 = 2 → **5/8 inch** ✓

**Example:** Convert 0.7 inches to the nearest 16th.

Step 1: 0.7 × 16 = 11.2
Step 2: Round to nearest whole = 11
Step 3: 11/16 inch (already in lowest terms — 11 is prime)

**Answer: 0.7 inches ≈ 11/16 inch** (within 0.0125 in = 1/80 in of the true value — acceptable for most layout work)[^1]

---

## Converting decimal feet to feet-and-inch fractions

This is a real job skill. A computer gives you 7.375 feet. Your tape measure doesn't read decimal feet. You need to convert.[^2]

**Step 1:** The whole number is the feet. → **7 feet**

**Step 2:** The decimal part is the fractional feet. Multiply by 12 to get inches: 0.375 × 12 = **4.5 inches**

**Step 3:** The whole number from step 2 is the inches. → **4 inches**

**Step 4:** Any remaining decimal × 16 to get sixteenths: 0.5 × 16 = **8 sixteenths = 1/2 inch**

**Answer: 7.375 feet = 7 feet 4 1/2 inches**

**Verification:** 7 + 4.5/12 = 7 + 0.375 = 7.375 ft ✓[^2]

---

## Full worked example — heat input calculation

**Scenario:** A Welding Procedure Specification (WPS) limits heat input to 65 kJ/in maximum. Your GMAW setup is running at 185 A, 26 V, travel speed 8.5 in/min. What is your actual heat input?

**Heat input formula:** HI = (Amps × Volts × 60) / Travel Speed (in/min) / 1000 [result in kJ/in][^4]

Step 1: 185 × 26 = 4,810

Step 2: 4,810 × 60 = 288,600

Step 3: 288,600 ÷ 8.5 = 33,953

Step 4: 33,953 ÷ 1000 = **33.95 kJ/in**

**Well within the 65 kJ/in WPS limit.** If you had run at 10 A higher and 1 V higher (195 A, 27 V) at the same travel speed:

195 × 27 × 60 ÷ 8.5 ÷ 1000 = 195 × 27 = 5,265 → × 60 = 315,900 → ÷ 8.5 = 37,165 → ÷ 1000 = **37.2 kJ/in**

Still within the limit. Heat input calculations are always decimal arithmetic.[^4]

---

## Numbers you need to memorize

- **1/16 = 0.0625; 1/8 = 0.125; 1/4 = 0.250; 3/8 = 0.375; 1/2 = 0.500; 5/8 = 0.625; 3/4 = 0.750**[^2]
- **Converting decimal feet to inches:** multiply the decimal fraction by 12[^2]
- **Converting decimal inches to 16ths:** multiply decimal by 16, round to nearest whole, simplify[^2]
- **Rounding rule:** digit to the right of the cut ≥ 5 → round up; < 5 → round down (keep)[^2]
- **Heat input formula: (A × V × 60) / travel speed (in/min) / 1000 = kJ/in**[^4]

---

## What the textbook doesn't tell you

**Digital calipers drift.** A caliper that's been dropped or left open in a steel environment may have a zero error. Always zero your caliper with the jaws closed before measuring, and check it against a known gauge block (or against your steel rule) periodically. A caliper that reads 0.003 in with jaws closed needs its zero reset before every measurement session.[^3]

**The "practical denominator" concept matters in real layout work.** A CNC nesting program outputs coordinates to 4 decimal places. When you convert those to tape-measurable fractions for manual layout (because a part needs to be re-cut by hand), you round to the nearest 1/16 or 1/32. If you round to the nearest 1/4 to make the math easier, you may introduce 0.125 in of error — which is larger than a root opening tolerance. Know what precision your conversion needs.[^1]

**Pocket calculator rounding errors compound.** If you're doing a multi-step calculation and round after every step, you accumulate error. Carry extra decimal places through intermediate steps and round only the final answer to the specified precision.[^2]

---

## Key terms

- **Decimal fraction:** a fraction whose denominator is a power of 10 — expressed using a decimal point (0.375 = 375/1000)
- **Place value:** the value represented by each digit's position relative to the decimal point (tenths, hundredths, thousandths...)
- **Rounding:** reducing precision to a specified place value using the ≥5 round-up rule
- **Practical denominator:** a denominator that can be measured on a standard tape (2, 4, 8, 16, 32)
- **Decimal foot:** feet expressed as a decimal (7.375 ft) rather than feet-and-inches (7' 4 1/2")
- **Heat input:** the energy delivered to the weld per unit length — (A × V × 60) / travel speed / 1000 in kJ/in — controlled by WPS limits

---

## Common exam trap

- **"0.500 in is not the same as 1/2 in"** — wrong. 0.500 = 1/2 exactly. Any value with trailing zeros after the last significant digit is still the same number.
- **Rounding 0.5 — which way?** The standard rule (used by AIT and AWS) is that exactly 0.5 rounds UP. So 3.5 rounds to 4, and 3.45 rounded to tenths rounds to 3.5 (since 5 ≥ 5).
- **Decimal feet conversion:** "Convert 0.75 ft to inches by multiplying by 16" — wrong. Multiply decimal feet by 12 (not 16) to get inches. Multiply decimal inches by 16 to get sixteenths.
- **Heat input units:** "Heat input of 33.95 A·V·min/in" — wrong. After multiplying A × V × 60 / travel speed, divide by 1000 to get kJ/in (not kJ/mm — the formula changes for metric).

---

## Practice question preview

**Q:** A drawing dimension gives a plate edge to be cut at 0.8125 inches from a reference mark. A journeyperson asks for this dimension as a fraction. Which of the following is correct?

A) 3/4 inch  
B) 13/16 inch  
C) 7/8 inch  
D) 25/32 inch  

**Correct: B**

**Explanation:** Convert 0.8125 to a fraction with denominator 16: 0.8125 × 16 = 13.0 (exact). Numerator = 13. Result: 13/16 inch. This is already in simplest form (13 is prime). Option A (3/4 = 0.750) is too small. Option C (7/8 = 0.875) is too large. Option D (25/32 = 0.78125) is a different value. The clean multiplication 0.8125 × 16 = 13.0 confirms the answer exactly.

**Red Seal mapping:** B-7.02 (Transfers dimensions from drawings to materials — converts between decimal and fractional measurements for layout)

---

[^1]: [AIT Welder Curriculum Guide 012 (2026)](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), Period 1 Section 2 Topic C: decimal-to-fraction conversion for tape measure use, practical denominators (16ths, 32nds), decimal foot to feet-and-inches conversion
[^2]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Appendix A "Math for Welders": decimal place values, rounding rules, arithmetic operations with decimals, fraction-to-decimal conversion table, worked examples
[^3]: [Miller Electric — Weld Setting Calculators](https://www.millerwelds.com/resources/welding-calculators), wire feed speed calculations, travel speed, decimal arithmetic in welding parameter setting; caliper zeroing notes
[^4]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook), heat input formula (A × V × 60 / travel speed / 1000 = kJ/in), WPS heat input limits, welding variable calculations with decimal arithmetic
