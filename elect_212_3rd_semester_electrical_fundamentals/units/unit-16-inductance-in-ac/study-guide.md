# Unit 16 Study Guide: Inductance in AC Circuits

Oct 22, 2026 · @Jeff

## Why this chapter matters

Most loads you'll wire have a coil in them: motors, transformers, magnetic ballasts, contactor and relay coils, line reactors. A coil limits AC current in a way that isn't resistance, and it makes current **lag** voltage. That lag is the root of power factor, VARs, and why a meter's volts × amps doesn't equal watts on a motor circuit.

This unit introduces four ideas you'll use for the rest of the AC course:

| Idea | Symbol | Unit | One-line meaning |
| --- | --- | --- | --- |
| Inductance | L | henry (H) | How strongly a coil resists a *change* in current; set by how it's built |
| Inductive reactance | Xₗ | ohm (Ω) | How much a coil limits AC current at a given frequency |
| Impedance | Z | ohm (Ω) | Total current-limiting effect: R and X combined as a right triangle |
| Reactive power | VAR | volt-amp reactive | Power that charges the magnetic field and is handed back each cycle; does no work |

The chapter's big result: in a pure inductor, **current lags voltage by 90°**, and the coil uses **no true power** (watts).

## 16–1 Inductance and induced voltage

**Intuition:** A coil is like a heavy flywheel for current. It doesn't care how much current flows; it fights any *change* in current. AC is changing all the time, so a coil is always pushing back.

**The four facts from Unit 13 that the whole chapter rests on**

1. When magnetic flux cuts a coil, a voltage is induced in it.
2. The induced voltage opposes the applied voltage. This is **counter-EMF (CEMF)**, also called Lenz's law.
3. The induced voltage is proportional to the **rate of change** of current, not to the current itself.
4. So an inductor **opposes a change of current**.

**Definitions**

- **Inductance (L):** a coil's ability to induce voltage in itself. Measured in **henrys (H)**. Small coils are in millihenrys: 1 mH = 0.001 H.
- **Where it matters:** every conductor has a tiny bit of inductance, but it's only counted when the load contains a coil (motor, transformer, ballast, choke, solenoid).

**How a coil limits current.** Most of the applied voltage is cancelled by the CEMF. Only what's left pushes current through the wire's resistance. The book's example: a coil with 6 Ω of wire on 120 V draws only 0.8 A, because only 4.8 V is "left over" for the resistance.

**Book inconsistency to watch:** The book first says 120 V − 116 V CEMF = 4 V left for the resistance (plain subtraction). A page later it does it correctly: the resistive drop and the CEMF are 90° apart, so they combine by the Pythagorean theorem, √(120² − 4.8²) = 119.904 V. Use the Pythagorean method. The subtraction example is only a rough illustration.

**Common misunderstanding:** An ohmmeter only measures a coil's wire **resistance**, not its reactance. A contactor coil that reads 6 Ω does *not* draw 120/6 = 20 A on 120 VAC. It draws far less, because reactance limits it. That's also why a coil that "reads fine" on an ohmmeter can still be the wrong coil.

## 16–2 Inductive Reactance (Xₗ)

**Intuition:** Reactance is the coil's push-back measured in ohms, so you can drop it into Ohm's law in place of R. It isn't resistance: nothing heats up. It's the CEMF limiting the current.

**Formula**

```math
X_L = 2\pi f L
```

- **Xₗ:** inductive reactance, in ohms (Ω)
- **2π:** a constant, about 6.2832
- **f:** frequency in hertz
- **L:** inductance in henrys

**Rearranged:** L = Xₗ / (2πf) and f = Xₗ / (2πL).

**Ohm's law with reactance:** I = E / Xₗ, E = I × Xₗ, Xₗ = E / I.

**Memorize 377.** At 60 Hz, 2π × 60 = 376.99 ≈ **377**. So at 60 Hz, Xₗ = 377 × L and L = Xₗ / 377.

**What sets the reactance**

- **Construction (sets L):** number of turns, how tightly they're wound, coil size, and the core material. An iron core gives far more inductance than air.
- **Frequency (sets how fast the flux cuts the turns):** higher frequency, faster cutting, more CEMF, more reactance.

**Minimum to solve problems:** Find Xₗ first (from 2πfL or from E/I), then use Ohm's law. If the frequency changes, L stays the same, so find L at the old frequency, then compute the new Xₗ (Example 16–3).

**Shortcut for frequency changes:** Xₗ is directly proportional to f, so current in a pure inductor is *inversely* proportional to f. Example 16–3: 24 A at 60 Hz becomes 24 × 60/400 = 3.6 A at 400 Hz. Same answer, no need to find L.

**Exceptions and pitfalls**

- **At DC (f = 0), Xₗ = 0.** The coil is just its wire resistance. Putting an AC coil (contactor, solenoid, transformer) on DC of the same voltage lets huge current flow and burns it up.
- **Lower frequency means more current.** A 60 Hz coil or transformer on 50 Hz draws about 20% more current and runs hotter; iron cores can also saturate.
- **Iron-core inductance isn't truly constant.** The book treats L as fixed. Real iron cores **saturate** at high current, L drops, and current climbs fast. Air-core coils don't saturate.
- **Units:** mH must be converted to H (33 mH = 0.033 H), and kHz to Hz, before using the formula.

## 16–3 to 16–5 Symbols, Series and Parallel

**Schematic symbols (16–3):** An inductor is drawn as a coil (a row of loops or bumps). **Two parallel lines** beside it mean an **iron core**; no lines means an **air core**.

**Intuition:** Inductors combine exactly like resistors. So do their reactances.

|  | Series | Parallel |
| --- | --- | --- |
| Inductance | Lₜ = L₁ + L₂ + L₃ | 1/Lₜ = 1/L₁ + 1/L₂ + 1/L₃ |
| Reactance | Xₗₜ = Xₗ₁ + Xₗ₂ + Xₗ₃ | 1/Xₗₜ = 1/Xₗ₁ + 1/Xₗ₂ + 1/Xₗ₃ |
| Two in parallel | — | Product over sum: L₁L₂ / (L₁ + L₂) |
| N equal ones in parallel | — | L / N |

**Sanity checks**

- Series total is **larger** than any single inductor.
- Parallel total is **smaller** than the smallest one.

**Exception the book doesn't mention:** These formulas assume the coils are **not magnetically coupled** (their fields don't link). If two coils sit close together or share a core, their **mutual inductance** adds or subtracts, depending on how they're wound and connected. That's how transformers work, and it's covered later.

**Pitfalls**

- Use the reciprocal key carefully: find the sum of reciprocals, then take its reciprocal one more time. Forgetting that last step is the most common error.
- Don't mix henrys and millihenrys in the same sum.

## 16–6 Voltage and Current in a Pure Inductor: the 90° Lag

**The result:** In a pure inductive circuit, **current lags the applied voltage by 90°**. Current reaches its peak a quarter cycle (4.17 ms at 60 Hz) after voltage does.

**Why, in three steps**

1. Induced voltage depends on how fast current is *changing*, not how big it is.
   - At the current's peak, it momentarily stops changing, so induced voltage = 0.
   - As current crosses zero, it's changing fastest, so induced voltage is at its peak.
   - That puts the induced voltage 90° away from the current (current leads the induced voltage by 90°).
2. The induced voltage is 180° opposite the applied voltage.
3. 180° − 90°: current **lags the applied voltage** by 90°.

**Memory aid:** **ELI the ICE man.**

- **ELI:** in an inductor (L), voltage (E) comes before current (I). Current lags.
- **ICE:** in a capacitor (C), current (I) comes before voltage (E). Current leads. (That's next unit.)

**Exception:** Exactly 90° only happens in a *pure* inductor. Real coils have wire resistance, so the angle is a bit less than 90°. Real motor circuits are often 30° to 40°, because the motor is doing work (a resistive part).

**Common mistake:** "Lags" doesn't mean the current is smaller or delayed in starting. It means its peaks and zero crossings happen later in each cycle.

## 16–7 and 16–8 Power and Reactive Power (VARs)

**Intuition:** A pure inductor is like a spring. Every quarter cycle it stores energy in its magnetic field; the next quarter cycle it hands it back to the source. Over a full cycle, nothing is used up, so **true power = 0 W**. But the current still really flows in the wires.

**Sign logic from Unit 15:** With a 90° shift, voltage and current have the **same sign half the time** (power flows into the field) and **opposite signs half the time** (power flows back). The two halves cancel.

**General power formula**

```math
P = E \times I \times \cos\theta
```

- **θ:** the phase angle between applied voltage and current.
- Resistive load: θ = 0°, cos 0° = 1, so P = E × I.
- Pure inductor: θ = 90°, cos 90° = 0, so P = 0.
- cos θ is the **power factor**, coming in later units.

**Reactive power (VARs)** = **v**olt-**a**mperes-**r**eactive. Same math as watts, using inductive values:

- VARs = Eₗ × Iₗ
- VARs = Eₗ² / Xₗ
- VARs = Iₗ² × Xₗ
- kVAR = VARs / 1000

**Key point:** VARs aren't true power, but they're **real current in real conductors**. Wires, breakers and transformers have to carry it and heat up from it. That's why reactors and capacitors carry a kVAR rating, and why an undersized one fails (Example 16–7: 480 V × 125 A = 60 kVAR minimum).

**Where the coil's watts do come from:** losses. I²R in the wire, plus **eddy currents** and **hysteresis** in an iron core. These are why a transformer or ballast gets warm with no load attached.

**Pitfalls**

- Use the voltage **across the inductor** (Eₗ) and the current **through it** (Iₗ), not the supply voltage if other parts are in series.
- Don't label VARs as watts. Different units, different meaning.

## 16–9 Q of an Inductor and Impedance

**Intuition:** Every real coil is an ideal inductor in series with a little resistance (its wire). **Q (quality)** says how "pure" the coil is: how much reactance it has compared with resistance.

**Formulas**

- Q = Xₗ / R
- Xₗ = Q × R
- R = Xₗ / Q

Q has no units (ohms divided by ohms).

**What raises Q:** heavier wire (less resistance), fewer losses. Many turns of fine wire gives low Q.

**Rule of thumb:** **Q ≥ 10** is treated as a pure inductor, and R is ignored. With Xₗ = 100 Ω and R = 10 Ω, Z is only 100.5 Ω, half an ohm more than Xₗ alone.

**Impedance (Z):** the total current-limiting effect of R and Xₗ together, in ohms. R and Xₗ are 90° apart, so they form the legs of a right triangle, and Z is the hypotenuse (Unit 14 pays off again):

```math
Z = \sqrt{R^2 + X_L^2}
```

- Z = E / I (what you get from measured volts and amps)
- Xₗ = √(Z² − R²) (to back out the reactance)

**Minimum procedure to find a real coil's true inductance** (the book's 480 V / 0.6 A / 150 Ω example):

1. Measure volts and amps, then Z = E / I (800 Ω).
2. Measure wire resistance with an ohmmeter, power off (150 Ω).
3. Xₗ = √(Z² − R²) (785.8 Ω).
4. L = Xₗ / (2πf) (2.084 H).

**Pitfalls**

- **Z ≠ R + Xₗ.** They're 90° apart, so use the Pythagorean theorem. Adding them straight is the Unit 14 mistake again.
- E / I gives **Z**, not Xₗ. They're only about equal when Q ≥ 10.

## Easily overlooked things for electricians

1. **Inductive kick.** Open a circuit with a coil in it and the collapsing field tries to keep current flowing. It does that by producing a voltage spike that can be many times the supply voltage. That's the arc you see at contactor and relay contacts, and it's why coils get suppression diodes, RC snubbers or MOVs. It can also damage PLC outputs.
2. **Stored energy during testing.** Large windings store a lot of energy when DC test current flows through them, for example during a transformer winding-resistance or DLRO test on a big coil. Breaking the test leads can produce a dangerous kick. Let the test set discharge the winding before you disconnect.
3. **Never open a loaded CT secondary.** The same physics, at a larger scale: with nothing to limit it, the secondary voltage can climb to lethal levels. Short the CT secondary before you disconnect a meter or relay.
4. **Contactor coil inrush.** When a contactor's armature is open, the air gap lowers L, so Xₗ is low and inrush current is several times the sealed current. If the armature sticks open (dirt, a mechanical jam, low voltage), the coil keeps drawing inrush current and burns out.
5. **AC coil on DC = burned coil.** At DC, Xₗ = 0, so only the wire resistance limits current. Always match coil voltage *and* type (AC or DC).
6. **Frequency matters on nameplates.** 60 Hz gear on 50 Hz draws more current and can saturate. 50 Hz gear on 60 Hz draws less current but may underperform (Practical Application 1).
7. **Inductive loads drag power factor down.** Motors, transformers and magnetic ballasts make current lag. Utilities bill large customers for low power factor, which is why capacitor banks are used for PF correction (coming in the capacitance and power-factor units).
8. **Line reactors on VFDs** are just inductors in series with the line, sized in % impedance and kVAR. They limit inrush and fault current and smooth out harmonics, all using the Xₗ ideas from this chapter.

## Notes on the homework

- **Q3 ("to what is Xₗ proportional?"):** Inductance *and* frequency. Students often name only one.
- **Q5 (three inductors in parallel):** Watch the reciprocal-of-the-sum step. Your answer must be smaller than 0.05 H.
- **Q6:** It uses the Q5 inductors **in series** at 60 Hz. Add the inductances, then multiply by 377.
- **Q7:** Uses 1000 Hz, so **377 doesn't apply**. Compute 2πf fresh.
- **Q9 and Q10 (frequency changes):** L doesn't change. Use the proportion shortcut: Xₗ scales with f, current scales inversely with f.
- **Q12 and Q13:** Direct use of Q = Xₗ / R, rearranged.
- **Practice Problem 1 table:** Each row is missing one of L, f or Xₗ. Pick the matching rearrangement: Xₗ = 2πfL, L = Xₗ / (2πf), f = Xₗ / (2πL).
- **Practice Problems 2–5:** 33 mH = 0.033 H. Problems 3–5 give wire resistance, so use the impedance-triangle procedure: Z = E/I, then Xₗ = √(Z² − R²). In Problem 4, "total current-limiting effect" means **Z**, not Xₗ.
- **Practical App 1 (50 Hz ballasts on 60 Hz):** Think about which way Xₗ moves when f goes up, and what that does to current. Then ask whether the likely problem is too much current or too little.
- **Practical App 2 (replacement inductor):**
  - Use the **324 V measured across the inductor**, not the 480 V supply. That's the trap.
  - Z = 324 / 18, then remove the 1.2 Ω wire resistance with the Pythagorean theorem to get Xₗ, then L = Xₗ / 377.
  - VAR rating uses the inductor's voltage and current.
  - For "should you worry about the resistance?", compute Q. If it's well above 10, the resistance barely matters.

## One-glance cheat sheet

- **Inductance:** L, in henrys. Set by construction: turns, spacing, size, core. It doesn't change with frequency (until an iron core saturates).
- **Reactance:** Xₗ = 2πfL. At 60 Hz, Xₗ = 377 × L. L = Xₗ / (2πf). f = Xₗ / (2πL).
- **Ohm's law:** I = E / Xₗ for a pure inductor. I = E / Z for a real coil.
- **Frequency:** Xₗ goes up with f, so current goes down. At DC, Xₗ = 0.
- **Series:** Lₜ = L₁ + L₂ + … (same for Xₗ). **Parallel:** reciprocal formula, product over sum, or L/N.
- **Phase:** Current lags voltage by 90° in a pure inductor. **ELI** the ICE man.
- **Power:** P = E × I × cos θ. Pure inductor: 0 W.
- **VARs:** Eₗ × Iₗ = Eₗ² / Xₗ = Iₗ² × Xₗ. kVAR = VARs / 1000.
- **Q:** Xₗ / R. Q ≥ 10 counts as pure.
- **Impedance:** Z = √(R² + Xₗ²). Xₗ = √(Z² − R²). Never R + Xₗ.
- **Ohmmeter:** reads only a coil's R, never its Xₗ or Z.
