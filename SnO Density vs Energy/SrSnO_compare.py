"""
Density vs Energy Plotter, SrSnO Comparison
Joshua Santy

Be sure to change num_atoms to however many atoms were used

"""
import matplotlib.pyplot as plt
import numpy as np

# ===== User Input =====
num_atoms = [138, 140, 138, 135, 130, 134]
file_names = ["Data/SnO2_av_etot300K_density_runs.dat", "Data/TaO5_av_etot300K_density_runs.dat",
              "Data/SnO_av_etot300K_density_runs_1.dat", "Data/Ta2Sn10O15_av_etot300K_density_runs.dat",
              "Data/Ta2Sn3O8_av_etot300K_density_runs.dat", "Data/Ta2SnO6_av_etot300K_density_runs.dat"]
# Save the Figure as a PDF?
SAVEPDF = False

# ===== Initialization =====
row = 0
col = 0
fig, ax = plt.subplots(3, 2)
k = 0

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
    average_array = []
    count = 0
    straight_counter = 0
    for values in temp1:
        tot_sum = sum(energies[count:count + density_count[straight_counter]])
        average_array.append(tot_sum / density_count[straight_counter])
        count += density_count[straight_counter]
        straight_counter += 1

    smallest = min(average_array)

    # Energy Values:
    for i in range(len(energies)):
        energies[i] -= smallest  # 765.2191713
        energies[i] /= num_atoms[k]  # make this general as well

    for i in range(len(average_array)):
        average_array[i] -= smallest
        average_array[i] /= num_atoms[k]

    # meV Units
    for i in range(len(energies)):
        energies[i] *= 1000
    for i in range(len(average_array)):
        average_array[i] *= 1000

    # ===== Plotting =====
    ax[row, col].scatter(density_list, energies, color="orange")
    ax[row, col].scatter(temp1, average_array, color="deepskyblue")
    ax[row, col].plot(temp1, average_array, color="black")

    ax[row, col].tick_params(axis='x', labelsize=13)
    ax[row, col].tick_params(axis='y', labelsize=13)
    ax[row, col].spines['bottom'].set_linewidth(1.8)
    ax[row, col].spines['left'].set_linewidth(1.8)
    ax[row, col].spines['right'].set_linewidth(1.8)
    ax[row, col].spines['top'].set_linewidth(1.8)
    ax[row, col].grid(True, alpha=0.35)

    col += 1
    if col == 2:
        row += 1
        col = 0
    k += 1
ax[0, 0].set_title(r'Amorphous $\mathrm{SnO_2}$', loc='center', fontsize='17')
ax[0, 1].set_title(r'Amorphous $\mathrm{Ta_2O_5}$', loc='center', fontsize='17')
ax[1, 0].set_title(r'Amorphous $\mathrm{SnO}$', loc='center', fontsize='17')
ax[1, 1].set_title(r'Amorphous $\mathrm{Ta_2Sn_{10}O_{15}}$', loc='center', fontsize='17')
ax[2, 0].set_title(r'Amorphous $\mathrm{Ta_2Sn_3O_8}$', loc='center', fontsize='17')
ax[2, 1].set_title(r'Amorphous $\mathrm{Ta_2SnO_6}$', loc='center', fontsize='17')

for a in ax.flat:
    a.set_ylim(-40, 75)
    a.set_yticks(np.arange(-40, 75, 20))

x_min_1, x_max_1 = 5.0, 7.5
ax[0, 0].set_xlim(x_min_1, x_max_1)
ax[0, 0].set_xticks(np.arange(x_min_1, x_max_1, 1))

x_min_3, x_max_3 = 2.5, 6.5
ax[1, 0].set_xlim(x_min_3, x_max_3)
ax[1, 0].set_xticks(np.arange(x_min_3, x_max_3, 1))

x_min_4, x_max_4 = 1.5, 7
ax[1, 1].set_xlim(x_min_4, x_max_4)
ax[1, 1].set_xticks(np.arange(x_min_4 + 1, x_max_4 + 1, 1))

x_min_5, x_max_5 = 3, 8
ax[2, 0].set_xlim(x_min_5, x_max_5)
ax[2, 0].set_xticks(np.arange(x_min_5, x_max_5, 1))

x_min_6, x_max_6 = 4, 8.5
ax[2, 1].set_xlim(x_min_6, x_max_6)
ax[2, 1].set_xticks(np.arange(x_min_6 + 1, x_max_6 + 1, 1))

ax[0, 0].set_ylabel(r'$\mathrm{ΔE, meV/atom}$', fontsize='18.5')
ax[1, 0].set_ylabel(r'$\mathrm{ΔE, meV/atom}$', fontsize='18.5')
ax[2, 0].set_ylabel(r'$\mathrm{ΔE, meV/atom}$', fontsize='18.5')
ax[1, 1].set_yticklabels([])
ax[2, 1].set_yticklabels([])
ax[2, 0].set_xlabel(r'Density, g/$cm^3$', fontsize='19')
ax[2, 0].xaxis.set_label_coords(1, -0.2)

plt.subplots_adjust(left=0.33,
                    bottom=0.137,
                    right=0.67,
                    top=0.9,
                    wspace=0.0,
                    hspace=0.61)
ax[0, 1].cla()

# ===== SrSnO =====

DEST_DIR = './SrSnO'
densities = ["6p27", "5p74", "5p27", "4p85", "4p47", "4p13", "3p82"]
average_values = []
density_values = []

# Step 1: Calculate the average for each density
density_averages = {}
for density in densities:
    file_name = f"{DEST_DIR}/etot300k_{density}"
    data = np.loadtxt(file_name)
    avg_value = np.mean(data)
    density_averages[density] = avg_value

# Step 2: Find the lowest average value
min_average = min(density_averages.values())

# Step 3: Process each file and adjust based on the lowest average
for density in densities:
    # Define the file path
    file_name = f"{DEST_DIR}/etot300k_{density}"

    # Read the data from the file
    data = np.loadtxt(file_name)

    # Normalize the data by subtracting the minimum average value
    normalized_data = data - min_average

    # Scale the normalized data
    scaled_data = (normalized_data / 138) * 1000

    # Calculate the average of the scaled data
    avg_scaled_data = np.mean(scaled_data)

    # Store the average and the corresponding density value
    average_values.append(avg_scaled_data)
    density_values.append(float(density.replace('p', '.')))  # Convert density to a float (e.g., '6p27' -> 6.27)

    # Plotting the scaled energy values (scatter plot)
    ax[0, 1].scatter([density_values[-1]] * len(scaled_data), scaled_data, alpha=0.7)
ax[0, 1].plot(density_values, average_values, marker='o', color='black', label="Average", linestyle='-', linewidth=2)

x_min_2, x_max_2 = 3.5, 6.5
ax[0, 1].set_xlim(x_min_2, x_max_2)
ax[0, 1].set_xticks([4, 5, 6])
ax[0, 1].set_ylim(-40, 75)
ax[0, 1].set_yticks(np.arange(-40, 80, 20))
ax[0, 1].set_yticklabels([])
ax[0, 1].grid(True, linewidth=0.5, color='gray')
ax[0, 1].set_title("Amorphous SrSnO (10% Sr)", loc='center', fontsize='17')

plt.show()

if SAVEPDF:
    plt.savefig('SrSnO_Compare_Density_vs_Energy.pdf', bbox_inches='tight')
