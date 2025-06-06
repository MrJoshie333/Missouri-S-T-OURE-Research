import os
import numpy as np
#10/90:

# density_list = [
#     '10_90/a13p4_d6p27', '10_90/a13p8_d5p74', '10_90/a14p2_d5p27', '10_90/a14p6_d4p85',
#     '10_90/a15p0_d4p47', '10_90/a15p4_d4p13', '10_90/a15p8_d3p82'
# ]

#30/70:
density_list = ['30_70/a15p0_d4p25', '30_70/a14p212_d5p0']

def compute_overall_for_density(folder):
    # the six numeric fields for Sn and Sr
    fields = ['ecn','ecn_time','L_ave','L_ave_time','Distortion','Distortion_time']
    run_sn = {f: [] for f in fields}
    run_sr = {f: [] for f in fields}

    for run in range(1, 10):
        path = os.path.join(folder, f'run{run}', 'avAllConfigECN.dat')
        with open(path) as f:
            lines = f.readlines()

        # collect raw data for this run
        temp_sn = {f: [] for f in fields}
        temp_sr = {f: [] for f in fields}
        for line in lines:
            p = line.split()
            tag = p[0]  # 'Sn' or 'Sr'
            vals = list(map(float, p[3:9]))  # [ecn, ecn_time, L_ave, L_ave_time, Distortion, Distortion_time]
            if tag == 'Sn':
                for i, f in enumerate(fields):
                    temp_sn[f].append(vals[i])
            else:
                for i, f in enumerate(fields):
                    temp_sr[f].append(vals[i])

        # compute this run's mean for each field
        for f in fields:
            run_sn[f].append(np.mean(temp_sn[f]))
            run_sr[f].append(np.mean(temp_sr[f]))

    # now average those 9 run‑means to get one number per field
    overall_sn = {f: np.mean(run_sn[f]) for f in fields}
    overall_sr = {f: np.mean(run_sr[f]) for f in fields}
    return overall_sn, overall_sr

# gather all densities
results_sn = []
results_sr = []
for density in density_list:
    sn_avg, sr_avg = compute_overall_for_density(density)
    # build one output line per density
    sn_line = f"{density} Sn " + " ".join(f"{sn_avg[f]:.6f}" for f in sn_avg)
    sr_line = f"{density} Sr " + " ".join(f"{sr_avg[f]:.6f}" for f in sr_avg)
    results_sn.append(sn_line)
    results_sr.append(sr_line)

# write files
with open("30_70 txt/sn.txt", "w", encoding="utf-8") as f:
    for line in results_sn:
        f.write(line + "\n")

with open("30_70 txt/sr.txt", "w", encoding="utf-8") as f:
    for line in results_sr:
        f.write(line + "\n")

print("Wrote sn.txt and sr.txt")