import matplotlib.pyplot as plt
import numpy as np

from utility import filenameToLatex

# ===== Setup =====
# Save the Figure as a PDF?
SAVEPDF = False
num_atoms = 69

'''---------------------- Data And Plotting for SnO ----------------------'''
# Line 4 of ECN_Sn-O_average.dat, the outlier
# a14p1_d5p51 Sn 2.86306 0.0543204 2.15148 0.00314071 0.0101796 0.000163069
with open("Data/ECN_Sn-O_average.dat") as f:
    next(f)  # skips header line
    data_1 = f.readlines()
iteration = 0
warm_color = ["red", "gold", "darkorange"]
cool_color = ["blueviolet", "dodgerblue", "darkblue"]
orig_density = []
ECN = []
ECN_time = []
L_ave = []
L_ave_time = []
Distortion = []
Distortion_time = []
rowData = []

for i in data_1:
    rowData = i.split(" ")

    orig_density.append(rowData[0])
    ECN.append(float(rowData[2]))
    ECN_time.append(float(rowData[3]))
    L_ave.append(float(rowData[4]))
    L_ave_time.append(float(rowData[5]))
    Distortion.append(float(rowData[6]))
    Distortion_time.append(float(rowData[7]))

'''Getting Density'''
density_list = []
for i in orig_density:
    i = i.split("_")
    i = i[1]
    i = i.replace("d", "")
    i = i.replace("p", ".")
    i = float(i)
    density_list.append(i)

fig, axs = plt.subplots(2, 3)
axs[0, 0].plot(density_list, ECN, label="SnO", color="darkred")
axs[1, 0].plot(density_list, ECN_time, label="SnO", color="darkred")
axs[0, 1].plot(density_list, L_ave, label="SnO", color="darkred")
axs[1, 1].plot(density_list, L_ave_time, label="SnO", color="darkred")
axs[0, 2].plot(density_list, Distortion, label="SnO", color="darkred")
axs[1, 2].plot(density_list, Distortion_time, label="SnO", color="darkred")

'''---------------------- Data And Plotting for the other 3  ----------------------'''
file_names = ["Data/ECN_Ta2Sn10O15_average.dat", "Data/ECN_Ta2SnO6_average.dat", "Data/ECN_Ta2Sn3O8_average.dat"]
for a in file_names:
    cleanName = a.replace("Data/ECN_", "")
    cleanName = cleanName.replace("_average.dat", "")
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
    ECN_time_Sn = []
    L_ave_Sn = []
    L_ave_time_Sn = []
    Distortion_Sn = []
    Distortion_time_Sn = []
    rowData_Sn = []

    orig_density_Ta = []
    ECN_Ta = []
    ECN_time_Ta = []
    L_ave_Ta = []
    L_ave_time_Ta = []
    Distortion_Ta = []
    Distortion_time_Ta = []
    rowData_Ta = []

    for i in Sn:
        rowData = i.split(" ")
        orig_density_Sn.append(rowData[0])
        ECN_Sn.append(float(rowData[2]))
        ECN_time_Sn.append(float(rowData[3]))
        L_ave_Sn.append(float(rowData[4]))
        L_ave_time_Sn.append(float(rowData[5]))
        Distortion_Sn.append(float(rowData[6]))
        Distortion_time_Sn.append(float(rowData[7]))

    for j in Ta:
        if len(j) > 2:
            rowData_Ta = j.split(" ")
            orig_density_Ta.append(rowData_Ta[0])
            ECN_Ta.append(float(rowData_Ta[2]))
            ECN_time_Ta.append(float(rowData_Ta[3]))
            L_ave_Ta.append(float(rowData_Ta[4]))
            L_ave_time_Ta.append(float(rowData_Ta[5]))
            Distortion_Ta.append(float(rowData_Ta[6]))
            Distortion_time_Ta.append(float(rowData_Ta[7]))
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

    a = filenameToLatex(cleanName)  # Label

    axs[0, 0].plot(density_list_Sn, ECN_Sn, label=f'Sn-O:{a}', color=warm_color[iteration])
    axs[1, 0].plot(density_list_Sn, ECN_time_Sn, label=f'Sn:{a}', color=warm_color[iteration])
    axs[0, 1].plot(density_list_Sn, L_ave_Sn, label=f'Sn:{a}', color=warm_color[iteration])
    axs[1, 1].plot(density_list_Sn, L_ave_time_Sn, label=f'Sn:{a}', color=warm_color[iteration])
    axs[0, 2].plot(density_list_Sn, Distortion_Sn, label=f'Sn:{a}', color=warm_color[iteration])
    axs[1, 2].plot(density_list_Sn, Distortion_time_Sn, label=f'Sn:{a}', color=warm_color[iteration])

    axs[0, 0].plot(density_list_Ta, ECN_Ta, label=f'Ta-O:{a}', color=cool_color[iteration])
    axs[1, 0].plot(density_list_Ta, ECN_time_Ta, label=f'Ta-O:{a}', color=cool_color[iteration])
    axs[0, 1].plot(density_list_Ta, L_ave_Ta, label=f'Ta-O:{a}', color=cool_color[iteration])
    axs[1, 1].plot(density_list_Ta, L_ave_time_Ta, label=f'Ta-O:{a}', color=cool_color[iteration])
    axs[0, 2].plot(density_list_Ta, Distortion_Ta, label=f'Ta-O:{a}', color=cool_color[iteration])
    axs[1, 2].plot(density_list_Ta, Distortion_time_Ta, label=f'Ta-O:{a}', color=cool_color[iteration])
    iteration += 1

'''SnO2:----------------'''
with open("Data/ECN_Sn-O2_average.dat") as f:
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

'''Getting Density'''
density_list_SnO2 = []
for i in orig_density_1:
    i = i.split("_")
    i = i[1]
    i = i.replace("d", "")
    i = i.replace("p", ".")
    i = float(i)
    density_list_SnO2.append(i)

axs[0, 0].plot(density_list_SnO2, ECN_1, label=r'$\mathrm{SnO_2}$', color="limegreen")
axs[1, 0].plot(density_list_SnO2, ECN_time_1, label=r'$\mathrm{SnO_2}$', color="limegreen")
axs[0, 1].plot(density_list_SnO2, L_ave_1, label=r'$\mathrm{SnO_2}$', color="limegreen")
axs[1, 1].plot(density_list_SnO2, L_ave_time_1, label=r'$\mathrm{SnO_2}$', color="limegreen")
axs[0, 2].plot(density_list_SnO2, Distortion_1, label=r'$\mathrm{SnO_2}$', color="limegreen")
axs[1, 2].plot(density_list_SnO2, Distortion_time_1, label=r'$\mathrm{SnO_2}$', color="limegreen")

'''Ta-O -----------'''
with open("Data/ECN_Ta-O_average.dat") as f:
    data_3 = f.readlines()
orig_density_2 = []
ECN_2 = []
ECN_time_2 = []
L_ave_2 = []
L_ave_time_2 = []
Distortion_2 = []
Distortion_time_2 = []
rowData_2 = []

for i in data_3:
    rowData_2 = i.split(" ")
    orig_density_2.append(rowData_2[0])
    ECN_2.append(float(rowData_2[2]))
    ECN_time_2.append(float(rowData_2[3]))
    L_ave_2.append(float(rowData_2[4]))
    L_ave_time_2.append(float(rowData_2[5]))
    Distortion_2.append(float(rowData_2[6]))
    Distortion_time_2.append(float(rowData_2[7]))

'''Getting Density'''
density_list_Ta_O = []
for i in orig_density_2:
    i = i.split("_")
    i = i[1]
    i = i.replace("d", "")
    i = i.replace("p", ".")
    i = float(i)
    density_list_Ta_O.append(i)
print(density_list_Ta_O)

axs[0, 0].plot(density_list_Ta_O, ECN_2, label=r'$\mathrm{Ta_2O_5}$')
axs[1, 0].plot(density_list_Ta_O, ECN_time_2, label=r'$\mathrm{Ta_2O_5}$')
axs[0, 1].plot(density_list_Ta_O, L_ave_2, label=r'$\mathrm{Ta_2O_5}$')
axs[1, 1].plot(density_list_Ta_O, L_ave_time_2, label=r'$\mathrm{Ta_2O_5}$')
axs[0, 2].plot(density_list_Ta_O, Distortion_2, label=r'$\mathrm{Ta_2O_5}$')
axs[1, 2].plot(density_list_Ta_O, Distortion_time_2, label=r'$\mathrm{Ta_2O_5}$')

axs[1, 0].set_xlabel(r'Density, g/$cm^3$', fontsize=18)
axs[1, 1].set_xlabel(r'Density, g/$cm^3$', fontsize=18)
axs[1, 2].set_xlabel(r'Density, g/$cm^3$', fontsize=18)

axs[0, 0].set_ylabel("ECN", fontsize=18, labelpad=20)
axs[1, 0].set_ylabel("ECN Time Variance", fontsize=18, labelpad=20)
axs[0, 1].set_ylabel(r'L_Average, $\AA$', fontsize=18, labelpad=20)
axs[1, 1].set_ylabel("L_Average Time Variance", fontsize=18, labelpad=20)
axs[0, 2].set_ylabel(r'Distortion, $\AA^2$', fontsize=18, labelpad=20)
axs[1, 2].set_ylabel("Distortion Time Variance", fontsize=18, labelpad=20)

plt.subplots_adjust(
    # left=0.1,
    # bottom=0.1,
    # right=0.9,
    # top=0.9,
    wspace=0.425,
    hspace=0.0)

'''Sorting the labels in the legend'''
handles, labels = axs[0, 0].get_legend_handles_labels()
# print(labels)
handles = [handles[7], handles[0], handles[8], handles[1], handles[5], handles[3], handles[2], handles[6], handles[4]]
labels = [labels[7], labels[0], labels[8], labels[1], labels[5], labels[3], labels[2], labels[6], labels[4]]
# print(labels)

axs[0, 1].legend(handles, labels, prop={'size': 16}, loc='upper center', bbox_to_anchor=(0.5, 1.32),
                 ncol=3, fancybox=True, shadow=True, fontsize='large')

axs[1, 0].set_yticks(np.arange(0.05, 0.4, 0.1))
axs[0, 1].set_yticks(np.arange(1.90, 2.25, 0.07))
axs[1, 1].set_yticks(np.arange(0.0005, 0.004, 0.00075))

for a in axs.flat:
    a.grid(True, alpha=0.25)
    a.tick_params(axis='x', labelsize=15)
    a.tick_params(axis='y', labelsize=15)

plt.show()
if SAVEPDF == True:
    plt.savefig('ECN.pdf')
