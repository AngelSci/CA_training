Profile settings
================

The following profile settings can be used to define cluster
configurations for cloud-based or bare-metal clusters. Each named
profile file should contain information for a single cluster definition.

Profile settings
----------------

### anaconda\_url (optional)

Set a custom location to download Anaconda/Miniconda from (default:
Miniconda with Python 2).

``` {.sourceCode .yaml}
anaconda_url: http://localhost/miniconda/Miniconda-latest-Linux-x86_64.sh
```

### aws (optional)

Set AWS options for all instances:

> -   `tags` are optional key/value metadata that are assigned to
>     each instance.
> -   `termination_protection` prevents your instances from being
>     accidentally terminated (default: true).
> -   `use_private_ip` uses the private IP addresses of the AWS nodes
>     instead of the public IP addresses. This is useful if you are
>     using a custom security group (default: false).

``` {.sourceCode .yaml}
aws:
  tags:
    - billingProject: anaconda-cluster
    - cluster_version: production
    - ...
  termination_protection: true
  use_private_ip: true
```

### conda\_channels (optional)

Set custom channels to download conda packages from on the cluster
nodes. This setting will overwrite all of the configured conda channels,
including the default channels. If you are using this setting, you will
need to explicitly include the two default channels, `defaults` and
`anaconda-cluster`, followed by your custom channels.

``` {.sourceCode .yaml}
conda_channels:
  - defaults
  - anaconda-cluster
  - blaze
  - pypi
  - username
  - https://conda.anaconda.org/username/
```

### default\_channels (optional)

Set
[default\_channels](http://conda.pydata.org/docs/install/central.html?highlight=default_channels#default-channels-default-channels)
to download the default conda packages from the URL defined. This
setting will overwrite the default conda channels:
<http://repo.continuum.io>.

``` {.sourceCode .yaml}
default_channels: http://localhost/conda/anaconda
```

### channel\_alias (optional)

Set
[channel\_alias](http://conda.pydata.org/docs/config.html#set-a-channel-alias-channel-alias)
to instruct conda to look for channels in a local repository This
setting will overwrite the default: <http://conda.anaconda.org>.

``` {.sourceCode .yaml}
default_channels: http://localhost/conda/
```

### name

Name of the profile.

``` {.sourceCode .yaml}
name: profile_name
```

### node\_id

Image to configure on each node. For bare-metal clusters, a dummy value
such as `bare-metal` can be used.

``` {.sourceCode .yaml}
node_id: ami-d05e75b8  # Ubuntu 14.04, us-east-1 region
```

### node\_type

The type of node to launch. For bare-metal clusters, a dummy value such
as `bare-metal` can be used.

``` {.sourceCode .yaml}
node_type: m3.large
```

### num\_nodes

Number of nodes to launch (cloud-based) or manage (bare-metal).

``` {.sourceCode .yaml}
num_nodes: 4
```

### machines (optional)

IP addresses of head and compute nodes in the cluster. Note that only IP
addresses should be used with this setting, not hostnames or FQDNs.

This is used along with the create-bare and can refer to bare-metal
nodes, cloud-based nodes that were manually launched outside of Anaconda
for cluster management, or a collection of virtual machines. If SSH is
running on a port other than 22, you can optionally include the SSH port
number (e.g., `192.168.1.1:2222`).

``` {.sourceCode .yaml}
machines:
  head:
    - 192.168.1.1
  compute:
    - 192.168.1.2
    - 192.168.1.3
    - 192.168.1.4
```

### plugins (optional)

Install plugins upon cluster creation or provisioning. Some plugins also
have configruable settings. Refer to the plugin\_settings documentation
for more information.

``` {.sourceCode .yaml}
plugins:
  - notebook
  - dask
```

### provider

Name of the provider to use to launch instances for a cloud-based or
bare-metal cluster. For more information, refer to the config-provider
documentation.

``` {.sourceCode .yaml}
provider: aws_east
```

### root\_size (optional)

Size of the root volume (GB). Currently only used for Amazon EBS
volumes.

``` {.sourceCode .yaml}
root_size: 200
```

### security (optional)

Security settings to enable/disable SELinux or flush iptables rules
(default: true).

``` {.sourceCode .yaml}
security:
  disable_selinux: true
  flush_iptables: true
```

### user

User to SSH to the cluster nodes as. This user must have passwordless
sudo access.

``` {.sourceCode .yaml}
user: ubuntu
```

Sample cloud-based profile file
-------------------------------

Below is a sample cloud-based profile named `profile_name` located in
the `~/.acluster/profiles/profile_name.yaml` file that is configured
with all required and optional settings.

``` {.sourceCode .yaml}
name: profile_name
node_id: ami-d05e75b8  # Ubuntu 14.04, us-east-1 region
node_type: m3.large
num_nodes: 4
provider: aws_east
root_size: 50
user: ubuntu
anaconda_url: http://localhost/miniconda/Miniconda-latest-Linux-x86_64.sh

aws:
  tags:
    - billingProject: anaconda-cluster

plugins:
  - notebook
  - dask

default_channels: http://localhost/conda/anaconda

channel_alias: http://localhost/conda/

conda_channels:
  - defaults
  - anaconda-cluster
  - blaze
  - pypi
  - username
  - https://conda.anaconda.org/username/

security:
  disable_selinux: true
  flush_iptables: true
```

Sample bare-metal profile file
------------------------------

Below is a sample bare-metal profile named `profile_name` located in the
`~/.acluster/profiles/profile_name.yaml` file that is configured with
all required and optional settings.

``` {.sourceCode .yaml}
name: profile_name
node_id: bare_metal
node_type: bare_metal
num_nodes: 4
provider: bare_metal
user: ubuntu
anaconda_url: http://localhost/miniconda/Miniconda-latest-Linux-x86_64.sh

machines:
  head:
    - 192.168.1.1
  compute:
    - 192.168.1.2
    - 192.168.1.3
    - 192.168.1.4

plugins:
  - notebook
  - dask

default_channels: http://localhost/conda/anaconda

channel_alias: http://localhost/conda/

conda_channels:
  - defaults
  - anaconda-cluster
  - blaze
  - pypi
  - username
  - https://conda.anaconda.org/username/

security:
  disable_selinux: false
  flush_iptables: false
```
