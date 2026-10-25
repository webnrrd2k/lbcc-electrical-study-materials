# Unit 14 Study Guide: Basic Trigonometry and Vectors

Oct 22, 2026 · @Jeff

## Why this chapter exists

In DC, volts × amps = watts. In AC that stops being true, because voltage and current don't always peak at the same moment. A coil (motor, transformer, ballast) makes current lag voltage. A capacitor makes it lead. Ideal pure inductance or capacitance gives a 90° shift. Real loads land somewhere between 0° and 90°.

Two quantities that are 90° apart can't just be added. They combine like the two legs of a right triangle. Almost every AC triangle you'll use later works this way:

| Triangle | Hypotenuse | Horizontal leg | Vertical leg | Angle θ |
| --- | --- | --- | --- | --- |
| Impedance | Z (ohms) | R | X (reactance) | phase angle |
| Power | VA (apparent) | W (true) | VAR (reactive) | cos θ = power factor |
| Series voltages | E applied | E\_R | E\_L or E\_C | phase angle |

This chapter is the toolkit for all of those. If it clicks now, Units 15 onward get much easier.

## 14–1 Right Triangles

**Intuition:** A right triangle is the shape you get from "go this far across, then this far up." Its long side is the shortcut, the straight-line distance.

**Definitions**

- **Right angle:** exactly 90°, usually marked with a small square in the corner.
- **Right triangle:** a triangle with one 90° angle.
- **Hypotenuse:** the side across from the 90° angle. It's always the longest side.
- **Legs:** the other two sides, which form the 90° corner.

**Key facts**

- The three angles of any triangle add up to 180°.
- In a right triangle, the two non-right angles therefore add up to 90°. If you know one, the other is 90° − that angle. (Review Q10 is just this.)

**Pitfalls**

- Don't find the hypotenuse by which side is drawn slanted. Find the 90° corner and take the side directly across from it.
- If your answer for a leg comes out longer than the hypotenuse, you made a mistake. Check this every time.

## 14–2 The Pythagorean Theorem

**Intuition:** If you walk 3 ft east and then 4 ft north, you end up 5 ft from where you started, not 7 ft. The side lengths add in squares, not straight.

**Formula** (c = hypotenuse, a and b = the legs)

```math
c^2 = a^2 + b^2
```

- To find the hypotenuse: **c = √(a² + b²)**
- To find a leg: **a = √(c² − b²)**. Note the minus sign.

**Minimum to solve a problem:** You need two of the three sides. Square them, add them (or subtract if you're finding a leg), then take the square root.

**Exceptions**

- It only works for **right triangles**. Other triangles need the Law of Cosines, which this chapter doesn't cover.
- In AC terms, it only works when the two quantities are **exactly 90° apart**. Resistance and reactance are, so Z = √(R² + X²). Two quantities at 60° apart are not, and you'd need the vector methods further down.

**Common mistakes**

- **a + b ≠ c.** Adding 3 + 4 to get 7 is the most common error. The same mistake shows up in AC as adding 30 Ω of resistance to 40 Ω of reactance and calling it 70 Ω. The correct answer is 50 Ω.
- Calculator order: type `√(18² − 7²)`, not `√18² − 7²`. Use parentheses, or square and subtract first and take the root last.
- √(a² + b²) is **not** a + b. You can't "distribute" the square root.

**In the trade**

- **3-4-5 rule:** For laying out a square corner (equipment pad, strut rack, building line), measure 3 along one line and 4 along the other. When the diagonal is exactly 5, the corner is 90°. Scaled-up versions like 6-8-10 work the same way.
- **Rolling offsets:** When conduit has to move both over and up, the true offset = √(rise² + roll²).
- **Diagonal runs:** Like the parking-lot problem in the homework notes.

## 14–3 Sines, Cosines, and Tangents

**Intuition:** The *shape* of a right triangle depends only on its angle. A 30° triangle has the same side proportions whether it's 1 inch or 1 mile long. Sine, cosine and tangent are those fixed proportions. They let you go from angle to sides and back.

**Labeling the sides.** The labels depend on **which angle you're working from**:

- **Hypotenuse (H):** across from the 90° angle. It never changes.
- **Opposite (O):** the side across from your chosen angle. It doesn't touch that angle.
- **Adjacent (A):** the leg that touches your chosen angle and isn't the hypotenuse.

The book's trick of drawing a line that splits the angle in half works: that line runs into the opposite side. Simpler: the opposite side is the one your angle "looks at."

**The three ratios**

- sin θ = O / H
- cos θ = A / H
- tan θ = O / A

Two ways to remember them:

- The book's phrase: **"Oscar Had A Heap Of Apples"** gives O/H, A/H, O/A in the order sin, cos, tan.
- The more common one, which you'll hear on the job: **SOH-CAH-TOA**.

**Notation**

- **θ (theta):** the usual symbol for "the angle." The book also writes ∠X.
- **sin⁻¹, cos⁻¹, tan⁻¹** (also called arcsin, arccos, arctan, INV, or 2nd-function keys): these run the ratio backward. You give them a ratio and they return the angle.
  - sin⁻¹ does **not** mean 1/sin. It's an "undo" button, not an exponent.

**Minimum to solve a problem**

1. Mark the angle you care about.
2. Label H, O and A from that angle.
3. Ask which two sides are involved (known, or wanted). That pair tells you the function: O and H use sin, A and H use cos, O and A use tan.
4. To find an angle, compute the ratio, then use the inverse key. To find a side, rearrange the formula (see 14–4).

**Supporting idea the book glosses over:** In Examples 14–2 and 14–3, sin X and cos Y both came out to 0.643. That's not a coincidence. The side opposite X is the side adjacent to Y. So in any right triangle, **sin X = cos Y** whenever X + Y = 90°. You can always check one angle with the other: 40° + 50° = 90°.

**Range check:** sin and cos are always between 0 and 1 for these angles, because H is the longest side. If your calculator says **ERROR** on sin⁻¹ or cos⁻¹, you put the hypotenuse on top. Tan can be any positive number. Tan 45° = 1, and it gets very large as the angle approaches 90°.

**Calculator pitfalls (these cost the most points)**

- **DEG vs RAD mode.** If you're in radian mode, every answer is wrong and nothing warns you. Look for "D" or "DEG" on the screen. A quick test: sin 30 should give 0.5.
- **Pressing SIN instead of SIN⁻¹.** The book shows this exact mistake: sin(0.643) gives 0.0112, which is nonsense.
- **Rounding too early.** Keep the full ratio in the calculator, or carry at least 4 digits, and round only the final answer. Rounding 0.643 before taking the inverse can move your angle by a tenth of a degree or more.
- **Typing order.** Some calculators want the function first (`sin 30`), others want the number first (`30 sin`). Learn yours before the test.

**Exception:** SOH-CAH-TOA only applies to **right triangles**. You'll run into the more general version, which works for any angle, when we get to phasors and 3-phase.

## 14–4 Formulas (Rearranging)

**Intuition:** There's really just one formula per function. Everything else in the book's list is that formula rearranged.

**Starting from sin θ = O / H:**

- Multiply both sides by H to get **O = H × sin θ**.
- Divide by sin θ to get **H = O / sin θ**.

The same moves apply to cos (A = H × cos θ, H = A / cos θ) and tan (O = A × tan θ, A = O / tan θ).

A memory aid: cover the side you want in a "triangle" with O over S·H (or A over C·H, or O over T·A), the same way you'd use an Ohm's law circle.

**Pitfall:** You'll be tempted to multiply when you should divide. Sanity check: when you're **solving for the hypotenuse**, the answer must be **bigger** than the leg you started with. Dividing by a number less than 1 makes it bigger, so that's correct.

**Electrical preview of where these formulas land:**

- **W = VA × cos θ** (true power = apparent power × power factor)
- **VAR = VA × sin θ**
- **R = Z × cos θ**
- **X = Z × sin θ**

## 14–5 Practical Application (Shadow Height)

**Idea:** The sun hits everything nearby at the same angle. A short stick and a tall building make similar triangles. You measure the angle with the stick, then apply it to the building.

**Book example check:** tan θ = 12 / 7.5 = 1.6, so θ ≈ 58°. Height = 35 ft × 1.6 = 56 ft. Correct.

**Shortcut the book doesn't mention:** You don't need the angle at all. The ratio is the same for both triangles, so 12 in / 7.5 in = height / 35 ft, which gives 56 ft. Finding the angle and then taking its tangent just undoes itself. It's still worth learning the angle method, because the angle itself is what matters in AC.

**Watch your units:** Inches and inches in the ratio, feet and feet in the measurement. Mixing them is the usual mistake.

## Vectors

**Intuition:** A plain number (a **scalar**) answers "how much?" A **vector** answers "how much, and which way?" "Walk 3 blocks" is a scalar. "Walk 3 blocks south" is a vector. In AC, "which way" means **"at what point in the cycle."** That's what phase angle is.

**Definitions and conventions**

- **Magnitude:** the length of the arrow, representing volts, amps, ohms and so on.
- **Direction:** the angle, **measured counterclockwise from 0°**. The 0° direction is the horizontal line pointing right ("3 o'clock").
- Every angle is measured **from 0°, not from the previous vector.** Figure 14–13 makes this point, and students still get it wrong.
- **Notation you'll see:** 5∠30° means a magnitude of 5 at an angle of 30°. This is called **polar form**.
- **Negative angles** go clockwise: −30° is the same direction as 330°. Later you'll see lagging current written with a negative angle.
- **Resultant:** the single vector that equals the combined effect of all the vectors added together.
- In AC these rotating vectors are formally called **phasors**. The textbook keeps calling them vectors, and that's fine for now.

### 1. Same direction

Just add the magnitudes. Examples are batteries in series aiding (6 V + 4 V = 10 V) and series resistors (80 + 50 + 30 = 160 Ω). The book says these "become scalars." More precisely, they're still vectors, but since they point the same way, plain addition gives the right answer.

### 2. Opposite directions (180° apart)

Subtract the smaller magnitude from the larger. The result points in the direction of the larger one. Example: 6 V − 4 V = 2 V, in the direction of the 6 V battery.

**Textbook error:** The book has this backwards. It says to "subtract the magnitude of the larger vector from the magnitude of the smaller." It should be larger minus smaller.

**In the trade:** On a 120/240 V split-phase panel, the two legs are 180° apart.

- Measured leg to leg, they add: 120 + 120 = 240 V.
- On the neutral, the two leg currents oppose each other. **Neutral current = the difference between the two leg currents.** For example, 30 A on L1 and 20 A on L2 gives 10 A on the neutral.

That's why a balanced multiwire branch circuit carries almost nothing on its neutral. It's also why an **open (lost) neutral** is so dangerous: the voltage splits by load instead of staying at 120 each, so one side goes high and burns out equipment.

### 3. Different directions: tip-to-tail

Place the tail of the second vector at the head (arrow end) of the first. The **resultant** runs from the very first tail to the very last head. This works for any number of vectors, and the order you add them in doesn't change the answer.

### 4. Parallelogram method

Use this when both vectors start from the same point. Draw a copy of each vector at the head of the other to complete a parallelogram. The resultant is the diagonal from the shared starting corner. This is the same answer as tip-to-tail, just drawn differently. (The book's "tale" is a typo for "tail.")

### The exact method (not in this chapter, but your instructor may expect it)

Both drawing methods are only as accurate as your ruler and protractor. The book's Figure 14–17 gives 6.4832 at 34°. The exact answer is **6.478 at 34.1°**, so drawn answers will be a little off. The exact method uses the trig from above:

1. Split each vector into horizontal and vertical pieces:
   - x = magnitude × cos θ
   - y = magnitude × sin θ
2. Add all the x pieces together, and all the y pieces together.
3. Resultant magnitude = √(x² + y²) (Pythagorean theorem). Resultant angle = tan⁻¹(y / x).

Worked through for Figure 14–17 (4∠15° + 3∠60°):

- x = 3.864 + 1.500 = 5.364
- y = 1.035 + 2.598 = 3.633
- Magnitude = √(5.364² + 3.633²) = **6.48**
- Angle = tan⁻¹(3.633 / 5.364) = **34.1°**

This method is where the whole chapter comes together.

**Exception to step 3:** tan⁻¹ only returns angles between −90° and +90°. If the total x is negative (the resultant points left), add 180° to whatever the calculator gives you. Many scientific calculators have **R→P / P→R** (rectangular↔polar) keys that handle this automatically and are worth learning.

**Pitfall:** Adding magnitudes when the angles differ. 4∠15° + 3∠60° is **not** 7. Vectors at an angle always add up to less than their straight sum. The sum only reaches the straight total when they point the same way.

## Easily overlooked things for electricians

1. **Conduit bending is trig.** The offset multiplier for a bend angle θ is 1/sin θ. That gives the multipliers you'll memorize: 10° → 6.0, 22½° → 2.6, 30° → 2.0, 45° → 1.4, 60° → 1.2. The 30° multiplier is exactly 2 because sin 30° = 0.5.
   - Distance between bends = offset depth × multiplier.
   - Learning that the multipliers come from sine makes them easy to reconstruct when you forget them.
2. **120 V + 120 V doesn't make 240 V in a 3-phase wye.** The phases are 120° apart, so phase-to-phase is 120 × √3 ≈ **208 V**.
   - The √3 comes straight from vector addition, the same way the 4∠15° + 3∠60° example works.
   - In a balanced wye, the neutral current is zero because three equal vectors 120° apart cancel.
3. **High-leg (wild-leg) delta.** On a 120/240 V delta, the high leg measures 240 × (√3 / 2) ≈ **208 V** to neutral. It's the right-triangle math from this chapter.
   - NEC requires it to be marked orange.
   - Landing a 120 V load on it is a classic way to burn up equipment.
4. **Power factor = cos θ.** Utilities bill industrial customers for poor PF, and PF-correction capacitors exist to shrink θ. This is the power triangle from "Why this chapter exists."
5. **Your clamp meter only shows magnitude.** A DMM reads volts and amps, not angle. That's why V × A on your meter doesn't equal watts on an inductive load. You'd need a power-quality analyzer or wattmeter to see the angle.

## Notes on the homework

- **Figure 14–22 orientation:** In this figure, angle X is at the bottom right and angle Y is at the top left. Side A is the vertical leg and side B is the horizontal leg.
  - From X: A is opposite and B is adjacent.
  - From Y: B is opposite and A is adjacent.
  - Re-label the sides for every question, because the question switches between X and Y.
- **Practice chart:** In each row, find the missing angle first using 90° − the given one. Then choose a function based on whichever side pairs with your known values.
- **Practical Application 1 (parking lot):**
  - The run is the diagonal: √(275² + 200²).
  - The "equally spaced pull boxes" detail is a distractor. It doesn't change the length.
  - The 2 ft burial depth means the conduit has to come up at each end. Ask your instructor whether to add those vertical runs. The book likely wants the plain diagonal plus the stated extras, but on a real job you'd add them.
- **Practical Application 2 (solar collector):**
  - The yardstick is **3 ft**, and the shadow is 3.5 ft. Don't mix units.
  - The trap: tan⁻¹(3 / 3.5) gives the **sun's angle above the ground**, not the collector's tilt. For the rays to hit the panel at 90°, the panel has to be tilted at 90° minus the sun angle.
  - Sketch it before answering.

## One-glance cheat sheet

- **Calculator:** must be in DEG mode. Test: sin 30 = 0.5.
- **Pythagorean theorem:** c = √(a² + b²) and a = √(c² − b²). Right triangles only.
- **SOH-CAH-TOA:** sin = O/H, cos = A/H, tan = O/A. Label O and A from your chosen angle.
- **Angles:** use the inverse key (sin⁻¹, cos⁻¹, tan⁻¹) to get an angle. The two acute angles add to 90°.
- **Rearranging:**
  - Finding a side next to H: multiply (O = H sin θ, A = H cos θ).
  - Finding H: divide (H = O/sin θ = A/cos θ).
  - Using tan: O = A tan θ, A = O / tan θ.
- **Sanity checks:** H is the longest side. sin and cos are always ≤ 1. Vectors at an angle add to less than the straight sum of their magnitudes.
- **Vectors:** angles are measured counterclockwise from 0° (pointing right). Add same-direction vectors, subtract opposite ones. For any other angle, use tip-to-tail or the parallelogram, or split into x and y components for an exact answer.
