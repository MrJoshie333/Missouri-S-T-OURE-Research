# ===== Ternary PDF Distribution =====
# ===== Joshua Santy =====
import re

import matplotlib.pyplot as plt


def parse_line(line):
    # Split the line by any whitespace (spaces or tabs)
    parts = re.split(r'\s+', line.strip())

    # Convert each part to the appropriate data type
    r_value = float(parts[0])
    # cryst_value = float(parts[1]) #No crystalline
    dens_values = list(map(float, parts[1:]))

    return r_value, dens_values


def process_file(file_path):
    # Lists to store the parsed data
    r = []
    dens_lists = []

    with open(file_path, 'r') as file:
        for line in file:
            # Parse each line
            r_value, dens_values = parse_line(line)

            # Append the values to their respective lists
            r.append(r_value)

            # Append each density value to the corresponding list within dens_lists
            if not dens_lists:
                # Initialize density lists if they are empty
                dens_lists = [[] for _ in range(len(dens_values))]

            # Populate the density lists
            for i, value in enumerate(dens_values):
                dens_lists[i].append(value)

    return r, dens_lists


fig, axs = plt.subplots(3, 2, figsize=(10, 8))

# Define color schemes
colors_1 = ['#610202', '#871e0d', '#ad390f', '#d2560e', '#f67503', '#fc9336', '#fba652', '#f9b86e', '#f8c88c',
            '#FFE7C4']
colors_2 = ['#08012A', '#181f4c', '#2b3964', '#41537d', '#586f95', '#728cae', '#8ea9c6', '#acc7df', '#cce6f8']

# ===== Ta2Sn10O15 =====
file_path = 'Data/Ta2Sn10O15/PDF_amorphous.dat'
r, dens_lists = process_file(file_path)

dens_top = dens_lists[:10]
dens_bottom = dens_lists[10:]

labels = ['6.61', '6.04', '5.53', '5.3', '5.08', '4.87', '4.68', '4.49', '4.32', '3.99', '3.7', '3.43', '3.19', '2.97',
          '2.77', '2.59', '2.425', '2.27', '2.13']

for i, dens in enumerate(dens_top):
    axs[0, 0].plot(r, dens, color=colors_1[i], label=labels[i])

axs[0, 0].set_title(r'$\mathrm{Ta_2Sn_{10}O_{15}}$', y=1, pad=-20, fontsize=20)
axs[0, 0].set_ylabel('g(r)', fontsize=16)
axs[0, 0].set_ylim(0, 6)
axs[0, 0].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', ncol=2,
                 fontsize=11)  # Split legend into two columns

for i, dens in enumerate(dens_bottom):
    axs[0, 1].plot(r, dens, color=colors_2[i], label=labels[i + 10])
axs[0, 1].set_title(r'$\mathrm{Ta_2Sn_{10}O_{15}}$', y=1, pad=-20, fontsize=20)
axs[0, 1].set_xlabel('r (Å)', fontsize=16)
axs[0, 1].set_ylabel('g(r)', fontsize=16)
axs[0, 1].set_ylim(0, 11)
axs[0, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', ncol=2,
                 fontsize=11)

# ===== Ta2Sn3O8 =====
file_path = 'Data/Ta2Sn3O8/PDF_amorphous.dat'
r, dens_lists = process_file(file_path)

# Split the data into two groups
dens_top = dens_lists[:5]
dens_bottom = dens_lists[5:]
labels = ['7.55', '6.86', '6.25', '5.71', '5.23', '4.81', '4.42', '4.08', '3.77', '3.5']

for i, dens in enumerate(dens_top):
    axs[1, 0].plot(r, dens, color=colors_1[i], label=labels[i])
axs[1, 0].set_title(r'$\mathrm{Ta_2Sn_3O_8}$', y=1, pad=-20, fontsize=20)
axs[1, 0].set_ylabel('g(r)', fontsize=16)
axs[1, 0].set_ylim(0, 6)
axs[1, 0].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=11)

for i, dens in enumerate(dens_bottom):
    axs[1, 1].plot(r, dens, color=colors_2[i], label=labels[i + 5])
axs[1, 1].set_title(r'$\mathrm{Ta_2Sn_3O_8}$', y=1, pad=-20, fontsize=20)
axs[1, 1].set_xlabel('r (Å)', fontsize=16)
axs[1, 1].set_ylabel('g(r)', fontsize=16)
axs[1, 1].set_ylim(0, 6)
axs[1, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=11)

# ===== Ta2SnO6 ======
file_path = 'Data/Ta2SnO6/PDF_amorphous.dat'
r, dens_lists = process_file(file_path)
dens_top = dens_lists[:6]
dens_bottom = dens_lists[6:]
labels = ['8.4', '7.61', '6.92', '6.6', '6.3', '6.02', '5.76', '5.51', '5.28', '4.85', '4.47']

for i, dens in enumerate(dens_top):
    axs[2, 0].plot(r, dens, color=colors_1[i], label=labels[i])
axs[2, 0].set_title(r'$\mathrm{Ta_2SnO_6}$', y=1, pad=-20, fontsize=20)
axs[2, 0].set_xlabel('r (Å)', fontsize=16)
axs[2, 0].set_ylabel('g(r)', fontsize=16)
axs[2, 0].set_ylim(0, 5)
axs[2, 0].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=11)

for i, dens in enumerate(dens_bottom):
    axs[2, 1].plot(r, dens, color=colors_2[i], label=labels[i + 6])
axs[2, 1].set_title(r'$\mathrm{Ta_2SnO_6}$', y=1, pad=-20, fontsize=20)
axs[2, 1].set_xlabel('r (Å)', fontsize=16)
axs[2, 1].set_ylabel('g(r)', fontsize=16)
axs[2, 1].set_ylim(0, 5)
axs[2, 1].legend(title=r'Density (g/$\mathrm{cm}^3$)', loc='upper right', fontsize=11)

# ===== Plot Formatting =====

axs[0, 0].set_yticks(range(1, 6))
axs[1, 0].set_yticks(range(1, 6))
axs[2, 0].set_yticks(range(1, 5))
axs[0, 1].set_yticks([2, 4, 6, 8, 10])
axs[1, 1].set_yticks(range(1, 6))
axs[2, 1].set_yticks(range(1, 5))

for i in range(2):
    axs[0, i].set_xticklabels([])
    axs[1, i].set_xticklabels([])
for i in range(3):
    axs[i, 0].set_xlim(1.6, 5)
    axs[i, 1].set_xlim(1.6, 5)

for a in axs.flat:
    a.grid(alpha=0.25)
    a.tick_params(axis='x', labelsize=13)
    a.tick_params(axis='y', labelsize=13)

plt.subplots_adjust(hspace=0.0, wspace=0.15, left=0.2, right=0.871)

plt.show()
