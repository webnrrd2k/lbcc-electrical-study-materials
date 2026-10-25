# Study Guide: Polar & Rectangular Form Practice Problems

Oct 22, 2026 · @Jeff

## Why Polar and Rectangular Form Matter

Every AC quantity you've worked with since Unit 14 has a **size and an angle**: a voltage at 30°, a current lagging 53°, an impedance of 12 Ω resistance plus 16 Ω reactance. Polar and rectangular form are two ways to write those quantities as single numbers so you can do Ohm's law and Kirchhoff's laws on them directly, without drawing a triangle every time.

- **Rectangular (a + jb):** "how far across, how far up." Best for **adding and subtracting**.
- **Polar (M∠θ):** "how big, which direction." Best for **multiplying and dividing**.

**The two worksheets**

| Worksheet | Problems | Skill |
| --- | --- | --- |
| No. 4, Polar ↔ Rectangular Conversion | 24 | Q1–12: polar to rectangular. Q13–24: rectangular to polar. |
| No. 5, Add / Subtract / Multiply / Divide | 36 | Q1–15: sums and differences (answers in polar). Q16–26: products. Q27–36: quotients. |

**Why electricians care:** an impedance like 12 + j16 Ω is the R-L series circuit from Unit 17 written as one number. In polar it's 20∠ 53.13°: Z = 20 Ω and θ = 53.13°. Divide a voltage by it in polar and you get the current *and* its phase angle in one step. Later units on three-phase and complex circuits rely on this.

**How to use this guide:** learn the notation, practice the two conversions until they're automatic (everything else depends on them), then do the arithmetic sections. Check your work against the answer keys.

## Notation: j, Rectangular and Polar

**Intuition:** picture a vector on a graph. Rectangular form gives its **x and y coordinates**. Polar form gives its **length and angle**. They describe the same arrow.

**Rectangular form: a + jb**

- **a** is the **real** part, the horizontal (x) component. In circuits it's the resistive or in-phase part.
- **b** is the **imaginary** or **j** part, the vertical (y) component. In circuits it's the reactive part.
- **j** marks the vertical axis. It means "rotated 90° counterclockwise." Mathematically, j = √(−1), so **j² = −1**. Electricians use j instead of i because i already means current.
- +j points up (inductive: +jXₗ). −j points down (capacitive: −jXᶜ).

**Polar form: M ∠ θ**

- **M** is the magnitude (length), always positive.
- **θ** is the angle, measured **counterclockwise from the positive real axis (0°)**. Negative angles go clockwise.
- The same direction can be written two ways: −90° = 270°, and −190° = 170° (add or subtract 360°).

**The four quadrants (this is where most mistakes happen)**

| Quadrant | Sign of a | Sign of b | Angle range |
| --- | --- | --- | --- |
| I | + | + | 0° to 90° |
| II | − | + | 90° to 180° |
| III | − | − | 180° to 270° (or −180° to −90°) |
| IV | + | − | 270° to 360° (or −90° to 0°) |

**Habit that prevents most errors:** before calculating, look at the signs of a and b, name the quadrant, and estimate the angle. Then check that your answer lands there.

**Electrical examples**

| Rectangular | Polar | Meaning |
| --- | --- | --- |
| 12 + j16 Ω | 20 ∠ 53.13° Ω | R-L series impedance (lagging) |
| 12 − j16 Ω | 20 ∠ −53.13° Ω | R-C series impedance (leading) |
| 0 + j10 | 10 ∠ 90° | Pure inductive reactance |
| 0 − j10 | 10 ∠ −90° | Pure capacitive reactance |
| 120 + j0 | 120 ∠ 0° | Reference voltage |

## Converting Between Forms (Worksheet No. 4)

### Polar to rectangular (Q1–12)

It's the Unit 14 trig: the real part is the adjacent side and the j part is the opposite side.

```math
a = M\cos\theta \qquad b = M\sin\theta
```

**Example (Q1): 12.3 ∠ 30°**

- a = 12.3 × cos 30° = 10.65
- b = 12.3 × sin 30° = 6.15
- Answer: **10.65 + j6.15**

**The good news:** in this direction, cos and sin give the **signs automatically** for any angle. Q2 (53 ∠ 160°) gives −49.80 + j18.13 with no extra thought. Just type the angle exactly as written, including the minus sign.

**Spot checks:** Q9–12 use the same 50 at 36°, −36°, 126° and 216°. They give the same two numbers (40.45 and 29.39) with different signs, and Q11 even swaps their order. They're a great drill on quadrants.

### Rectangular to polar (Q13–24)

```math
M = \sqrt{a^2 + b^2} \qquad \theta = \tan^{-1}\left(\frac{b}{a}\right)\ \text{(then fix the quadrant)}
```

**The quadrant trap:** tan⁻¹ on a calculator only returns angles between −90° and +90° (quadrants I and IV). It **can't tell** (−25, −5) from (25, 5), because b/a is the same.

**Fix:** if **a is negative**, add 180° to the calculator's answer. If that puts you over 180°, subtract 360° to get the equivalent negative angle.

**Example (Q17): −12 + j16**

- M = √(144 + 256) = **20**
- The calculator gives tan⁻¹(16 / −12) = −53.13°. **Wrong quadrant.**
- a is negative, so add 180°: −53.13 + 180 = **126.87°**. That's quadrant II (−, +) ✓.
- Answer: **20 ∠ 126.87°**.

**Problems on this sheet where the plain calculator answer is wrong:** Q14, Q15, Q17, Q19, Q23 and Q24. All have a negative real part.

**Shortcut:** most scientific calculators have **R→P** and **P→R** (or Pol( and Rec() functions that handle the quadrant for you. Learn yours, but also learn the manual method for when you have to show work.

## Adding and Subtracting (Worksheet No. 5, Q1–15)

**Rule: add and subtract in RECTANGULAR form.** It's the component method from Unit 14: add the across parts together and the up parts together.

```math
(a_1 + jb_1) \pm (a_2 + jb_2) = (a_1 \pm a_2) + j(b_1 \pm b_2)
```

**Never add polar magnitudes or angles directly.** 17∠45° + 22∠70° is **not** 39∠115°.

**Procedure**

1. Convert any polar terms to rectangular (P→R).
2. Add or subtract the real parts. Add or subtract the j parts.
3. Convert the result back to polar (R→P). Fix the quadrant!

**Example (Q1): 17∠45° + 22∠70°**

- 17∠45° = 12.02 + j12.02
- 22∠70° = 7.52 + j20.67
- Sum = 19.55 + j32.69, which is **38.09∠ 59.13°**.
- Sanity check: the answer's angle (59°) sits between 45° and 70°, and its magnitude is less than 17 + 22 = 39, because the vectors don't point the same way.

**Subtraction tip:** subtracting a vector is adding its opposite. Distribute the minus sign to **both** parts: −(2 − j8) = −2 **+** j8. Dropping the sign on the j part is the classic error (Q12, Q14, Q15).

**Problems designed to come out clean** (use them to check your method):

- **Q9:** 10∠53.1° is 6 + j8, so the sum = 10 + j10 = **14.14∠ 45°**.
- **Q12:** 2.83∠45° is 2 + j2, so 2 + j2 − 2 + j8 = 0 + j10 = **10∠ 90°**.
- **Q13:** 7.07∠135° is −5 + j5, so the difference is **0**. Your calculator may show a tiny leftover like 0.001 from rounding; treat it as zero.
- **Q14:** (2 − j10) − (1 − j10) = **1 + j0 = 1∠ 0°**. The j parts cancel.

**Watch the signs in Q5–8:** Q7 subtracts 41∠**+57°**, while Q3 added 41∠**−57°**. Read each angle's sign carefully.

## Multiplying and Dividing (Worksheet No. 5, Q16–36)

**Rule: multiply and divide in POLAR form.**

```math
M_1\angle\theta_1 \times M_2\angle\theta_2 = (M_1 M_2)\angle(\theta_1 + \theta_2)
```

```math
M_1\angle\theta_1 \div M_2\angle\theta_2 = (M_1 / M_2)\angle(\theta_1 - \theta_2)
```

- **Multiply:** multiply the magnitudes and **add** the angles.
- **Divide:** divide the magnitudes and **subtract** the angles (top minus bottom).

**Intuition:** multiplying by a vector stretches by its length and rotates by its angle. Dividing undoes that: it shrinks and rotates back.

**Example (Q16): 17∠45° × 22∠70°** = (17 × 22)∠(45 + 70) = **374∠115°**.

**Example (Q30): 84∠−64° ÷ 19∠120°** = 4.421∠(−64 − 120) = 4.421∠−184° = **4.421∠176°** (add 360° to bring it into range).

**Problems given in rectangular form (Q20–22, 25, 26, 31–33, 36)**

- **Method A (recommended):** convert each to polar, multiply or divide, and convert back if needed.
- **Method B (multiply directly):** FOIL, then use **j² = −1**. Example (Q26): (j1.63)(2.6 + j1) = j4.238 + j²1.63 = **−1.63 + j4.238**.
- **Method C (divide directly):** multiply the top and bottom by the **conjugate** of the bottom (flip the sign of its j part), which makes the bottom a real number. Example (Q36): (−10 + j20) / (2 − j1) × (2 + j1)/(2 + j1) = (−20 − j10 + j40 + j²20) / (4 + 1) = (−40 + j30) / 5 = **−8 + j6 = 10∠143.13°**.

**Mixed-form problems (Q24, Q34, Q35):** convert the rectangular term to polar first, then multiply or divide in polar.

**Problems designed to come out clean:** Q31 gives **5∠45°**, Q32 gives **≈ 6∠ 0° (5.99)**, Q33 gives **2∠125°**, and Q36 gives **10∠143.13°**. If you get these, your method is right.

**Electrical meaning:** this is AC Ohm's law. **I = E / Z** (divide) and **E = I × Z** (multiply). For example, 120∠0° V ÷ 20∠53.13° Ω = 6∠−53.13° A: 6 amps, lagging 53.13°, in one step.

## Answer Keys

Rounded to 4 significant figures, with angles to 0.01°. Small last-digit differences from rounding are fine. Angles are given between −180° and +180°; an equivalent angle (±360°) is also correct.

### Worksheet No. 4: Polar → Rectangular

| Q | Given | Answer |
| --- | --- | --- |
| 1 | 12.3∠30° | 10.65 + j6.15 |
| 2 | 53∠160° | −49.80 + j18.13 |
| 3 | 25∠−45° | 17.68 − j17.68 |
| 4 | 86∠−115° | −36.35 − j77.94 |
| 5 | 0.05∠−20° | 0.04698 − j0.0171 |
| 6 | 0.003∠80° | 0.000521 + j0.002954 |
| 7 | 0.013∠260° | −0.002257 − j0.0128 |
| 8 | 0.156∠−190° | −0.1536 + j0.02709 |
| 9 | 50∠36° | 40.45 + j29.39 |
| 10 | 50∠−36° | 40.45 − j29.39 |
| 11 | 50∠126° | −29.39 + j40.45 |
| 12 | 50∠216° | −40.45 − j29.39 |

### Worksheet No. 4: Rectangular → Polar

| Q | Given | Answer | Plain tan⁻¹ gives |
| --- | --- | --- | --- |
| 13 | 25 + j25 | 35.36∠45° | 45° ✓ |
| 14 | −25 − j5 | 25.50∠−168.69° | 11.31° ✗ |
| 15 | −25 + j5 | 25.50∠168.69° | −11.31° ✗ |
| 16 | 25 − j5 | 25.50∠−11.31° | −11.31° ✓ |
| 17 | −12 + j16 | 20∠126.87° | −53.13° ✗ |
| 18 | 2 − j4 | 4.472∠−63.43° | −63.43° ✓ |
| 19 | −59 − j25 | 64.08∠−157.04° | 22.96° ✗ |
| 20 | 700 + j200 | 728.0∠15.95° | 15.95° ✓ |
| 21 | 0.045 − j0.153 | 0.1595∠−73.61° | −73.61° ✓ |
| 22 | 0.0171 + j0.047 | 0.0500∠70.01° | 70.01° ✓ |
| 23 | −69.4 − j40 | 80.10∠−150.04° | 29.96° ✗ |
| 24 | −2 + j2 | 2.828∠135° | −45° ✗ |

### Worksheet No. 5: Sums and differences (Q1–15)

| Q | Polar answer | Rectangular |
| --- | --- | --- |
| 1 | 38.09∠59.13° | 19.55 + j32.69 |
| 2 | 118.6∠46.03° | 82.36 + j85.38 |
| 3 | 133.8∠−37.99° | 105.5 − j82.39 |
| 4 | 65.06∠−65.17° | 27.32 − j59.04 |
| 5 | 9.751∠−62.54° | 4.496 − j8.652 |
| 6 | 208.3∠91.01° | −3.678 + j208.3 |
| 7 | 102.4∠−53.57° | 60.81 − j82.39 |
| 8 | 103.0∠−63.26° | 46.32 − j91.95 |
| 9 | 14.14∠45° | 10 + j10 |
| 10 | 11.31∠45° | 8 + j8 |
| 11 | 2.828∠−135° | −2 − j2 |
| 12 | 10∠90° | 0 + j10 |
| 13 | ≈ 0 | ≈ 0 (rounding leftovers) |
| 14 | 1∠0° | 1 + j0 |
| 15 | 10.20∠78.68° | 2 + j10 |

### Worksheet No. 5: Products (Q16–26)

| Q | Polar answer | Rectangular |
| --- | --- | --- |
| 16 | 374∠115° | −158.1 + j339.0 |
| 17 | 11,400∠20° | 10,712 + j3,899 |
| 18 | 3,936∠−87° | 206.0 − j3,931 |
| 19 | 1,596∠56° | 892.5 + j1,323 |
| 20 | 45.18∠177.15° | −45.12 + j2.25 |
| 21 | 26.25∠−42.51° | 19.35 − j17.74 |
| 22 | 506.4∠29.85° | 439.2 + j252.0 |
| 23 | 6∠−25° | 5.438 − j2.536 |
| 24 | 113.8∠92.57° | −5.095 + j113.7 |
| 25 | 15.69∠19.82° | 14.76 + j5.32 |
| 26 | 4.541∠111.04° | −1.63 + j4.238 |

### Worksheet No. 5: Quotients (Q27–36)

| Q | Polar answer | Rectangular |
| --- | --- | --- |
| 27 | 0.7727∠−25° | 0.7003 − j0.3266 |
| 28 | 2.08∠130° | −1.337 + j1.593 |
| 29 | 2.341∠27° | 2.086 + j1.063 |
| 30 | 4.421∠176° | −4.410 + j0.3084 |
| 31 | 5.00∠45° | 3.54 + j3.54 |
| 32 | 5.99∠0° | 5.99 + j0 |
| 33 | 2.00∠125° | −1.148 + j1.639 |
| 34 | 3.077∠−14.57° | 2.978 − j0.774 |
| 35 | 1.414∠−35° | 1.158 − j0.811 |
| 36 | 10∠143.13° | −8 + j6 |

## Mistakes to Avoid and Calculator Tips

1. **Wrong quadrant on R→P.** If the real part is negative, add 180° to the calculator's tan⁻¹ answer. Six problems on Worksheet 4 test this.
2. **Adding in polar.** You can't add magnitudes or angles. Convert to rectangular first.
3. **Multiplying in rectangular without FOIL.** (a + jb)(c + jd) is **not** ac + jbd. Either FOIL with j² = −1, or convert to polar.
4. **Dividing angles instead of subtracting them.** Divide the magnitudes; **subtract** the angles (top minus bottom).
5. **Losing the minus sign on the j part when subtracting.** −(1 − j6) = −1 + j6.
6. **Not simplifying the angle.** −184° should be written as 176°. Either is mathematically correct, but most keys use −180° to +180°.
7. **Calculator in RAD mode.** Every trig result will be wrong. Check for DEG.
8. **Rounding too early.** Carry full precision through multi-step problems (convert, add, convert back), and round only the final answer.
9. **Tiny values (Q5–8, Q21–22 on Worksheet 4).** Keep enough digits. 0.003∠80° gives a real part of 0.000521; don't round it to 0.
10. **Treating rounding leftovers as real answers.** Q13 on Worksheet 5 is essentially zero. A result like 0.001∠135° is just rounding noise from 7.07 ≈ 5√2.

**Calculator tips**

- Learn your calculator's **Pol( / Rec(** or **R→P / P→R** keys. They handle the quadrant automatically. On TI-30 and Casio fx models, they're usually 2nd-function keys. Check where your model stores the two results.
- Many scientific calculators (Casio fx-115/991, TI-36X Pro) have a **complex mode** (CMPLX) that adds, multiplies and divides a + bi and r∠θ directly. Great for checking, but learn the manual steps for tests.
- **Quick check:** after any operation, convert your answer back and see if it still makes sense (quadrant, rough size).

## Formula Sheet

| Task | Formula | Best form |
| --- | --- | --- |
| Polar → rectangular | a = M cos θ, b = M sin θ | — |
| Rectangular → polar | M = √(a² + b²), θ = tan⁻¹(b/a), **+180° if a < 0** | — |
| Add / subtract | (a₁ ± a₂) + j(b₁ ± b₂) | Rectangular |
| Multiply | (M₁M₂)∠(θ₁ + θ₂) | Polar |
| Divide | (M₁/M₂)∠(θ₁ − θ₂) | Polar |
| j facts | j = √(−1), j² = −1, +j = 90°, −j = −90° | — |
| Conjugate | of a + jb is a − jb; (a + jb)(a − jb) = a² + b² | Used to divide in rectangular |

**Memory aid:** "**R**ectangular for **A**dding, **P**olar for **P**roducts."

**Circuit connections**

| Circuit idea | Complex form |
| --- | --- |
| Series impedance | Z = R + jXₗ − jXᶜ = R + j(Xₗ − Xᶜ) (add in rectangular) |
| Polar impedance | Z∠θ where θ is the circuit phase angle, and cos θ = PF |
| Ohm's law | I = E/Z and E = I × Z (divide and multiply in polar) |
| Lagging vs leading | +θ on Z (inductive) gives current at −θ (lagging). −θ on Z gives current at +θ (leading). |
