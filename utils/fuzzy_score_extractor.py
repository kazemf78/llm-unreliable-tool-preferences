import os
import json
import csv
import re
import sys

# Get the parent directory of the current script
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add it to sys.path
sys.path.append(parent_dir)

import func_description_optim
from pathlib import Path

parent_dir = Path('../score/')
input_dirs = [p for p in parent_dir.iterdir() if p.is_dir()]
print(input_dirs)

# input_dirs = [
#     # '../score/gpt-4.1-2025-04-14-FC',
# ]

output_csv = 'aggregated_results_v2.csv'

# v1 filename pattern
# pattern = re.compile(
#     r'^(?P<version>BFCL_v\d+)_(?P<category>[^_]+_[^_]+)_dup(?P<duplication_times>\d+)_(?P<mode>[^_]+)_(?P<mode_args_str>\d+)_(?P<order>[^_]+_[^_]+)_score\.json$'
# )

# Matches both: with and without mode_args_str
# v2 filename pattern
# pattern = re.compile(
#     r'^(?P<version>BFCL_v\d+)_(?P<category>[^_]+(?:_[^_]+)?)_dup(?P<duplication_times>\d+)_(?P<mode>[a-zA-Z0-9]+)(?:_(?P<mode_args_str>\d+))?_(?P<order>[^_]+_[^_]+)_score\.json$'
# )

# v3 filename pattern
pattern = re.compile(
    r'^(?P<version>BFCL_v\d+)_'
    r'(?P<category>[^_]+_[^_]+_[^_]+_[^_]+)_'
    r'dup(?P<duplication_times>\d+)_'
    r'(?P<mode1>[a-zA-Z]+)_(?P<mode2>[a-zA-Z]+)_(?P<first_mode>[a-zA-Z]+)_first_score\.json$'
)

rows = []
for input_dir in input_dirs:
    model = os.path.basename(input_dir)

    for filename in sorted(os.listdir(input_dir)):
        if not filename.endswith('_score.json'):
            continue

        match = pattern.match(filename)
        if not match:
            print(f"Skipping unmatched file: {filename}")
            continue

        metadata = match.groupdict()
        metadata['mode'] = f"{metadata['mode1']}_{metadata['mode2']}"
        metadata['order'] = f"{metadata['first_mode']}_first"
        if metadata.get('mode_args_str') is None:
            metadata['mode_args_str'] = '-1'

        with open(os.path.join(input_dir, filename), 'r') as f:
            first_line = f.readline().strip()
            try:
                data = json.loads(first_line)
            except json.JSONDecodeError:
                print(f"Invalid JSON in {filename}")
                continue

        flat_data = {
            'accuracy': round(data.get('accuracy'), 3),
            'correct_count': data.get('correct_count'),
            'total_count': data.get('total_count'),
        }

        # Extract original dicts
        index_count = data.get('index_count', {})
        correct_index_count = data.get('index_count_of_correct_answers', {})
        dup_mode_count = data.get('dup_mode_count', {})

        # Invert correct_index_count and dup_mode_count to infer mapping
        inferred_map = {}

        for idx, count in correct_index_count.items():
            for mode, mode_count in dup_mode_count.items():
                if count == mode_count and idx not in inferred_map and mode not in inferred_map.values():  # and mode not in used_modes:
                    inferred_map[idx] = mode
                    # used_modes.add(mode)
                    break
            else:
                inferred_map[idx] = f"unknown_{idx}"

        # legacy code for v1 and v2
        # Now rename index_count and correct_index_count using inferred mapping
        # for idx, count in index_count.items():
        #     mode = inferred_map.get(idx, f"original")
        #     mode_to_write = "optimized" if mode.lower() != "original" else mode
        #     flat_data[f'index_count_{mode_to_write}'] = count

        # for idx, count in correct_index_count.items():
        #     mode = inferred_map.get(idx, f"unknown_{idx}")
        #     flat_data[f'index_count_of_correct_answers_{mode}'] = count

        # for mode, count in dup_mode_count.items():
        #     mode_to_write = "optimized" if mode.lower() != "original" else mode
        #     flat_data[f'dup_mode_count_{mode_to_write}'] = count
        #     flat_data[f'proportion_of_corrects_{mode_to_write}'] = round(count / flat_data['correct_count'], 2)

        # Ensure proportions are always output for both mode1 and mode2
        for idx, mode in enumerate([metadata['mode1'], metadata['mode2']]):
            count = dup_mode_count.get(mode, 0)
            flat_data[f'count_mode{idx + 1}'] = count
            flat_data[f'proportion_of_corrects_mode{idx + 1}'] = round(count / flat_data['correct_count'], 4)

        row = {**metadata, **flat_data}
        row['model'] = model  # attach model here
        rows.append(row)

# Determine all headers
# fieldnames = sorted(set(k for row in rows for k in row.keys()))

# Add prompt_suffix to each row
for row in rows:
    mode = row['mode']
    mode1 = mode.split('_')[0]
    if row['first_mode'] == mode1:
        row['first_count'] = row['count_mode1']
        row['first_proportion'] = row['proportion_of_corrects_mode1']
        row['second_count'] = row['count_mode2']
        row['second_proportion'] = row['proportion_of_corrects_mode2']
    else:
        row['first_count'] = row['count_mode2']
        row['first_proportion'] = row['proportion_of_corrects_mode2']
        row['second_count'] = row['count_mode1']
        row['second_proportion'] = row['proportion_of_corrects_mode1']
    try:
        idx = int(row['mode_args_str'])
        if row['mode'] == 'expertEndorsement':
            row['prompt_suffix'] = func_description_optim.suffix_variations_endorsement[idx]
        elif row['mode'] == 'socialProof':
            row['prompt_suffix'] = func_description_optim.suffix_variations_social_proof[idx]
        elif row['mode'] == 'naive':
            row['prompt_suffix'] = func_description_optim.suffix_variations_naive[idx]
        else:
            # fallback: just use the mode as a readable suffix for modes like "makeCasual", "addEmojis", etc.
            row['prompt_suffix'] = row['mode']
    except (ValueError, IndexError):
        row['prompt_suffix'] = 'INVALID_INDEX'
rows = [row for row in rows if "combined" in row['category']]

fieldnames = ['model', 'category',
              # 'dup_mode_count_optimized', 'dup_mode_count_original',
              'correct_count',
              # "proportion_of_corrects_optimized", "proportion_of_corrects_original",
              # 'index_count_optimized', 'index_count_original',
              'total_count', 'accuracy', 'order', 'mode',
              'mode_args_str', 'duplication_times', 'version',
              # "proportion_of_corrects_optimized", "proportion_of_corrects_original",
              'proportion_of_corrects_mode1', 'proportion_of_corrects_mode2',
              'count_mode1', 'count_mode2',
              'first_proportion', 'second_proportion',
              'first_count', 'second_count',
              'order', 'prompt_suffix']
# Write to CSV
rows = sorted(
    rows,
    key=lambda x: (x['category'], x['mode'], int(x['mode_args_str']), x['order']),
    # reverse=True,
)

# Drop unneeded keys before writing
for row in rows:
    row.pop('first_mode', None)
    row.pop('mode1', None)
    row.pop('mode2', None)

print(f"Number of rows for the result CSV: {len(rows)}")
# print(len(os.listdir(input_dir)))

with open(output_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV saved to: {output_csv}")
