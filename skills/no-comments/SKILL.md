---
name: no-comments
description: "Review scoped code for comments and suppressions that obscure behavior, then fix accepted findings within scope. Use for `no-comments` or before reviewing a change."
---

# No comments

Use a configured read-only reviewer profile when one is available. Otherwise ask a read-only agent to follow this skill. If delegation is unavailable, perform the review directly. Apply accepted findings yourself.

## Scope

Use the caller's files or diff. Otherwise inspect the working diff against the base branch, defaulting to `main` when that is the repository's base.

## Steps

1. Give the reviewer the exact scope. Ask it to inspect comments, dead code, workaround narration, lint suppressions, and type suppressions. It reports only, and makes no edits.
2. Inspect the report and cited code. Reject application-code edits, scope escapes, exception-protected deletions, misstated `MUST KILL` reasons, and flags that treat intentional code as guilty. Do not restore a comment without proof that it describes a constraint the code cannot express.
3. Fix accepted findings with the smallest root-cause change. If a fix needs a new shape, use `architect` and stop at the sketch before implementation.
4. For constraints that need to remain, offer the cheapest in-scope type, runtime, test, or CI encoding. Do not modify outside-scope code without the user's instruction.
5. Re-run a rejected report once with the failure named. If it fails again, report the open finding and fail this review.

## Output

Report the deletion count, restored comments, reruns, fixes, encoding offers, encoded constraints, and open work.
