# ===== Absorption Plotter with SrSnO=====
# Joshua Santy


import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from utility import read_dat_file_to_lists


def format_func(value, tick_number):
    # Convert the original value to a scaled value
    return f'{value / 10000:.0f}'


fig, axs = plt.subplots(1, 2)

# import and read the lines of all the ABSORPTION files
file_names_left = ["Data/SnO/av_ABSORPTION_a15p3_d4p31.dat", "Data/SnO/av_ABSORPTION_a14p5_d5p06.dat",
                   "Data/SnO2/av_ABSORPTION_a12.11.dat",
                   "Data/Ta2O5/av_ABSORPTION_a12p943_d6p77.dat"]
labels_left = [r'$\text{SnO, 4.31 g/cm}^3$', r'$\text{SnO, 5.06 g/cm}^3$', r'$\mathrm{SnO}_2$',
               r'$\text{Ta}_2\text{O}_5$']
colors_left = ["darkred", "red", "limegreen", "darkorange"]

file_names_right = ["Data/Ta2Sn10O15/av_ABSORPTION_a13p9_d5p53.dat", "Data/Ta2Sn3O8/av_ABSORPTION_a13p1_d6p25.dat",
                    "Data/Ta2SnO6/av_ABSORPTION_a12p96_d6p60.dat"]
labels_right = [r'$\text{Ta}_2\text{Sn}_{10}\text{O}_{15}$', r'$\text{Ta}_2\text{Sn}_3\text{O}_8$',
                r'$\text{Ta}_2\text{SnO}_6$']
colors_right = ["dodgerblue", "blueviolet", "darkblue"]

# ===== Left panel =====
for compound in file_names_left:
    energy, absorption = read_dat_file_to_lists(compound, "\t", True)
    axs[0].plot(
        energy,
        absorption,
        label=labels_left[file_names_left.index(compound)],
        color=colors_left[file_names_left.index(compound)],
        linewidth=3)
# ===== Right panel =====
for compound in file_names_right:
    energy, absorption = read_dat_file_to_lists(compound, "\t", True)
    axs[1].plot(
        energy,
        absorption,
        label=labels_right[file_names_right.index(compound)],
        color=colors_right[file_names_right.index(compound)],
        linewidth=3)
energy, absorption = read_dat_file_to_lists("Data/SrSnO/av_ABSORPTION_a15p0_d4p25.dat", "\t")
axs[0].plot(energy, absorption, label='SrSnO 4.25', marker="s", color="black", linewidth=3)
axs[1].plot(energy, absorption, label='SrSnO 4.25', marker="s", color="black", linewidth=3)
axs[0].set_ylabel(r'Absorption (cm$^{-1})$', fontsize=44)
axs[0].set_xlabel("Energy (eV)", fontsize=44)
axs[0].xaxis.set_label_coords(1, -0.09)

# y_lim for both plots is 250000
axs[0].set_ylim(0, 1 * 10 ** 5)
axs[1].set_ylim(0, 1 * 10 ** 5)
axs[0].set_xlim(0, 6)
axs[1].set_xlim(0, 6)

# make the plots share a common y-axis
axs[0].set_xticks([0, 1, 2, 3, 4, 5])
axs[0].set_yticks([2 * 10 ** 4, 4 * 10 ** 4, 6 * 10 ** 4, 8 * 10 ** 4, 10 * 10 ** 4])
axs[0].yaxis.set_major_formatter(FuncFormatter(format_func))
axs[0].set_ylabel(r'Absorption (10$^{4}$ cm$^{-1})$')
axs[1].set_yticklabels([])
axs[0].legend(fontsize=32)
axs[1].legend(fontsize=32)
legend0 = axs[0].legend(fontsize=32)
legend0.set_zorder(1)
axs[0].tick_params(axis='both', which='major', labelsize=27)
axs[1].tick_params(axis='both', which='major', labelsize=27)

# fig.tight_layout()
fig.subplots_adjust(left=0.075, bottom=0.14, right=0.99, top=0.98, wspace=0, hspace=0)

for ax in axs:
    ax.grid(alpha=0.75)
# add a thicker frame around the plots
for ax in axs:
    ax.spines['top'].set_linewidth(3)
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)
    ax.spines['right'].set_linewidth(3)

plt.show()
