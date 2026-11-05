# Lab 3 Motor Control: Forward / Reverse Wiring Diagrams (PRELIMINARY, text only)

Text version of `wiring-diagrams.html`, without the drawings. **Preliminary:** drawn from the lab sheet (LAB3-F20b) and the layout drawings, before the panel was built. Check the terminal positions on your own parts.

## Wire list (one row per physical conductor)

| # | Wire | Color | From | To | Route | Note |
|---|---|---|---|---|---|---|
| | **120 V supply** | | | | | |
| 1 | **H** | black | *cord* | CB1-1 (top) | cord → left tray → top duct | Cord hot (smooth conductor if a flat cord) |
| 2 | **N** | white | *cord* | TB1 (top) | cord → left tray → top duct | Cord neutral (may be ribbed black on a flat cord) |
| 3 | **G** | green | *cord* | TBG1 (top) | cord → left tray → top duct | Cord ground |
| 4 | **H1** | black | CB1-2 (bottom) | Transformer H1 | bottom duct → side channel → top duct |  |
| 5 | **N2** | white | TB1 (bottom) | Transformer H4 | bottom duct → side channel → top duct | Ladder calls this N2 at TB1 and N1 at the transformer. See note 4 |
| | **24 V secondary** | | | | | |
| 6 | **G** | green | TBG1 (bottom) | Transformer X4 | bottom duct | Bonds X4 to ground, landed ON the transformer X4 screw |
| 7 | **X4** | white | Transformer X4 | TB4 (bottom) | bottom duct | Starts the X4N bus (TB4–TB6 comb jumper) |
| 8 | **X1** | red | Transformer X1 | CB2-1 (top) | bottom duct → side channel → top duct |  |
| 9 | **24** | red | CB2-2 (bottom) | TB7 (bottom) | bottom duct | Starts the 24 V bus (TB7–TB9 comb jumper) |
| | **Rungs 5–6: FORWARD** | | | | | |
| 10 | **1** | red | STOP1 1 (door) | TB7 (top) | **DOOR CHANNEL (right tray)** |  |
| 11 | **2** | red | STOP1 2 (door) | STOP2 1 (door) | door (jumper) | Door jumper |
| 12 | **3** | red | STOP2 2 (door) | FWD 3 (door) | door (jumper) | Door jumper |
| 13 | **3** | red | FWD 3 (door) | REV 3 (door) | door (jumper) | Door jumper |
| 14 | **3** | red | REV 3 (door) | FW 7L4 | **DOOR CHANNEL (right tray)** | FW holding contact, line side (13 on some contactors) |
| 15 | **3** | red | FW 7L4 | RV 7L4 | top duct | Panel jumper to RV holding contact |
| 16 | **4** | red | FWD 4 (door) | FLS 21 (door) | door (jumper) | Door jumper |
| 17 | **4** | red | FLS 21 (door) | OLF 14/22 (= FW 8T4) | **DOOR CHANNEL (right tray)** | FW holding contact, load side (14 on some contactors) |
| 18 | **5** | red | FLS 22 (door) | RV aux 31 | **DOOR CHANNEL (right tray)** | Into the RV interlock (NC) |
| 19 | **6** | red | RV aux 32 | FW A1 | top duct |  |
| 20 | **7** | red | OLF A2 (= FW coil A2) | OLF 95 | on the overload face | Short loop on OLF face. Color: see note 3 |
| 21 | **8** | white | OLF 96 | TB5 (bottom) | bottom duct |  |
| | **Rungs 7–8: REVERSE** | | | | | |
| 22 | **9** | red | REV 4 (door) | RLS 21 (door) | door (jumper) | Door jumper |
| 23 | **9** | red | RLS 21 (door) | OLR 14/22 (= RV 8T4) | **DOOR CHANNEL (right tray)** | RV holding contact, load side |
| 24 | **10** | red | RLS 22 (door) | FW aux 31 | **DOOR CHANNEL (right tray)** | Into the FW interlock (NC) |
| 25 | **11** | red | FW aux 32 | RV A1 | top duct |  |
| 26 | **12** | red | OLR A2 (= RV coil A2) | OLR 95 | on the overload face | Short loop on OLR face. Color: see note 3 |
| 27 | **8** | white | OLR 96 | OLF 96 | bottom duct | OLR 96 joins OLF 96 |
| | **Rungs 9–10: pilot lights** | | | | | |
| 28 | **13** | red | TB8 (top) | FW aux 23 | top duct |  |
| 29 | **14** | red | FW aux 24 | FWDON X1 (door) | **DOOR CHANNEL (right tray)** |  |
| 30 | **16** | red | TB9 (top) | RV aux 23 | top duct |  |
| 31 | **17** | red | RV aux 24 | REVON X1 (door) | **DOOR CHANNEL (right tray)** |  |
| 32 | **15** | white | REVON X2 (door) | FWDON X2 (door) | door (jumper) | Door jumper |
| 33 | **15** | white | FWDON X2 (door) | TB6 (bottom) | **DOOR CHANNEL (right tray)** |  |
| | **Power circuit (simulated 3-phase)** | | | | | |
| 34 | **L1** | black | 3PHIN socket 24 (L1) | FW 1L1 | top duct |  |
| 35 | **L1** | black | FW 1L1 | RV 5L3 | top duct | RV swaps L1 and L3 |
| 36 | **L2** | black | 3PHIN socket 21 (L2) | FW 3L2 | top duct |  |
| 37 | **L2** | black | FW 3L2 | RV 3L2 | top duct |  |
| 38 | **L3** | black | 3PHIN socket 14 (L3) | FW 5L3 | top duct |  |
| 39 | **L3** | black | FW 5L3 | RV 1L1 | top duct | RV swaps L1 and L3 |
| 40 | **T1** | black | OLF 2T1 | TB-T1 (bottom) | bottom duct |  |
| 41 | **T1** | black | OLR 2T1 | TB-T1 (bottom) | bottom duct |  |
| 42 | **T2** | black | OLF 4T2 | TB-T2 (bottom) | bottom duct |  |
| 43 | **T2** | black | OLR 4T2 | TB-T2 (bottom) | bottom duct |  |
| 44 | **T3** | black | OLF 6T3 | TB-T3 (bottom) | bottom duct |  |
| 45 | **T3** | black | OLR 6T3 | TB-T3 (bottom) | bottom duct |  |

Door-channel wires (exactly 9): 1, 3, 4, 5, 9, 10, 14, 15, 17.

## Things to check

1. **PRELIMINARY: check your own parts before you wire.** This page was drawn from the lab sheet (LAB3-F20b), the component-layout and front-panel drawings, and the Additional Specifications. It was **not** drawn from photos of a built panel. The wire numbers and from/to terminals come from the ladder and should be right. Where each terminal physically sits on your contactors, aux blocks and the CR socket is a **guess**. Read the numbers stamped on your parts and go by those. Once the panel is wired, send photos and this page can be redrawn to match, the same as Lab 2.

2. **Exactly 9 wires through the door channel, and the door jumpers are why.** Wire numbers 1, 3, 4, 5, 9, 10, 14, 15 and 17 each cross the door **once** (the yellow tags). To keep it at one crossing per number, make these jumpers on the door itself: 2 (STOP1→STOP2), 3 (STOP2→FWD→REV), 4 (FWD→FLS), 9 (REV→RLS) and 15 (REVON X2→FWDON X2). Run all 9 in the **right** tray. The left tray is for the cord only. A control wire in the left tray, or a neutral (15) running by itself, loses selloff points.

3. **Wires 7 and 12 are not neutrals, so what color?** They run from the coil A2 to the overload 95, which is *upstream* of the OL contact. When an overload trips, 7 or 12 is at 24 V. The spec only says "24VAC Neutral: White", so they are drawn red here. In Lab 2 the same wire (wire 4) was white. Ask which color the instructor wants before you cut them. Wires 8 and 15 land straight on the X4N bus, so white is right for those.

4. **The lab sheet names the neutral jumper two ways.** The wire from TB1 (bottom) to the transformer is marked **N2** at TB1 and **N1** at the transformer. It is one conductor, so it gets one number. These labels use N2, as printed at the terminal block. Change it in the script if your instructor uses N1.

5. **Two kinds of contactor, same terminals.** The note on the lab sheet says some contactors use 13/14 for the holding contact and others use 7L4/14-22. 13 = 7L4 and 14 = 14/22. On the 7L4 type with the overload attached, the load side of that contact (8T4) is reached through the overload's **14/22** pass-through. The coil's A2 is reached through the overload's **A2** pass-through. Both work the same as in Lab 2. The interlocks (31-32, NC) and the pilot contacts (23-24, NO) are on the front aux block. Check that your aux block really has 23-24 NO and 31-32 NC.

6. **Transformer grounding: green goes to the X4 screw.** Per *Proper Grounding of the Motor Control Transformer*, the green bond lands directly on the transformer's X4 terminal, next to the white X4. Landing it at TB4 instead would be a code violation, even though Constructor draws it that way. Procedure photo 4 has to show it clearly.

7. **The power circuit: RV swaps L1 and L3.** FW gets L1/L2/L3 on 1L1/3L2/5L3. RV gets L3/L2/L1. The diagram makes the line-side jumpers contactor to contactor (FW 1L1→RV 5L3, FW 3L2→RV 3L2, FW 5L3→RV 1L1), so each socket terminal has only one wire. On the load side, both overloads land on the bottom of TB-T1..T3 (2 wires per terminal, which is allowed). Nothing goes on the top of TB-T (the motor is simulated) or upstream of the socket. Before power-on, an ohmmeter check catches a swap. FW 1L1 to RV 5L3 should be ~0 Ω, and FW 1L1 to RV 1L1 should be OL.

8. **Interlocking is electrical only.** FWD and REV are plain NO buttons with no button interlock. The only thing keeping FW and RV from both pulling in is each one's NC 31-32 in the other's rung. If your reversing pair has a mechanical interlock between them, install it too. Operation tests 7 and 8 film exactly this.

9. **Not used in this lab (leave empty).** TB2, TB3, TBG2, TBG3, the selector switch, the limit switches' NO 13-14, OLF/OLR 97-98, the other CR socket terminals, and the tops of TB-T1..T3. The spec says "No wiring to extra terminals".
