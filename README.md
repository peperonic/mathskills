# MathSkills Builder (prototype)

Served at https://mathskills.academy/builder/ (no login). A teacher picks the class, its languages and up to seven skills for the diagnostic hexagon matrix, then exports a class plan as JSON. The student file at /game/ does not read the plan yet.

- `index.html` is the page that is published. It is built from `builder-src.html` by `python3 builder/assemble.py game-land/index.html builder/builder-src.html builder/index.html`, which copies the fonts and the seven-language topic names from the student file, so both stay the same.
- Everything runs in the browser; the teacher's choices are kept in localStorage. Dropped files are listed by name only; nothing is uploaded.
- Fonts: the MathSkills pixel font and Vazirmatn (SIL Open Font License, `Vazirmatn-OFL.txt`).
