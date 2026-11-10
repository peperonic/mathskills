# syllabus-ib

A small database of the **prior skills** that IB Diploma Programme courses expect, made for **MathSkills Builder**: a teacher picks a course, sees the maths skills students need first, and builds the diagnostic hexagon of seven.

Courses, each at SL and HL:

| Course | Status | Prior skills from |
|---|---|---|
| Mathematics: analysis and approaches | ready | guide, "Prior learning topics" (SL items only) |
| Mathematics: applications and interpretation | assumed | the AA list until the AI guide is checked |
| Physics | ready | guide, Tool 3 "Applying general mathematics", owner's selection |
| Chemistry | ready | guide, Tool 3, same selection rules as Physics |
| Economics | ready | the calculations named in the syllabus |
| Biology | ready (partial list, no topics yet) | the guide's Tool 3 list as pasted by the owner; its last items were cut off |
| Environmental systems and societies | ready (no topics yet) | the mathematical requirements for all ESS students, as given by the owner |

## What is in it

```
data/skills.yaml          the skill catalogue: id, name, matching MathSkills skill
data/courses/*.yaml       one file per course: guide, prior knowledge, default hexagon, topics
build.py                  checks everything and writes dist/
dist/ib-skills.json       the whole database in one file
dist/ib-skills.js         the same as  window.IB_SKILLS = {...};
dist/builder-topics.json  course -> topic -> skills, in the builder's own table shape
docs/                     sources, connecting MathSkills Builder, uploading to Codeberg
```

To change something, edit a YAML file and run:

```bash
pip install pyyaml
python3 build.py
```

`build.py` refuses to write if a skill id is unknown, a hexagon does not have exactly 7 different skills, or a hexagon skill is not one of the course's prior skills. With `--guides DIR` (a folder holding the IB guide PDFs, never committed) it also checks that no 8-word run of an IB guide was copied into our texts.

## Rules

- **No IB text.** IB guides are copyright of the International Baccalaureate Organization. This database holds only structure (topic codes and titles as labels, SL/HL), our own short wording, and references to the guides. Keep the guide PDFs out of the repository.
- **Commercial use needs care.** The guides state that operators of curriculum mapping or teacher resource platforms need a written IB licence for commercial use of IB publications. The owner does not intend commercial use; if that changes, or before IB course data goes live on a public site, ask copyright@ibo.org. This is not legal advice.
- Every skill and prior-knowledge item says where it comes from (`origin: guide` or `origin: curator`).

See `docs/sources.md`, `docs/mathskills-builder.md` and `docs/upload-to-codeberg.md`.
