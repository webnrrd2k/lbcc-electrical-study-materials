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
| [ELECT 212 — Electrical Fundamentals (3rd semester)](elect_212_3rd_semester_electrical_fundamentals/) | AC theory: trig and vectors, AC waveforms, inductance, capacitance, R-L, R-C and R-L-C series and parallel circuits (Units 14–24) | 11 study guides, 637 flashcards, 2 practice-problem sets, formula cheat sheet |
| [ELECT 435A — Motor Control Wiring and Troubleshooting](elect_435a_motor_control_wiring%2Btrouble/) | Motor control labs: Lab 2 Start/Stop/Jog, Lab 3 Forward/Reverse (coming soon) | Wiring diagrams: what to physically hook up, plus troubleshooting notes |

More classes will be added as they're covered.

### Interactive tools

- **[RLC Circuit Dashboard](https://webnrrd2k.github.io/rlc-dashboard)** ([source](https://github.com/webnrrd2k/rlc-dashboard)) — adjust R, L, C, and frequency and see impedance, current, phase angle, and phasor diagrams update live. Runs in any browser, including on your phone.

- **[Lab 2 — Start/Stop/Jog - Wiring Diagrams](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_2_startstopjog/wiring-diagrams.html)**  — Clearly labeled and layed-out wiring diagram for Lab 2.

- **[Lab 3 —  Lab #3 Forward/Reverse Controls - Wiring Diagrams](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring+trouble/labs/lab_3_forwardreverse_controls)**  — Plan of attack and clear wiring diagram for Lab 3.
    + [Plan of Attack](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring+trouble/labs/lab_3_forwardreverse_controls/lab3-plan.md) the plan
    + [Tasks to complete](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring+trouble/labs/lab_3_forwardreverse_controls/lab3-tasks.org) is the task-by-task list in Emacs org-mode format, but It's a plain-text document, so should be usable as a checklist by anyone. Changing the extension to .txt and it should open correctly. It has 11 milestones (M0–M10), sub-milestones and checkboxes

---

## How this repository is organized

```
.
├── README.md                    (this page)
└── <class folder>/              (one per class, e.g. elect_212_...)
    ├── README.md                (that class's table of contents)
    ├── units/                   (lecture classes: one folder per unit, study guide + flashcards)
    ├── practice-problems/
    └── labs/                    (lab classes: one folder per lab, wiring diagrams + troubleshooting)
```

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
- **Not comfortable with GitHub?** Opening an issue only requires a free GitHub account — no git knowledge needed.

Please only contribute material you created yourself. Do not upload textbook pages, publisher materials, instructor slides, exams, or answer keys.

---

## Academic honesty

These materials are for **learning and review**. Use them to understand the concepts, not to get around graded work. Follow your instructor's rules on what's allowed for homework, quizzes, and exams.

---

## Disclaimer

This is an unofficial student resource. It is not a substitute for the course textbook, your instructor, the NEC, or proper safety training. Nothing here is professional engineering advice.
