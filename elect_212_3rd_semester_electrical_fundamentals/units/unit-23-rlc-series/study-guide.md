# Unit 23 Study Guide: R-L-C Series Circuits

Oct 22, 2026 · @Jeff

## Why this chapter matters

This is where everything from Units 16–22 comes together. With R, L and C all in one series loop, the inductor and capacitor **fight each other**: their reactances (and VARs) point in opposite directions and partly cancel. That cancellation explains three things you'll meet in the field:

- Why a circuit's PF can be **leading or lagging** depending on which reactance wins.
- Why the voltage across a coil or capacitor can be **far higher than the supply**.
- **Resonance:** at one frequency the reactances cancel completely, the current jumps, and the component voltages can climb to dangerous levels.

The chapter's main example is R = 12 Ω, Xₗ = 24 Ω and Xᶜ = 8 Ω in series on 240 V, 60 Hz.

**The four groups now:**

| Resistive | Inductive | Capacitive | Total |
| --- | --- | --- | --- |
| R | Xₗ | Xᶜ | Z |
| Eᵣ | Eₗ | Eᶜ | Eₜ |
| P (W) | VARsₗ | VARsᶜ | VA |
| — | L | C | PF, θ |

Current is shared by all four groups (series). Ohm's law works inside one column. Inductive and capacitive columns **subtract**, and the net result combines with resistance by the Pythagorean theorem.

## 23–1 How Xₗ and Xᶜ Cancel in Series

**Intuition:** In a series loop, one current flows through everything. The inductor's voltage peaks 90° **ahead** of that current, and the capacitor's voltage peaks 90° **behind** it. That puts them 180° apart, exactly opposite. At every instant, when the coil pushes one way, the capacitor pushes the other. So they cancel, and only the **difference** is left to oppose the current.

**Phase of each drop relative to the shared current** (Review Q1–3)

| Component | Voltage vs current |
| --- | --- |
| Resistor | In phase |
| Inductor | Eₗ **leads** I by 90° |
| Capacitor | Eᶜ **lags** I by 90° |

**Net reactance:** X = Xₗ − Xᶜ. The smaller one is "eliminated" and the larger is reduced by that amount.

- Example: 24 − 8 = **16 Ω inductive**.
- If Xᶜ is bigger, the net is capacitive. With 30 Ω Xₗ and 54 Ω Xᶜ, the net is 24 Ω capacitive.

**Which way does the circuit lean?**

- More inductive (Xₗ > Xᶜ, VARsₗ > VARsᶜ): current **lags**, giving a **lagging PF**.
- More capacitive (Xᶜ > Xₗ): current **leads**, giving a **leading PF**.
- Equal: **resonance** (section 23–2). The circuit is purely resistive and the PF is 100%.

**Exceptions and pitfalls**

- **Never add Xₗ + Xᶜ.** They're 180° apart, so they subtract.
- **Never put Xₗ or Xᶜ directly into the Pythagorean theorem with R.** Subtract them first, then use the net X.
- The net reactance can be **smaller than either reactance**, so Z can be surprisingly small and the current surprisingly large.

## Impedance, Current and Voltage Drops

**Impedance**

```math
Z = \sqrt{R^2 + (X_L - X_C)^2}
```

- Example: √(12² + (24 − 8)²) = √(144 + 256) = **20 Ω**.
- If Xᶜ > Xₗ, the difference is negative, but squaring makes it positive: √(10² + (30 − 54)²) = 26 Ω.
- Rearranged for R: R = √(Z² − (Xₗ − Xᶜ)²). Example 23–3: Z = 208/8 = 26 Ω and the net X = 62 − 38 = 24 Ω, so R = **10 Ω**.

**Current:** I = E / Z = 240 / 20 = **12 A**, the same through R, L and C.

**Voltage drops (each in its own group)**

- Eᵣ = I × R = **144 V**
- Eₗ = I × Xₗ = **288 V** (more than the 240 V supply!)
- Eᶜ = I × Xᶜ = **96 V**
- Component values: L = Xₗ/377 = 0.0637 H; C = 1/(377 × Xᶜ) = 331.6 µF.

**Total voltage:** Eₜ = √(Eᵣ² + (Eₗ − Eᶜ)²) = √(144² + 192²) = 240 V ✓.

**The big surprise:** a single component's voltage can **exceed the supply**. Eₗ and Eᶜ partly cancel each other, so the supply only has to provide their difference. Each component still sees its full drop. On the job, a 240 V circuit can put 288 V (or, near resonance, far more) across a coil or capacitor. Always check Eᶜ against the capacitor's rating.

**When you're given L and C instead of reactances (Example 23–2):** convert first. 66.3 µF gives Xᶜ = 40.0 Ω, and 0.0663 H gives Xₗ = 25.0 Ω. Then Z = √(8² + (25 − 40)²) = 17.0 Ω and I = 120 / 17 = **7.05 A**.

## Power: Watts, Net VARs and VA

| Quantity | Formula | Example |
| --- | --- | --- |
| True power P | Eᵣ × I | 1728 W |
| Inductive VARs | Eₗ × I | 3456 VARsₗ |
| Capacitive VARs | Eᶜ × I | 1152 VARsᶜ |
| Net VARs | VARsₗ − VARsᶜ | 2304 (inductive) |
| Apparent power | Eₜ × I | 2880 VA |

```math
VA = \sqrt{P^2 + (VARs_L - VARs_C)^2}
```

**Intuition:** while the coil is storing energy, the capacitor is releasing it, and vice versa. They trade energy back and forth with each other locally, and the source only supplies the **net** reactive power. That's exactly how power-factor-correction capacitors help a motor load.

**Pitfalls**

- VA ≠ √(P² + VARsₗ² + VARsᶜ²). Subtract the VARs first.
- Watts never cancel. Only the reactive parts do.
- **Book typo:** Figure 23–6 lists VARsᶜ as **1142**. The correct value is **1152** (96 V × 12 A).

## Power Factor and Angle Theta: Leading or Lagging

- PF = P / VA = 1728 / 2880 = **0.60 (60%)**. It's series, so R/Z and Eᵣ/Eₜ also work.
- θ = cos⁻¹(0.6) = **53.13°**.
- **Direction:** VARsₗ > VARsᶜ here, so the circuit is net inductive. The current **lags**, giving a 60% **lagging** PF.
- Other trig: tan θ = (Xₗ − Xᶜ) / R = (VARsₗ − VARsᶜ) / P.

**Deciding leading vs lagging (Practice 7):** compare the two reactive quantities. Bigger inductive means lagging. Bigger capacitive means leading. The PF number alone doesn't tell you.

**Book typo:** the PF line reads "PF = 0.06 × 100." It's **0.6** × 100 = 60%.

## 23–2 Series Resonance, Bandwidth and Q

**Intuition:** Xₗ rises with frequency and Xᶜ falls. Somewhere they must cross. At that one frequency they're **equal**, they cancel completely, and the only thing left limiting the current is the resistance (often just the coil's wire). The current shoots up. Since each reactance is still there individually, the voltage across L and across C each shoots up too.

**Resonant frequency**

```math
f_R = \frac{1}{2\pi\sqrt{LC}}
```

- L in henrys, C in farads, fᵣ in hertz.
- **To find the L or C needed to resonate** (series or parallel): L = 1 / (4π²f²C) and C = 1 / (4π²f²L). The π and the f are both **squared**.
- Examples: 0.2 H at 1200 Hz needs C = **88 nF**. 50 µF at 400 Hz needs L = **3.17 mH**.

**What happens at series resonance** (book circuit: 0.0159 H with 5 Ω wire resistance, 1.59 µF, 50 V)

| Frequency | Xₗ | Xᶜ | Z | Current |
| --- | --- | --- | --- | --- |
| 600 Hz | 59.9 Ω | 166.8 Ω | 107.0 Ω | 0.47 A |
| **1000 Hz (resonance)** | 100 Ω | 100 Ω | **5 Ω** | **10 A** |
| 1400 Hz | 139.9 Ω | 71.5 Ω | 68.5 Ω | 0.73 A |

- **Series resonance:** Z is at its **minimum** (= R), current is at its **maximum**, PF = 100%, θ = 0°.
- **Voltage magnification:** Eₗ = Eᶜ = 10 A × 100 Ω = **1000 V** each, on a **50 V** supply. The magnification factor equals the circuit's Q: Xₗ/R = 100/5 = 20, and 20 × 50 V = 1000 V.

**Bandwidth (B):** the range of frequencies over which the current stays at or above **0.707 × maximum**.

- B = f₂ − f₁ (the upper and lower 0.707 points).
- B = fᵣ / Q. **High Q** (low resistance) gives a **narrow**, sharp peak. **Low Q** gives a **wide**, flat one.
- Book examples: 995–1005 Hz is a 10 Hz bandwidth (narrow, high Q). 1150–1250 Hz is a 100 Hz bandwidth (wide, low Q).
- For the 1000 Hz circuit above: Q = 20, so B = 1000/20 = 50 Hz.

**Exceptions and pitfalls**

- At resonance the circuit **looks** purely resistive, but L and C are still there, carrying full current and seeing high voltage.
- Forgetting to square π and f in the L/C formulas. That's the most common resonance error.
- Resonance depends on **frequency**. A circuit that's harmless at 60 Hz can resonate at a harmonic (300 Hz, 420 Hz…).

## Book Errors and Wording Slips

| Where | Book says | Should be |
| --- | --- | --- |
| PF calculation, Example 23–1 | PF = 0.06 × 100 | PF = **0.6** × 100 = 60% |
| Figure 23–6 | VARsᶜ = 1142 | **1152** (96 V × 12 A) |
| Bandwidth text | "1 A × 0.707 B" | 1 A × 0.707 = 0.707 A (stray "B") |
| L/C resonance formulas (as printed) | Easy to misread as 4πf² | **4π²f²**: both π and f are squared. The book's worked numbers do square both. |
| 23–1 | "Ratio of resistance, inductance, and capacitance" sets the angle | Strictly, R vs the **net reactance** (Xₗ − Xᶜ) sets it: tan θ = (Xₗ − Xᶜ) / R |

All the main worked answers (Z = 20 Ω, I = 12 A, 53.13°, 7.05 A, R = 10 Ω, the resonance table, 88 nF, 3.17 mH) check out.

## Easily overlooked things for electricians

1. **Component voltage can exceed line voltage.** In any series circuit with both L and C, measure across the capacitor or coil before assuming it's within the line rating. Near resonance it can be many times the supply.
2. **Harmonic resonance with PF capacitors.** A PF capacitor bank plus the system (transformer) inductance forms an L-C circuit. If its resonant frequency lands near a harmonic from VFDs or other electronic loads (the 5th harmonic at 300 Hz, the 7th at 420 Hz), currents and voltages can be magnified. You'll see blown capacitor fuses, failed capacitors and overheated transformers. That's why **detuned** (reactor-equipped) PF banks are used in plants with drives.
3. **Resonant HV test sets.** Large cable and generator AC hipot tests often use **series-resonant test systems**: a variable inductor tuned to resonate with the cable's capacitance. A modest supply then produces a very high test voltage. It's this chapter's 50 V → 1000 V example scaled up, and it's what the Practical Application describes.
4. **Ferroresonance.** An iron-core transformer (nonlinear L) plus cable or grading capacitance can resonate when a single phase is opened, for example by a blown fuse or single-pole switching on a lightly loaded transformer. It can produce erratic overvoltages. Know that it exists and why switching procedures matter.
5. **Capacitors still store energy at resonance.** Voltages in resonant circuits can be very high. Discharge and verify zero before touching (Unit 19).
6. **Net VARs are what the utility sees.** This series cancellation is the same physics that lets PF capacitors offset motor VARs (in parallel, next unit).

## Notes on the homework

- **General method:** Convert any L or C to Xₗ or Xᶜ. Net X = Xₗ − Xᶜ. Z = √(R² + X²), I = E/Z. Then each component with Ohm's law using the shared current.
- **Q1–Q3:** Eᵣ is in phase with I, Eₗ leads I by 90°, Eᶜ lags I by 90°.
- **Q4–Q10 (400 Hz):** **Don't use 377.** Xₗ = 2π × 400 × 0.0119 and Xᶜ = 1 / (2π × 400 × 16.6 µF). Then Z, I, the three drops (Eₗ or Eᶜ may exceed 440 V; that's expected), P = I²R, VA = E × I, PF and θ. Say leading or lagging.
- **Practical Application (400 Hz resonant HV source):**
  - C = 1 / (4π² × 400² × 0.015).
  - At resonance, Z = the 2 Ω wire resistance, so I = 240/2.
  - Eᶜ = I × Xᶜ (= I × Xₗ). The capacitor's minimum voltage rating is **that** value, not 240 V. If you choose a DC-rated capacitor, multiply by 1.414.
- **Practice 2 (powers given):** Net VARs = 28.8 − 12.96 (capacitive). VA = √(P² + net²). I = VA / E. Then each part with power / I.
- **Practice 4 (drops given):** Eₜ = √(185² + (740 − 444)²). I = VA / Eₜ.
- **Practice 5:** kΩ values. Net X = 1.1 kΩ. Z = √(4² + 1.1²) kΩ. Eₗ = I × 3.5 kΩ.
- **Practice 6 and 7:** Net VARs = 34 − 24 = 10 (capacitive). PF = 18 / √(18² + 10²). Capacitive VARs are larger, so the PF is **leading**.
- **Practice 8:** I = Eᵣ / R, then Eᶜ = I × 16.
- **Practice 9:** Z = 240² / 600 (or E / I with I = VA / E), then R = Z × PF (series: PF = R/Z).
- **Practice 10:** Convert 0.796 H and 5.89 µF to reactances at 60 Hz, then Z. Xᶜ comes out larger than Xₗ, so the circuit is net capacitive.

## One-glance cheat sheet

**Book example, all values (240 V, 60 Hz, R 12 Ω, Xₗ 24 Ω, Xᶜ 8 Ω)**

| Total | Resistive | Inductive | Capacitive |
| --- | --- | --- | --- |
| Eₜ = 240 V | Eᵣ = 144 V | Eₗ = 288 V | Eᶜ = 96 V |
| I = 12 A | 12 A | 12 A | 12 A |
| Z = 20 Ω | R = 12 Ω | Xₗ = 24 Ω | Xᶜ = 8 Ω |
| VA = 2880 | P = 1728 W | VARsₗ = 3456 | VARsᶜ = 1152 |
| PF 60% lagging, θ 53.13° | — | L = 0.0637 H | C = 331.6 µF |

**Rules**

- **Phase vs the shared current:** Eᵣ in phase, Eₗ leads 90°, Eᶜ lags 90°. So Eₗ and Eᶜ are 180° apart and **subtract**.
- **Z** = √(R² + (Xₗ − Xᶜ)²). **R** = √(Z² − (Xₗ − Xᶜ)²).
- **Eₜ** = √(Eᵣ² + (Eₗ − Eᶜ)²). **VA** = √(P² + (VARsₗ − VARsᶜ)²).
- **Net inductive** means lagging PF. **Net capacitive** means leading PF.
- **Eₗ or Eᶜ can exceed Eₜ.** Check the component ratings.
- **Resonance:** Xₗ = Xᶜ, fᵣ = 1/(2π√(LC)). Series resonance: Z = R (minimum), I maximum, PF 100%, voltage magnified by Q.
- **Finding L or C to resonate:** L = 1/(4π²f²C), C = 1/(4π²f²L).
- **Bandwidth:** B = f₂ − f₁ at 0.707 × I(max). B = fᵣ / Q. High Q means narrow.
