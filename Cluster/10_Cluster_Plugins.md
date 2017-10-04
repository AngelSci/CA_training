Plugins
=======

List of available plugins
-------------------------

Anaconda for cluster management can install and manage the following
plugins on a cluster:

> -   [Anaconda](https://docs.continuum.io/anaconda/index)
> -   [Dask/Distributed](http://distributed.readthedocs.org/en/latest/)
> -   [Ganglia](http://ganglia.sourceforge.net/)
> -   [IPython Parallel](https://ipyparallel.readthedocs.org/)
> -   [Jupyter Notebook](https://jupyter.org/)
> -   [Salt](http://saltstack.com/)

The following plugins are unsupported and should only by used for
prototyping/experimental purposes:

> -   [Elasticsearch](https://www.elastic.co/products/elasticsearch)
> -   [HDFS](http://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
> -   [Hive](https://hive.apache.org/)
> -   [Impala](http://impala.io/)
> -   [Kibana](https://www.elastic.co/products/kibana)
> -   [Logstash](https://www.elastic.co/products/logstash)
> -   [Spark (standalone mode or YARN)](https://spark.apache.org/)
> -   [Storm](https://storm.apache.org/)
> -   [YARN](http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html)
> -   [ZooKeeper](https://zookeeper.apache.org/)

If you're interested in using Anaconda with production Hadoop clusters,
Anaconda for cluster management works with enterprise Hadoop
distributions such as [Cloudera
CDH](https://www.cloudera.com/products/apache-hadoop/key-cdh-components.html)
or [Hortonworks HDP](http://hortonworks.com/products/hdp/).

On clusters with existing enterprise Hadoop installations, Anaconda for
cluster management can manage packages (e.g., for PySpark, SparkR, or
Dask) and can install and manage the Jupyter Notebook and Dask plugins.

Installing Plugins
------------------

Plugins can be installed using two methods:

> 1.  Using the cluster `profile.yaml` file when creating or
>     provisioning a cluster.
> 2.  Using the `acluster install` command after the cluster is created.

**1. Install plugins with the profile.yaml file**

When creating or provisioning a cluster, create or edit the file
`~/.acluster/profiles.d/profile_name.yaml` as shown in the example
below:

    name: profile_name
    provider: aws
    node_id: ami-d05e75b8  # Ubuntu 14.04, us-east-1 region
    user: ubuntu
    node_type: m3.large
    num_nodes: 5
    plugins:
      - notebook
      - dask

Optionally, you can configure some plugin settings from within your
profile. For example, you can specify a password to protect a Jupyter
Notebook using:

    name: profile_name
    provider: aws
    node_id: ami-d05e75b8  # Ubuntu 14.04, us-east-1 region
    user: ubuntu
    node_type: m3.large
    num_nodes: 5
    plugins:
      - notebook:
          password: secret

Refer to the plugin\_settings section for more details on configuring
plugin settings.

**2. Install plugins using the acluster install command**

After the cluster has been created, you can view a list of available
plugins with the command `acluster install` as shown in the example
below:

    $ acluster install
    Usage: acluster install [OPTIONS] COMMAND [ARGS]...

      Install plugins across the cluster

    Options:
      -h, --help  Show this message and exit.

    Commands:
      conda             Install (mini)conda
      dask              Install Dask/Distributed
      elasticsearch     Install Elasticsearch
      ganglia           Install Ganglia
      hdfs              Install HDFS
      hive              Install Hive
      impala            Install Impala
      ipython-parallel  Install IPython Parallel
      kibana            Install Kibana
      notebook          Install Jupyter Notebook
      logstash          Install Logstash
      salt              Install Salt
      spark-standalone  Install Spark (standalone)
      spark-yarn        Install Spark (YARN)
      storm             Install Storm
      yarn              Install YARN
      zookeeper         Install Zookeeper

All of the above subcommands can optionally receive a `--cluster/-x`
option to specify a cluster. This option is not required if you only
have one cluster running.

**Note**: Salt is the base for all plugins except Conda. Therefore, the
Salt plugin needs to be installed before the other plugins can be
installed. Salt is installed by default when you create or provision a
cluster using the `acluster create` or `acluster provision` command.

Plugin Settings
---------------

The following plugins support custom settings that can be defined within
a profile.

### Conda

Configure conda packages and environments to be installed upon cluster
creation or provisioning:

    name: profile_name
    plugins:
      - conda:
          environments:
            root:
              - numpy
            py27:
              - python=2.7
              - scipy
              - numba
            py34:
              - python=3.4
              - pandas
              - nltk

Configure the installation location of conda (default: `/opt/anaconda`):

    name: profile_name
    plugins:
      - conda:
          install_prefix: /opt/another_anaconda

Set `conda_sh` to false to disable the creation of
`/etc/profile.d/conda.sh` on cluster nodes (default: true):

    name: profile_name
    plugins:
      - conda:
          conda_sh: false

Set `conda_acl` to a list of users who will be given access for Anaconda
Cluster admin capabilities. Note: When using this setting at least one
user must have sudo access during the provisioning phase. Typically,
this will include the user previously set above as `user`.

    name: profile_name
    plugins:
      - conda:
          conda_acl:
            - user1
            - user2

Set `ssl_verify` to a custom SSL path or to `False` to disable SSL
verification for `conda`. Refer to the [conda
documentation](http://conda.pydata.org/docs/install/central.html#ssl-verification)
for more information.

    name: profile_name
    plugins:
      - conda:
          ssl_verify: False

### Dask

You can optionally set the number of processes (`nprocs`) to use for the
Dask/Distributed workers and the `host` to access the Dask/Distributed
UI via a browser. Refer to the [Dask distributed scheduler
documentation](http://distributed.readthedocs.org/en/latest/) for more
information about these settings.

    name: profile_name
    plugins:
      - dask:
          nprocs: 8
          host: dask-ui.com

### HDFS

By default, the HDFS plugin is configured to use the following
directories: `/data/dfs/nn` on the namenode and `/data/dfs/dn` on the
datanodes. When multiple drives are available, the same directories are
used on all non-root drives.

You can optionally set custom directories for the HDFS namenode and
datanode. For example, the following settings can be used if you want to
utilize a large root volume (e.g., using the `root_volume` profile
setting with Amazon EC2):

    name: profile_name
    plugins:
      - hdfs:
          namenode_dirs:
            - /data/dfs/nn
          datanode_dirs:
            - /data/dfs/dn

### Jupyter Notebook

Set a custom password to protect a Jupyter Notebook (default:
`acluster`):

    name: profile_name
    plugins:
      - notebook:
          password: acluster

Set a custom port for the Jupyter Notebook server (default: `8888`):

    name: profile_name
    plugins:
      - notebook:
          port: 8888

Set a custom directory for Jupyter Notebooks (default:
`/opt/notebooks`):

    name: profile_name
    plugins:
      - notebook:
          directory: /opt/notebooks

### Custom download settings for plugins

Most plugins are installed from the standard package management
repositories for your Linux distribution. Some plugins are downloaded
directly from their source/project website. You can override the default
download settings for the following plugins:

    name: profile_name
    plugins:
      - elasticsearch:
          download_url: https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.1.0/elasticsearch-2.1.0.tar.gz
          download_hash: sha1=b6d681b878e3a906fff8c067b3cfe855240bffbb
          version: elasticsearch-2.1.0
      - logstash:
          download_url: https://download.elastic.co/logstash/logstash/logstash-2.1.1.tar.gz
          download_hash: sha1=d71a6e015509030ab6012adcf79291994ece0b39
          version: logstash-2.1.1
      - kibana:
          download_url: https://download.elastic.co/kibana/kibana/kibana-4.3.0-linux-x64.tar.gz
          download_hash: sha1=d64e1fc0ddeaaab85e168177de6c78ed82bb3a3b
          version: kibana-4.3.0-linux-x64
      - storm:
          source_url: http://apache.arvixe.com/storm/apache-storm-0.9.5/apache-storm-0.9.5.tar.gz
          version_name: apache-storm-0.9.5

Managing Plugins
----------------

The following commands can be used to manage your plugins:

### Plugin Status

Check the status of the plugins by using the `acluster status` command:

    $ acluster status
    Usage: acluster status [OPTIONS] COMMAND [ARGS]...

    Options:
      -x, --cluster TEXT              Cluster name
      -l, --log-level [info|debug|error]
                                      Library logging level
      -h, --help                      Show this message and exit.

    Commands:
      conda             Check Conda status
      dask              Check Dask/Distributed status
      elasticsearch     Check Elasticsearch status
      ganglia           Check Ganglia status
      hdfs              Check HDFS status
      hive              Check Hive status
      impala            Check Impala status
      ipython-parallel  Check IPython Parallel status
      kibana            Check Kibana status
      notebook          Check IPython/Jupyter Notebook status
      salt              Check Salt package status
      salt-conda        Check Salt Conda module status
      salt-key          Check salt-minion keys status
      spark-standalone  Check Spark (standalone) status
      ssh               Check SSH status
      storm             Check Storm status
      yarn              Check YARN status

Example:

    $ acluster status conda
    Checking status of conda on cluster: demo_cluster
    54.81.187.22: True
    54.91.219.252: True
    54.163.26.229: True
    54.145.10.211: True
    Status all: True

    $ acluster status salt
    54.167.128.130: True
    54.205.160.114: True
    50.16.32.99: True
    50.16.34.82: True
    54.163.143.34: True
    Status all: True

    $ acluster status salt-key
    ip-10-156-23-215.ec2.internal: True
    ip-10-147-47-235.ec2.internal: True
    ip-10-225-181-251.ec2.internal: True
    ip-10-237-145-2.ec2.internal: True
    ip-10-156-30-32.ec2.internal: True
    Status all: True

    $ acluster status salt-conda
    ip-10-156-23-215.ec2.internal: True
    ip-10-237-145-2.ec2.internal: True
    ip-10-225-181-251.ec2.internal: True
    ip-10-147-47-235.ec2.internal: True
    ip-10-156-30-32.ec2.internal: True
    Status all: True

The multiple salt status checks perform different checks. The
`acluster status salt` command verifies that the salt package is
installed, the `acluster status salt-key` command verifies that the salt
minions are connected to the head node, and the
`acluster status salt-conda` command verifies that the salt conda module
is distributed across the cluster and is operational.

All of the above checks should return a successful status after
executing `acluster install salt`.

### Open Plugin UIs

Some of the plugins provide a browser UI that can be displayed to the
user. The `acluster open` command is a utility command that opens a
browser window corresponding to each plugin. The command:

    $ acluster open notebook

will open a browser window to the Jupyter Notebook (port 8888).

Use the `--no-browser` option to print the URL for the plugin interface
without opening a browser window.

    $ acluster open notebook --no-browser
    notebook: http://54.172.82.53:8888

### Restart Plugins

If a plugin is not working correctly, restart the processes by using the
`acluster restart` command.

### Stop Plugins

To stop a plugin, use the `acluster stop` command.

Plugin Notes and Network Ports
------------------------------

### HDFS

Requires: `salt`

Distributed file system used by many of the distributed analytics
engines such as `Impala`, `Hive`, and `Spark`.

  Service       Location      Port
  ------------- ------------- -------------
  NameNode UI   Head node     50070
  HDFS Master   Head node     9000
  WebHDFS       Head node     14000

### Jupyter Notebook

Requires: `salt`

Web-based interactive computational environment for Python.

  Service       Location      Port
  ------------- ------------- -------------
  Notebook      Head node     8888

Notebooks are saved in the directory `/opt/notebooks`. You can upload
and download notebooks from the cluster by using the `put` and `get`
commands, respectively.

    $ acluster put mynotebook.ipynb /opt/notebooks/mynotebook.ipynb
    $ acluster get /opt/notebooks/mynotebook.ipynb mynotebook.ipynb

### Miniconda

Python distribution from [Continuum Analytics](http://continuum.io) --
ships with Python libraries for large-scale data processing, predictive
analytics, and scientific computing.

### Salt

Requires: `conda`

Configuration management system.

  Service                 Location       Port
  ----------------------- -------------- --------------
  Salt Master/Minion      All nodes      4505
  Salt Master/Minion      All nodes      4506

### Spark

Computing framework and analytics engine written in Java/Scala with a
Python interface (PySpark).

  Service                  Location      Port
  ------------------------ ------------- -------------
  Spark UI (standalone)    Head node     8080

### YARN

Resource manager in which all Hadoop and Hadoop-like jobs are run.

  Service       Location           Port
  ------------- ------------------ ------------
  Resource UI   Head node          9026
  NodeManager   Compute node(s)    9035


