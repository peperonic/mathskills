# Connecting MathSkills Builder

The builder (`builder/builder-src.html` in the mathskills repository) already has the right shape: a table of topics, each listing the prior skills it suggests, by MathSkills skill id. `dist/builder-topics.json` uses the same shape, keyed by the course names the builder already offers for IB (for example `DP Physics SL`).

Smallest change, two steps:

1. Copy `dist/builder-topics.json` into the mathskills repository, for example as `builder/ib-topics.json`.
2. In `builder/assemble.py`, inline it into the page when the page is assembled (the builder makes no outside requests), and look topics up by course first:

```js
const COURSE_TOPICS = /* contents of builder/ib-topics.json, inlined by assemble.py */;
const topicsFor = () => COURSE_TOPICS[ST.course] || SUBJECT_TOPICS[ST.subject] || TOPICS;
```

Skills MathSkills knows appear as their id (`sci`, `prop`, `expo` ...), so their check questions show. The others appear by name (for example "Rearranging equations and formulas"); the builder already treats an unknown skill as the teacher's own. The entry `(whole course)` holds the course's default hexagon of seven.

`dist/ib-skills.json` has everything else (guide references, the prior-knowledge items in our wording, SL/HL, topic codes) for later features.

Courses the builder does not list yet: Biology and Environmental systems and societies.
