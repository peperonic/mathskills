# MathSkills Builder (prototype)

Served at https://mathskills.academy/builder/ (no login). The teacher is "Sensei" unless they type a name. They pick a curriculum board (IB, A-Level, GCSE, National Curriculum, Other) and describe it in their own words. Then come three columns: the classroom languages, typed in freely; the topics with their prior skills, suggested for known topics and editable; and under each skill, any number of YouTube links and handouts of any file type. Below is the diagnostic hexagon matrix (always seven cells, 2-3-2), and the class plan can be downloaded as JSON. The student file at /game/ does not read the plan yet.

- `index.html` is the page that is published. It is built from `builder-src.html` by `python3 builder/assemble.py game-land/index.html builder/builder-src.html builder/index.html`, which copies the fonts and the topic names from the student file.
- Everything stays in the teacher's browser: choices in localStorage, handout files in IndexedDB. Nothing is uploaded, and no YouTube thumbnails or other outside requests are loaded.
- Language names, writing direction and decimal signs come from the browser's Unicode CLDR data (Intl). For the seven languages of the student file, its own decimal signs are used.
- Fonts: the MathSkills pixel font and Vazirmatn (SIL Open Font License, `Vazirmatn-OFL.txt`).
