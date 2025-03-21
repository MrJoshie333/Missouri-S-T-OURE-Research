import matplotlib.pyplot as plt
import numpy as np

# ===== User Input =====
DEST_DIR = './SrSnO'

# List of directory names (the last four characters are the density)
densities = ["6p27", "5p74", "5p27", "4p85", "4p47", "4p13", "3p82"]

# Save the Figure as a PDF?
SAVEPDF = False

# ===== Initialization =====

plt.figure(figsize=(5, 3))

average_values = []
density_values = []

# ===== Average Density =====
density_averages = {}
for density in densities:
    file_name = f"{DEST_DIR}/etot300k_{density}"
    data = np.loadtxt(file_name)
    avg_value = np.mean(data)
    density_averages[density] = avg_value

min_average = min(density_averages.values())

# ===== Correct Density =====
for density in densities:
    file_name = f"{DEST_DIR}/etot300k_{density}"
    data = np.loadtxt(file_name)
    normalized_data = data - min_average
    scaled_data = (normalized_data / 130) * 1000
    avg_scaled_data = np.mean(scaled_data)
    average_values.append(avg_scaled_data)
    density_values.append(float(density.replace('p', '.')))
    plt.scatter([density_values[-1]] * len(scaled_data), scaled_data, alpha=0.7)

plt.plot(density_values, average_values, marker='o', color='r', label="Average", linestyle='-', linewidth=2)

plt.title("Energy vs. Density , A-SrSnO")
plt.xlabel(r'Density, g/$cm^3$')
plt.ylabel(r'$\mathrm{ΔE, meV/atom}$')
plt.legend(title="Density", loc='upper left')
plt.grid(True, alpha=0.25)
for spine in plt.gca().spines.values():
    spine.set_linewidth(1.8)
plt.tight_layout()
plt.show()

if SAVEPDF == True:
    plt.savefig('SrSnO_single_figure.pdf', format='pdf')
