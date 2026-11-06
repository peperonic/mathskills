import re, sys, json, pathlib
game, src, out = map(pathlib.Path, sys.argv[1:4])
g = game.read_text()
fonts = "\n".join(l for l in g.splitlines() if l.lstrip().startswith("@font-face"))
names = {}
pos = [m.start() for m in re.finditer(r"\bt_round: ", g)]
assert len(pos) == 7, len(pos)
for lang, p0 in zip(["en", "de", "fr", "es", "ru", "ar", "fa"], pos):
    block = g[p0:p0 + 4000]
    d = {}
    for k, t, v in re.findall(r'\b([tsh])_(round|ten|pow|sci|coord|pyth|line): "([^"]*)"', block):
        d.setdefault(f"{k}_{t}", v)
    assert len(d) == 21, (lang, len(d))
    names[lang] = d
s = src.read_text().replace("/*@FONTS@*/", fonts).replace("/*@NAMES@*/", "const NAMES = " + json.dumps(names, ensure_ascii=False) + ";")
out.write_text(s); print("ok", len(s), fonts.count("@font-face"))
