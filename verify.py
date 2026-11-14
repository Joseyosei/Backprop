#!/usr/bin/env python3
"""Integrity check for the Backprop data files. Exits non-zero on any problem."""
import json, re, sys, pathlib

root = pathlib.Path(__file__).parent
problems = []

d = json.load(open(root / "courses.json"))
u = json.load(open(root / "universities.json"))

FREE = ("free", "audit", "beta", "freecert")
ids = set()

for c in d["courses"]:
    tag = c.get("id", "?")
    if tag in ids:
        problems.append(f"{tag}: duplicate id")
    ids.add(tag)
    for field in ("name", "platform", "topic", "cost", "hours", "url", "why", "level", "tracks"):
        if not c.get(field) and c.get(field) is not False:
            problems.append(f"{tag}: missing {field}")
    if c["platform"] not in d["platforms"]:
        problems.append(f"{tag}: unknown platform {c['platform']}")
    if c["topic"] not in d["topics"]:
        problems.append(f"{tag}: unknown topic {c['topic']}")
    if c["cost"] not in d["costs"]:
        problems.append(f"{tag}: unknown cost {c['cost']}")
    if not re.match(r"^https://", c["url"]):
        problems.append(f"{tag}: url is not https: {c['url']}")
    if c["level"] not in ("beginner", "intermediate", "advanced"):
        problems.append(f"{tag}: bad level {c['level']}")
    if len(c["why"]) < 40:
        problems.append(f"{tag}: why is too short to be useful")

for k in d["topics"]:
    if not any(c["topic"] == k for c in d["courses"]):
        problems.append(f"topic {k} has no courses")
for k in d["platforms"]:
    if not any(c["platform"] == k for c in d["courses"]):
        problems.append(f"platform {k} has no courses")

for r in d["retired"]:
    for field in ("code", "name", "when", "instead"):
        if not r.get(field):
            problems.append(f"retired entry missing {field}")

for p in u["programmes"]:
    for field in ("inst", "short", "country", "city", "prog", "level", "url", "covers", "note"):
        if not p.get(field):
            problems.append(f"{p.get('short','?')} {p.get('prog','?')}: missing {field}")
    for k in p["covers"]:
        if k not in d["topics"]:
            problems.append(f"{p['short']}: covers unknown topic {k}")
    if not re.match(r"^https://", p["url"]):
        problems.append(f"{p['short']}: url is not https")

n = len(d["courses"])
nfree = sum(1 for c in d["courses"] if c["cost"] in FREE)
ncert = sum(1 for c in d["courses"] if c["cert"])
nplat = len(d["platforms"])
ntop = len(d["topics"])
nuni = len(u["programmes"])

html = (root / "index.html").read_text()
readme = (root / "README.md").read_text()
for label, text in (("index.html", html), ("README.md", readme)):
    for num, what in ((n, "course count"), (nfree, "free count"), (nplat, "provider count")):
        if str(num) not in text:
            problems.append(f"{label}: {what} {num} not found, counts may be stale")

print(f"courses {n} | free {nfree} | certs {ncert} | providers {nplat} | topics {ntop} | degrees {nuni}")
print(f"data updated {d.get('updated')} | universities updated {u.get('updated')}")
if problems:
    print(f"\n{len(problems)} PROBLEM(S):")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print("\nAll checks passed.")
