import matplotlib.pyplot as plt
import numpy as np
import re

plt.rcParams['font.family'] = 'DejaVu Sans'

# Parse Table 4 from the Turkish source document (data is language-independent)
with open('/mnt/user-data/outputs/TRUSTLab_Makale_Taslak_TR.md') as f:
    text = f.read()

start = text.find('**Tablo 4.**')
end = text.find('¹ Şiddet eşikleri')
table_text = text[start:end]

rows = []
for line in table_text.split('\n'):
    m = re.match(r'\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*([\d,]+)\s*\|\s*(\S+)\s*\|\s*(.+?)\s*\|', line)
    if m:
        idx, feat, ks_str, sev, status = m.groups()
        ks = float(ks_str.replace(',', '.'))
        is_active_idle = 'Active/Idle' in status
        rows.append((int(idx), feat, ks, is_active_idle))

print(f"Parsed {len(rows)} features")
rows.sort(key=lambda x: x[0])

features = [r[1] for r in rows]
ks_values = [r[2] for r in rows]
colors = ['#C0392B' if r[3] else '#2C5F8A' for r in rows]

fig, ax = plt.subplots(figsize=(9, 13))
y_pos = np.arange(len(features))
ax.barh(y_pos, ks_values, color=colors, height=0.7)
ax.set_yticks(y_pos)
ax.set_yticklabels(features, fontsize=7.5)
ax.invert_yaxis()
ax.set_xlabel('Kolmogorov-Smirnov Statistic (D)', fontsize=10.5)
ax.axvline(0.1, color='gray', linestyle=':', linewidth=0.8)
ax.axvline(0.3, color='gray', linestyle=':', linewidth=0.8)
ax.axvline(0.6, color='gray', linestyle=':', linewidth=0.8)
ax.set_title('TRUSTLab-CICIDS2017 Per-Feature KS Statistic (59 Features)', fontsize=12)

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#C0392B', label='Removed (Active/Idle family)'),
                    Patch(facecolor='#2C5F8A', label='Retained (final 51 features)')]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('/home/claude/figures_en/fig3_ks_drift.png', dpi=300, bbox_inches='tight', facecolor='white')
print("saved fig3 (EN)")
