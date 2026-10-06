### Autopilot-stack

**Build and verify a linear PR stack for the user to review and land.** Use this when the user wants the work prepared but not merged. This workflow needs a usable forge CLI and independent verification. Parallel work uses the host's native agent support when available; it does not assume detached agents or a background scheduler.

1. List each change, dependency, target branch, acceptance condition, and verification path. If one session cannot finish the stack, deliver a finite phase and handoff.
2. Keep one owner per PR and one writer per branch. Isolate work that can run in parallel. Use pstack custom profiles when installed; otherwise subagents inherit the parent model.
3. Open PRs in dependency order. Keep titles and descriptions concise, include the verification evidence, and do not merge or arm auto-merge.
4. For every PR, record the exact head SHA and base SHA. Run checks on that head, then ask an independent read-only agent to review it when the host supports delegation. Inspect findings and artifacts yourself. State when review was not independent or model-diverse.
5. Recheck every PR after a rebase or push. A verdict for an old SHA does not cover a new patch. Keep the stack linear and stop if a conflict changes the design or the available session ends.
6. Return the stack in bottom-to-top order with URLs, SHAs, checks, verification evidence, open risks, and a clear statement that the user must land it.
