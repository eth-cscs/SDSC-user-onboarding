# Custom Conda Environments & Jupyter Kernels

This section discusses a common workflow to maintain persistent Python environments for development. In this example, we will discuss customizing the user environment with the popular package management system Conda (Miniconda).

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

