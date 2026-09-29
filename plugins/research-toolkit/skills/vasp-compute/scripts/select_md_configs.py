#!/usr/bin/env python3
"""Select measured MD configurations within one matched comparison group."""
import argparse
import json
import math
from pathlib import Path


def select(records, min_speed_fraction=None):
    rows = []
    seen = set()
    for record in records:
        if record.get('valid') is not True:
            continue
        row = dict(record)
        identity = row['id']
        if identity in seen:
            raise ValueError(f'Duplicate configuration id: {identity}')
        seen.add(identity)
        n = row['trajectories']
        total = float(row['aggregate_ns_h'])
        if isinstance(n, bool) or not isinstance(n, int) or n < 1 or not math.isfinite(total) or total <= 0:
            raise ValueError(f'Invalid throughput or trajectory count: {identity}')
        row['per_trajectory_ns_h'] = total / n
        rows.append(row)
    if not rows:
        raise ValueError('No validated configuration in this comparison group')
    fastest = max(rows, key=lambda r: (r['per_trajectory_ns_h'], r['aggregate_ns_h']))
    throughput = max(rows, key=lambda r: (r['aggregate_ns_h'], r['per_trajectory_ns_h']))
    frontier = []
    for row in rows:
        dominated = any(
            other['per_trajectory_ns_h'] >= row['per_trajectory_ns_h']
            and other['aggregate_ns_h'] >= row['aggregate_ns_h']
            and (other['per_trajectory_ns_h'] > row['per_trajectory_ns_h']
                 or other['aggregate_ns_h'] > row['aggregate_ns_h'])
            for other in rows)
        if not dominated:
            row['single_speed_fraction'] = row['per_trajectory_ns_h'] / fastest['per_trajectory_ns_h']
            frontier.append(row)
    output = dict(fastest_trajectory=fastest, highest_throughput=throughput,
                  tradeoffs=sorted(frontier, key=lambda r: r['per_trajectory_ns_h'], reverse=True),
                  scope='Measured valid configurations only; caller must ensure matched workload/resources. Per-trajectory speed is a mean, not the slowest worker.')
    if min_speed_fraction is not None:
        if not 0 < min_speed_fraction <= 1:
            raise ValueError('min-speed-fraction must be in (0,1]')
        candidates = [r for r in rows if r['per_trajectory_ns_h'] >= min_speed_fraction * fastest['per_trajectory_ns_h']]
        output['balanced'] = max(candidates, key=lambda r: (r['aggregate_ns_h'], r['per_trajectory_ns_h']))
        output['explicit_min_speed_fraction'] = min_speed_fraction
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--min-speed-fraction', type=float)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    result = select(data['records'], args.min_speed_fraction)
    result['comparison'] = data.get('comparison')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
