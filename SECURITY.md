# Security Policy

## What counts as a security problem here

This repository is documentation plus small Python tooling, so security issues
fall into three groups:

1. **Tooling vulnerabilities** in `tools/` (for example unsafe path handling).
2. **Unsafe teaching content**: a lesson presenting insecure code, weak
   cryptography or a dangerous operational practice as if it were good practice.
3. **Supply-chain risk**: dependencies or scripts that fetch or run untrusted code.

## Important: validation executes code from Markdown

`python3 tools/validate.py` (the `code` check) **runs the code blocks marked
`<!-- run:... -->` in lessons**. Treat lesson contributions as untrusted input:
run the validator in a container or other sandbox, not on a machine holding
secrets, and review code blocks before executing them. The validator applies a
timeout to each block but is not a security boundary.

## Reporting

The maintainers have not yet published a private security contact:
**[to be set by the repository owner]**. If the hosting platform offers private
vulnerability reporting, enable it and use it. Until a contact is published,
open an issue titled "Security: request private channel" **without** technical
details, and a maintainer will arrange a private way to receive them.

## What to expect

Reports will be acknowledged, assessed and, where valid, fixed or corrected in
the lesson with a note in `CHANGELOG.md`. Errors in teaching content that could
cause harm if followed are treated with the same priority as tooling bugs.
