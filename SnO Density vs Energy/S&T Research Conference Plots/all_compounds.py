"""
Density vs Energy Plotter
Joshua Santy

Be sure to change num_atoms to however many atoms were used

"""
import matplotlib.pyplot as plt
import numpy as np

# ========= User Input =========
# Save the Figure as a PDF?
SAVEPDF = False
num_atoms = [138, 140, 138, 135, 130, 134]
file_names = ["../Data/SnO2_av_etot300K_density_runs.dat", "../Data/TaO5_av_etot300K_density_runs.dat",
              "../Data/SnO_av_etot300K_density_runs_1.dat", "../Data/Ta2Sn10O15_av_etot300K_density_runs.dat",
              "../Data/Ta2Sn3O8_av_etot300K_density_runs.dat", "../Data/Ta2SnO6_av_etot300K_density_runs.dat"]

# ===== Initialization =====
row = 0
col = 0
fig, ax = plt.subplots(3, 2)
k = 0

# ===== Data Collection =====
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

    ax[row, col].scatter(density_list, energies, color="orange", marker=".")
    # ax[row, col].scatter(temp1, average_array, color="deepskyblue")
    ax[row, col].scatter(temp1, average_array, color="tomato")

    ax[row, col].plot(temp1, average_array, color="black")
    for spine in ax[row, col].spines.values():
        spine.set_linewidth(1.8)

    ax[row, col].tick_params(axis='both', labelsize=11)
    ax[row, col].grid(True, alpha=0.35)

    col += 1
    if col == 2:
        row += 1
        col = 0
    k += 1

# ===== Formatting =====
ax[0, 0].set_title(r'$\mathrm{SnO_2}$', loc='center', fontsize='17')
ax[0, 1].set_title(r'$\mathrm{Ta_2O_5}$', loc='center', fontsize='17')
ax[1, 0].set_title(r'$\mathrm{SnO}$', loc='center', fontsize='17', fontweight = 'bold')
ax[1, 1].set_title(r'$\mathrm{Ta_2Sn_{10}O_{15}}$', loc='center', fontsize='17')
ax[2, 0].set_title(r'$\mathrm{Ta_2Sn_3O_8}$', loc='center', fontsize='17')
ax[2, 1].set_title(r'$\mathrm{Ta_2SnO_6}$', loc='center', fontsize='17')

for a in ax.flat:
    a.set_ylim(-40, 75)
    a.set_yticks(np.arange(-40, 75, 20))


x_min_1, x_max_1 = 5.0, 7.5
ax[0, 0].set_xlim(5.0, 7.5)
ax[0, 0].set_xticks(np.arange(x_min_1, x_max_1, 1))

x_min_2, x_max_2 = 4.5, 9
ax[0, 1].set_xlim(x_min_2, x_max_2)
ax[0, 1].set_xticks(np.arange(x_min_2 + 1, x_max_2, 1))
ax[0, 1].set_xticks([5, 6, 7, 8])

x_min_3, x_max_3 = 2, 6.5
ax[1, 0].set_xlim(x_min_3, x_max_3)
ax[1, 0].set_xticks(np.arange(x_min_3, x_max_3, 1))

x_min_4, x_max_4 = 1.5, 7
ax[1, 1].set_xlim(x_min_4, x_max_4)
ax[1, 1].set_xticks(np.arange(x_min_4 + 1, x_max_4 + 1, 1))
ax[1, 1].set_xticks([2, 3, 4, 5, 6, 7])

x_min_5, x_max_5 = 3, 8
ax[2, 0].set_xlim(x_min_5, x_max_5)
ax[2, 0].set_xticks(np.arange(x_min_5, x_max_5, 1))

x_min_6, x_max_6 = 4, 8.5
ax[2, 1].set_xlim(x_min_6, x_max_6)
ax[2, 1].set_xticks(np.arange(x_min_6 + 1, x_max_6 + 1, 1))

ax[1, 0].set_ylabel(r'$\mathrm{ΔE, meV/atom}$', fontsize='18.5')
# ax[1, 0].yaxis.set_label_coords(-0.3, 0.2)

ax[1, 1].set_yticklabels([])
ax[2, 1].set_yticklabels([])
ax[0, 1].set_yticklabels([])
ax[2, 0].set_xlabel(r'$\mathrm{Density, g/cm}^3$', fontsize='19')
ax[2, 0].xaxis.set_label_coords(1, -0.3)

plt.subplots_adjust(left=0.33,
                    bottom=0.137,
                    right=0.67,
                    top=0.9,
                    wspace=0.0,
                    hspace=0.61)

if SAVEPDF == True:
    plt.savefig('energy_vs_density_figure.pdf', format='pdf')
plt.show()
