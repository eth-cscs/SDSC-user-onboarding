# Quick Start to Slurm

Slurm is a commonly used workload manager in HPC clusters. As a cluster workload manager, Slurm has three key functions. 

- First, it allocates exclusive and/or non-exclusive access to resources (compute nodes) to users for some duration of time so they can perform work.
- Second, it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes.
- Third, it arbitrates contention for resources by managing a queue of pending work.

These series of commands work on `daint`.

### `salloc`

This command is used to request an compute resources interactively.

```bash
salloc -N 1 -C gpu -A <project-account> -t 30
```

The command above requests for `1` node from the `gpu` partition for `30` mins. One may also request a multicore partition by specifying `mc` if a GPU is not required.

The output specfies the job ID and node ID(s).

```console
<username>@daint105:> salloc -N 1 -C gpu -t 30
salloc: Pending job allocation 49592309
salloc: job 49592309 queued and waiting for resources
salloc: job 49592309 has been allocated resources
salloc: Granted job allocation 49592309
salloc: Waiting for resource configuration
salloc: Nodes nid01984 are ready for job
```

### `squeue`

This command is used to check allocation of compute resources.

```bash
squeue -u <username>
```

The output looks like this. Also specifies the job ID.

```console
JOBID USER     ACCOUNT           NAME EXEC_HOST ST     REASON   START_TIME     END_TIME  TIME_LEFT NODES   PRIORITY
49592309 <username> csstaff    interactive daint105-  R       None     22:24:22     22:54:24      27:41     1     455674
```

To check the corresponding nodes assigned to the given JOBID:

```bash
squeue -j <jobid> -o "%N"
```

### `scancel`

Use this command release allocations that are not needed anymore.

```bash
scancel <jobid>
```

### `srun`

Use this command to execute a program on an already allocated compute node from the login node.

```bash
srun ./my_executable arg1 arg2
```

## Batch Job Submissions

### `sbatch`

Use this to run a batch script to launch jobs across multiple nodes. Does not require prior allocations. The job is sent to the queue and is executed whenever the scheduler finds a slot.

```
sbatch my_batch_script.sh
```

Batch scripts have specific attributes and syntax which cover the configuration of the run. An example is show in the `sarus` directory. Once in the repo, try:

```bash
cd sarus/
sbatch submit_dist_example.sh dist_ex/dist_example.py
```
