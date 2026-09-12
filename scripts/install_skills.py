#!/usr/bin/env python3
"""Link selected repository skills into Codex, backing up only on explicit replacement."""
import argparse
import os
from pathlib import Path
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--all', action='store_true')
    group.add_argument('--skill', action='append', default=[])
    parser.add_argument('--replace', action='store_true', help='Back up conflicting entries before linking')
    parser.add_argument('--codex-home', type=Path, default=Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    sources = {p.parent.name: p.parent for p in root.glob('plugins/*/skills/*/SKILL.md')}
    names = set(sources) if args.all else set(args.skill)
    unknown = names - sources.keys()
    if unknown:
        parser.error('Unknown skills: ' + ', '.join(sorted(unknown)))
    if any(sources[n].parts[-3] == 'research-toolkit' for n in names):
        names.add('nature-shared')
    target = args.codex_home.expanduser().resolve() / 'skills'
    conflicts = [target/n for n in sorted(names) if (target/n).exists() or (target/n).is_symlink()]
    conflicts = [p for p in conflicts if not (p.is_symlink() and p.resolve() == sources[p.name])]
    if conflicts and not args.replace:
        parser.error('Existing entries; use --replace to back them up: ' + ', '.join(str(p) for p in conflicts))
    backup = target.parent / 'skill-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    target.mkdir(parents=True, exist_ok=True)
    for name in sorted(names):
        dest = target / name
        if dest.is_symlink() and dest.resolve() == sources[name]:
            print('Already linked:', name)
            continue
        moved = dest in conflicts
        if moved:
            backup.mkdir(parents=True, exist_ok=True)
            dest.rename(backup/name)
        try:
            dest.symlink_to(sources[name], target_is_directory=True)
        except OSError:
            if moved:
                (backup/name).rename(dest)
            raise
        print('Linked:', name)
    if conflicts:
        print('Previous entries backed up:', backup)

if __name__ == '__main__':
    main()
