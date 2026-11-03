#!/usr/bin/env python3
"""Validate the repository.

    python3 tools/validate.py                 # run every check
    python3 tools/validate.py --only links,code

Checks: source, coverage, frontmatter, markdown, links, mermaid, code, fresh.
Exit status 1 if any check fails. Requires Python 3.10+, PyYAML, gcc (for C
samples) and, for Mermaid, the @mermaid-js/mermaid-cli `mmdc` binary plus a
Chromium (set PUPPETEER_EXECUTABLE_PATH or use a standard install path).
"""
import argparse
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from curlib import ROOT, RANK, STATUSES, REQUIRED_LESSON_KEYS, Repo, read_front_matter
from gen_inventory import gh_slug

FAILS = []


def fail(check, msg):
    FAILS.append((check, msg))
    print("  FAIL [%s] %s" % (check, msg))


def md_files():
    skip = {"curriculum/source"}
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if any(rel.startswith(s) for s in skip) or "/.cache/" in rel or rel.startswith(".cache/"):
            continue
        yield p


FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def split_fences(text):
    """Yield (kind, lang, body, start_line) for 'code' fences and ('text', ...) for the rest."""
    lines = text.split("\n")
    i, buf, start = 0, [], 1
    out = []
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if m:
            if buf:
                out.append(("text", "", "\n".join(buf), start))
                buf = []
            fence, info = m.group(1), m.group(2).strip()
            j = i + 1
            body = []
            while j < len(lines) and not re.match(r"^ {0,3}%s\s*$" % re.escape(fence[0] * len(fence)), lines[j]):
                body.append(lines[j])
                j += 1
            closed = j < len(lines)
            out.append(("code", info.split()[0] if info else "", "\n".join(body), i + 1, closed))
            i = j + 1
            start = i + 1
        else:
            buf.append(lines[i])
            i += 1
    if buf:
        out.append(("text", "", "\n".join(buf), start))
    return out


# --------------------------------------------------------------------------
def check_source(r):
    print("[source] re-counting the .docx independently of the parser")
    docx = ROOT / "curriculum/source" / r.cur["source"]["file"]
    raw = docx.read_bytes()
    if hashlib.sha256(raw).hexdigest() != r.cur["source"]["sha256"]:
        fail("source", "curriculum.json was parsed from a different .docx (sha256 mismatch); re-run parse_syllabus.py")
    x = zipfile.ZipFile(docx).read("word/document.xml").decode("utf8")
    paras = re.findall(r"<w:p[ >].*?</w:p>", x, flags=re.S)
    parts = subjects = bullets = 0
    nums = []
    for p in paras:
        text = "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", p)).strip()
        ol = re.search(r'<w:outlineLvl w:val="(\d+)"', p)
        if ol and ol.group(1) == "0":
            parts += 1
        elif ol and ol.group(1) == "1":
            m = re.match(r"(\d+)\.\s", text)
            if m:
                subjects += 1
                nums.append(int(m.group(1)))
        elif "<w:numPr>" in p:
            bullets += 1
    tables = x.count("<w:tbl>")
    st = r.cur["stats"]
    checks = [("parts", parts, st["parts"]), ("subjects", subjects, st["subjects"]),
              ("bullet items", bullets, r.cur["leaf_kinds"]["item"]), ("tables", tables, 5)]
    for name, raw_n, parsed in checks:
        ok = raw_n == parsed
        print("  %-13s raw=%-5d parsed=%-5d %s" % (name, raw_n, parsed, "ok" if ok else "MISMATCH"))
        if not ok:
            fail("source", "%s: raw %d vs parsed %d" % (name, raw_n, parsed))
    if nums != list(range(1, 65)):
        fail("source", "subject numbers are not 1..64 in order")


def check_coverage(r):
    print("[coverage] every syllabus topic ID appears exactly once in the matrix")
    seen = {}
    for f in (ROOT / "curriculum/coverage").glob("part-*.md"):
        for line in f.read_text("utf8").split("\n"):
            m = re.match(r"^\| `([P0-9.]+)` \|", line)
            if m:
                seen[m.group(1)] = seen.get(m.group(1), 0) + 1
    ids = set(r.leaf_index)
    missing = ids - set(seen)
    extra = set(seen) - ids
    dup = [k for k, v in seen.items() if v > 1]
    print("  topics in source: %d, rows in matrix: %d" % (len(ids), len(seen)))
    if missing:
        fail("coverage", "%d topics missing from the matrix, e.g. %s" % (len(missing), sorted(missing)[:5]))
    if extra:
        fail("coverage", "%d unknown IDs in the matrix, e.g. %s" % (len(extra), sorted(extra)[:5]))
    if dup:
        fail("coverage", "%d IDs appear more than once, e.g. %s" % (len(dup), dup[:5]))
    for ls in r.lessons:
        for lid in ls["_covers"]:
            rel = ls["_path"].relative_to(ROOT).as_posix()
            if lid not in ids:
                fail("coverage", "%s covers unknown ID %s" % (rel, lid))
            elif not lid.startswith("%02d.%02d." % (ls["subject"], ls["chapter"])):
                fail("coverage", "%s covers %s outside its own subject/chapter" % (rel, lid))


def check_frontmatter(r):
    print("[frontmatter] %d lessons, %d chapter indexes" % (len(r.lessons), len(r.chapter_files)))
    for pr in r.problems:
        fail("frontmatter", pr)
    for ls in r.lessons:
        p = ls["_path"]
        rel = p.relative_to(ROOT).as_posix()
        for k in REQUIRED_LESSON_KEYS:
            if k not in ls or ls[k] in (None, "", []):
                fail("frontmatter", "%s: missing '%s'" % (rel, k))
        if not ls.get("covers") and not ls.get("adds"):
            fail("frontmatter", "%s: a lesson must list syllabus topics in 'covers' or declare what it introduces in 'adds'" % rel)
        if ls.get("status") not in STATUSES:
            fail("frontmatter", "%s: bad status %r" % (rel, ls.get("status")))
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(ls.get("reviewed", ""))):
            fail("frontmatter", "%s: 'reviewed' must be YYYY-MM-DD" % rel)
        n, ch = ls.get("subject"), ls.get("chapter")
        if n in r.subjects and ch and 1 <= ch <= len(r.subjects[n]["groups"]):
            g = r.subjects[n]["groups"][ch - 1]
            if p.parent != r.chapter_dir(n, g):
                fail("frontmatter", "%s: lives in the wrong directory (expected %s)" % (rel, r.chapter_dir(n, g).relative_to(ROOT)))
            if not r.chapter_index(n, g).exists():
                fail("frontmatter", "%s: chapter index.md is missing" % rel)
        else:
            fail("frontmatter", "%s: subject/chapter out of range" % rel)
        if not re.match(r"^%02d-[a-z0-9-]+\.md$" % int(ls.get("order", 0)), p.name):
            fail("frontmatter", "%s: file name must be '%02d-<slug>.md' matching 'order'" % (rel, int(ls.get("order", 0))))
        _, body = read_front_matter(p)
        h1 = re.findall(r"^# (.+)$", re.sub(r"```.*?```", "", body, flags=re.S), re.M)
        if len(h1) != 1:
            fail("frontmatter", "%s: expected exactly one H1, found %d" % (rel, len(h1)))
        elif h1[0].strip() != ls["title"]:
            fail("frontmatter", "%s: H1 %r differs from title %r" % (rel, h1[0], ls["title"]))
        for key in ("prerequisites", "related"):
            for x in ls.get(key) or []:
                if str(x).endswith(".md") and not (ROOT / x).exists():
                    fail("frontmatter", "%s: %s path does not exist: %s" % (rel, key, x))
        m = re.search(r"- \*\*Status:\*\* (\w[\w ]*?) \(", body)
        if m and m.group(1) != ls["status"]:
            fail("frontmatter", "%s: header status %r differs from front matter %r" % (rel, m.group(1), ls["status"]))
    orders = {}
    for ls in r.lessons:
        key = (ls["subject"], ls["chapter"])
        orders.setdefault(key, []).append(ls["order"])
    for key, o in orders.items():
        if sorted(o) != list(range(1, len(o) + 1)):
            fail("frontmatter", "subject %s chapter %s: lesson order values must be 1..N without gaps, got %s" % (key[0], key[1], sorted(o)))


CODE_LANGS = {"python", "c", "cpp", "java", "js", "javascript", "ts", "typescript", "go", "rust", "sql", "bash",
              "sh", "asm", "nasm", "json", "yaml", "solidity"}
MARK_RE = re.compile(r"<!-- (run:[\w+]+(?: [^>]*?)?|illustrative|expect) -->")


def check_markdown(r):
    print("[markdown] fences, headings, placeholders, code classification")
    for f in md_files():
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text("utf8")
        lessons = rel.startswith("docs/") and read_front_matter(f)[0] is not None and read_front_matter(f)[0].get("type", "lesson") == "lesson"
        blocks = split_fences(text)
        for b in blocks:
            if b[0] == "code" and not b[4]:
                fail("markdown", "%s:%d unclosed code fence" % (rel, b[3]))
        if lessons:
            prev_text = ""
            for b in blocks:
                if b[0] == "text":
                    prev_text = b[2]
                    continue
                lang = b[1].lower()
                if lang in CODE_LANGS:
                    tail = [ln for ln in prev_text.strip().split("\n") if ln.strip()]
                    last = tail[-1] if tail else ""
                    if not MARK_RE.search(last):
                        fail("markdown", "%s:%d %s block needs a preceding <!-- run:... -->, <!-- illustrative --> or <!-- expect --> marker" % (rel, b[3], lang))
            plain = re.sub(r"```.*?```", "", text, flags=re.S)
            for bad in ("TODO", "TBD", "lorem ipsum", "FIXME"):
                if re.search(r"\b%s\b" % bad, plain, re.I):
                    fail("markdown", "%s: contains placeholder text %r" % (rel, bad))
            levels = [len(m.group(1)) for m in re.finditer(r"^(#{1,6}) ", plain, re.M)]
            for a, b2 in zip(levels, levels[1:]):
                if b2 > a + 1:
                    fail("markdown", "%s: heading level jumps from H%d to H%d" % (rel, a, b2))
                    break


def anchors_of(path, cache={}):
    if path in cache:
        return cache[path]
    text = re.sub(r"```.*?```", "", path.read_text("utf8"), flags=re.S)
    seen, out = {}, set()
    for m in re.finditer(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        title = re.sub(r"<[^>]+>", "", re.sub(r"[*_`]|\[([^\]]*)\]\([^)]*\)", lambda mm: mm.group(1) or "", m.group(1)))
        slug = gh_slug(title)
        k = seen.get(slug, 0)
        out.add(slug if k == 0 else "%s-%d" % (slug, k))
        seen[slug] = k + 1
    cache[path] = out
    return out


LINK_RE = re.compile(r"(?<!\!)\[(?:[^\]\\]|\\.)*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links(r):
    print("[links] relative links and heading anchors")
    n = 0
    for f in md_files():
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text("utf8")
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        text = "\n".join(b[2] for b in split_fences(text) if b[0] == "text")
        text = re.sub(r"`[^`\n]*`", "", text)
        for m in LINK_RE.finditer(text):
            tgt = m.group(1)
            if re.match(r"^[a-z][a-z0-9+.-]*:", tgt, re.I) or tgt.startswith("#") and False:
                continue
            n += 1
            path_part, _, anchor = tgt.partition("#")
            dest = f if not path_part else (f.parent / path_part).resolve()
            if not dest.exists():
                fail("links", "%s -> %s (target not found)" % (rel, tgt))
            elif anchor and dest.suffix == ".md" and anchor not in anchors_of(dest):
                fail("links", "%s -> %s (anchor not found)" % (rel, tgt))
    print("  checked %d relative links" % n)


# --------------------------------------------------------------------------
def find_chrome():
    env = os.environ.get("PUPPETEER_EXECUTABLE_PATH")
    if env and Path(env).exists():
        return env
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                os.path.expanduser("~/.cache/puppeteer/chrome/*/chrome-linux64/chrome")):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    for name in ("chromium", "chromium-browser", "google-chrome"):
        w = shutil.which(name)
        if w:
            return w
    return None


def check_mermaid(r):
    print("[mermaid] parsing every diagram with mermaid-cli")
    mmdc = shutil.which("mmdc") or "/home/claude/.npm-global/bin/mmdc"
    chrome = find_chrome()
    if not Path(mmdc).exists() or not chrome:
        fail("mermaid", "mmdc or Chromium not found; cannot validate diagrams")
        return
    cache_f = ROOT / ".cache/mermaid.json"
    cache = json.loads(cache_f.read_text()) if cache_f.exists() else {}
    work = Path(tempfile.mkdtemp(prefix="mmd-"))
    pp = work / "pp.json"
    pp.write_text(json.dumps({"executablePath": chrome, "args": ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu"]}))
    todo, total = {}, 0
    for f in md_files():
        for i, b in enumerate(split_fences(f.read_text("utf8"))):
            if b[0] == "code" and b[1] == "mermaid":
                total += 1
                h = hashlib.sha256(b[2].encode()).hexdigest()
                if not cache.get(h):
                    todo.setdefault(f, []).append((h, b[2], b[3]))

    def run(f):
        items = todo[f]
        md = work / ("%d.md" % abs(hash(str(f))))
        md.write_text("\n\n".join("```mermaid\n%s\n```" % t for _, t, _ in items))
        res = subprocess.run([mmdc, "-i", str(md), "-o", str(md) + ".out.md", "-p", str(pp), "-q"],
                             capture_output=True, text=True, timeout=600)
        if res.returncode == 0:
            return f, [(h, None, ln) for h, _, ln in items]
        out = []
        for h, t, ln in items:  # pinpoint which diagram failed
            one = work / ("one-%s.mmd" % h[:10])
            one.write_text(t)
            rr = subprocess.run([mmdc, "-i", str(one), "-o", str(one) + ".svg", "-p", str(pp), "-q"],
                                capture_output=True, text=True, timeout=300)
            msg = None
            if rr.returncode != 0:
                msg = next((x for x in (rr.stderr + rr.stdout).split("\n") if "rror" in x), "render failed")
            out.append((h, msg, ln))
        return f, out

    with ThreadPoolExecutor(max_workers=4) as ex:
        for f, results in ex.map(run, list(todo)):
            for h, msg, ln in results:
                if msg is None:
                    cache[h] = True
                else:
                    fail("mermaid", "%s:%d %s" % (f.relative_to(ROOT).as_posix(), ln, msg))
    cache_f.parent.mkdir(exist_ok=True)
    cache_f.write_text(json.dumps(cache))
    shutil.rmtree(work, ignore_errors=True)
    print("  %d diagrams in repo (%d newly parsed, rest cached)" % (total, sum(len(v) for v in todo.values())))


RUN_RE = re.compile(r"<!-- run:(\w+)((?: [^>]*?)?) -->\s*\n```[\w+-]*\n(.*?)\n```"
                    r"(?:\s*\n<!-- expect -->\s*\n```[\w+-]*\n(.*?)\n```)?", re.S)


def check_code(r):
    print("[code] executing every <!-- run:... --> block and comparing expected output")
    n = 0
    for f in md_files():
        text = f.read_text("utf8")
        for m in RUN_RE.finditer(text):
            lang, flags, code, expect = m.group(1), m.group(2).strip(), m.group(3), m.group(4)
            line = text[:m.start()].count("\n") + 1
            where = "%s:%d" % (f.relative_to(ROOT).as_posix(), line)
            n += 1
            tmp = Path(tempfile.mkdtemp(prefix="code-"))
            try:
                if lang == "python":
                    src = tmp / "main.py"
                    src.write_text(code + "\n")
                    cmd = [sys.executable, str(src)]
                elif lang == "c":
                    src = tmp / "main.c"
                    src.write_text(code + "\n")
                    cc = subprocess.run(["gcc", "-std=c11", "-Wall", "-Wextra", "-pedantic", "-O0", str(src), "-o", str(tmp / "a.out")] + flags.split(),
                                        capture_output=True, text=True)
                    if cc.returncode != 0 or cc.stderr.strip():
                        fail("code", "%s: C compile problems:\n%s" % (where, cc.stderr.strip()[:600]))
                        continue
                    cmd = [str(tmp / "a.out")]
                else:
                    fail("code", "%s: unsupported run language %r" % (where, lang))
                    continue
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=60, cwd=tmp)
                if res.returncode != 0:
                    fail("code", "%s: exit %d\n%s" % (where, res.returncode, res.stderr.strip()[:600]))
                elif expect is not None:
                    got = "\n".join(x.rstrip() for x in res.stdout.rstrip().split("\n"))
                    want = "\n".join(x.rstrip() for x in expect.rstrip().split("\n"))
                    if got != want:
                        fail("code", "%s: output differs.\n--- expected\n%s\n--- got\n%s" % (where, want, got))
            except subprocess.TimeoutExpired:
                fail("code", "%s: timed out" % where)
            finally:
                shutil.rmtree(tmp, ignore_errors=True)
    print("  executed %d code blocks" % n)


def check_fresh(r):
    print("[fresh] generated files are up to date")
    res = subprocess.run([sys.executable, str(ROOT / "tools/build.py"), "--check"], capture_output=True, text=True)
    if res.returncode != 0:
        fail("fresh", "generated files are stale or have problems:\n" + res.stdout.strip()[:800])


CHECKS = {"source": check_source, "coverage": check_coverage, "frontmatter": check_frontmatter,
          "markdown": check_markdown, "links": check_links, "mermaid": check_mermaid,
          "code": check_code, "fresh": check_fresh}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=",".join(CHECKS))
    a = ap.parse_args()
    r = Repo()
    for name in a.only.split(","):
        CHECKS[name.strip()](r)
    print()
    if FAILS:
        print("%d problem(s) found." % len(FAILS))
        sys.exit(1)
    print("All selected checks passed.")


if __name__ == "__main__":
    main()
