# MathSkills

**Open, multilingual maths learning: first find out what a learner already knows, then teach the rest.**

MathSkills is a browser game made by maths teachers. A learner walks across a black-and-white map, answers two short questions at each station, and then sees a *learning realm*: a hexagon for every topic, white if they already know it, black if it is still to learn. Every hexagon opens a short video, a step-by-step "underworld" lesson, a practice game and a re-check.

It works in seven languages, among them Arabic and Dari, and it needs no account, no installation and no internet connection once loaded. Learners' results stay on their own device.

> 🇩🇪 **Kurz auf Deutsch:** MathSkills ist ein offenes, mehrsprachiges Mathe-Lernspiel von Lehrkräften. Es findet zuerst heraus, was Lernende schon können, und vermittelt dann den Rest, ohne Konten, ohne Tracking, die Daten bleiben auf dem Gerät.

---

## Try it

1. Download the HTML file from this repository.
2. Open it in any modern browser (Firefox, Chrome, Safari, Edge), on a computer, tablet or phone.
3. Choose a language and start walking.

That's it: no server, no build step, no sign-up.

## What's inside

**Diagnostic land:** 7 stations, 2 questions each, aimed at the most common misconceptions:

| Station | Example |
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

العربية · دری · English · Deutsch · Français · Español · Русский

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
- 🌍 checks and corrections of the translations by native speakers
- 🧮 ideas for questions that reveal typical misconceptions
- 🐞 bug reports, with the device, browser and language you used

Contributions to the code are accepted under the project's AGPL licence.

## Team

- **Chiara Perrone:** product and education lead, maths teacher
- **Thomas Haferlach:** technical lead

## Licence

- **Code:** GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). See [`LICENSE`](LICENSE).
- **Videos, comics, songs and their characters, artwork and music:** © 2026 Chiara Perrone. All rights reserved. They are **not** covered by the AGPL and may not be copied, changed, redistributed or used in other projects without written permission. Learners and teachers may of course watch and use them within MathSkills.
