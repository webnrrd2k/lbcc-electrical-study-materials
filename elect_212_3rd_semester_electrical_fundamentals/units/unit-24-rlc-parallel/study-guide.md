# Unit 24 Study Guide: R-L-C Parallel Circuits

Oct 22, 2026 · @Jeff

## Why this chapter matters

This is the last of the circuit-solving units, and the most practical. Real plant wiring is **parallel**: motors, lights, heaters and PF capacitors all hang across the same line. This chapter shows how inductive and capacitive **currents** cancel in parallel. That one idea explains three things you'll meet on the job:

- **Power-factor correction:** sizing a capacitor to cut a motor's line current. The book gives a step-by-step method.
- **Tank circuits** (parallel resonance): tiny line current with huge circulating current. Used in induction heating and metal-detecting proximity sensors.
- **Why feeder current can be less than a single branch current.**

The main example is R = 12 Ω, Xₗ = 8 Ω and Xᶜ = 16 Ω in parallel on 240 V, 60 Hz.

**Series vs parallel R-L-C at a glance**

|  | Series (Unit 23) | Parallel (Unit 24) |
| --- | --- | --- |
| Shared | Current | Voltage |
| What cancels | Eₗ vs Eᶜ (voltages) | Iₗ vs Iᶜ (currents) |
| Surprise | A component's **voltage** can exceed the supply | A branch's **current** can exceed the line current |
| At resonance | Z minimum, current maximum | Z maximum, line current minimum |
| Leading/lagging decided by | Bigger reactive **voltage** (bigger X) | Bigger reactive **current** (smaller X) |

## 24–1 How Iₗ and Iᶜ Cancel in Parallel

**Intuition:** All three branches see the same voltage. The coil's current lags that voltage by 90° and the capacitor's current leads it by 90°, so they're 180° apart. At every instant, while current flows **into** the coil it's flowing **out of** the capacitor. Much of the reactive current just sloshes back and forth between L and C and never goes out on the line.

**Branch phases (relative to the shared voltage)**

| Branch | Current vs voltage |
| --- | --- |
| Resistor | In phase |
| Inductor | Iₗ **lags** 90° |
| Capacitor | Iᶜ **leads** 90° |

**Net reactive current:** Iₗ − Iᶜ. The smaller one is eliminated and the larger is reduced.

**Leading or lagging?**

- Iₗ > Iᶜ (VARsₗ > VARsᶜ): net inductive, **lagging** PF.
- Iᶜ > Iₗ: net capacitive, **leading** PF.
- In parallel, the **smaller** reactance draws the **bigger** current and wins. In the example, Xₗ = 8 Ω beats Xᶜ = 16 Ω, so it's inductive. That's the reverse of series, where the bigger reactance wins.

**Pitfall:** Deciding leading or lagging by which reactance is **larger**. In parallel, look at currents or VARs, not ohms.

## Branch Currents, Total Current and Impedance

**Branches (Ohm's law with the full 240 V):**

- Iᵣ = 240/12 = **20 A**, so P = 4800 W.
- Iₗ = 240/8 = **30 A**, so VARsₗ = 7200. L = 8/377 = 0.0212 H.
- Iᶜ = 240/16 = **15 A**, so VARsᶜ = 3600. C = 1/(377 × 16) = 165.8 µF.

**Total current**

```math
I_T = \sqrt{I_R^2 + (I_L - I_C)^2}
```

√(20² + (30 − 15)²) = √(400 + 225) = **25 A**. The line carries 25 A while the coil alone carries 30 A. **A branch can carry more current than the line.**

**Impedance: three ways**

1. **Ohm's law (easiest):** Z = E / Iₜ = 240 / 25 = **9.6 Ω**.
2. **Reciprocal (vector) formula:**

```math
Z = \frac{1}{\sqrt{\left(\frac{1}{R}\right)^2 + \left(\frac{1}{X_L} - \frac{1}{X_C}\right)^2}}
```

3. **Combine the reactances first, then product over vector sum:** X = (Xₗ × Xᶜ) / (Xₗ + Xᶜ), with Xᶜ entered as **negative**. That gives X = (8 × −16) / (8 − 16) = 16 Ω, inductive since the result is positive. Then Z = R·X / √(R² + X²) = 192 / 20 = **9.6 Ω**.

**Calculator tip (the book's key sequence):** 12 \[1/x\] \[x²\] + ( 8 \[1/x\] − 16 \[1/x\] ) \[x²\] = \[√\] \[1/x\]. Let the calculator carry full precision.

**Example 24–2 (1200 Hz, given L and C):** convert first. Xₗ = 2π × 1200 × 0.00976 = 73.59 Ω, and Xᶜ = 1/(2π × 1200 × 5.5 µF) = 24.11 Ω. Then Z ≈ **16.1 Ω**. Note the book's typo of 74.589 Ω in the substitution.

**Pitfalls**

- Iₜ ≠ Iᵣ + Iₗ + Iᶜ, and Iₜ ≠ √(Iᵣ² + Iₗ² + Iᶜ²). Subtract the reactive currents first.
- Subtract the **reciprocals** 1/Xₗ − 1/Xᶜ, not Xₗ − Xᶜ, in the parallel formula.
- Losing the sign of Xᶜ in the X = XₗXᶜ/(Xₗ + Xᶜ) formula.

## Power, Power Factor and Angle Theta

| Quantity | Formula | Example |
| --- | --- | --- |
| P | E × Iᵣ | 4800 W |
| VARsₗ | E × Iₗ | 7200 |
| VARsᶜ | E × Iᶜ | 3600 |
| VA | E × Iₜ, or √(P² + (VARsₗ − VARsᶜ)²) | 6000 |

- **PF** = P / VA = 4800 / 6000 = **80%**. In parallel, Iᵣ / Iₜ = 20/25 and Z / R = 9.6/12 also work.
- **θ** = cos⁻¹(0.8) = **36.87°**, current **lagging** (more inductive VARs).
- Other trig: tan θ = (Iₗ − Iᶜ) / Iᵣ = (VARsₗ − VARsᶜ) / P.

**Pitfall:** In parallel, PF = Z/R, not R/Z, and voltage ratios are useless (E is the same on every branch).

## 24–2 Parallel Resonance and the Tank Circuit

**Intuition:** At resonance, Xₗ = Xᶜ, so Iₗ = Iᶜ exactly. They cancel on the line. Energy swings back and forth between the coil's magnetic field and the capacitor's electric field, like water sloshing in a tank. That's why it's called a **tank circuit**. The source only has to make up the small energy lost in the coil's resistance each cycle.

**Parallel resonance vs series resonance**

|  | Series resonance | Parallel resonance (tank) |
| --- | --- | --- |
| Impedance | **Minimum** (= R) | **Maximum** |
| Line current | **Maximum** | **Minimum** |
| What's magnified | Voltage across L and C | Current circulating inside L-C |
| Resonant frequency | fᵣ = 1/(2π√(LC)) | Same formula |

**In theory** (perfect parts) the line current would be zero and Z infinite. **In practice** the coil's resistance sets them. Capacitors have very high Q, so the **coil's Q** is the limit.

**Q of a tank circuit**

- Q = Xₗ / R (coil) = I(tank) / I(line).
- I(tank) = I(line) × Q, and I(line) = I(tank) / Q.

**Book example:** 0.0398 H with 10 Ω of wire resistance, 0.442 µF, 480 V. Resonance at 1200 Hz, where Xₗ = Xᶜ = 300 Ω.

1. Each branch: 480 / 300 = **1.6 A** circulating in the tank.
2. Q = 300 / 10 = 30.
3. Line current = 1.6 / 30 = **0.0533 A**.
4. Check by watts: P = I²R = 1.6² × 10 = 25.6 W, so I = P/E = 25.6 / 480 = 0.0533 A ✓.
5. Z = 480 / 0.0533 ≈ **9000 Ω**. The book's 9006 Ω comes from rounding the current.

**Bandwidth:** the frequencies on either side of resonance where the impedance falls to 0.707 × maximum. High Q gives a narrow bandwidth; low Q gives a wide one (same idea as series).

**Applications**

- **Induction heating:** the work coil is the L and the pipe or part is its core. With Q = 10, a 100 A line current drives 1000 A in the tank. The circuit only resonates with the part in the coil, because the part changes L. Frequency sets heating depth: **≤ 400 Hz** heats through evenly; **≥ 1000 Hz**, skin effect concentrates the heat at the surface for **case hardening**.
- **Inductive proximity sensors:** a small tank oscillator. Metal near the face adds eddy-current losses, Q collapses, the oscillation drops, and the sensor switches.
- **Filters** in electronics: they pass or block one frequency.

**Pitfall:** "Line current is tiny, so the parts are lightly loaded." Wrong. The inductor and capacitor each carry the **full** tank current (Q times the line current), and must be rated for it.

## Power-Factor Correction (Step by Step)

**Intuition:** A motor draws in-phase current for the work and lagging current to magnetize its iron. A capacitor **in parallel** supplies leading current that cancels much of the lagging part locally, so the line only carries what's left. The motor runs exactly the same; the feeder current drops.

**Motor model:** a motor looks like R in series with L. The **inductive (magnetizing) part stays roughly constant**. The resistive part grows with load (it represents the mechanical work). At no load, it's mostly inductive with low PF. At full load, it's mostly resistive with higher PF.

**Book method:** 240 V, 60 Hz, 10 A, 1630 W, corrected to **95%**.

1. **Existing VA and PF:** VA = 240 × 10 = 2400. PF = 1630 / 2400 = **67.9%**.
2. **Existing VARs:** VARsₗ = √(2400² − 1630²) = **1761.6**.
3. **VA at the target PF** (the watts don't change): VA = 1630 / 0.95 = **1715.8**.
4. **VARs allowed at the target:** √(1715.8² − 1630²) = **535.8**.
5. **Capacitive VARs to add:** 1761.6 − 535.8 = **1225.8 VARsᶜ**.
6. **Xᶜ needed:** Xᶜ = E² / VARsᶜ = 240² / 1225.8 = **46.99 Ω**.
7. **Capacitance:** C = 1 / (377 × 46.99) = **56.45 µF**, connected in **parallel** with the motor.

**Result:** the line current drops from 10 A to 1715.8 / 240 ≈ **7.15 A**. The motor's own current is unchanged.

**Shortcuts**

- For unity (100%): add VARsᶜ equal to all the existing VARsₗ (Review Q6).
- Steps 3–4 combined: VARs at the target = P × tan(cos⁻¹ PF).

**Why stop at about 95%?** Each extra point of PF needs more and more kVAR for less and less current reduction. Overshooting makes the PF **leading**, raising the voltage.

**Book claim to question:** it says once corrected, the PF "will remain constant regardless of the motor load." Not really. The magnetizing VARs (and the capacitor's VARs) stay about the same, but the **watts drop at light load**, so the PF falls again. And if the capacitor is sized too big, it can **overcorrect** when the motor is lightly loaded.

## Book Errors and Wording Slips

| Where | Book says | Should be |
| --- | --- | --- |
| Example 24–2 substitution | 74.589 Ω | 73.589 Ω (its own Xₗ). Also shows 1/R as 0.05552 inside a squared sum; it should be (1/18)². The final Z ≈ 16.1 Ω is about right. |
| Tank example | Z = 9006.63 Ω (text), 9005.629 (figure) | 480 / (1.6/30) = **9000 Ω** exactly. The difference is rounding 0.0533 A. |
| PF correction, step 1 | PF = 0679 | **0.679** (67.9%) |
| PF correction, step 5 | "reduce the inductive VARs from 1715.789 to 535.754" | From **1761.562**. 1715.789 is the target **VA**, not VARs. The arithmetic shown is correct. |
| Motor model | "PF will remain constant regardless of the motor load" | PF still changes with load (see above). |
| Summary | "The same amount of capacitive VARs must be connected as inductive VARs" | Only for **unity** PF. For 95%, you add less. |

## Easily overlooked things for electricians

1. **PF capacitors and the NEC (Article 460).** When a capacitor is connected on the **load side of the motor overload**:
   - Its kVAR must not exceed the amount needed to raise the motor's **no-load** PF to unity (460.7). Oversizing can cause **self-excitation**: when the motor is switched off, it keeps generating voltage while it coasts.
   - The overload setting must be based on the **reduced** line current after correction (460.9). The overload now sees less current than the motor actually draws.
2. **Where the capacitor goes changes what's corrected.** At the motor, the branch circuit's current drops too. At the service, only the utility side improves. Switched or automatic banks track the load and avoid running leading at night.
3. **Branch current can exceed line current.** In a resonant or near-resonant circuit, the inductor or capacitor branch can carry many times the feeder current. Size and fuse the parts for their branch current, not the line.
4. **Harmonic resonance (again).** A PF bank in parallel with the system inductance is a tank circuit. At a harmonic frequency it can show **very high impedance**, magnifying harmonic voltages and currents. That's the reason for detuned banks on systems with drives.
5. **Induction heating and proximity sensors are tank circuits.** Changing the load (the part, a metal target) changes L or Q and detunes the circuit. That's what makes both of them work.
6. **Measuring PF in the field:** a wattmeter (or power analyzer) plus a clamp ammeter and a voltmeter give P and VA, so PF = P / VA. That's exactly the book's first step.

## Notes on the homework

- **General method:** In parallel, E is shared, so get it first. Branch currents by Ohm's law. Iₜ = √(Iᵣ² + (Iₗ − Iᶜ)²). Then Z = E / Iₜ, powers, PF, θ. State leading or lagging.
- **Q1 (400 Hz):** 377 doesn't apply. Xₗ = 2π × 400 × 0.0159 and Xᶜ = 1/(2π × 400 × 13.3 µF). Then the branch currents and the rest.
- **Q2:** Use 1/√((1/16)² + (1/8 − 1/20)²), or the X-combining method. The answer must be smaller than 8 Ω.
- **Q3:** √(38² + (22 − 7)²).
- **Q4 (tank, 30 Ω reactance, Q = 15, 277 V):** Tank current = 277/30. Line current = tank current ÷ 15.
- **Q5:** For resonance, Xᶜ must equal Xₗ = 50 Ω at 10 kHz, so C = 1/(2π × 10,000 × 50). Or use C = 1/(4π²f²L).
- **Q6 (unity correction):** VARsᶜ needed = all of the existing VARsₗ = √((560 × 53)² − 18,700²). Then Xᶜ = 560² / VARsᶜ and C = 1/(377 × Xᶜ).
- **Practical Application (15 A, 2.2 kW, 240 V, correct to 95%):** Follow the seven steps exactly as in the PF correction section.
- **Practice 2 (400 Hz):** Net VARs = 5760 − 1920 = 3840 capacitive. VA = √(3840² + 3840²). E = VA / Iₜ.
- **Practice 4:** E = Iₜ × Z, after Iₜ = √(60² + (150 − 70)²).
- **Practice 7:** Net VARs = 760 − 360 = 400 capacitive. θ = tan⁻¹(400/260), **leading**.
- **Practice 8:** P = √(400² − (450 − 200)²).
- **Practice 9:** Eᶜ = E = Iᵣ × R (parallel, so the same voltage everywhere).
- **Practice 10:** VA = 600 / 0.75, then Iₜ = VA / 240.

## One-glance cheat sheet

**Book example, all values (240 V, 60 Hz, R 12 Ω ‖ Xₗ 8 Ω ‖ Xᶜ 16 Ω)**

| Total | Resistive | Inductive | Capacitive |
| --- | --- | --- | --- |
| E = 240 V | 240 V | 240 V | 240 V |
| Iₜ = 25 A | Iᵣ = 20 A | Iₗ = 30 A | Iᶜ = 15 A |
| Z = 9.6 Ω | R = 12 Ω | Xₗ = 8 Ω | Xᶜ = 16 Ω |
| VA = 6000 | P = 4800 W | VARsₗ = 7200 | VARsᶜ = 3600 |
| PF 80% lagging, θ 36.87° | — | L = 0.0212 H | C = 165.8 µF |

**Rules**

- **Same voltage everywhere.** Iᵣ in phase, Iₗ lags 90°, Iᶜ leads 90°. Iₗ and Iᶜ are 180° apart and **subtract**.
- **Iₜ** = √(Iᵣ² + (Iₗ − Iᶜ)²). **VA** = √(P² + (VARsₗ − VARsᶜ)²).
- **Z** = E/Iₜ = 1/√((1/R)² + (1/Xₗ − 1/Xᶜ)²).
- **More Iₗ (smaller Xₗ)** means lagging. **More Iᶜ** means leading.
- **PF** = P/VA = Iᵣ/Iₜ = Z/R. θ = cos⁻¹(PF).
- **Tank (parallel resonance):** Xₗ = Xᶜ. Z is **maximum** and line I is **minimum**. Q = Xₗ/R = I(tank)/I(line). I(tank) = Q × I(line).
- **fᵣ** = 1/(2π√(LC)). L = 1/(4π²f²C), C = 1/(4π²f²L).
- **PF correction:** VARs now − VARs at target = VARsᶜ to add. Xᶜ = E²/VARsᶜ. C = 1/(2πf Xᶜ). Connect in **parallel**. Aim for about 95%.
