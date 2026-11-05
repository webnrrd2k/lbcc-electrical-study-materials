# Lab 3 — Forward/Reverse Controls: Plan

ELECT 435A (70156), Fall 2026. Written 2026-11-05 from the Canvas pages saved in this folder.
The task-by-task checklist is in `lab3-tasks.org`.

---

## 1. The most important thing: the real deadline is drop-off, not Nov 30

Canvas lists **Testing Prior to Power ON**, **Operation (video)** and **Procedure Component Install & Wiring (photos)** as due **Mon Nov 30**. But:

- **Controller Drop-off** is due **Tue Nov 24, 6 pm**, and the page says "*By now it is expected that your wiring is completed and operational.*"
- The listed drop-off windows are **Fri Nov 20 (1–9 pm)** and **Sat Nov 21 (8 am–2 pm)** in RR101.
- When the box comes back it has **4 faults installed**. You can't film a clean operation demo or take "as-built" photos after that.

So everything that needs a working, unmodified box has to be done **before you drop it off**. Your real target is a finished, tested, filmed and photographed box by **Thu Nov 19**, then drop-off Fri Nov 20 or Sat Nov 21. The Nov 30 dates only say when you have to upload.

## 2. Everything Lab 3 is graded on (672 pts total)

Listed in the order you will actually do them, not the order Canvas shows them.

| # | Deliverable | Pts | Canvas due | When you actually do it | Type |
|---|---|---|---|---|---|
| 1 | Check In 1 (3 photos) | 10 | Mon Nov 16 | Sun Nov 15 | PDF |
| 2 | Testing Prior to Power ON (20-question quiz) | 100 | Mon Nov 30 | Wed Nov 18, *before* power-on | Quiz |
| 3 | Operation (demo video, 10 tests) | 100 | Mon Nov 30 | Thu Nov 19, before drop-off | Media |
| 4 | Procedure Component Install & Wiring (5 photos) | 55 | Mon Nov 30 | Thu Nov 19, before drop-off | Image upload |
| 5 | Check In 2 (3 photos) | 10 | Mon Nov 23 | Thu Nov 19 (take the photos before drop-off) | PDF |
| 6 | Controller Drop-off (text: your pick-up time) | 10 | Tue Nov 24 | The day you drop off | Text |
| 7 | Selloff (instructor grades your wiring) | 100 | Mon Dec 7 | Graded while the instructor has the box. Your part is the self-inspection before drop-off | — |
| 8 | Check In 4 (3 photos) | 10 | Sun Dec 6 | After troubleshooting | PDF |
| 9 | Timed Troubleshooting (4-hr quiz + video) | 2 | Mon Dec 7 | One 4-hour block after pick-up | Quiz + video |
| 10 | Forward/Reverse Lab Report | **275** | Sat Dec 12 | Write it in pieces as you go, finish ~Dec 10 | PDF |

The report is 41% of the lab. The **Project Conclusion alone is 50 pts**, more than the operation video's wiring score.

## 3. Phases

### Phase 0 — Orientation (Nov 5–8)
1. Watch, in this order:
   - `ELECT-435A-Lab3-Circuit [amJ3XY5agPo].mkv` (20:42): how the circuit works. Take notes on the ladder as you go.
   - `ELECT-435A-Lab3-Wiring [D7uTXLA_n8g].mkv` (6:49): installing and wiring.
   - Hold off on `ELECT 435A LAB3 OPERATION DEMO [AAsnMvPTKYE].mkv` (2:42) until you're ready to film. It's the model for your own video.
2. Study `LAB3-F20b(Ladder Diagram)-1.pdf` with `Additional Specifications…pdf`, `LAB3-COMPONENTS-1.PNG`, `LAB3-FRONT PANEL-1.PNG`, and `Proper Grounding of the Motor Control Transformer-2.pdf`.
3. Write your own wire list (a draft is in §8 of this file) and mark which wires cross the "door" (exactly 9).
4. Start the report file now: cover sheet and all section headers (see §7).

### Phase 1 — Diagrams (Nov 6–10): 40 report pts you can earn before touching a screwdriver
- **Constructor diagram** of the ladder (20 pts). There are videos in the Introduction module: *Printing your Line Ladder Diagram with Constructor* and *Getting Line Ladder Diagrams into your Lab Reports*.
- **Hand-drawn diagram** (20 pts). Use a straightedge, label everything, and draw it neatly. "Crooked lines" and "not labeled" are the rubric's markdown reasons.

### Phase 2 — Install components (Nov 7–10)
Follow the component layout from left to right: transformer, CB1, TBG1–3 (green), TB1–3, TB4–6 (24V-N), TB7–9 (24V-H), CB2, 3PHIN (CR socket), FR (FW) and RV contactors with OLF/OLR, 3PH POWER terminals TB-T1..T3. Put **end stops between every component** (not between terminal blocks). Door layout from the front: STOP1, FWD, STOP2, REV, selector (unused), FLS, RLS, FWDON, REVON, AC IN.

### Phase 3 — Wire it (Nov 9–17)
Suggested order, one rung at a time, checking each wire off on the ladder:
1. 120 V input: cord → CB1, TB1, TBG1 → transformer primary (black/white/green).
2. Transformer secondary + grounding: X1 → CB2 → TB7 (24 bus); X4 → TB4 (X4N bus); green from TBG1 **directly to X4 on the transformer** (see grounding PDF).
3. Rung 5–6 (FWD), rungs 7–8 (REV), rungs 9–10 (pilot lights).
4. Power circuit: 3PHIN socket → FW/RV line side (RV swaps L1 and L3) → OLF/OLR → TB-T1..T3.

Check In 1 photos on Sun Nov 15, whatever state the box is in. Points are for following the instructions and showing progress, not for being finished.

### Phase 4 — Self-inspection, then the test quiz (Nov 17–18)
1. Do the **selloff self-inspection** in §6 first. The selloff is 100 pts and gets graded while the instructor has your box.
2. Make a **paper testing worksheet** (20 rows: question, meter leads, expected, actual). **The report gives credit only for the original sheet you filled in, not a retyped one.**
3. Take the *Testing Prior to Power ON* quiz with the power **off**, writing each reading on the sheet. Repeat until you get 100%. Write down anything you fix ("Items you fixed" is a required report item).
4. **Screenshot / print the quiz** for the report.

### Phase 5 — Power on, film, photograph (Nov 19)
1. Power up only after scoring 100% on the test quiz.
2. Print `LAB 3 OPERATIONAL DEMONSTRATION.pdf`. Rehearse every test, then watch the instructor's demo video.
3. Film in **horizontal** format, close up, showing the buttons, lights and contactors. **Start with 5 s of your phone showing the date and time.** Film all **10** rubric tests (see §5). The printed sheet lists only 8.
4. Take the 5 Procedure photos (§4) and the Check In 2 photos. Upload them now or any time before the due date.

### Phase 6 — Drop-off (Fri Nov 20 or Sat Nov 21; hard limit Tue Nov 24, 6 pm)
- Email Tedde Titus (ttitus@lbcc.edu) **this week** to set up drop-off **and** a pick-up appointment.
- **Do not take anything apart.** Submit the Drop-off text entry with your pick-up time.

### Phase 7 — Timed troubleshooting (after pick-up; due Mon Dec 7)
1. **Before** starting: re-study the ladder, have your wire list and meter ready, and block off 4 uninterrupted hours.
2. Starting the quiz starts a 245-minute clock. Set your own timer for just under 4 hours.
3. Keep a **fault log as you go** in the report's table format: *Error # / Description / Problem caused / How you found it / What you did to fix it*. Be **very** detailed (30 pts in the report).
4. **One fault is a transformer problem.** The report asks specifically how you found it with a meter (20 pts). Write down your exact meter steps when you find it.
5. Answer the 2 quiz questions, film an operation video of the repaired box (same tests), and upload it to "*Lab 3 – Timed Troubleshooting Video Upload*". That assignment is **not** in the module list, so look for it under Assignments.
6. Check In 4 photos (due Sun Dec 6).

### Phase 8 — Finish the report (due Sat Dec 12; aim for Thu Dec 10)
Needs your selloff results from the instructor. Ask for them if they haven't appeared by about Dec 8.

## 4. Photo checklists

**Check In 1 / 2 / 4** (same spec each time, PDF: title page with name, class and lab number + 3 cropped photos):
1. Front view of controls 2. Rear of control panel 3. Top-down view of wiring area.
Graded on: all 3 views (3), following the wiring instructions (3), components installed/wired correctly (3), progress since last week (1).

**Procedure Component Install & Wiring** (in this order):
1. Front panel: all buttons and lights in one shot
2. Rear of front panel, wiring and cable trays **open**
3. FWD/REV starter area: everything right of CB2, between the two horizontal trays, **covers off**
4. Transformer area: transformer to left of CB2, **transformer grounding clearly visible**
5. Overview: top-down, cable trays **installed**

## 5. Operation video: 10 tests and what should happen

Graded 8 pts each + 20 for wiring/neatness. The printed sheet has 8 tests, but the rubric grades 10. Film all 10.

| # | Test | Steps | Expected |
|---|---|---|---|
| 1 | FWD & STOP1 | FWD, STOP1 | FW pulls in + FWDON on and stays on; STOP1 drops it |
| 2 | REV & STOP2 | REV, STOP2 | RV pulls in + REVON on; STOP2 drops it |
| 3 | OLF | FWD, press OL test on OLF | FW drops, FWDON off. Reset OLF afterward |
| 4 | OLR | REV, press OL test on OLR | RV drops, REVON off. Reset OLR |
| 5 | FWD limit | FWD, RLS, FLS | RLS does nothing; FLS drops FW |
| 6 | REV limit | REV, FLS, RLS | FLS does nothing; RLS drops RV |
| 7 | FWD interlock | FWD, REV, STOP2 | REV does nothing while FW is on (FW 31-32 open); STOP2 stops |
| 8 | REV interlock | REV, FWD, STOP1 | FWD does nothing while RV is on; STOP1 stops |
| 9 | FWD & STOP2 | FWD, STOP2 | Runs, STOP2 drops it |
| 10 | REV & STOP1 | REV, STOP1 | Runs, STOP1 drops it |

## 6. Selloff self-inspection (100 pts, 10 each)

- [ ] **Neat wiring**, up to industry standard
- [ ] **No exposed copper** at any terminal (tug and look at every one)
- [ ] **No loose wires**: re-torque every screw. Loose wires found at inspection become *extra* faults in your troubleshooting.
- [ ] **Wire routes**: all front-panel control wires in the **right** cable tray, none in the left tray to the panel, **no solo neutrals** (hot and neutral run together)
- [ ] **3-phase wired** between CR socket and terminal blocks (all of it, not half)
- [ ] **Exactly 9 wires** through the door channel
- [ ] **Components in the proper location** per the layout picture
- [ ] **Cable trays**: wires routed properly, not overstuffed, no bypassing, not too tight
- [ ] **All cable tray covers on**
- [ ] **Proper colors**: 24 V hot red, 24 V neutral white, 120 V hot black, 120 V neutral white, 3-phase black, ground green, all 16 AWG stranded

Also from the general spec: wires in the top and out the bottom; max 2 wires per terminal; **1 wire per circuit-breaker terminal**; no wire nuts; nothing on unused terminals; the transformer primary feeds nothing else; end stops between components.

## 7. Report outline (275 pts), in the required order with required headers

| Section | Contents | Pts |
|---|---|---|
| Cover sheet | Standard | 5 |
| **WIRING SECTION** | Hand-written diagram (20); Constructor diagram (20); Summary ≥2 ¶ (10); Conclusion ≥2 ¶ (20) | 70 |
| **Testing Worksheets** | Scan/photo of the *original* paper sheet, expected vs actual | 20 |
| **TESTING SECTION** | Testing-process description + quiz printout; Items you fixed; Summary ≥2 ¶ (10); Conclusion ≥2 ¶ (20) | 30 |
| **TROUBLESHOOTING SECTION** | Errors Found Table (10 format + 20 content); Transformer problem Q&A (20); Summary ≥2 ¶ (10); Conclusion ≥2 ¶ (20) | 80 |
| **SELL-OFF SECTION** | Points lost and why, with your final score, even if no points were lost (20); **Project Conclusion**: substantial, well beyond 2 ¶, concrete learnings backed by examples (50) | 70 |

Summary = what you did. Conclusion = what you learned, with evidence. Label every item so the instructor never has to guess which one they're reading.

Write each section's draft **right after** that phase ends, while it's fresh.

## 8. Draft wire list (derived from LAB3-F20b; verify against your sheet)

Feed-through TBs: top and bottom screws are the same point. TB7–9 are bussed (24 V hot) and TB4–6 are bussed (X4N), as in Lab 2.

| Wire | Color | Connects | Crosses door? |
|---|---|---|---|
| H | black | Cord hot → CB1-1; CB1-2 → transformer H1 | |
| N | white | Cord neutral → TB1; TB1 → transformer (N1) | |
| G | green | Cord ground → TBG1; TBG1 → **X4 at the transformer** | |
| X1 | red | Transformer X1 → CB2-1 | |
| 24 | red | CB2-2 → TB7 | |
| X4 | white | Transformer X4 → TB4 | |
| 1 | red | TB7 → STOP1-1 | **yes** |
| 2 | red | STOP1-2 → STOP2-1 | door only |
| 3 | red | STOP2-2 → FWD-3 → REV-3 (door); → FW 7L4 → RV 7L4 (panel) | **yes** |
| 4 | red | FWD-4 → FLS-21 (door); → FW 14/22 | **yes** |
| 5 | red | FLS-22 → RV 31 | **yes** |
| 6 | red | RV 32 → FW A1 | |
| 7 | red* | FW A2 → OLF 95 | |
| 8 | white | OLF 96 + OLR 96 → TB5 | |
| 9 | red | REV-4 → RLS-21 (door); → RV 14/22 | **yes** |
| 10 | red | RLS-22 → FW 31 | **yes** |
| 11 | red | FW 32 → RV A1 | |
| 12 | red* | RV A2 → OLR 95 | |
| 13 | red | TB8 → FW 23 | |
| 14 | red | FW 24 → FWDON X1 | **yes** |
| 15 | white | FWDON X2 → REVON X2 (door); → TB6 | **yes** |
| 16 | red | TB9 → RV 23 | |
| 17 | red | RV 24 → REVON X1 | **yes** |

Door-crossing count: 1, 3, 4, 5, 9, 10, 14, 15, 17 = **9** ✓. This only works if you make the jumpers on the door (STOP1→STOP2, STOP2→FWD→REV, FWDON X2→REVON X2), so each signal crosses once.

\*Wires 7 and 12 sit upstream of the overload contact, so they're *not* grounded conductors. That's the same question as wire 4 in Lab 2. Use whatever color your instructor accepts for this.

**Power (all black):** 3PHIN socket L1 (pin 24), L2 (21), L3 (14) → FW 1L1/3L2/5L3 = L1/L2/L3 and RV 1L1/3L2/5L3 = **L3**/L2/**L1** (the L1–L3 swap reverses rotation). OLF and OLR 2T1/4T2/6T3 tie together → TB-T1/T2/T3. The contactor's 13 = 7L4 and 14 = 14/22, as noted on the ladder.

## 9. Clarification - ask the instructor

1. **Testing/Operation/Procedure are due Nov 30, but the box is dropped off by Nov 24.** Confirm they must be done before drop-off. I'm assuming they do.
2. **Pick-up is "Thursday or Friday"**, which is probably **Nov 26–27, Thanksgiving**. Confirm the actual pick-up days.
3. **Drop-off**: the page says "by Tuesday 6 pm" but only lists Fri/Sat windows. Is Tuesday an option?
4. **Check In 3 doesn't exist** in the module (1, 2, 4 only). Is that intentional?
5. **Timed Troubleshooting Video Upload** assignment is referenced but isn't in the module list.
6. **Operation video**: the page says 9 scenes, the printed sheet has 8 tests, and the rubric grades 10. Film all 10.
7. **Testing worksheet**: there's no worksheet file. Is a self-made paper sheet OK?
8. Two slightly different report specs exist (the "REPORT SPECIFICATIONS-2" page vs. the report assignment). **Follow the assignment page**, since it has the rubric.

## 10. Other deadlines in the same window

Test #2 (Start/Stop/Jog) and Ch. 8 HW **Mon Nov 16** (same day as Check In 1) · Ch. 7 HW Mon Nov 23 · Ch. 12 HW Sun Dec 6 · **Final Exam Mon Dec 14**.
