Bare-metal Cluster Setup
========================

Anaconda for cluster management can be used to manage pre-existing
clusters, such as bare-metal machines, collections of virtual machines
(Vagrant, Docker, etc.), or previously instantiated cloud instances.
These types of installations are collectively referred to as *bare-metal
installations.*

**Additional bare-metal cluster requirements:**

-   

    Client machine:

    :   -   Passwordless SSH access to all cluster nodes

-   

    Cluster Nodes:

    :   -   Matching user account/credentials on all nodes with
            passwordless sudo enabled

Provisioning instructions
-------------------------

### 1. Provider Setup

A sample providers file is included with a new installation of Anaconda
for cluster management and is located within the
`~/.acluster/providers.yaml` file on the client machine. You can edit
the contents of this file to reflect the settings for your bare metal
provider.

An example `~/.acluster/providers.yaml` file with a provider named
`bare_metal` is shown below:

``` {.sourceCode .yaml}
bare_metal:
  cloud_provider: none
  private_key: ~/.ssh/my-private-key
```

Refer to the config-provider page for more details about provider
settings.

### 2. Profile Setup

Create a file on the client machine located at
`~/.acluster/profiles.d/profile_name.yaml` that defines the following
information:

``` {.sourceCode .yaml}
name: profile_name
provider: bare_metal
node_id: bare_metal
node_type: bare_metal
user: ubuntu
num_nodes: 4
machines:
  head:
    - 192.168.1.1
  compute:
    - 192.168.1.2
    - 192.168.1.3
    - 192.168.1.4

# Optional for Anaconda Server
# (note that the ports might be different in your configuration)
anaconda_url: http://[your-anaconda-server-ip]:9000/Miniconda-latest-Linux-x86_64.sh
conda_channels:
  - http://[your-anaconda-server-ip]:8080/conda/anaconda-cluster
  - http://[your-anaconda-server-ip]:8080/conda/anaconda
  - defaults
```

The example profile shown above is named `profile_name` and is
configured for a 4-node bare-metal cluster.

Refer to the config-profile page for more details about profile
settings.

### 3. Configure Cluster

Use the following command to configure a bare-metal cluster with the
specified profile:

    $ acluster create demo_cluster --profile profile_name

**Note**: Replace `demo_cluster` with the name of your cluster, and
`profile_name` with the name of your profile.

After this command is executed, the bare-metal cluster will be
configured, and you will see updates as the tasks and initialization
steps are completed.

A typical bare-metal cluster configuration takes a few minutes, and has
output similar to the following:

    $ acluster create demo_cluster --profile profile_name
    Creating cluster
    Number of existing nodes: 0
    Number of requested nodes: 4
    Licensed nodes: 16
    License is valid for the current number of nodes.
    INFO: Creating new cluster "demo_cluster" with profile "profile_name"
    INFO: Creating 4 instances
    INFO: Successfully created instances
    INFO: Cluster info: {'ips': ['54.84.227.194', '52.23.192.232',
          '54.84.184.193', '54.88.116.203'], 'user': 'ubuntu',
          'name': u'demo_cluster'}
    Saving cluster file
    Cluster "demo_cluster": 4 nodes
    Number of existing nodes: 4
    Number of requested nodes: 0
    Licensed nodes: 16
    License is valid for the current number of nodes.
    Checking ssh connection
    INFO: Checking SSH connection
    Checking sudo
    Bootstraping conda
    INFO: Installing miniconda
    INFO: Anaconda URL: https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
    INFO: Checking conda installation
    INFO: Checking conda installation
    Bootstraping salt
    INFO: Setting up Salt master and Minions
    INFO: Creating conda env for salt
    INFO: Installing salt
    Starting salt
    INFO: Flushing iptables rules
    INFO: Setting SELinux to permissive
    INFO: Starting salt-master daemon
    INFO: Starting salt-minion daemon
    Checking salt connection
    Uploading formulas
    INFO: Uploading formulas to head
    INFO: Uploading profile
    Setting Roles
    INFO: Settings grains/roles
    Syncing formulas
    Done

The cluster is now ready for use.

View the troubleshooting\_faq if you encounter errors while creating a
cluster.
