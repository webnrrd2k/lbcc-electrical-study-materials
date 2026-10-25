# Study Guide: Series RL, RC & RLC Practice Problems

Oct 22, 2026 · @Jeff

## What these problem sets test

All three worksheets have the same format. Each gives five series circuits with Eₜ and the ohm values (R, Xₗ, Xᶜ), and asks you to fill in the table:

| Worksheet | Unit | Problems | Blanks per problem |
| --- | --- | --- | --- |
| No. 6, Series RL | 17 | 5 (Q1–55) | 11: Z, PF, θ, Iᵣ, Iₗ, Iₜ, Eᵣ, Eₗ, VA, Watts, VARs |
| No. 7, Series RC | 21 | 5 (Q1–55) | 11: Z, PF, θ, Iᵣ, Iᶜ, Iₜ, Eᵣ, Eᶜ, VA, Watts, VARs |
| No. 8, Series RLC | 23 | 5 (Q1–65) | 13: adds Iₗ, Iᶜ, Eₗ, Eᶜ |

The skills are the same every time:

1. Combine R and X into Z with the Pythagorean theorem.
2. Use the fact that **current is the same everywhere in series**.
3. Use Ohm's law inside each group.
4. Build the power triangle.
5. Get PF and θ (and say leading or lagging).

The RLC set adds one step: subtract Xᶜ from Xₗ first.

**Two surprises to watch for:**

- Several problems use **kΩ**, so the current comes out in **milliamps** and the power in **milliwatts**.
- In one RLC problem, a component's voltage is **higher than the 120 V supply**.

**How to use this guide:** Work each problem yourself first using the method below, then check your table against the answer key under each worksheet. The first problem of each set is worked step by step.

## One Method for Every Series Problem

**Why it works:** in a series circuit there's only **one current**. Find it, and it unlocks every other blank, because each part's voltage and power is just that current times its own ohms.

| Step | Find | Formula | Notes |
| --- | --- | --- | --- |
| 1 | Net reactance X | RL: X = Xₗ. RC: X = Xᶜ. RLC: X = Xₗ − Xᶜ | RLC only: subtract, and note which is bigger |
| 2 | **Z** | √(R² + X²) | Never R + X |
| 3 | **Iₜ** | Eₜ / Z | Then Iᵣ = Iₗ = Iᶜ = Iₜ (series) |
| 4 | **Eᵣ, Eₗ, Eᶜ** | I × R, I × Xₗ, I × Xᶜ | Each part's own ohms |
| 5 | **Watts** | I² × R (or Eᵣ × I) | Resistor only |
| 6 | **VARs** | I² × X (or Eₓ × I) | RLC: net = VARsₗ − VARsᶜ |
| 7 | **VA** | Eₜ × Iₜ | Check: √(W² + VARs²) should match |
| 8 | **PF** | R / Z (= W/VA = Eᵣ/Eₜ) | × 100 for percent |
| 9 | **θ** | cos⁻¹(PF as a decimal) | Lagging if inductive; leading if capacitive |

**Built-in checks (use them on every problem)**

- √(Eᵣ² + (Eₗ − Eᶜ)²) should equal Eₜ. In RL and RC, use just the one reactive drop.
- √(W² + VARs²) should equal VA.
- W / VA, R / Z and Eᵣ / Eₜ should all give the same PF.
- The three triangles (impedance, voltage, power) all have the **same angle θ**.

**Calculator habits**

- Work in base units: convert kΩ to Ω (10 kΩ = 10,000 Ω). The current then comes out in amps; convert to mA at the end.
- Keep full precision in the calculator, and round only the final answers (2–3 decimal places is typical).
- DEG mode for cos⁻¹.

## Series RL Practice Problems (No. 6)

**Worked example: Q1–11** (Eₜ = 20 V, R = 10 kΩ, Xₗ = 6.5 kΩ)

1. Z = √(10,000² + 6,500²) = **11,926.9 Ω** (11.93 kΩ).
2. I = 20 / 11,926.9 = 0.001677 A = **1.677 mA**. So Iᵣ = Iₗ = Iₜ = 1.677 mA.
3. Eᵣ = 0.001677 × 10,000 = **16.77 V**. Eₗ = 0.001677 × 6,500 = **10.90 V**.
   - Check: √(16.77² + 10.90²) = 20 V ✓. (16.77 + 10.90 = 27.67 V is **not** supposed to equal 20 V.)
4. Watts = 16.77 × 0.001677 = **28.12 mW**. VARs = 10.90 × 0.001677 = **18.28 mVAR**. VA = 20 × 0.001677 = **33.54 mVA**.
5. PF = R / Z = 10,000 / 11,926.9 = **83.84%**. θ = cos⁻¹(0.8384) = **33.02°**, current lagging.

**Things to notice in this set**

- Q1–33 are kΩ circuits, so expect mA, mW, mVAR and mVA. Don't report 0.0017 A as "1.7 A".
- **Q34–44** (12 Ω and 9 Ω) is a 3-4-5 triangle: Z = 15 Ω exactly. A good confidence check.
- All five are inductive, so every PF is **lagging**.

**Answer key (check your work)**

| Q | Z | I (all) | Eᵣ | Eₗ | Watts | VARs | VA | PF | θ (lag) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1–11 | 11.93 kΩ | 1.677 mA | 16.77 V | 10.90 V | 28.12 mW | 18.28 mVAR | 33.54 mVA | 83.84% | 33.02° |
| 12–22 | 3.041 kΩ | 14.80 mA | 39.95 V | 20.71 V | 591.1 mW | 306.5 mVAR | 665.8 mVA | 88.78% | 27.41° |
| 23–33 | 4.140 kΩ | 6.039 mA | 19.93 V | 15.10 V | 120.3 mW | 91.16 mVAR | 151.0 mVA | 79.71% | 37.15° |
| 34–44 | 15 Ω | 8 A | 96 V | 72 V | 768 W | 576 VAR | 960 VA | 80.00% | 36.87° |
| 45–55 | 14.42 Ω | 16.64 A | 199.7 V | 133.1 V | 3323 W | 2215 VAR | 3994 VA | 83.21% | 33.69° |

Small differences in the last digit come from rounding and are fine.

## Series RC Practice Problems (No. 7)

Same method as RL. The only differences are that the reactive part is Xᶜ, and the current **leads**.

**Worked example: Q1–11** (Eₜ = 45 V, R = 2.7 kΩ, Xᶜ = 3.8 kΩ)

1. Z = √(2,700² + 3,800²) = **4,661.5 Ω** (4.662 kΩ).
2. I = 45 / 4,661.5 = **9.653 mA**, the same through R and C.
3. Eᵣ = 0.009653 × 2,700 = **26.06 V**. Eᶜ = 0.009653 × 3,800 = **36.68 V**. Check: √(26.06² + 36.68²) = 45 V ✓.
4. Watts = **251.6 mW**, VARs = **354.1 mVAR**, VA = 45 × 0.009653 = **434.4 mVA**.
5. PF = 2,700 / 4,661.5 = **57.92%**. θ = **54.61°**, current **leading**.

**Things to notice in this set**

- **Q1–11 is the only problem where X is bigger than R**, so it has the lowest PF and largest angle of the set, and Eᶜ (36.7 V) is bigger than Eᵣ.
- Q12–33 have small ohm values but small voltages too, so the currents are in mA again (295 mA, 69.4 mA).
- Every PF here is **leading**. Write "leading" next to θ.
- These sheets give Xᶜ directly. You don't need C or 1/(2πfC) unless your instructor asks for it.

**Answer key (check your work)**

| Q | Z | I (all) | Eᵣ | Eᶜ | Watts | VARs | VA | PF | θ (lead) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1–11 | 4.662 kΩ | 9.653 mA | 26.06 V | 36.68 V | 251.6 mW | 354.1 mVAR | 434.4 mVA | 57.92% | 54.61° |
| 12–22 | 67.91 Ω | 294.5 mA | 17.67 V | 9.37 V | 5.20 W | 2.76 VAR | 5.89 VA | 88.36% | 27.92° |
| 23–33 | 144.0 Ω | 69.44 mA | 8.33 V | 5.53 V | 578.7 mW | 383.9 mVAR | 694.4 mVA | 83.33% | 33.56° |
| 34–44 | 17.49 Ω | 6.860 A | 102.9 V | 61.74 V | 705.9 W | 423.5 VAR | 823.2 VA | 85.75% | 30.96° |
| 45–55 | 31.40 Ω | 3.822 A | 95.54 V | 72.61 V | 365.1 W | 277.5 VAR | 458.6 VA | 79.62% | 37.23° |

## Series RLC Practice Problems (No. 8)

**The one new step:** Xₗ and Xᶜ are 180° apart, so **subtract them first** (net X = Xₗ − Xᶜ). Then it's just like RL or RC. Whichever reactance is bigger decides leading or lagging.

**Worked example: Q1–13** (120 V, R = 40 Ω, Xₗ = 35 Ω, Xᶜ = 15 Ω)

1. Net X = 35 − 15 = **20 Ω inductive**.
2. Z = √(40² + 20²) = **44.72 Ω**.
3. I = 120 / 44.72 = **2.683 A**, so Iᵣ = Iₗ = Iᶜ = Iₜ = 2.683 A.
4. Eᵣ = 2.683 × 40 = **107.3 V**. Eₗ = 2.683 × 35 = **93.91 V**. Eᶜ = 2.683 × 15 = **40.25 V**.
   - Check: √(107.3² + (93.91 − 40.25)²) = 120 V ✓.
5. Watts = I²R = **288 W**. VARsₗ = I²Xₗ = 252 and VARsᶜ = I²Xᶜ = 108, so **net VARs = 144** (inductive). VA = 120 × 2.683 = **322.0 VA**.
6. PF = 40 / 44.72 = **89.44%**. θ = **26.57° lagging**.

**What goes in the single "VARs" box?** The worksheet has one VARs cell, so enter the **net** reactive power (VARsₗ − VARsᶜ). That's the value that fits the power triangle with Watts and VA. If your instructor wants VARsₗ and VARsᶜ separately, they're in the key below.

**Things to notice in this set**

- **Q14–26 is the only capacitive one** (Xᶜ 75 > Xₗ 45), so its PF is **leading**. The rest are lagging.
- **Q40–52** gives a 3-4-5 shape: net X = 30, R = 40, so Z = 50 Ω exactly. Easy to check.
- **Q40–52: Eₗ = 108 V**, close to the 120 V supply.
- **Q53–65: Eₗ = 159 V on a 120 V supply.** That's not a mistake. Eₗ and Eᶜ partly cancel, so a single component can exceed the source voltage.
- Q27–39 has R much bigger than the net X, so the PF is almost 98%.

**Answer key (check your work)**

| Q | Net X | Z | I (all) | Eᵣ | Eₗ | Eᶜ | Watts | Net VARs | VA | PF | θ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1–13 | 20 Ω L | 44.72 Ω | 2.683 A | 107.3 V | 93.91 V | 40.25 V | 288.0 W | 144.0 | 322.0 VA | 89.44% | 26.57° lag |
| 14–26 | 30 Ω C | 104.4 Ω | 1.149 A | 114.9 V | 51.72 V | 86.20 V | 132.1 W | 39.63 | 137.9 VA | 95.78% | 16.70° lead |
| 27–39 | 30 Ω L | 143.2 Ω | 838.1 mA | 117.3 V | 37.72 V | 12.57 V | 98.34 W | 21.07 | 100.6 VA | 97.78% | 12.09° lag |
| 40–52 | 30 Ω L | 50.00 Ω | 2.400 A | 96.00 V | 108.0 V | 36.00 V | 230.4 W | 172.8 | 288.0 VA | 80.00% | 36.87° lag |
| 53–65 | 336 Ω L | 418.8 Ω | 286.5 mA | 71.63 V | 159.0 V | 62.75 V | 20.52 W | 27.59 | 34.38 VA | 59.69% | 53.35° lag |

**Separate VARs, if asked:**

| Q | VARsₗ | VARsᶜ |
| --- | --- | --- |
| 1–13 | 252.0 | 108.0 |
| 14–26 | 59.45 | 99.08 |
| 27–39 | 31.61 | 10.54 |
| 40–52 | 259.2 | 86.40 |
| 53–65 | 45.57 | 17.98 |

## Mistakes These Worksheets Are Built to Catch

1. **Adding R + X for Z.** Q34–44 on the RL sheet would give 21 Ω instead of 15 Ω. Always use the Pythagorean theorem.
2. **Adding the voltage drops straight.** Eᵣ + Eₗ won't equal Eₜ, and it isn't supposed to. Only √(Eᵣ² + Eₓ²) equals Eₜ.
3. **kΩ slip-ups.** Using 10 instead of 10,000 gives a current 1000× too big. Convert to ohms first, then express the answer in mA.
4. **Mixing groups in Ohm's law.** Eᵣ = I × R, not I × Z. Watts = I²R, not Eₜ × I (that's VA).
5. **Forgetting to subtract in RLC.** √(R² + Xₗ² + Xᶜ²) and √(R² + (Xₗ + Xᶜ)²) are both wrong.
6. **Leaving off leading/lagging.** All RL answers are lagging and all RC answers are leading. In RLC, the bigger reactance decides (only Q14–26 leads).
7. **PF as a percent inside cos⁻¹.** Use 0.8944, not 89.44.
8. **Rounding too early.** Round I to 2 places and your watts can drift. Keep the full value in the calculator.
9. **Writing different currents for different parts.** It's series: Iᵣ, Iₗ, Iᶜ and Iₜ are **all the same number**. Those four blanks get the same value.
10. **Thinking a component voltage above the supply is an error.** In RLC (Q53–65) it's real. It's also why capacitor voltage ratings matter.

## Formula Sheet

| Quantity | Series RL | Series RC | Series RLC |
| --- | --- | --- | --- |
| Net X | Xₗ | Xᶜ | Xₗ − Xᶜ |
| Z | √(R² + Xₗ²) | √(R² + Xᶜ²) | √(R² + (Xₗ − Xᶜ)²) |
| I (everywhere) | Eₜ / Z | Eₜ / Z | Eₜ / Z |
| Drops | Eᵣ = IR, Eₗ = IXₗ | Eᵣ = IR, Eᶜ = IXᶜ | Eᵣ = IR, Eₗ = IXₗ, Eᶜ = IXᶜ |
| Eₜ check | √(Eᵣ² + Eₗ²) | √(Eᵣ² + Eᶜ²) | √(Eᵣ² + (Eₗ − Eᶜ)²) |
| Watts | I²R | I²R | I²R |
| VARs | I²Xₗ | I²Xᶜ | I²(Xₗ − Xᶜ) (net) |
| VA | Eₜ × I | Eₜ × I | Eₜ × I |
| PF | R/Z = W/VA = Eᵣ/Eₜ | same | same |
| θ | cos⁻¹(PF), lagging | cos⁻¹(PF), leading | cos⁻¹(PF), lag if Xₗ > Xᶜ, lead if Xᶜ > Xₗ |

**If a test gives L or C instead of ohms:** Xₗ = 2πfL and Xᶜ = 1/(2πfC). At 60 Hz, 2πf = 377. Convert first, then follow the table.

For the theory behind each step, see the Unit 17 (R-L series), Unit 21 (R-C series) and Unit 23 (R-L-C series) study guides.
