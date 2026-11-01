# Frequently Asked Questions

## About the library

**Where does the curriculum come from?**
From one authoritative source file, `curriculum/source/Software_Engineering_Topics.docx`: 15 parts and 64 numbered subject areas. Every topic in it has a stable ID and appears in the [coverage matrix](curriculum/coverage-matrix.md). The full text is in [COMPLETE-CURRICULUM.md](COMPLETE-CURRICULUM.md).

**Why are most topics not written yet?**
The library is very large and is being built in a fixed order, starting with Part I. Topics that are not written are shown as *not started* or *planned*; they are never hidden or counted as done. See [PROGRESS.md](PROGRESS.md) and [ROADMAP.md](ROADMAP.md).

**Do I need to learn everything?**
No. The source itself says a software engineer is not expected to master the whole map. Use [LEARNING-PATHS.md](LEARNING-PATHS.md) to separate common foundations from role-specific depth.

**Was the syllabus changed?**
No topic text was changed or removed. The parser removed web-image captions and citation chips left over from the file's export and recorded every removal in the [extraction report](curriculum/extraction-report.md). Topics that this library adds are labelled as additions in the coverage matrix.

## About quality

**What does "Drafted" mean?**
A complete lesson that passes the automated checks (links, front matter, executed code, parsed diagrams). It has not yet been independently reviewed. Only *Reviewed* and *Complete* imply a second person checked the content.

**Can I trust the code examples?**
Runnable examples are executed by `tools/validate.py` and their output is compared with the output shown. Examples labelled *illustrative* are fragments or pseudocode and are not executed. Execution proves the code runs and matches the shown output; it does not prove the explanation around it is right, which is what review is for.

**How do I know a technical claim is current?**
Each lesson records the date it was last reviewed. Fast-moving topics state the versions they refer to. Where a claim comes from a standard or book it is cited; claims that could not be verified are not made.

**Why Mermaid diagrams?**
They are plain text, render natively on GitHub, diff well in pull requests, and can be validated by a parser.

## Using and contributing

**Which programming languages are used?**
Whichever fits the idea: Python for most demonstrations, C where memory and machine representation matter, and others (SQL, Go, Rust, Java, JavaScript, TypeScript, assembly, Solidity, quantum frameworks) as later subjects need them. Each block states what it needs.

**I found a mistake or a confusing explanation.**
Please open an issue naming the lesson and the passage, and say what you expected. If you can, propose a fix in a pull request; see [CONTRIBUTING.md](CONTRIBUTING.md).

**Can I add a topic that is not in the syllabus?**
Yes, by proposing it in [curriculum/proposed-additions.md](curriculum/proposed-additions.md) and declaring it with `adds:` in the lesson that introduces it, so the inventory stays honest.

**What licence applies?**
None has been chosen yet; see [LICENSE](LICENSE).
