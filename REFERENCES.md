# References

The master index of sources. Each lesson also ends with its own *Further reading* section that separates official specifications, textbooks, research and documentation.

## Reference policy

- Prefer official documentation, standards (IEEE, ISO, IETF, W3C, WHATWG, NIST), academic textbooks and peer-reviewed work.
- **No invented citations, URLs, benchmarks or APIs.** Where a source cannot be verified, the claim is left out or flagged below.
- Only stable, well-known addresses are linked (organisation home pages, `rfc-editor.org` RFC pages, `docs.python.org` module pages). The authoring environment had no general network access, so those links were **not fetched**; confirm them before relying on them.
- Lessons paraphrase sources; they do not reproduce them.

## Reference pages

| Page | Contents |
|---|---|
| [Recommended books](resources/recommended-books.md) | Textbooks by subject |
| [Research papers](resources/research-papers.md) | Foundational papers and incident reports |
| [Standards and specifications](resources/standards-and-specifications.md) | IEEE, ISO, IETF, Unicode and others |
| [Official documentation](resources/official-documentation.md) | Language and tool documentation |

## Verification log

Claims that were checked against sources while writing Subject 1, chapters 1 and 2 (checked 2026-11-01 by web search):

| Claim in the lessons | Check |
|---|---|
| Frontier at Oak Ridge National Laboratory was the first system on the TOP500 list to exceed one exaflop/s on the Linpack benchmark, announced in May 2022 | Confirmed by the TOP500 site and US Department of Energy and HPC press reports. Some reports note that China reportedly operates exascale-class systems that were not submitted, so the lessons say "first on the TOP500", not "first in the world". |
| C23 requires two's complement representation for signed integers (WG14 proposal N2412) | Confirmed from the committee document and secondary discussion. |
| C++20 requires two's complement (proposal P1236R1), and signed overflow remains undefined behaviour in both languages | Confirmed from the proposal and discussion of it. |
| Python 3.12's built-in `sum()` accuracy for floats | **Observed** (a million additions of 0.1 gave no error with `sum()` on Python 3.12 but an error of about 1.3e-6 with an explicit loop). The statement that earlier versions do not compensate, and the exact version that introduced the change, should be confirmed against the Python 3.12 "What's New". |

Executed claims: every runnable code block in the lessons was run (Python 3.12 and GCC 13 in the authoring environment) and its output compared with the documented output; see [PROGRESS.md](PROGRESS.md).

## Claims from established knowledge, not re-verified here

The historical and incident details in the lessons come from standard sources, but were **not re-checked against primary documents** in this session. They are queued for verification in [PROGRESS.md](PROGRESS.md) before any lesson is promoted beyond *Drafted*: the Analytical Engine and Ada Lovelace's 1843 notes; Turing 1936; the 1945 EDVAC report; the dates of the Manchester "Baby" (1948) and EDSAC (1949); ENIAC reprogramming time; the Setun ternary computer; the CDC 6600's ones'-complement arithmetic; the Shannon switching-circuit thesis; and the details of the Patriot (GAO/IMTEC-92-26) and Ariane 5 (Flight 501 Inquiry Board) incidents.
