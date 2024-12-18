import matplotlib.pyplot as plt
import numpy as np

from utility import filenameToLatex

fig, axs = plt.subplots(1, 1)
file_names = ["Data/ECN_O-SN_SnO_average.dat", "Data/ECN_O-Ta_Ta2O5_average.dat"]
iteration = 0
colors = ["red", "darkorange", "blueviolet", "dodgerblue", "darkblue"]

# ====== Data Processing =====
for a in file_names:
    with open(a) as f:
        data_1 = f.readlines()
    orig_density = []
    ECN = []
    rowData = []

    for i in data_1:
        rowData = i.split(" ")
        orig_density.append(rowData[0])
        ECN.append(float(rowData[1]))

    '''Getting Density'''
    density_list = []
    for i in orig_density:
        i = i.split("_")
        i = i[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list.append(i)

    a = a[9:]
    a = a[:-12]
    axs.plot(density_list, ECN, label=f'{a}', color=colors[iteration])

    # Compute the average ECN and find the closest density value
    avg_ECN = np.mean(ECN)
    closest_density = min(density_list, key=lambda x: abs(ECN[density_list.index(x)] - avg_ECN))

    # Plot the average ECN point and label it
    axs.scatter(closest_density, avg_ECN, color=colors[iteration], zorder=5)
    axs.text(closest_density, avg_ECN, f'{avg_ECN:.2f}', color=colors[iteration], fontsize=10, ha='right')

    iteration += 1

iteration = 2
file_names = ["Data/ECN_O-M_Ta2Sn3O8_average.dat", "Data/ECN_O-M_Ta2Sn10O15_average.dat",
              "Data/ECN_O-M_Ta2SnO6_average.dat"]
for a in file_names:
    with open(a) as f:
        data_1 = f.readlines()
    orig_density = []
    ECN = []
    rowData = []

    for i in data_1:
        rowData = i.split(" ")
        orig_density.append(rowData[0])
        ECN.append(float(rowData[1]))

    '''Getting Density'''
    density_list = []
    for i in orig_density:
        i = i.split("_")
        i = i[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list.append(i)

    a = filenameToLatex(a)
    axs.plot(density_list, ECN, label=f'O-M: {a}', color=colors[iteration])

    # Compute the average ECN and find the closest density value
    avg_ECN = np.mean(ECN)
    closest_density = min(density_list, key=lambda x: abs(ECN[density_list.index(x)] - avg_ECN))

    # Plot the average ECN point and label it
    axs.scatter(closest_density, avg_ECN, color=colors[iteration], zorder=5)
    axs.text(closest_density, avg_ECN, f'{avg_ECN:.2f}', color=colors[iteration], fontsize=10, ha='right')

    iteration += 1

with open("Data/ECN_O-Sn_SnO2_average.dat") as f:
    data_1 = f.readlines()
orig_density_1 = []
ECN_1 = []
rowData_1 = []

for i in data_1:
    rowData_1 = i.split(" ")
    orig_density_1.append(rowData_1[0])
    ECN_1.append(float(rowData_1[1]))

'''Getting Density'''
density_list_SnO2 = []
for i in orig_density_1:
    i = i.split("_")
    i = i[1]
    i = i.replace("d", "")
    i = i.replace("p", ".")
    i = float(i)
    density_list_SnO2.append(i)

axs.plot(density_list_SnO2, ECN_1, label="SnO2", color="limegreen")

# Compute the average ECN and find the closest density value
avg_ECN_SnO2 = np.mean(ECN_1)
closest_density_SnO2 = min(density_list_SnO2, key=lambda x: abs(ECN_1[density_list_SnO2.index(x)] - avg_ECN_SnO2))

# Plot the average ECN point and label it
axs.scatter(closest_density_SnO2, avg_ECN_SnO2, color="limegreen", zorder=5)
axs.text(closest_density_SnO2, avg_ECN_SnO2, f'{avg_ECN_SnO2:.2f}', color="limegreen", fontsize=10, ha='right')
axs.set_ylabel("ECN", fontsize=18, labelpad=30)
axs.axhline(y=2.38365, color='brown', linestyle='-', linewidth=2, label='O-M: SrSnO')
handles, labels = axs.get_legend_handles_labels()
axs.legend(handles, labels, loc='lower right')
axs.set_xlabel("Density (g/cm³)", fontsize=18, labelpad=20)

plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
axs.grid(True, linestyle='--')

plt.show()
