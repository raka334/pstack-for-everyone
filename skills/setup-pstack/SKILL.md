---
name: setup-pstack
description: "Install pstack's optional Codex agent profile templates in project or personal configuration. Use only when configuring pstack agent profiles in Codex."
---

# Setup pstack for Codex

Codex plugins package skills, while custom agents are configured separately as TOML files. This workflow installs the included profiles into Codex's project `.codex/agents/` directory or personal `~/.codex/agents/` directory. The templates inherit the parent model and reasoning effort. Do not guess a model ID or overwrite an existing profile without showing the difference and getting the user's choice.

## Steps

1. Read the templates in `references/agents/`. They define `poteto-agent`, `pstack-explorer`, and `comment-sicko`.
2. Choose the target scope. Use project `.codex/agents/` when the profiles should apply only to the current repository. Use personal `~/.codex/agents/` when they should apply across projects. If the user's intent is not clear, ask once.
3. Inspect existing target files before writing. Preserve any user-chosen `model`, `model_reasoning_effort`, sandbox, MCP, or skills settings. If a file already exists, propose a minimal merge and wait for the user's approval before replacing it.
4. For each missing profile, copy the template. Explain that model and reasoning effort inherit from the parent. The user can add supported `model` and `model_reasoning_effort` settings to a profile later.
5. Verify the TOML parses, each profile has `name`, `description`, and `developer_instructions`, and Codex can discover the target directory. Report exact paths changed.
6. Offer `create-verification-skill` only when the project has no way to drive its real app and the user is working on a product repository.

If filesystem access prevents writing personal configuration, leave the files ready in project `.codex/agents/` only with the user's agreement, or provide the patch for manual installation. These templates target Codex and do not configure other hosts.
