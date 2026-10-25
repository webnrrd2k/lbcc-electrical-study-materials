# Unit 21 Study Guide: Resistive-Capacitive Series Circuits

Oct 22, 2026 · @Jeff

## Why this chapter matters

This unit is Unit 17 (R-L series) with the inductor swapped for a capacitor. The procedure is identical. The **only real changes** are that Xₗ becomes Xᶜ, VARsₗ becomes VARsᶜ, and the current **leads** instead of lagging. If Unit 17 made sense, this one will too.

The chapter works one example all the way through: R = 12 Ω in series with Xᶜ = 16 Ω on 240 V, 60 Hz. It's the same 3-4-5 triangle shape as Unit 17's 30/40/50, so many of the numbers look familiar.

**The three groups still rule everything:**

| Resistive | Capacitive | Total |
| --- | --- | --- |
| R | Xᶜ | Z |
| Eᵣ | Eᶜ | Eₜ |
| Iᵣ | Iᶜ | Iₜ |
| P (W) | VARsᶜ | VA |
| — | C (farads) | PF, θ |

Use Ohm's law and the power formulas **inside one column**. Cross between columns with the right triangle: total² = resistive² + capacitive².

## 21–1 R-C Series Circuits

**Intuition:** A resistor keeps current in step with voltage. A capacitor makes the current lead by 90°. Put them in series and the total current leads by some angle **between 0° and 90°**. The larger of R and Xᶜ pulls the angle toward its own behaviour.

**Core facts**

- One current flows through everything: Iₜ = Iᵣ = Iᶜ.
- Eᵣ is in phase with the current. Eᶜ **lags** the current by 90° (the same thing as the current leading Eᶜ).
- So Eᵣ and Eᶜ are 90° apart and add as vectors.
- The total current **leads** the applied voltage (R-L circuits **lag**).
- The angle depends on the ratio of **R to Xᶜ**: tan θ = Xᶜ / R. The book says the "ratio of resistance to capacitance," but it's really to capacitive *reactance*.

**Counterintuitive point:** A **bigger** capacitor has **less** reactance, so it makes the series circuit **more resistive** (smaller angle). A tiny capacitor dominates a series R-C circuit.

## 21–2 and 21–3 Impedance and Total Current

**Intuition:** R and Xᶜ both limit current, but at different moments in the cycle (90° apart). They combine as the legs of a right triangle, with Z as the hypotenuse.

```math
Z = \sqrt{R^2 + X_C^2}
```

- Example: √(12² + 16²) = **20 Ω** (not 28 Ω).
- Rearranged: R = √(Z² − Xᶜ²) and Xᶜ = √(Z² − R²) (Review Q4).
- Total current: Iₜ = Eₜ / Z = 240 / 20 = **12 A**, the same through R and C.

**Getting Xᶜ when you're given capacitance:** Xᶜ = 1 / (2πfC). C must be in **farads**. Review Q2: 110.5 µF at 60 Hz gives Xᶜ ≈ 24 Ω.

**Pitfalls**

- Z = R + Xᶜ is wrong (they're 90° apart).
- In the impedance triangle, Xᶜ is conventionally drawn **downward** (opposite Xₗ). The math is the same. The direction just reminds you it's capacitive.
- **Two capacitors in series:** add their Xᶜ's first (same direction), then use the Pythagorean theorem once with R.

## 21–4, 21–6, 21–7, 21–8 Voltage Drops and Capacitance

**Each part drops voltage according to its own opposition** (stay inside the group):

- Eᵣ = I × R = 12 × 12 = **144 V**
- Eᶜ = I × Xᶜ = 12 × 16 = **192 V**
- C = 1 / (2πf Xᶜ) = 1 / (377 × 16) = **165.8 µF**

**Total voltage (vector sum)**

```math
E_T = \sqrt{E_R^2 + E_C^2}
```

- √(144² + 192²) = 240 V. Rearranged: Eᵣ = √(Eₜ² − Eᶜ²) and Eᶜ = √(Eₜ² − Eᵣ²).

**On the job:** meter each part and the drops look like they add to 336 V on a 240 V supply. That's normal: the drops are 90° apart.

**A trap specific to capacitors:** the capacitor's drop can be **nearly as large as, or in an R-L-C circuit even larger than**, the supply voltage. Check the capacitor's own voltage (Eᶜ), not just the supply, against its rating, and convert to peak if the rating is in VDC (Review Q6).

**Pitfalls**

- Eᵣ = I × Z or Eᶜ = I × R mixes groups. Wrong.
- Forgetting to convert C from µF to farads, or forgetting the reciprocal in Xᶜ = 1 / (2πfC).

## 21–5, 21–9, 21–10 True, Reactive and Apparent Power

| Quantity | Group | Formula (example) | Value |
| --- | --- | --- | --- |
| True power P (W) | Resistive | Eᵣ × I = 144 × 12 | 1728 W |
| Reactive power VARsᶜ | Capacitive | Eᶜ × I = 192 × 12 | 2304 VARs |
| Apparent power VA | Total | Eₜ × I = 240 × 12 | 2880 VA |

```math
VA = \sqrt{P^2 + VARs_C^2}
```

- Only the resistor produces watts. The capacitor's energy is stored and returned every cycle.
- The power triangle is the impedance triangle × I² (12² = 144: 12/16/20 × 144 = 1728/2304/2880). Same shape, same angle.

**Several capacitors (Example 21–1):** add their VARs straight (3.75 + 5.625 = 9.375), then VA = √(P² + VARsᶜ²). Watts add to watts the same way.

**Pitfalls**

- Eₜ × I is VA, not watts.
- Don't mix VARsᶜ with VARsₗ. They **subtract** (next units). Within this chapter there are only capacitive VARs.

## 21–11 and 21–12 Power Factor and Angle Theta

**Power factor:** true power ÷ apparent power, or any resistive value ÷ its matching total.

- PF = P/VA = 1728 / 2880 = **0.60 (60%)**
- Also PF = R/Z = 12/20 and Eᵣ/Eₜ = 144/240 (series, so current can't be used).

**Angle theta:** cos θ = PF, so θ = cos⁻¹(0.6) = **53.13°**. Here the current **leads** the voltage by 53.13°.

- Other trig: tan θ = Xᶜ / R = VARsᶜ / P, and sin θ = Xᶜ / Z = Eᶜ / Eₜ.

**Leading vs lagging:** PF and θ come out the same number for an R-L or an R-C circuit with the same triangle. The **direction** differs:

- R-L: current **lags**, called "lagging PF" (most industrial loads).
- R-C: current **leads**, called "leading PF".
- Always state which when it matters: "60% leading."

**Pitfalls**

- Convert percent to a decimal before cos⁻¹ (Review Q3: 76% means use 0.76).
- "Better" PF doesn't mean leading. The goal of PF correction is to get **close to 1.0**, not to overshoot into leading.

## Worked Examples and Book Errors

### Example 21–1: one resistor, two capacitors (given as powers)

Given: 42.5 V, 60 Hz; C₁ = 3.75 VARs, R = 5 W, C₂ = 5.625 VARs.

1. VARsᶜₜ = 3.75 + 5.625 = 9.375. VA = √(5² + 9.375²) = **10.625 VA**.
2. I = VA / E = 10.625 / 42.5 = **0.25 A**, the same everywhere.
3. Z = 42.5 / 0.25 = 170 Ω. PF = 5 / 10.625 = 47.06%. θ = 61.93° leading.
4. Each part on its own: E = power / I gives Eᶜ₁ = 15 V, Eᵣ = 20 V, Eᶜ₂ = 22.5 V. Then ohms = E / I gives Xᶜ₁ = 60 Ω, R = 80 Ω, Xᶜ₂ = 90 Ω. Then C = 1 / (377 × Xᶜ) gives 44.2 µF and 29.5 µF.

**Key move (same as Unit 17):** in series, get the current as early as possible. It's the bridge into every group.

### Example 21–2: a capacitor as a "voltage dropper"

A 2 W, 120 V indicator lamp must run on 480 V.

1. Lamp current = 2 / 120 = **0.01667 A**.
2. The lamp (resistive) and capacitor drops are 90° apart: Eᶜ = √(480² − 120²) = **464.8 V**. That's not 360 V!
3. Xᶜ = 464.8 / 0.01667 ≈ 27,885 Ω, so C ≈ **95 nF**. The book gets 95.3 nF by rounding the current to 0.0167 A.

**Why a capacitor instead of a resistor?** A dropping resistor would burn about 6 W as heat. The capacitor drops the voltage with essentially **no watts**, because its power is reactive. But the capacitor must be rated for about 465 V RMS, which is 657 V peak.

**Exception:** this only works because the lamp is treated as a constant resistance. A real incandescent filament has a much lower cold resistance, and LEDs aren't resistive at all.

### Book errors

- Example 21–1 writes C₁ = 1 / (377 × **30** Ω). It should be **60 Ω**. The answer, 44.2 µF, is correct for 60 Ω.
- Figures 21–9 and 21–10 label C₁'s reactive power as **3.73** VARs. It's **3.75**.
- The objectives list "inductive reactance" for an R-C circuit. It means **capacitive** reactance.

## Easily overlooked things for electricians

1. **Leading PF is real and can be a problem.** Over-corrected PF banks, long lightly loaded cables, and some electronic loads make the current lead. Too much leading kVAR raises voltage and can upset generators and voltage regulators. PF correction aims for about 0.95–1.0, not "as capacitive as possible."
2. **Check the voltage across the capacitor, not the supply.** In series circuits the capacitor's drop can approach (and in R-L-C circuits exceed) the line voltage. Compare Eᶜ (converted to peak, if the rating is VDC) with the rating.
3. **Capacitive droppers waste almost no power.** That's why indicator and pilot lights, cheap power supplies and some timers use a series capacitor instead of a resistor. Treat them as live: there's no isolation from the line.
4. **Series R-C circuits are everywhere in controls:** RC snubbers across contacts and triacs, and phase-shift networks in motor and SCR circuits (Unit 19's applications).
5. **Meters still read only the totals.** V × A gives VA. You need a wattmeter or power analyzer to see watts and leading/lagging PF. Many clamp-on power meters display "lead" or "lag."

## Notes on the homework

- **General method:** List the givens in the three groups. Find I as soon as possible. Ohm's law within each group, and the triangle between groups.
- **Q2:** Convert 110.5 µF to Xᶜ first (1 / (377 × 0.0001105)), then Z = √(R² + Xᶜ²).
- **Q3:** θ = cos⁻¹(0.76).
- **Q5:** Frequency goes from 60 to 1000 Hz, so Xᶜ drops by the same ratio: 50 × 60/1000.
- **Q6 (600 WVDC capacitor in series with 50 Ω on 480 V):** Find Xᶜ, Z, I, then **Eᶜ = I × Xᶜ**. Compare Eᶜ × 1.414 (peak) with 600 V. The capacitor's drop here is close to the full 480 V.
- **Q7:** I = 65 / 25. Then Eᶜ = √(120² − 65²), Xᶜ = Eᶜ / I, C = 1 / (377 × Xᶜ).
- **Q8:** PF = 3000 / (240 × 20). For C: R = P / I², Z = E / I, Xᶜ = √(Z² − R²), C = 1 / (377 × Xᶜ).
- **Practice 2:** Eₜ = √(78² + 104²), then I = Eₜ / Z.
- **Practice 4 (400 Hz):** 377 doesn't apply. Use 2π × 400.
- **Practice 8 (Eₜ and θ only):** Eᶜ = Eₜ × sin θ (Eᶜ is the side opposite θ).
- **Practice 9:** Z = 240 / 0.75, Xᶜ = √(Z² − 140²), C = 1 / (377 × Xᶜ).
- **Practice 10:** P = √(VA² − VARs²).

## One-glance cheat sheet

**Book example, all values (240 V, 60 Hz, R = 12 Ω, Xᶜ = 16 Ω)**

| Total | Resistive | Capacitive |
| --- | --- | --- |
| Eₜ = 240 V | Eᵣ = 144 V | Eᶜ = 192 V |
| Iₜ = 12 A | Iᵣ = 12 A | Iᶜ = 12 A |
| Z = 20 Ω | R = 12 Ω | Xᶜ = 16 Ω |
| VA = 2880 | P = 1728 W | VARsᶜ = 2304 |
| PF = 60% leading, θ = 53.13° | — | C = 165.8 µF |

**Rules**

- **Series:** one current. Find it first.
- **Z** = √(R² + Xᶜ²). **Eₜ** = √(Eᵣ² + Eᶜ²). **VA** = √(P² + VARsᶜ²).
- **Xᶜ** = 1/(2πfC), C in farads. **C** = 1/(2πf Xᶜ).
- **PF** = P/VA = R/Z = Eᵣ/Eₜ = cos θ. **θ** = cos⁻¹(PF), current **leading**.
- **Other trig:** tan θ = Xᶜ/R, sin θ = Xᶜ/Z = Eᶜ/Eₜ.
- **Like adds to like** (watts, VARsᶜ, series Xᶜ's). Cross-group sums use the Pythagorean theorem.
- **Capacitor rating:** compare Eᶜ (× 1.414 if the rating is VDC), not the supply voltage.
