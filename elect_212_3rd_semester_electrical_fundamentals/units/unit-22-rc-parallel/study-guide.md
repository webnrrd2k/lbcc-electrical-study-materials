# Unit 22 Study Guide: Resistive-Capacitive Parallel Circuits

Oct 22, 2026 · @Jeff

## Why this chapter matters

This unit is Unit 18 (R-L parallel) with the inductor swapped for a capacitor. The procedure is the same. The capacitive branch current **leads** instead of lagging. It's the last "two-element" circuit before the units that combine R, L and C, and it's the circuit picture behind **power-factor correction capacitors**, which are always connected in parallel with the load.

The chapter works one example all the way through: R = 30 Ω in parallel with Xᶜ = 20 Ω on 240 V, 60 Hz.

**What carries over from Unit 18 (parallel rules)**

|  | Parallel R-C |
| --- | --- |
| Same everywhere (reference) | Voltage |
| Adds as vectors | Iᵣ and Iᶜ |
| Impedance | Smaller than R and smaller than Xᶜ |
| PF ratios | P/VA, Iᵣ/Iₜ, Z/R |
| Can't use for PF | Voltage (same on every branch) |
| Current vs voltage | Total current **leads** |

The three groups still apply: resistive (R, Iᵣ, P), capacitive (Xᶜ, Iᶜ, VARsᶜ, C), total (Z, Iₜ, VA, PF, θ). Ohm's law only works inside one group.

## 22–1 Operation of R-C Parallel Circuits

**Intuition:** Each branch is wired straight across the supply, so each sees the same voltage and draws its own current. The resistor's current is in step with the voltage. The capacitor's current is a quarter-cycle **ahead**. The line has to carry both, and they combine as a right triangle.

**Core facts**

- Eₜ = Eᵣ = Eᶜ, the same in magnitude and phase.
- Iᵣ is in phase with E. Iᶜ **leads** E by 90°.
- So Iᵣ and Iᶜ are **90° apart** (Review Q1).
- The total current leads the voltage by an angle between 0° and 90°.
- The angle depends on how the current splits: tan θ = Iᶜ / Iᵣ = R / Xᶜ. (The book says "ratio of resistance to capacitance"; it's really to capacitive *reactance*.)

**Parallel twist (same as Unit 18):** the branch drawing **more current** dominates. A **bigger** capacitor (lower Xᶜ, more Iᶜ) or a **bigger** resistance (less Iᵣ) makes the circuit **more capacitive**, with a bigger angle and a lower PF. That's the opposite of the series R-C behaviour in Unit 21.

**Phasor picture:** voltage is the 0° reference. Iᵣ lies along it, Iᶜ points **up** (leading), and Iₜ is the hypotenuse. Compare Unit 18, where Iₗ pointed down.

## Branch Currents and Total Current

**Each branch is plain Ohm's law with the full supply voltage:**

- Iᵣ = E / R = 240 / 30 = **8 A**, and P = E × Iᵣ = **1920 W**.
- Iᶜ = E / Xᶜ = 240 / 20 = **12 A**, and VARsᶜ = E × Iᶜ = **2880 VARs**.
- C = 1 / (377 × 20) = **132.6 µF**.

**Total current (the current triangle):**

```math
I_T = \sqrt{I_R^2 + I_C^2}
```

- √(8² + 12²) = √208 = **14.42 A**, not 20 A.
- Rearranged: Iᵣ = √(Iₜ² − Iᶜ²) and Iᶜ = √(Iₜ² − Iᵣ²).

**On the job:** clamp each branch (8 A and 12 A) and then the feeder, and you'll read 14.4 A. That's normal, because the branch currents peak at different times.

**Pitfalls**

- Iₜ = Iᵣ + Iᶜ is wrong (except for branches of the same type).
- Several capacitor branches: add their currents straight first (same phase), then use the Pythagorean theorem with Iᵣ.

## Impedance in a Parallel R-C Circuit

**Intuition:** A second path lowers the total opposition, so Z is **smaller than both** R and Xᶜ. Here 16.64 Ω is less than both 30 and 20.

**Three ways to find Z**

1. **Ohm's law:** Z = E / Iₜ = 240 / 14.422 = **16.64 Ω**.
2. **Reciprocal (vector) formula:** Z = 1 / √((1/R)² + (1/Xᶜ)²).
3. **Product over vector sum:**

```math
Z = \frac{R \times X_C}{\sqrt{R^2 + X_C^2}}
```

(30 × 20) / √(30² + 20²) = 600 / 36.06 = 16.64 Ω.

**Pitfalls (same traps as Unit 18)**

- √(R² + Xᶜ²) = 36.06 Ω is the **series** answer. In parallel it's only the *bottom* of the fraction.
- Plain product-over-sum, (30 × 20) / (30 + 20) = 12 Ω, ignores the 90°. Wrong.
- There's **no impedance triangle** with R and Xᶜ as legs in a parallel circuit. Draw the **current** triangle instead.
- Sanity check: Z must be smaller than the smaller of R and Xᶜ.

## Power: Watts, VARs and Volt-Amps

| Quantity | Formula | Example value |
| --- | --- | --- |
| True power P | E × Iᵣ | 1920 W |
| Reactive power VARsᶜ | E × Iᶜ | 2880 VARs |
| Apparent power VA | E × Iₜ, or √(P² + VARsᶜ²) | 3461 VA |

- The power triangle has the same form as in every other circuit. Power doesn't care about series vs parallel.
- In parallel, the power triangle is the **current** triangle multiplied by E (8, 12, 14.42 A × 240 V).
- **Find E from power and reactance:** E = √(VARs × Xᶜ) or √(P × R) (Example 22–2). These come from VARs = E²/Xᶜ and P = E²/R.
- **Pitfall:** E × Iₜ is VA, not watts.

## Power Factor and Angle Theta

**PF formulas for parallel R-C**

- PF = P / VA = 1920 / 3461 = **0.5547 (55.47%)**
- PF = Iᵣ / Iₜ = 8 / 14.42 = 0.5547
- PF = Z / R = 16.64 / 30 = 0.5547. Note the parallel version is **Z/R**, not R/Z.

**Angle theta:** cos θ = PF, so θ = cos⁻¹(0.5547) = **56.31°**, with the current **leading** the voltage.

- Other trig: tan θ = Iᶜ / Iᵣ = VARsᶜ / P, and sin θ = Iᶜ / Iₜ = VARsᶜ / VA.
- To go backward from PF: P = VA × PF, then VARs = √(VA² − P²), or VARs = VA × sin θ.

**Pitfalls**

- Convert the percent to a decimal before cos⁻¹ (Example 22–2: 47.1% means use 0.471).
- Eᵣ / Eₜ is always 1 in parallel. Use currents.
- Say **leading**. An R-C circuit's PF is leading, the opposite of the motor loads you'll usually meet.

**Book wording slip:** 22–1 says the circuit PF is "determined by the ratio of resistance and capacitance." PF is true power ÷ apparent power. The R-to-Xᶜ ratio sets the angle that produces it.

## Example 22–2: Working Backward from PF and VA

Given: 400 Hz, PF = 47.1%, VA = 4086.13, C = 33.15 µF. No voltage or current given.

1. **θ** = cos⁻¹(0.471) = **61.9°**.
2. **P** = VA × PF = 4086.13 × 0.471 = **1924.5 W**.
3. **VARsᶜ** = √(VA² − P²) = **3604.6**.
4. **Xᶜ** = 1 / (2π × 400 × 0.00003315) = **12.0 Ω**. It's 400 Hz, so 377 does **not** apply.
5. **Voltage:** E = √(VARs × Xᶜ) = √(3604.6 × 12) = **208 V**. It's the same on every branch.
6. **Currents:** Iᶜ = 208 / 12 = 17.33 A. Iᵣ = P / E = 9.25 A. Iₜ = √(9.25² + 17.33²) = **19.64 A**.
7. **R** = 208 / 9.25 = **22.49 Ω**. **Z** = (R × Xᶜ) / √(R² + Xᶜ²) = **10.59 Ω**. Check: 208 / 19.64 = 10.59 Ω ✓.

**Key move:** in parallel, find the voltage first. It's the bridge into every branch, just as current is in series. When E isn't given, get it from a power and an impedance: E = √(VARs × Xᶜ), √(P × R), or √(VA × Z).

**Book typos here**

- The Xᶜ formula shows "1 Hz" on top of the fraction. It's just **1**.
- θ is given as 61.9° at the start and 61.93° in the final figure. It's rounding, not a different angle.

## Easily overlooked things for electricians

1. **This is the PF-correction circuit.** Correction capacitors go **in parallel** with the load (across the line), never in series. Their leading branch current cancels the motor's lagging current, so the feeder current drops while the load keeps its full voltage.
2. **A capacitor alone on a line still draws real current.** 132.6 µF on 240 V draws 12 A even though it uses no watts. That's why capacitor feeders and disconnects are sized at **135% of the capacitor's rated current** (NEC 460.8), not from watts.
3. **Capacitor current rises with frequency and voltage.** A capacitor bank on a circuit with harmonics, or with high voltage, draws more current than its nameplate. See Unit 20.
4. **Too much parallel capacitance gives a leading PF.** If the load drops off (motors stop) but the capacitors stay on, the plant goes leading and the voltage can rise. That's why PF banks are often switched with the load or controlled automatically.
5. **Branch clamps vs feeder clamp.** With capacitive and resistive branches, the feeder reads less than the sum. In R-L-C circuits later, the feeder can read **less than a single branch**, because capacitive and inductive currents cancel.
6. **Discharge before you touch.** Parallel capacitors stay charged after the supply opens (Unit 19).

## Notes on the homework

- **General method:** In parallel, get **E** first (it's often given). Then each branch with Ohm's law, then add currents (or powers) with the Pythagorean theorem.
- **Q1:** Iᵣ and Iᶜ are 90° apart.
- **Q2–Q5 (40 Ω ‖ 132.6 µF on 120 V):** Convert C to Xᶜ first (it should come out to a round number). Then Iᵣ, Iᶜ, Iₜ, then Z = E / Iₜ, PF = Iᵣ / Iₜ, θ = cos⁻¹(PF).
- **Q6 and Q7 (208 V, 46 A, 4975 W):** Iᵣ = P / E, R = E / Iᵣ. Then Iᶜ = √(Iₜ² − Iᵣ²), Xᶜ = E / Iᶜ, C = 1 / (377 × Xᶜ).
- **Q8:** Convert 40 µF to Xᶜ, find the branch currents, then PF = Iᵣ / Iₜ.
- **Practice 2 (Z and R given, Iᶜ = 2 A, 400 Hz):** You need E. Try PF = Z / R and θ, or note that Iᶜ = Iₜ × sin θ. 377 doesn't apply at 400 Hz.
- **Practice 3:** E = Iₜ × Z, after Iₜ = √(Iᵣ² + Iᶜ²).
- **Practice 5:** Use the product-over-vector-sum formula (kΩ is fine if you keep both in kΩ).
- **Practice 6:** E = Iᵣ × R, then Iᶜ = E / Xᶜ.
- **Practice 7:** Iᵣ = 120 / 240. Then Iᶜ = √(1.2² − Iᵣ²) and Xᶜ = 120 / Iᶜ.
- **Practice 8:** VARs = VA × sin 58°.
- **Practice 10 (1 kHz):** Iᵣ = 7.5 / 4. Then Iᶜ, then Xᶜ, then C = 1 / (2π × 1000 × Xᶜ).

## One-glance cheat sheet

**Book example, all values (240 V, 60 Hz, R = 30 Ω ‖ Xᶜ = 20 Ω)**

| Total | Resistive branch | Capacitive branch |
| --- | --- | --- |
| Eₜ = 240 V | Eᵣ = 240 V | Eᶜ = 240 V |
| Iₜ = 14.42 A | Iᵣ = 8 A | Iᶜ = 12 A |
| Z = 16.64 Ω | R = 30 Ω | Xᶜ = 20 Ω |
| VA = 3461 | P = 1920 W | VARsᶜ = 2880 |
| PF = 55.47% leading, θ = 56.31° | — | C = 132.6 µF |

**Rules**

- **Same voltage on every branch.** It's the reference, so get it first.
- **Iₜ** = √(Iᵣ² + Iᶜ²). Never Iᵣ + Iᶜ.
- **Z** = E/Iₜ = R·Xᶜ / √(R² + Xᶜ²). Z is smaller than both R and Xᶜ. No impedance triangle.
- **Power triangle unchanged:** VA = √(P² + VARs²).
- **Finding E:** E = √(VARs × Xᶜ) = √(P × R) = √(VA × Z).
- **PF** = P/VA = Iᵣ/Iₜ = **Z/R** = cos θ. Current **leads**.
- **Bigger C or bigger R in parallel** makes the circuit more capacitive (lower PF).
- **Xᶜ** = 1/(2πfC). 377 only at 60 Hz.
