---
trigger: always_on
description: "Ponytail rule: minimal code engineering, YAGNI ladder, and shortest diffs."
---

# Ponytail Rule (Minimal Engineering)

Active by default.
The best code is code never written.

## Decision Ladder (Stop at first rung)
1. **YAGNI**: Does feature need to exist? If not, skip.
2. **Reuse**: Check codebase first before writing new helpers.
3. **Stdlib/Native**: Standard library over custom code/packages.
4. **Installed Deps**: Never add new dependencies for simple logic.
5. **One-Liner**: One line when possible.
6. **Minimal Diff**: Fewest files, shortest working diff.

## Principles
- **Root Cause**: Fix origin, not symptom. Grep callers before patching.
- **Understand First**: Trace actual execution flow end-to-end before editing.
- **Non-Negotiables**: Never compromise input validation, error handling, security, or data safety.
