FAQ / Known issues
==================

Product FAQ
-----------

**Does Anaconda for cluster management work with a cluster that already
has a managed Spark/Hadoop stack?**

Yes, Anaconda for cluster management can be installed alongside
enterprise Hadoop distributions such as Cloudera CDH or Hortonworks HDP
and can be used to manage Python and R conda packages and environments
across a cluster.

**Does Anaconda for cluster management offer integration with Anaconda
Repository or Anaconda Cloud?**

Yes, conda packages can be installed from Anaconda Repository or
[Anaconda Cloud](http://anaconda.org) by using channel specifications.
Refer to the documentation regarding conda\_channels for more details.

**Which cloud providers does Anaconda for cluster management support?**

Currently Anaconda for cluster management offers full support for Amazon
Elastic Compute Cloud (EC2). Other providers such as Microsoft Azure,
Google Cloud Platform, Rackspace, and others are on our roadmap. If you
are interested in a cloud provider that is not listed here, please
contact us at <sales@continuum.io>.

**Can I use Anaconda for cluster management with a different cloud
provider?**

Yes, you can manually create instances on another cloud provider, then
provision the nodes as if you were using a bare-metal cluster. Refer to
the create-bare documentation for more information.

**Does Anaconda for cluster management support Amazon EMR?**

Anaconda for cluster management does not support Amazon Elastic
MapReduce (EMR), which provides a managed Hadoop framework in the cloud.
Anaconda for cluster management can be used to manage conda packages and
environments across a cluster. Anaconda for cluster management does
support Amazon EC2.

Technical FAQ
-------------

**Which versions of Python does Anaconda for cluster management
support?**

Some of the plugins have dependencies that require the use of Python 2.
Therefore, by default, Anaconda for cluster management installs
Miniconda with Python 2 into the root conda environment.

However, you can easily create a new conda environment on the cluster
with Python 3, or you can specify a different root version of
Anaconda/Miniconda in the profile.

**Which network ports need to be accessible from the client machine and
cluster nodes?**

From the client machine to the cluster nodes, you will need access to
ports 22, 4505, and 4506 to provision the cluster via SSH and Salt. For
communication between the cluster nodes, Salt uses ports 4505 and 4506.

**Can I use Anaconda for cluster management with iptables and SElinux?**

Yes, you can customize the security behavior of Anaconda for cluster
management when creating or provisioning a cluster using the Security
settings in the profile. Refer to the config-profile documentation for
more information.

Troubleshooting FAQ
-------------------

**Errors when creating or provisioning a cluster**

Verify the following:

-   The contents of your SSH private key are correct (and set to `600`
    permissions on Mac/Linux)
-   The user name in your profile (e.g., `user: ubuntu`) is defined
    correctly
-   Profile settings are defined correctly in
    `~/.acluster/profiles.d/<profile_name>.yaml`
-   Provider settings are defined correctly in
    `~/.acluster/providers.yaml`

Known Issues
------------

**No matching SLS error (Salt)**

When installing a plugin during cluster creation/provisioning or using
the `acluster install` command, you might receive an error similar to:

``` {.sourceCode .none}
============================= Standard output =============================

ip-10-144-206-102.ec2.internal:
- No matching sls found for 'cdh5.hdfs' in env 'base'

===========================================================================

Fatal error: One or more hosts failed while executing task 'parallel_sudo'

Aborting.
One or more hosts failed while executing task 'parallel_sudo'
```

This is a known issue with Salt that periodically occurs. You can
reprovision or reinstall the plugin that failed, and the installation
should succeed.

**Theading error when creating a cluster**

When creating/provisioning a cluster, you might receive an error similar
to:

``` {.sourceCode .none}
Uploading formulas
INFO: Uploading formulas to head
Syncing formulas
INFO: Syncing formulas across the cluster
Done
Exception in thread Thread-6 (most likely raised during interpreter shutdown):
Exception in thread Thread-8 (most likely raised during interpreter shutdown):
```

This is a known issue with Paramiko/Fabric. You can safely disregard
this message. This issue was resolved in Anaconda for cluster management
1.3.1.
