#!/usr/bin/env python3
"""Shared helpers for the curriculum tools (build.py, validate.py).

Requires Python 3.10+ and PyYAML.
"""
import json
import os
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STATUSES = ["Not started", "In progress", "Drafted", "Reviewed", "Complete"]
RANK = {s: i for i, s in enumerate(STATUSES)}
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
# `covers` may be empty only for a lesson that introduces an addition (`adds`); see validate.py
REQUIRED_LESSON_KEYS = ["title", "subject", "chapter", "order", "difficulty",
                        "time_minutes", "status", "reviewed", "summary"]


def rel_link(from_file, to_path):
    """Relative POSIX path from a file's directory to another path."""
    return os.path.relpath(str(to_path), start=str(Path(from_file).parent)).replace(os.sep, "/")


def link(text, from_file, to_path, anchor=None):
    href = rel_link(from_file, to_path)
    if anchor:
        href += "#" + anchor
    return "[%s](%s)" % (text, href)


def read_front_matter(path):
    """Return (front_matter_dict | None, body_text)."""
    text = Path(path).read_text("utf8")
    m = FM_RE.match(text)
    if not m:
        return None, text
    fm = yaml.safe_load(m.group(1)) or {}
    for k, v in list(fm.items()):
        if hasattr(v, "isoformat"):
            fm[k] = v.isoformat()
    return fm, text[m.end():]


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(" --- " for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)


def expand_covers(entries):
    out = []
    for e in entries or []:
        e = str(e).strip()
        if "-" in e:
            a, b = e.split("-")
            sa, ga, na = a.split(".")
            sb, gb, nb = b.split(".")
            if (sa, ga) != (sb, gb):
                raise ValueError("covers range crosses chapters: " + e)
            out += ["%s.%s.%02d" % (sa, ga, i) for i in range(int(na), int(nb) + 1)]
        else:
            out.append(e)
    return out


def leaf_label(leaf):
    """Human-readable label for a leaf, preserving source detail."""
    k, t = leaf["kind"], leaf["text"]
    if k == "card":
        return "**%s** — %s" % (t, leaf["detail"]) if leaf.get("detail") else "**%s**" % t
    if k == "row":
        return "%s — %s" % (t, leaf["detail"])
    if k == "framework":
        return "%s *(%s)*" % (t, leaf["language"])
    if k == "service":
        return "%s *(service of %s)*" % (t, leaf["parent"])
    if k == "stage":
        return "Stage %d: %s *(target: %s)*" % (leaf["stage"], t, leaf["detail"])
    if k == "role":
        return "%s — %s" % (t, leaf["detail"])
    return t


class Repo:
    def __init__(self):
        self.cur = json.loads((ROOT / "curriculum/curriculum.json").read_text("utf8"))
        self.meta = json.loads((ROOT / "curriculum/subject-meta.json").read_text("utf8"))
        self.parts = {p["number"]: p for p in self.cur["parts"]}
        self.subjects, self.subj_part = {}, {}
        for p in self.cur["parts"]:
            for s in p["subjects"]:
                self.subjects[s["number"]] = s
                self.subj_part[s["number"]] = p["number"]
        self.leaf_index = {}  # id -> (part, subject|None, group, leaf)
        for p in self.cur["parts"]:
            for s in p["subjects"]:
                for g in s["groups"]:
                    for l in g["leaves"]:
                        self.leaf_index[l["id"]] = (p, s, g, l)
            for g in p.get("groups", []):
                for l in g["leaves"]:
                    self.leaf_index[l["id"]] = (p, None, g, l)
        self.scan_docs()

    # ---- paths -----------------------------------------------------------
    def part_dir(self, n):
        return ROOT / "docs" / self.meta["parts"][str(n)]["dir"]

    def part_index(self, n):
        return self.part_dir(n) / "index.md"

    def subj_dir(self, n):
        return self.part_dir(self.subj_part[n]) / ("%02d-%s" % (n, self.meta["subjects"][str(n)]["slug"]))

    def subj_index(self, n):
        return self.subj_dir(n) / "index.md"

    def chapter_dir(self, n, g):
        return self.subj_dir(n) / ("%02d-%s" % (g["number"], g["slug"]))

    def chapter_index(self, n, g):
        return self.chapter_dir(n, g) / "index.md"

    # ---- docs scan ---------------------------------------------------------
    def scan_docs(self):
        self.lessons, self.chapter_files = [], {}
        self.problems = []
        for path in sorted((ROOT / "docs").rglob("*.md")):
            fm, _ = read_front_matter(path)
            if fm is None:
                if path.name != "index.md":
                    self.problems.append("%s: missing front matter" % path.relative_to(ROOT))
                continue
            t = fm.get("type", "lesson")
            if t == "lesson":
                fm["_path"] = path
                try:
                    fm["_covers"] = expand_covers(fm.get("covers"))
                except ValueError as e:
                    self.problems.append("%s: %s" % (path.relative_to(ROOT), e))
                    fm["_covers"] = []
                self.lessons.append(fm)
            elif t == "chapter-index":
                self.chapter_files[path.parent] = fm
        self.lessons.sort(key=lambda f: (f.get("subject", 0), f.get("chapter", 0), f.get("order", 0)))
        self.leaf_cover = defaultdict(list)
        for ls in self.lessons:
            for lid in ls["_covers"]:
                self.leaf_cover[lid].append(ls)
        self.additions = [(ls, a) for ls in self.lessons for a in (ls.get("adds") or [])]

    # ---- status ------------------------------------------------------------
    def leaf_status(self, lid):
        covering = self.leaf_cover.get(lid, [])
        if lid.startswith("P"):  # Parts XIII-XV are covered by generated pages
            return "Drafted"
        if not covering:
            return "Not started"
        return max((c["status"] for c in covering), key=lambda s: RANK[s])

    def group_status(self, n, g):
        sts = [self.leaf_status(l["id"]) for l in g["leaves"]]
        return self.rollup(sts)

    def subject_status(self, n):
        sts = [self.leaf_status(l["id"]) for g in self.subjects[n]["groups"] for l in g["leaves"]]
        return self.rollup(sts)

    def part_status(self, pn):
        if pn >= 13:
            return "Drafted"
        return self.rollup([self.subject_status(s["number"]) for s in self.parts[pn]["subjects"]])

    @staticmethod
    def rollup(sts):
        if not sts or all(s == "Not started" for s in sts):
            return "Not started"
        low = min(sts, key=lambda s: RANK[s])
        return "In progress" if low in ("Not started", "In progress") else low

    def lessons_in(self, n, chapter_no):
        return [l for l in self.lessons if l["subject"] == n and l["chapter"] == chapter_no]

    def chapter_exists(self, n, g):
        return self.chapter_index(n, g).exists()

    def counts(self):
        c = defaultdict(int)
        for lid in self.leaf_index:
            if lid.startswith("P"):
                continue
            c[self.leaf_status(lid)] += 1
            c["total"] += 1
        return c
