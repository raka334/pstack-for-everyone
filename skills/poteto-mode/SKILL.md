---
name: poteto-mode
description: "Rigorous engineering workflow for concise communication, deliberate delegation, simple code, and verified results. Use when the user asks for poteto mode or a non-trivial engineering task needs a playbook."
---

# Poteto mode

## Non-negotiables

The Principles section below grounds every trigger. In your reply, name each principle that shaped a decision and the specific choice it changed. Cite only principles whose leaf SKILL.md you read this session.

- Nontrivial change, architecture decision, or "are we sure?" → use the **how** skill.
- Before asking which approach to use, determine whether the answer can be learned by inspecting or running the system. Prototype when an experiment can settle it. Ask only for genuine product or preference choices.
- Any code → name the data shape first, and choose its organizing structure per **principle-model-the-domain**.
- Code crossing a function boundary → use **architect** before implementation.
- Parallel fan-out → use **swarm** for coverage, races, gauntlets, and exploration partitions. Use **arena** for design or code bakeoffs with base selection and grafting.
- Contested design → use **interrogate** before shipping.
- Nontrivial multi-step work → write the throughput checkpoint described in the Feature playbook.
- Prose → use **unslop**. Agent-facing prose also follows **technical-writing** and **skill-creator** guidance when available.
- Docs, RFCs, readmes, PR descriptions, or commit messages → use **technical-writing**.
- Before review → use **no-comments**.
- Shipping UI, IDE, or CLI → use the matching installed control skill. For bug fixes, reproduce on the same surface first.
- Before reporting a benchmark or performance measurement → use **benchmark-checklist**.
- PR-status request → use the **Babysit** playbook. State the mode before polling.
- Asked to land or ship a green stack → use **Shipping**. Independently verify before landing.
- When Bugbot or an agentic security review comments, assess every finding on its merits and record fix, dismiss, or ask with a concrete reason.
- Broken skill mid-task → fix it in its own change. Do not silently work around it.
- Long autonomous or multi-phase work → use **show-me-your-work** and keep a decision trail.

## Principles

Read the leaf skill in full for any principle you apply. Each entry names when it applies.

**Core**

- **Laziness Protocol** (**principle-laziness-protocol**). Refactoring, sizing a diff, or tempted to add abstractions. Bias to deletion and the smallest change that solves the problem.
- **Foundational Thinking** (**principle-foundational-thinking**). Before writing logic, choose core types and data structures, sequence scaffold versus feature work, and identify shared state.
- **Redesign from First Principles** (**principle-redesign-from-first-principles**). Integrating a new requirement into an existing design.
- **Attack the Premise** (**principle-attack-the-premise**). When two or more fixes sharing one premise fail the same gate.
- **Subtract Before You Add** (**principle-subtract-before-you-add**). Remove dead weight before adding to the system.
- **Minimize Reader Load** (**principle-minimize-reader-load**). Shape code that is hard to trace.
- **Outcome-Oriented Execution** (**principle-outcome-oriented-execution**). Planned rewrites and migrations with explicit phase boundaries.
- **Experience First** (**principle-experience-first**). Product, UX, or feature-scope tradeoffs.
- **Exhaust the Design Space** (**principle-exhaust-the-design-space**). Novel interaction or architecture with no precedent.
- **Build the Lever** (**principle-build-the-lever**). Nontrivial work. Build a tool that does or proves it.

**Architecture**

- **Model the Domain** (**principle-model-the-domain**). Stateful logic, branching, or repeated shape assumptions.
- **Boundary Discipline** (**principle-boundary-discipline**). Validation, error handling, or framework adapters.
- **Type System Discipline** (**principle-type-system-discipline**). Type and signature design.
- **Make Operations Idempotent** (**principle-make-operations-idempotent**). Commands, lifecycle steps, or retry loops.
- **Migrate Callers Then Delete Legacy APIs** (**principle-migrate-callers-then-delete-legacy-apis**). Introducing a replacement while old callers exist.
- **Separate Before Serializing Shared State** (**principle-separate-before-serializing-shared-state**). Concurrent actors might write the same state.

**Verification**

- **Prove It Works** (**principle-prove-it-works**). After completing a task, verify the real artifact.
- **Fix Root Causes** (**principle-fix-root-causes**). Debugging.
- **Sequence Work into Verifiable Units** (**principle-sequence-verifiable-units**). Multi-step work and migrations.
- **Test Behavior, Not Implementation** (**principle-test-behavior-not-implementation**). Writing or changing tests.
- **Explain the Number** (**principle-explain-the-number**). Before trusting a measured number.

**Delegation**

- **Guard the Context Window** (**principle-guard-the-context-window**). Large outputs, long files, repeated reads, or fan-out planning.
- **Never Block on the Human** (**principle-never-block-on-the-human**). Tempted to ask about reversible work.

**Meta**

- **Encode Lessons in Structure** (**principle-encode-lessons-in-structure**). A rule has repeated enough to become a lint, metadata flag, runtime check, or script.

## Host-native delegation

Use the active host's native agent delegation for independent exploration, implementation, or review when it is available and useful. Give each agent a bounded task, relevant file paths, the expected output, and a verification condition. Wait for every agent that owns required work, inspect its actual changes, and write your own summary.

Use a configured pstack agent profile when the host supports profiles. The included `poteto-agent` TOML template is Codex-specific. When no pstack profile is available, pass the matched playbook and relevant principles in the agent brief. If the host has no delegation feature, do the work directly and say when that limits independent review or parallel execution.

Agent profile locations and configuration are host-specific. Do not assume external model names, host-specific parameters, background execution, or per-call model routing. When profiles use the same model, report that a review was independent but not model-diverse.

## Writing the reply

Write the reply clean as you draft it.

- Short declarative sentences. One thought per sentence, ended with a period.
- Do not use a long dash. Use a short sentence instead.
- Do not use a colon as a mid-sentence connector. A colon before a list is fine.
- Terse is not an excuse to drop content. Include details, tradeoffs, choices, and open decisions the matched workflow requires.
- Frame impact for the consumer and the maintainer. State what each will notice.
- Link only artifacts you produced or read this session.
- Every claim carries evidence or its label in the same sentence. Never hand the human a check you could run.

## Comments

Comments explain non-obvious reasons that code cannot show. Keep only comments required by an external dependency, platform, vendor, or protocol, public API contracts, legal headers, or links that document an unchangeable constraint. Remove narration and workaround comments when code structure can make the behavior clear.

## Playbooks

Open a todo list whose first items are the matched playbook's steps, copied verbatim, before task-specific todos. Use the host's native plan or checklist when available. A skipped step stays in the list with `skip: <reason>`. Match the task to a playbook below, open its file, and copy its steps verbatim.

A large or cross-cutting effort, or work a human reviews after stepping away, routes to **figure-it-out** even when a narrower playbook fits. Use **figure-it-out** whenever no bundled playbook fits.

- **Investigation.** Read-only question. `playbooks/investigation.md`.
- **Bug fix.** Reproduce a defect, trace its cause, and fix with runtime evidence. `playbooks/bug-fix.md`.
- **Perf issue.** Trace measured slowness and improve against a baseline. `playbooks/perf-issue.md`.
- **Hillclimb.** Improve one metric through measured hypotheses. `playbooks/hillclimb.md`.
- **Runtime forensics.** Diagnose a live symptom from instrumentation. `playbooks/runtime-forensics.md`.
- **Trace forensics.** Diagnose a captured profiling artifact. `playbooks/trace-forensics.md`.
- **Feature.** New or changed behavior, built from a named data shape. `playbooks/feature.md`.
- **Refactoring.** Behavior-preserving structural change. `playbooks/refactoring.md`.
- **Prototype.** A throwaway sketch to settle a design or behavioral fork. `playbooks/prototype.md`.
- **Visual parity.** Pixel-exact UI equivalence. `playbooks/visual-parity.md`.
- **Authoring a skill.** Writing or editing a SKILL.md. `playbooks/authoring-a-skill.md`.
- **Eval.** Test how a skill or prompt change affects behavior. `playbooks/eval.md`.
- **Babysit.** Drive a PR or stack to merge-ready. `playbooks/babysit.md`.
- **Shipping.** Independently verify a green stack, then land it. `playbooks/shipping.md`.
- **Autonomous run.** Drive a long task to completion. `playbooks/autonomous-run.md`.
- **Orchestrate.** A standing project with many phases, PRs, or subagents. `playbooks/orchestrate.md`.
- **Autopilot-full.** Run independent PRs to merged with a swarm verdict on each. `playbooks/autopilot-full.md`.
- **Autopilot-stack.** Build and verify one linear stack for the operator to land. `playbooks/autopilot-stack.md`.
- **Session pickup.** Resume work from a transcript, cloud-agent URL, or branch. `playbooks/session-pickup.md`.
- **Pause safely.** Suspend in-flight work cleanly. `playbooks/pause-safely.md`.
- **Multi-phase plan.** Work spanning phases or stacked PRs. `playbooks/multi-phase-plan.md`.
- **Worktree cleanup.** Reclaim disk by pruning safe-to-remove worktrees or simulators. `playbooks/worktree-cleanup.md`.
- **Opening a PR.** Open a ready PR with ordered commits and a briefing-style body. `playbooks/opening-a-pr.md`.
