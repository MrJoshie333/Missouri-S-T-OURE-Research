"""
Density vs Energy Plotter
Joshua Santy

Be sure to change num_atoms to however many atoms were used

"""

import matplotlib.pyplot as plt

from utility import read_dat_file_to_lists


def averages(input_list: list[float]):
    average_array = []
    count = 0
    straight_counter = 0
    for _ in unique_densities:
        tot_sum = sum(input_list[count:count + density_count[straight_counter]])
        average_array.append(tot_sum / density_count[straight_counter])
        count += density_count[straight_counter]
        straight_counter += 1
    return average_array


fig, axs = plt.subplots(ncols=3)
num_atoms = [138, 140, 138, 135, 130, 134]
k = 0

file_names = ["SnO_voids_runs.dat"]
for a in file_names:

    orig_density, num_runs, void_percent, largest_void, surface_vs_largest, sn_percent, o_percent = read_dat_file_to_lists(
        a, True)

    unique_densities = []
    density_count = []
    density_list = []

    # Turning Density into Float
    for i in orig_density:
        i = i.split("_")[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        density_list.append(float(i))

    for j in density_list:
        if j not in unique_densities:
            unique_densities.append(j)
            density_count.append(density_list.count(j))
    # Averages
    void_percent_avg = averages(void_percent)
    largest_void_avg = averages(largest_void)
    surface_vs_largest_avg = averages(surface_vs_largest)

    axs[0].plot(unique_densities, void_percent_avg, color="navy")
    axs[0].scatter(density_list, void_percent, color="orange")
    axs[1].plot(unique_densities, largest_void_avg, color="navy")
    axs[1].scatter(density_list, largest_void, color="orange")
    axs[2].plot(unique_densities, surface_vs_largest_avg, color="navy")
    axs[2].scatter(density_list, surface_vs_largest, color="orange")

    axs[1].set_xlabel(r'$\mathrm{Density, \frac{g}{cm^3}}$', fontsize='16')
    axs[0].set_ylabel('Fraction of Void Volume', fontsize='16')
    axs[1].set_ylabel('Fraction of 1st Largest Void', fontsize='16')
    axs[2].set_ylabel('Surface to Volume of 1st Largest Void', fontsize='16')

axs[0].grid(True, alpha=0.35)
axs[1].grid(True, alpha=0.35)
axs[2].grid(True, alpha=0.35)

axs[1].set_title("SnO", fontsize=24)
plt.subplots_adjust(left=0.2,
                    bottom=0.3,
                    right=0.8,
                    top=0.7,
                    wspace=0.3,
                    hspace=0.61)
plt.show()
