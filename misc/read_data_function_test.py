from utility import read_dat_file_to_lists
import matplotlib.pyplot as plt

a, b, c, d, e, f, g = read_dat_file_to_lists("SnO_voids_runs.dat", True)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
# scatter plot density against run num
plt.scatter(a, c)

plt.show()
