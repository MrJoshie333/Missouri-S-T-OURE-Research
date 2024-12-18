# ===== Binary PDF Distribution with SrSnO Comparison =====
# ===== Joshua Santy =====
import re

import matplotlib.pyplot as plt

from utility import read_dat_file_to_lists


def parse_line(line):
    # Split the line by any whitespace (spaces or tabs)
    parts = re.split(r'\s+', line.strip())

    # Convert each part to the appropriate data type
    r_value = float(parts[0])
    cryst_value = float(parts[1])
    dens_values = list(map(float, parts[2:]))

    return r_value, cryst_value, dens_values


def process_file(file_path):
    # Lists to store the parsed data
    r = []
    cryst = []
    dens_lists = []

    with open(file_path, 'r') as file:
        for line in file:
            # Parse each line
            r_value, cryst_value, dens_values = parse_line(line)

            # Append the values to their respective lists
            r.append(r_value)
            cryst.append(cryst_value)

            # Append each density value to the corresponding list within dens_lists
            if not dens_lists:
                # Initialize density lists if they are empty
                dens_lists = [[] for _ in range(len(dens_values))]

            # Populate the density lists
            for i, value in enumerate(dens_values):
                dens_lists[i].append(value)

    return r, cryst, dens_lists


# ===== SnO =====

file_path = 'Data/SnO/PDF_cryst_amorphous.dat'
r, cryst, dens_lists = process_file(file_path)

dens_top = dens_lists[:10]
dens_bottom = dens_lists[10:]

colors_1 = ['#610202', '#871e0d', '#ad390f', '#d2560e', '#f67503', '#fc9336', '#fba652', '#f9b86e', '#f8c88c',
            '#FFE7C4']
colors_2 = ['#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df', '#cce6f8']

labels = ['6.01', '5.75', '5.51', '5.28', '5.06', '4.86', '4.67', '4.48', '4.31', '4.15',
          '3.99', '3.84', '3.7', '3.57', '3.44', '3.2', '2.98', '2.78', '2.6']

fig, axs = plt.subplots(3, 2, figsize=(10, 8))

r, prob = read_dat_file_to_lists("Data/SrSnO/PDF_amorphous.dat")
axs[0, 0].plot(r, prob, label='SrSno 4.25', color="black", linewidth=3)
axs[1, 0].plot(r, prob, label='SrSno 4.25', color="black", linewidth=3)
axs[1, 1].plot(r, prob, label='SrSno 4.25', color="black", linewidth=3)
axs[2, 0].plot(r, prob, label='SrSno 4.25', color="black", linewidth=3)
axs[2, 1].plot(r, prob, label='SrSno 4.25', color="black", linewidth=3)

for i, dens in enumerate(dens_top):
    axs[1, 0].plot(r, dens, color=colors_1[i], label=labels[i])
axs[1, 0].plot(r, cryst, color='limegreen', label='Crystalline')
axs[1, 0].set_title('SnO', y=1, pad=-20, fontsize=20)
axs[1, 0].set_ylabel('g(r)', fontsize=24, y=0.5, labelpad=20)
axs[1, 0].set_ylim(0, 11)
axs[1, 0].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', ncols=2, fontsize=11)
axs[1, 0].grid(alpha=0.25)

for i, dens in enumerate(dens_bottom):
    axs[1, 1].plot(r, dens, color=colors_2[i], label=labels[i + 10])
axs[1, 1].set_title('SnO', y=1, pad=-20, fontsize=20)
axs[1, 1].set_xlabel('r (Å)', fontsize=16)
axs[1, 1].set_ylim(0, 11)
axs[1, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', ncols=2, fontsize=11)

# ===== SnO2 =====
file_path = 'Data/SnO2/PDF_cryst_ave_run_12.51_31_11_91.dat'
r, cryst, dens_lists = process_file(file_path)

labels = [6.48, 6.17, 5.88, 5.35]
for i, dens in enumerate(dens_lists):
    axs[0, 0].plot(r, dens, color=colors_1[i], label=labels[i])
axs[0, 0].plot(r, cryst, color='limegreen', label='Crystalline')
axs[0, 0].set_title(r' $\mathrm{SnO_2}$', y=1, pad=-20, fontsize=20)
axs[0, 0].set_ylim(0, 6)
axs[0, 0].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=11)

# ===== Ta2O5 =====
file_path = 'Data/Ta2O5/PDF_cryst_amorphous.dat'
r, cryst, dens_lists = process_file(file_path)
labels = ['8.199', '7.81', '7.44', '7.09', '6.77', '6.18', '5.66', '5.19']
dens_top = dens_lists[:4]
dens_bottom = dens_lists[4:]
for i, dens in enumerate(dens_top):
    axs[2, 0].plot(r, dens, color=colors_1[i], label=labels[i])
axs[2, 0].plot(r, cryst, color='limegreen', label='Crystalline')
axs[2, 0].set_title(r'$\mathrm{Ta_2O_5}$', y=1, pad=-20, fontsize=20)
axs[2, 0].set_xlabel('r (Å)', fontsize=24)
axs[2, 0].xaxis.set_label_coords(1, -0.2)
axs[2, 0].set_ylim(0, 6)
axs[2, 0].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=11)

for i, dens in enumerate(dens_bottom):
    axs[2, 1].plot(r, dens, color=colors_2[i], label=labels[i + 4])
axs[2, 1].set_title(r'$\mathrm{Ta_2O_5}$', y=1, pad=-20, fontsize=20)
axs[2, 1].set_ylim(0, 6)
axs[2, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=11)

# ===== Plot Formatting =====
for i in range(2):
    axs[0, i].set_xticklabels([])
    axs[1, i].set_xticklabels([])
for i in range(3):
    axs[i, 1].set_yticklabels([])
    axs[i, 0].set_xlim(1.7, 5)
    axs[i, 1].set_xlim(1.7, 5)
    
axs[0, 0].set_yticks([2, 4, 6, 8])
axs[2, 0].set_xticks([2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
axs[0, 1].set_yticks([2, 4, 6, 8, 10])
axs[1, 1].set_yticks([2, 4, 6, 8, 10])
axs[2, 0].set_yticks(range(1, 6))
axs[0, 1].set_yticks([2, 4, 6, 8, 10])

for a in axs.flat:
    a.grid(alpha=0.25)
    a.tick_params(axis='x', labelsize=13)
    a.tick_params(axis='y', labelsize=13)
axs[0, 1].grid(alpha=0)
axs[0, 1].spines['top'].set_visible(False)  # Remove top border
axs[0, 1].spines['right'].set_visible(False)  # Remove right border
plt.subplots_adjust(wspace=0.0, hspace=0.0, left=0.2, right=0.833)

plt.show()
