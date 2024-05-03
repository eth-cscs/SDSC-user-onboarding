# Native environment hands-on

1. On Piz Daint's login node, allocate a compute node

```
lukasd@daintYYY:~> salloc -A sd00 -C gpu --nodes=1 --time=30:00
```

2. Get shell access on the compute node using

```
lukasd@daintYYY:~> srun --pty bash
```

or, alternatively, with `native_interactive.sh`. To open any extra shells, SSH directly into the compute node (via Ela and Daint login nodes)

```
lukasd@ThinkPad-T470s:~$ ssh nid0XXXX
```

Note that in this case the environment is different from the process managed by `srun` as can be observed in the output of `env`. To load the same environment as in `srun`, you can `source` the output of `declare -x` run in the `srun` shell created above directly after ssh-ing into the compute node.

Once on the compute node, load your environment, e.g. with 

```
module load daint-gpu
module load cray-python
```

and start working interactively

3. Running a single process example script with Python asynchronously through sbatch can be achieved with

```
sbatch submit_native_single.sh env_ex/env.py
```

4. Running a distributed example script with PyTorch DDP asynchronously through sbatch can be achieved with

```
sbatch submit_native_ddp.sh dist_ex/dist_example.py
```

A more complete example will be focused on in the [sarus](../sarus/Readme.md) section.