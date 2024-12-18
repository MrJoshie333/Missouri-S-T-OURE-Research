# ===== Ternary ECN_Distribution =====
# ===== Joshua Santy =====
import re
import matplotlib.pyplot as plt
import numpy as np


# ===== Functions =====
def parse_line(line):
    # Split the line by any whitespace (spaces or tabs)
    parts = re.split(r'\s+', line.strip())

    # Convert each part to the appropriate data type
    ECN_value = float(parts[0])
    dens_values = list(map(float, parts[2:]))

    return ECN_value, dens_values


def process_file(file_path):
    # Lists to store the parsed data
    ECN = []
    dens_lists = []

    with open(file_path, 'r') as file:
        for line in file:
            # Parse each line
            ECN_value, dens_values = parse_line(line)

            # Append the values to their respective lists
            ECN.append(ECN_value)

            # Append each density value to the corresponding list within dens_lists
            if not dens_lists:
                # Initialize density lists if they are empty
                dens_lists = [[] for _ in range(len(dens_values))]

            # Populate the density lists
            for i, value in enumerate(dens_values):
                dens_lists[i].append(value)

    return ECN, dens_lists


# ===== Initialization =====
fig, axs = plt.subplots(4, 3, figsize=(12, 12), constrained_layout=True)

labels_Ta2Sn3O8 = ['7.55', '6.86', '6.25', '5.71', '5.23', '4.81', '4.42', '4.08', '3.77', '3.5']
labels_Ta2SnO6 = ['8.4', '7.61', '6.92', '6.6', '6.3', '6.02', '5.76', '5.51', '5.28', '4.85', '4.47']
colors_1 = ['#610202', '#871e0d', '#ad390f', '#d2560e', '#f67503', '#fc9336', '#fba652', '#f9b86e', '#f8c88c',
            '#FFE7C4', '#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df',
            '#cce6f8']

# ===== Ta2Sn10O15 Sn-O=====
labels_Ta2Sn10O15 = ['6.61', '6.04', '5.53', '5.3', '5.08', '4.87', '4.68', '4.49', '4.32', '3.99', '3.7', '3.43',
                     '3.19', '2.97', '2.77', '2.59', '2.425', '2.27', '2.13']
file_path = 'Data/Ta2Sn10O15/distrib_ECN_SnO.dat'
ECN, dens_lists = process_file(file_path)

dens_top = dens_lists[:9]  # First 10 densities for the top plot
dens_bottom = dens_lists[9:]  # Last 9 densities for the bottom plot

for i, dens in enumerate(dens_top):
    axs[0, 0].plot(ECN, dens, color=colors_1[i], label=labels_Ta2Sn10O15[i])
axs[0, 0].set_title('Sn-O', fontsize=24)
axs[0, 0].set_ylim(0, 0.3)
axs[0, 0].text(4, 0.21, r'$\mathrm{Ta_2Sn_{10}O_{15}}$', fontsize=18)

for i, dens in enumerate(dens_bottom):
    axs[1, 0].plot(ECN, dens, color=colors_1[i + 10], label=labels_Ta2Sn10O15[i + 9])
axs[1, 0].set_ylim(0, 0.3)
axs[1, 0].text(4, 0.21, r'$\mathrm{Ta_2Sn_{10}O_{15}}$', fontsize=18)

# ===== Ta2Sn10O15 Ta-O =====
file_path = 'Data/Ta2Sn10O15/distrib_ECN_TaO.dat'
ECN, dens_lists = process_file(file_path)
dens_top = dens_lists[:9]
dens_bottom = dens_lists[9:]

for i, dens in enumerate(dens_top):
    axs[0, 1].plot(ECN, dens, color=colors_1[i], label=labels_Ta2Sn10O15[i])
axs[0, 1].set_title('Ta-O', fontsize=24)
axs[0, 1].text(5, 0.21, r'$\mathrm{Ta_2Sn_{10}O_{15}}$', fontsize=18)
axs[0, 1].set_ylim(0, 0.3)

for i, dens in enumerate(dens_bottom):
    axs[1, 1].plot(ECN, dens, color=colors_1[i + 10], label=labels_Ta2Sn10O15[i + 9])
axs[1, 1].text(5, 0.21, r'$\mathrm{Ta_2Sn_{10}O_{15}}$', fontsize=18)
axs[1, 1].set_ylim(0, 0.3)

# ===== Ta2Sn10O15 O-M =====
file_path = 'Data/Ta2Sn10O15/distrib_ECN_OM.dat'
ECN, dens_lists = process_file(file_path)
dens_top = dens_lists[:9]
dens_bottom = dens_lists[9:]

for i, dens in enumerate(dens_top):
    axs[0, 2].plot(ECN, dens, color=colors_1[i], label=labels_Ta2Sn10O15[i])
axs[0, 2].set_title('O-M', fontsize=24)
axs[0, 2].text(2.3, 0.21, r'$\mathrm{Ta_2Sn_{10}O_{15}}$', fontsize=18)
axs[0, 2].set_ylim(0, 0.3)

for i, dens in enumerate(dens_bottom):
    axs[1, 2].plot(ECN, dens, color=colors_1[i + 10], label=labels_Ta2Sn10O15[i + 9])
axs[1, 2].text(2.3, 0.21, r'$\mathrm{Ta_2Sn_{10}O_{15}}$', fontsize=18)
axs[1, 2].set_ylim(0, 0.3)

# ===== Ta2Sn3O8 Sn-O=====
file_path = 'Data/Ta2Sn3O8/distrib_ECN_SnO.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[2, 0].plot(ECN, dens, color=colors_1[i], label=labels_Ta2Sn3O8[i])
axs[2, 0].text(4.2, 0.21, r'$\mathrm{Ta_2Sn_3O_8}$', fontsize=18)
axs[2, 0].set_ylim(0, 0.3)

# ===== Ta2Sn3O8 Ta-O ====
file_path = 'Data/Ta2Sn3O8/distrib_ECN_TaO.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[2, 1].plot(ECN, dens, color=colors_1[i], label=labels_Ta2Sn3O8[i])
axs[2, 1].text(5.2, 0.21, r'$\mathrm{Ta_2Sn_3O_8}$', fontsize=18)
axs[2, 1].set_ylim(0, 0.3)

# ===== Ta2Sn3O8 O-M =====
file_path = 'Data/Ta2Sn3O8/distrib_ECN_OM.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[2, 2].plot(ECN, dens, color=colors_1[i], label=labels_Ta2Sn3O8[i])
axs[2, 2].text(2.3, 0.21, r'$\mathrm{Ta_2Sn_3O_8}$', fontsize=18)
axs[2, 2].set_ylim(0, 0.3)

# ===== Ta2SnO6 Sn-O =====
file_path = 'Data/Ta2SnO6/distrib_ECN_SnO.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[3, 0].plot(ECN, dens, color=colors_1[i], label=labels_Ta2SnO6[i])
axs[3, 0].set_ylim(0, 0.3)
axs[3, 0].text(4.3, 0.21, r'$\mathrm{Ta_2SnO_6}$', fontsize=18)

# ===== Ta2SnO6 Ta-O =====
file_path = 'Data/Ta2SnO6/distrib_ECN_TaO.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[3, 1].plot(ECN, dens, color=colors_1[i], label=labels_Ta2SnO6[i])
axs[3, 1].set_ylim(0, 0.3)
axs[3, 1].text(5.3, 0.21, r'$\mathrm{Ta_2SnO_6}$', fontsize=18)

# ===== Ta2SnO6 O-M =====
file_path = 'Data/Ta2SnO6/distrib_ECN_OM.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[3, 2].plot(ECN, dens, color=colors_1[i], label=labels_Ta2SnO6[i])
axs[3, 2].text(2.3, 0.21, r'$\mathrm{Ta_2SnO_6}$', fontsize=18)
axs[3, 2].set_ylim(0, 0.3)

# ===== Formatting Plots =====

# ===== Ticks and Labels =====
for i in range(4):
    axs[i, 1].set_yticklabels([])
    axs[i, 2].set_yticklabels([])

axs[0, 0].set_xticklabels([])
axs[1, 2].set_xticklabels([])
axs[2, 2].set_xticklabels([])

for i in range(4):
    for j in range(3):
        axs[i, 0].set_xlim(0.9, 6.2)
        axs[i, 0].set_xticks([1, 2, 3, 4, 5, 6])
        axs[i, 1].set_xlim(3.35, 6.2)
        axs[i, 1].set_xticks([4, 5, 6])
        axs[i, 2].set_xlim(0.65, 3.5)
        axs[i, 2].set_xticks([1, 2, 3])
        axs[i, j].set_yticks(np.arange(0.05, 0.29, 0.05))

# ===== Legends =====
for a in axs[:, 2]:
    a.legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', ncols=2, fontsize=12,
             bbox_to_anchor=(1.53, 1))

axs[1, 2].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', ncols=2, fontsize=12,
                 bbox_to_anchor=(1.55, 1))
axs[3, 1].set_xlabel('Effective Coordination Number', fontsize=22)
axs[1, 0].set_ylabel('Probability Density', fontsize=22, y=0, labelpad=10)

for a in axs[:, 0]:
    a.tick_params(axis='both', which='major', labelsize=13)
axs[3, 1].tick_params(axis='both', which='major', labelsize=13)
axs[3, 2].tick_params(axis='both', which='major', labelsize=13)

for a in axs.flat:
    a.grid(alpha=0.25)
plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0, left=0.1, right=0.8)

plt.show()
