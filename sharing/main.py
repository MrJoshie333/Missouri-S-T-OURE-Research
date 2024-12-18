# ===== Sharing Plotter =====
# ===== Joshua Santy =====
import matplotlib.pyplot as plt

from utility import read_dat_file_to_lists, extract_density


def convertDensity(density):
    extracted_densities = []

    for d in density:
        extracted_density = extract_density(d)
        if extracted_density is not None:  # Only append valid densities
            extracted_densities.append(extracted_density)

    return extracted_densities


fig, axs = plt.subplots(1, 2)

file_names_SnO = "Data/SnO/sharing_average.dat"

file_names_left = ["Data/SnO2/sharing_average.dat", "Data/Ta2O5/sharing_average.dat"]
labels_left = [r'$\text{SnO}$', r'$\mathrm{SnO}_2$',
               r'$\text{Ta}_2\text{O}_5$']
colors_left = ["darkred", "limegreen", "darkorange"]

file_names_right = ["Data/Ta2Sn10O15/sharing_average.dat", "Data/Ta2Sn3O8/sharing_average.dat",
                    "Data/Ta2SnO6/sharing_average.dat"]
labels_right = [r'$\text{Ta}_2\text{Sn}_{10}\text{O}_{15}$', r'$\text{Ta}_2\text{Sn}_3\text{O}_8$',
                r'$\text{Ta}_2\text{SnO}_6$']
colors_right = ["dodgerblue", "blueviolet", "darkblue"]

# ===== SnO =====

density, normalized, face, edge_shared, corner = read_dat_file_to_lists("Data/SnO/sharing_average.dat", " ", True)
extracted_densities = convertDensity(density)
axs[0].plot(
    extracted_densities,
    edge_shared,
    label=labels_left[0],
    color=colors_left[0],
    linewidth=3)

# ===== SnO2, Ta2O5 =====
for compound in file_names_left:
    density, normalized, face, edge_shared, corner = read_dat_file_to_lists(compound, " ", False)
    extracted_densities = convertDensity(density)
    axs[0].plot(
        extracted_densities,
        edge_shared,
        label=labels_left[file_names_left.index(compound) + 1],
        color=colors_left[file_names_left.index(compound) + 1],
        linewidth=3)  # Adjust this value to set the thickness

# ===== Ta2Sn10O15, Ta2Sn3O8, Ta2SnO6 =====
for compound in file_names_right:
    # Read data from file
    density, normalized, face, edge_shared, corner = read_dat_file_to_lists(compound, " ", False)
    extracted_densities = convertDensity(density)
    axs[1].plot(
        extracted_densities,
        edge_shared,
        label=labels_right[file_names_right.index(compound)],
        color=colors_right[file_names_right.index(compound)],
        linewidth=3
    )

axs[0].set_ylabel(r'Edge Sharing %', fontsize=44)
axs[0].set_xlabel("Density (g/cm$^3$)", fontsize=44)
axs[0].xaxis.set_label_coords(1, -0.09)
axs[0].yaxis.set_label_coords(-0.15, 0.5)

# show legends
axs[0].legend(fontsize=32)
axs[1].legend(loc='upper left', fontsize=32)

axs[0].tick_params(axis='both', which='major', labelsize=27)
axs[1].tick_params(axis='both', which='major', labelsize=27)
# gridlines
axs[0].grid(alpha=0.75)
axs[1].grid(alpha=0.75)

# y_lim for both plots is 10 to 40
axs[0].set_ylim(10, 45)
axs[1].set_ylim(10, 45)
axs[1].set_xlim(2, 8.5)
axs[1].set_yticklabels([])
axs[0].set_xticks([3, 4, 5, 6, 7, 8])
axs[1].set_xticks([3, 4, 5, 6, 7, 8])

fig.subplots_adjust(left=0.125, bottom=0.2, right=0.9, top=0.9, wspace=0, hspace=0.2)
for ax in axs:
    ax.spines['top'].set_linewidth(3)
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)
    ax.spines['right'].set_linewidth(3)

plt.show()
