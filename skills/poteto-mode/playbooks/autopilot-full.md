### Autopilot-full

**Drive independent PRs to merge only when the user grants that scope and the current host can support it.** Use this for an explicitly requested full-autonomy queue. If durable sessions, agents, or a scheduler are unavailable, stop at a finite checkpoint and report the handoff instead of claiming background progress.

1. List the queue, owners, base branch, checks, verification bar, and user-granted actions. Keep user-named items at the approval boundary the user specified.
2. Check required tools and permissions before starting. Resolve the forge once. Do not assume cloud agents, cross-model routing, detached workers, or continuous monitoring. Use configured host profiles when available; report when profiles share the parent model.
3. Give each independent PR one owner and one isolated branch or worktree. Keep every brief bounded and self-contained. Require a decision log, exact head SHA, verification receipts, and open risks.
4. Verify each owner’s code-ready head with an independent read-only review. Inspect the resulting artifacts yourself. A reviewer that used the same model is an independent pass, not model-diverse review.
5. Merge only when the user explicitly authorized merges, repository policy allows them, current CI is green, the independent verdict matches the exact head SHA, and the base is current. Never force-push a shared branch. Stop at any approval boundary the user named.
6. After a merge, verify the merged SHA and checks before the next queue item. If the host cannot keep work running between turns, return the verified checkpoint and next action.
7. Honor a stop request immediately and report active branches, running work, and any side effects already completed.

**Reply:** the queue with each PR's owner, state, and head SHA; verdicts and evidence; what merged; open approval gates; and the next checkpoint.
