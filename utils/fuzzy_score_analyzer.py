import pandas as pd
from collections import defaultdict
from statsmodels.stats.proportion import proportions_ztest

P_VALUE_CUTOFF = 0.01

# === Specify your input CSVs from different models ===
input_csvs = [
    "aggregated_results_v2.csv",
    # "aggregated_results_gpt-4o-mini.csv"
]

# === Load and combine all input CSVs ===
df_list = [pd.read_csv(path) for path in input_csvs]
df = pd.concat(df_list, ignore_index=True)

# === Extract mode1 and mode2 from 'mode' column ===
df[['mode1', 'mode2']] = df['mode'].str.split('_', expand=True)

# === Group by model ===
grouped = df.groupby('model')

all_results = []

for model_name, model_df in grouped:
    print(f"📊 Analyzing model: {model_name}")

    mode_pair_stats = defaultdict(lambda: {'count': 0, 'modes': defaultdict(int)})

    for _, row in model_df.iterrows():
        m1, m2 = row['mode1'], row['mode2']
        key = frozenset([m1, m2])

        c1 = int(row['count_mode1'])
        c2 = int(row['count_mode2'])

        mode_pair_stats[key]['count'] += 1
        mode_pair_stats[key]['modes'][m1] += c1
        mode_pair_stats[key]['modes'][m2] += c2

    # Build long-format rows
    records = []
    for pair, stats in mode_pair_stats.items():
        m1, m2 = sorted(pair)  # consistent order
        c1 = stats['modes'][m1]
        c2 = stats['modes'][m2]

        # Assume the number of trials is the same for both (or proportional to count)
        # If each count is out of N, then nobs = [N1, N2]; here we assume N1 + N2 = c1 + c2
        successes = [c1, c2]
        nobs = [c1 + c2, c1 + c2]  # fallback: assume same base (if unknown) and counts represent opportunities

        # You can alternatively use actual total counts if available (e.g., c1_trials, c2_trials)
        try:
            stat, pval = proportions_ztest(successes, nobs)
        except Exception as e:
            stat, pval = float('nan'), float('nan')

        # winner only if significant
        if pval < P_VALUE_CUTOFF:
            winner = m1 if c1 > c2 else m2
        else:
            winner = 'tie'

        ratio = round(max(c1, c2) / min(c1, c2), 2) if min(c1, c2) > 0 else float('inf')
        proportions = f'{c1 / (c1 + c2):.2%} vs {c2 / (c1 + c2):.2%}'
        # append results
        records.append({
            'model': model_name,
            'mode_1': m1,
            'count_1': c1,
            'mode_2': m2,
            'count_2': c2,
            'total_pairs': stats['count'],
            'winner': winner,
            'ratio': ratio,
            'proportions': proportions,
            # 'z_stat': stat,
            'p_value': pval,
            'significant': pval < P_VALUE_CUTOFF
        })

    # Create and sort DataFrame
    results_df = pd.DataFrame(records)
    results_df['has_original'] = results_df['mode_1'].str.contains('original') | results_df['mode_2'].str.contains(
        'original')
    results_df = results_df.sort_values(by=['has_original', 'ratio'], ascending=[False, False])
    results_df = results_df.drop(columns='has_original')
    results_df['p_value'] = results_df['p_value'].apply(
        lambda x: f"{float(x):.2e}" if pd.notnull(x) and x != '' else ""
    )

    # Save or append
    output_path = f"mode_effectiveness_{model_name}_v2.csv"
    results_df.to_csv(output_path, index=False, float_format="%.3f")
    print(f"✅ Saved: {output_path}")

    all_results.append(results_df)

# Optional: concatenate all for display or aggregate view
combined = pd.concat(all_results, ignore_index=True)
results_df = combined.copy()
results_df['has_original'] = results_df['mode_1'].str.contains('original') | results_df['mode_2'].str.contains(
    'original')
results_df = results_df.sort_values(by=['has_original', 'ratio'], ascending=[False, False])
results_df = results_df.drop(columns='has_original')
results_df['p_value'] = results_df['p_value'].apply(
    lambda x: f"{float(x):.2e}" if pd.notnull(x) and x != '' else ""
)
print("\n🧾 Sample of combined results:")
print(results_df.head(10))
results_df.to_csv(f"mode_effectiveness_across_all_v2.csv", index=False, float_format="%.3f")

