import matplotlib.pyplot as plt
import numpy as np

from utility import filenameToLatex

# ===== Setup =====
# Save the Figure as a PDF?
SAVEPDF = False

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

#10/90:
iteration = 0
# warm_color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
with open('10_90 txt/' +file_name, 'r', encoding='utf-8') as f:
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
        i = i[2] #2nd _ since we have an extra one up front
        # print(i)
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list_Sn.append(i)

    axs[0, 0].plot(density_list_Sn, ECN_Sn, 'o-', label=r'Sn-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='coral', markersize=6)
    axs[1, 0].plot(density_list_Sn, ECN_time_Sn, 'o-', label=r'Sn-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='coral', markersize=6)
    axs[0, 1].plot(density_list_Sn, L_ave_Sn, 'o-', label=r'Sn-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='coral', markersize=6)
    axs[1, 1].plot(density_list_Sn, L_ave_time_Sn, 'o-', label=r'Sn-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='coral', markersize=6)
    axs[0, 2].plot(density_list_Sn, Distortion_Sn, 'o-', label=r'Sn-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='coral', markersize=6)
    axs[1, 2].plot(density_list_Sn, Distortion_time_Sn, 'o-', label=r'Sn-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='coral', markersize=6)

    iteration += 1

#Sr:

orig_density_Sr   = []
runs_Sr           = []
ECN_Sr            = []
ECN_time_Sr       = []
L_ave_Sr          = []
L_ave_time_Sr     = []
Distortion_Sr     = []
Distortion_time_Sr= []

iteration = 0
with open("10_90 txt/sr.txt", 'r', encoding='utf-8') as f:
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
        i = i[2]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list_Sr.append(i)

    axs[0, 0].plot(density_list_Sr, ECN_Sr, 'o-', label=r'Sr-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='cornflowerblue', markersize=6, marker='^')
    axs[1, 0].plot(density_list_Sr, ECN_time_Sr, 'o-', label=r'Sr-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='cornflowerblue', markersize=6, marker='^')
    axs[0, 1].plot(density_list_Sr, L_ave_Sr, 'o-', label=r'Sr-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='cornflowerblue', markersize=6, marker='^')
    axs[1, 1].plot(density_list_Sr, L_ave_time_Sr, 'o-', label=r'Sr-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='cornflowerblue', markersize=6, marker='^')
    axs[0, 2].plot(density_list_Sr, Distortion_Sr, 'o-', label=r'Sr-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='cornflowerblue', markersize=6, marker='^')
    axs[1, 2].plot(density_list_Sr, Distortion_time_Sr, 'o-', label=r'Sr-O: Sn$_{62}$Sr$_{7}$O$_{69}$', color='cornflowerblue', markersize=6, marker='^')

    iteration += 1
 #30/70:
orig_density_Sn = []
runs_Sn = []
ECN_Sn = []
ECN_time_Sn = []
L_ave_Sn = []
L_ave_time_Sn = []
Distortion_Sn = []
Distortion_time_Sn = []
iteration = 0
# file_name =
# warm_color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
with open('30_70 txt/' + file_name, 'r', encoding='utf-8') as f:
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
        i = i[2]  # 2nd _ since we have an extra one up front
        # print(i)
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list_Sn.append(i)

    axs[0, 0].plot(density_list_Sn, ECN_Sn, 'o-', label=r'Sn-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='red', markersize=6, linestyle='dashed')
    axs[1, 0].plot(density_list_Sn, ECN_time_Sn, 'o-', label=r'Sn-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='red', markersize=6, linestyle='dashed')
    axs[0, 1].plot(density_list_Sn, L_ave_Sn, 'o-', label=r'Sn-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='red', markersize=6, linestyle='dashed')
    axs[1, 1].plot(density_list_Sn, L_ave_time_Sn, 'o-', label=r'Sn-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='red', markersize=6, linestyle='dashed')
    axs[0, 2].plot(density_list_Sn, Distortion_Sn, 'o-', label=r'Sn-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='red', markersize=6, linestyle='dashed')
    axs[1, 2].plot(density_list_Sn, Distortion_time_Sn, 'o-', label=r'Sn-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='red', markersize=6, linestyle='dashed')

    iteration += 1

# Sr:

orig_density_Sr = []
runs_Sr = []
ECN_Sr = []
ECN_time_Sr = []
L_ave_Sr = []
L_ave_time_Sr = []
Distortion_Sr = []
Distortion_time_Sr = []

iteration = 0
with open("30_70 txt/sr.txt", 'r', encoding='utf-8') as f:
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
        i = i[2]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list_Sr.append(i)

    axs[0, 0].plot(density_list_Sr, ECN_Sr, 'o-', label=r'Sr-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='blue', markersize=6, marker='^', linestyle='dashed')
    axs[1, 0].plot(density_list_Sr, ECN_time_Sr, 'o-', label=r'Sr-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='blue', markersize=6, marker='^', linestyle='dashed')
    axs[0, 1].plot(density_list_Sr, L_ave_Sr, 'o-', label=r'Sr-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='blue', markersize=6, marker='^', linestyle='dashed')
    axs[1, 1].plot(density_list_Sr, L_ave_time_Sr, 'o-', label=r'Sr-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='blue', markersize=6, marker='^', linestyle='dashed')
    axs[0, 2].plot(density_list_Sr, Distortion_Sr, 'o-', label=r'Sr-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='blue', markersize=6, marker='^', linestyle='dashed')
    axs[1, 2].plot(density_list_Sr, Distortion_time_Sr, 'o-', label=r'Sr-O: Sn$_{48}$Sr$_{21}$O$_{69}$', color='blue', markersize=6, marker='^', linestyle='dashed')

    iteration += 1




axs[1, 0].set_xlabel(r'Density, g/cm$^3$', fontsize=18)
axs[1, 1].set_xlabel(r'Density, g/cm$^3$', fontsize=18)
axs[1, 2].set_xlabel(r'Density, g/cm$^3$', fontsize=18)

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

axs[0, 2].legend(prop={'size': 16}, loc='upper center', bbox_to_anchor=(0.5, 1.27),
                 ncol=2, fancybox=True, shadow=True, fontsize='large')
axs[0,0].set_title(r'ECN, L Average, and Distortion for Sn$_{62}$Sr$_7$O$_{69}$ and Sn$_{48}$Sr$_{21}$O$_{69}$', pad=20, fontsize=20, x=1)
# # axs[1, 0].set_yticks(np.arange(0.05, 0.4, 0.1))
# axs[0, 1].set_yticks(np.arange(1.90, 2.25, 0.07))
# axs[1, 1].set_yticks(np.arange(0.0005, 0.004, 0.00075))

for a in axs.flat:
    a.grid(True, alpha=0.380)
    a.tick_params(axis='x', labelsize=15)
    a.tick_params(axis='y', labelsize=15)

plt.show()
if SAVEPDF == True:
    plt.savefig('ECN.pdf')
