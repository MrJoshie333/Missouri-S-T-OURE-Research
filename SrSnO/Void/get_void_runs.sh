#!/bin/bash

# Define connection
REMOTE_USER=jmsch4
REMOTE_HOST=mill.mst.edu
REMOTE_BASE=/mnt/stor/ceph/physa/medvedeva/juliaem/ZTO/transfer/SnO/Ta2Sn3O8
LOCAL_BASE="/mnt/c/Users/joshu/PycharmProjects/S&T OURE Research/SrSnO/Void/Ta2Sn3O8_120" # Or any path on your local machine

# List of densities you want to pull from
DENSITIES=(
  a12p30_d7p55 a12p70_d6p86 a13p1_d6p25 a13p5_d5p71 a13p9_d5p23 a14p3_d4p81 a14p7_d4p42 a15p1_d4p08 a15p5_d3p77 a15p9_d3p50
)


for dens in "${DENSITIES[@]}"; do
  for run in {1..10}; do


    REMOTE_FILE="$REMOTE_BASE/$dens/run$run/_quench_200_eq_300/_voids120/volumes.txt"
    LOCAL_DIR="$LOCAL_BASE/$dens/run$run"
    
    mkdir -p "$LOCAL_DIR"

    echo "Copying from $REMOTE_FILE to $LOCAL_DIR"
    scp "$REMOTE_USER@$REMOTE_HOST:$REMOTE_FILE" "$LOCAL_DIR/"
  done
done
