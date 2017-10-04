Overview of Spark, YARN and HDFS
================================

[Spark](http://spark.apache.org/) is an analytics engine and framework
that is capable of running queries 100 times faster than traditional
MapReduce jobs written in Hadoop. In addition to the performance boost,
developers can write Spark jobs in Scala, Python and Java if they so
desire. Spark can load data directly from disk, memory and other data
storage technologies such as Amazon S3, Hadoop Distributed File System
(HDFS), HBase, Cassandra, etc.

You can install Spark using an enterprise Hadoop distribution such as
[Cloudera
CDH](https://www.cloudera.com/products/apache-hadoop/key-cdh-components.html)
or [Hortonworks HDP](http://hortonworks.com/products/hdp/).

Submitting Spark Jobs
---------------------

Spark scripts are often developed interactively and can be written as a
script file or as a Jupyter notebook file.

A Spark script can be submitted to a Spark cluster using various
methods:

-   Running the script directly on the head node.
-   Using the
    [spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html)
    script in either Standalone mode or with the YARN resource manager
-   Interactively in an IPython shell or Jupyter Notebook on the cluster

To run a script on the head node, simply execute `python example.py` on
the cluster.

Note: that in order to launch Jupyter Notebook on the cluster, the
plugin must already be installed. See the ../plugins documentation for
more information.

Working with Data in HDFS
-------------------------

Moving data in and around HDFS can be difficult. If you need to move
data from your local machine to HDFS, from Amazon S3 to HDFS, from
Amazon S3 to Redshift, from HDFS to Hive and so on, we recommend using
[odo](http://odo.readthedocs.org/en/latest/), which is part of the
[Blaze ecosystem](http://blaze.pydata.org/). `Odo` efficiently migrates
data from the source to the target through a network of conversions.

If you are unfamiliar with Spark and/or SQL, we recommend using
[Blaze](http://blaze.readthedocs.org) to express selections,
aggregations, groupbys, etc. in a dataframe-like style. Blaze provides
Python users with a familiar interface to query data that exists in
different data storage systems.
