# Unit 17 Study Guide: Resistive-Inductive Series Circuits

Oct 22, 2026 · @Jeff

## Why this chapter matters

Real loads are almost never pure resistance or pure inductance. A motor, transformer or magnetic ballast acts like **a resistor and an inductor in series**: the wire and the useful work look resistive, and the coil looks inductive. This chapter shows how to solve that combination. It also introduces **power factor**, which shows up on industrial power bills and in later units on PF correction.

The chapter works one example circuit all the way through: R = 30 Ω in series with Xₗ = 40 Ω on 240 V, 60 Hz. Every section finds one more value, and they're collected in the cheat sheet at the end.

**The one idea that makes the whole chapter easy:** every quantity belongs to one of three groups. Ohm's law and the power formulas only work **inside one group**. To move between groups, use the right triangle (Pythagorean theorem or trig).

| Resistive group | Inductive group | Total group |
| --- | --- | --- |
| R (Ω) | Xₗ (Ω) | Z (Ω) |
| Eᵣ (volts across R) | Eₗ (volts across L) | Eₜ (applied volts) |
| Iᵣ | Iₗ | Iₜ |
| P (watts, true power) | VARs (reactive power) | VA (apparent power) |
| — | L (henrys) | PF, θ |

In every triangle in this chapter, the **resistive** quantity is the horizontal leg, the **inductive** quantity is the vertical leg, and the **total** is the hypotenuse.

## 17–1 R-L Series Circuits

**Intuition:** A resistor alone keeps current in step with voltage (0°). An inductor alone makes current lag by 90°. Put them in series and the result lands **in between**. The bigger share of the opposition, resistance or reactance, pulls the angle toward its own value.

**Core facts**

- In an R-L series circuit, current lags the applied voltage by some angle between **0° and 90°**.
- The exact angle depends on the **ratio** of R to Xₗ, not on their sizes alone. R = 30 and Xₗ = 40 gives the same 53.13° as R = 300 and Xₗ = 400.
- Being series, there's **one current**, the same everywhere: Iₜ = Iᵣ = Iₗ.
- Inside the circuit, the resistor's voltage is **in phase** with that current, and the inductor's voltage **leads** it by 90°.

**Assumption the book makes:** the inductor is pure (negligible wire resistance, Q ≥ 10). If a coil has significant wire resistance, that resistance counts as part of R.

**Why a phasor picture helps:** Current is the one thing shared by every part of a series circuit, so it's drawn as the 0° reference. Eᵣ sits on top of it at 0°, and Eₗ points straight up at 90°. Those two voltages are the legs of the voltage triangle.

## 17–2 and 17–3 Impedance and Total Current

**Intuition:** R and Xₗ both limit current, but they push back at different moments in the cycle (90° apart). So you can't just add their ohms. They combine like walking 30 ft east and then 40 ft north: you end up 50 ft away, not 70.

**Impedance (Z):** the total opposition to current in an AC circuit, in ohms.

```math
Z = \sqrt{R^2 + X_L^2}
```

- Example: √(30² + 40²) = 50 Ω, not 70 Ω.
- Rearranged: R = √(Z² − Xₗ²) and Xₗ = √(Z² − R²).
- Shown three ways in the book: a right triangle, tip-to-tail vectors, and the parallelogram method. All give the same answer.

**Total current:** Z replaces R in Ohm's law.

- Iₜ = Eₜ / Z = 240 / 50 = **4.8 A**
- Z = Eₜ / Iₜ also works backward from measured volts and amps.

**Pitfalls**

- **Adding R + Xₗ.** It's the most common mistake in AC work, and it's the Unit 14 mistake again.
- **Eₜ / R or Eₜ / Xₗ is not the current.** Only the total voltage over the total opposition gives total current.
- **Several resistors and several inductors in series:** add all the R's together and all the Xₗ's together *first* (they each point in the same direction), then do the Pythagorean theorem once. Practice Problem 13 tests this.

## 17–4, 17–6, 17–7, 17–8 Voltage Drops and Inductance

**Intuition:** Each part drops voltage according to its own opposition: E = I × (its own ohms). The drops still add up to the supply, but **as vectors**, because they peak at different times.

**Formulas (each stays in its own group)**

- Resistor: Eᵣ = Iᵣ × R = 4.8 × 30 = **144 V**
- Inductor: Eₗ = Iₗ × Xₗ = 4.8 × 40 = **192 V**
- Inductance: L = Xₗ / (2πf) = 40 / 377 = **0.106 H**

**Total voltage (the voltage triangle)**

```math
E_T = \sqrt{E_R^2 + E_L^2}
```

- √(144² + 192²) = 240 V. That matches the supply.
- Rearranged: Eᵣ = √(Eₜ² − Eₗ²) and Eₗ = √(Eₜ² − Eᵣ²).

**The surprise that confuses people on the job:** Measure each drop with a meter, and they seem to add up to more than the supply. 144 V + 192 V = 336 V on a 240 V circuit. That's not a bad meter. It's Kirchhoff's voltage law working with vectors. The meter shows magnitudes only, not the timing.

**Pitfalls (the book makes a point of these)**

- Eᵣ = I × Xₗ is **wrong**: it mixes groups.
- Eᵣ = I × Z is **wrong** too: Z is a total quantity, so I × Z gives Eₜ, not Eᵣ.
- Only the current can be used anywhere, because in a series circuit it really is the same number in every group.

**Similar triangles:** The voltage triangle is the impedance triangle multiplied by I (30→40→50 becomes 144→192→240, ×4.8). Same shape, same angle.

## 17–5, 17–9, 17–10 Watts, VARs and Volt-Amps

**Intuition:** Three kinds of "power" flow in the same circuit:

- **Watts** are the part that actually becomes heat, light or shaft work.
- **VARs** are the part that sloshes back and forth to build and collapse the coil's magnetic field.
- **VA** is what the wires and the utility actually have to carry: the two combined.

| Name | Symbol / unit | Group | Formulas |
| --- | --- | --- | --- |
| True power | P, watts (W) | Resistive | Eᵣ × Iᵣ, I²R, Eᵣ²/R |
| Reactive power ("quadrature" or "wattless" power) | VARs | Inductive | Eₗ × Iₗ, I²Xₗ, Eₗ²/Xₗ |
| Apparent power | VA | Total | Eₜ × Iₜ |

**Worked values:** P = 144 × 4.8 = **691.2 W**. VARs = 4.8² × 40 = **921.6 VARs**. VA = 240 × 4.8 = **1152 VA**.

**Why "apparent":** VA is what you'd get by clamping an ammeter on, reading a voltmeter, and multiplying. It *looks like* the power, but only part of it does work.

**The power triangle**

```math
VA = \sqrt{P^2 + VARs^2}
```

- Rearranged: P = √(VA² − VARs²) and VARs = √(VA² − P²).
- It's the impedance triangle multiplied by I² (30→40→50 × 23.04). Same shape, same angle.

**Book error:** Figures 17–12, 17–14 and 17–15 label the VARs as **691.2**. That's the watts number copied by mistake. The correct value is **921.6 VARs** (as Figure 17–13 and the text show).

**Pitfalls**

- Eₜ × Iₜ gives VA, **not watts**.
- I² × Xₗ gives VARs, **not watts**.
- **Watts add straight, and VARs add straight** (Example 17–1: 56 W + 44 W = 100 W, and 152 + 88 = 240 VARs), because each set points in the same direction. Only W and VARs combined need the Pythagorean theorem. VA from separate loads can't be added straight unless they're at the same angle.

## 17–11 and 17–12 Power Factor and Angle Theta

**Intuition:** Power factor answers: *of all the current I'm paying to move through the wires, what fraction actually does work?* A PF of 100% means all of it. A PF of 60% means the wires carry 1/0.6 = 1.67 times the current the work alone would need.

**Power factor (PF):** the ratio of true power to apparent power. Any resistive quantity divided by its matching total quantity:

- PF = P / VA = 691.2 / 1152 = 0.6
- PF = R / Z = 30 / 50 = 0.6
- PF = Eᵣ / Eₜ = 144 / 240 = 0.6
- Usually written as a percent: 0.6 × 100 = **60%**.

**Angle theta (θ):** the phase angle between the applied voltage and the total current. On every triangle it sits between the **resistive leg** (adjacent) and the **total hypotenuse**.

```math
\cos\theta = PF
```

- θ = cos⁻¹(0.6) = **53.13°**, with current lagging voltage.
- You can also use sin θ = VARs / VA or tan θ = VARs / P (or Xₗ/R, or Eₗ/Eᵣ). All three triangles give the same angle.

**Book wording error:** The book says "angle theta is the cosine of watts divided by volt-amperes" and "angle theta is the cosine of the power factor." That's backwards. The **cosine of θ is the PF**, so θ = cos⁻¹(PF). Its math is right; only the sentence is wrong.

**Exceptions and pitfalls**

- **Convert percent to a decimal first.** cos⁻¹(86) is an error; cos⁻¹(0.86) = 30.7°.
- **Current can't give PF in a series circuit**, because Iₜ, Iᵣ and Iₗ are all the same number. (In parallel circuits, next unit, it can.)
- **PF alone doesn't say leading or lagging.** R-L circuits are always **lagging**. Capacitive circuits lead. Write "0.6 lagging" when it matters.
- PF runs from 0 (pure reactance) to 1 (pure resistance). It can never be over 100%.

**Why utilities care:** They sell watt-hours but have to supply VA. The book's plant uses 5 MW:

| Power factor | Utility must supply |
| --- | --- |
| 60% | 5 MW ÷ 0.60 = 8.333 MVA |
| 95% | 5 MW ÷ 0.95 = 5.263 MVA |

Same work, about 37% less current. That's why low-PF customers pay a surcharge.

## Multi-component circuits and real-world R-L loads

### Several resistors and inductors (Example 17–1)

When you're given parts of a series circuit as **powers** (watts and VARs) instead of ohms, work through the power triangle:

1. Add all the watts: 56 + 44 = **100 W**.
2. Add all the VARs: 152 + 88 = **240 VARs**.
3. VA = √(100² + 240²) = **260 VA**.
4. Iₜ = VA / Eₜ = 260 / 130 = **2 A**, the same through every part.
5. Now each part solves on its own: E = P / I (or VARs / I), then R or Xₗ = E / I, then L = Xₗ / 377.
6. Z = Eₜ / Iₜ = 65 Ω. PF = 100 / 260 = 38.5%. θ = 67.38°.

**Key move:** Find the current as early as possible. In a series circuit, current is the bridge into every group.

### Motors are R-L series circuits

- A winding is a coil (inductance) made of wire (resistance), with one current path.
- **No load:** mostly inductive. Low PF, current lags a lot.
- **Full load:** the converted mechanical work shows up electrically as extra "resistance." PF rises, and current lags less.
- **Trade takeaway:** **lightly loaded motors have poor power factor.** An oversized motor running half-loaded wastes capacity.

### Gas-discharge lighting ballasts

- Fluorescent, mercury vapor and sodium vapor lamps conduct almost like a short once the gas ionizes.
- A magnetic **ballast** (an inductor) in series limits the current with its reactance, which wastes far less power than a resistor would.
- The lamp acts as the R, the ballast as the Xₗ. Magnetic ballasts give low PF unless the fixture includes a capacitor (a "high-PF" ballast).

## Easily overlooked things for electricians

1. **Size conductors and OCPDs on amps (VA), not watts.** A 10 kW load at 60% PF draws the current of 16.7 kVA. Watts alone undersize the wire. Transformer and generator ratings are in **kVA** for this reason.
2. **Your meters measure the total group.** A voltmeter and clamp meter give Eₜ and Iₜ, so V × A = VA. To read watts or PF directly you need a wattmeter, a PF meter or a power-quality analyzer.
3. **Voltage drops that "don't add up"** across a coil and a resistor (or a ballast and lamp) are normal in AC. Add them as vectors before you suspect a bad meter or connection.
4. **Low PF costs money and capacity.** Extra current means more I²R heat in feeders and transformers, more voltage drop, and utility surcharges. The fix is capacitors (PF correction, coming in the capacitance units) or right-sizing motors.
5. **Wire resistance counts when Q is low.** If a coil's Xₗ/R is under about 10, include its wire resistance in R. Practical Application 2 is built on this.
6. **Reduced-voltage starting** (primary resistor starting, Practical Application 1) uses this exact math: adding series R raises Z, which cuts inrush current. Since the motor is mostly reactive at start, the added R has to be found through the impedance triangle, not by simple subtraction.
7. **Motor PF changes with load.** A motor's nameplate PF applies at full load. Measure an idling motor and you'll see a much lower PF. That's normal, not a fault.

## Notes on the homework

- **General method:** List the givens in the three groups (resistive, inductive, total). Find Iₜ as soon as you can. Then fill in each group with Ohm's law, and cross groups with the triangle.
- **Q4:** Convert L to Xₗ first (377 × 0.093), then use Z = √(R² + Xₗ²).
- **Q5 and Q11:** θ = cos⁻¹(PF as a decimal), and PF = cos θ. DEG mode.
- **Q8:** You have VARs and VA, which means opposite and hypotenuse, so use sin⁻¹.
- **Q9:** Z = E/I first, then Xₗ = √(Z² − R²). Q10 is then just I × R.
- **Q12:** P = VA × PF, and keep the k in kVA → kW.
- **Practice 2:** Given Eᵣ, Eₗ and Z, find Eₜ from the voltage triangle, then Iₜ = Eₜ / Z.
- **Practice 9:** Here VA = E × I, then P = √(VA² − VARs²), then R = P / I².
- **Practice 12:** tan θ = VARs / P, so VARs = P × tan 22°.
- **Practice 13–16 (two R's and two Xₗ's):** Add like with like first (Rₜ = R₁ + R₂, Xₗₜ = Xₗ₁ + Xₗ₂), then build Z. For one part's drop (15, 16), find Iₜ = Eₜ / Z, then E = Iₜ × that part's ohms. Watch the kΩ units in 6 and 16.
- **Practical App 1 (motor inrush):**
  - Motor Z at start = 240 / 34. Use the 3 Ω wire resistance to split it into R and Xₗ.
  - The target Z = 240 / 20. Xₗ doesn't change, so find the **total R** needed with Rₜ = √(Z² − Xₗ²).
  - The resistor to add = that total R minus the motor's own 3 Ω.
  - **Trap:** subtracting the two impedances (12 − 7.06) gives the wrong answer.
- **Practical App 2 (inductor on 480 V):** Xₗ = 377 × 0.1. Q is only about 3.8, so the 10 Ω **can't** be ignored. Use Z = √(R² + Xₗ²), then I = E / Z.

## One-glance cheat sheet

**Book example, all values (240 V, 60 Hz, R = 30 Ω, Xₗ = 40 Ω)**

| Total | Resistive | Inductive |
| --- | --- | --- |
| Eₜ = 240 V | Eᵣ = 144 V | Eₗ = 192 V |
| Iₜ = 4.8 A | Iᵣ = 4.8 A | Iₗ = 4.8 A |
| Z = 50 Ω | R = 30 Ω | Xₗ = 40 Ω |
| VA = 1152 | P = 691.2 W | VARs = 921.6 |
| PF = 60%, θ = 53.13° | — | L = 0.106 H |

**Rules**

- **Ohm's law inside a group only.** Cross groups with the triangle: total² = resistive² + inductive².
- **Series:** one current everywhere. Find it early.
- **Same angle in every triangle** (impedance, voltage, power).
- **PF** = P/VA = R/Z = Eᵣ/Eₜ = cos θ. **θ** = cos⁻¹(PF), current lagging.
- **Other trig for θ:** sin θ = VARs/VA, tan θ = VARs/P = Xₗ/R.
- **Like adds to like:** watts add to watts and VARs add to VARs, straight. Only cross-group sums use the Pythagorean theorem.
- **Never:** Z = R + Xₗ, Eₜ = Eᵣ + Eₗ, or P = Eₜ × Iₜ.
- **Size wiring on VA (amps), not watts.**
