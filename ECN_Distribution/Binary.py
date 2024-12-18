# ===== Binary ECN_Distribution =====
# ===== Joshua Santy =====

import re
import matplotlib.pyplot as plt
from utility import read_dat_file_to_lists


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
fig, axs = plt.subplots(4, 2, figsize=(8, 8))

# ===== Sn-O =====
labels_SnO = ['6.01', '5.75', '5.51', '5.28', '5.06', '4.86', '4.67', '4.48', '4.31', '4.15',
              '3.99', '3.84', '3.7', '3.57', '3.44', '3.2', '2.98', '2.78', '2.6']
file_path = 'Data/SnO/distrib_ECN_SnO_density.dat'
ECN, dens_lists = process_file(file_path)

dens_top = dens_lists[:10]  # First 10 densities for the top plot
dens_bottom = dens_lists[10:]  # Last 9 densities for the bottom plot

colors_1 = ['#610202', '#871e0d', '#ad390f', '#d2560e', '#f67503', '#fc9336', '#fba652', '#f9b86e', '#f8c88c',
            '#FFE7C4']
colors_2 = ['#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df', '#cce6f8']

# Top plot (first 10 densities)
for i, dens in enumerate(dens_top):
    axs[0, 0].plot(ECN, dens, color=colors_1[i], label=labels_SnO[i])
axs[0, 0].set_title('M-O', fontsize=20)
axs[0, 0].text(5.2, 0.55, "SnO", fontsize=18)
axs[0, 0].set_ylim(0, 0.7)
axs[0, 0].grid(alpha=0.25)

# Bottom plot (last 9 densities)
for i, dens in enumerate(dens_bottom):
    axs[1, 0].plot(ECN, dens, color=colors_2[i], label=labels_SnO[i + 10])
axs[1, 0].text(5.2, 0.3, "SnO", fontsize=18)
axs[1, 0].set_ylim(0, 0.4)

# ===== O-Sn =====
file_path = 'Data/SnO/distrib_ECN_OSn.dat'
ECN, dens_lists = process_file(file_path)

dens_top = dens_lists[:10]  # First 10 densities for the top plot
dens_bottom = dens_lists[10:]  # Last 9 densities for the bottom plot

for i, dens in enumerate(dens_top):
    axs[0, 1].plot(ECN, dens, color=colors_1[i], label=labels_SnO[i])
axs[0, 1].set_title('O-M', fontsize=20)
axs[0, 1].text(3.3, 0.55, "SnO", fontsize=18)
axs[0, 1].set_ylim(0, 0.7)
axs[0, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', ncols=2, fontsize=11)

for i, dens in enumerate(dens_bottom):
    axs[1, 1].plot(ECN, dens, color=colors_2[i], label=labels_SnO[i + 10])
axs[1, 1].text(3.3, 0.3, "SnO", fontsize=18)
axs[1, 1].set_ylim(0, 0.4)
axs[1, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', ncols=2, fontsize=12,
                 bbox_to_anchor=(1.85, 0.9))

# ===== SnO2 =====
labels_SnO2 = [7.17, 6.81, 6.48, 6.17, 5.88, 5.6, 5.35]
file_path = 'Data/SnO2/distrib_ECN_SnO.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[2, 0].plot(ECN, dens, color=colors_1[i], label=labels_SnO2[i])
axs[2, 0].text(5.2, 0.55, r'$\text{SnO}_2$', fontsize=18)
axs[2, 0].set_ylim(0, 0.7)

# ===== SnO2 O-Sn =====
file_path = 'Data/SnO2/distrib_ECN_OSn.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[2, 1].plot(ECN, dens, color=colors_1[i], label=labels_SnO2[i])
axs[2, 1].text(3.3, 0.55, r'$\text{SnO}_2$', fontsize=18)
axs[2, 1].set_ylim(0, 0.7)
axs[2, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=11)

# ===== Ta2O5 =====
labels_Ta2O5 = ['8.199', '7.81', '7.44', '7.09', '6.77', '6.18', '5.66', '5.19']
file_path = 'Data/Ta2O5/distrib_ECN_TaO.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[3, 0].plot(ECN, dens, color=colors_1[i], label=labels_Ta2O5[i])
axs[3, 0].text(5.1, 0.38, r'$\text{Ta}_2\text{O}_5$', fontsize=18)
axs[3, 0].set_ylim(0, 0.5)

# ===== Ta2O5 O-Ta =====
file_path = 'Data/Ta2O5/distrib_ECN_OTa.dat'
ECN, dens_lists = process_file(file_path)

for i, dens in enumerate(dens_lists):
    axs[3, 1].plot(ECN, dens, color=colors_1[i], label=labels_Ta2O5[i])
axs[3, 1].text(3.1, 0.38, r'$\text{Ta}_2\text{O}_5$', fontsize=18)
axs[3, 1].set_ylim(0, 0.5)
axs[3, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=8)

# ===== Crystalline =====

# ===== SnO =====
file_path = 'Data/SnO/cryst/distrib_ECN_SnO.dat'
ECN, cryst = read_dat_file_to_lists(file_path)
axs[0, 0].plot(ECN, cryst, color='limegreen', label='Crystalline')

# ===== SnO2 O-Sn =====
file_path = 'Data/SnO/cryst/distrib_ECN_OSn.dat'
ECN, cryst = read_dat_file_to_lists(file_path)
axs[0, 1].plot(ECN, cryst, color='limegreen', label='Crystalline')
axs[0, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=12, ncols=2,
                 bbox_to_anchor=(2.03, 1.05))

# ===== SnO2 =====
file_path = 'Data/SnO2/cryst/distrib_ECN_SnO.dat'
ECN, cryst = read_dat_file_to_lists(file_path)
axs[2, 0].plot(ECN, cryst, color='limegreen', label='Crystalline')

# ===== SnO2 O-Sn =====
file_path = 'Data/SnO2/cryst/distrib_ECN_OSn.dat'
ECN, cryst = read_dat_file_to_lists(file_path)
axs[2, 1].plot(ECN, cryst, color='limegreen', label='Crystalline')
axs[2, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=12, ncols=2,
                 bbox_to_anchor=(2.02, 0.9))

# ===== Ta2O5 =====
file_path = 'Data/Ta2O5/cryst/distrib_ECN_TaO.dat'
ECN, cryst = read_dat_file_to_lists(file_path)
axs[3, 0].plot(ECN, cryst, color='limegreen', label='Crystalline')

# ===== Ta2O5 O-Ta =====
file_path = 'Data/Ta2O5/cryst/distrib_ECN_OTa.dat'
ECN, cryst = read_dat_file_to_lists(file_path)
axs[3, 1].plot(ECN, cryst, color='limegreen', label='Crystalline')
axs[3, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=12, ncols=2,
                 bbox_to_anchor=(2.07, 0.9))

# ===== Formatting Plots =====
axs[3, 1].set_xlabel('Effective Coordination Number', fontsize=24, x=0, labelpad=10)
axs[1, 0].set_ylabel('Probability Density', fontsize=24, y=0, labelpad=10)
for a in axs[:, 1].flat:
    a.set_yticklabels([])

axs[2, 1].set_xticks([1, 2, 3, 4])
axs[3, 1].set_xticks([1, 2, 3, 4])
axs[0, 0].set_yticks([0.2, 0.4, 0.6])
axs[1, 0].set_yticks([0.1, 0.2, 0.3])
axs[2, 0].set_yticks([0.2, 0.4, 0.6])
axs[3, 0].set_yticks([0.0, 0.1, 0.2, 0.3, 0.4])
for i in range(4):  # Loop over rows
    for j in range(2):  # Loop over columns
        axs[i, 0].set_xlim(1.7, 6.5)
        axs[i, 1].set_xlim(0.9, 4.1)

plt.subplots_adjust(left=0.35, right=0.65, hspace=0.0, wspace=0.0)
for a in axs.flat:
    a.grid(alpha=0.25)
    a.tick_params(axis='both', which='major', labelsize=13)
plt.show()
