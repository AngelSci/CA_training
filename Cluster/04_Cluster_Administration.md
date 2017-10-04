Cluster management
==================

Overview
--------

Anaconda for cluster management provides functionality to easily
interact with clusters, including:

-   Secure shell (SSH) to cluster nodes
-   Executing commands on cluster nodes
-   Uploading (put) and downloading (get) files from cluster nodes
-   Executing salt module commands:
    <http://docs.saltstack.com/en/latest/ref/modules/all/>

For a concise overview of all of the available commands, view the
Anaconda for cluster management Cheat Sheet&lt;anaconda\_cluster\_cheat\_sheet.pdf&gt;.

For the `acluster` commands shown below, you can optionally specify a
`--cluster/-x` option to specify a target cluster to operate on. This
option is not required if only one cluster is running.

SSH access
----------

The command `acluster ssh` can be used to SSH into any node within the
cluster.

The first (optional) argument is a zero-indexed number that refers to a
node, where `0` is the head node, `1` is the first compute node, and so
on.

**Note**: This functionality requires SSH. **Windows users:** Install an
SSH client such as [PuTTY](http://www.putty.org/).

Executing commands
------------------

The `acluster cmd` command allows commands to be executed across
multiple nodes on the cluster. This functionality is performed via salt
(default) or fabric (using the `--ssh/-s` flag).

Salt provides faster execution times (especially in large clusters) of
remote commands, assuming salt is installed and running on the cluster.
Salt is installed by default on cloud providers and can be installed on
bare-metal clusters using the command `acluster install salt`.

Fabric provides remote command execution based on SSH, which can be slow
in big clusters but does not require salt to be installed on the
cluster. Using fabric, you can also target specific nodes using the
`--target/-t` option. The `--target/-t` option can receive the keywords
'head' and 'compute', a number (zero-indexed, where 0 is the head node
and 1 is the first compute node), or two numbers separated by a comma to
target a group of consecutive nodes.

Example:

    $ acluster cmd 'date'
    Executing command "date" target: "*" cluster: "demo_cluster"
    4 nodes response: Thu May 14 19:21:48 UTC 2015
    1 nodes response: Thu May 14 19:21:44 UTC 2015
    1 nodes response: Thu May 14 19:21:47 UTC 2015

    $ acluster cmd 'date' --ssh
    54.196.149.0: Thu May 14 19:22:06 UTC 2015
    54.159.15.86: Thu May 14 19:22:03 UTC 2015
    107.21.159.226: Thu May 14 19:22:06 UTC 2015
    107.20.60.246: Thu May 14 19:22:06 UTC 2015
    54.237.177.104: Thu May 14 19:22:06 UTC 2015
    54.227.91.24: Thu May 14 19:22:06 UTC 2015

    $ acluster cmd 'date' --ssh -t head
    107.21.159.226: Thu May 14 19:23:02 UTC 2015

    $ acluster cmd 'date' --ssh -t 3,6
    54.196.149.0: Thu May 14 19:23:29 UTC 2015
    54.159.15.86: Thu May 14 19:23:26 UTC 2015
    54.227.91.24: Thu May 14 19:23:29 UTC 2015

Upload/download files
---------------------

The commands `acluster put` and `acluster get` allow files to be
uploaded to and downloaded from any node in the cluster. By default, the
`put` and `get` commands target the head node.

Both of the `put` and `get` commands have the same `--target/-t` option,
which has the same functionality as `cmd` with the `-ssh/-s` flag.

Example:

    $ acluster put environment.yml /tmp/env.yml
    Uploading file "environment.yml" to "/tmp/env.yml" - cluster: "demo_cluster" - hosts:
    "['107.21.159.226']"

    $ acluster put environment.yml /tmp/env.yml --all
    Uploading file "environment.yml" to "/tmp/env.yml" - cluster: "demo_cluster" - hosts:
    "['107.21.159.226', '107.20.60.246', '54.237.177.104', '54.159.15.86', '54.196.149.0',
    '54.227.91.24']"

    $ acluster put environment.yml /tmp/env.yml -t ,3
    Uploading file "environment.yml" to "/tmp/env.yml" - cluster: "demo_cluster" - hosts:
    "['107.21.159.226', '107.20.60.246', '54.237.177.104']"

    $ acluster put environment.yml /tmp/env.yml -t compute
    Uploading file "environment.yml" to "/tmp/env.yml" - cluster: "demo_cluster" - hosts:
    "['107.20.60.246', '54.237.177.104', '54.159.15.86', '54.196.149.0', '54.227.91.24']"

The `get` command has similar behavior. Although the `-target/-t` option
is also available, it might not make sense to download the same file
repeatedly since it will get overwritten.

Example:

    $ acluster get /tmp/env.yml env2.yml
    Downloading file "/tmp/env.yml" to "env2.yml" - cluster: "demo_cluster" - hosts:
    "['107.21.159.226']"

    $ acluster get /tmp/env.yml env2.yml --all
    Downloading file "/tmp/env.yml" to "env2.yml" - cluster: "demo_cluster" - hosts:
    "['107.21.159.226', '107.20.60.246', '54.237.177.104', '54.159.15.86', '54.196.149.0',
     '54.227.91.24']"
    Warning: Local file /tmp/env2.yml already exists and is being overwritten.
    Warning: Local file /tmp/env2.yml already exists and is being overwritten.

Command history
---------------

The `acluster history` command displays commands that were previously
executed using `acluster`. By default, the ten most recent commands are
shown.

    $ acluster history
    2015-06-09 23:39:22,515: acluster create demo_cluster --profile profile_name
    2015-06-10 00:00:46,151: acluster ssh
    2015-06-10 00:01:35,304: acluster acluster conda install numpy scipy
    2015-06-10 00:02:01,029: acluster open notebook

Centralized logging
-------------------

You can install the Elasticsearch, Logstash, and Kibana (ELK) plugins
and use them to collect, search, and analyze data. When you install the
ELK plugins, they come preconfigured for centralized logging of other
Anaconda for cluster management plugins. For more information about
plugins, refer to the plugins documentation.

To install the ELK plugins, insert the following in your cluster profile
before you create or provision a cluster:

    plugins:
      - elasticsearch
      - logstash
      - kibana

or, use the following command to install the ELK plugins on an active
cluster:

    $ acluster install elasticsearch logstash kibana

After the ELK plugins are installed, they will begin collecting logs for
various services, and the log data can be searched using Elasticsearch
and visualized using Kibana. You can open the Kibana UI in your browser
using the following command:

    $ acluster open kibana

By default, the following index patterns are available in Kibana:

    YYYY-MM-DD
    salt
    hdfs
    yarn
    spark_yarn
    spark_standalone
    zookeeper
    impala
    hive
    hbase
    hadoop-httpfs
    mapreduce
    syslog

Note that you can use the ELK plugins in a number of different workflows
once they are installed on the cluster, including:

> -   Viewing and searching logs for all cluster-related plugins
> -   Viewing logs for Spark or YARN jobs for centralized job monitoring
>     and troubleshooting
> -   Utilizing centralized logging capabilities from your application

Anaconda for cluster management client information
--------------------------------------------------

The `acluster info` command displays version information related to the
Anaconda for cluster management client installation.

    $ acluster info
    anaconda-cluster version: 1.0
    Platform: Darwin-14.3.0-x86_64
    Processor: i386
    Byte-ordering: little
    Python version: 2.7.10 |Continuum Analytics, Inc.| (default, May 28 2015, 17:04:42)
    [GCC 4.2.1 (Apple Inc. build 5577)]
    apache-libcloud version: 0.16.0
    yaml version: 3.11

Advanced: Running Salt modules
------------------------------

By default, salt provides quite a bit of functionality in its default
modules. All of this functionality is available by using the
`acluster function` command.

For example, you can ping all of the cluster nodes to see that they are
available:

    $ acluster function test.ping
    ip-10-153-156-45.ec2.internal:
        True
    ip-10-169-57-125.ec2.internal:
        True
    ip-10-181-18-153.ec2.internal:
        True
    ip-10-144-199-24.ec2.internal:
        True
    ip-10-113-145-230.ec2.internal:
        True
    ip-10-136-78-206.ec2.internal:
        True

Advanced functions are also available, such as listing all of the IP
address associated with a node:

    $ acluster function network.ipaddrs
    ip-10-169-57-125.ec2.internal:
        - 10.169.57.125
    ip-10-144-199-24.ec2.internal:
        - 10.144.199.24
    ip-10-181-18-153.ec2.internal:
        - 10.181.18.153
    ip-10-153-156-45.ec2.internal:
        - 10.153.156.45
    ip-10-136-78-206.ec2.internal:
        - 10.136.78.206
    ip-10-113-145-230.ec2.internal:
        - 10.113.145.230

Another common salt command can be used to install packages using the
system package manager:

    $ acluster function pkg.install httpd
    ip-10-136-78-206.ec2.internal:
        ...
        httpd:
            ----------
            new:
                2.2.15-39.el6.centos
            old:
        ...

    ip-10-144-199-24.ec2.internal:
        ...
        httpd:
            ----------
            new:
                2.2.15-39.el6.centos
            old:
        ...

> ...

For more information on salt commands, see
<http://docs.saltstack.com/en/latest/ref/modules/all/>

Advanced: Syncing Salt formulas
-------------------------------

The `acluster sync` command is an advanced feature that synchronizes the
Salt formulas from the client to the head node and then across the
cluster.
