# SSH and VS Code Setup

## SSH Configuration

For passwordless access to the CSCS machines, we configure SSH in our local machines with the keys MFA tools. We need to add some more configuration information in our `~/.ssh/config` file.

```bash
Host ela
    HostName ela.cscs.ch
    IdentitiesOnly yes
    User <username>
    IdentityFile ~/.ssh/cscs-key
    ForwardAgent yes
    ForwardX11 yes
    ForwardX11Trusted yes

Host daint
    HostName daint
    IdentitiesOnly yes
    User <username>
    IdentityFile ~/.ssh/cscs-key
    ProxyJump <username>@ela.cscs.ch
    ForwardAgent yes
    ForwardX11 yes
    ForwardX11Trusted yes
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

## Visual Studio Code Setup

