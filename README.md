# LBCC Electrical Technology — Student Study Materials

Study guides, flashcards, practice problems, and interactive tools for students in the **Electrical Technology Program at Long Beach City College (LBCC)**.

This is an unofficial, student-made collection. It is not affiliated with or endorsed by LBCC or its faculty.

---

## Why this exists

Some of the core material in the program is hard to follow from the lecture slides alone. These materials were put together to make the concepts clearer, organize them unit by unit, and give you more ways to practice: plain-language study guides, flashcards for memorizing formulas and terms, worked practice problems, and interactive tools where you can change values and watch what happens.

---

## Classes

Pick your class to see its materials.

| Class | Topics | What's there |
|-------|--------|--------------|
| [ELECT 212 — Electrical Fundamentals (3rd semester)](elect_212_3rd_semester_electrical_fundamentals/) | AC theory: trig and vectors, AC waveforms, inductance, capacitance, R-L, R-C and R-L-C series and parallel circuits, single-phase transformers (Units 14–24 and 27); split-phase, wye and delta systems (Labs 4–6) | 13 study guides, 891 flashcards, 2 practice-problem sets, formula cheat sheet |
| [ELECT 245 — Electrical Code: Commercial](elect_245_electrical_code_commercial/) | The NEC for commercial buildings (2023 NEC): panelboards and working space (Ch. 12), services and grounding (Ch. 13) | Chapter 12 study guide, 200 flashcards with original diagrams |
| [ELECT 275 — Electrical Pipe Bending](elect_275_electrical_pipe_bending/) | Hand bending EMT and rigid (RMC) conduit: 90° stub-ups, back-to-back 90s, offsets, 3- and 4-point saddles, box offsets | [Conduit bending cheat sheet](elect_275_electrical_pipe_bending/conduit_bending_cheat_sheet.pdf): formulas, bender shoe marks, constants, practice bends, NEC rules; [study guide](elect_275_electrical_pipe_bending/lbcc_conduit_bending_guide.md) with each practice bend worked out; 44 flashcards |
| [ELECT 280 — Traffic Signal Systems 1](elect_280_traffic_signal_systems_1/) | Caltrans signal plans and Standard Plans legend, phasing and the ring diagram, the Model 332 cabinet, loop detectors, the 210 conflict monitor, conduit and conductor schedules, power, lighting and grounding | [Cheat sheet](elect_280_traffic_signal_systems_1/elect_280_cheat_sheet.pdf), [syllabus study guide](elect_280_traffic_signal_systems_1/elect_280_study_guide.pdf), 229 flashcards (course concepts and Caltrans plan symbols) |
| [ELECT 435A — Motor Control Wiring and Troubleshooting](elect_435a_motor_control_wiring%2Btrouble/) | Motor control labs: Lab 2 Start/Stop/Jog, Lab 3 Forward/Reverse | Wiring diagrams: what to physically hook up, plus troubleshooting notes; 53 motor control flashcards |

More classes will be added as they're covered.

### Tools

- **[Flashcard study page](https://webnrrd2k.github.io/lbcc-electrical-study-materials/flashcards/)** — every flashcard deck in one place (1,417 cards). Pick a class and deck, shuffle, flip, and mark the cards you know; your progress is saved in your browser. Works on a phone.

- **[RLC Circuit Dashboard](https://webnrrd2k.github.io/rlc-dashboard)** ([source](https://github.com/webnrrd2k/rlc-dashboard)) — adjust R, L, C, and frequency and see impedance, current, phase angle, and phasor diagrams update live. Runs in any browser, including on your phone.

- **[Lab 2 — Start/Stop/Jog - Wiring Diagrams](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_2_startstopjog/wiring-diagrams.html)**  — Clearly labeled and laid-out wiring diagram for Lab 2.

- **[Lab 3 — Forward/Reverse Controls - Wiring Diagrams](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/wiring_diagrams/wiring-diagrams.html)** — Clearly labeled wiring diagram, wire list, and a build order with quick meter checks after each stage for Lab 3.
    + Wire Labels [HTML](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/wiring_diagrams/wire-labels.html) [CSV](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/wiring_diagrams/wire-labels.csv)
    + Tasks to complete: [Emacs org-mode](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/lab3-tasks.org) or [plain text](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/lab3-tasks.txt). The task-by-task checklist for the whole lab: 11 milestones (M0–M10), sub-milestones and checkboxes, following the build order. Both files have the same content; the .txt opens in any text editor.

---

## How this repository is organized

```
.
├── README.md                    (this page)
└── <class folder>/              (one per class, e.g. elect_212_...)
│   ├── README.md                (that class's table of contents)
│   ├── units/ or chapter_NN/    (lecture classes: one folder per unit or chapter, study guide + flashcards)
│   ├── practice-problems/
│   └── labs/                    (lab classes: one folder per lab, wiring diagrams + troubleshooting)
├── flashcards/                  (the flashcard study page and its deck index)
└── tools/flashcards/            (deck format and the script that builds every deck)
```

Every flashcard deck is one JSON file in its own `flashcards/` folder. Next to it are files generated from that JSON: a `README.md` with clickable cards, an Anki package (`.apkg`), a Quizlet import file (`_quizlet.txt`) and an Emacs org-drill file (`.org`).

Everything here can be read on GitHub or on the website version at **https://webnrrd2k.github.io/lbcc-electrical-study-materials/**. Interactive pages and diagrams (`.html` files) only display properly on the website version, so links to them always go there.

Each class has its own page listing everything for that class, unit by unit.

---

## How these were made

Most of the material here was drafted with AI tools (Claude and Google Gemini), then organized and reviewed by a student in the program. That makes it fast to produce, but **it can contain mistakes.** Always check formulas and answers against your textbook and your instructor, especially before an exam.

If you find an error, please report it (see below) so everyone benefits.

---

## Contributing

Corrections and additions from other LBCC students are welcome.

- **Found a mistake?** Open an [issue](https://github.com/webnrrd2k/lbcc-electrical-study-materials/issues) and say which class, unit and file, what's wrong, and what it should be.
- **Have your own notes, practice problems, or tools?** Open a pull request, or open an issue and attach the file.
- **Fixing or adding flashcards?** Edit the deck's `.json` file (the format is in `tools/flashcards/deck.schema.json`), then run `python3 tools/flashcards/build_decks.py` to regenerate the card pages and downloads. Never reuse or renumber a card id; Anki uses it to keep everyone's review history.
- **Not comfortable with GitHub?** Opening an issue only requires a free GitHub account — no git knowledge needed.

Please only contribute material you created yourself. Do not upload textbook pages, publisher materials, instructor slides, exams, or answer keys.

---

## Academic honesty

These materials are for **learning and review**. Use them to understand the concepts, not to get around graded work. Follow your instructor's rules on what's allowed for homework, quizzes, and exams.

---

## Disclaimer

This is an unofficial student resource. It is not a substitute for the course textbook, your instructor, the NEC, or proper safety training. Nothing here is professional engineering advice.
