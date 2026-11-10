"""Check the data and build the files MathSkills Builder reads.

    python3 build.py                     # check, then write dist/
    python3 build.py --check-only        # check, write nothing
    python3 build.py --guides DIR        # also check that no IB guide text was copied
                                         # (DIR holds the guide PDFs or .txt exports; never commit them)

Writes:
    dist/ib-skills.json     everything: skills and one entry per course and level
    dist/ib-skills.js       the same, as  window.IB_SKILLS = {...};  for a <script> tag or inlining
    dist/builder-topics.json  just what the builder's topic table needs:
                            {"DP Physics SL": {"A.1 Kinematics": ["sci", "Rearranging equations and formulas", ...]}}
                            Skills that MathSkills knows appear as its id (so their check questions show);
                            the others appear by name, which the builder treats as the teacher's own skill.

Needs Python 3.9+ and PyYAML (pip install pyyaml).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
LEVELS = ("SL", "HL")
STATUSES = {"ready", "assumed", "pending"}


def load():
    skills = yaml.safe_load((ROOT / "data" / "skills.yaml").read_text(encoding="utf-8"))["skills"]
    courses = {}
    for p in sorted((ROOT / "data" / "courses").glob("*.yaml")):
        courses[p.stem] = yaml.safe_load(p.read_text(encoding="utf-8"))
    return skills, courses


def check(skills, courses) -> list[str]:
    errs = []
    ids = [s["id"] for s in skills]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errs.append(f"skills.yaml: duplicate ids {sorted(dup)}")
    known = set(ids)
    for s in skills:
        if not s.get("name"):
            errs.append(f"skill {s['id']}: no name")
    for cid, c in courses.items():
        where = f"courses/{cid}.yaml"
        if c.get("status") not in STATUSES:
            errs.append(f"{where}: status must be one of {sorted(STATUSES)}")
        if set(c.get("courses", {})) != set(LEVELS):
            errs.append(f"{where}: courses must name SL and HL")
        if c.get("status") == "pending":
            continue
        pk_ids = [i["id"] for i in c.get("prior_knowledge", [])]
        if len(pk_ids) != len(set(pk_ids)):
            errs.append(f"{where}: duplicate prior_knowledge ids")
        for i in c.get("prior_knowledge", []):
            for s in i["skills"]:
                if s not in known:
                    errs.append(f"{where} {i['id']}: unknown skill {s}")
            for lv in i.get("levels", LEVELS):
                if lv not in LEVELS:
                    errs.append(f"{where} {i['id']}: unknown level {lv}")
            if i.get("origin") not in ("guide", "curator"):
                errs.append(f"{where} {i['id']}: origin must be guide or curator")
        for lv in LEVELS:
            offered = set(prior_skills(c, lv))
            hexa = c.get("hexagon", {}).get(lv, [])
            if len(hexa) != 7 or len(set(hexa)) != 7:
                errs.append(f"{where}: hexagon {lv} needs 7 different skills, has {hexa}")
            for s in hexa:
                if s not in offered:
                    errs.append(f"{where}: hexagon {lv} skill {s} is not among the course's {lv} prior skills")
        codes = [t["code"] for t in c.get("topics", [])]
        if len(codes) != len(set(codes)):
            errs.append(f"{where}: duplicate topic codes")
        for t in c.get("topics", []):
            for s in t.get("skills", []) + t.get("hl_skills", []):
                if s not in known:
                    errs.append(f"{where} topic {t['code']}: unknown skill {s}")
    return errs


def prior_skills(c, level) -> list[str]:
    out = []
    for i in c.get("prior_knowledge", []):
        if level in i.get("levels", LEVELS):
            for s in i["skills"]:
                if s not in out:
                    out.append(s)
    return out


def build(skills, courses) -> dict:
    by_id = {s["id"]: s for s in skills}
    out_courses = []
    for cid, c in courses.items():
        for lv in LEVELS:
            topics = []
            for t in c.get("topics", []):
                if lv not in t.get("levels", LEVELS):
                    continue
                sk = list(t.get("skills", [])) + ([s for s in t.get("hl_skills", []) if s not in t.get("skills", [])] if lv == "HL" else [])
                topics.append({"code": t["code"], "name": t["name"], "skills": sk})
            out_courses.append({
                "id": f"ib-dp-{cid}-{lv.lower()}",
                "board": "IB", "subject": c["subject"], "course": c["courses"][lv], "level": lv,
                "status": c["status"],
                "guide": c.get("guide", {}),
                "prior_knowledge": [{"id": i["id"], "text": i["text"], "skills": i["skills"], "origin": i["origin"]}
                                    for i in c.get("prior_knowledge", []) if lv in i.get("levels", LEVELS)],
                "prior_skills": prior_skills(c, lv),
                "hexagon": c.get("hexagon", {}).get(lv, []),
                "topics": topics,
            })
    return {
        "schema": "ib-skills/1",
        "generated": dt.date.today().isoformat(),
        "note": "Structure and our own wording only; no text from IB publications. IB topic codes and titles are used as labels.",
        "skills": {s["id"]: {"name": s["name"], "mathskills": s.get("mathskills"), **({"note": s["note"]} if s.get("note") else {})}
                   for s in skills},
        "courses": out_courses,
    }


def builder_topics(data: dict) -> dict:
    """The builder's own shape: course -> topic label -> skill ids (MathSkills ids or names)."""
    sk = data["skills"]
    show = lambda s: sk[s]["mathskills"] or sk[s]["name"]
    out = {}
    for c in data["courses"]:
        if c["status"] == "pending":
            continue
        out[c["course"]] = {f"{t['code']} {t['name']}": [show(s) for s in t["skills"]] for t in c["topics"]}
        out[c["course"]]["(whole course)"] = [show(s) for s in c["hexagon"]]
    return out


def guide_overlap(guides: Path, courses, skills, n: int = 8) -> list[str]:
    """Flag any run of n words in our own texts that also appears in a guide."""
    texts = []
    for p in sorted(guides.iterdir()):
        if p.suffix.lower() == ".txt":
            texts.append(p.read_text(encoding="utf-8", errors="replace"))
        elif p.suffix.lower() == ".pdf":
            try:
                import pymupdf
            except ImportError:
                sys.exit("--guides with PDFs needs PyMuPDF: pip install pymupdf")
            with pymupdf.open(p) as d:
                texts.append(" ".join(pg.get_text() for pg in d))
    norm = lambda s: re.findall(r"[a-zäöüß0-9]+", s.lower())
    grams = set()
    for t in texts:
        w = norm(t)
        grams.update(tuple(w[i:i + n]) for i in range(len(w) - n + 1))
    hits = []
    ours = [(f"skill {s['id']}", s["name"]) for s in skills]
    ours += [(f"{cid} {i['id']}", i["text"]) for cid, c in courses.items() for i in c.get("prior_knowledge", [])]
    for where, text in ours:
        w = norm(text)
        for i in range(len(w) - n + 1):
            if tuple(w[i:i + n]) in grams:
                hits.append(f"{where}: '{' '.join(w[i:i + n])}' appears in a guide; reword it")
                break
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--guides", type=Path)
    a = ap.parse_args()
    skills, courses = load()
    errs = check(skills, courses)
    if a.guides:
        errs += guide_overlap(a.guides, courses, skills)
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    data = build(skills, courses)
    ready = sum(c["status"] != "pending" for c in data["courses"])
    print(f"ok: {len(data['skills'])} skills, {len(data['courses'])} course levels ({ready} with data)")
    if a.check_only:
        return
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    js = json.dumps(data, ensure_ascii=False, indent=1)
    (dist / "ib-skills.json").write_text(js + "\n", encoding="utf-8")
    (dist / "ib-skills.js").write_text("window.IB_SKILLS = " + js + ";\n", encoding="utf-8")
    (dist / "builder-topics.json").write_text(json.dumps(builder_topics(data), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("wrote dist/ib-skills.json, dist/ib-skills.js, dist/builder-topics.json")


if __name__ == "__main__":
    main()
