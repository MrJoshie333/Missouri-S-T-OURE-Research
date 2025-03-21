import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# ===== User Input =====
DEST_DIR = '../SrSnO'

# List of directory names (the last four characters are the density)
densities = ["6p27", "5p74", "5p27", "4p85", "4p47", "4p13", "3p82"]
num_atoms = [138, 134]
color = ["orange", "green"]
k = 0
# Save the Figure as a PDF?
SAVEPDF = False

# ===== Initialization =====
file_names = ["../Data/SnO_av_etot300K_density_runs_1.dat", "../Data/Ta2SnO6_av_etot300K_density_runs.dat"]

plt.figure(figsize=(5, 3))

average_values = []
density_values = []

# ===== Average Density =====
density_averages = {}
for density in densities:
    file_name = f"{DEST_DIR}/etot300k_{density}"
    data = np.loadtxt(file_name)
    avg_value = np.mean(data)
    density_averages[density] = avg_value

min_average = min(density_averages.values())

# ===== Correct Density =====
for density in densities:
    file_name = f"{DEST_DIR}/etot300k_{density}"
    data = np.loadtxt(file_name)
    normalized_data = data - min_average
    scaled_data = (normalized_data / 130) * 1000
    avg_scaled_data = np.mean(scaled_data)
    average_values.append(avg_scaled_data)
    density_values.append(float(density.replace('p', '.')))
    plt.scatter([density_values[-1]] * len(scaled_data), scaled_data, color = "lightblue", alpha=0.4)

plt.plot(density_values, average_values, color='black', linestyle='-', linewidth=3, alpha=1, zorder=2)  # Line
plt.scatter(density_values, average_values, color='red', label="Average", zorder=2)  # Points
for a in file_names:
    with open(a) as f:
        data = f.readlines()
    a = a[:-29]
    orig_density = []
    num_runs = []
    energies = []
    temp1 = []
    density_count = []

    # Getting Data
    for i in data:
        rowData = i.split(" ")
        orig_density.append(rowData[0])
        num_runs.append(rowData[1])
        energies.append(float(rowData[2]))

    density_list = []

    # ===== Turning Density into Float ======
    for i in orig_density:
        i = i.split("_")
        i = i[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list.append(i)

    for j in density_list:
        if j not in temp1:
            temp1.append(j)
            density_count.append(density_list.count(j))

    # ===== Averages =====
    average_array = []
    count = 0
    straight_counter = 0
    for values in temp1:
        tot_sum = sum(energies[count:count + density_count[straight_counter]])
        average_array.append(tot_sum / density_count[straight_counter])
        count += density_count[straight_counter]
        straight_counter += 1

    smallest = min(average_array)

    # ===== Energy Values: Getting correct scale and dividing by number of atoms
    for i in range(len(energies)):
        energies[i] -= smallest  # 765.2191713
        energies[i] /= num_atoms[k]

    for i in range(len(average_array)):
        average_array[i] -= smallest
        average_array[i] /= num_atoms[k]

    # meV Units
    for i in range(len(energies)):
        energies[i] *= 1000
    for i in range(len(average_array)):
        average_array[i] *= 1000

    # plt.scatter(density_list, energies, color="orange", marker=".")
    # ax[row, col].scatter(temp1, average_array, color="deepskyblue")
    plt.scatter(temp1, average_array, color=color[k], alpha = 0.5)
    plt.plot(temp1, average_array, color="black", linestyle="dashed", alpha = 0.5, zorder=1)
    k += 1


legend_entry = [
    Line2D([0], [0], color='black', linestyle='-', linewidth=3, marker='o', markersize=8, markerfacecolor='firebrick', label="SrSnO"),
    Line2D([0], [0], color='black', linestyle='-', linewidth=3, marker='o', markersize=8, markerfacecolor='orange', label='SnO'),
    Line2D([0], [0], color='black', linestyle='-', linewidth=3, marker='o', markersize=8, markerfacecolor='green', label=r'$\mathrm{Ta_{2}SnO_{6}}$')
]
fig = plt.gcf()  # Get the current figure
fig.set_size_inches(6, 3.5)  # Resize without making a new figure


plt.title("a-SrSnO Energy vs. Density", fontsize = 19)
plt.xlabel(r'$\mathrm{Density, g/cm}^3$', fontsize = 17)
plt.ylabel(r'$\mathrm{ΔE, meV/atom}$', fontsize = 17)
plt.legend(title="Composition", loc='upper left', handles=legend_entry)
plt.grid(True, alpha=0.25)
for spine in plt.gca().spines.values():
    spine.set_linewidth(1.8)
plt.subplots_adjust(bottom = 0.176)
# plt.tight_layout()

plt.show()


if SAVEPDF == True:
    plt.savefig('SrSnO_single_figure.pdf', format='pdf')
