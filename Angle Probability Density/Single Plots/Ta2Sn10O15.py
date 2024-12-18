import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 3)
file_names = ["../Data/Ta2Sn10O15_distrib_angle_MOM_density.dat", "../Data/Ta2Sn10O15_distrib_angle_OSnO_density.dat", "../Data/Ta2Sn10O15_distrib_angle_OTaO_density.dat"]
count = 0

color_1 = []
color_2 = []
density_leg_1 = []
density_leg_2 = []

with open("../Data/Ta2Sn10O15_density.dat") as g:
    density_data = g.readlines()
for i in density_data:
    density_leg_1.append(float(i))
del density_leg_1[10:]

for i in density_data:
    density_leg_2.append(float(i))
del density_leg_2[:10]

print(density_leg_1)
print(density_leg_2)
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
    print(density_1)
    print(density_2)
    columnData1 = [[] for i in density_1[0]]
    for sublist in density_1:
        for col in range(len(sublist)):
            columnData1[col].append(sublist[col])
    columnData2 = [[] for i in density_2[0]]
    for sublist in density_2:
        for col in range(len(sublist)):
            columnData2[col].append(sublist[col])

    #colors = ['#e3440e', '#e75423', '#eb6234', '#ee6f44', '#f17c53', '#f38963', '#f49573', '#f6a183', '#f6ad93', 'linen']

    '''colors_1 = ['#7f0000', '#b30000', '#ef6548', '#fc4e2a', '#fd8d3c', '#fc9272', '#fc8d59', '#fdbb84', '#fcbba1',
              '#fdd49e', '#fee8c8', '#1a1a$', '#005a32', '#238b45', '#41ab5d', '#74c476', '#a1d99b', '#c7e9c0', '#d9f0a3',
              '#f7fcb9', '#3f007d', '#54278f', '#6a51a3', '#807dba', '#9e9ac8', '#bcbddc', '#dadaeb', '#c6dbef', '#deebf7']'''

    # https://colordesigner.io/gradient-generator
    #On the website, split between the two groups (dark red to orange, then orange to light orange)
    colors_1 =['#610202', '#871e0d', '#ad390f', '#d2560e', '#f67503' , '#fc9336', '#fba652', '#f9b86e', '#f8c88c', '#FFE7C4']
    colors_2 = ['#040f56', '#163b8b', '#246ac0', '#339df6', '#3e35fd' , '#660ef6', '#7551fe', '#8a7aff', '#a39fff']





    colors_2 =['#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df', '#cce6f8']

    a = a[14:]
    a = a[:-12]
    density_count = 0
    for i in columnData1:
        axs[0, count].plot(angle, i, label=r'' + f'{density_leg_1[density_count]}' + r' g/$\mathrm{cm}^3$', color = colors_1[density_count])#, color=colors[iteration])
        density_count += 1
    density_count = 0
    for i in columnData2:
        axs[1, count].plot(angle, i, label=r'' + f'{density_leg_2[density_count]}' + r' g/$\mathrm{cm}^3$', color=colors_2[density_count])
        density_count += 1

    count += 1
axs[0, 0].set_title('M-O-M', fontsize = 20)
axs[0,1].set_title('O-Sn-O', fontsize = 20)
axs[0,2].set_title('O-Ta-O', fontsize = 20)

x = 0
i = 0
j = 0


while x < 6:

    axs[0, j].set_xticklabels([])
    axs[i,1].set_yticklabels([])
    axs[i, 2].set_yticklabels([])
    axs[i, j].tick_params(axis = 'y', labelsize = 13)
    axs[i,j].tick_params(axis = 'x', labelsize = 13)
    axs[i,j].set_xlim(60, 185)
    axs[i,j].set_ylim(0, 0.035)
    axs[i,j].grid(True, alpha=0.25)
    axs[i,j].set_yticks(np.arange(0, 0.035, 0.01))
    axs[i, j].set_xticks(np.arange(60, 180, 30))
    axs[i, j].set_aspect(1.0 / axs[i, j].get_data_ratio(), adjustable='box')
    #iterator:
    x += 1
    j += 1
    if j == 3:
        j = 0
        i += 1
axs[0,2].legend(bbox_to_anchor=(1.0,1.25))
axs[1,2].legend(bbox_to_anchor=(1.0,1))
axs[1,1].set_xlabel(r'Angle ($^{\circ}$)', fontsize = '20')
axs[1,0].xaxis.set_label_coords(1.0,-.15)
axs[0,0].set_ylabel('Probability Density', fontsize = '20')
axs[0,0].yaxis.set_label_coords(-.3,0)


plt.subplots_adjust(left=0.3,
                    #bottom=0.1,
                    right=0.7,
                    #top=0.9,
                    wspace=0.0,
                    hspace=(-.467)
                    )

fig.suptitle("Ta2Sn10O15", fontsize=25)
plt.show()