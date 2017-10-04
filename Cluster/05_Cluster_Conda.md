Conda management
================

Overview
--------

One of the primary features of Anaconda for cluster management is the
remote deployment and management of Anaconda environments across a
cluster.

Prepending `acluster` to core `conda` commands will execute those
commands across all of the cluster nodes.

For example, to view the conda environments on all of the cluster nodes:

    $ acluster conda info -e
    All nodes (x3) response:
    # conda environments:
    #
    root                  *  /opt/anaconda

To install numpy on all of the cluster nodes:

    $ acluster conda install numpy
    Installing (u'numpy',) on cluster "demo_cluster"
    Node "ip-10-234-8-208.ec2.internal":
        Successful actions: 1/1
    Node "ip-10-170-59-28.ec2.internal":
        Successful actions: 1/1
    Node "ip-10-232-42-58.ec2.internal":
        Successful actions: 1/1

For a concise overview of all of the available commands, view the
Anaconda for cluster management Cheat Sheet&lt;anaconda\_cluster\_cheat\_sheet.pdf&gt;.

Installing packages from channels
---------------------------------

You can install packages from [Anaconda Cloud](http://anaconda.org) or
from an Anaconda Server installation by adding the `--channel/-c`
option. For example, to install the apache-libcloud package from the
anaconda-cluster channel:

    $ acluster conda install -c https://conda.anaconda.org/anaconda-cluster apache-libcloud
    Installing (u'apache-libcloud',) on cluster "demo_cluster"
    Node "ip-10-136-80-92.ec2.internal":
        Successful actions: 1/1
    Node "ip-10-63-173-62.ec2.internal":
        Successful actions: 1/1
    $ acluster conda list | grep apache-libcloud
    - 'apache-libcloud: 0.16.0 (py27_0)'

List of remote conda commands
-----------------------------

The following conda commands are available in Anaconda for cluster
management:

-   `acluster conda install` -- Install package(s)
-   `acluster conda update` -- Update package(s)
-   `acluster conda remove` -- Remove package(s)
-   `acluster conda list` -- List package(s)
-   `acluster conda create` -- Create conda environment
-   `acluster conda info` -- Display information about current conda
    install
-   `acluster conda push` -- Push conda environment to cluster

For more information about conda, refer to the [conda
documentation](http://conda.pydata.org/).

Example remote conda commands
-----------------------------

### Install conda packages

Any conda package can be installed on a cluster managed by Anaconda for
cluster management:

    $ acluster conda install numpy

    Node "ip-10-136-80-92.ec2.internal":
        Successful actions: 1/1
    Node "ip-10-63-173-62.ec2.internal":
        Successful actions: 1/1

Verify that the package was installed using the `list` command:

    $ acluster conda list

    All nodes (x2) response:
    ...
    - 'numpy: 1.9.2 (py27_0)'
    ...

You may also install multiple conda packages with a single command:

    $ acluster conda install scipy pandas scikit-learn
    Node "ip-10-136-80-92.ec2.internal":
        Successful actions: 3/3
    Node "ip-10-63-173-62.ec2.internal":
        Successful actions: 3/3

    $ acluster conda list
    All nodes (x2) response:
    ...
    - 'pandas: 0.16.1 (np19py27_0)'
    ...
    - 'scikit-learn: 0.16.1 (np19py27_0)'
    - 'scipy: 0.15.1 (np19py27_0)'
    ...

**Note**: It is recommended that you install all of the packages you
want at once. Installing one package at a time can result in dependency
conflicts.

### List conda packages

A useful conda command to run on a cluster is to list the packages that
are available on the nodes (by default all of the nodes should have the
same packages):

    $ acluster conda list

    All nodes (x2) response:
    - 'libsodium: 0.4.5 (0)'
    - 'sqlite: 3.8.4.1 (1)'
    - 'conda-env: 2.1.4 (py27_0)'
    - 'python: 2.7.9 (3)'
    ...

### Update conda packages

You can also specify which versions of conda packages to install or
update:

    $ acluster conda install pandas==0.13
    Installing (u'pandas==0.13',) on cluster "demo_cluster"
    Node "ip-10-136-80-92.ec2.internal":
        Successful actions: 1/1
    Node "ip-10-63-173-62.ec2.internal":
        Successful actions: 1/1
    $ acluster conda list | grep pandas
    - 'pandas: 0.13.0 (np18py27_0)'

    $ acluster conda update pandas
    Updating (u'pandas',) on cluster "demo_cluster"
    Node "ip-10-136-80-92.ec2.internal":
        Successful actions: 1/1
    Node "ip-10-63-173-62.ec2.internal":
        Successful actions: 1/1
    $ acluster conda list | grep pandas
    - 'pandas: 0.16.1 (np19py27_0)'

### Remove conda packages

You can remove conda packages across a cluster:

    $ acluster conda remove pandas
    Removing (u'pandas',) on cluster "demo_cluster"
    Node "ip-10-136-80-92.ec2.internal":
        Successful actions: 1/1
    Node "ip-10-63-173-62.ec2.internal":
        Successful actions: 1/1

    $ acluster conda list | grep pandas
    ... NO OUTPUT ...

### Create conda environments

You can also manage conda environments across a cluster with Anaconda
for cluster management.

To create a new conda environment that contains Python and numpy, use
the command `conda create -n test_env numpy`.

On a cluster, use the same command and simply prepend `acluster` as
shown:

    $ acluster conda create -n test_env numpy
    All nodes (x2) response:
    Conda environment "test_env" created

Once the environment is created, refer to that named environment by
adding the `-n` name option to `conda` commands:

    $ acluster conda list -n test_env
    All nodes (x2) response:
    - 'sqlite: 3.8.4.1 (1)'
    - 'python: 2.7.9 (3)'
    - 'zlib: 1.2.8 (0)'
    - 'openssl: 1.0.1k (1)'
    - 'system: 5.8 (2)'
    - 'tk: 8.5.18 (0)'
    - 'setuptools: 15.2 (py27_0)'
    - 'pip: 6.1.1 (py27_0)'
    - 'readline: 6.2 (2)'
    - 'numpy: 1.9.2 (py27_0)'

    $ acluster conda install -n test_env requests
    Installing (u'requests',) on cluster "d" - target: "*"
    Node "ip-10-136-80-92.ec2.internal":
        Successful actions: 1/1
    Node "ip-10-63-173-62.ec2.internal":
        Successful actions: 1/1

    $ acluster conda list -n test_env
    All nodes (x2) response:
    - 'sqlite: 3.8.4.1 (1)'
    - 'python: 2.7.9 (3)'
    - 'zlib: 1.2.8 (0)'
    - 'openssl: 1.0.1k (1)'
    - 'system: 5.8 (2)'
    - 'tk: 8.5.18 (0)'
    - 'setuptools: 15.2 (py27_0)'
    - 'pip: 6.1.1 (py27_0)'
    - 'readline: 6.2 (2)'
    - 'numpy: 1.9.2 (py27_0)'
    - 'requests: 2.7.0 (py27_0)'

### Push conda environments

You can also push conda environments from the client machine to the
cluster by using a conda `environment.yml` file:

    $ acluster conda push ./environment.yml
    ['ip-10-234-8-208.ec2.internal'] nodes response:
    Conda environment with "/tmp/anaconda-cluster/environment.yml" created
    ...

### List conda environments

To verify that the environment has been pushed to all nodes, use the
`info` command:

    $ acluster conda info -e
    All nodes (x3) response:
    # conda environments:
    #
    stats                    /opt/anaconda/envs/stats
    root                  *  /opt/anaconda
