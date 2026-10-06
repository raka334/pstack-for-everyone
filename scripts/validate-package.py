#!/usr/bin/env python3
"""Check manifests, skill frontmatter, local links, and host adapter paths."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path.relative_to(ROOT)}: expected a JSON object")
        return {}
    return value


plugin = load_json(ROOT / "plugin.json")
if plugin.get("name") != "pstack":
    errors.append("plugin.json: plugin name must be pstack")
if plugin.get("license") != "MIT":
    errors.append("plugin.json: license must be MIT")
if plugin.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
    errors.append("plugin.json: must use the portable Agent Plugins schema")

claude_plugin = load_json(ROOT / ".claude-plugin" / "plugin.json")
claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
entries = claude_marketplace.get("plugins", [])
if claude_plugin.get("name") != "pstack":
    errors.append(".claude-plugin/plugin.json: plugin name must match pstack")
if not isinstance(entries, list) or not any(
    isinstance(entry, dict)
    and entry.get("name") == "pstack"
    and entry.get("source") == "./"
    for entry in entries
):
    errors.append(".claude-plugin/marketplace.json: missing pstack entry")

codex_marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
codex_entries = codex_marketplace.get("plugins", [])
if not isinstance(codex_entries, list) or not any(
    isinstance(entry, dict)
    and entry.get("name") == "pstack"
    and isinstance(entry.get("source"), dict)
    and entry["source"].get("path") == "./"
    for entry in codex_entries
):
    errors.append(".agents/plugins/marketplace.json: missing root pstack plugin")

package = load_json(ROOT / "package.json")
if package.get("name") != "dsh-pstack-for-everyone":
    errors.append("package.json: name must be dsh-pstack-for-everyone")
for path in ("README.md", "LICENSE", "plugin.json", ".claude-plugin/", ".agents/", "skills/", "dsh/cordis.patch.yml", "scripts/"):
    if path not in package.get("files", []):
        errors.append(f"package.json: files must include {path}")
if package.get("pi", {}).get("skills") != ["./skills"]:
    errors.append("package.json: Pi skills must point to the shared ./skills directory")
patch_path = package.get("dsh", {}).get("bundle", {}).get("patch")
if patch_path != "./dsh/cordis.patch.yml" or not (ROOT / "dsh" / "cordis.patch.yml").is_file():
    errors.append("package.json: DSH bundle must point to dsh/cordis.patch.yml")

skill_paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
if len(skill_paths) != 50:
    errors.append(f"skills/: expected the 50 pstack skills, found {len(skill_paths)}")
names: set[str] = set()
for path in skill_paths:
    content = path.read_text()
    match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n", content)
    if not match:
        errors.append(f"{path.relative_to(ROOT)}: expected name and description frontmatter")
        continue
    name, description_value = match.groups()
    try:
        description = json.loads(description_value)
    except json.JSONDecodeError:
        description = description_value
    if name != path.parent.name:
        errors.append(f"{path.relative_to(ROOT)}: name does not match its directory")
    if name in names:
        errors.append(f"{path.relative_to(ROOT)}: duplicate skill name {name}")
    names.add(name)
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{path.relative_to(ROOT)}: description must be non-empty")

skill_tokens = "|".join(re.escape(name) for name in sorted(names, key=len, reverse=True))
host_invocation = re.compile(rf"(?<![\w])\$(?:{skill_tokens})\b") if skill_tokens else None
markdown_files = [*([ROOT / "README.md"] if (ROOT / "README.md").is_file() else []), *ROOT.glob("skills/**/*.md")]
link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for source in markdown_files:
    content = source.read_text()
    if host_invocation and host_invocation.search(content):
        errors.append(f"{source.relative_to(ROOT)}: contains host-specific $skill invocation syntax")
    for raw_target in link_pattern.findall(content):
        target = raw_target.split()[0].strip("<>")
        if not target or target in {"url", "URL"} or target.startswith(("#", "mailto:")) or re.match(r"(?:[a-z]+:)?//", target, re.I):
            continue
        local_target = unquote(target.split("#", 1)[0])
        if local_target and not (source.parent / local_target).resolve().exists():
            errors.append(f"{source.relative_to(ROOT)}: broken local link {target}")

dsh_patch = ROOT / "dsh" / "cordis.patch.yml"
if dsh_patch.is_file():
    patch = dsh_patch.read_text()
    for marker in (
        "id: pstack-skills",
        "@deepseek-ai/dsh-skill-filesystem",
        "providerName: pstack-for-everyone",
        "includeDefaultRoots: false",
        "dsh-pstack-for-everyone/package.json",
        "'skills'",
    ):
        if marker not in patch:
            errors.append(f"dsh/cordis.patch.yml: missing {marker}")

readme = (ROOT / "README.md").read_text() if (ROOT / "README.md").is_file() else ""
for host in ("Cursor", "Codex", "Claude Code", "Pi", "OpenCode", "oh-my-pi", "DeepSeek Harness"):
    if host not in readme:
        errors.append(f"README.md: missing host support for {host}")
if "codex plugin add " in readme or "Plugins Directory" not in readme:
    errors.append("README.md: document Codex desktop installation after adding the marketplace")

if errors:
    print("Package validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(f"Valid pstack for Everyone package: {len(skill_paths)} shared skills")
