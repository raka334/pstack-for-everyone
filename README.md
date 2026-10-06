# pstack for Everyone

50 pstack skills for inspecting code, designing changes, implementing features, and reviewing the result. Use them in Cursor, Codex, Claude Code, Pi, OpenCode, oh-my-pi, or DeepSeek Harness (DSH).

Each host loads the same [`skills/`](skills/) directory. The package includes native metadata for plugin, package, or skill discovery, so you can use pstack outside Cursor without maintaining a separate copy of its skills.

## Start here

1. Install using the instructions for your host below.
2. Open a project in that host.
3. Ask your agent to use a skill with a concrete task:

```text
Use poteto-mode to implement this feature. Inspect the existing code first.
Use architect to propose a design before making changes.
Use interrogate to review this design and identify weak assumptions.
```

Skill invocation syntax varies by host. Naming the skill in your request tells the agent which workflow you want. Start with [`poteto-help`](skills/poteto-help/SKILL.md) if you need help choosing one.

## Choose a skill

| What you need | Skill |
|---|---|
| A workflow for engineering work | [`poteto-mode`](skills/poteto-mode/SKILL.md) |
| A design with types, signatures, and responsibilities | [`architect`](skills/architect/SKILL.md) |
| An explanation of how code works | [`how`](skills/how/SKILL.md) |
| Evidence for why a decision was made | [`why`](skills/why/SKILL.md) |
| The effects of a change beyond its diff | [`blast-radius`](skills/blast-radius/SKILL.md) |
| An adversarial review of a design | [`interrogate`](skills/interrogate/SKILL.md) |
| A tests-first workflow when you request TDD | [`tdd`](skills/tdd/SKILL.md) |
| Clearer writing with less filler | [`unslop`](skills/unslop/SKILL.md) |

Browse [`skills/`](skills/) for the full collection. Skills guide the agent's work; the host supplies its tools, permissions, and delegation capabilities. Available behavior therefore depends on the host.

## Install

Choose your host below. Installation uses that host's plugin or skill system. Reading this README does not install anything or change an existing local installation.

### Cursor

Cursor supports the root [Agent Plugin manifest](plugin.json) used here. Install from a Cursor marketplace that includes this repository, or test a checkout using Cursor's [local plugin testing instructions](https://prod.cursor.com/docs/plugins#test-plugins-locally).

This repository does not imply a listing in Cursor's public marketplace. Public listings require Cursor's review.

### Codex

```sh
codex plugin marketplace add raka334/pstack-for-everyone
```

Restart the ChatGPT desktop app, open the Plugins Directory, select **pstack for Everyone**, then install **pstack**. The CLI adds the marketplace source; plugin installation happens in the desktop app.

### Claude Code

```sh
claude plugin marketplace add raka334/pstack-for-everyone
claude plugin install pstack@pstack-for-everyone
```

### Pi

```sh
pi install git:github.com/raka334/pstack-for-everyone
```

### OpenCode

```sh
npx skills add raka334/pstack-for-everyone --skill '*' --agent opencode
```

This installs the shared skills through the Skills CLI. It does not add an OpenCode runtime plugin.

### oh-my-pi

```sh
omp plugin marketplace add raka334/pstack-for-everyone
omp plugin install pstack@pstack-for-everyone
```

### DeepSeek Harness

Replace `web` with the DSH profile you want to configure:

```sh
dsh plugin --profile web add github:raka334/pstack-for-everyone
```

DSH loads the packaged `skills/` directory through its skill filesystem provider. Use a profile with DSH's standard skill registry and skill tool enabled. The bundle metadata and plugin patch are in [`package.json`](package.json) and [`dsh/cordis.patch.yml`](dsh/cordis.patch.yml).

The DSH adapter follows DSH's documented bundle interface. It has not been tested in a live DSH profile. Validate it in your target profile before relying on it.

## Optional Codex setup

[`setup-pstack`](skills/setup-pstack/SKILL.md) and its included TOML profiles configure Codex-specific routing. Use them only when you want that configuration. Other hosts can use the shared skills without these profiles.

## Validate a checkout

Run from the repository root:

```sh
python3 scripts/validate-package.py
```

This checks the host manifests, DSH bundle reference, skill metadata, README coverage, and local Markdown links. It validates the package structure; it does not run each host or prove that every skill works with its tools.

## Attribution and license

This collection is adapted from [pstack in cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack). The original skill copyright and [MIT license](LICENSE) are preserved.

[raka334](https://github.com/raka334) maintains this multi-host package. It is an independent adaptation, not an official Cursor or upstream pstack release.

## Host documentation

- [Agent Plugins](https://agent-plugins.org/) and [Agent Skills](https://agentskills.io/specification)
- [Cursor plugins](https://prod.cursor.com/docs/plugins)
- [Codex plugins](https://developers.openai.com/plugins/build/plugins)
- [Claude Code plugins and marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Pi packages](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/packages.md)
- [OpenCode skills](https://opencode.ai/docs/skills/)
- [oh-my-pi plugin marketplaces](https://github.com/can1357/oh-my-pi/blob/main/docs/skills/authoring-marketplaces.md)
- [DeepSeek Harness plugin bundles](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/develop/basic/publish.md)
