"""
Joshua Santy Void Data All Compounds
"""

import matplotlib.pyplot as plt
import numpy as np

# ===== Setup =====
# Save the Figure as a PDF?
SAVEPDF = False

file_names = ["Data/SnO_voids_runs.dat", "Data/SnO2_voids_runs.dat", "Data/Ta2O5_voids_runs.dat",
              "Data/Ta2Sn10O15_voids_runs.dat", "Data/Ta2Sn3O8_voids_runs.dat", "Data/Ta2SnO6_voids_runs.dat"]


def averages(input):
    average_array = []
    count = 0
    straight_counter = 0
    for values in temp1:
        tot_sum = sum(input[count:count + density_count[straight_counter]])
        average_array.append(tot_sum / density_count[straight_counter])
        count += density_count[straight_counter]
        straight_counter += 1
    return average_array


def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


# ===== Initialization =====

fig, axs = plt.subplots(nrows=2, ncols=6)
row = 0
col = 0

for a in file_names:
    with open(a) as f:
        data = f.readlines()

    orig_density = []
    num_runs = []
    temp1 = []
    density_count = []
    void_percent = []
    largest_void = []
    surface_vs_largest = []
    if a == "Data/SnO_voids_runs.dat":
        del data[0]

    # Getting Data
    for i in data:
        rowData = i.split(" ")
        orig_density.append(rowData[0])
        num_runs.append(rowData[1])
        void_percent.append(float(rowData[2]))
        largest_void.append(float(rowData[3]))
        surface_vs_largest.append(float(rowData[4]))

    density_list = []

    # Turning Density into Float
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
    # Averages
    void_percent_avg = averages(void_percent)
    largest_void_avg = averages(largest_void)
    surface_vs_largest_avg = averages(surface_vs_largest)

    # ===== Plotting =====

    axs[row, col].plot(temp1, void_percent_avg, color="navy", label='Total Void')
    axs[row, col].plot(temp1, largest_void_avg, color="red", label='Largest Void')
    axs[1, col].plot(temp1, surface_vs_largest_avg, color="navy")
    axs[1, col].scatter(density_list, surface_vs_largest, color="orange")
    axs[0, col].grid(True, alpha=0.35)
    axs[1, col].grid(True, alpha=0.35)
    axs[1, col].set_ylim(0, 25)

    surface_vs_largest_avg_no_NaN = [x for x in surface_vs_largest_avg if str(x) != 'nan']
    min_val = min(surface_vs_largest_avg_no_NaN, key=lambda x: abs(x - 1))

    index = surface_vs_largest_avg.index(min_val)
    density_list = remove_duplicates(density_list)

    if col != 1:
        axs[1, col].scatter(density_list[index], min_val)

    a = a[:-15]
    print(f'{a}: {density_list[index]} ')  # Averages

    axs[0, col].set_xticklabels([])
    axs[1, col].set_yticks(np.arange(0, 21, 5))
    col += 1
    if col == 6:
        row = 1
        col = 0

# ===== Formatting =====

axs[0, 0].set_title("SnO", fontsize='20')
axs[0, 1].set_title(r' $\mathrm{SnO_2}$', fontsize='20')
axs[0, 2].set_title(r'$\mathrm{Ta_2O_5}$', fontsize='20')
axs[0, 3].set_title(r'$\mathrm{Ta_2Sn_{10}O_{15}}$', fontsize='20')
axs[0, 4].set_title(r'$\mathrm{Ta_2Sn_3O_8}$', fontsize='20')
axs[0, 5].set_title(r'$\mathrm{Ta_2SnO_6}$', fontsize='20')

axs[1, 3].set_xlabel(r'$\mathrm{Density, \frac{g}{cm^3}}$', fontsize='16')
axs[1, 3].set_xlabel(r'Density, g/$\mathrm{cm^3}$', fontsize='16')
r'$\mathrm{Ta_2SnO_6}$'

axs[1, 0].set_ylabel('Surface to Volume', fontsize='14')
axs[0, 0].set_ylabel('Void Volume, %', fontsize='14')
axs[0, 0].yaxis.set_label_coords(-.3, 0.5)
axs[1, 0].yaxis.set_label_coords(-0.3, 0.5)
axs[1, 3].xaxis.set_label_coords(-0.2, -.2)
axs[0, 2].legend(loc='upper right', bbox_to_anchor=(-.23, 1), prop={"size": 11}, fontsize=20)
plt.subplots_adjust(left=0.2,
                    bottom=0.3,
                    right=0.8,
                    top=0.7,
                    wspace=0.25,
                    hspace=0)

axs[0, 1].set_ylim(0, 10)
axs[0, 1].set_xlim(5, 7.5)
axs[1, 1].set_xlim(5, 7.5)

for a in axs.flat:
    a.tick_params(axis='x', labelsize=13)
    a.tick_params(axis='y', labelsize=13)

plt.show()

if SAVEPDF == True:
    plt.savefig('voids_all_compounds.pdf')
