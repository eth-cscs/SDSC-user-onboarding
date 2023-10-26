# SDSC user onboarding workshop

This repository contains materials from the user onboarding workshop for SDSC on Piz Daint at CSCS held on 19th October 2023.

### Morning

An overview on the morning activities is in the following [presentation](slides/morning_presentation.pdf). Topics covered include


- Alps overview
- MFA access
- SSH configuration and using remote IDEs
- SLURM introduction
- Conda environments
  - create custom jupyter-kernel
  - shared between Jupyter service, IDE and shell

The presentation is accompanied by hands-on sections on

- [SSH configuration and using remote IDE usage](ssh_vscode_pycharm.md)
- [SLURM introduction](slurm_intro.md)
- [Custom Conda Environments & Jupyter Kernels](conda_jupyter.md) 


### Afternoon

The afternoon builds on the material in the morning. Refer to these [slides](slides/afternoon_presentation.pdf) for the afternoon. Topics discussed include 

- More in-depth on SLURM
  - running distributed workloads with PyTorch DDP
- Containers at CSCS
  - the Sarus container engine
  - using NGC containers for single node and distributed deep learning with PyTorch DDP on Piz Daint
- Experience in large scale training within MLPerf HPC
- Outlook on Alps
  - Container engine
  - FirecREST
  - High-performance data science on Clariden

The presentation is accompanied by hands-on sections on

- [SLURM in-depth](slurm/Readme.md)
- [Development with containers using Sarus](sarus/Readme.md)

and results from a [data science notebook run](clariden/1M_brain_gpu_analysis_multigpu_clariden.ipynb) on Clariden.
