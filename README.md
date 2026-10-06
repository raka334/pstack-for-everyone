# pstack for Everyone

Portable pstack skills for Cursor, Codex, Claude Code, Pi, OpenCode, oh-my-pi, and DeepSeek Harness (DSH).

This repository packages one shared `skills/` directory with each host's native plugin or package metadata. It is not a Cursor-only plugin: the root [Agent Plugin manifest](plugin.json) is the portable format, and Cursor supports that format alongside its own plugin format. Host-specific metadata only handles installation and discovery; the skill content stays shared.

The 50 skills are adapted from the pstack collection in [cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack). The original skill copyright and MIT license are preserved. This multi-host package is maintained by [raka334](https://github.com/raka334); it is an independent adaptation, not an official Cursor or pstack release.

## Install

Use the matching host instructions. These commands install the plugin for that host; they do not change your settings for other agents.

### Cursor

Cursor supports the root Agent Plugin format used here. Install from a Cursor marketplace that includes this repository. To test a checkout locally, follow Cursor's [local plugin testing instructions](https://prod.cursor.com/docs/plugins#test-plugins-locally). Listing in Cursor's public marketplace requires submitting the plugin for review.

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

DSH loads the packaged `skills/` directory through its skill filesystem provider. Use a profile with DSH's standard skill registry and skill tool enabled. The bundle metadata and plugin patch are in `package.json` and `dsh/cordis.patch.yml`.

## Use

Ask your agent to use a skill by name, for example: “Use `poteto-mode` to implement this feature” or “Use `interrogate` to review this design.” Each host exposes skills through its own native interface, so exact invocation syntax varies.

Start with `poteto-mode` for engineering work and `poteto-help` when choosing a workflow. `setup-pstack` and its included TOML profiles are Codex-specific; they are optional and are not needed to use the shared skills on other hosts.

## Validate

```sh
python3 scripts/validate-package.py
```

This checks the host manifests, DSH bundle reference, skill metadata, README coverage, and local Markdown links. The DSH adapter is packaged against DSH's documented bundle interface; validate it in a DSH profile before using it in a live environment.

## Host documentation

- [Agent Plugins](https://agent-plugins.org/) and [Agent Skills](https://agentskills.io/specification)
- [Cursor plugins](https://prod.cursor.com/docs/plugins)
- [Codex plugins](https://developers.openai.com/plugins/build/plugins)
- [Claude Code plugins and marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Pi packages](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/packages.md)
- [OpenCode skills](https://opencode.ai/docs/skills/)
- [oh-my-pi plugin marketplaces](https://github.com/can1357/oh-my-pi/blob/main/docs/skills/authoring-marketplaces.md)
- [DeepSeek Harness plugin bundles](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/develop/basic/publish.md)
