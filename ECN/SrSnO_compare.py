import matplotlib.pyplot as plt
import numpy as np
from utility import filenameToLatex

# ===== Setup =====
# Save the Figure as a PDF?
SAVEPDF = False
num_atoms = 69


# Function to find the closest x value corresponding to the average y value
def find_closest_x(x_values, y_values, avg_y):
    closest_idx = np.argmin(np.abs(np.array(y_values) - avg_y))  # Find index of closest y-value to avg_y
    return x_values[closest_idx]

# Line 4 of ECN_Sn-O_average.dat, the outlier
with open("Data/ECN_Sn-O_average.dat") as f:
    next(f)  # skips header line
    data_1 = f.readlines()

'''---------------------- Data And Plotting for SnO ----------------------'''
iteration = 0
warm_color = ["red", "gold", "darkorange"]
cool_color = ["blueviolet", "dodgerblue", "darkblue"]
orig_density = []
ECN = []
rowData = []

for i in data_1:
    rowData = i.split(" ")

    orig_density.append(rowData[0])
    ECN.append(float(rowData[2]))

'''Getting Density'''
density_list = []
for i in orig_density:
    i = i.split("_")
    i = i[1]
    i = i.replace("d", "")
    i = i.replace("p", ".")
    i = float(i)
    density_list.append(i)

fig, axs = plt.subplots(1, 1)
axs.plot(density_list, ECN, label="SnO", color="darkred")

# Calculate and plot the average point for SnO
avg_y_sno = np.mean(ECN)
avg_x_sno = find_closest_x(density_list, ECN, avg_y_sno)
axs.scatter(avg_x_sno, avg_y_sno, color='darkred', zorder=5)  # Plot the average point
axs.text(avg_x_sno, avg_y_sno + 0.1, f'{avg_y_sno:.2f}', color='darkred', fontsize=12, ha='center')  # Label the point

'''---------------------- Data And Plotting for the other 3  ----------------------'''
file_names = ["Data/ECN_Ta2Sn10O15_average.dat", "Data/ECN_Ta2SnO6_average.dat", "Data/ECN_Ta2Sn3O8_average.dat"]
for a in file_names:
    Sn = []
    Ta = []
    with open(a) as f:
        for count, line in enumerate(f, start=0):
            if count % 2 == 0:
                Sn.append(line)
            else:
                Ta.append(line)
    '''Getting Density'''
    orig_density_Sn = []
    ECN_Sn = []
    rowData_Sn = []

    orig_density_Ta = []
    ECN_Ta = []
    rowData_Ta = []

    for i in Sn:
        rowData = i.split(" ")
        orig_density_Sn.append(rowData[0])
        ECN_Sn.append(float(rowData[2]))

    for j in Ta:
        if len(j) > 2:
            rowData_Ta = j.split(" ")
            orig_density_Ta.append(rowData_Ta[0])
            ECN_Ta.append(float(rowData_Ta[2]))

    '''Getting Densities'''
    density_list_Sn = []
    for i in orig_density_Sn:
        i = i.split("_")
        i = i[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list_Sn.append(i)

    density_list_Ta = []
    for i in orig_density_Ta:
        i = i.split("_")
        i = i[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list_Ta.append(i)

    '''Parsing for the Label'''
    a = filenameToLatex(a)

    axs.plot(density_list_Sn, ECN_Sn, label=f'Sn-O:{a}', color=warm_color[iteration])
    axs.plot(density_list_Ta, ECN_Ta, label=f'Ta-O:{a}', color=cool_color[iteration])

    # Calculate and plot the average point for Sn and Ta
    avg_y_sn = np.mean(ECN_Sn)
    avg_x_sn = find_closest_x(density_list_Sn, ECN_Sn, avg_y_sn)
    axs.scatter(avg_x_sn, avg_y_sn, color=warm_color[iteration], zorder=5)
    axs.text(avg_x_sn, avg_y_sn + 0.1, f'{avg_y_sn:.2f}', color=warm_color[iteration], fontsize=12, ha='center')

    avg_y_ta = np.mean(ECN_Ta)
    avg_x_ta = find_closest_x(density_list_Ta, ECN_Ta, avg_y_ta)
    axs.scatter(avg_x_ta, avg_y_ta, color=cool_color[iteration], zorder=5)
    axs.text(avg_x_ta, avg_y_ta + 0.1, f'{avg_y_ta:.2f}', color=cool_color[iteration], fontsize=12, ha='center')

    iteration += 1

'''SnO2:----------------'''
with open("Data/ECN_Sn-O2_average.dat") as f:
    data_2 = f.readlines()
orig_density_1 = []
ECN_1 = []
rowData_1 = []

for i in data_2:
    rowData_1 = i.split(" ")
    orig_density_1.append(rowData_1[0])
    ECN_1.append(float(rowData_1[2]))

'''Getting Density'''
density_list_SnO2 = []
for i in orig_density_1:
    i = i.split("_")
    i = i[1]
    i = i.replace("d", "")
    i = i.replace("p", ".")
    i = float(i)
    density_list_SnO2.append(i)

axs.plot(density_list_SnO2, ECN_1, label=r'$\mathrm{SnO_2}$', color="limegreen")

# Calculate and plot the average point for SnO2
avg_y_sno2 = np.mean(ECN_1)
avg_x_sno2 = find_closest_x(density_list_SnO2, ECN_1, avg_y_sno2)
axs.scatter(avg_x_sno2, avg_y_sno2, color='limegreen', zorder=5)  # Plot the average point
axs.text(avg_x_sno2, avg_y_sno2 + 0.1, f'{avg_y_sno2:.2f}', color='limegreen', fontsize=12,
         ha='center')  # Label the point

'''Ta-O -----------'''
with open("Data/ECN_Ta-O_average.dat") as f:
    data_3 = f.readlines()
orig_density_2 = []
ECN_2 = []
rowData_2 = []

for i in data_3:
    rowData_2 = i.split(" ")
    orig_density_2.append(rowData_2[0])
    ECN_2.append(float(rowData_2[2]))

'''Getting Density'''
density_list_Ta_O = []
for i in orig_density_2:
    i = i.split("_")
    i = i[1]
    i = i.replace("d", "")
    i = i.replace("p", ".")
    i = float(i)
    density_list_Ta_O.append(i)

axs.plot(density_list_Ta_O, ECN_2, label=r'$\mathrm{Ta_2O_5}$')

# Calculate and plot the average point for Ta-O
avg_y_ta_o = np.mean(ECN_2)
avg_x_ta_o = find_closest_x(density_list_Ta_O, ECN_2, avg_y_ta_o)
axs.scatter(avg_x_ta_o, avg_y_ta_o, color='blue', zorder=5)  # Plot the average point
axs.text(avg_x_ta_o, avg_y_ta_o + 0.1, f'{avg_y_ta_o:.2f}', color='blue', fontsize=12, ha='center')  # Label the point

axs.set_ylabel("ECN", fontsize=18, labelpad=20)
axs.tick_params(axis='y', labelsize=13)
axs.tick_params(axis='x', labelsize=13)

plt.subplots_adjust(wspace=0.425, hspace=0.0)

# Add horizontal solid lines with different colors (brown and gray)
axs.axhline(y=4.31456, color='brown', linestyle='-', linewidth=2, label='Sr-O: SrSnO')
axs.axhline(y=2.73034, color='gray', linestyle='-', linewidth=2, label='Sn-O: SrSnO')

# Ensure the legend includes the new lines
handles, labels = axs.get_legend_handles_labels()
axs.legend(handles, labels, loc='lower right')

axs.set_xlabel("Density (g/cm³)", fontsize=18, labelpad=20)

plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
axs.grid(True, linestyle='--')

plt.show()
if SAVEPDF == True:
    plt.savefig('ECN_compare.png', dpi=300, bbox_inches='tight')
