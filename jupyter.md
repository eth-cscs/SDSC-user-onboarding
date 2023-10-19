# Custom Conda Environments & Jupyter Kernels

This section discusses a common workflow to maintain persistent Python environments for development. In this example, we will discuss customizing the user environment with the popular package management system Conda (Miniconda).

Before starting, ensure the right modules are loaded on the shell.

```bash
module load daint-gpu cudatoolkit jupyter-utils
```

## Install Miniconda

Download the installation script

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Run the installer script.

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

Accept the terms by typing `yes` at the end of the agreements and select the default install location.

```console
Do you accept the license terms? [yes|no]
[no] >>> yes

Miniconda3 will now be installed into this location:
/users/<username>/miniconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/users/<username>/miniconda3] >>> 

```

After installation it will ask to initialize conda for which also we type `yes`.

```console
Unpacking payload ...
                                                                                                        
Installing base environment...


Downloading and Extracting Packages


Downloading and Extracting Packages

Preparing transaction: done
Executing transaction: done
installation finished.
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>> yes
```

One may remove the install script once completed
```bash
rm Miniconda3-latest-Linux-x86_64.sh
```

In case something was missed in the previous step, one may initialize your conda installation in bash

```bash
~/miniconda3/bin/conda init bash
```

Now the `.bashrc` file should be updated with some conda setup which will be executed at login.

Logout and log back in again, or type:

```bash
source ~/.bashrc
```

With this, the terminal prompt should look like the following:

```
(base) <username>@daint104:~> 
```

To verify, one may also check the Conda version:

```bash
(base) <username>@daint104:~> conda --version
conda 23.5.2
```

## Create Custom Conda Virtual Environment

### Manually Using Commands

We start with specifying the name of our new environment `myenv` and our desired Python version. By default, a new environment will have v2.7.

```bash
conda create --name myenv python=3.12
```

When conda asks you to proceed, type `y`:

```bash
proceed ([y]/n)?
```

This creates the myenv environment in `/users/<username>/miniconda3/envs/`. No packages will be installed in this environment till this step.

Activate the environment using:

```bash
conda activate myenv
```

Observe the change in the command prompt reflecting the new virtual environment.

```bash
(base) <username>@daint104:~> conda activate myenv
(myenv) <username>@daint104:~> 
```

Now one may install any python packages using pip or a `requirements.txt` file from any project.

### From `environment.yml` File

One may create an `environment.yml` file from another system/cluster to replicate on Daint.

```bash
conda env export > environment.yml
```

OR one may also write their own custom file:

```yaml
name: stats
dependencies:
  - numpy
  - pandas
```

Create the environment from the `environment.yml` file:

```bash
conda env create -f environment.yml
```

The first line of the yml file sets the new environment's name.

Use the following command to check the environments present.

```console
(myenv) <username>@daint104:~> conda info --envs
# conda environments:
#
base                     /users/<username>/miniconda3
myenv                 *  /users/<username>/miniconda3/envs/myenv
```

Use `conda list` to see the packages installed in the current virtual environment.

## Custom JupyterLab Kernels

Users would like to maintain one persistent python environment for development and reuse the same environment for Jupyter Notebooks as well.

CSCS offers a [JupyterLab service](https://jupyter.cscs.ch/) which allows users to run Jupyter notebooks on a compute node on Daint.

Once the desired environment is activated, the `ipykernel` package must be installed in order to create custom Jupyter kernels.

```bash
pip install ipykernel
```

Now to create a Jupyter kernel associated with the currently active conda environment:

```bash
kernel-create -n myenv-kernel
```

Now a kernel named `myenv-kernel` will appear in the drop-down menu in the Jupyterlab service.

This kernel is created in the `/users/<username>/.local/share/jupyter/kernels/` folder. To delete a kernel, one may just delete the folder named after the kernel in the path above.

For more details, visit the official [documentation](https://user.cscs.ch/tools/interactive/jupyterlab/).

#### Ending your interactive session and logging out

The Jupyter servers can be shut down through the Hub. To end a JupyterLab session, please select `Hub Control Panel` under the `File` menu and then `Stop My Server`. By contrast, clicking `Logout` will log you out of the server, but the server will continue to run until the Slurm job reaches its maximum wall time.