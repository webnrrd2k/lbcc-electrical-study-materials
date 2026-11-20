# Conduit Bending Study Guide & Cheat Sheet (EMT & RMC)

A comprehensive reference guide for electrical conduit bending math, bender shoe markings (Standard, Greenlee, and Milwaukee), and layout formulas for Electrical Metallic Tubing (EMT) and Rigid Metal Conduit (RMC).

---

## 1. Essential Bending Formulas

1. **90° Stub-Up Mark:**
   $$\text{Mark} = \text{Desired Stub Height} - \text{Bender Take-Up (Deduction)}$$
   *(Align pencil mark with the **Arrow**)*

2. **90° Gain (True Developed Pipe Length):**
   $$\text{Total Pipe Required} = \text{Leg 1} + \text{Leg 2} - \text{Gain}$$
   $$\text{Gain} \approx (2 \times \text{Take-Up}) - (1.57 \times \text{Centerline Radius})$$

3. **Back-to-Back 90° Bend:**
   $$\text{Mark 2} = \text{Exact Outside-to-Outside Distance}$$
   *(Measured from the back heel of the first 90°; align with the **Star** with the hook facing away—**no deduction** subtracted)*

4. **Offset Distance Between Bends (Travel):**
   $$\text{Distance Between Marks} = \text{Obstacle Height (Offset Depth)} \times \text{Multiplier}$$
   *(Align both marks with the **Arrow**)*

5. **Total Shrinkage:**
   $$\text{Shrinkage} = \text{Obstacle Height (Offset Depth)} \times \text{Shrinkage Constant per Inch}$$
   *(Always **add** shrinkage to your distance to the obstruction when bending toward an obstacle)*

6. **3-Point Saddle (45° Center / 22.5° Outers):**
   $$\text{Center Mark} = \text{Distance to Center of Obstacle} + \left(\text{Height} \times \frac{3}{16}"\right)$$
   *(Align with the **Notch/Rim**)*
   $$\text{Outer Marks} = \text{Center Mark} \pm (\text{Height} \times 2.5")$$
   *(Align with the **Arrow**)*

7. **4-Point Saddle (Two Back-to-Back Offsets):**
   * **Mark 1 (closest to box):** $\text{Distance to Start of Obstacle} + \text{Shrinkage}$
   * **Mark 2:** $\text{Mark 1} + (\text{Height} \times \text{Multiplier})$
   * **Mark 3:** $\text{Mark 2} + \text{Width of Obstacle}$
   * **Mark 4:** $\text{Mark 3} + (\text{Height} \times \text{Multiplier})$

8. **Box Offset (Two 10° Bends):**
   * **Mark 1:** $2"\text{–}3"$ from the end of the conduit
   * **Mark 2:** $\text{Mark 1} + (\text{Offset Depth} \times 6.0)$ *(e.g., for a $1/2"$ box offset: $0.5" \times 6.0 = 3"$ apart; bend the box offset **before** bending a stub-up)*

---

## 2. Hand Bender Shoe Markings (Standard, Greenlee & Milwaukee)

### Standard Shoe Symbols
* **Arrow (Front of Hook):** Alignment mark for standard **90° stub-ups**, **offsets**, and the **outer bends** of a 3-point saddle.
* **Star (Back Heel of Shoe):** Alignment mark for the **back of a 90° bend** (used for back-to-back 90s when measuring from the outside heel of the first 90°).
* **Notch / Rim / Teardrop (Center of Shoe):** Center-of-bend mark used for the **center 45° bend** of a 3-point saddle.
* **Degree Scale ($10^\circ, 22.5^\circ, 30^\circ, 45^\circ, 60^\circ$):** Cast on the side of the shoe to verify bend angle.

### Greenlee vs. Milwaukee Shoe Differences
* **Greenlee (Site-Rite™ Head):**
  * **Center-of-Bend Mark:** Uses a **V-notch** on the top rim for 45° saddle centers.
  * **Degree Sighting:** Features the cast-in **Site-Rite™** sighting system—read the angle at the edge of the shoe when bending in the air, or align the cast degree lines parallel to the floor when bending on the ground.
  * **Dual-Sizing:** A **3/4" EMT** shoe is dual-rated to bend **1/2" Rigid/IMC** (6" deduction); a **1" EMT** shoe bends **3/4" Rigid/IMC** (8" deduction).
* **Milwaukee (High-Contrast Head):**
  * **Center-of-Bend Mark:** Uses a **triangle/notch** on the top rim for 45° saddle centers and a prominent **Star** on the heel.
  * **Degree Sighting:** Features **high-contrast raised degree markings** on both sides of the shoe plus a **multiplier/shrinkage reference chart** cast directly onto the handle.
  * **Dual-Sizing:** Like Greenlee, the **3/4" EMT** shoe bends **1/2" Rigid/IMC** (6" deduction) and the **1" EMT** shoe bends **3/4" Rigid/IMC** (8" deduction).

---

## 3. Core Bending Constants & Multipliers

### 90° Stub-Up Deductions (Take-Up) & Gain
> **Note:** Rigid (RMC) uses the next-size-up EMT bender shoe for 1/2" and 3/4", so its deduction matches that shoe size. Account for slightly greater springback on steel RMC by over-bending ~2°–3°.

| Conduit Size & Type | Hand Bender Shoe Used | 90° Deduction (Take-Up) | Approx. 90° Gain |
| :--- | :--- | :--- | :--- |
| **1/2" EMT** | 1/2" EMT Shoe | **5"** | ~2-5/8" |
| **3/4" EMT** | 3/4" EMT Shoe | **6"** | ~3-1/4" |
| **1" EMT** | 1" EMT Shoe | **8"** | ~4-1/4" |
| **1-1/4" EMT** | 1-1/4" EMT Shoe | **11"** | ~5-3/4" |
| **1/2" RMC (Rigid)** | 3/4" EMT / 1/2" Rigid Shoe | **6"** | ~3-1/4" |
| **3/4" RMC (Rigid)** | 1" EMT / 3/4" Rigid Shoe | **8"** | ~4-1/4" |
| **1" RMC (Rigid)** | 1-1/4" EMT / 1" Rigid Shoe | **11"** | ~5-3/4" |

### Offset Multipliers & Shrinkage Constants (Applies to Both EMT & RMC)

| Bend Angle | Multiplier ($\text{Distance} = \text{Height} \times M$) | Shrinkage per Inch ($\text{Shrink} = \text{Height} \times S$) |
| :--- | :--- | :--- |
| **10°** | **6.0** | **1/16"** ($0.0625"$) |
| **22.5°** | **2.6** | **3/16"** ($0.1875"$) |
| **30°** | **2.0** | **1/4"** ($0.25"$) |
| **45°** | **1.4** *(exact: 1.414)* | **3/8"** ($0.375"$) |
| **60°** | **1.2** *(exact: 1.155)* | **1/2"** ($0.50"$) |

---

## 4. Practice Bends Quick-Reference Restatement

### 1. EMT 3-Point Saddle
* **Angles:** **22.5° – 45° – 22.5°**
* **Constants:** Shrinkage = **3/16" per inch** of height | Outer spacing = **2.5" per inch** of height
* **Formulas:**
  * $\text{Center Mark} = \text{Distance to Center} + (\text{Height} \times \frac{3}{16}")$ *(Align with **Notch/Rim**)*
  * $\text{Outer Marks} = \text{Center Mark} \pm (\text{Height} \times 2.5")$ *(Align with **Arrow**)*

### 2. EMT 4-Point Saddle
* **Angles:** Two back-to-back offsets (typically **30°** or **22.5°**)
* **Constants (at 30°):** Multiplier = **2.0** | Shrinkage = **1/4" per inch**
* **Formulas:**
  * $\text{Mark 1} = \text{Distance to Start of Obstacle} + \text{Shrinkage}$
  * $\text{Mark 2} = \text{Mark 1} + (\text{Height} \times \text{Multiplier})$
  * $\text{Mark 3} = \text{Mark 2} + \text{Width of Obstacle}$
  * $\text{Mark 4} = \text{Mark 3} + (\text{Height} \times \text{Multiplier})$

### 3. EMT Offsets
* **Angles:** **10°, 22.5°, 30°, or 45°**
* **Constants (at 30°):** Multiplier = **2.0** | Shrinkage = **1/4" per inch**
* **Formulas:**
  * $\text{Mark 1 (toward obstruction)} = \text{Distance to Obstruction} + (\text{Height} \times \text{Shrinkage})$
  * $\text{Mark 2} = \text{Mark 1} + (\text{Height} \times \text{Multiplier})$ *(Align both with **Arrow**)*

### 4. EMT Back-to-Back 90°
* **Angles:** Two **90°** bends
* **Constants:** **No deduction (0")** subtracted when measuring from the outside heel of the first 90°.
* **Formula:**
  * $\text{Mark 2} = \text{Exact Outside-to-Outside Distance}$ from the back of the first 90° *(Align with **Star**, hook facing away)*

### 5. EMT Stub 90° with Box Offset
* **Angles:** One **90°** stub + two **10°** bends (typically a **3/8"** or **1/2"** box offset)
* **Constants:** 90° Deductions: **5"** (1/2"), **6"** (3/4"), **8"** (1") | 10° Multiplier: **6.0** | 10° Shrinkage: **1/16" per inch**
* **Formulas:**
  * **Box Offset:** $\text{Mark 1} = 2"\text{–}3"$ from end; $\text{Mark 2} = \text{Mark 1} + (\text{Offset Depth} \times 6.0)$
  * **Stub 90°:** $\text{Stub Mark} = \text{Desired Stub Height} - \text{Deduction}$ *(Make the box offset first, then measure from that end)*

### 6. RMC 3-Point Saddle
* **Angles:** **22.5° – 45° – 22.5°**
* **Constants:** Shrinkage = **3/16" per inch** | Outer spacing = **2.5" per inch** *(Over-bend ~2°–3° for springback)*
* **Formulas:**
  * $\text{Center Mark} = \text{Distance to Center} + (\text{Height} \times \frac{3}{16}")$ *(Notch/Rim)*
  * $\text{Outer Marks} = \text{Center Mark} \pm (\text{Height} \times 2.5")$ *(Arrow)*

### 7. RMC Offsets
* **Angles:** **10°, 22.5°, 30°, or 45°**
* **Constants (at 30°):** Multiplier = **2.0** | Shrinkage = **1/4" per inch**
* **Formulas:**
  * $\text{Mark 1} = \text{Distance to Obstruction} + (\text{Height} \times \text{Shrinkage})$
  * $\text{Mark 2} = \text{Mark 1} + (\text{Height} \times \text{Multiplier})$ *(Arrow)*

### 8. RMC 4-Point Saddle
* **Angles:** Two back-to-back offsets (typically **30°** or **22.5°**)
* **Constants (at 30°):** Multiplier = **2.0** | Shrinkage = **1/4" per inch**
* **Formulas:**
  * $\text{Mark 1} = \text{Distance to Start of Obstacle} + \text{Shrinkage}$
  * $\text{Mark 2} = \text{Mark 1} + (\text{Height} \times \text{Multiplier})$
  * $\text{Mark 3} = \text{Mark 2} + \text{Width of Obstacle}$
  * $\text{Mark 4} = \text{Mark 3} + (\text{Height} \times \text{Multiplier})$

### 9. RMC Stub 90°
* **Angles:** One **90°** bend
* **Constants (Deductions):** **1/2" RMC** = **6"** | **3/4" RMC** = **8"** | **1" RMC** = **11"** *(Uses the next-size-up EMT shoe)*
* **Formula:**
  * $\text{Stub Mark} = \text{Desired Stub Height} - \text{RMC Deduction}$ *(Align with **Arrow**)*

### 10. RMC Back-to-Back 90°
* **Angles:** Two **90°** bends
* **Constants:** **No deduction (0")** when measuring from the outside back of the first 90°.
* **Formula:**
  * $\text{Mark 2} = \text{Exact Outside-to-Outside Distance}$ from the back heel of the first 90° *(Align with **Star**, hook facing away)*

---

## 5. High-Yield NEC Code Quick Check
* **Maximum Bends Between Pull Points:** **360°** total including offsets (*NEC 358.26 for EMT / NEC 344.26 for RMC*).
* **EMT Securing & Supporting:** Within **3 ft** of every box, cabinet, or fitting, and at intervals not exceeding **10 ft** (*NEC 358.30(A)*).
* **RMC Securing & Supporting:** Within **3 ft** of every box or fitting, and every **10 ft** (*NEC 344.30(A)*; up to 20 ft allowed for straight runs with threaded couplings).