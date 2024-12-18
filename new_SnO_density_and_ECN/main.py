# ===== SnO Density and ECN =====
# ===== Joshua Santy =====
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import subplots_adjust

from utility import read_dat_file_to_lists

fig, axs = plt.subplots(1, 2)

a, b, density, c, energy = read_dat_file_to_lists("Data/zeropressure_results.dat", True)
# print(density)
# print(energy)

# multiply each energy by 1000
for i in range(len(energy)):
    energy[i] *= 1000
# ===== Plotting =====
axs[0].scatter(density, energy)
axs[0].set_xlim(2.5, 6.1)
axs[0].set_ylim(-30, 40)

a, density, ECN, d, e, f, g, h = read_dat_file_to_lists("Data/avECN_zp_SnO.dat", True)
axs[1].scatter(density, ECN)
axs[1].set_xlim(2.5, 6.1)

# ===== Formatting =====
axs[0].set_axisbelow(True)
axs[1].set_axisbelow(True)

axs[0].set_xlabel(r'Density, g/$\text{cm}^3$', fontsize=42, labelpad=25)
axs[1].set_xlabel(r'Density, g/$\text{cm}^3$', fontsize=42, labelpad=25)
axs[0].set_ylabel(r'$\Delta \text{E, meV/atom}$', fontsize=42, labelpad=20)
axs[1].set_ylabel("Effective Coordination \n Number", fontsize=42, labelpad=20)
axs[0].set_yticks(np.arange(-20, 41, 10))
axs[1].set_yticks(np.arange(2.6, 3.01, 0.1))
axs[0].tick_params(axis='both', which='major', labelsize=26)
axs[1].tick_params(axis='both', which='major', labelsize=26)

fig.set_frameon(True)
fig.set_facecolor('white')
for ax in axs[:2]:
    for spine in ax.spines.values():
        spine.set_linewidth(1.8)
    ax.grid(True, alpha=0.35)
axs[0].set_xticks([2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])
axs[1].set_xticks([2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])
subplots_adjust(bottom=0.31, top=0.7, wspace=0.448, right=0.952)
plt.show()
