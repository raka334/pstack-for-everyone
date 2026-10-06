---
name: why
description: "Trace the evidence behind an architectural choice, regression, postmortem, or measured threshold. Use for why-do-we-do-this and why-did-we-pick-that questions. Use how for runtime behavior."
---

# Why

Build a cited account of the decision and its tradeoffs. Search available evidence; do not assume an issue tracker, chat service, or observability MCP is connected.

## Step 1. Identify the decision

Use the user's stated subject. If it is vague, infer the likely referent from the current conversation and working tree, then state that interpretation. Ask only if multiple materially different decisions remain plausible.

## Step 2. Collect evidence

Inspect the relevant code, tests, docs, and repository history. Use connected tools only when they are visible in the current session and relevant to the decision. Potential evidence sources include source control, tickets, long-form docs, chat, infrastructure observability, error tracking, and analytics.

For a broad question, delegate distinct evidence categories to read-only agents when the host supports delegation. Give each the exact question and ask for source links, file and line references, dates, and uncertainty. If delegation is unavailable, inspect evidence categories sequentially. Never claim to have searched a system that is not connected.

## Step 3. Reconstruct the rationale

Separate original intent from what the implementation now does. Identify the problem, constraints, alternatives, chosen tradeoff, later changes, and whether the original evidence still applies. Treat comments and old decisions as leads, not proof.

## Step 4. Report

Return the answer with citations next to each claim. Include a short Sources Consulted list. Label inferences. If the question precedes a code change, turn the lineage into Preserve, Change, Avoid, and Risk constraints for the planning skill.
