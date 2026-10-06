---
name: automate-me
description: "Create or improve a personal work-style skill from preferences and evidence in the current conversation or records the user supplies. Use for automate-me and requests to capture how the user works."
---

# Automate me

Create a small reusable skill from evidence, not assumptions. This workflow uses `skill-creator` and `unslop` when those skills are available.

## Steps

1. Inspect the current conversation, project instructions, and user-provided examples for repeated preferences, corrections, and workflows. Do not assume a private transcript path or scan other projects' history.
2. Summarize the evidence as observed facts. Separate stable preferences from task-specific constraints and unresolved questions.
3. Ask only about preferences that cannot be inferred from evidence and would materially change the skill.
4. Draft the skill at the path the user chooses. For a project skill, use `.agents/skills/<skill-name>/SKILL.md` when the host supports that convention. For a personal skill, use the active host's documented skills directory. Inspect existing files before replacing anything.
5. Use `skill-creator` to validate the structure and `unslop` to tighten the writing when available. Test direct, indirect, and negative activation examples.
6. Report which observed preferences were encoded, where the skill lives, and which claims remain unverified.
