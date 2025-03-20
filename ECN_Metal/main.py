# ===== ECN_Metal =====
# ===== Joshua Santy =====

import matplotlib.pyplot as plt
import numpy as np

from utility import extract_density, filenameToLatex, read_dat_file_to_lists


# Function to process density strings from a list
def extract_density_from_list(orig_density):
    density_list = []
    for item in orig_density:
        density = extract_density(item)
        if density is not None:
            density_list.append(density)
    return density_list


fig, axs = plt.subplots(2, 3)

# ===== SnO2 =====
with open("Data/SnO2/ECN_Sn-Sn_average.dat") as f:
    data_2 = f.readlines()
orig_density_1 = []
ECN_1 = []
ECN_time_1 = []
L_ave_1 = []
L_ave_time_1 = []
Distortion_1 = []
Distortion_time_1 = []
rowData_1 = []

for i in data_2:
    rowData_1 = i.split(" ")
    orig_density_1.append(rowData_1[0])
    ECN_1.append(float(rowData_1[2]))
    ECN_time_1.append(float(rowData_1[3]))
    L_ave_1.append(float(rowData_1[4]))
    L_ave_time_1.append(float(rowData_1[5]))
    Distortion_1.append(float(rowData_1[6]))
    Distortion_time_1.append(float(rowData_1[7]))

density_list_SnO2 = []
for i in orig_density_1:
    i = i.split("_")
    i = i[1]
    i = i.replace("d", "")
    i = i.replace("p", ".")
    i = float(i)
    density_list_SnO2.append(i)

axs[0, 0].plot(density_list_SnO2, ECN_1, label="SnO$_2$", color="limegreen")
axs[1, 0].plot(density_list_SnO2, ECN_time_1, label="SnO$_2$", color="limegreen")
axs[0, 1].plot(density_list_SnO2, L_ave_1, label="SnO$_2$", color="limegreen")
axs[1, 1].plot(density_list_SnO2, L_ave_time_1, label="SnO$_2$", color="limegreen")
axs[0, 2].plot(density_list_SnO2, Distortion_1, label="SnO$_2$", color="limegreen")
axs[1, 2].plot(density_list_SnO2, Distortion_time_1, label="SnO$_2$", color="limegreen")

# ===== Iterating the Others =====

colors = ["darkred", "#1f77b4", "red", "darkorange", "gold", "blueviolet", "darkblue", "dodgerblue"]


# Function to plot the data
def plot_data(axs, density_list, data_dict, label, color):
    axs[0, 0].plot(density_list, data_dict["ECN"], label=label, color=color)
    axs[1, 0].plot(density_list, data_dict["ECN_time"], label=label, color=color)
    axs[0, 1].plot(density_list, data_dict["L_ave"], label=label, color=color)
    axs[1, 1].plot(density_list, data_dict["L_ave_time"], label=label, color=color)
    axs[0, 2].plot(density_list, data_dict["Distortion"], label=label, color=color)
    axs[1, 2].plot(density_list, data_dict["Distortion_time"], label=label, color=color)


# File paths and labels
file_names = [
    ("Data/SnO/ECN_Sn-Sn_average.dat", "Sn-Sn"),
    ("Data/Ta2O5/ECN_Ta-Ta_average.dat", "Sn-Ta"),
    ("Data/Ta2Sn10O15/ECN_Sn-Sn_average.dat", "Sn-Sn"),
    ("Data/Ta2Sn3O8/ECN_Sn-Sn_average.dat", "Sn-Sn"),
    ("Data/Ta2SnO6/ECN_Sn-Sn_average.dat", "Sn-Sn"),
    ("Data/Ta2Sn10O15/ECN_Sn-Ta_average.dat", "Sn-Ta"),
    ("Data/Ta2Sn3O8/ECN_Sn-Ta_average.dat", "Sn-Ta"),
    ("Data/Ta2SnO6/ECN_Sn-Ta_average.dat", "Sn-Ta"),
]
# Iterate through the files and plot
for idx, (file_path, label_type) in enumerate(file_names):
    orig_density, _, ECN, ECN_time, L_ave, L_ave_time, Distortion, Distortion_time = read_dat_file_to_lists(
        file_path, " ", skip_first_line=False
    )

    # Extract density list
    density_list = extract_density_from_list(orig_density)

    # Generate compound label
    compound = filenameToLatex(file_path, 2)

    # Plot data on the subplots
    axs[0, 0].plot(density_list, ECN, label=f"{label_type}:{compound}", color=colors[idx % len(colors)])
    axs[1, 0].plot(density_list, ECN_time, label=f"{label_type}:{compound}", color=colors[idx % len(colors)])
    axs[0, 1].plot(density_list, L_ave, label=f"{label_type}:{compound}", color=colors[idx % len(colors)])
    axs[1, 1].plot(density_list, L_ave_time, label=f"{label_type}:{compound}", color=colors[idx % len(colors)])
    axs[0, 2].plot(density_list, Distortion, label=f"{label_type}:{compound}", color=colors[idx % len(colors)])
    axs[1, 2].plot(density_list, Distortion_time, label=f"{label_type}:{compound}",
                   color=colors[idx % len(colors)])

# ===== Plot Formatting =====
for a in axs[1, :].flat:
    a.set_xlabel(r'Density, g/$\mathrm{cm^3}$', fontsize=18)

axs[0, 0].set_ylabel("ECN", fontsize=18, labelpad=20)
axs[1, 0].set_ylabel("ECN Time Variance", fontsize=18, labelpad=20)
axs[0, 1].set_ylabel(r'L_Average, $\AA$', fontsize=18, labelpad=20)
axs[1, 1].set_ylabel("L_Average Time Variance", fontsize=18, labelpad=20)
axs[0, 2].set_ylabel(r'Distortion, $\AA^2$', fontsize=18, labelpad=20)
axs[1, 2].set_ylabel("Distortion Time Variance", fontsize=18, labelpad=20)

for i in range(2):
    for j in range(3):
        axs[i, j].tick_params(axis='x', labelsize=13)
        axs[i, j].tick_params(axis='y', labelsize=13)

plt.subplots_adjust(
    wspace=0.425,
    hspace=0.0)

axs[1, 0].set_yticks(np.arange(0.05, 1, 0.2))
axs[0, 1].set_yticks(np.arange(3, 4, 0.2))
axs[1, 1].set_yticks(np.arange(0.05, 0.5, 0.1))

for a in axs.flat:
    a.tick_params(axis='x', labelsize=15)
    a.tick_params(axis='y', labelsize=15)
    a.grid(True, alpha=0.25)

axs[0, 1].lines[1].set_label("SnO")
axs[0, 1].lines[2].set_label(r'$\mathrm{Ta_2O_5}$')
axs[0, 1].legend(prop={'size': 16}, loc='upper center', bbox_to_anchor=(0.5, 1.339), ncol=3, fancybox=True, shadow=True,
                 fontsize='large')
plt.show()
