import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.widgets import Slider

# ===== User Input =====
DEST_DIR = '../SrSnO'

densities = ["6p27", "5p74", "5p27", "4p85", "4p47", "4p13", "3p82"]
num_atoms = [138, 134]
color = ["orange", "green"]
k = 0
SAVEPDF = False

# ===== Initialization =====
file_names = ["../Data/SnO_av_etot300K_density_runs_1.dat",
              "../Data/Ta2Sn10O15_av_etot300K_density_runs.dat"]

fig, ax = plt.subplots(figsize=(5, 3))
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

ax.plot(density_values, average_values, color='black', linestyle='-', linewidth=3, alpha=1, zorder=2)
ax.scatter(density_values, average_values, color='firebrick', label="Average", zorder=2)

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
        i = i.split("_")[1]
        i = i.replace("d", "").replace("p", ".")
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
        energies[i] -= smallest
        energies[i] /= num_atoms[k]

    for i in range(len(average_array)):
        average_array[i] -= smallest
        average_array[i] /= num_atoms[k]

    # Convert to meV Units
    for i in range(len(energies)):
        energies[i] *= 1000
    for i in range(len(average_array)):
        average_array[i] *= 1000

    ax.scatter(temp1, average_array, color=color[k], alpha=0.5)
    ax.plot(temp1, average_array, color="black", linestyle="dashed", alpha=0.5, zorder=1)
    k += 1

legend_entry = [
    Line2D([0], [0], color='black', linestyle='-', linewidth=3, marker='o', markersize=8, markerfacecolor='firebrick',
           label=r'$\mathrm{Sr_{7}Sn_{62}O_{69}}$'),
    Line2D([0], [0], color='black', linestyle='-', linewidth=3, marker='o', markersize=8, markerfacecolor='orange',
           label='SnO'),
    Line2D([0], [0], color='black', linestyle='-', linewidth=3, marker='o', markersize=8, markerfacecolor='green',
           label=r'$\mathrm{Ta_{2}Sn_{10}O_{15}}$')
]

fig = plt.gcf()
fig.set_size_inches(6, 3.5)

ax.set_title("a-SrSnO Energy vs. Density", fontsize=19)
ax.set_xlabel(r'$\mathrm{Density, g/cm}^3$', fontsize=17)
ylabel = ax.set_ylabel(r'$\mathrm{ΔE, meV/atom}$', fontsize=17)
ax.legend(loc='upper left', handles=legend_entry, fontsize=12)
ax.grid(True, alpha=0.25)
for spine in ax.spines.values():
    spine.set_linewidth(1.8)
plt.subplots_adjust(bottom=0.186, left=0.275, right=0.745)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.yaxis.set_label_coords(-0.172, 0.5)



# --- Adjust y-axis title using a slider ---
t = False
if t == True:
    # Get the initial coordinates of the y-axis label
    init_coords = ax.yaxis.get_label().get_position()

    # Create a slider for adjusting the x-coordinate
    slider_ax = plt.axes([0.15, 0.05, 0.65, 0.03])  # [left, bottom, width, height]
    x_slider = Slider(slider_ax, 'Y-Label X', -1.5, 0.5, valinit=init_coords[0])


    # Callback function to update the y-axis label's position
    def update(val):
        new_x = x_slider.val
        # Set the new x coordinate while keeping the original y coordinate
        ax.yaxis.set_label_coords(new_x, init_coords[1])
        fig.canvas.draw_idle()
        print(f"New Y-label position: x = {new_x:.3f}, y = {init_coords[1]:.3f}")

    x_slider.on_changed(update)

plt.show()

if SAVEPDF:
    plt.savefig('SrSnO_single_figure.pdf', format='pdf')
