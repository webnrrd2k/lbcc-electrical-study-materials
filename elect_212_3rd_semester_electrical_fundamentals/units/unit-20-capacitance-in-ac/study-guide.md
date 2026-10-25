# Unit 20 Study Guide: Capacitance in AC Circuits

Oct 22, 2026 · @Jeff

## Why this chapter matters

Capacitors are the third AC load type and the **mirror image of inductors**. This unit shows how a capacitor limits AC current (capacitive reactance), why its current **leads** the voltage, and how to read its voltage rating correctly. Those three ideas are the foundation for power-factor correction, motor run capacitors and the R-C and R-L-C circuits in the next units.

**Inductor vs capacitor in AC**

|  | Inductor | Capacitor |
| --- | --- | --- |
| Reactance formula | Xₗ = 2πfL | Xᶜ = 1 / (2πfC) |
| Raise frequency → reactance | goes **up** | goes **down** |
| Raise L or C → reactance | goes up | goes **down** |
| Current vs voltage | current **lags** 90° (ELI) | current **leads** 90° (ICE) |
| True power (pure) | 0 W | 0 W |
| VARs | VARsₗ | VARsᶜ, 180° opposite VARsₗ |
| Q | Xₗ / R (R in series) | R / Xᶜ (R = dielectric leakage) |
| Series combination of the *component* | add | reciprocal |
| Series combination of the *reactance* | add | **add** |

## 20–1 How Current "Flows" Through a Capacitor on AC

**Intuition:** Picture two tanks joined by a pump that keeps reversing (Figure 20–2). Water flows back and forth in the pipes all the time, but never passes from one tank directly into the other. A capacitor on AC is the same: electrons rush onto one plate, then back off it and onto the other, every half-cycle. An ammeter in the line reads a steady current, even though no electrons cross the dielectric.

**Core facts**

- No current passes **through** the dielectric (it's an insulator). Current flows **in the circuit** because the capacitor keeps charging, discharging and recharging the other way.
- That's why the book says current "**appears to flow**" through a capacitor. (Review Q1: no electrons cross the dielectric, but AC current does flow in the circuit.)
- On DC, the capacitor charges once and current stops (Unit 19). On AC the voltage never stops changing, so the current never stops.

**Common misunderstanding:** "A capacitor blocks AC." It's the reverse: capacitors **block steady DC** and **pass AC**, and they pass higher frequencies more easily.

## 20–2, 20–3, 20–8 Capacitive Reactance (Xᶜ)

**Intuition:** As the capacitor charges, its own voltage (the **impressed voltage**, or countervoltage) pushes back against the supply and limits the current. That push-back, expressed in ohms, is capacitive reactance.

- A **bigger** capacitor holds more charge before its voltage builds up, so it pushes back **less**.
- A **higher frequency** reverses the voltage before the capacitor gets very full, so it also pushes back **less**.

**Formula**

```math
X_C = \frac{1}{2\pi f C}
```

- **Xᶜ:** capacitive reactance in ohms. **f:** frequency in Hz. **C:** capacitance in **farads**.
- At 60 Hz: Xᶜ = 1 / (377 × C).
- Rearranged: C = 1 / (2πf Xᶜ) and f = 1 / (2π C Xᶜ).
- Ohm's law with Xᶜ in place of R: I = E / Xᶜ, Xᶜ = E / I, E = I × Xᶜ.

**Worked examples**

- 35 µF on 120 V, 60 Hz: Xᶜ = 1 / (377 × 0.000035) = **75.79 Ω**, so I = 120 / 75.79 = **1.58 A** (Example 20–1).
- 480 V, 60 Hz, 2.6 A: Xᶜ = 480 / 2.6 = 184.6 Ω, so C = 1 / (377 × 184.6) = **14.37 µF** (Example 20–2).

**Two factors that set Xᶜ** (Review Q2): **capacitance** and **frequency**. Xᶜ is **inversely** proportional to both.

**Frequency effect (20–8)**

- Double the frequency and Xᶜ halves, so the current doubles.
- Why: current is charge per second (I = Q / t). At a higher frequency the capacitor moves the same charge in less time.
- Shortcut: Xᶜ(new) = Xᶜ(old) × f(old) / f(new). Practice 6: 300 Ω at 60 Hz gives 300 × 60/100 = 180 Ω at 100 Hz.

**Exceptions and pitfalls**

- **C must be in farads.** 35 µF = 0.000035 F. This is the most common error. Watch nF (10⁻⁹) and pF (10⁻¹²) too.
- **At DC (f = 0), Xᶜ is infinite**, so the capacitor blocks steady DC. The opposite of an inductor, where Xₗ = 0 at DC.
- **The formula has the 2πfC on the bottom.** Typing 2πfC and forgetting the reciprocal gives a tiny number instead of the reactance. Use the 1/x key.
- **Book table errors (Table 20–1):** three entries are labeled kΩ but are actually ohms. 470 nF at 400 Hz = **846.6 Ω**. 470 nF at 1000 Hz = **338.6 Ω**. 750 nF at 400 Hz = **530.5 Ω**.

## 20–9 and 20–10 Capacitors in Series and Parallel

**Intuition:** Reactances behave like resistances: they add in series and use reciprocals in parallel. Capacitance does the **opposite** (Unit 19). Keep the two straight and these problems are just Ohm's law.

|  | Series | Parallel |
| --- | --- | --- |
| Total **reactance** | Xᶜₜ = Xᶜ₁ + Xᶜ₂ + Xᶜ₃ | 1/Xᶜₜ = 1/Xᶜ₁ + 1/Xᶜ₂ + 1/Xᶜ₃ |
| Total **capacitance** | 1/Cₜ = 1/C₁ + 1/C₂ + 1/C₃ | Cₜ = C₁ + C₂ + C₃ |
| Same everywhere | Current | Voltage |
| VARs | Add | Add |

**Series example (20–4):** 10, 30 and 15 µF on 480 V, 60 Hz.

1. Xᶜ's: 265.25, 88.42 and 176.84 Ω. They're all at the same angle, so they **add**: Xᶜₜ = 530.5 Ω.
2. Cₜ = 5 µF (reciprocal formula), and 1 / (377 × 530.5) also gives 5 µF. Two routes, same answer.
3. I = 480 / 530.5 = **0.905 A**, the same through each capacitor.
4. Drops: E = I × Xᶜ gives 240, 80 and 160 V. **The smallest capacitor (10 µF) takes the biggest share.** Unlike R-L circuits, these drops add straight (240 + 80 + 160 = 480 V), because they're all in phase with each other.
5. VARs: 217 + 72 + 145 = **434.5 VARs**.

**Parallel example (20–5):** 50, 75 and 20 µF, with 787 VARs total, 60 Hz.

1. Xᶜ's: 53.05, 35.37 and 132.6 Ω. Parallel reciprocal gives Xᶜₜ = 18.29 Ω.
2. Voltage from VARs and Xᶜ: E = √(VARs × Xᶜₜ) = √(787 × 18.29) ≈ **120 V**.
3. Branch currents: 2.26, 3.39 and 0.905 A. They add straight to 6.56 A (same angle).
4. Cₜ = 145 µF.

**Pitfalls**

- Combining capacitance the resistor way. Reactance follows resistor rules; capacitance doesn't.
- In series, **check every capacitor's voltage rating**. The drops are uneven, and the smallest capacitor sees the most voltage.
- Same-type reactive quantities add straight. The Pythagorean theorem is only for mixing R with X.

## 20–4 Voltage and Current: Current Leads by 90°

**The result:** In a pure capacitive circuit, **current leads the applied voltage by 90°**. (Review Q3, Q4.) Memory aid: **ICE**, meaning in a capacitor (C), current (I) comes before voltage (E).

**Why, step by step**

- The charge follows the applied voltage exactly (Q = C × V). The charge is zero when the voltage is zero and maximum when the voltage is maximum.
- **Current is the rate the charge changes.** At 0° the voltage is changing fastest, so current is **maximum**. At 90° the voltage is at its peak and momentarily not changing, so current is **zero**.
- So the current peaks a quarter cycle **before** the voltage does.
- The capacitor's impressed (counter) voltage is 180° from the applied voltage, just as an inductor's CEMF is.

**Contrast to remember**

- Inductor: current **lags** 90° (it fights changes in current).
- Capacitor: current **leads** 90° (it fights changes in voltage).
- Resistor: in phase.

**Exception:** exactly 90° only for a perfect capacitor. Real capacitors are very close (high Q), much closer than real inductors.

**Misunderstanding:** "Leads" doesn't mean the current exists before the voltage is switched on. It means that in steady AC, the current's peaks and zero crossings come 90° earlier in each cycle.

## 20–5 Power in a Capacitive Circuit (VARsᶜ)

**Intuition:** Like an inductor, a capacitor borrows energy and hands it back. For a quarter cycle it charges, storing energy in its electrostatic field. The next quarter it discharges, returning it. Net true power: **zero watts**.

**Facts**

- P = E × I × cos θ. With θ = 90°, cos 90° = 0, so P = 0 W.
- Capacitor power is **reactive**, measured in VARs: VARsᶜ = Eᶜ × Iᶜ = I² × Xᶜ = E² / Xᶜ.
- **Capacitive VARs and inductive VARs are 180° apart.** They point in opposite directions and **cancel each other**. That one fact is the whole basis of power-factor correction.
- Label them VARsᶜ and VARsₗ so you don't mix them up.

**Pitfall:** Don't add VARsᶜ and VARsₗ as if they were the same kind. You **subtract** them. (That's next unit's R-L-C math.)

**Trade preview:** A plant drawing lagging (inductive) VARs from its motors adds capacitor banks rated in **kVAR** to supply leading (capacitive) VARs locally. The utility then only has to deliver the difference, so the current and losses drop and PF rises.
