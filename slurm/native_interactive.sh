#!/bin/bash

# Allocate a node using salloc before running this script, e.g.
# salloc --job-name=sdsc-interactive --time=00:15:00 --nodes=1 --ntasks-per-node=1 --cpus-per-task=12 --constraint=gpu --partition=debug --account=csstaff

# Then run this script to launch an interactive shell in the native environment using
srun --pty bash