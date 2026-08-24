import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

classes = ['API', 'Benign', 'Bruteforce', 'BufferOverflow', 'C2Beaconing', 'DDoS', 'DNS', 'DoS',
           'Evasion', 'Exfiltration', 'Exploitation', 'MITM', 'PortScan', 'Slowloris', 'TLSSSL', 'WebBased']
models = ['1D-CNN', 'LSTM', 'LightGBM', 'RandomForest', 'XGBoost']

data = np.array([
    [0.9567, 0.9251, 0.9979, 0.9979, 0.9982],
    [0.9615, 0.9507, 0.9835, 0.9843, 0.9844],
    [0.8227, 0.7962, 0.9314, 0.9379, 0.9388],
    [0.7340, 0.7678, 0.7280, 0.7692, 0.7672],
    [0.8051, 0.8207, 0.8808, 0.8854, 0.8858],
    [0.9059, 0.9455, 0.9978, 0.9995, 0.9985],
    [0.9773, 0.9548, 0.9999, 0.9999, 0.9999],
    [0.6957, 0.6670, 0.6902, 0.7178, 0.7275],
    [0.7419, 0.8366, 0.8822, 0.9088, 0.9091],
    [0.9966, 0.9895, 0.9999, 0.9998, 0.9999],
    [0.5326, 0.4089, 0.7590, 0.7637, 0.7651],
    [0.9016, 0.9154, 0.9986, 0.9993, 0.9984],
    [0.8355, 0.8572, 0.9865, 0.9932, 0.9894],
    [0.4683, 0.5895, 0.6898, 0.6523, 0.6475],
    [0.9586, 0.9519, 0.9825, 0.9838, 0.9827],
    [0.9480, 0.9191, 0.9955, 0.9942, 0.9946],
])

fig, ax = plt.subplots(figsize=(7.5, 10))
im = ax.imshow(data, cmap='RdYlGn', vmin=0.4, vmax=1.0, aspect='auto')

ax.set_xticks(np.arange(len(models)))
ax.set_xticklabels(models, fontsize=10, rotation=20, ha='right')
ax.set_yticks(np.arange(len(classes)))
ax.set_yticklabels(classes, fontsize=10)

for i in range(len(classes)):
    for j in range(len(models)):
        val = data[i, j]
        color = 'white' if val < 0.62 else 'black'
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', color=color, fontsize=8.3)

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('F1 Score', fontsize=10)

ax.set_title('Per-Class F1 Scores\n(TRUSTLab, Within-Dataset, 16 Classes × 5 Models)', fontsize=12, pad=12)
plt.tight_layout()
plt.savefig('/home/claude/figures_en/fig4_heatmap.png', dpi=300, bbox_inches='tight', facecolor='white')
print("saved fig4 (EN)")
