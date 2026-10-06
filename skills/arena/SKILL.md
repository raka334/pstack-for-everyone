---
name: arena
description: "Run parallel agent attempts at the same task, choose a base, graft the strongest ideas from the others, and verify the synthesis. Use when the host supports delegation and the artifact has competing approaches."
---

# Arena

Run independent attempts at the same task, read every candidate, select a base using explicit criteria, graft only the best ideas, then verify the result.

## Start

Create a checklist with one entry per phase: Frame, Fan out, Cross-judge, Pick, Graft, Verify.

## Phase A: Frame

1. State the artifact each candidate is producing.
2. Derive three to six concrete success criteria. Candidates receive the same task and do not see the picker rubric unless it is part of the task.
3. Choose the number of candidates. If the host supports configured profiles with different model settings, use them for model diversity. If they all inherit the same parent model, say so. Do not invent model IDs or assume per-call model routing.
4. Give each candidate a separate output path or worktree. Candidates must not edit the same files concurrently.

## Phase B: Fan out

Ask the active host to give the same complete brief to each candidate. Each returns the artifact and a short rationale naming the alternatives considered and rejected. Start independent attempts together when supported; otherwise run them sequentially and disclose it. If the host has no delegation support, use separate reasoning passes and say they were not independent agents.

## Phase C: Cross-judge

Wait until every candidate has stopped writing. If a separate read-only judge is available, give it the rubric and candidate paths. A judge using the same model adds an independent review, not model diversity. Do not ask the judge to edit files.

## Phase D: Pick a base

Read every candidate end to end. Score each criterion separately and compare that score with the cross-judge. Resolve disagreement by rereading the artifacts and the rubric. Pick the base that a future maintainer can extend most easily.

Record the base and reason in a short synthesis note alongside the output.

## Phase E: Graft

Walk each losing candidate once more. Port only the strongest ideas into the base and record what was grafted and what was rejected. When all candidates converge, record the agreement and skip grafting. When candidates diverge because the brief was unclear, reframe and rerun.

## Phase F: Verify

Verify the synthesized artifact against the same criteria. If it fails, reframe and rerun or return to grafting. Do not paper over a failed criterion.

## Outputs

Return one synthesized artifact and one short synthesis note with the base, grafts, rejections, dropouts, and verification result.
