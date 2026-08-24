import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

model_colors = {
    'RandomForest': '#2C5F8A', 'XGBoost': '#B5651D', 'LightGBM': '#3A7D44',
    '1D-CNN': '#8E44AD', 'LSTM': '#C0392B'
}
models_order = ['RandomForest', 'XGBoost', 'LightGBM', '1D-CNN', 'LSTM']
families_order = ['DDoS', 'DoS', 'Bruteforce', 'WebBased', 'PortScan']

data = {
    'DDoS': {
        'RandomForest': {'cic': (0.500578, 0.497892, 0.503214), 'cse': (0.642066, 0.641298, 0.642835)},
        'XGBoost':      {'cic': (0.506339, 0.503646, 0.508967), 'cse': (0.758513, 0.757886, 0.759158)},
        'LightGBM':     {'cic': (0.506347, 0.503638, 0.508976), 'cse': (0.758896, 0.758271, 0.759546)},
        '1D-CNN':       {'cic': (0.418912, 0.416253, 0.421436), 'cse': (0.682518, 0.681873, 0.683207)},
        'LSTM':         {'cic': (0.448442, 0.445791, 0.451100), 'cse': (0.707895, 0.707246, 0.708588)},
    },
    'DoS': {
        'RandomForest': {'cic': (0.454108, 0.452092, 0.455906), 'cse': (0.812406, 0.811706, 0.813088)},
        'XGBoost':      {'cic': (0.442625, 0.440657, 0.444485), 'cse': (0.786973, 0.786242, 0.787675)},
        'LightGBM':     {'cic': (0.432934, 0.430709, 0.434914), 'cse': (0.863330, 0.862674, 0.863941)},
        '1D-CNN':       {'cic': (0.000176, 0.000115, 0.000253), 'cse': (0.000000, 0.000000, 0.000000)},
        'LSTM':         {'cic': (0.455627, 0.453590, 0.457493), 'cse': (0.838017, 0.837332, 0.838644)},
    },
    'Bruteforce': {
        'RandomForest': {'cic': (0.051457, 0.047119, 0.056117), 'cse': (0.318694, 0.317170, 0.320275)},
        'XGBoost':      {'cic': (0.000000, 0.000000, 0.000000), 'cse': (0.000000, 0.000000, 0.000000)},
        'LightGBM':     {'cic': (0.000000, 0.000000, 0.000000), 'cse': (0.000000, 0.000000, 0.000000)},
        '1D-CNN':       {'cic': (0.000000, 0.000000, 0.000000), 'cse': (0.000000, 0.000000, 0.000000)},
        'LSTM':         {'cic': (0.000000, 0.000000, 0.000000), 'cse': (0.000000, 0.000000, 0.000000)},
    },
    'WebBased': {
        'RandomForest': {'cic': (0.000000, 0.000000, 0.000000), 'cse': (0.000048, 0.000000, 0.000111)},
        'XGBoost':      {'cic': (0.000000, 0.000000, 0.000000), 'cse': (0.000599, 0.000467, 0.000758)},
        'LightGBM':     {'cic': (0.000000, 0.000000, 0.000000), 'cse': (0.003520, 0.002873, 0.004265)},
        '1D-CNN':       {'cic': (0.000000, 0.000000, 0.000000), 'cse': (0.000000, 0.000000, 0.000000)},
        'LSTM':         {'cic': (0.037212, 0.032392, 0.041825), 'cse': (0.011555, 0.010143, 0.012961)},
    },
    'PortScan': {
        'RandomForest': {'cic': (0.614582, 0.612337, 0.616905), 'cse': None},
        'XGBoost':      {'cic': (0.000000, 0.000000, 0.000000), 'cse': None},
        'LightGBM':     {'cic': (0.000700, 0.000536, 0.000875), 'cse': None},
        '1D-CNN':       {'cic': (0.907555, 0.906543, 0.908484), 'cse': None},
        'LSTM':         {'cic': (0.903582, 0.902594, 0.904600), 'cse': None},
    },
}

def build_panel(ax, target_key, title):
    y_labels = []
    y_pos = []
    y = 0
    yticks_family = []
    for fam in families_order:
        fam_start = y
        for model in models_order:
            entry = data[fam][model].get(target_key)
            if entry is None:
                continue
            f1, lo, hi = entry
            color = model_colors[model]
            ax.errorbar(f1, y, xerr=[[f1-lo], [hi-f1]], fmt='o', color=color,
                        markersize=5, capsize=3, elinewidth=1.3, capthick=1.3)
            y_labels.append(model)
            y_pos.append(y)
            y -= 1
        yticks_family.append((fam, (fam_start + y + 1) / 2))
        y -= 0.6

    ax.set_yticks(y_pos)
    ax.set_yticklabels(y_labels, fontsize=7.5)
    ax.axvline(0.5, color='gray', linestyle=':', linewidth=0.9)
    ax.set_xlim(-0.02, 1.02)
    ax.set_xlabel('F1 Score (point estimate \u00b1 95% bootstrap CI)', fontsize=9.5)
    ax.set_title(title, fontsize=11.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for fam, ypos in yticks_family:
        ax.text(1.06, ypos, fam, fontsize=9.5, fontweight='bold', va='center', ha='left',
                 transform=ax.transData)

fig, axes = plt.subplots(1, 2, figsize=(13, 11))
build_panel(axes[0], 'cic', 'CICIDS2017 (5 families \u00d7 5 models = 25 points)')
build_panel(axes[1], 'cse', 'CSE-CIC-IDS2018 (4 families \u00d7 5 models = 20 points)')

from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color=c, label=m, linestyle='None', markersize=6)
                    for m, c in model_colors.items()]
fig.legend(handles=legend_elements, loc='lower center', ncol=5, fontsize=9.5, bbox_to_anchor=(0.5, -0.02), frameon=False)

fig.suptitle('Bootstrap 95% Confidence Intervals Across Five Attack Families (F1, 1,000 Resamples)', fontsize=13, y=1.01)
plt.tight_layout()
plt.savefig('/home/claude/figures_en/fig7_bootstrap_forest.png', dpi=300, bbox_inches='tight', facecolor='white')
print("saved fig7 (EN)")
