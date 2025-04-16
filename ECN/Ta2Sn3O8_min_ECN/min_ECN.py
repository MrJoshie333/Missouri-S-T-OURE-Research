import matplotlib.pyplot as plt
file = "output.txt"

run_nums = []
ecns = []
config_nums = []

with open(file, "r") as f:
    temp = f.readlines()
for line in temp:
    data = line.split()
    run_num = data[1]
    run_num = int(run_num.strip(':'))
    config_num = int(data[3])
    ecn = float(data[5])
    run_nums.append(run_num)
    ecns.append(ecn)
    config_nums.append(config_num)
    print(run_num, config_num, ecn)

#create matplotlib plot
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].plot(run_nums, ecns, 'o')
ax[0].set_xlabel('Run Number', fontsize=12)
ax[0].set_ylabel('ECN', fontsize=12)
ax[0].set_title('ECN vs Run Number, Ta2Sn3O8', fontsize=14)

# Add config numbers as text labels above each point
for i, config in enumerate(config_nums):
    ax[0].annotate(str(config), 
                  (run_nums[i], ecns[i]),
                  xytext=(0, 10), # 10 points vertical offset
                  textcoords='offset points',
                  ha='center') # horizontal alignment



ax[1].scatter(config_nums, ecns)
ax[1].set_xlabel('Config Number', fontsize=12)
ax[1].set_ylabel('ECN', fontsize=12)
ax[1].set_title('ECN vs Config Number, Ta2Sn3O8', fontsize=14)

for i, runnum in enumerate(run_nums):
    ax[1].annotate(str(runnum),
                   (config_nums[i], ecns[i]),
                   xytext=(0, 10),  # 10 points vertical offset
                   textcoords='offset points',
                   ha='center')  # horizontal alignment

plt.tight_layout()
plt.show()
