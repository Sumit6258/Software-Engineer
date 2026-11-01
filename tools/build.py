#!/usr/bin/env python3
"""Regenerate every curriculum-derived page.

    python3 tools/build.py            # write generated files
    python3 tools/build.py --check    # exit 1 if any generated file is stale

Inputs:  curriculum/curriculum.json, curriculum/subject-meta.json, and the
         front matter of every lesson under docs/.
Outputs: see the generator modules (gen_inventory.py, gen_navigation.py).
"""
import argparse
import re
import sys

from curlib import ROOT, STATUSES, RANK, Repo, md_table, link
import gen_inventory as inv
import gen_navigation as nav


def prose_words(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"^---\n.*?\n---\n", " ", text, flags=re.S)
    return len(re.findall(r"[A-Za-z0-9’'-]+", text))


def stats_block(r):
    st = r.cur["stats"]
    c = r.counts()
    done = sum(c[s] for s in ("Drafted", "Reviewed", "Complete"))
    rows = [["Parts", st["parts"]], ["Numbered subject areas", st["subjects"]],
            ["Chapters (groups) in the syllabus", st["groups"]],
            ["Syllabus topics inside the 64 subjects", st["leaves"]],
            ["Lessons written", len(r.lessons)],
            ["Topics covered by a drafted-or-better lesson", "%d of %d (%.1f%%)" % (done, c["total"], 100.0 * done / c["total"])],
            ["Topics reviewed or complete", sum(c[s] for s in ("Reviewed", "Complete"))]]
    return md_table(["Measure", "Value"], rows)


def progress_block(r):
    c = r.counts()
    L = [md_table(["Status", "Topics"], [[s, c[s]] for s in STATUSES] + [["Total", c["total"]]]), "",
         "### Lessons written", ""]
    rows = []
    for ls in r.lessons:
        txt = ls["_path"].read_text("utf8")
        rows.append([link(ls["title"], ROOT / "PROGRESS.md", ls["_path"]), "S%02d / ch%d" % (ls["subject"], ls["chapter"]),
                     ls["status"], ls["reviewed"], prose_words(txt)])
    L += [md_table(["Lesson", "Where", "Status", "Last reviewed", "Prose words"], rows) if rows else "_None yet._", "",
          "### Subjects with at least one lesson", ""]
    started = [(n, r.subject_status(n)) for n in sorted(r.subjects) if r.subject_status(n) != "Not started"]
    L += [md_table(["Subject", "Status"], [[nav.sub_link(r, n, ROOT / "PROGRESS.md"), s] for n, s in started]) if started else "_None yet._"]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="do not write; fail if generated files are stale")
    a = ap.parse_args()
    r = Repo()
    out = {}
    for fn in (inv.complete_curriculum, inv.curriculum_index, inv.coverage_matrix, inv.extraction_report,
               inv.technology_index, nav.subject_pages, nav.part_pages, nav.tech_pages, nav.master_index,
               nav.prerequisite_map, nav.knowledge_graph, nav.learning_paths, nav.practical_projects, nav.inject_lessons,
               nav.inject_chapter_indexes):
        out.update(fn(r))
    for name, fn, rel in (("STATS", stats_block, "README.md"), ("AUTO", progress_block, "PROGRESS.md")):
        p = ROOT / rel
        if p.exists():
            out[p] = nav.update_block(p, name, fn(r))
        else:
            r.problems.append("%s not found; auto block %s skipped" % (rel, name))
    changed = []
    for path, text in out.items():
        text = text if text.endswith("\n") else text + "\n"
        old = path.read_text("utf8") if path.exists() else None
        if old != text:
            changed.append(path)
            if not a.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, "utf8")
    for pr in r.problems:
        print("PROBLEM:", pr)
    verb = "stale" if a.check else "written"
    print("%d generated files; %d %s." % (len(out), len(changed), verb))
    if a.check and changed:
        for p in changed[:20]:
            print("  stale:", p.relative_to(ROOT))
        sys.exit(1)
    if r.problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
