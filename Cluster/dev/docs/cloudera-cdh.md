Using Anaconda with Cloudera CDH
================================

There are two methods of using Anaconda on an existing cluster with
[Cloudera
CDH](http://www.cloudera.com/products/apache-hadoop/key-cdh-components.html),
Cloudera's Distribution Including Apache Hadoop: 1) the [Anaconda parcel
for Cloudera CDH](http://docs.continuum.io/anaconda/cloudera), and 2)
Anaconda for cluster management. The instructions below describe how to
uninstall the Anaconda parcel on a CDH cluster and transition to
Anaconda for cluster management.

Uninstalling the Anaconda parcel
--------------------------------

If the Anaconda parcel is installed on the CDH cluster, use the
following steps to uninstall the parcel. Otherwise, you can skip to the
next section.

1.  From the Cloudera Manager Admin Console, click the Parcels indicator
    in the top navigation bar.
2.  Click the `Deactivate` button to the right of the Anaconda
    parcel listing.
3.  Click `OK` on the Deactivate prompt to deactive the Anaconda parcel
    and restart Spark and related services.
4.  Click the arrow to the right of the Anaconda parcel listing and
    choose `Remove From Hosts`, which will prompt with a
    confirmation dialog.
5.  The Anaconda parcel has been removed from the cluster nodes.

For more information about managing Cloudera parcels, refer to the
[Cloudera
documentation](http://www.cloudera.com/documentation/enterprise/latest/topics/cm_ig_parcels.html#cmug_topic_7_11_5_unique_1__section_sd4_bzx_bm_unique_1).

Using Anaconda for cluster management
-------------------------------------

Anaconda for cluster management provides additional functionality,
including the ability to manage multiple conda environments and packages
(including Python and R) alongside an existing CDH cluster.

1.  Configure the nodes with Anaconda for cluster management using the
    [Bare-metal Cluster Setup
    instructions](http://docs.continuum.io/anaconda-cluster/create-bare).
2.  During this process, you will create a profile and provider that
    describes the cluster.
3.  Provision the cluster using the following command, replacing
    `cluster-cdh` with the name of your cluster and `profile-cdh` with
    the name of your profile:

    ``` {.sourceCode .bash}
    $ acluster create cluster-cdh -p profile-cdh
    ```

4.  You can submit Spark jobs along with the `PYSPARK_PYTHON`
    environment variable that refers to the location of Anaconda, for
    example:

    ``` {.sourceCode .bash}
    $ PYSPARK_PYTHON=/opt/anaconda/bin/python spark-submit pyspark_script.py
    ```


