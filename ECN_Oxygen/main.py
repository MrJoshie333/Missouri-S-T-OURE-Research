import matplotlib.pyplot as plt
import numpy as np

# ===== Setup =====
colors = ["red", "darkorange", "blueviolet", "dodgerblue", "darkblue", "limegreen"]
#Save the Figure as a PDF?
SAVEPDF = False

fig, axs = plt.subplots(2, 3)
# ===== Helper Functions =====

# ===== Converts raw density strings to float values =====
def process_density(orig_density):
    return [float(i.split("_")[1].replace("d", "").replace("p", ".")) for i in orig_density]

# ===== Data Processing =====
def process_file(file_path):
    with open(file_path) as f:
        data = f.readlines()

    orig_density, ECN, ECN_time, L_ave, L_ave_time, Distortion, Distortion_time = [], [], [], [], [], [], []
    for row in data:
        row_data = row.split(" ")
        orig_density.append(row_data[0])
        ECN.append(float(row_data[1]))
        ECN_time.append(float(row_data[2]))
        L_ave.append(float(row_data[3]))
        L_ave_time.append(float(row_data[4]))
        Distortion.append(float(row_data[5]))
        Distortion_time.append(float(row_data[6]))

    density_list = process_density(orig_density)
    return density_list, ECN, ECN_time, L_ave, L_ave_time, Distortion, Distortion_time

# ===== Plotting =====
def plot_data(axs, density_list, metrics, label, color):
    (ECN, ECN_time, L_ave, L_ave_time, Distortion, Distortion_time) = metrics
    axs[0, 0].plot(density_list, ECN, label=label, color=color)
    axs[1, 0].plot(density_list, ECN_time, label=label, color=color)
    axs[0, 1].plot(density_list, L_ave, label=label, color=color)
    axs[1, 1].plot(density_list, L_ave_time, label=label, color=color)
    axs[0, 2].plot(density_list, Distortion, label=label, color=color)
    axs[1, 2].plot(density_list, Distortion_time, label=label, color=color)


# ===== File Paths and Plotting =====
files_and_labels = [
    ("Data/ECN_O-SN_SnO_average.dat", "SnO"),
    ("Data/ECN_O-Ta_Ta2O5_average.dat", "Ta2O5"),
    ("Data/ECN_O-M_Ta2Sn3O8_average.dat", "O-M: Ta2Sn3O8"),
    ("Data/ECN_O-M_Ta2Sn10O15_average.dat", "O-M: Ta2Sn10O15"),
    ("Data/ECN_O-M_Ta2SnO6_average.dat", "O-M: Ta2SnO6"),
    ("Data/ECN_O-Sn_SnO2_average.dat", "SnO2")
]

for idx, (file_path, label) in enumerate(files_and_labels):
    density_list, *metrics = process_file(file_path)
    plot_data(axs, density_list, metrics, label, colors[idx])

# ===== Legend and Labels =====
handles, labels = axs[0, 0].get_legend_handles_labels()
handles, labels = handles[:5] + handles[5:], labels[:5] + labels[5:]
axs[0, 1].legend(
    handles,
    labels,
    prop={"size": 16},
    loc="upper center",
    bbox_to_anchor=(0.5, 1.32),
    ncol=2,
    fancybox=True,
    shadow=True,
    fontsize="large",
)

x_labels = [r"Density, g/$cm^3$"] * 3
for ax_row in axs:
    for ax, x_label in zip(ax_row, x_labels):
        ax.set_xlabel(x_label, fontsize=18)

y_labels = [
    "ECN",
    "ECN Time Variance",
    r"L_Average, $\AA$",
    "L_Average Time Variance",
    r"Distortion, $\AA^2$",
    "Distortion Time Variance",
]
for ax, y_label in zip(axs.T.flatten(), y_labels):
    ax.set_ylabel(y_label, fontsize=18, labelpad=30 if "Distortion" not in y_label else 20)

axs[0, 2].set_yticks(np.arange(0.008, 0.022, 0.004))
axs[1, 1].set_yticks(np.arange(0.0008, 0.0022, 0.0004))
axs[1, 2].set_yticks(np.arange(0.0001, 0.00035, 0.00006))

# ===== Grid and Formatting =====
for ax_row in axs:
    for ax in ax_row:
        ax.tick_params(axis="x", labelsize=15)
        ax.tick_params(axis="y", labelsize=15)
        ax.grid(True, alpha=0.25)

plt.subplots_adjust(wspace=0.425, hspace=0.0)
plt.show()

if SAVEPDF == True:
    plt.savefig("Oxygen_ECN_figure.pdf", format="pdf")
