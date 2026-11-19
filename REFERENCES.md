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

Claims that were checked against sources while writing Subject 1, chapters 1 to 5 (checked 2026-11-01 by web search):

| Claim in the lessons | Check |
|---|---|
| Frontier at Oak Ridge National Laboratory was the first system on the TOP500 list to exceed one exaflop/s on the Linpack benchmark, announced in May 2022 | Confirmed by the TOP500 site and US Department of Energy and HPC press reports. Some reports note that China reportedly operates exascale-class systems that were not submitted, so the lessons say "first on the TOP500", not "first in the world". |
| C23 requires two's complement representation for signed integers (WG14 proposal N2412) | Confirmed from the committee document and secondary discussion. |
| C++20 requires two's complement (proposal P1236R1), and signed overflow remains undefined behaviour in both languages | Confirmed from the proposal and discussion of it. |
| Python 3.12's built-in `sum()` uses compensated (Neumaier) summation for floats | Confirmed from the Python 3.12 "What's New" entry (gh-100425). It was also observed: a million additions of 0.1 gave no error with `sum()` on Python 3.12 but an error of about 1.3e-6 with an explicit loop. |
| The WHATWG Encoding Standard describes UTF-8 as the most appropriate encoding for the interchange of Unicode | Confirmed from the standard at encoding.spec.whatwg.org and its 2018 snapshot. |
| The MAC address range 00:00:5e:00:53:00 to 00:00:5e:00:53:ff is reserved for documentation examples | Confirmed from RFC 7042 and the IANA Ethernet Numbers registry; RFC 9542 has since replaced RFC 7042, and the lesson cites RFC 9542. |

Claims that were checked against sources while writing Subject 1, chapter 6 (checked 2026-11-14 by web search). Most pages consulted are secondary (mirrors of manuals, kernel tables, course notes); the primary specifications themselves were **not** opened, and each row says what was read.

| Claim in the lessons | Check |
|---|---|
| The stored-program design was described in von Neumann's *First Draft of a Report on the EDVAC*, dated 30 June 1945, from discussions with the EDVAC team at the Moore School; credit for the design is disputed | Confirmed from encyclopedic and course sources: a 101-page draft, circulated under von Neumann's name alone, describing one memory for numbers and orders; Eckert, Mauchly and others contested the attribution. The report itself was not read. |
| Linux system-call conventions: x86-64 `syscall` with the number and the result in `rax` and the first three arguments in `rdi`, `rsi` and `rdx`; arm64 `svc #0` with the number in `x8` and the result in `x0`; RISC-V with the number in `a7` and the result in `a0` | Confirmed from the Linux `syscall(2)` manual page. The page lists the RISC-V instruction as `scall`; the lesson uses `ecall`, the name used in the RISC-V trap material checked below. |
| `write` is system call 1 on x86-64 and 64 in the generic table used by arm64 and RISC-V | x86-64 confirmed from the kernel's `syscall_64.tbl` and arm64 from `asm-generic/unistd.h`, both as mirrored on public pages. RISC-V's use of the generic table is stated by encyclopedic sources and was not checked in the RISC-V port's source. |
| x86 has 256 interrupt vectors; 0 to 31 are reserved for architecture-defined exceptions and interrupts and 32 to 255 are available for external interrupts; the interrupt descriptor table is located through the IDTR register | Confirmed from passages of the Intel SDM volume 3A quoted on mirror sites. |
| x86-64 `SYSCALL` leaves the next instruction's address in RCX and the flags in R11, and loads RIP from the IA32_LSTAR register | Confirmed from the SYSCALL instruction reference as reproduced on mirror sites. |
| x86 instructions are 1 to 15 bytes long | Confirmed from a quoted SDM statement and the OSDev wiki. |
| AArch64: a vector table of 16 slots (four sources by four types), each 128 bytes and holding instructions, located through `VBAR_ELn`; `svc` raises a synchronous exception; `eret` returns; the return address is kept in `ELR_ELn`; the general-purpose registers are x0 to x30 | Confirmed from the OSDev wiki, a bare-metal tutorial and university course notes. The stack pointer and zero register are stated from established knowledge. The Arm Architecture Reference Manual was not consulted. |
| RISC-V: `ecall` raises an environment-call exception handled through `stvec`; `sepc` holds the address of the `ecall` itself, so software adds 4 before `sret`; there are 32 integer registers with x0 always zero; compressed 16-bit instructions are an optional extension | Confirmed from MIT 6.1810 course material and other course notes. The RISC-V specifications were not consulted. |
| Linux timer-tick rates of 100, 250, 300 and 1000 per second are build options, and idle processors can stop the tick (`NO_HZ_IDLE`) | Confirmed from `kernel/Kconfig.hz` and the kernel's NO_HZ documentation, as mirrored on public pages. |
| `write(2)`: a call may transfer fewer bytes than requested; failure returns -1 and sets `errno`; `EBADF` means an invalid descriptor; `EINTR` applies only when the call was interrupted before anything was written | Confirmed from the Linux `write(2)` manual page as mirrored on public pages. |
| *Operating Systems: Three Easy Pieces* is free online and its chapter 6 is "Mechanism: Limited Direct Execution" | Confirmed from the book's site and course material that cites it. |

Claims that were checked against sources while writing Subject 2, chapter 1 (checked 2026-11-18 by web search):

| Claim in the lessons | Check |
|---|---|
| The Moon is about 384,000 km from Earth on average (about 363,300 km at the nearest point and about 405,500 km at the farthest). The paper-folding figures in *Exponents and Logarithms* (about 220,000 km after 41 folds and about 440,000 km after 42) therefore fall short of the Moon at its nearest and pass it at its farthest | Confirmed from several astronomy sources that cite NASA figures. The 0.1 mm sheet thickness is an assumption stated in the lesson. |
| C89 left the direction of truncation of integer division, and so the sign of the remainder, implementation-defined for negative operands. C99 requires truncation toward zero, guarantees `(a/b)*b + a%b == a`, and gives the remainder the sign of the dividend | Confirmed from the CERT C secure-coding guidance, which quotes ISO/IEC 9899 section 6.5.5, and from discussion of the C89 and C99 texts. The standards themselves were not opened. |

The addresses added in Subject 2, chapter 1 are `docs.python.org` pages and were not opened either. The addresses added in chapter 6 were not fetched. The OSTEP address appeared in search results, the man-pages project address is quoted in the manual pages themselves, and the three `docs.python.org` pages were not opened.

Executed claims: every runnable code block in the lessons was run (Python 3.12 and GCC 13 in the authoring environment) and its output compared with the documented output; see [PROGRESS.md](PROGRESS.md). In chapter 6 the extended machine was also rebuilt independently from the design in the session summary, and its recorded results were reproduced exactly: 79, 85 and 127 steps with 0, 1 and 8 timer interrupts; the wrong answer 82 after 1,555 steps and 118 interrupts when the zero flag is not saved; the interrupt storm; and the protection fault. In Subject 2, chapter 1, the claims about Python's behaviour (that `math.log(0)` raises a `ValueError`, that `2.0 ** 1024` raises an `OverflowError` while the integer `2 ** 1024` is exact, and that `math.log1p` and `math.expm1` keep digits that the direct formulas lose) were checked by running them.

## Claims from established knowledge, not re-verified here

The historical, factual and incident details in the lessons come from standard sources, but were **not re-checked against primary documents** in this session. They are queued for verification in [PROGRESS.md](PROGRESS.md) before any lesson is promoted beyond *Drafted*:

- **History:** the Analytical Engine and Ada Lovelace's 1843 notes; Turing 1936; the Manchester "Baby" (1948) and EDSAC (1949); ENIAC reprogramming effort; the Setun ternary computer; the CDC 6600's ones'-complement arithmetic; Shannon's thesis and papers; the origin of the word *byte* and the System/360; the standardisation of ASCII; the design of UTF-8 by Thompson and Pike in 1992.
- **Incidents:** the Patriot (GAO/IMTEC-92-26) and Ariane 5 (Flight 501 Inquiry Board) details.
- **Practice:** MySQL's `utf8` being an alias for `utf8mb3`; the four QR-code error-correction levels; which formats use which byte order; CRC-32 in Ethernet, ZIP and PNG; byte-swap instructions on x86 and Arm; bit order on UART and Ethernet; the number of Unicode characters assigned.
- **Hardware figures:** typical sizes and latencies of caches, DRAM, SSDs and hard disks; PCIe encoding and per-lane rates; USB, SATA and NVMe speeds; 80 PLUS and PUE; the dates and names of Spectre, Meltdown and Row Hammer; big.LITTLE; Amdahl's 1967 paper. The lessons label the figures as orders of magnitude, but they have not been checked against datasheets or the original papers.
- **Architecture and system practice in chapter 6:** `HLT` and `WFI` as idle instructions; the Harvard architecture in microcontrollers and the split first-level cache; modern x86 translating instructions into micro-operations; the stack-based designs of the JVM, WebAssembly and Python's bytecode; the W^X policy; `objdump -d` and QEMU; AT&T versus Intel operand order; `sysenter`, `int 0x80` on 32-bit Linux and `int3` breakpoints; `sysret`, `eret` and `sret` being restricted to privileged code; the interrupt controllers APIC, GIC and PLIC; top and bottom halves; Linux's NAPI; the vDSO; the cost of Meltdown mitigations on kernel entry; the bibliographic details of Dijkstra's 1968 paper on the THE system; and the two illustrative `strace` lines in *Interrupts and System Calls*, which were not run because `strace` was not available.
- **Mathematics and computing facts in Subject 2, chapter 1:** that Java and JavaScript truncate integer division toward zero as C does; Euclid's *Elements* as the source of the GCD algorithm, and the result usually attributed to Lamé that consecutive Fibonacci numbers are the worst case for it; that Python's `round` and IEEE 754's default mode both send exact halves to the even neighbour (the lesson's own output shows Python doing so); that IEEE 754 defines decimal formats and that Python's `decimal` module follows a general decimal arithmetic specification; the Abel-Ruffini theorem; decibels as ten times a base-10 logarithm; the discrete logarithm and Diffie-Hellman; the size of numbers in public-key cryptography; Euler's formula; the lambda calculus; and the bibliographic details of Shannon (1948), Diffie and Hellman (1976) and Backus (1978).
- **Teaching models are simplified:** the two simulators in chapter 6 are models, not descriptions of any real processor. The simplifications are listed in the lessons (for example, the timer ignores ticks while the CPU is in the kernel).
- **Code validated by its own reader only:** the PNG and WAV files the lessons build were checked by the lessons' own readers (structure and CRC) and by Python's `wave` module, **not** by an independent image or audio decoder.
