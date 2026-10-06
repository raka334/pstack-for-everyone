---
name: swarm
description: "Coordinate agents across independent slices, repeated attempts, or coverage checks, then return one evidence-based report. Use when the host supports delegation and the work benefits from parallel coverage."
---

# Swarm

Use the host's native agent delegation to cover independent slices. The parent owns the task, drains every required result, checks the evidence, and returns one report.

## Start

Create a checklist with one entry per phase.

1. Frame.
2. Fan out.
3. Aggregate.
4. Report.

## Phase A: Frame

1. State the done predicate and artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race identical briefs, or mix both. For a race, declare `first pass`, `rank all`, or `best-of` before starting.
3. Set the number of workers from the user request or the size of the work. The host's configured concurrency limit may require batches.
4. Give each worker a bounded brief with goal, exact scope, evidence required, and verification condition. Give separate writable files or worktrees when parallel workers edit.
5. If candidates need different models, use installed host profiles with distinct configured models. Otherwise state that the run has no model diversity.

## Phase B: Fan out

Delegate workers through the host's native agent capability. Start independent workers together when supported. Each report must include `PASS`, `ISSUES`, or `BLOCKED`, with evidence and any exact files changed.

If the host has no available agent capacity, work through the slices sequentially and report that fan-out was unavailable. If a worker drops out, continue with completed work and note the gap.

## Phase C: Aggregate

Read terminal results and inspect any changed files yourself. Reject reports that omit required evidence. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Keep a compact results table, evidenced issues, and explicit gaps.

## Phase D: Report

Return one consolidated report with the result table, issue one-liners, gaps or dropouts, and the declared race rule when used. Do not paste raw worker dumps.
