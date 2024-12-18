"""
Density vs Energy Plotter
Joshua Santy

Be sure to change num_atoms to however many atoms were used

"""
import matplotlib.pyplot as plt

# ===== User Input =====
# Save the Figure as a PDF?
SAVEPDF = False
num_atoms = [138, 140, 138, 135, 130, 134]


def averages(input):
    average_array = []
    count = 0
    straight_counter = 0
    for values in temp1:
        tot_sum = sum(input[count:count + density_count[straight_counter]])
        average_array.append(tot_sum / density_count[straight_counter])
        count += density_count[straight_counter]
        straight_counter += 1
    return average_array

# ===== Initialization =====
fig, axs = plt.subplots(ncols=3)
k = 0

file_names = ["Data/SnO_voids_runs.dat"]
for a in file_names:
    with open(a) as f:
        data = f.readlines()
    a = a[:-29]
    orig_density = []
    num_runs = []
    temp1 = []
    density_count = []
    void_percent = []
    largest_void = []
    surface_vs_largest = []
    del data[0]

    # Getting Data
    for i in data:
        rowData = i.split(" ")
        orig_density.append(rowData[0])
        num_runs.append(rowData[1])
        void_percent.append(float(rowData[2]))
        largest_void.append(float(rowData[3]))
        surface_vs_largest.append(float(rowData[4]))

    density_list = []

    # Turning Density into Float
    for i in orig_density:
        i = i.split("_")
        i = i[1]
        i = i.replace("d", "")
        i = i.replace("p", ".")
        i = float(i)
        density_list.append(i)

    for j in density_list:
        if j not in temp1:
            temp1.append(j)
            density_count.append(density_list.count(j))
    # Averages
    void_percent_avg = averages(void_percent)
    largest_void_avg = averages(largest_void)
    surface_vs_largest_avg = averages(surface_vs_largest)

    axs[0].plot(temp1, void_percent_avg, color="navy")
    axs[0].scatter(density_list, void_percent, color="orange")
    axs[1].plot(temp1, largest_void_avg, color="navy")
    axs[1].scatter(density_list, largest_void, color="orange")
    axs[2].plot(temp1, surface_vs_largest_avg, color="navy")
    axs[2].scatter(density_list, surface_vs_largest, color="orange")

    axs[1].set_xlabel(r'$\mathrm{Density, \frac{g}{cm^3}}$', fontsize='16')
    axs[0].set_ylabel('Fraction of Void Volume', fontsize='16')
    axs[1].set_ylabel('Fraction of 1st Largest Void', fontsize='16')
    axs[2].set_ylabel('Surface to Volume of 1st Largest Void', fontsize='16')

for a in axs.flat:
    a.grid(True, alpha=0.35)

axs[1].set_title("SnO", fontsize=24)
plt.subplots_adjust(left=0.2,
                    bottom=0.3,
                    right=0.8,
                    top=0.7,
                    wspace=0.3,
                    hspace=0.61)
plt.show()
if SAVEPDF == True:
    plt.savefig('void_SnO_only.pdf', format='pdf')