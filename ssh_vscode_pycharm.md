# MFA, SSH Config and Remote IDE Setup for VS Code & PyCharm

## Multi-Factor Authentication

Before setting this, ensure that the authenticator app is setup for the CSCS account. More on that [here](slides/MFA.pdf).

Use the command line tool to refresh SSH keys that expire every 24 hrs. Download the tool using:

```bash
git clone git@github.com:eth-cscs/sshservice-cli.git
```

Then to get the ssh keys:

```bash
cd sshservice-cli
bash cscs-keygen.sh
```

It will ask you to enter username, password and the OTP from the authenticator app.

```bash
➜  sshservice-cli git:(main) bash cscs-keygen.sh          
Username : pkanduri
Password: 
Enter OTP (6-digit code): 
Setting the environment : [##########------------------------------] 25%  Authenticating to the SSH key service...
Setting the environment : [####################--------------------] 50%  Retrieving the SSH keys...
Setting the environment : [##############################----------] 75%  Setting up the SSH keys into your home folder...
Setting the environment : [########################################] 100%  Completed.
```

Once this happens, use the following command to add the generated key to the SSH agent for 1 day.

```bash
ssh-add -t 1d ~/.ssh/cscs-key
```

## SSH Configuration

For passwordless access to the CSCS machines, we configure SSH in our local machines with the keys configured using the [MFA](https://user.cscs.ch/access/auth/mfa/) tools. We need to add some more configuration information in our `~/.ssh/config` file.

We configure for Ela which is CSCS's front-end machine which connects remote users to clusters within the CSCS network.

```bash
Host ela
    HostName ela.cscs.ch
    User <username>
    IdentitiesOnly yes
    IdentityFile ~/.ssh/cscs-key

Host daint
    User <username>
    IdentitiesOnly yes
    IdentityFile ~/.ssh/cscs-key
    ProxyJump ela

Host nid0*
    User <username>
    IdentitiesOnly yes
    IdentityFile ~/.ssh/cscs-key
    ProxyJump daint
```

With this configuration saved, and active SSH keys from the MFA, we can now do `ssh ela` and reach:

```console
➜  .ssh ssh ela
Last login: Thu Jun 22 17:40:02 2023 from 31-10-158-193.cgn.dynamic.upc.ch
  =========================================================================
               IMPORTANT NOTICE FOR USERS of CSCS facilities
      Documentation: CSCS User Portal - https://user.cscs.ch
      Request support: https://support.cscs.ch
  =========================================================================




  =========================================================================
               IMPORTANT NOTICE FOR USERS of CSCS facilities
      Documentation: CSCS User Portal - https://user.cscs.ch
      Request support: https://support.cscs.ch
  =========================================================================
```

We should also be able to do the same with `daint`.

Once logged into `ela`, the command `quota` reveals the storage used by the user. From `daint`, the command `accounting` shows the usage of the allocated node hours.

## Visual Studio Code Setup

Install the Remote-SSH extension by Microsoft from the marketplace.

![Remote - SSH extension](images/remote-ext.png)

After installation, in the settings, scroll down to the extensions and find the section concerning the one above. There activate the *Remote Server Listen On Socket* setting.

![Listen on Server Setting](images/settings.png)

With these settings, on reload one should be able to find the hosts on the *Remote Explorer* on the left hand side.

![Remote explorer](images/connect-menu.png)

### Connect VS Code to a Compute Node

Obtain an allocation using `salloc`. That should allocate a compute node with nodeID as `nid0XXXX`.

Now in the VS Code settings, add the nodeID along with a path where one'd like VS Code to start from in the *Server Install Path* panel in the Remote-SSH extension section.

![Add nodeID and path](images/add-node.png)

Check in the terminal if `ssh nid0XXXX` works. If yes, then proceed to connect in VS Code using:

`Connect to Host -> nid0XXXX`.


## PyCharm Setup

To use PyCharm Remote Development on Piz Daint, first launch a remote development server and then connect to it using [these instructions](https://www.jetbrains.com/help/pycharm/2023.2/remote-development-a.html#use_idea).

### Initial Setup

For the initial setup, unpack the PyCharm tar archive on $SCRATCH (on $HOME should work as well), which can be done either on a login node or on a compute node.

```
cd $SCRATCH
mkdir pycharm/{.cache,.config}
cd pycharm
# download pycharm-professional-2023.2.3.tar.gz (or any other recent version)
tar -xf pycharm-professional-2023.2.3.tar.gz
```

### Launch the Remote Development Server

After getting a node allocated, launch the remote development server on the compute node (use `export REMOTE_DEV_SERVER_TRACE=1` for debug output). If your Python environment depends on modules, load them before launching the development server as PyCharm has no integration for the module system. Note that the `IJ_HOST_CONFIG_BASE_DIR` and `IJ_HOST_SYSTEM_BASE_DIR` environment variables need to be set to paths under `$SCRATCH`. In the second argument to the development server the project to open is specified.

```
module load ...  # load environment dependencies
IJ_HOST_CONFIG_BASE_DIR=$SCRATCH/pycharm/.config IJ_HOST_SYSTEM_BASE_DIR=$SCRATCH/pycharm/.cache pycharm-2023.2.3/bin/remote-dev-server.sh run $SCRATCH/path/to/project/git/repo --ssh-link-host $(hostname) --ssh-link-user $USER --ssh-link-port 22
```

### Connect PyCharm to the Server

Once the server started, return to your local machine and create an SSH tunnel to the compute node using

```
ssh -N -L 5990:localhost:5990 nid0XXXX
```

Now, copy the `tcp://...` address displayed on the compute node into the form below `Connect to Running IDE` under `Remote Development` when opening PyCharm and click `Connect`. That should open the desired project in your previously loaded environment on the compute node.
