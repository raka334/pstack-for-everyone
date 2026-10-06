---
name: poteto-help
description: "Help a user install and use pstack for Everyone or choose a skill, playbook, or principle. Use for pstack questions. For requests to do work, use poteto-mode and do the work."
---

# Pstack help

Answer the user's pstack question from this package and its README. Read the relevant skill page before making detailed claims. Do not route a request for work into a help-only answer.

## Start here

- Use `poteto-mode` for non-trivial engineering work.
- Use `setup-pstack` only to install the optional Codex custom agent profiles.
- Use `poteto-help` when the user is unsure which workflow applies.
- Select a named skill through the active host's native skill command or ask the host to use it by name.

## Host support

The README documents install commands and native invocation for Cursor, Codex, Claude Code, Pi, OpenCode, oh-my-pi, and DeepSeek Harness. Agent delegation, commands, and profile configuration vary by host. Use only capabilities that the active host exposes.

The included `setup-pstack` skill and its TOML templates configure Codex-specific agent profiles. Other hosts use their own agent configuration.

The Cursor-hosted `make-bot-ui` automation workflow is not included in this package.

## Skill map

Read the linked `SKILL.md` before explaining a workflow. The main entry point is [`poteto-mode`](../poteto-mode/SKILL.md). Use [`how`](../how/SKILL.md) for implementation walkthroughs, [`why`](../why/SKILL.md) for decision evidence, [`architect`](../architect/SKILL.md) before a boundary-crossing design, [`interrogate`](../interrogate/SKILL.md) for adversarial review, and [`swarm`](../swarm/SKILL.md) or [`arena`](../arena/SKILL.md) when the host supports useful parallel work.
