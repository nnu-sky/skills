#!/usr/bin/env python3
"""Read VASP OUTCAR timing evidence; no job launch or label acceptance."""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import statistics

NUMBER = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[EeDd][-+]?\d+)?"
TIMING = re.compile(r"^\s*([A-Z0-9][A-Z0-9_+\-]*):\s+cpu time\s+(" + NUMBER +
                    r"):\s+real time\s+(" + NUMBER + r")", re.M)


def number(text):
    return float(text.replace('D', 'E').replace('d', 'e'))


def inspect(path):
    raw = path.read_text(errors='replace')
    headers = re.findall(r'^\s*vasp\.\d+[^\n]*', raw, re.M)
    if len(headers) != 1:
        raise ValueError('Expected one VASP run per OUTCAR; missing or repeated VASP header')
    times = defaultdict(list)
    for label, _, seconds in TIMING.findall(raw):
        times[label].append(number(seconds))
    elapsed = re.findall(r'Elapsed time \(sec\):\s*(' + NUMBER + ')', raw)
    steps = re.findall(r'Iteration\s+(\d+)\(\s*(\d+)\)', raw)
    iterations = defaultdict(int)
    for ionic, electronic in steps:
        iterations[ionic] = max(iterations[ionic], int(electronic))
    parameters = {}
    for tag in ('NIONS', 'NBANDS', 'NKPTS', 'ISPIN', 'NSIM', 'NELM', 'NSW', 'IBRION', 'ISIF', 'IALGO'):
        found = re.search(r'\b' + tag + r'\s*=\s*(-?\d+)', raw)
        parameters[tag] = int(found[1]) if found else None
    for tag in ('ENCUT', 'EDIFF'):
        found = re.search(r'\b' + tag + r'\s*=\s*(' + NUMBER + ')', raw)
        parameters[tag] = number(found[1]) if found else None
    warnings = []
    footer = 'General timing and accounting informations' in raw
    if not footer:
        warnings.append('No timing footer: output may still be running or truncated.')
    loops = times.get('LOOP', [])
    wall = number(elapsed[-1]) if elapsed else None
    return {
        'outcar': str(path.resolve()), 'version_header': headers[0].strip(),
        'parameters': parameters, 'timing_footer_present': footer,
        'vasp_elapsed_seconds': wall,
        'electronic_loop_records': len(loops),
        'electronic_iterations_by_ionic_step': dict(iterations),
        'ediff_reached_markers': raw.count('aborting loop because EDIFF is reached'),
        'ionic_accuracy_marker': 'reached required accuracy' in raw,
        'timers_seconds': {label: {'count': len(values), 'sum': sum(values),
                                 'median': statistics.median(values)}
                          for label, values in sorted(times.items())},
        'elapsed_minus_electronic_loops_seconds': wall - sum(loops) if wall is not None and loops else None,
        'warnings': warnings,
        'interpretation': 'Timers overlap hierarchically: do not sum LOOP, LOOP+ and inner timers. '
                          'Elapsed minus LOOP is unclassified overhead, not measured I/O. '
                          'SCF markers and footer alone do not certify every ionic step, labels or collection.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('outcar', type=Path, nargs='+')
    args = parser.parse_args()
    try:
        result = [inspect(path) for path in args.outcar]
    except (OSError, ValueError) as error:
        parser.exit(2, f'Cannot inspect OUTCAR: {error}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
