'''
IPR Plotter
Joshua Santy
'''
import os

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=3, nrows=2)

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))


def plot(compound, x, y, color, name):
    directory_path = os.path.join(BASE_DIR, compound)  # === Change to custom directory if it doesn't work
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")
    files = os.listdir(directory_path)
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)  # Correctly construct the full file path
        with open(file_path) as f:
            data = f.readlines()
        energy = []
        IPRC = []
        for i in data:
            rowData = i.split()
            energy.append(float(rowData[0]))
            IPRC.append(float(rowData[1]))

        axs[x, y].scatter(energy, IPRC, s=25, facecolors='none', edgecolors=color, alpha=0.25)
        axs[x, y].set_xlim(-6, 4)
        axs[x, y].set_ylim(-3, 80)
        axs[x, y].set_yticks(np.arange(0, 80, 10))
        axs[x, y].set_xticks(np.arange(-6, 3, 2))
        axs[x, y].axvline(x=0, color='gray', alpha=0.05, linestyle='dashed')
        axs[x, y].set_title(name, x=0.20, y=.83, fontsize=20)
        axs[x, y].tick_params(axis='x', labelsize=16)
        axs[x, y].tick_params(axis='y', labelsize=16)


plot('SnO_4.31', 0, 0, 'red', "$\mathrm{SnO}$, 4.31")
plot('SnO_5.06', 0, 1, 'aqua', "$\mathrm{SnO}$, 5.06")
plot('SnO2', 0, 2, 'purple', "$\mathrm{SnO_2}$")
plot('Ta2Sn10O15', 1, 0, 'orange', "$\mathrm{Ta_2Sn_{10}O_{15}}$")
plot('Ta2Sn3O8', 1, 1, 'green', "$\mathrm{Ta_2Sn_3O_8}$")
plot('Ta2O5', 1, 2, 'blue', "$\mathrm{Ta_2O_5}$")

axs[1, 1].set_xlabel('Energy (eV)', fontsize='20')
axs[0, 0].set_ylabel('IPR', fontsize='20')
axs[0, 0].yaxis.set_label_coords(-0.1, 0)
axs[0, 1].set_yticklabels([])
axs[0, 2].set_yticklabels([])
axs[1, 1].set_yticklabels([])
axs[1, 2].set_yticklabels([])

plt.subplots_adjust(  # left=0.2,
    # bottom=0.3,
    # right=0.8,
    # top=0.7,
    wspace=0,
    hspace=0)

plt.show()
