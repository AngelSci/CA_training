How to Run a Spark Standalone Job
=================================

Overview
--------

This is a minimal Spark script that imports PySpark, initializes a
SparkContext and performs a distributed calculation on a Spark cluster
in standalone mode.

Who is this for?
----------------

This how-to is for users of a Spark cluster that has been configured in
standalone mode who wish to run Python code.

Spark Standalone Summary
------------------------

1.  before-you-start1
2.  modify-std-script
3.  run-std-job
4.  troubleshooting1
5.  further-info1

Before you start
----------------

To execute this example, download the
spark-basic.py example script&lt;spark-basic/spark-basic.py&gt; to the
cluster node where you submit Spark jobs.

For this example, you'll need Spark running with the standalone
scheduler. You can install Spark using an enterprise Hadoop distribution
such as [Cloudera
CDH](https://www.cloudera.com/products/apache-hadoop/key-cdh-components.html)
or [Hortonworks HDP](http://hortonworks.com/products/hdp/). Some
additional configuration might be necessary to use Spark in standalone
mode.

Modifying the script
--------------------

After downloading the
spark-basic.py example script&lt;spark-basic/spark-basic.py&gt; open the
file in a text editor on your cluster. Replace `HEAD_NODE_HOSTNAME` with
the hostname of the head node of the Spark cluster.

``` {.sourceCode .python}
# spark-basic.py
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('spark://HEAD_NODE_HOSTNAME:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)

def mod(x):
    import numpy as np
    return (x, np.mod(x, 2))

rdd = sc.parallelize(range(1000)).map(mod).take(10)
print rdd
```

Let's analyze the contents of the `spark-basic.rst example script`. The
first code block contains imports from PySpark.

The second code block initializes the SparkContext and sets the
application name.

The third code block contains the analysis code that calculates the
modulus of a range of numbers up to 1000 using the NumPy package and
returns/prints the first 10 results.

Note: you may have to install NumPy with `acluster conda install numpy`.

Running the job
---------------

You can run this script by submitting it to your cluster for execution
using
[spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html)
or by running this command

``` {.sourceCode .text}
python spark-basic.py
```

The output from the above command shows the first ten values that were
returned from the `spark-basic.py` script.

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
