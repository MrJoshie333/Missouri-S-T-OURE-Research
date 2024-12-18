import matplotlib.pyplot as plt
import numpy as np

colors_1 = ['#7f0000', '#b30000', '#ef6548', '#fc4e2a', '#fd8d3c', '#fc9272', '#fc8d59', '#fdbb84', '#fcbba1',
            '#fdd49e', '#fee8c8', 'red', 'blue', 'green', 'yellow', 'orange', 'purple']
colors_2 = ['#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df', '#cce6f8']

# ===== Graphing =====
fig, axs = plt.subplots(nrows=4, ncols=2)


def graph(file_names, rowNum):
    b = file_names[0]
    b = b[:-30]
    #print(b)
    density_leg = []
    count = 0
    with open(f'{b}_density.dat') as g:
        density_data = g.readlines()
    for i in density_data:
        density_leg.append(float(i))

    for a in file_names:
        with open(a) as f:
            data = f.readlines()

        angle = []
        density = []

        for i in data:
            rowData = i.split("\t")
            angle.append(float(rowData[0]))
            density.append([float(x) for x in rowData[1:]])

        columnData = [[] for i in density[0]]
        for sublist in density:
            for col in range(len(sublist)):
                columnData[col].append(sublist[col])

        a = a[14:]
        a = a[:-12]

        density_count = 0
        for i in columnData:
            axs[rowNum, count].plot(angle, i, label=r'' + f'{density_leg[density_count]}',
                                    color=colors_1[density_count])
            density_count += 1

        count += 1
    # axs[rowNum,0].set_xticklabels([])
    # axs[rowNum,1].set_xticklabels([])
    if (rowNum == 2):
        pass
    else:
        axs[rowNum, 1].set_yticklabels([])
        # axs[rowNum,2].set_yticklabels([])


# ===== Data Processing =====
file_names = [["Data/SnO2_distrib_angle_MOM_density.dat", "Data/SnO2_distrib_angle_OSnO_density.dat"],
              ["Data/Ta2O5_distrib_angle_MOM_density.dat", "Data/Ta2O5_distrib_angle_OTaO_density.dat"]]

rowNum = 0
while rowNum < 2:
    graph(file_names[rowNum], rowNum)
    rowNum += 1

file_names = ["Data/SnO_distrib_angle_MOM_density.dat", "Data/SnO_distrib_angle_OSnO_density.dat"]
count = 0

color_1 = []
color_2 = []
density_leg_1 = []
density_leg_2 = []

with open("Data/SnO_density.dat") as g:
    density_data = g.readlines()
for i in density_data:
    density_leg_1.append(float(i))
del density_leg_1[10:]

for i in density_data:
    density_leg_2.append(float(i))
del density_leg_2[:10]

for a in file_names:
    with open(a) as f:
        data = f.readlines()

    angle = []
    density_1 = []
    density_2 = []

    for i in data:
        rowData = i.split("\t")
        angle.append(float(rowData[0]))
        density_1.append([float(x) for x in rowData[1:11]])
        density_2.append([float(x) for x in rowData[11:]])
    # print(density_1)
    # print(density_2)
    columnData1 = [[] for i in density_1[0]]
    for sublist in density_1:
        for col in range(len(sublist)):
            columnData1[col].append(sublist[col])
    columnData2 = [[] for i in density_2[0]]
    for sublist in density_2:
        for col in range(len(sublist)):
            columnData2[col].append(sublist[col])

    colors_1 = ['#610202', '#871e0d', '#ad390f', '#d2560e', '#f67503', '#fc9336', '#fba652', '#f9b86e', '#f8c88c',
                '#FFE7C4']
    colors_2 = ['#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df', '#cce6f8']
    a = a[14:]
    a = a[:-12]
    density_count = 0
    for i in columnData1:
        axs[2, count].plot(angle, i, label=r'' + f'{density_leg_1[density_count]}',
                           color=colors_1[density_count])  # , color=colors[iteration])
        density_count += 1
    density_count = 0
    for i in columnData2:
        axs[3, count].plot(angle, i, label=r'' + f'{density_leg_2[density_count]}',
                           color=colors_2[density_count])
        density_count += 1
    count += 1

i = 0
j = 0

# ===== Graph Formatting =====
while i < 4:

    axs[i, j].tick_params(axis='y', labelsize=13)
    axs[i, j].tick_params(axis='x', labelsize=13)
    axs[i, j].set_xlim(50, 180)
    axs[i, j].grid(True, alpha=0.25)
    axs[i, j].set_ylim(-.0001, 0.038)
    axs[i, j].set_yticks(np.arange(0, 0.04, 0.01))
    axs[i, j].set_xticks(np.arange(60, 180, 30))
    j += 1
    if j == 2:
        i += 1
        j = 0

axs[1, 1].set_xlabel(r'Angle ($^{\circ}$)', fontsize='20')
axs[2, 0].set_ylabel('Probability Density', fontsize='20')
axs[1, 1].xaxis.set_label_coords(0, -.25)
axs[2, 0].yaxis.set_label_coords(-.33, 0)

axs[0, 1].legend(loc='right', title=r'Density (g/$\mathrm{cm}^3$)', bbox_to_anchor=(2.3, 0.5), prop={"size": 12},
                 ncols=2)
axs[1, 1].legend(loc='right', bbox_to_anchor=(2.3, 0.5), prop={"size": 12}, ncols=2)
axs[2, 1].legend(loc='right', bbox_to_anchor=(2.3, 0.5), prop={"size": 12}, ncols=2)
axs[3, 1].legend(loc='right', bbox_to_anchor=(2.3, 0.5), prop={"size": 12}, ncols=2)

axs[0, 0].text(55, 0.031, "(a)", fontsize=16)
axs[1, 0].text(55, 0.031, "(d)", fontsize=16)
axs[2, 0].text(55, 0.031, "(b)", fontsize=16)
axs[3, 0].text(55, 0.031, "(c)", fontsize=16)

axs[0, 0].text(138, 0.031, r'$\mathrm{SnO_2}$', fontsize=16)
axs[1, 0].text(128, 0.031, r'$\mathrm{Ta_2O_5}$', fontsize=16)

axs[2, 0].text(138, 0.031, r'$\mathrm{SnO}$', fontsize=16)
axs[3, 0].text(138, 0.031, r'$\mathrm{SnO}$', fontsize=16)

plt.subplots_adjust(left=0.40,
                    # bottom=0.1,
                    right=0.60,
                    # top=0.9,
                    wspace=-.0005,
                    hspace=0.5
                    )

# Retrieve positions
positions = [axs[i, j].get_position() for i in range(4) for j in range(2)]

# Reassign positions
axs[1, 0].set_position(positions[6])  # pos7
axs[1, 1].set_position(positions[7])  # pos8
axs[2, 0].set_position(positions[2])  # pos3
axs[2, 1].set_position(positions[3])  # pos4
axs[3, 0].set_position(positions[4])  # pos5
axs[3, 1].set_position(positions[5])  # pos6

axs[2, 0].set_xticklabels([])
axs[2, 1].set_xticklabels([])
axs[3, 1].set_xticklabels([])
axs[3, 0].set_xticklabels([])
axs[0, 0].set_xticklabels([])
axs[0, 1].set_xticklabels([])

axs[3, 1].set_yticklabels([])
axs[2, 1].set_yticklabels([])

axs[0, 0].set_title('M-O-M', fontsize=20)
axs[0, 1].set_title('O-Sn-O', fontsize=20)
axs[1, 0].set_title('M-O-M', fontsize=20)
axs[1, 1].set_title('O-Ta-O', fontsize=20)

plt.show()
