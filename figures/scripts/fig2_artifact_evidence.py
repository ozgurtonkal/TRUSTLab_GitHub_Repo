import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

trust_vals = ['65535', '0']
trust_counts = [2260241, 1341112]
ax = axes[0]
ax.bar(np.arange(len(trust_vals)), trust_counts, color='#3A7D44', width=0.6)
ax.set_xticks(np.arange(len(trust_vals)))
ax.set_xticklabels(trust_vals, fontsize=9.5)
ax.set_title("TRUSTLab\n(only 2 unique values)", fontsize=10.5)
ax.set_ylabel('Flow count', fontsize=10)
for i, v in enumerate(trust_counts):
    ax.annotate(f'{v:,}', xy=(i, v), xytext=(0, 3), textcoords='offset points', ha='center', fontsize=7.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 9_200_000)

cic_vals = ['-1', '0', '235', '229', '256']
cic_counts = [1441552, 271893, 178098, 104516, 42608]
ax2 = axes[1]
ax2.bar(np.arange(len(cic_vals)), cic_counts, color='#B5651D', width=0.6)
ax2.set_xticks(np.arange(len(cic_vals)))
ax2.set_xticklabels(cic_vals, fontsize=9.5)
ax2.set_title("CICIDS2017\n(236+ unique values across 2,830,743 rows)", fontsize=10.5)
for i, v in enumerate(cic_counts):
    ax2.annotate(f'{v:,}', xy=(i, v), xytext=(0, 3), textcoords='offset points', ha='center', fontsize=7.5)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_ylim(0, 9_200_000)

cse_vals = ['-1', '0', '211', '62852', '149']
cse_counts = [8255549, 1114835, 702526, 645957, 361642]
ax3 = axes[2]
ax3.bar(np.arange(len(cse_vals)), cse_counts, color='#2C5F8A', width=0.6)
ax3.set_xticks(np.arange(len(cse_vals)))
ax3.set_xticklabels(cse_vals, fontsize=9.5)
ax3.set_title("CSE-CIC-IDS2018\n(15,522 unique values across 16,232,943 rows)", fontsize=10.5)
for i, v in enumerate(cse_counts):
    ax3.annotate(f'{v:,}', xy=(i, v), xytext=(0, 3), textcoords='offset points', ha='center', fontsize=7.5)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.set_ylim(0, 9_200_000)

fig.suptitle("Environment Fingerprint Evidence: 'Init Bwd Win Byts' Value Distribution (Three Datasets)", fontsize=13, y=1.04)
plt.tight_layout()
plt.savefig('/home/claude/figures_en/fig2_artifact_evidence.png', dpi=300, bbox_inches='tight', facecolor='white')
print("saved fig2 (EN)")
