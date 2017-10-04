How to Run with the YARN resource manager
=========================================

Overview
--------

This script runs on the Spark cluster with the YARN resource manager and
returns the hostname of each node in the cluster.

Who is this for?
----------------

This how-to is for users of a Spark cluster who wish to run Python code
using the YARN resource mananger.

Spark YARN Summary
------------------

1.  before-you-start2
2.  run-yarn-job
3.  troubleshooting2
4.  further-info2

Before you start
----------------

To execute this example, download the
spark-yarn.py example script&lt;spark-yarn/spark-yarn.py&gt; to your
cluster.

For this example, you'll need Spark running with the YARN resource
manager. You can install Spark and YARN using an enterprise Hadoop
distribution such as [Cloudera
CDH](https://www.cloudera.com/products/apache-hadoop/key-cdh-components.html)
or [Hortonworks HDP](http://hortonworks.com/products/hdp/).

Running the Job
---------------

Here is the complete script to run the Spark + YARN example in PySpark:

``` {.sourceCode .python}
# spark-yarn.py
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('spark-yarn')
sc = SparkContext(conf=conf)


def mod(x):
    import numpy as np
    return (x, np.mod(x, 2))

rdd = sc.parallelize(range(1000)).map(mod).take(10)
print rdd
```

Note: you may have to install NumPy with `acluster conda install numpy`.

Run the script on the Spark cluster with
[spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html).
The output shows the first ten values that were returned from the
`spark-basic.py` script.

``` {.sourceCode .text}
16/05/05 22:26:53 INFO spark.SparkContext: Running Spark version 1.6.0

[...]

16/05/05 22:27:03 INFO scheduler.TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0, localhost, partition 0,PROCESS_LOCAL, 3242 bytes)
16/05/05 22:27:04 INFO storage.BlockManagerInfo: Added broadcast_0_piece0 in memory on localhost:46587 (size: 2.6 KB, free: 530.3 MB)
16/05/05 22:27:04 INFO scheduler.TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 652 ms on localhost (1/1)
16/05/05 22:27:04 INFO cluster.YarnScheduler: Removed TaskSet 0.0, whose tasks have all completed, from pool
16/05/05 22:27:04 INFO scheduler.DAGScheduler: ResultStage 0 (runJob at PythonRDD.scala:393) finished in 4.558 s
16/05/05 22:27:04 INFO scheduler.DAGScheduler: Job 0 finished: runJob at PythonRDD.scala:393, took 4.951328 s
[(0, 0), (1, 1), (2, 0), (3, 1), (4, 0), (5, 1), (6, 0), (7, 1), (8, 0), (9, 1)]
```

Troubleshooting
---------------

If something goes wrong consult the ../faq page.

Further information
-------------------

See the [Spark](https://spark.apache.org/) and
[PySpark](https://spark.apache.org/docs/latest/programming-guide.html)
documentation pages for more information.
