# Labs 4–6 — Power Systems: Split-Phase, Wye and Delta: Study Guide

These three labs move from single circuits to the systems that feed buildings: the 120/240 V single-phase three-wire system (Lab 4), the three-phase wye system (Lab 5), and the three-phase delta system (Lab 6). The math is the same Ohm's law and phasor addition from Units 14–24, plus one new number: $\sqrt{3} \approx 1.732$.

---

## 1. The 120/240 V single-phase three-wire system (Lab 4)

**Main idea.** A utility transformer's secondary has a center tap. The center tap is grounded and becomes the neutral. Each end of the winding is a "hot" line. Each line is 120 V to neutral, and the two lines are 240 V to each other because they are 180° apart.

- 120 V loads connect line to neutral; 240 V loads (ranges, dryers, water heaters, A/C) connect line to line.
- **Neutral current = the difference of the two line currents**, not the sum:

$$
I_N = |I_{L1} - I_{L2}|
$$

  Balanced loads give 0 A on the neutral. With 15 A on L1 and 9 A on L2, the neutral carries 6 A.
- A **multiwire branch circuit** (NEC Article 100) shares one neutral between two hots. The NEC requires a way to open both hots at once, such as a 2-pole breaker or handle tie (NEC 210.4(B)), and the neutral must not depend on a device for its continuity (NEC 300.13(B)).

### The open-neutral problem

If the neutral opens, two 120 V loads on opposite lines end up **in series across 240 V**. The voltage divides by resistance, so the smaller load (higher resistance) gets most of it.

**Worked example.** A 1000 W lamp and a 100 W lamp, both rated 120 V, on opposite lines.

| Step | Work | Result |
|---|---|---|
| Resistance of 1000 W lamp | $R = V^2/P = 120^2/1000$ | 14.4 Ω |
| Resistance of 100 W lamp | $120^2/100$ | 144 Ω |
| Series current across 240 V | $240 / (14.4 + 144)$ | 1.52 A |
| Voltage on 1000 W lamp | $1.52 \times 14.4$ | 21.8 V (dim) |
| Voltage on 100 W lamp | $1.52 \times 144$ | 218 V (burns out) |

(Real lamp resistance changes with temperature, so a real test differs a little, but the direction is the same.)

---

## 2. Three-phase basics

- A three-phase source makes three voltages of the same size, **120° apart**. The order they peak in is the **phase sequence** or rotation (A-B-C). Swapping any two lines reverses a three-phase motor.
- Why use it: power delivery is smooth (constant, not pulsing), it moves more power per pound of copper, and three-phase motors start and run without extra parts.
- Two ways to connect the three windings or loads: **wye** (star) and **delta**.

**Line vs. phase.** *Line* values are measured between the lines (or in the line wires). *Phase* values are measured across one winding or one load.

---

## 3. Wye (Lab 5)

One end of each winding ties to a common point, which is usually grounded as the neutral.

$$
V_{L} = \sqrt{3}\, V_{P} \qquad I_{L} = I_{P}
$$

| System | Line-to-neutral (phase) | Line-to-line |
|---|---|---|
| 208Y/120 V | 120 V | 120 × 1.732 = 208 V |
| 480Y/277 V | 277 V | 277 × 1.732 = 480 V |

- **Why 208 and not 240:** the two 120 V phase voltages are 120° apart, not 180°, so they add to 1.732 × 120.
- **Balanced load:** the three phase currents cancel and the neutral carries 0 A.
- **Unbalanced resistive load:** the neutral carries the *phasor* sum, which is always less than the arithmetic sum:

$$
I_N = \sqrt{I_A^2 + I_B^2 + I_C^2 - I_A I_B - I_B I_C - I_C I_A}
$$

  Example: 10 A, 8 A and 6 A give $I_N = \sqrt{100 + 64 + 36 - 80 - 48 - 60} = \sqrt{12} \approx 3.5$ A.
- Non-linear loads (computers, LED drivers) make triplen harmonics that **add** in the neutral instead of cancelling, so a wye neutral can carry more current than the phases.

---

## 4. Delta (Lab 6)

The three windings connect end to end in a loop. There is no neutral in a plain 3-wire delta.

$$
V_{L} = V_{P} \qquad I_{L} = \sqrt{3}\, I_{P}
$$

- In a 240 V delta, each load sees 240 V. If each phase load draws 10 A, each line carries 10 × 1.732 = 17.3 A.
- In the lab, **phase amps** are measured inside the delta (in a load leg) and **line amps** in the feeder wires. Line amps are larger.
- **High-leg (wild-leg) delta:** a 240 V delta with one winding center-tapped to make a 120/240 V four-wire system. Two lines read 120 V to neutral, but the high leg reads about **208 V to neutral**. The NEC requires the high leg to be marked orange (NEC 110.15) and to be the B phase in panelboards (NEC 408.3(E)).
- **Open delta:** two transformers can supply three-phase power, but only at **57.7%** of what three would carry.

---

## 5. Three-phase power

$$
P = \sqrt{3}\, V_L\, I_L\, \text{PF} \qquad S = \sqrt{3}\, V_L\, I_L
$$

The same result comes from adding the three phases: $P = 3\, V_P\, I_P\, \text{PF}$.

**Worked example.** A balanced 240 V delta heater bank draws 17.3 A per line at PF = 1.

| Step | Work | Result |
|---|---|---|
| Line formula | 1.732 × 240 × 17.3 × 1 | 7,190 W |
| Check with phase values | phase current = 17.3 ÷ 1.732 = 10 A; 3 × 240 × 10 | 7,200 W |

(The small difference is rounding.)

---

## 6. Dangerous conditions

- **Open neutral** on a split-phase or wye system puts unequal, sometimes near-line voltage on 120 V equipment. It destroys electronics and can start fires.
- **High-leg delta:** connecting a 120 V load to the high leg puts about 208 V on it. Always check the orange-marked leg before landing 120 V loads.
- **Never assume a voltage to ground.** On a corner-grounded or ungrounded delta, line-to-ground readings can be surprising. Measure every combination.
- **Shared neutrals:** turning off one breaker of a multiwire branch circuit does not de-energize the shared neutral. Open both hots.

## 7. Common misunderstandings

- Neutral current on split-phase is the **difference** of the line currents; on an unbalanced wye it is the **phasor** sum. Neither is the plain arithmetic sum.
- 208 V is not "about 240 V". 240 V equipment on 208 V runs about 13% low (heaters give about 75% of their rated heat, since power varies with the square of voltage).
- In a delta, line current is larger than phase current; in a wye, line voltage is larger than phase voltage. Don't mix them up.

## 8. Easily overlooked

- $\sqrt{3}$ appears only when you convert between line and phase values, or use line values in the power formula.
- The clamp-on ammeter reads line current on a feeder wire, and phase current only if you clamp inside the delta.
- Lamp loads in the lab are close to resistive, so PF ≈ 1. Motor loads are not.
