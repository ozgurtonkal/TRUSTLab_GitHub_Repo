import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams['font.family'] = 'DejaVu Sans'

fig, ax = plt.subplots(figsize=(7, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 30)
ax.axis('off')

def box(x, y, w, h, text, color='#E8F0E8', fontsize=9.5, edgecolor='#3A7D44'):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15", 
                         facecolor=color, edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, wrap=True)

def arrow(x1, y1, x2, y2):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=15,
                          color='#444444', linewidth=1.3)
    ax.add_patch(a)

# Data sources
box(0.5, 27, 2.8, 1.8, "TRUSTLab\n73 features\n4,501,692 flows", color='#E8F0E8')
box(3.6, 27, 2.8, 1.8, "CICIDS2017\n79 features\n2,830,743 flows", color='#F5E8D8')
box(6.4, 27, 2.8, 1.8, "CSE-CIC-IDS2018\n80 features\n16,232,943 flows", color='#DCE8F0')

arrow(1.9, 27, 3.5, 25.3)
arrow(5, 27, 5, 25.3)
arrow(8.1, 27, 6.5, 25.3)

box(2.5, 23.5, 5, 1.8, "Common Feature Schema Extraction\n(72 overlapping features)", color='#FFF3D6')

arrow(5, 23.5, 5, 21.8)

box(2, 20, 6, 1.6, "Artifact Screening: Group A/B/C\n(13 features removed)", color='#FADBD8')

arrow(5, 20, 5, 18.3)

box(2, 16.5, 6, 1.6, "Within-TRUSTLab Inconsistency: Active/Idle\n(8 features removed)", color='#FADBD8')

arrow(5, 16.5, 5, 14.8)

box(2, 13, 6, 1.6, "KS-Test Verification\n(59 features, 51 retained)", color='#FADBD8')

arrow(5, 13, 5, 11.3)

box(1.5, 9.5, 7, 1.6, "Final Feature Set: 51 Features", color='#D5F0D5', edgecolor='#2C5F2D')

arrow(5, 9.5, 5, 7.8)

box(0.3, 5.8, 4.3, 1.8, "Model Training (TRUSTLab)\nRF, XGBoost, LightGBM,\n1D-CNN, LSTM", color='#E8E0F0', fontsize=8.5)
box(5.4, 5.8, 4.3, 1.8, "Evaluation Protocol\nMulti-Seed, Bootstrap,\nSingle-Attack Analysis", color='#E8E0F0', fontsize=8.5)

arrow(2.5, 5.8, 2.5, 4.1)
arrow(7.5, 5.8, 7.5, 4.1)

box(0.5, 2, 4, 1.8, "Within-Dataset\nEvaluation", color='#D5E8F5')
box(5.5, 2, 4, 1.8, "Cross-Dataset\nEvaluation\n(CICIDS2017, CSE-CIC-IDS2018)", color='#D5E8F5', fontsize=8)

plt.tight_layout()
plt.savefig('/home/claude/figures_en/fig1_methodology.png', dpi=300, bbox_inches='tight', facecolor='white')
print("saved fig1 (EN)")
