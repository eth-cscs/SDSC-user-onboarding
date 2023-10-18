# Containers hands-on

1. On Piz Daint's login node, allocate a compute node

```
lukasd@daintYYY:~> salloc -A csstaff -C gpu --nodes=1 --time=30:00
```

2. Get shell access on the compute node - either directly from the login node

```
lukasd@daintYYY:~> srun --pty bash
```

or SSH directly into the compute node (via Ela and Daint login nodes)

```
lukasd@ThinkPad-T470s:~$ ssh ${USER}@nid0XXXX
```

3. Load the required environment for Sarus via the modules system

```
module load daint-gpu
module load sarus
```

4. Display you locally available container images

```
sarus images
```

5. Check the installed CUDA driver version on Daint

```
lukasd@nid02065:~> nvidia-smi
Wed Oct 18 15:28:21 2023       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  On   | 00000000:02:00.0 Off |                    0 |
| N/A   28C    P0    26W / 250W |      0MiB / 16280MiB |      0%   E. Process |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

to find the corresponding compatible CUDA versions according to this [compatibility matrix](https://docs.nvidia.com/deploy/cuda-compatibility/):

> **CUDA 11 and Later Defaults to Minor Version Compatibility**
> 
> From CUDA 11 onwards, applications compiled with a CUDA Toolkit release from within a CUDA major release family can run, with limited feature-set, on systems having at least the minimum required driver version as indicated below. This minimum required driver can be different from the driver packaged with the CUDA Toolkit but should belong to the same major release. 
> 
> | CUDA Toolkit | Linux x86_64 Minimum Required Driver Version |
> | :----------- | :-------: |
> | CUDA 12.x | >= 525.60.13 |
> | CUDA 11.x | >= 450.80.02* |

and using the corresponding release notes for your container of choice, e.g. for PyTorch https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/index.html

Note that due to the [forward compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/index.html#deployment-consideration-forward) feature, the current CUDA kernel driver can support up to the newest PyTorch release.

6. For Deep Learning with PyTorch, pull a compatible PyTorch image from NVIDIA GPU Cloud (NGC)

```
sarus pull nvcr.io/nvidia/pytorch:23.09-py3
```

There are other containers available for other Deep Learning and Data Science stacks (e.g. TensorFlow or JAX). These contain optimized builds of these dependencies. If you require to build your own environment, you can use `nvcr.io/nvidia/cuda:11.8.0-devel-ubuntu22.04`.

7. You should now find your Sarus image present

```
sarus images
```

8. You can now start an interactive (`-tty`) shell session, mounting your code from the host and starting in the same working directory as you were on the host (`--workdir`)

```
sarus --tty --workdir "$(pwd)" --mount type=bind,source=/scratch,destination=/scratch --mount type=bind,source=${HOME},destination=${HOME} nvcr.io/nvidia/pytorch:23.09-py3 bash
```

If needed, you can also set additional environment variables using `--env` or customize the application launched upon container startup with `--entrypoint`.

