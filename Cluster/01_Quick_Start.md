Quickstart
==========

This quickstart provides a walkthrough of Anaconda for cluster
management using Amazon Web Services (AWS) Elastic Compute Cloud (EC2).
The steps covered in this quickstart include defining and launching a
cloud-based cluster on Amazon EC2, managing conda packages on the
cluster nodes, and installing plugins.

Installation
------------

Install Anaconda for cluster management on your local machine following
the instructions on the installation page.

Create a provider
-----------------

A sample providers file (shown below) is included with a new
installation of Anaconda for cluster management and is located within
the `~/.acluster/providers.yaml` file.

``` {.sourceCode .yaml}
aws_east:
  cloud_provider: ec2
  keyname: my-private-key
  location: us-east-1
  private_key: ~/.ssh/my-private-key.pem
  secret_id: AKIAXXXXXX
  secret_key: XXXXXXXXXX
```

Edit this file and replace the settings and credentials with your
information.

Refer to the config-provider page for more details about provider
settings, including security groups.

You can list the providers with the command:

    $ acluster list providers

Create a profile
----------------

A sample profile is included with a new installation of Anaconda for
cluster management and is located in the `~/.acluster/profiles.d/`
directory. The sample profile named `aws_profile_sample` is shown below:

``` {.sourceCode .yaml}
name: aws_profile_sample
provider: aws_east
num_nodes: 4
node_id: ami-d05e75b8  # Ubuntu 14.04, us-east-1 region
node_type: m3.large
user: ubuntu
```

You can use this profile to create a 4-node cluster based on Ubuntu
14.04.

Refer to the config-profile page for more details about profile
settings.

You can list the profiles with the command:

    $ acluster list profiles

Create the cluster
------------------

After the provider and profile files are defined, you can create a
cluster using the command:

    $ acluster create demo_cluster --profile aws_profile_sample

This will create your new cluster on Amazon EC2 and provision the
cluster nodes, which typically requires between 5 and 10 minutes. You
will see updates as the tasks and initialization steps are completed.

Install conda packages
----------------------

Now that you have a cluster running, you can install conda packages
using the `acluster conda` command. The `acluster` command can be
prepended to most of the `conda` commands.

To install numpy, scipy, and pandas on all of the cluster nodes, use the
following command:

    $ acluster conda install numpy scipy pandas

**Note**: Refer to the manage-conda page for a full list of remote conda
commands.

Install plugins
---------------

Anaconda for cluster management supports multiple plugins such as Apache
Spark, Hadoop Distributed File System (HDFS), the Jupyter Notebook, and
more. These plugins can be installed on the cluster by using the
`acluster install` command.

For example, the following command can be used to install IPython
Notebook on the cluster:

    $ acluster install notebook

The notebook will be available on `http://{{ HEAD_NODE_IP }}:8888`. You
can open the respective URLs for many of these applications in your
browser using the `acluster open` command:

    $ acluster open notebook

Run the `acluster open` command to view a complete list of supported
applications.

Destroy the cluster
-------------------

When you are finished, the following command can be used to destroy the
cluster and terminate all instances in it. It will prompt for
confirmation before destroying the cluster.

    $ acluster destroy demo_cluster

Further information
-------------------

Refer to the howto-overview page for more example use cases for
use-cases and example scripts.
