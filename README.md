# MathSkills

Tailored maths skills: a learner is tested on a handful of simple maths skills. They get a chance to demonstrate what they already know, and quickly move on to learn what they need to know better or learn from scratch. All of this happens in a learner’s chosen language, within a gamified environment called ‘Mathskills Game’.

The environment itself can be put together by any teacher via a ‘Mathskills Builder’. Within the builder, a teacher can select their subject (Biology, Chemistry, Economics, Maths or Physics for now), their curriculum, their students’ languages and the topics they need students to master in order to teach that topic well.

On the grounds of the curriculum and the topics specified by the teacher, seven skills for the students to focus on are suggested that the teacher can upload resources for (videos, websites and/or handouts). The teacher can also override and add the skills that, according to their experience, are required for a student to do well on a topic.

Based on the teacher’s input, an html file is generated that any teacher or student can download and run locally, so that no data on the students is saved elsewhere. The file runs a game in two realms. In the Discovery Realm, the learner walks across a black-and-white map and answers two short questions at each station, discovering what they already know. Based on their results, a Learning Realm is generated: a hexagon for every topic, white if they already know it, black if it is still to learn. Every hexagon opens a short video, a step-by-step “underworld” lesson, a practice game and a re-check.

No account, installation or internet connection are needed, and results stay on the students’ own device unless they decide to share them with their teacher via a QR code. Mathskills works in multiple languages, among them Arabic and Dari, so that learners with interrupted education, in particular refugees, do not feel left out. A toggle at the top allows learners to switch between languages when they want to.

---

## Try it

1. Download the HTML file from this repository.
2. Open it in any modern browser (Firefox, Chrome, Safari, Edge), on a computer, tablet or phone.
3. Choose a language and start walking.

That's it: no server, no build step, no sign-up.

## What's inside

**Diagnostic land:** 7 stations, 2 questions each, aimed at the most common misconceptions:

| Station | Example Question (misconceptions in brackets) |
|---|---|
| Rounding to decimal places | 3.4449 → 3.44 (not 3.45: never round twice) |
| × and ÷ by powers of ten | 7 cm = 0.07 m, by "hopping" the decimal point |
| Powers of ten | 1 = 10⁰ |
| Scientific notation | 45 600 = 4.56 × 10⁴ |
| Coordinates | plot points that form a right angle at the origin |
| Pythagoras' theorem | substitute into a² + b² = c²; which length is possible? (no calculator) |
| Straight line graphs | match a graph to y = mx + c |

**Learning realm:** one hexagon per topic, each with:

1. **Watch:** a short video; learners choose the language.
2. **Underworld:** a step-by-step lesson, one action at a time, with two worked examples.
3. **Play:** a practice game.
4. **Check again:** two new questions; both right turns the hexagon white.

## Languages

Arabic (العربية) · Dari (دری) · English · German (Deutsch) · French (Français) · Spanish (Español) · Russian (Русский)

MathSkills doesn't just translate words. It also shows maths the way each language writes it: decimal comma, point or ٫, right-to-left text with maths kept left-to-right, and each country's notation (for example y = mx + b, y = kx + b).

*All texts except English are drafts and need review by native-speaking maths teachers. Corrections are very welcome.*

## Privacy

- No accounts, no advertising, no tracking, no cookies.
- Progress is stored only in the learner's own browser.
- No data is sent to any server.

## Roadmap

- A reusable diagnostic component that teachers can fill with their own questions and languages
- A language layer for maths that adds new languages without changing the code
- Teacher activities via H5P (e.g. made with the free editor Lumi)
- Packaging for learning platforms such as Moodle (SCORM / H5P)

## Contributing

This repository on **Codeberg** is the main home of the project. A copy is mirrored automatically to GitHub; please open issues and contributions here on Codeberg.

Especially welcome:
- checks and corrections of the translations by native speakers
- ideas for questions that reveal typical misconceptions
- bug reports, with the device, browser and language you used

Contributions to the code are accepted under the project's AGPL licence.

## Team, in alphabetical order of first names

- **Chiara Perrone:** product and education lead, maths teacher 
- **Gianfranco Dbeis:** game design lead https://giandbeis.com/ 
- **Thomas Haferlach:** technical lead https://github.com/voodoohop/json-resume-thomash/blob/master/Thomas-Haferlach-CV-2026-09-28.pdf 

## Licence

- **Code:** GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). See [`LICENSE`](LICENSE).
- **Videos, comics, songs and their characters, artwork and music:** © 2026 Chiara Perrone. All rights reserved. They are **not** covered by the AGPL and may not be copied, changed, redistributed or used in other projects without written permission. Learners and teachers may of course watch and use them within MathSkills.

## Folders

| Folder | What it is |
|---|---|
| `index.html` | Start page: links to the game and the builder |
| `game/` | The Mathskills Game, one HTML file |
| `merge/` | Merge and Clear, a timed practice game in one HTML file: drop one disc on another to clear the board (common divisors, fractions that make a whole, equal fractions/decimals/percentages, like terms). English, German, Italian |
| `builder/` | The Mathskills Builder for teachers, one HTML file (built from `builder-src.html`, see `builder/README.md`) |
| `builder/syllabus-ib/` | Prior skills for IB Diploma courses (Mathematics AA and AI, Physics, Chemistry, Biology, ESS, Economics; SL and HL), in a form the builder reads |
| `builder/syllabus-de/` | German school curricula knowledge base (Baden-Württemberg Mathematik so far) with a read-only MCP server |

`builder/syllabus-ib` holds no text from IB publications: only structure, our own wording and references to the guides.
