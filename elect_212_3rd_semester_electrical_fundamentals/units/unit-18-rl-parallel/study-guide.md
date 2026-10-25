# Unit 18 Study Guide: Resistive-Inductive Parallel Circuits

Oct 22, 2026 · @Jeff

## Why this chapter matters

Almost every real branch circuit is a **parallel** circuit with mixed loads: lights next to a fan motor, heat strips next to a compressor, receptacles feeding a bit of everything. This chapter shows how to find the total current, impedance and power factor when resistive and inductive loads share the same voltage.

The book works one example all the way through: R = 15 Ω in parallel with Xₗ = 20 Ω on 240 V, 60 Hz. Every value is collected in the cheat sheet at the end.

**The one idea to carry over from Unit 17, with a twist:** the three groups (resistive, inductive, total) still hold, and Ohm's law still only works inside one group. What changes is the shared quantity:

|  | Series (Unit 17) | Parallel (Unit 18) |
| --- | --- | --- |
| Same everywhere | Current | **Voltage** |
| Splits and adds as vectors | Voltages | **Currents** |
| Right triangle you draw | Z, voltage, power | **Current**, power |
| PF from... | R/Z, Eᵣ/Eₜ, P/VA | **Z/R**, **Iᵣ/Iₜ**, P/VA |

## 18–1 R-L Parallel Circuits

**Intuition:** Each branch is connected straight across the same supply, so each branch "sees" the full voltage and does its own thing. The resistor draws current in step with the voltage. The inductor draws current that lags by 90°. The line has to carry both at once, and since they peak at different times, they combine as a right triangle.

**Core facts**

- The voltage is the **same across every branch**, in magnitude and phase: Eₜ = Eᵣ = Eₗ.
- **Iᵣ is in phase** with the voltage.
- **Iₗ lags** the voltage by 90°.
- So Iᵣ and Iₗ are **90° apart from each other**. (Review Q1.)
- The total current lags the voltage by some angle between 0° and 90°. The angle depends on how the current is split between the branches.
- PF is still true power ÷ apparent power.

**Phasor picture:** Voltage is the shared quantity, so it's the 0° reference. Iᵣ lies along it, and Iₗ points straight down (lagging). Iₜ is the hypotenuse.

**Exception to the series intuition:** In series, a *bigger* resistance makes the circuit *more* resistive. In parallel, the **branch drawing more current dominates**. A *smaller* resistance (more Iᵣ) pushes the PF toward 100%, and a *smaller* Xₗ (more Iₗ) pushes it down. Big values in a parallel branch mean that branch matters *less*.

**Assumption:** the inductors are pure (Q ≥ 10), so their wire resistance is ignored.

## 18–2 Branch Currents and Total Current

**Intuition:** Each branch is just Ohm's law with the full supply voltage. The only new step is adding the branch currents, and since they're 90° apart, you add them with the Pythagorean theorem.

**Branch values (each stays in its own group)**

- Resistive branch: Iᵣ = E / R = 240 / 15 = **16 A**, and P = E × Iᵣ = 240 × 16 = **3840 W**.
- Inductive branch: Iₗ = E / Xₗ = 240 / 20 = **12 A**, and VARs = E × Iₗ = 240 × 12 = **2880 VARs**.
- Inductance: L = Xₗ / 377 = 20 / 377 = **0.0531 H**.

**Total current (the current triangle)**

```math
I_T = \sqrt{I_R^2 + I_L^2}
```

- √(16² + 12²) = **20 A**, not 28 A.
- Rearranged: Iᵣ = √(Iₜ² − Iₗ²) and Iₗ = √(Iₜ² − Iᵣ²).

**The field surprise:** Clamp each branch and you read 16 A and 12 A. Clamp the feeder and you read **20 A**, less than 28. Nothing is wrong. The branch currents peak at different moments, so the line never carries their straight sum.

**Pitfalls**

- **Iₜ = Iᵣ + Iₗ is wrong** unless both branches have the same phase angle.
- **Several branches of the same kind add straight first.** Two resistors: add Iᵣ's. Two inductors: add Iₗ's (Example 18–2: 9 A + 6 A = 15 A). Then do the Pythagorean theorem once.
- Use the voltage across the branch, which in parallel is just the supply voltage.

## Impedance in a Parallel R-L Circuit

**Intuition:** Adding a branch in parallel gives current another path, so the total opposition goes **down**. Z is smaller than R and smaller than Xₗ (12 Ω is less than both 15 and 20).

**Method 1, easiest when you know E and Iₜ:** Z = Eₜ / Iₜ = 240 / 20 = **12 Ω**.

**Method 2, the reciprocal formula** (reciprocals add as vectors):

```math
Z = \frac{1}{\sqrt{\left(\frac{1}{R}\right)^2 + \left(\frac{1}{X_L}\right)^2}}
```

**Method 3, product over vector sum:**

```math
Z = \frac{R \times X_L}{\sqrt{R^2 + X_L^2}}
```

- (15 × 20) / √(15² + 20²) = 300 / 25 = **12 Ω**.
- It looks like the product-over-sum rule for resistors, but the bottom is a **vector** sum.

**Book's helpful hint, and the biggest trap:** In a parallel circuit, you **can't** draw R and Xₗ as the legs of an impedance triangle with Z as the hypotenuse. That only works in series. √(15² + 20²) = 25 Ω is the series answer, and it's twice the real 12 Ω.

**Other pitfalls**

- Plain product-over-sum (15 × 20) / (15 + 20) = 8.57 Ω is also **wrong**: it ignores the 90°.
- In the reciprocal formula, square each reciprocal, add, take the square root, then take the reciprocal again. Losing the last step is the usual error.
- **Several inductors in parallel:** combine them first, with the ordinary reciprocal (non-vector) formula, because they're all at the same angle. Example 18–2: 40 Ω ‖ 60 Ω = 24 Ω. Then use that Xₗₜ with R in the vector formula.

## Power: Watts, VARs and Volt-Amps

**Intuition:** Power doesn't care how the circuit is wired. Watts from every resistive load add up, VARs from every inductive load add up, and the two combine at 90° into VA. The **power triangle is identical** for series and parallel.

| Quantity | Formula (parallel example) | Value |
| --- | --- | --- |
| True power P (W) | E × Iᵣ = 240 × 16 | 3840 W |
| Reactive power (VARs) | E × Iₗ = 240 × 12 | 2880 VARs |
| Apparent power (VA) | E × Iₜ = 240 × 20 | 4800 VA |

```math
VA = \sqrt{P^2 + VARs^2}
```

Check: √(3840² + 2880²) = 4800 VA. Rearranged: P = √(VA² − VARs²) and VARs = √(VA² − P²).

**Similar triangles again:** The power triangle is the current triangle multiplied by E (16, 12, 20 A × 240 V). Same shape, same angle.

**Handy formula from Example 18–2:** If you know VA and Z but not E, then VA = E² / Z, so **E = √(VA × Z)**.

**Pitfalls**

- E × Iₜ gives VA, not watts.
- Add watts to watts and VARs to VARs straight. Never add VA from loads at different angles without splitting them into W and VARs first.

## Power Factor and Angle Theta in Parallel

**Intuition:** PF still means "what fraction of the line current does real work." In parallel, that fraction is literally visible: it's the resistive branch's share of the total current.

**PF formulas for a parallel R-L circuit**

- PF = P / VA = 3840 / 4800 = **0.80 (80%)** (works for any circuit)
- PF = **Iᵣ / Iₜ** = 16 / 20 = 0.80 (the parallel version of Eᵣ/Eₜ)
- PF = **Z / R** = 12 / 15 = 0.80 (note: **upside down** compared with series)
- The book also writes this as PF = 1 / (R/Z). It's the same thing.

**Why Z/R flips:** In parallel, Z is *smaller* than R. R/Z would be greater than 1, and PF can never exceed 1. Example 18–1: R = 8 Ω, Z = 5 Ω gives PF = 5/8 = **62.5%**.

**Why voltage can't give PF in parallel:** E is the same on every branch, so Eᵣ/Eₜ is always 1. That's the mirror image of the series rule, where current couldn't be used.

**Angle theta**

- cos θ = PF, so θ = cos⁻¹(0.80) = **36.87°**, current lagging. This works for any AC circuit.
- Other trig: tan θ = Iₗ/Iᵣ = VARs/P, and sin θ = Iₗ/Iₜ = VARs/VA.
- θ sits between the resistive leg (watts or Iᵣ) and the hypotenuse (VA or Iₜ).

**Book wording slip:** The text says PF is "the relationship of apparent power to the true power." It's the other way around: **true power ÷ apparent power**. The book's formulas are right.

## Example 18–2: One Resistor, Two Inductors

Given: R = 45 Ω, Xₗ₁ = 40 Ω, Xₗ₂ = 60 Ω, VA = 6120, 60 Hz. No voltage given.

1. **Combine like branches first.** The inductors are both at 90°, so use the ordinary parallel formula: Xₗₜ = 1 / (1/40 + 1/60) = **24 Ω**.
2. **Z with the vector formula:** Z = (45 × 24) / √(45² + 24²) = **21.176 Ω**.
3. **Voltage from VA and Z:** E = √(6120 × 21.176) = **360 V**. It's the same across every branch.
4. **Currents:** Iₜ = 360 / 21.176 = 17 A. Iᵣ = 360 / 45 = 8 A. Iₗ₁ = 360 / 40 = 9 A. Iₗ₂ = 360 / 60 = 6 A.
5. **Check:** Iₗ total = 9 + 6 = 15 A, and √(8² + 15²) = 17 A. It matches.
6. **Power:** P = 360 × 8 = 2880 W. VARs = 3240 + 2160 = 5400. PF = 2880 / 6120 = **47.06%**. θ = **61.93°**.
7. **Inductances:** L₁ = 40 / 377 = 0.106 H. L₂ = 60 / 377 = 0.159 H.

**Book typos here:** "P = 359.996 V × 8 V" should be **8 A**. Figure 18–13 labels the VARs slightly differently (3239.904, 2159.926) from the text (3239.964, 2159.976). Rounding noise, not a concept error.

**Real-world parallel R-L loads (Figure 18–16):** a ceiling fan with a light kit (motor = L, incandescent lamps = R), or a branch with lamps, fluorescent fixtures and motors together. Every load on a branch circuit is in parallel.

## Series vs Parallel R-L: Side by Side

|  | Series R-L (Unit 17) | Parallel R-L (Unit 18) |
| --- | --- | --- |
| Shared quantity (phasor reference) | Current | Voltage |
| What adds as vectors | Eᵣ and Eₗ | Iᵣ and Iₗ |
| Impedance | Z = √(R² + Xₗ²) (bigger than either) | Z = R·Xₗ / √(R² + Xₗ²) (smaller than either) |
| Impedance triangle? | Yes | No (can't draw R and Xₗ as legs) |
| PF ratios | R/Z, Eᵣ/Eₜ, P/VA | Z/R, Iᵣ/Iₜ, P/VA |
| Can't use for PF | Current (same everywhere) | Voltage (same everywhere) |
| Power triangle | VA² = W² + VARs² | Same |
| Bigger R makes the circuit... | More resistive (higher PF) | Less resistive (lower PF) |
| Typical example | Motor winding, ballast + lamp | Branch circuit: lights + fan, heat strips + compressor |

## Easily overlooked things for electricians

1. **Branch currents don't add straight on mixed loads.** Adding nameplate amps of a motor and a heater overstates the feeder current. The real total is the vector sum. (NEC load calculations often add them anyway: that's a deliberate, conservative simplification, not the physics.)
2. **A clamp on the feeder reads less than the sum of clamps on the branches.** It's normal with mixed resistive and inductive loads. Don't chase it as a fault.
3. **Adding resistive load *raises* a circuit's PF.** Heat strips coming on next to a compressor improve the PF, because the resistive current grows while the VARs stay the same. That doesn't make the VARs go away.
4. **Power-factor correction happens in parallel.** PF capacitors are connected across the line, in parallel with the motors, to cancel their lagging current. That's why the parallel picture is the one to master (capacitors come in the next units).
5. **Each branch gets full line voltage.** Unlike series, one load failing open doesn't drop voltage on the others. That's why building loads are wired in parallel.
6. **Motor power factor changes with load.** A compressor's lagging current is largest relative to its watts when lightly loaded, so a circuit's PF changes as equipment cycles.
7. **Heat pump example (Practical App 2):** compressor amps and heat-strip amps must be combined as vectors. Split the compressor's current into its resistive and inductive parts using its PF, add the strip heat's current to the resistive part, then use the Pythagorean theorem.

## Notes on the homework

- **General method:** In parallel, the voltage is your bridge into every branch (like current was in series). Get E first if it isn't given, then each branch with Ohm's law, then add currents (or powers) with the Pythagorean theorem.
- **Q2–Q5:** Convert 0.2 H to Xₗ first (377 × 0.2). Then find Iᵣ, Iₗ, Iₜ, then Z = E/Iₜ, PF = Iᵣ/Iₜ, θ = cos⁻¹(PF).
- **Q6:** √(6.5² + 8²), not 14.5 A.
- **Q7:** Use the parallel formula. Your answer must be below 20 Ω. If you get 31.2 Ω, you used the series formula.
- **Q8–Q10:** These are power-triangle questions, identical to series: P = VA × PF, VARs = √(VA² − P²), θ = cos⁻¹(P/VA).
- **Practice 2:** Find Iₜ from Iᵣ and Iₗ, then E = VA / Iₜ.
- **Practice 6:** Find Iₗ = √(Iₜ² − Iᵣ²) first, then E = VARs / Iₗ.
- **Practice 8:** Find Iᵣ = E / R, then Iₗ = √(Iₜ² − Iᵣ²), then Xₗ = E / Iₗ.
- **Practice 12:** PF = Z / R (or Iᵣ / Iₜ), **not** R / Z.
- **Practice 13:** No voltage given. Find Z with the parallel formula, E = Iₜ × Z, then Iᵣ = E / R. Watch the kΩ.
- **Practice 15:** Asks for "the reactance of the inductor," but Xₗ is given (48 Ω). It almost certainly means **inductance**: L = Xₗ / 377.
- **Practical App 1 (lights + inductive load):** Iᵣ = 500 W / 120 V. Then Iₗ = √(7² − Iᵣ²), Xₗ = 120 / Iₗ, L = Xₗ / 377.
- **Practical App 2 (heat pump):**
  - Compressor: Iᵣ = 34 × 0.70 and Iₗ = √(34² − Iᵣ²).
  - Strip heat: 10,000 W / 240 V, all resistive.
  - Total Iᵣ = compressor Iᵣ + strip current. Then Iₜ = √(Iᵣₜ² + Iₗ²).
  - **Trap:** 34 + 41.7 = 75.7 A overstates the total.

## One-glance cheat sheet

**Book example, all values (240 V, 60 Hz, R = 15 Ω ‖ Xₗ = 20 Ω)**

| Total | Resistive branch | Inductive branch |
| --- | --- | --- |
| Eₜ = 240 V | Eᵣ = 240 V | Eₗ = 240 V |
| Iₜ = 20 A | Iᵣ = 16 A | Iₗ = 12 A |
| Z = 12 Ω | R = 15 Ω | Xₗ = 20 Ω |
| VA = 4800 | P = 3840 W | VARs = 2880 |
| PF = 80%, θ = 36.87° | — | L = 0.0531 H |

**Rules**

- **Same voltage on every branch.** It's the reference. Get it early.
- **Currents add as vectors:** Iₜ = √(Iᵣ² + Iₗ²). Never Iᵣ + Iₗ.
- **Impedance:** Z = E/Iₜ = R·Xₗ / √(R² + Xₗ²). Z is smaller than both R and Xₗ. No impedance triangle in parallel.
- **Same-type branches first:** add like currents straight; combine like reactances with the ordinary reciprocal formula.
- **Power triangle unchanged:** VA = √(P² + VARs²). E = √(VA × Z).
- **PF** = P/VA = Iᵣ/Iₜ = **Z/R**. θ = cos⁻¹(PF), current lagging.
- **Never:** R/Z for PF in parallel, √(R² + Xₗ²) for parallel Z, or Eᵣ/Eₜ for PF.
