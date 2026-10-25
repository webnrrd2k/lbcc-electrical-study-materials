# LBCC Electrical Technology — Student Study Materials

Study guides, flashcards, practice problems, and interactive tools for students in the **Electrical Technology Program at Long Beach City College (LBCC)**.

This is an unofficial, student-made collection. It is not affiliated with or endorsed by LBCC or its faculty.

---

## Why this exists

Some of the core AC theory material is hard to follow from the lecture slides alone. These materials were put together to make the concepts clearer, organize them unit by unit, and give you more ways to practice: plain-language study guides, flashcards for memorizing formulas and terms, worked practice problems, and an interactive dashboard where you can change circuit values and watch what happens.

If you're stuck on a unit, start with the study guide, drill the flashcards, then try the practice problems.

---

## Quick start

1. Find your unit in the table below.
2. Open the **study guide** — it renders right here on GitHub, no download needed.
3. Open the **flashcards** and quiz yourself: each card shows a question, and clicking it reveals the answer.
4. Keep the **[formula cheat sheet](formula_cheat_sheet.pdf)** handy for homework and review.
5. Use the **[RLC Circuit Dashboard](https://webnrrd2k.github.io/rlc-dashboard)** to see how resistance, inductance, and capacitance affect impedance, current, and phase angle.

---

## Materials by unit

Unit numbers follow the course textbook.

| Unit | Topic | Study Guide | Flashcards |
|------|-------|-------------|------------|
| 14 | Basic Trigonometry and Vectors | [Guide](units/unit-14-trig-and-vectors/study-guide.md) | [63 cards](units/unit-14-trig-and-vectors/flashcards/) |
| 15 | Alternating Current | [Guide](units/unit-15-alternating-current/study-guide.md) | [75 cards](units/unit-15-alternating-current/flashcards/) |
| 16 | Inductance in AC Circuits | [Guide](units/unit-16-inductance-in-ac/study-guide.md) | [62 cards](units/unit-16-inductance-in-ac/flashcards/) |
| 17 | Resistive-Inductive (RL) Series Circuits | [Guide](units/unit-17-rl-series/study-guide.md) | [59 cards](units/unit-17-rl-series/flashcards/) |
| 18 | Resistive-Inductive (RL) Parallel Circuits | [Guide](units/unit-18-rl-parallel/study-guide.md) | [54 cards](units/unit-18-rl-parallel/flashcards/) |
| 19 | Capacitors | [Guide](units/unit-19-capacitors/study-guide.md) | [87 cards](units/unit-19-capacitors/flashcards/) |
| 20 | Capacitance in AC Circuits | [Guide](units/unit-20-capacitance-in-ac/study-guide.md) | [56 cards](units/unit-20-capacitance-in-ac/flashcards/) |
| 21 | Resistive-Capacitive (RC) Series Circuits | [Guide](units/unit-21-rc-series/study-guide.md) | [42 cards](units/unit-21-rc-series/flashcards/) |
| 22 | Resistive-Capacitive (RC) Parallel Circuits | [Guide](units/unit-22-rc-parallel/study-guide.md) | [44 cards](units/unit-22-rc-parallel/flashcards/) |
| 23 | RLC Series Circuits | [Guide](units/unit-23-rlc-series/study-guide.md) | [46 cards](units/unit-23-rlc-series/flashcards/) |
| 24 | RLC Parallel Circuits | [Guide](units/unit-24-rlc-parallel/study-guide.md) | [49 cards](units/unit-24-rlc-parallel/flashcards/) |

Each flashcard folder also holds the raw card data (`unitNN_flashcards.json`) and the diagrams, if you'd rather import the cards into a flashcard app.

### Formula cheat sheet

- [Formula Cheat Sheet (PDF)](formula_cheat_sheet.pdf) — the key AC formulas from these units on one page.

### Practice problems (multi-unit)

- [Polar & Rectangular Form](practice-problems/polar-and-rectangular-form.md) — converting between forms and doing vector math with complex numbers. Pairs with Unit 14 and everything after it.
- [Series RL, RC & RLC Circuits](practice-problems/series-rl-rc-rlc.md) — worked problems covering Units 17, 21, and 23.

### Interactive tools

- **[RLC Circuit Dashboard](https://webnrrd2k.github.io/rlc-dashboard)** ([source](https://github.com/webnrrd2k/rlc-dashboard)) — adjust R, L, C, and frequency and see impedance, current, phase angle, and phasor diagrams update live. Runs in any browser, including on your phone.

---

## Repository layout

```
.
├── README.md
├── formula_cheat_sheet.pdf
├── units/
│   ├── unit-14-trig-and-vectors/
│   │   ├── study-guide.md
│   │   └── flashcards/
│   │       ├── README.md                 (the clickable cards)
│   │       ├── unit14_flashcards.json    (raw card data)
│   │       └── *.png                     (card diagrams)
│   └── ... (one folder per unit, same pattern)
└── practice-problems/
    ├── polar-and-rectangular-form.md
    └── series-rl-rc-rlc.md
```

Everything for a unit lives in one folder, so if you only need one unit, that's the only place you have to look.

---

## How these were made

Most of the material here was drafted with AI tools (Claude and Google Gemini), then organized and reviewed by a student in the program. That makes it fast to produce, but **it can contain mistakes.** Always check formulas and answers against your textbook and your instructor, especially before an exam.

If you find an error, please report it (see below) so everyone benefits.

---

## Contributing

Corrections and additions from other LBCC students are welcome.

- **Found a mistake?** Open an [issue](../../issues) and say which unit and file, what's wrong, and what it should be.
- **Have your own notes, practice problems, or tools?** Open a pull request, or open an issue and attach the file.
- **Not comfortable with GitHub?** Opening an issue only requires a free GitHub account — no git knowledge needed.

Please only contribute material you created yourself. Do not upload textbook pages, publisher materials, instructor slides, exams, or answer keys.

---

## Academic honesty

These materials are for **learning and review**. Use them to understand the concepts, not to get around graded work. Follow your instructor's rules on what's allowed for homework, quizzes, and exams.

---

## Disclaimer

This is an unofficial student resource. It is not a substitute for the course textbook, your instructor, the NEC, or proper safety training. Nothing here is professional engineering advice.
