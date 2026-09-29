#!/usr/bin/env python3
"""Summarize one observed VASP batch without launching or changing any job."""
import argparse
import json
import math
from pathlib import Path


STATES = ('completed', 'converged', 'labels_parsed', 'collected')


def summarize(data):
    seconds = data['wall_seconds']
    if isinstance(seconds, bool) or not isinstance(seconds, (int, float)) or not math.isfinite(seconds) or seconds <= 0:
        raise ValueError('wall_seconds must be finite and positive')
    scope = data['scope']
    if scope not in ('short_batch', 'observed_window'):
        raise ValueError('scope must be short_batch or observed_window')
    jobs = data['jobs']
    if not isinstance(jobs, list):
        raise ValueError('jobs must be a list')
    seen = set()
    counts = dict.fromkeys(STATES, 0)
    unknown = dict.fromkeys(STATES, 0)
    confirmed = 0
    parsed_calculations = 0
    qualified = 0
    quality_unknown = 0
    for job in jobs:
        if not isinstance(job, dict):
            raise ValueError('Each job must be an object')
        identity = job['id']
        if not isinstance(identity, str) or not identity.strip() or identity in seen:
            raise ValueError('Every task needs a unique nonempty string id')
        seen.add(identity)
        for state in STATES:
            value = job.get(state)
            if value is not None and not isinstance(value, bool):
                raise ValueError(f'{identity}: {state} must be boolean or null')
            counts[state] += value is True
            unknown[state] += value is None
        confirmed += all(job.get(state) is True for state in STATES)
        parsed_calculations += all(job.get(state) is True for state in STATES[:3])
        quality = job.get('quality_passed')
        if quality is not None and not isinstance(quality, bool):
            raise ValueError(f'{identity}: quality_passed must be boolean or null')
        quality_unknown += quality is None
        qualified += quality is True and all(job.get(state) is True for state in STATES)
    result = {
        'configuration': data.get('configuration'),
        'scope': scope,
        'wall_seconds': seconds,
        'unique_tasks': len(seen),
        'state_counts': counts,
        'unknown_state_counts': unknown,
        'confirmed_collected_labels': confirmed,
        'confirmed_parsed_calculations': parsed_calculations,
        'parsed_calculations_per_hour': parsed_calculations * 3600 / seconds,
        'collected_labels_per_hour': confirmed * 3600 / seconds,
        'qualified_collected_labels': qualified,
        'quality_unknown_tasks': quality_unknown,
        'qualified_collected_labels_per_hour': qualified * 3600 / seconds,
        'rate_interpretation': 'short_batch_extrapolation' if scope == 'short_batch' else 'observed_window_average',
    }
    for name in ('sampled_peak_gpu_memory_mib', 'allocated_physical_cores'):
        value = data.get(name)
        if value is not None:
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise ValueError(f'{name} must be nonnegative or null')
        result[name] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=Path)
    args = parser.parse_args()
    try:
        result = summarize(json.loads(args.batch.read_text()))
    except (OSError, KeyError, TypeError, ValueError) as error:
        parser.exit(2, f'Invalid batch record: {error}\n')
    print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))


if __name__ == '__main__':
    main()
