# Proposed Additions to the Syllabus

Topics that are **not in the source syllabus** but would complete it. The source is authoritative and nothing here replaces any of its topics; these are complements.

**Method.** Each candidate was tested by case-insensitive search across every topic and group title in `curriculum/curriculum.json`, then confirmed by reading the neighbouring topic lists. Some candidates that looked missing at first are in fact present and are *not* listed (time-series analysis, variational quantum algorithms, performance modelling, sensor fusion, LLM inference optimisation, prompt injection, MCP and others).

A proposal becomes an **addition** when a lesson introduces it and declares it with `adds:` in its front matter; it then appears in the [coverage matrix](coverage-matrix.md). Status "Added" below means exactly that.

| # | Proposed topic | Suggested home | Why it is needed | Status |
|---|---|---|---|---|
| 1 | Binary-coded decimal (BCD) and Gray code | Subject 1, chapter 2 | Standard binary codes met in displays, clocks and position encoders | Added |
| 2 | Bitwise operations and shifts | Subject 1, chapter 2 | Needed from the first day of systems programming; the source covers binary arithmetic but not the operators | Added |
| 3 | Integer overflow, wraparound and saturation | Subject 1, chapter 2 | A leading cause of real bugs and vulnerabilities | Added |
| 4 | Fixed-point arithmetic | Subject 1, chapter 2 | The main alternative to floating point in embedded and signal-processing work, and the right way to hold money | Added |
| 5 | Error detection and correction codes (parity, checksums, CRC, Hamming codes) | Subject 1, chapter 3, with a pointer from Subject 5 | Underpin storage, memory (ECC) and networking; no topic names them | Added |
| 6 | Date, time and time zones | Subject 6 | A notorious source of bugs in every language | Proposed |
| 7 | Regular expressions and text processing | Subject 6 or 9 | Ubiquitous tool; not named in the source | Proposed |
| 8 | Bloom filters and probabilistic data structures | Subject 9 (advanced) | Widely used in databases and caches | Proposed |
| 9 | Consistent hashing | Subject 22 | Foundation of sharded caches and databases | Proposed |
| 10 | Conflict-free replicated data types (CRDTs) | Subject 22 | A central technique for convergent replicated state | Proposed |
| 11 | Queueing theory and Little's law | Subject 29 | The mathematics behind latency under load | Proposed |
| 12 | Flame graphs | Subject 29 | The standard way to read a CPU profile | Proposed |
| 13 | Service mesh | Subject 25 | Common part of the container ecosystem; only the sidecar pattern is named | Proposed |
| 14 | Dimensional modelling (star and snowflake schemas, slowly changing dimensions) | Subject 32 or 33 | Core warehouse design technique | Proposed |
| 15 | Differential privacy | Subject 31 or 46 | The principal formal privacy guarantee; the source names privacy-preserving computation only generally | Proposed |
| 16 | Entity-component-system architecture | Subject 47 | The dominant data-oriented game architecture | Proposed |
| 17 | Kalman filtering | Subject 51 | The classic state-estimation tool behind sensor fusion | Proposed |
| 18 | Amdahl's law, Gustafson's law and the roofline model | Subject 53 | The core performance models; the source names only performance modelling in general | Proposed |
| 19 | Named safety-critical standards (DO-178C, ISO 26262, IEC 61508) | Subject 57 or 59 | The source mentions functional safety but names none of these standards | Proposed |
| 20 | Lambda calculus | Subject 7 or 64 | Theoretical root of functional programming; absent by name | Proposed |
