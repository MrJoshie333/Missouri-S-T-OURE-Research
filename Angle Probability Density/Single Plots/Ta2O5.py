import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols = 2)
file_names = ["../Data/Ta2O5_distrib_angle_MOM_density.dat", "../Data/Ta2O5_distrib_angle_OTaO_density.dat"]
count = 0

color_1 = []
color_2 = []
density_leg = []


with open("../Data/Ta2O5_density.dat") as g:
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

    #colors = ['#e3440e', '#e75423', '#eb6234', '#ee6f44', '#f17c53', '#f38963', '#f49573', '#f6a183', '#f6ad93', 'linen']

    '''colors_1 = ['#7f0000', '#b30000', '#ef6548', '#fc4e2a', '#fd8d3c', '#fc9272', '#fc8d59', '#fdbb84', '#fcbba1',
              '#fdd49e', '#fee8c8', '#1a1a$', '#005a32', '#238b45', '#41ab5d', '#74c476', '#a1d99b', '#c7e9c0', '#d9f0a3',
              '#f7fcb9', '#3f007d', '#54278f', '#6a51a3', '#807dba', '#9e9ac8', '#bcbddc', '#dadaeb', '#c6dbef', '#deebf7']'''

    # https://colordesigner.io/gradient-generator
    #On the website, split between the two groups (dark red to orange, then orange to light orange)
    colors_1 =['#610202', '#871e0d', '#ad390f', '#d2560e', '#fc9336', '#fba652', '#f9b86e', '#FFE7C4']
    colors_2 = ['#040f56', '#163b8b', '#246ac0', '#339df6', '#3e35fd' , '#660ef6', '#7551fe', '#8a7aff', '#a39fff']

    colors_2 =['#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df', '#cce6f8']

    a = a[14:]
    a = a[:-12]
    density_count = 0
    for i in columnData:
        axs[count].plot(angle, i, label=r'' + f'{density_leg[density_count]}' + r' g/$\mathrm{cm}^3$', color = colors_1[density_count])#, color=colors[iteration])
        density_count += 1

    count += 1



axs[0].set_title('M-O-M', fontsize = 20)
axs[1].set_title('O-Ta-O', fontsize = 20)

j = 0

axs[1].set_yticklabels([])
while j < 2:


    axs[j].tick_params(axis = 'y', labelsize = 13)
    axs[j].tick_params(axis = 'x', labelsize = 13)
    axs[j].set_xlim(60, 180)
    axs[j].grid(True, alpha=0.25)
    axs[j].set_ylim(-.0001,0.027)
    axs[j].set_yticks(np.arange(0, 0.03, 0.01))

    axs[j].set_aspect(1.0 / axs[j].get_data_ratio(), adjustable='box')
    j += 1

axs[0].legend(loc = 'right', bbox_to_anchor=(2.5,0.5))

axs[0].set_xlabel(r'Angle ($^{\circ}$)', fontsize = '20')
axs[0].xaxis.set_label_coords(1,-.1)
axs[0].set_ylabel('Probability Density', fontsize = '20')
#axs[0].yaxis.set_label_coords(0,0)
axs[0].set_xticks(np.arange(60, 170, 20))
axs[1].set_xticks(np.arange(60, 200, 20))
#plt.setp(axs[0].get_xticklabels(), rotation=30, horizontalalignment='right')
#plt.setp(axs[1].get_xticklabels(), rotation=30, horizontalalignment='right')

plt.subplots_adjust(left=0.3,
                    #bottom=0.1,
                    right=0.7,
                    #top=0.9,
                    wspace=0.0,
                    hspace=0.0)

fig.suptitle("Ta2O5", fontsize=25)

plt.show()