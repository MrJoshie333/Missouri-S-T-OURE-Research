import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(1, 2, figsize=(6, 4))

densities = [
    'a13p4_d6p27', 'a13p8_d5p74', 'a14p2_d5p27', 'a14p6_d4p85',
    'a15p0_d4p47', 'a15p4_d4p13', 'a15p8_d3p82'
]

# These will collect ALL points across all densities:
all_x_total_void = []
all_y_total_void = []

all_x_largest_void = []
all_y_largest_void = []

# These will collect the average per-density:
density_vals_total = []
mean_vals_total = []

density_vals_largest_void = []
mean_vals_largest_void = []

for density in densities:
    # extract numeric density value, e.g. "6.27"
    dval = float(density.split('_d')[1].replace('p', '.'))

    void_total = []
    largest_void = []
    for run in range(1, 10):
        path = f"data/{density}/run{run}/volumes.txt"
        with open(path) as f:
            lines = f.readlines()
            void_total.append(float(lines[1].split()[0]))
            largest_void.append(float(lines[3].split()[0]))

    # append all the raw points at x = dval
    all_x_total_void.extend([dval] * len(void_total))
    all_y_total_void.extend(void_total)

    # compute & store the per-density mean
    density_vals_total.append(dval)
    mean_vals_total.append(np.mean(void_total))

    all_x_largest_void.extend([dval] * len(largest_void))
    all_y_largest_void.extend(largest_void)

    # compute & store the per-density mean
    density_vals_largest_void.append(dval)
    mean_vals_largest_void.append(np.mean(largest_void))

# scatter raw points
ax[0].scatter(all_x_total_void, all_y_total_void, alpha=1,)

# plot the average trend
ax[0].plot(density_vals_total, mean_vals_total, '-o', label='Total Void')

ax[0].scatter(all_x_largest_void, all_y_largest_void, alpha=1,)

# plot the average trend
ax[0].plot(density_vals_largest_void, mean_vals_largest_void, '-o', label='Largest Void')

ax[0].set_xlabel(r'Density, g/cm$^3$', fontsize=16)
ax[0].set_ylabel(r'Void Volume, $\AA^3$', fontsize=16)
ax[0].set_title(r'Sn$_{62}$Sr$_7$O$_{69}$', fontsize=22)
ax[0].legend()
#grid
ax[0].grid(True, alpha=0.25)

#=================================
#Ta2Sn3O8

densities = [
    'a12p30_d7p55', 'a12p70_d6p86', 'a13p1_d6p25', 'a13p5_d5p71', 'a13p9_d5p23', 'a14p3_d4p81', 'a14p7_d4p42', 'a15p1_d4p08', 'a15p5_d3p77', 'a15p9_d3p50'
]

# These will collect ALL points across all densities:
all_x_total_void = []
all_y_total_void = []

all_x_largest_void = []
all_y_largest_void = []

# These will collect the average per-density:
density_vals_total = []
mean_vals_total = []

density_vals_largest_void = []
mean_vals_largest_void = []

for density in densities:
    # extract numeric density value, e.g. "6.27"
    dval = float(density.split('_d')[1].replace('p', '.'))

    void_total = []
    largest_void = []
    for run in range(1, 11):
        path = f"../Ta2Sn3O8_120/{density}/run{run}/volumes.txt"
        with open(path) as f:
            lines = f.readlines()
            void_total.append(float(lines[1].split()[0]))
            largest_void.append(float(lines[3].split()[0]))

    # append all the raw points at x = dval
    all_x_total_void.extend([dval] * len(void_total))
    all_y_total_void.extend(void_total)

    # compute & store the per-density mean
    density_vals_total.append(dval)
    mean_vals_total.append(np.mean(void_total))

    all_x_largest_void.extend([dval] * len(largest_void))
    all_y_largest_void.extend(largest_void)

    # compute & store the per-density mean
    density_vals_largest_void.append(dval)
    mean_vals_largest_void.append(np.mean(largest_void))

# scatter raw points
ax[1].scatter(all_x_total_void, all_y_total_void, alpha=1,)

# plot the average trend
ax[1].plot(density_vals_total, mean_vals_total, '-o', label='Total Void')

ax[1].scatter(all_x_largest_void, all_y_largest_void, alpha=1,)

# plot the average trend
ax[1].plot(density_vals_largest_void, mean_vals_largest_void, '-o', label='Largest Void')

ax[1].set_xlabel(r'Density, g/cm$^3$', fontsize=16)
# ax[1].set_ylabel(r'Void Volume, $\AA^3$')
ax[1].set_title(r'Ta$_2$Sn$_3$O$_8$', fontsize=22)
ax[1].legend()
ax[0].legend(loc='upper right')

ax[1].legend(loc='upper right')

#grid
ax[1].grid(True, alpha=0.25)
ax[1].set_yticklabels([])
ax[0].axvline(x=3.82, color='k', linestyle='--', linewidth=1.5, alpha = 0.4)
ax[0].axvline(x=6.27, color='k', linestyle='--', linewidth=1.5, alpha = 0.4)
ax[1].axvline(x=3.82, color='k', linestyle='--', linewidth=1.5, alpha = 0.4)
ax[1].axvline(x=6.27, color='k', linestyle='--', linewidth=1.5, alpha = 0.4)

for ax in ax.flat:
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(12)
    ax.set_ylim(0, 1700)

    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(1.75)

plt.subplots_adjust(wspace=0.0, left = 0.198, right = 0.645)

#if horizontal lines:


plt.show()
