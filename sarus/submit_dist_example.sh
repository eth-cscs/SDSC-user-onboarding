#!/bin/bash -l

#SBATCH --job-name=sdsc-onboarding
#SBATCH --time=00:05:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=12
#SBATCH --constraint=gpu
#SBATCH --partition=debug
#SBATCH --account=csstaff

#SBATCH --output=logs/slurm-%x.%j.out
#SBATCH --error=logs/slurm-%x.%j.err


module load daint-gpu
module load sarus

# Environment variable for OpenMP
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Environment variables needed by the NCCL backend for distributed training
export NCCL_DEBUG=INFO
export NCCL_NET_GDR_LEVEL=PHB
export MASTER_ADDR=$(hostname)

echo "SLURM/sbatch: Running sbatch script on ${MASTER_ADDR} - about to launch srun command."

srun -ul sarus run --workdir "$(pwd)" --mount type=bind,source=/scratch,destination=/scratch --mount type=bind,source=${HOME},destination=${HOME} nvcr.io/nvidia/pytorch:23.09-py3 bash -c "
    source ./export_DDP_vars.sh
    python dist_example.py
    "
