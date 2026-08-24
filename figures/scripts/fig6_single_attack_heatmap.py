import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

families = ['DDoS', 'DoS', 'Bruteforce', 'WebBased', 'PortScan']
families_cse = ['DDoS', 'DoS', 'Bruteforce', 'WebBased']
models = ['RandomForest', 'XGBoost', 'LightGBM', '1D-CNN', 'LSTM']

cic_data = np.array([
    [0.500578, 0.506339, 0.506347, 0.000000, 0.000000],
    [0.454108, 0.442625, 0.432934, 0.000000, 0.481557],
    [0.051457, 0.000000, 0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000, 0.000000, 0.029167],
    [0.614582, 0.000000, 0.000700, 0.908815, 0.895777],
])

cse_data = np.array([
    [0.642066, 0.758513, 0.758896, 0.000000, 0.000000],
    [0.812406, 0.786973, 0.863330, 0.000000, 0.829263],
    [0.318694, 0.000000, 0.000000, 0.000000, 0.000000],
    [0.000048, 0.000599, 0.003520, 0.000000, 0.062557],
])

fig, axes = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [5, 4]})

for ax, data, fams, title in [(axes[0], cic_data, families, 'CICIDS2017 (5 families)'),
                                (axes[1], cse_data, families_cse, 'CSE-CIC-IDS2018 (4 families, no PortScan)')]:
    im = ax.imshow(data, cmap='RdYlGn', vmin=0, vmax=1.0, aspect='auto')
    ax.set_xticks(np.arange(len(models)))
    ax.set_xticklabels(models, fontsize=9, rotation=25, ha='right')
    ax.set_yticks(np.arange(len(fams)))
    ax.set_yticklabels(fams, fontsize=10)
    for i in range(len(fams)):
        for j in range(len(models)):
            val = data[i, j]
            color = 'white' if val < 0.35 else 'black'
            ax.text(j, i, f'{val:.2f}', ha='center', va='center', color=color, fontsize=9)
    ax.set_title(title, fontsize=11)

cbar = fig.colorbar(im, ax=axes, fraction=0.03, pad=0.03)
cbar.set_label('F1 Score (Cross-Dataset)', fontsize=10)

fig.suptitle('Cross-Dataset F1 Scores at the Single-Attack Level (TRUSTLab \u2192 Target)', fontsize=13, y=1.02)
plt.savefig('/home/claude/figures_en/fig6_single_attack_heatmap.png', dpi=300, bbox_inches='tight', facecolor='white')
print("saved fig6 (EN)")
