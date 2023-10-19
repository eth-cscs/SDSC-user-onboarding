#!/bin/bash -l

#SBATCH --job-name=sdsc-single
#SBATCH --time=00:05:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=12
#SBATCH --constraint=gpu
#SBATCH --partition=debug
#SBATCH --account=csstaff

#SBATCH --output=logs/slurm-%x.%j.out
#SBATCH --error=logs/slurm-%x.%j.err

args="${@}"

module load daint-gpu
# load any further dependencies
module load cray-python

# Environment variable for OpenMP
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

echo "SLURM/$(basename "${SLURM_JOB_SCRIPT}"): Running sbatch script on ${MASTER_ADDR}"

# change to directory of this sbatch script
cd "$(dirname "${SLURM_JOB_SCRIPT}")"
echo "SLURM/$(basename "${SLURM_JOB_SCRIPT}"): Working in $(pwd) - about to launch srun command."

set -x
srun -ul python -u "${args}"
