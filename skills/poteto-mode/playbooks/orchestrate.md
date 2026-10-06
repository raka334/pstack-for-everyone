### Orchestrate

Use this for a standing project that outlives one session and needs durable state across many work units. A complex task that one session can finish belongs in **figure-it-out** or **autonomous-run** instead.

Skills do not provide a durable multi-day coordinator, background workers, or a scheduler by themselves. Before starting, verify the repository has an orchestration store and scripts, and the active host can launch and resume the required work. If either is missing, write a phased plan and complete one bounded phase. Do not simulate liveness or promise that work will continue after the session.

## Roles

- **Coordinator.** Owns the done predicate, briefs, queue, verification ledger, and user report. It may implement work only when no independent owner is assigned.
- **Track owner.** Owns a bounded workstream and its unit list. Use only when the number of units exceeds what the coordinator can drain.
- **Worker or verifier.** Owns one isolated unit or one read-only verification. Use project worktrees for concurrent writers. A verifier should not have authored the patch it reviews.

Prefer fewer, broader workers. Agent profiles may inherit the parent model unless their host-specific configuration says otherwise. Do not claim model diversity without distinct configured models.

## Durable state

Use the repository's existing orchestration store when present. Keep one writer per file and make the tables human-readable. At minimum, track standing constraints, units, branches, PRs, head SHAs, verification status, decisions, and human approval gates. Do not invent a global transcript path for the active host. Store the evidence the next session needs in the repository or an explicitly selected user-accessible location.

Each unit brief names:

- Goal and exact scope.
- Files or paths the worker may change.
- Relevant evidence and upstream findings.
- Acceptance criteria and exact verification commands.
- Required approvals and forbidden actions.
- Report shape, including status, branch, head SHA, evidence, and open risks.

## Phases

1. **Frame.** Count the units, name dependencies and done predicates, check the tools and session persistence, and write the standing orders before delegation.
2. **Pilot.** Run one representative unit through implementation, verification, and state recording. Fix the brief or verification procedure from evidence.
3. **Scale.** Delegate independent units through native agents or sessions when available. Use separate branches or worktrees for concurrent writers. Refuse to spawn work when its scope or verification path is missing.
4. **Drain.** At each checkpoint, reconcile every result against its branch, SHA, tests, PR, and decision log. Do not rely on a completion message alone.
5. **Integrate.** Land only through repository-approved procedures. Keep the bottom of a dependent stack verified before working above it. Stop at user approval boundaries.
6. **Close.** Reconcile every unit, verify the final predicate on the real artifact, audit the decision log, and record unfinished work with an exact next action.

## Limits and escalation

A tool failure is not evidence that a worker is dead. Check actual state before retrying. After bounded retries, record a blocker and hand off. Ask the user only for genuine product choices, explicitly reserved approvals, or a dead end that cannot be tested. Honor stop requests by ending new work and reporting current side effects.

**Reply:** the done predicate, unit and PR states, current verified frontier, evidence, approval gates, and exact next action.
