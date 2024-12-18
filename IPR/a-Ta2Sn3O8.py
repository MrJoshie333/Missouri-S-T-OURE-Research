'''
IPR Plotter - All runs of Ta2Sn3O8
Joshua Santy
'''
import os

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=5, nrows=2)

files = os.listdir('a-Ta2Sn3O8')
run = 1
files.sort(key=lambda f: int(f.split('_')[0]))
x = 0
y = 0
for file_name in files:
    # print(f"Processing file: {file_name}")
    file_path = os.path.join('a-Ta2Sn3O8', file_name)
    with open(file_path) as f:
        data = f.readlines()
    energy = []
    IPRC = []

    for i in data:
        rowData = i.split()
        energy.append(float(rowData[0]))
        IPRC.append(float(rowData[1]))

    axs[x, y].scatter(energy, IPRC, s=25, facecolors='none', edgecolors='red', alpha=0.25)
    axs[x, y].set_xlim(-6, 4)
    axs[x, y].set_ylim(-3, 80)
    axs[x, y].set_yticks(np.arange(0, 80, 10))
    axs[x, y].set_xticks(np.arange(-6, 3, 2))
    axs[x, y].axvline(x=0, color='gray', alpha=0.05, linestyle='dashed')
    # axs[x, y].set_title(name, x = 0.20, y = .83, fontsize = 20)
    axs[x, y].tick_params(axis='x', labelsize=16)
    axs[x, y].tick_params(axis='y', labelsize=16)
    # add text in the top right
    axs[x, y].text(0.85, 60, "Run " + str(run), fontsize=16, verticalalignment='top')
    run += 1
    y += 1
    if y == 5:
        y = 0
        x += 1

axs[1, 2].set_xlabel('Energy (eV)', fontsize='20')
axs[0, 0].set_ylabel('IPR', fontsize='20')
axs[0, 0].yaxis.set_label_coords(-0.1, 0)
axs[0, 1].set_yticklabels([])
axs[0, 2].set_yticklabels([])
axs[0, 3].set_yticklabels([])
axs[0, 4].set_yticklabels([])
axs[1, 1].set_yticklabels([])
axs[1, 2].set_yticklabels([])
axs[1, 3].set_yticklabels([])
axs[1, 4].set_yticklabels([])

fig.suptitle('a-Ta2Sn3O8 IPR', fontsize='24')

for ax in axs.flat:
    ax.grid(True, alpha=0.25)

plt.subplots_adjust(  # left=0.2,
    # bottom=0.3,
    # right=0.8,
    # top=0.7,
    wspace=0,
    hspace=0)

plt.show()
