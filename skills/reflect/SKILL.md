---
name: reflect
description: "Review a completed task or supplied transcript for reusable lessons, then route each lesson to a concrete skill edit. Use when the user asks to reflect on the work."
---

# Reflect

Capture lessons that change future agent behavior. Do not invent a transcript path. Use the current conversation and task artifacts, or a transcript the user provides.

## Steps

1. Identify the completed task and its evidence. If the active conversation does not contain enough context, ask for a transcript or relevant artifacts.
2. Extract concrete decisions, mistakes, corrections, and successful practices. Separate observed events from interpretation.
3. If the host supports agent delegation, ask independent reviewers to inspect distinct parts of the evidence using the templates in `references/`. Otherwise do separate passes yourself. Reviewers report only; they do not edit files.
4. Map each accepted lesson to an existing skill and propose the smallest edit that would prevent a repeat. Do not create a new rule for a one-off preference.
5. Apply edits only when the user asked you to update skills. Otherwise return proposed diffs and evidence.
6. Run the relevant skill validation after changes and summarize accepted and rejected lessons.
