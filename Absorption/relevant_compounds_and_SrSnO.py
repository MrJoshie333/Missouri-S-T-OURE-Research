# ===== Relevant Compounds Absorption Plotter with SrSnO=====
# Joshua Santy

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from utility import read_dat_file_to_lists


def format_func(value, tick_number):
    # Convert the original value to a scaled value
    return f'{value / 10000:.0f}'


fig, ax = plt.subplots(figsize=(10, 6))  # Increase figure size for better layout

# Import and read the lines of the ABSORPTION files
file_names = [
    "Data/SnO/av_ABSORPTION_a15p3_d4p31.dat",
    "Data/SnO/av_ABSORPTION_a14p5_d5p06.dat",
    "Data/SnO/av_ABSORPTION_a13p9_d5p75.dat",
    "Data/Ta2Sn10O15/av_ABSORPTION_a13p9_d5p53.dat",
    "Data/SrSnO/av_ABSORPTION_a15p0_d4p25.dat"
]
labels = [
    r'$\text{SnO, 4.31 g/cm}^3$',
    r'$\text{SnO, 5.06 g/cm}^3$',
    r'$\text{SnO, 5.75 g/cm}^3$',
    r'$\text{Ta}_2\text{Sn}_{10}\text{O}_{15},\text{5.53 g/cm}^3$',
    r'$\text{SrSnO, 4.25 g/cm}^3$'
]
colors = ["darkred", "red", "orange", "dodgerblue", "black"]

# Plot each compound
for i, compound in enumerate(file_names):
    energy, absorption = read_dat_file_to_lists(compound, "\t", True)
    ax.plot(
        energy,
        absorption,
        label=labels[i],
        color=colors[i],
        linewidth=3
    )

# Set labels and axis limits
ax.set_ylabel(r'Absorption (cm$^{-1})$', fontsize=22)
ax.set_xlabel("Energy (eV)", fontsize=22)
ax.set_ylim(0, 1 * 10 ** 5)
ax.set_xlim(0, 6)

# Adjust tick labels and formatting
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}"))
ax.yaxis.set_major_formatter(FuncFormatter(format_func))
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_yticks([2 * 10 ** 4, 4 * 10 ** 4, 6 * 10 ** 4, 8 * 10 ** 4, 10 * 10 ** 4])

# ===== Legend =====
ax.legend(
    fontsize=14,
    loc='center left',
    bbox_to_anchor=(1.05, 0.5),
    borderaxespad=0
)

ax.grid(alpha=0.75)
for spine in ax.spines.values():
    spine.set_linewidth(3)

ax.tick_params(axis='both', which='major', labelsize=14)
plt.subplots_adjust(right=0.75)
plt.show()
