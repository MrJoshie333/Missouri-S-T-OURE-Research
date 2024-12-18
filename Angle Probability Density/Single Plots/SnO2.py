import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols = 2)
file_names = ["../Data/SnO2_distrib_angle_MOM_density.dat", "../Data/SnO2_distrib_angle_OSnO_density.dat"]
count = 0

color_1 = []
color_2 = []
density_leg = []


with open("../Data/SnO2_density.dat") as g:
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

    # https://colordesigner.io/gradient-generator
    #On the website, split between the two groups (dark red to orange, then orange to light orange)
    colors_1 =['#610202', '#871e0d', '#ad390f', '#d2560e', '#f67503' , '#f9b86e', '#f8c88c']


    colors_2 =['#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df', '#cce6f8']

    a = a[14:]
    a = a[:-12]
    density_count = 0
    for i in columnData:
        axs[count].plot(angle, i, label=r'' + f'{density_leg[density_count]}' + r' g/$\mathrm{cm}^3$', color = colors_1[density_count])#, color=colors[iteration])
        density_count += 1

    count += 1



axs[0].set_title('M-O-M', fontsize = 20)
axs[1].set_title('O-Sn-O', fontsize = 20)

j = 0

axs[1].set_yticklabels([])
while j < 2:


    axs[j].tick_params(axis = 'y', labelsize = 13)
    axs[j].tick_params(axis = 'x', labelsize = 13)
    axs[j].set_xlim(60, 180)
    axs[j].grid(True, alpha=0.25)
    axs[j].set_ylim(-.0001,0.035)
    axs[j].set_yticks(np.arange(0, 0.035, 0.01))

    axs[j].set_aspect(1.0 / axs[j].get_data_ratio(), adjustable='box')
    j += 1

axs[0].legend(loc = 'right', bbox_to_anchor=(2.5,0.5))
axs[0].set_xticks(np.arange(60, 170, 30))
axs[1].set_xticks(np.arange(60, 200, 30))
axs[0].set_xlabel(r'Angle ($^{\circ}$)', fontsize = '20')
axs[0].xaxis.set_label_coords(1,-.1)
axs[0].set_ylabel('Probability Density', fontsize = '20')
axs[0].yaxis.set_label_coords(-.3,.5)


plt.subplots_adjust(left=0.3,
                    bottom=0.25,
                    right=0.7,
                    top=0.75,
                    wspace=0.0,
                    hspace=0.0)

fig.suptitle("SnO2", fontsize=25)

plt.show()