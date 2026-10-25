# Unit 15 Study Guide: Alternating Current

Oct 22, 2026 · @Jeff

## Why this chapter matters

About 99% of what you'll work on is AC. This chapter answers three practical questions:

1. What does the voltage actually look like over time?
2. Which number on the meter is the "real" one?
3. Why does "120 volts" actually reach about 170 volts twice every cycle?

That last question decides whether a capacitor, diode, ballast or surge device survives on a circuit. Units 16 and later build inductive and capacitive circuits on top of this. This chapter covers the simple case first: pure resistance, where AC acts almost exactly like DC.

## 15–1 Advantages of AC

**Core idea:** AC can go through a **transformer** and DC can't (at least not without electronics). Transformers let the utility do two things:

- **Step voltage up** for transmission, at 69 kV, 138 kV, 345 kV and higher.
- **Step it back down** for use: 480, 277, 240, 120 V.

**Why high voltage?** For the same power, P = E × I. Raise E and you lower I.

- Line loss is I²R, so cutting current to 1/10 cuts the loss to **1/100**.
- Lower current also means smaller conductors and less copper.

**Exceptions and corrections**

- **"DC cannot be transformed"** was true in the 1890s. Today, power electronics convert DC to DC: phone chargers, solar optimizers, and **HVDC** transmission lines that carry DC over very long distances. For the exam, the book's answer is the one to give. Just know it's no longer absolute.
- **History error:** The big AC-vs-DC lighting contract is usually credited to the **1893 World's Columbian Exposition in Chicago**, which Westinghouse won. The book says 1904 St. Louis. Use the book's answer on the book's test, but don't be surprised if you read otherwise.

## 15–2 AC Waveforms

**Intuition:** DC is a steady push in one direction. AC pushes one way, then the other, over and over. The **waveform** is a graph of voltage (vertical axis) against time (horizontal axis). Its shape depends on what produced it.

### Square wave

- The voltage snaps between +V and −V, holding flat at each level.
- It's produced by electronic switching, using circuits called **oscillators** (the book shows one built from transistors and a transformer).
- **In the trade:** Cheap inverters and some UPS units put out a "modified sine wave," which is a stepped square wave. Some motors, clocks and electronics run hot or noisy on it.

### Triangle wave

- A **linear wave**: the voltage rises and falls at a constant rate, so the graph is made of straight lines.
- For example, if it reaches 100 V at 2 ms, it's at 50 V at 1 ms. It's simple proportion.

### Sine wave

This is the standard waveform, produced by any **rotating machine** (generator or alternator).

| Term | Meaning |
| --- | --- |
| **Cycle** | One complete wave: 0 → +peak → 0 → −peak → 0 |
| **Electrical degrees** | One cycle = 360°. +Peak at 90°, zero at 180°, −peak at 270°, back to zero at 360° |
| **Frequency (f)** | Cycles per second, measured in **hertz (Hz)**. 60 Hz in the US and Canada |
| **Period (T)** | Time for one cycle, in seconds |

**Formulas:** T = 1/f and f = 1/T.

- At 60 Hz, T = 1/60 = 16.67 ms, so a peak comes every 8.33 ms.
- **Pitfall: unit prefixes.** 0.04 ms = 0.00004 s, not 0.04 s. Convert to seconds and Hz *before* dividing. Example 15–2 is built to catch this.
  - ms = 10⁻³ s
  - µs = 10⁻⁶ s
  - kHz = 10³ Hz
  - MHz = 10⁶ Hz

**Overlooked points**

- **Electrical degrees ≠ mechanical degrees.** On a 2-pole generator, one turn is one cycle. On a 4-pole machine, one mechanical turn is **720 electrical degrees** (two cycles). You'll need this for motor speed later.
- **50 Hz** is standard in most of the world. A 60 Hz motor on 50 Hz runs at about 5/6 speed and may overheat. Aircraft use 400 Hz. Always check the nameplate frequency.

## The instantaneous value (the trig from Unit 14 pays off)

**Intuition:** As the generator loop turns, it cuts magnetic flux lines slowly near 0° (moving almost parallel to them) and fastest at 90° (moving straight across them). The rate of cutting follows the sine of the angle, so the voltage does too. That's where the name "sine wave" comes from.

**Formula**

```math
e_{inst} = E_{max} \times \sin\theta
```

- **E(INST)** (often written lowercase *e*): the voltage at one instant.
- **E(MAX)**: the peak voltage, also called **amplitude**.
- **θ**: the electrical angle at that instant.

**Rearranged:** E(max) = e / sin θ, and sin θ = e / E(max), which gives θ = sin⁻¹(e / E(max)).

**Supporting idea:** Angle and time are tied together by θ = 360° × f × t. That turns "how many degrees in" into "how many milliseconds in."

**Exceptions and pitfalls**

- **Every voltage happens twice per half cycle.** sin⁻¹ only returns angles from 0° to 90°. Example 15–5 found 53 V at 8.7°, but the wave also passes 53 V on the way down at **180° − 8.7° = 171.3°**. Unless a question says "on the rising side," that second angle is also a valid answer.
- **Angles from 180° to 360° give negative voltages,** because sine is negative there. sin 225° = −0.707. A negative answer isn't an error.
- **Angles over 360°** (one practice problem uses 400°) just wrap around: 400° is the same as 40°.
- **Rounding:** The book rounds sin to 3 digits, which is why its answers are slightly off. 53/350 gives 8.71°, not the book's 8.685°. Keep full precision in the calculator.
- **DEG mode,** same as Unit 14.

## 15–3 Sine Wave Values

Four different numbers describe the same wave. Most mistakes in this unit come from using the wrong one.

| Value | What it measures | Conversion from peak | Where you see it |
| --- | --- | --- | --- |
| **Peak-to-peak (p-p)** | +peak to −peak | 2 × peak | Read off an oscilloscope screen |
| **Peak (max, amplitude)** | 0 to either peak | — | Ratings for insulation, capacitors, diodes, MOVs |
| **RMS (effective)** | Heating-equivalent DC value | peak × 0.707 | What your meter reads; what "120 V" means |
| **Average (rectified)** | DC value after rectifying | peak × 0.637 (full-wave) | DC voltmeter on rectified output |

### RMS: the key idea

**Intuition:** A sine wave peaking at 100 V spends most of its time below 100 V. Across a resistor, it makes only half the heat that 100 V DC would (Figure 15–10: 50 W vs 100 W). RMS is **the DC voltage that would make the same heat.** That's why it's also called the **effective** value.

**Name decoded:** **R**oot of the **M**ean of the **S**quares. You square every instantaneous value, average those squares, then take the square root.

**Formulas**

- RMS = peak × 0.707 (that's 1/√2)
- Peak = RMS × 1.414 (that's √2)

**Numbers worth memorizing**

| Nameplate (RMS) | Peak | Peak-to-peak |
| --- | --- | --- |
| 120 V | 170 V | 339 V |
| 208 V | 294 V | 588 V |
| 240 V | 339 V | 679 V |
| 277 V | 392 V | 783 V |
| 480 V | 679 V | 1,358 V |

**Rules**

- All AC values in this book (and on nameplates and in the NEC) are **RMS unless stated otherwise.**
- Never mix peak and RMS in the same Ohm's law calculation.

**Exceptions and pitfalls**

- **0.707 and 1.414 only apply to pure sine waves.** For a square wave, RMS = peak. For a triangle wave, RMS = peak × 0.577.
- **Average-responding vs True RMS meters.** Cheaper meters measure the average and multiply by a sine-wave correction factor. On distorted waveforms (VFDs, LED drivers, computers, electronic ballasts), they can read **20–40% off**, usually low. That's why the trade insists on **True RMS** meters, especially for current on nonlinear loads.
- **Book typo:** "100 V RMS applied to a 100-V resistor" should say 100-**Ω** resistor.
- The book says oscilloscopes "display peak-to-peak." More accurately, a scope shows the wave itself, and p-p is the easiest thing to read off it. Modern scopes also calculate RMS.
- **Safety:** "It's only 120" understates it. The insulation sees 170 V twice every cycle.

### Average values

**Intuition:** Averaged over a full cycle, a sine wave is **zero**, because the positive and negative halves cancel. So "average value" only means something once the wave has been **rectified**, meaning the negative half is flipped or removed so current only flows one way.

**Definitions**

- **Rectifier:** diodes that let current through in one direction only.
- **Full-wave (bridge) rectifier:** 4 diodes; both halves are flipped positive.
- **Half-wave rectifier:** 1 diode; the negative half is just blocked.
- **Pulsating DC:** DC that rises and falls but never reverses direction.
- **Ripple:** the leftover bumps in pulsating DC.

**Formulas**

| Rectifier | From peak | From RMS |
| --- | --- | --- |
| Full-wave | avg = peak × 0.637 | avg = RMS × 0.9 |
| Half-wave | avg = peak × 0.318 | avg = RMS × 0.45 |

0.9 is just 0.637 × 1.414, so both routes give the same answer (Example 15–8).

**The biggest overlooked point: filter capacitors change everything.** The book's 0.9 factor assumes a bare rectifier feeding a resistor. Most real power supplies put a **capacitor** after the rectifier. The capacitor charges up to the **peak** and holds it there, so the DC output sits close to **1.414 × RMS**, not 0.9 × RMS.

- **In the field:** the DC bus in a VFD on 480 V reads about **650–680 VDC**, not 432. Students who expect 432 V get surprised. Treat a VFD DC bus as lethal until you've verified it has discharged.

## Wavelength

**Intuition:** At high frequency, the field around a conductor radiates outward at the speed of light. **Wavelength** is how far that wave travels during one cycle.

**Formula:** λ (lambda) = speed of light / f = 300,000,000 m/s ÷ f (in Hz). The answer is in meters.

**Example:** At 100 MHz (FM radio), λ = 3 m.

**Context:**

- At **60 Hz**, λ is about **5,000 km (≈3,100 miles)**. That's why power wiring doesn't act like a radio antenna.
- Radio, data and communications work cares about wavelength. Building power wiring mostly doesn't.

**Pitfall:** Use meters with 300,000,000. If you use 186,000 miles/s, your answer is in miles.

## 15–4 Resistive Loads

**Core idea:** In a **pure resistance**, current exactly follows voltage. They cross zero together and peak together. This is called being **in phase** (0° phase angle).

**Examples:** heaters, water-heater and range elements, incandescent lamps.

**Two characteristics the book lists**

1. They produce heat.
2. Voltage and current are in phase.

**Minimum to solve problems:** For pure resistance, **every DC Ohm's law and power formula works unchanged**, as long as you use RMS values throughout.

**Exceptions and preview**

- AC loads come in three types: resistive, **inductive** (motors, transformers, ballasts) and **capacitive**. Only resistive loads are in phase. Real loads are mixtures.
- Incandescent lamps aren't constant resistance. Cold filament resistance is roughly 1/10 of the hot value, so they draw a large inrush current at switch-on.
- The book's line that DC motors "appear resistive" is a simplification. Ignore it for now.

## 15–5 Power in an AC Circuit

**Core idea:** Instantaneous power = e × i at each moment.

- In a resistive circuit, e and i are always the same sign: both + or both −.
- Since + × + = + and − × − = +, **power is always positive.** All the energy flows into the load and becomes heat.
- Watts = E(RMS) × I(RMS), exactly like DC.

**Supporting ideas the book skips**

- The power wave pulses at **twice line frequency** (120 Hz on a 60 Hz system), because it peaks on both the + and − halves. That's why incandescent and some LED lights flicker at 120 Hz.
- **Average power is half of peak power.** That's where the 50 W in Figure 15–10 came from: 100 V peak × 1 A peak = 100 W peak, which averages to 50 W.
- **Preview of later units:** When current and voltage are *out of phase*, there are moments when they have opposite signs. During those moments power is negative, meaning it flows back to the source. That's the root of reactive power, power factor, and why VA ≠ W.

## 15–6 Skin Effect

**Intuition:** With AC, the current crowds toward the **outer surface** of a conductor. The center carries less of the load, so the conductor acts like a thinner wire with higher resistance. The effect grows with frequency.

**The book's explanation, plus a correction:** The book blames eddy currents. More precisely, the conductor's own changing magnetic field pushes back hardest at its center. That's self-inductance, but the result is the same.

**Book's rules**

- Skin effect increases with frequency.
- At 60 Hz it's small enough to ignore for routine wire sizing.
- At high frequency, use conductors with a lot of **surface area**, like flat braid or wide copper strap, for things such as RF grounding.

**Overlooked points for electricians**

- **It still matters at 60 Hz for large conductors.** The current-carrying "skin" in copper at 60 Hz is about 8.5 mm (⅓ in) deep. Large cables (roughly 500 kcmil and up) and bus bars have measurably higher AC resistance. That's why **NEC Chapter 9, Table 9** lists AC resistance separately from DC (Table 8). It's also one reason big feeders run several smaller conductors in parallel instead of one giant one.
- **Harmonics make it worse.** Nonlinear loads (VFDs, computers, LED drivers) produce currents at 180 Hz, 300 Hz and higher. Those raise conductor and transformer heating, which is why you see K-rated transformers and oversized neutrals.
- **Don't confuse this with induction heating of steel.** Running a single AC conductor alone through steel conduit or a steel box knockout heats the steel by induction. That's why the NEC requires **all phase conductors, plus the neutral and EGC, to be run together in the same raceway** (300.3(B) and 300.20). It's a related magnetic effect, but not the same thing as skin effect.

## Homework notes

- **Q9 (88 V p-p, find average):** Halve it to get peak *first*. Using p-p directly is the classic mistake.
- **Q10 ("DC average 68 V, find RMS"):** The question assumes full-wave rectified sine. Work backward: RMS = average ÷ 0.9.
- **Practice table (inst./peak/degrees):** One angle is over 360°, so wrap it. Some combinations have two valid angles (see the instantaneous-value section).
- **Practical App 1 (crane magnet bridge):**
  - Diodes are rated by **peak** voltage, so convert 240 V RMS to peak before comparing it to the 400 V rating.
  - In a bridge, each blocking diode sees about the full peak.
  - Then use the full-wave average formula for the DC output.
  - On a real job, also allow for line voltage running 5–10% high and for spikes. Designers usually want around 2× margin on diode ratings, so "technically enough" and "good practice" may give different answers. Say which one you're answering.
- **Practical App 2 (277 V ballast, 350 V peak rating):** The trap is comparing 277 directly to 350. The ratings are in different units (RMS vs peak). Convert 277 to peak first.

## One-glance cheat sheet

- **Period and frequency:** T = 1/f and f = 1/T. Work in seconds and Hz. 60 Hz → 16.67 ms per cycle.
- **Instantaneous value:** e = E(max) × sin θ. Each value occurs at θ and 180° − θ; angles from 180–360° give negative values.
- **Conversions (sine waves only):**
  - p-p = 2 × peak
  - RMS = peak × 0.707
  - peak = RMS × 1.414
- **Average:**
  - Full-wave: peak × 0.637 = RMS × 0.9
  - Half-wave: half of that
  - With a filter capacitor, the output is close to peak
- **Ratings:** Nameplates, meters and the NEC use RMS. Component voltage ratings (diodes, capacitors, MOVs, ballast maximums) are usually peak.
- **Resistive loads:** E and I are in phase, so W = E × I and all of Ohm's law works with RMS values.
- **Wavelength:** λ = 3×10⁸ / f, in meters.
- **Skin effect:** rises with frequency. Ignore it for small 60 Hz wire; it matters for big conductors, harmonics and RF.
- **Meters:** Use a True RMS meter on anything with electronics.
