# Unit 19 Study Guide: Capacitors

Oct 22, 2026 · @Jeff

## Why this chapter matters

Capacitors are the third basic AC load, after resistors and inductors. On the job you'll meet them as motor start and run capacitors, power-factor correction banks, VFD and power-supply filter capacitors, and in timing circuits. They also store energy and can hurt you **after the power is off**.

This unit covers what a capacitor is, how it charges and discharges, how to combine capacitors, how to read their markings, and how to test them. The next unit (capacitive reactance) builds on it.

**Inductor vs capacitor, the mirror image:**

|  | Inductor (Unit 16) | Capacitor (Unit 19) |
| --- | --- | --- |
| Opposes a change in... | Current | **Voltage** |
| Stores energy in a... | Magnetic field | **Electrostatic field** (in the dielectric) |
| Unit | henry (H) | **farad (F)** |
| Series combination | Add (L₁ + L₂) | **Reciprocal** formula |
| Parallel combination | Reciprocal formula | **Add** (C₁ + C₂) |
| Dangerous when... | Circuit is opened (inductive kick) | **Stays charged after power is removed** |

## 19–1 and 19–2 What a Capacitor Is and How It Stores Energy

**Intuition:** A capacitor is two metal plates with an insulator between them. Connect a battery and electrons pile up on one plate and are pulled off the other. Current flows only until the capacitor's voltage matches the battery. Then it stops. Disconnect the battery and the charge stays put, like a tiny rechargeable battery that can dump all its energy at once.

**Definitions**

- **Capacitor:** a device that **opposes a change of voltage**.
- **Plates:** the two conductive surfaces.
- **Dielectric:** the insulating material between the plates. (Review Q1.)
- **Electrostatic field:** the field of stationary charges between the plates. This is where the energy is stored. (Review Q4.)
- **Dielectric stress:** the dielectric's electron orbits are stretched toward the positive plate. It's like a drawn bowstring: stored energy waiting to be released.
- **Leakage current:** the small current that creeps through the imperfect dielectric, slowly discharging the capacitor. A capacitor with a weakened dielectric that leaks too much is called **leaky**.

**Key rule:** current flows **only while a capacitor is charging or discharging**. A fully charged capacitor on steady DC passes no current (except leakage). (Preview: on AC, the voltage keeps changing, so the capacitor is always charging or discharging and current flows all the time.)

**Voltage and dielectric stress**

- Stress is proportional to the voltage across the plates. Too much voltage breaks the dielectric down and shorts the capacitor.
- That's why every capacitor has a **voltage rating**.
- **Life-span rule (military study):** a capacitor run at **half** its rated voltage lasts about **8 times** longer than one run at full rating.

**Why capacitors can deliver huge current:** Energy collected slowly (seconds) can be released in microseconds when the leads are shorted. That can mean thousands of amps for an instant. A camera flash charges a capacitor to about 500 V from two 1.5 V batteries, then dumps it through a xenon tube.

**Book error:** It says leakage current is "proportional to the resistance of the dielectric." It's the reverse: a **higher** dielectric resistance means **less** leakage. Leakage = voltage ÷ dielectric resistance.

**Caution from the book (take it seriously):** Never charge a capacitor and hand it to someone as a joke. A charged capacitor can deliver enough energy to put a heart into fibrillation.

## 19–3 and 19–4 Capacitance, Dielectric Constant and Units

**Intuition:** Capacitance is how much charge a capacitor holds per volt. Bigger plates hold more. Plates closer together hold more (the opposite charges pull harder on each other). A better dielectric holds more.

**Three factors that set capacitance** (Review Q2)

1. **Surface area of the plates:** more area, more capacitance.
2. **Distance between the plates:** closer, more capacitance.
3. **Type of dielectric:** a higher dielectric constant gives more capacitance.

**Dielectric constant (K):** how many times more capacitance a material gives than a vacuum (K = 1). Air ≈ 1.006, paper ≈ 3.5, mica ≈ 6.4–7, pure water 81, ceramic up to about 1200.

- If a capacitor goes from 1 µF with vacuum to 5 µF with a material between the plates (same spacing), K = 5. Review Q3 works the same way.
- K has no units. The book labels it "F/in.", which is a typo.

**Charge, capacitance and voltage**

```math
Q = C \times V
```

- **Q:** charge in coulombs. **C:** capacitance in farads. **V:** volts.
- One farad stores one coulomb per volt.

**Plate formula (book's version, in picofarads):** C = (K × A) / (4.45 × D), with A in square inches and D in inches. It shows why 1 F is enormous: an air capacitor with plates 1 in. apart would need about **1,108 square miles** of plate (Example 19–1).

**Units you'll actually use**

| Unit | Symbol | Value in farads |
| --- | --- | --- |
| microfarad | µF (older: MFD, mfd) | 10⁻⁶ |
| nanofarad | nF | 10⁻⁹ |
| picofarad | pF (older: µµF, mmF) | 10⁻¹² |

**Pitfalls**

- Convert to farads before using Q = CV or τ = RC. 50 µF = 0.000050 F.
- "MFD" on old motor capacitors means **microfarads**, not megafarads.
- 1 µF = 1000 nF = 1,000,000 pF.

**Supporting formula not in the book:** the energy stored is W = ½ × C × V² (joules). Doubling the voltage quadruples the energy. That's why high-voltage capacitors are far more dangerous than their µF rating suggests.

## 19–7 and 19–8 Charging, Discharging and RC Time Constants

**Intuition:** A capacitor fills like a tank through a narrow pipe. At first it fills fast. As it gets closer to full, there's less "push" left, so it slows down. It never quite finishes, but after five time constants it's close enough. Discharge is the same curve upside down.

**Exponential rule:** in each time constant, the voltage changes by **63.2% of the change still remaining**.

| Time constants | Charging (to 100 V) | Discharging (from 100 V) |
| --- | --- | --- |
| 1 | 63.2 V | 36.8 V |
| 2 | 86.5 V | 13.5 V |
| 3 | 95.0 V | 5.0 V |
| 4 | 98.2 V | 1.8 V |
| 5 | 99.3 V ("full") | 0.7 V ("empty") |

(The book's chart rounds slightly differently, e.g. 86.4 V and 13.6 V.)

**RC time constant**

```math
\tau = R \times C
```

- **τ (tau):** time for one time constant, in seconds. The book sometimes just writes t.
- **R** in ohms, **C** in farads.
- **Total charge (or discharge) time = 5τ.**
- Rearranged: R = τ / C and C = τ / R.

**Worked examples**

- 50 µF and 100 kΩ: τ = 0.000050 × 100,000 = **5 s**, so full charge takes **25 s** (Example 19–3).
- Total charge of 0.2 s with 100 pF: τ = 0.2 / 5 = 0.04 s, so R = 0.04 / (100 × 10⁻¹²) = **400 MΩ** (Example 19–4).
- 500 kΩ and 15 s total: τ = 3 s, so C = 3 / 500,000 = **6 µF** (Example 19–5).

**Pitfalls**

- **τ vs total time.** Problems that say "how long to charge" want 5τ. Problems that give a total time need dividing by 5 before you use R = τ/C.
- **Unit prefixes.** kΩ = 10³, MΩ = 10⁶, µF = 10⁻⁶, nF = 10⁻⁹, pF = 10⁻¹², ms = 10⁻³ s. Convert everything to ohms, farads and seconds first.
- **The charge and discharge times depend on R and C together.** A big capacitor with a small resistance can still charge or discharge quickly.

**Field point:** "5 time constants to discharge" is the theory behind bleed resistors. A capacitor with no discharge path (or a failed bleed resistor) can hold its charge for hours or days.

## 19–9 to 19–17 Uses, Types and Markings

**Applications (19–9):** power-factor correction; start and run capacitors for single-phase motors; phase shift for SCR and Triac controls; filtering pulsating DC; RC timing; frequency and pulse circuits in electronics.

### Nonpolarized ("AC") capacitors

- They work on **AC or DC**, either way around. (Review Q9: yes, they can go on DC.)
- **Oil-filled paper** capacitors are metal foil plates separated by oil-soaked paper. They're used as motor run and start capacitors and for PF correction.
- **Identified terminal** (an arrow, dot or dash on the can) marks the plate **nearest the metal case**. When these capacitors fail to ground, that plate is usually the one that shorts.
- **Connect the identified terminal to the line side, not the start winding.** If it shorts, the fault goes straight to ground and the breaker trips fast. Connected to the start winding instead, the winding's reactance limits the fault current, the breaker is slow, and the winding can overheat.

### Polarized (electrolytic) capacitors

- They have a marked + or − lead and are for **DC only**. Reversed polarity can destroy them, and they can **explode**.
- **Advantage:** very high capacitance in a small case, because the insulating oxide film is only a few molecules thick.
- **Wet type:** aluminum foil + borax electrolyte. If reversed, the oxide film dissolves and it shorts, but it **reforms** when polarity is corrected.
- **Dry type:** the electrolyte is held in gauze, so it's leak-proof. If reversed, it's **permanently damaged**. (Review Q11.)
- **AC electrolytic:** two wet-type electrolytics back-to-back (negative to negative) in one can. On each half-cycle one forms and the other shorts. Used as start capacitors for small motors and run capacitors in ceiling fans. (Review Q10.)

### Variable capacitors (19–12)

- Movable plates on a shaft interleave with fixed plates. Air dielectric and small area mean they're rated in **pF**.
- **Trimmer capacitors** adjust with a screw that moves one plate closer or farther.
- The symbol has an arrow through the capacitor.

### Reading markings

- Large and electrolytic capacitors usually print µF and voltage directly.
- **Color codes** (older or small parts) read in **pF**. There is **no single universal standard**, so check the manufacturer's data when in doubt.
- **Postage-stamp mica:** usually 5 dots (6-dot adds a third digit). **EIA** standard starts with a white dot (silver = paper dielectric). **JAN** (Joint Army-Navy, military) starts with a black dot. Then digits, multiplier, tolerance, and a class dot.
- **Ceramic:** the wide band is the **temperature coefficient**, then digits, multiplier and tolerance.
- **Dipped tantalum:** match-head shape, with color bands and dots for value, tolerance and voltage.
- **Film (number code), like "105 K":** first two digits = 10, the third digit = number of zeros (5), so 1,000,000 pF = **1 µF**. The letter is tolerance: J = ±5%, K = ±10%, M = ±20%, H = ±3%.

**Temperature coefficient (19–14):** how much capacitance changes with temperature, in **ppm/°C**. P (positive) means capacitance rises with heat, and N (negative) means it falls. "NP0" means essentially zero.

## 19–5 and 19–6 Capacitors in Parallel and Series

**Intuition:** Parallel capacitors act like one capacitor with bigger plates, so the capacitance adds. Series capacitors act like one capacitor with plates farther apart, so the total goes down. It's the **opposite of resistors and inductors**.

|  | Formula | Example (20, 30, 60 µF) |
| --- | --- | --- |
| Parallel | Cₜ = C₁ + C₂ + C₃ | **110 µF** |
| Series | 1/Cₜ = 1/C₁ + 1/C₂ + 1/C₃ | **10 µF** |
| Two in series | Cₜ = C₁C₂ / (C₁ + C₂) | — |
| N equal in series | Cₜ = C / N | two 50 µF → 25 µF |

**Voltage ratings (the part the formulas don't tell you)**

- **Parallel:** every capacitor sees the full voltage, so each one must be rated for it. The lowest rating limits the whole group.
- **Series:** the voltage **divides**. Equal capacitors split it equally. Two 370 V capacitors in series can handle about 740 V (Practical App 3).
- **Unequal series capacitors split voltage unevenly:** the **smallest** capacitor gets the **largest** share (voltage is inversely proportional to C). Check each one's rating.
- Real capacitors in series don't split perfectly, because of leakage differences. That's why high-voltage capacitor stacks use balancing resistors across each capacitor.

**Pitfalls**

- Using the resistor rules by habit: adding series capacitors, or using reciprocals for parallel ones.
- Mixing µF, nF and pF in one sum. Practice 4 (2.2 µF + 280 nF + 470 pF) is built to test this.
- Series total must be **smaller** than the smallest capacitor. Parallel total must be **larger** than the largest.

**Field use:** Two run capacitors in parallel can substitute for one larger value: 30 + 5 µF = 35 µF, as long as each is rated for the full voltage.
