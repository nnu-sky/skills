#!/usr/bin/env python3
"""Validate portable skill entrypoints, manifests and concrete relative Markdown links."""
import json
import re
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
errors = []
market = json.loads((root/'.agents/plugins/marketplace.json').read_text())
count = 0
for entry in market['plugins']:
    plugin = root/entry['source']['path']
    manifest = json.loads((plugin/'.codex-plugin/plugin.json').read_text())
    if manifest['name'] != entry['name'] or not manifest.get('version'):
        errors.append(f'Invalid plugin identity: {plugin}')
    for p in (plugin/'skills').glob('*/SKILL.md'):
        count += 1
        text = p.read_text()
        parts = text.split('---', 2)
        if len(parts) != 3:
            errors.append(f'Missing frontmatter: {p}')
            continue
        front = yaml.safe_load(parts[1])
        if front.get('name') != p.parent.name or not front.get('description'):
            errors.append(f'Invalid skill metadata: {p}')
        ui = p.parent/'agents/openai.yaml'
        if ui.exists():
            data = yaml.safe_load(ui.read_text())
            if not isinstance(data, dict): errors.append(f'Invalid UI metadata: {ui}')
        routing = p.parent/'manifest.yaml'
        if routing.exists():
            data = yaml.safe_load(routing.read_text())
            for relative in data.get('always_load', []):
                if not (p.parent/relative).exists(): errors.append(f'Missing core: {routing}: {relative}')
for p in root.rglob('*.md'):
    for dest in re.findall(r'\]\(([^)]+)\)', p.read_text(errors='replace')):
        dest = dest.split('#')[0].strip('<>')
        if not dest or '://' in dest or dest.startswith(('mailto:', '#', '<')) or ' ' in dest:
            continue
        if not (p.parent/dest).exists(): errors.append(f'Missing link: {p.relative_to(root)} -> {dest}')
for p in root.rglob('*'):
    if '.git' in p.parts: continue
    if p.is_file() and (p.suffix == '.pyc' or '__pycache__' in p.parts): errors.append(f'Cache in distribution: {p}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Validated {len(market["plugins"])} plugins, {count} skills, core resources and Markdown links')
