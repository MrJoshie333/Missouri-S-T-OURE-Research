import matplotlib.pyplot as plt
import numpy as np

from utility import filenameToLatex

# ===== Setup =====
# Save the Figure as a PDF?
SAVEPDF = False
num_atoms = 69

'''---------------------- Data And Plotting for SnO ----------------------'''

fig, axs = plt.subplots(2, 3)

'''---------------------- Data And Plotting for the other 3  ----------------------'''
file_name = 'sn.txt'

orig_density_Sn   = []
runs_Sn           = []
ECN_Sn            = []
ECN_time_Sn       = []
L_ave_Sn          = []
L_ave_time_Sn     = []
Distortion_Sn     = []
Distortion_time_Sn= []

iteration = 0
warm_color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
with open(file_name, 'r', encoding='utf-8') as f:
    # skip header line
    # next(f)

    # now process each data line
    for line in f:
        # split on whitespace
        density, compound, ecn, ecn_t, l_ave, l_ave_t, dist, dist_t = line.split()

        orig_density_Sn.append(density)
        # compound is always "Sn" here, but you could store it if you like
        ECN_Sn.append(float(ecn))
        ECN_time_Sn.append(float(ecn_t))
        L_ave_Sn.append(float(l_ave))
        L_ave_time_Sn.append(float(l_ave_t))
        Distortion_Sn.append(float(dist))
        Distortion_time_Sn.append(float(dist_t))

    '''Getting Densities'''
    density_list_Sn = []
    for i in orig_density_Sn:
        i = i.split("_")
        i = i[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list_Sn.append(i)

    axs[0, 0].plot(density_list_Sn, ECN_Sn, label='Sn-O', color='red')
    axs[1, 0].plot(density_list_Sn, ECN_time_Sn, label='Sn-O', color='red')
    axs[0, 1].plot(density_list_Sn, L_ave_Sn, label='Sn-O', color='red')
    axs[1, 1].plot(density_list_Sn, L_ave_time_Sn, label='Sn-O', color='red')
    axs[0, 2].plot(density_list_Sn, Distortion_Sn, label='Sn-O', color='red')
    axs[1, 2].plot(density_list_Sn, Distortion_time_Sn, label='Sn-O', color='red')

    iteration += 1



orig_density_Sr   = []
runs_Sr           = []
ECN_Sr            = []
ECN_time_Sr       = []
L_ave_Sr          = []
L_ave_time_Sr     = []
Distortion_Sr     = []
Distortion_time_Sr= []

iteration = 0
with open("sr.txt", 'r', encoding='utf-8') as f:
    # skip header line
    # next(f)

    # now process each data line
    for line in f:
        # split on whitespace
        density, compound, ecn, ecn_t, l_ave, l_ave_t, dist, dist_t = line.split()

        orig_density_Sr.append(density)
        # compound is always "Sr" here, but you could store it if you like
        ECN_Sr.append(float(ecn))
        ECN_time_Sr.append(float(ecn_t))
        L_ave_Sr.append(float(l_ave))
        L_ave_time_Sr.append(float(l_ave_t))
        Distortion_Sr.append(float(dist))
        Distortion_time_Sr.append(float(dist_t))

    '''Getting Densities'''
    density_list_Sr = []
    for i in orig_density_Sr:
        i = i.split("_")
        i = i[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list_Sr.append(i)

    axs[0, 0].plot(density_list_Sr, ECN_Sr, label='Sr-O', color='blue')
    axs[1, 0].plot(density_list_Sr, ECN_time_Sr, label='Sr-O', color='blue')
    axs[0, 1].plot(density_list_Sr, L_ave_Sr, label='Sr-O', color='blue')
    axs[1, 1].plot(density_list_Sr, L_ave_time_Sr, label='Sr-O', color='blue')
    axs[0, 2].plot(density_list_Sr, Distortion_Sr, label='Sr-O', color='blue')
    axs[1, 2].plot(density_list_Sr, Distortion_time_Sr, label='Sr-O', color='blue')

    iteration += 1

# axs[1, 0].set_xlabel(r'Density, g/$cm^3$', fontsize=18)
# axs[1, 1].set_xlabel(r'Density, g/$cm^3$', fontsize=18)
# axs[1, 2].set_xlabel(r'Density, g/$cm^3$', fontsize=18)
#
# axs[0, 0].set_ylabel("ECN", fontsize=18, labelpad=20)
# axs[1, 0].set_ylabel("ECN Time Variance", fontsize=18, labelpad=20)
# axs[0, 1].set_ylabel(r'L_Average, $\AA$', fontsize=18, labelpad=20)
# axs[1, 1].set_ylabel("L_Average Time Variance", fontsize=18, labelpad=20)
# axs[0, 2].set_ylabel(r'Distortion, $\AA^2$', fontsize=18, labelpad=20)
# axs[1, 2].set_ylabel("Distortion Time Variance", fontsize=18, labelpad=20)
#
# plt.subplots_adjust(
#     # left=0.1,
#     # bottom=0.1,
#     # right=0.9,
#     # top=0.9,
#     wspace=0.425,
#     hspace=0.0)
#
# '''Sorting the labels in the legend'''
# handles, labels = axs[0, 0].get_legend_handles_labels()
# # print(labels)
# handles = [handles[7], handles[0], handles[8], handles[1], handles[5], handles[3], handles[2], handles[6], handles[4]]
# labels = [labels[7], labels[0], labels[8], labels[1], labels[5], labels[3], labels[2], labels[6], labels[4]]
# # print(labels)
#
# axs[0, 1].legend(handles, labels, prop={'size': 16}, loc='upper center', bbox_to_anchor=(0.5, 1.32),
#                  ncol=3, fancybox=True, shadow=True, fontsize='large')
#
# axs[1, 0].set_yticks(np.arange(0.05, 0.4, 0.1))
# axs[0, 1].set_yticks(np.arange(1.90, 2.25, 0.07))
# axs[1, 1].set_yticks(np.arange(0.0005, 0.004, 0.00075))
#
# for a in axs.flat:
#     a.grid(True, alpha=0.25)
#     a.tick_params(axis='x', labelsize=15)
#     a.tick_params(axis='y', labelsize=15)

plt.show()
if SAVEPDF == True:
    plt.savefig('ECN.pdf')
