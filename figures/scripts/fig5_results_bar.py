import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

models = ['Random\nForest', 'XGBoost', 'LightGBM', '1D-CNN', 'LSTM']
indomain_mean = [0.9991, 0.9992, 0.9989, 0.9866, 0.9884]
indomain_std  = [0.0000, 0.0000, 0.0000, 0.0065, 0.0010]
cicids_mean = [0.649, 0.603, 0.582, 0.619, 0.531]
cicids_std  = [0.009, 0.039, 0.031, 0.087, 0.085]
csecic_mean = [0.665, 0.435, 0.531, 0.738, 0.642]
csecic_std  = [0.035, 0.015, 0.017, 0.054, 0.071]

x = np.arange(len(models))
width = 0.26

fig, ax = plt.subplots(figsize=(9.5, 5.8))
b1 = ax.bar(x - width, indomain_mean, width, yerr=indomain_std, capsize=3,
            label='Within-dataset (TRUSTLab)', color='#3A7D44', error_kw={'linewidth': 1.2, 'ecolor': '#1a1a1a'})
b2 = ax.bar(x, cicids_mean, width, yerr=cicids_std, capsize=3,
            label='Cross-dataset: CICIDS2017', color='#B5651D', error_kw={'linewidth': 1.2, 'ecolor': '#1a1a1a'})
b3 = ax.bar(x + width, csecic_mean, width, yerr=csecic_std, capsize=3,
            label='Cross-dataset: CSE-CIC-IDS2018', color='#2C5F8A', error_kw={'linewidth': 1.2, 'ecolor': '#1a1a1a'})

ax.axhline(0.5, color='gray', linestyle='--', linewidth=1, label='Random-guess boundary (AUC=0.5)')

ax.set_ylabel('ROC-AUC (mean ± std, n=3 seeds)', fontsize=10.5)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=10)
ax.set_ylim(0, 1.12)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=9, frameon=False)
ax.set_title('Within-Dataset and Cross-Dataset ROC-AUC Comparison\n(51 Features, Mean ± Standard Deviation Across 3 Seeds)', fontsize=11.5, pad=12)

for bars, means in [(b1, indomain_mean), (b2, cicids_mean), (b3, csecic_mean)]:
    for bar, m in zip(bars, means):
        h = bar.get_height()
        ax.annotate(f'{m:.2f}', xy=(bar.get_x() + bar.get_width()/2, h),
                     xytext=(0, 8), textcoords='offset points', ha='center', fontsize=7.3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('/home/claude/figures_en/fig5_results_bar.png', dpi=300, bbox_inches='tight', facecolor='white')
print("saved fig5 (EN)")
