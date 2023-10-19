#!/bin/bash

# Load these modules before running this script
# module load daint-gpu
# module load sarus

# ...and allocate a node using salloc, e.g.
# salloc --job-name=sdsc-interactive --time=00:15:00 --nodes=1 --ntasks-per-node=1 --cpus-per-task=12 --constraint=gpu --partition=debug --account=sd00

# Then run this script to launch a container with an interactive shell using
srun --pty sarus run --tty --workdir "$(pwd)" --mount type=bind,source=/scratch,destination=/scratch --mount type=bind,source=${HOME},destination=${HOME} nvcr.io/nvidia/pytorch:23.09-py3 bash