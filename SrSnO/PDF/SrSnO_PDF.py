# ===== SrSnO PDF Plotter =====
# ===== Joshua Santy =====
import matplotlib.pyplot as plt

from misc.utility import read_dat_file_to_lists

r, prob = read_dat_file_to_lists("PDF_amorphous.dat")
plt.plot(r, prob, label='4.25')
plt.xlim(1, 7)
plt.title('PDF of Amorphous SrSnO', fontsize=32)
plt.xlabel('r (Å)', fontsize=24)
plt.ylabel('g(r)', fontsize=24)
plt.legend(loc='upper right', fontsize=24)
plt.tick_params(axis='both', which='major', labelsize=24)

plt.grid(True, alpha=0.35)
plt.show()
