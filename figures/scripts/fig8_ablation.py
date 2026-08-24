import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

feature_counts = [5, 10, 51]
models = ['RandomForest', 'XGBoost', 'LightGBM', '1D-CNN', 'LSTM']
colors = ['#2C5F8A', '#B5651D', '#3A7D44', '#8E44AD', '#C0392B']

cic_mean = {
    'RandomForest': [0.584, 0.514, 0.649],
    'XGBoost': [0.636, 0.580, 0.603],
    'LightGBM': [0.664, 0.589, 0.582],
    '1D-CNN': [0.424, 0.664, 0.591],
    'LSTM': [0.529, 0.674, 0.433],
}
cic_std = {
    'RandomForest': [0.003, 0.011, 0.009],
    'XGBoost': [0.003, 0.027, 0.039],
    'LightGBM': [0.014, 0.034, 0.031],
    '1D-CNN': [0.147, 0.029, 0.073],
    'LSTM': [0.021, 0.045, 0.118],
}
cse_mean = {
    'RandomForest': [0.514, 0.503, 0.665],
    'XGBoost': [0.405, 0.520, 0.435],
    'LightGBM': [0.508, 0.586, 0.531],
    '1D-CNN': [0.497, 0.563, 0.732],
    'LSTM': [0.305, 0.503, 0.574],
}
cse_std = {
    'RandomForest': [0.019, 0.019, 0.035],
    'XGBoost': [0.024, 0.019, 0.015],
    'LightGBM': [0.024, 0.016, 0.017],
    '1D-CNN': [0.133, 0.020, 0.055],
    'LSTM': [0.085, 0.071, 0.113],
}

fig, axes = plt.subplots(1, 2, figsize=(13, 5.8))

for ax, mean_d, std_d, title in [(axes[0], cic_mean, cic_std, 'CICIDS2017'), (axes[1], cse_mean, cse_std, 'CSE-CIC-IDS2018')]:
    for i, m in enumerate(models):
        means = np.array(mean_d[m])
        stds = np.array(std_d[m])
        ax.errorbar(feature_counts, means, yerr=stds, marker='o', label=m, color=colors[i],
                     linewidth=1.8, markersize=6, capsize=4, elinewidth=1.2)
    avg_mean = np.mean([mean_d[m] for m in models], axis=0)
    ax.plot(feature_counts, avg_mean, marker='s', label='Mean', color='black',
            linewidth=2.8, markersize=8, linestyle='--')
    ax.axhline(0.5, color='gray', linestyle=':', linewidth=1)
    ax.set_xlabel('Number of Features', fontsize=10.5)
    ax.set_ylabel('Cross-Dataset ROC-AUC (mean \u00b1 std, n=3 seeds)', fontsize=9.5)
    ax.set_title(title, fontsize=11.5)
    ax.set_xticks(feature_counts)
    ax.set_ylim(0.2, 0.85)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

axes[1].legend(loc='upper center', bbox_to_anchor=(-0.15, -0.15), ncol=3, fontsize=8.5, frameon=False)
fig.suptitle('Feature Count Ablation: 5 \u2192 10 \u2192 51 Features\n(Mean \u00b1 Standard Deviation Across 3 Seeds)', fontsize=12.5, y=1.03)
plt.tight_layout()
plt.savefig('/home/claude/figures_en/fig8_ablation.png', dpi=300, bbox_inches='tight', facecolor='white')
print("saved fig8 (EN)")
