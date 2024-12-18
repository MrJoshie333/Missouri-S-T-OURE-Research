# ===== SrSnO Absorption Plotter =====
# ===== Joshua Santy =====
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

from misc.utility import read_dat_file_to_lists


def format_func(value, tick_number):
    # Convert the original value to a scaled value
    return f'{value / 10000:.0f}'


energy, absorption = read_dat_file_to_lists("av_ABSORPTION_a15p0_d4p25.dat")
plt.plot(energy, absorption, label='4.25')
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_func))

plt.title('Absorption of Amorphous SrSnO', fontsize=32)
plt.xlabel('Energy (ev)', fontsize=24)
plt.ylabel(r'Absorption (10$^{4}$ cm$^{-1})$', fontsize=24)
plt.legend(loc='upper right', fontsize=24)

# cutoff the plot
plt.xlim(0, 6)

plt.tick_params(axis='both', which='major', labelsize=24)
plt.grid(True, alpha=0.35)

plt.show()
