# -*- coding: utf-8 -*-
r"""gen_public_arch.py — Canvas public architecture diagram
====================================================================================
A minimal, detail-free block diagram of the Canvas pipeline:
inputs O / T, three modules CMRA / TGM / SAVR, output B.
Usage:  python gen_public_arch.py
Output: public_arch.pdf / .png  (in the current directory)
"""
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.dirname(os.path.abspath(__file__))
fig, ax = plt.subplots(figsize=(11, 2.6))
ax.set_xlim(0, 22); ax.set_ylim(0, 5); ax.axis('off')


def box(cx, cy, w, h, label, ec='#2C3E50', fc='white', fs=13):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle='round,pad=0.15,rounding_size=0.35',
                                fc=fc, ec=ec, lw=2.0))
    ax.text(cx, cy, label, ha='center', va='center', fontsize=fs, fontweight='bold', color='#2C3E50')


def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=18,
                                 color='#2C3E50', lw=2.0))


# inputs
box(1.4, 3.6, 2.0, 1.4, 'O')
box(1.4, 1.4, 2.0, 1.4, 'T')
# three modules
box(8.0, 2.5, 3.4, 1.8, 'CMRA')
box(13.0, 2.5, 3.4, 1.8, 'TGM')
box(18.0, 2.5, 3.4, 1.8, 'SAVR')
# output
box(21.2, 2.5, 1.4, 1.8, 'B')

# arrows
arrow(2.5, 3.6, 6.3, 2.9)      # O -> CMRA
arrow(2.5, 1.4, 6.3, 2.1)      # T -> CMRA
arrow(9.7, 2.5, 11.3, 2.5)     # CMRA -> TGM
arrow(14.7, 2.5, 16.3, 2.5)    # TGM -> SAVR
arrow(19.7, 2.5, 20.5, 2.5)    # SAVR -> B

plt.tight_layout()
fig.savefig(os.path.join(OUT, 'public_arch.pdf'), bbox_inches='tight', facecolor='white')
fig.savefig(os.path.join(OUT, 'public_arch.png'), dpi=300, bbox_inches='tight', facecolor='white')
print(f'[OK] {OUT}/public_arch.pdf / .png')
