# ===== SrSnO IPR Plotter =====
# ===== Joshua Santy =====
from matplotlib import pyplot as plt

from misc.utility import read_dat_file_to_lists

energy, IPR, a, b, c, d = read_dat_file_to_lists("IPRcontr_HSE.dat")

plt.scatter(energy, IPR, s=25, alpha=0.25, label='4.25')

plt.title('IPR of Amorphous SrSnO', fontsize=32)
plt.xlabel('Energy (ev)', fontsize=24)
plt.ylabel('IPR', fontsize=24)
plt.legend(loc='upper right', fontsize=24)

plt.tick_params(axis='both', which='major', labelsize=24)
plt.xlim(-6, 4)
plt.grid(True, alpha=0.35)
plt.show()
