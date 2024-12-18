#Comparing Volume information from runs 1, 2, 2_120, 2_240

import os
import matplotlib.pyplot as plt
import numpy as np

#TotalVoidVolume NumberOfVoids IsoCutOff CellVol TotalVol MaxIso SnVoid% OVoid%

fig, axs = plt.subplots(ncols = 4, nrows = 2)

#In order, 1, 2, 2_120, 2_240
TotalVoidVolume = [1250.501494000445, 1265.147182719721, 1265.147182719721, 1302.3692327830765]
NumberOfVoids = [93, 82, 82, 171]
IsoCutOff = [2.0, 2.0, 2.0, 2.0]
CellVol = [0.0023262031250000006, 0.0023262031250000006, 0.0023262031250000006, 0.00029077539062500007]
TotalVol = [4019.679, 4019.679, 4019.679, 4019.679]
MaxIso = [4.159113865592363, 5.216412230092665, 5.216412230092665, 5.219553817678642]
LargestVoidSn = [69.23598624649064, 69.82852384793526, 69.82852384793526, 69.81158378673119]
LargestVoidO = [30.764013753509353 , 30.171476152064738 , 30.171476152064738, 30.188416213268813]
Runs = [1, 2, 3, 4]

axs[0,0].plot(Runs, TotalVoidVolume, label = "Total Void Volume")
axs[0,1].plot(Runs, NumberOfVoids, label = "Number of Voids")
axs[0,2].plot(Runs, IsoCutOff, label = "ISO Cutoff")
axs[0,3].plot(Runs, CellVol, label = "Cell Volume")
axs[1,0].plot(Runs, TotalVol, label = "Total Volume")
axs[1,1].plot(Runs, MaxIso, label = "Max ISO")
axs[1,2].plot(Runs, LargestVoidSn, label = "Largest Void Sn")
axs[1,3].plot(Runs, LargestVoidO, label = "Largest Void O")


axs[0,0].set_title("Total Void Volume")
axs[0,1].set_title("Number of Voids")
axs[0,2].set_title("ISO Cutoff")
axs[0,3].set_title("Cell Volume")
axs[1,0].set_title("Total Volume")
axs[1,1].set_title("Max ISO")
axs[1,2].set_title("Largest Void Sn%")
axs[1,3].set_title("Largest Void O%")

x = 0
y = 0
while x < 2:
    while y < 4:
        axs[x, y].set_xticks(np.arange(1, 5, 1))
        y += 1
    x += 1
    y = 0
#axs[0, 0].plot(density_list, ECN, label=f'{a}', color=colors[iteration])
plt.show()
