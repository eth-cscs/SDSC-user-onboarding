# Native environment hands-on

1. On Piz Daint's login node, allocate a compute node

```
lukasd@daintYYY:~> salloc -A csstaff -C gpu --nodes=1 --time=30:00
```

2. Get shell access on the compute node - either directly from the login node

```
lukasd@daintYYY:~> srun --pty bash
```

(alternatively, with `native_interactive.sh`) or SSH directly into the compute node (via Ela and Daint login nodes)

```
lukasd@ThinkPad-T470s:~$ ssh ${USER}@nid0XXXX
```

where you can load your environment, e.g. with 

```
module load daint-gpu
module load cray-python
```

and start working interactively

3. Running a single node example script with Python asynchronously through sbatch can be achieved with

```
sbatch submit_native_single.sh env_ex/env.py
```

4. Running a distributed example script with PyTorch DDP asynchronously through sbatch can be achieved with

```
sbatch submit_native_ddp.sh dist_ex/dist_example.py
```

A more complete example will be focused on in the `sarus` section.