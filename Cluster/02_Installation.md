Installation
============

This page provides information about installing or updating Anaconda for
cluster management on a client machine (Windows, Mac, or Linux, 64-bit)
to manage cloud-based or bare-metal clusters.

Python Requirements
-------------------

Anaconda for cluster management requires Python 2.7. You can create a
new environment in conda with Python 2.7 using the following command:

    $ conda create -n acluster python=2.7

Then, activate the `acluster` environment before running the
installation instructions using the following command:

    $ source activate acluster

Installation Instructions
-------------------------

Anaconda for cluster management can be installed on the client machine
using the conda package manager, which is included in the Anaconda
Python distribution. To download Anaconda, follow the instructions on
the [Anaconda download page](https://www.continuum.io/downloads).

### 1. Authentication

Anaconda for cluster management can be installed after logging into your
[Anaconda Cloud](https://www.anaconda.org) account. After you have
installed Anaconda and refreshed or opened a new terminal window,
install the command-line client for [Anaconda
Cloud](https://www.anaconda.org) using the following command:

    $ conda install anaconda-client -n root

Login to your [Anaconda Cloud](https://www.anaconda.org) account using
the following command:

    $ anaconda login

### 2. Installing on client machine

After you have logged in to your [Anaconda
Cloud](https://www.anaconda.org) account, install Anaconda for cluster
management on your local machine using the following command:

    $ conda install anaconda-cluster -c anaconda-cluster

### 3. Initialization

Anaconda for cluster management saves all configuration information in
the `~/.acluster` directory. To create this directory and populate it
with the initial configuration, run the `acluster` command, which will
print all of the available subcommands:

    $ acluster

After running the `acluster` command, the `~/.acluster` directory is
created, along with an example `provider` file located in
`~/.acluster/providers.yaml` and example `profile` files located in
`~/.acluster/profiles.d/`.

After installing Anaconda for cluster management, you can use the
`acluster` command on your local machine to create new clusters, get
information about clusters that are currently running, install conda
packages on the cluster nodes, and more.

You can now proceed to the quickstart page for a brief walkthrough of
the functionality of Anaconda for cluster management or the create-cloud
or create-bare pages to create and manage a cloud-based or bare-metal
cluster.

Updating
--------

If you've installed Anaconda for cluster management and want to update
to the latest version, make sure you are logged in to your [Anaconda
Cloud](https://www.anaconda.org) account, and use the following command:

    $ conda update anaconda-cluster -c anaconda-cluster

License File Installation
-------------------------

A bundled Anaconda subscription license file (e.g.,
`license_bundle_20160329183212.txt`) can be copied into the
`~/.continuum` directory on the client machine.

A legacy Anaconda for cluster management license file (e.g.,
`cluster_20150408210022.lic`) can be copied into the `~/.acluster`
directory on the client machine.

Once the license file is copied there, you can create, provision, and
manage up to the maximum number of cluster nodes that your license is
valid for.

You can view information about your currently installed license using
the `acluster info` command:

    $ acluster info
    anaconda-cluster version: 1.4.0

    License information:
    License status: Valid
    Number of existing nodes: 4
    Licensed nodes: 16
    License expiration date: 2017-03-29

    Platform: Darwin-15.4.0-x86_64
    Processor: i386
    Byte-ordering: little
    Python version: 2.7.11 | Continuum Analytics, Inc.
    [GCC 4.2.1 (Apple Inc. build 5577)]
    apache-libcloud version: 0.20.1
    yaml version: 3.11

A bundled Anaconda subscription license file with additional products
(e.g., Accelerate) can be copied into the `licenses` directory of the
system-wide installation of Anaconda on each of the cluster nodes
(default: `/opt/anaconda/`). You might need to create the
`/opt/anaconda/licenses/` directory if it does not already exist.

Note that you can also use the following commands from the client
machine to upload a license file to all of the cluster nodes.

    $ acluster cmd "mkdir /opt/anaconda/licenses"
    $ acluster put <LOCAL_FILE> <REMOTE_FILE> --all
