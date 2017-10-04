How to do Image Processing with GPUs
====================================

Overview
--------

To demonstrate the capability of running a distributed job in PySpark
using a GPU, this example uses
[NumbaPro](http://docs.continuum.io/numbapro/) and the CUDA platform for
image analysis. This example executes 2-dimensional FFT convolution on
images in grayscale and compares the execution time of CPU-based and
GPU-based calculations.

Who is this for?
----------------

This how-to is for users of a Spark cluster who wish to run Python code
using the YARN resource manager. This how-to will show you how to
integrate third-party Python libraries with Spark.

Image processing summary
------------------------

1.  before-you-start5
2.  install-pkgs
3.  load-image-data
4.  run-numbapro-job
5.  troubleshooting5
6.  further-info5

Before you start
----------------

For this example, you'll need Spark running with the YARN resource
manager. You can install Spark and YARN using an enterprise Hadoop
distribution such as [Cloudera
CDH](https://www.cloudera.com/products/apache-hadoop/key-cdh-components.html)
or [Hortonworks HDP](http://hortonworks.com/products/hdp/).

You will also need valid [Amazon Web Services](http://aws.amazon.com/)
(AWS) credentials in order to download the example data.

For this example, we recommend the use of the GPU-enabled AWS instance
type `g2.2xlarge` and the AMI `ami-12fd8178` (us-east-1 region), which
has CUDA 7.0 and the NVIDIA drivers pre-installed. An example profile
(to be placed in `~/.acluster/profiles.d/gpu_profile.yaml`) is shown
below:

``` {.sourceCode .yaml}
name: gpu_profile
node_id: ami-12fd8178  # Ubuntu 14.04, Cuda 7.0, us-east-1 region
node_type: g2.2xlarge
num_nodes: 4
provider: aws_east
user: ubuntu
```

To execute this example, download the:
spark-numbapro.py example script&lt;spark-numbapro/spark-numbapro.py&gt;
or
spark-numbapro.ipynb example notebook&lt;spark-numbapro/spark-numbapro.ipynb&gt;.

If you wish to use the
spark-numbapro.ipynb example notebook&lt;spark-numbapro/spark-numbapro.ipynb&gt;
the Jupyter Notebook plugin can be installed on the cluster using the
following command:

``` {.sourceCode .text}
acluster install notebook
```

Once the Jupyter Notebook plugin is installed, you can view Jupyter
Notebook in your browser using the following command:

``` {.sourceCode .text}
acluster open notebook
```

Install dependencies
--------------------

If you have permission to install packages with `acluster` you can
install the required packages on all nodes using the following command.

``` {.sourceCode .text}
acluster conda install scipy matplotlib numbapro PIL
```

Load data into HDFS
-------------------

First, we will load the sample text data into the HDFS data store. The
following script will transfer sample image data (approximately 1.1 GB)
from a public Amazon S3 bucket to the HDFS data store on the cluster.

Download the
download-data.py script&lt;spark-numbapro/download-data.py&gt; to your
cluster and insert your Amazon AWS credentials in the `AWS_KEY` and
`AWS_SECRET` variables.

``` {.sourceCode .python}
import subprocess

AWS_KEY = 'YOUR_AWS_KEY'
AWS_SECRET = 'YOUR_AWS_SECRET'

s3_path = 's3n://{0}:{1}@blaze-data/dogs-cats-img/images'.format(AWS_KEY, AWS_SECRET)
cmd = ['hadoop', 'distcp', s3_path, 'hdfs:///tmp/dogs-cats']
subprocess.call(cmd)
```

Note: The `hadoop distcp` command might cause HDFS to fail on smaller
instance sizes due to memory limits.

Run the `download-data.py` script on the cluster.

``` {.sourceCode .bash}
python download-data.py
```

After a few minutes, the image data will be in the HDFS data store on
the cluster and ready for analysis.

Running the Job
---------------

Run the `spark-numbapro.py` script on the Spark cluster using
[spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html).
The output shows the image processing execution times for the CPU-based
vs. GPU-based calculations.

``` {.sourceCode .text}
54.164.123.31: Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
15/11/09 02:33:21 INFO SparkContext: Running Spark version 1.5.1

[...]

15/11/09 02:33:45 INFO TaskSetManager: Finished task 6.0 in stage 1.0 (TID 13)
in 106 ms on ip-172-31-9-24.ec2.internal (7/7)
15/11/09 02:33:45 INFO YarnScheduler: Removed TaskSet 1.0, whose tasks have
all completed, from pool
15/11/09 02:33:45 INFO DAGScheduler: ResultStage 1
(collect at /tmp/anaconda-cluster/spark-numbapro.py:106) finished in 4.844 s
15/11/09 02:33:45 INFO DAGScheduler: Job 1 finished:
collect at /tmp/anaconda-cluster/spark-numbapro.py:106, took 4.854970 s

10 images
CPU: 6.91735601425
GPU: 4.88133311272

[...]

15/11/09 02:34:27 INFO TaskSetManager: Finished task 255.0 in stage 3.0 (TID 525)
 in 139 ms on ip-172-31-9-24.ec2.internal (256/256)
15/11/09 02:34:27 INFO YarnScheduler: Removed TaskSet 3.0, whose tasks have
all completed, from pool
15/11/09 02:34:27 INFO DAGScheduler: ResultStage 3
(collect at /tmp/anaconda-cluster/spark-numbapro.py:126) finished in 19.340 s
15/11/09 02:34:27 INFO DAGScheduler: Job 3 finished:
collect at /tmp/anaconda-cluster/spark-numbapro.py:126, took 19.400670 s

500 images
CPU: 22.1282501221
GPU: 19.8209779263
```

Troubleshooting
---------------

If something goes wrong consult the ../faq page.

Further information
-------------------

See the [Spark](https://spark.apache.org/) and
[PySpark](https://spark.apache.org/docs/latest/programming-guide.html)
documentation pages for more information.

For more information on NumbaPro see the [NumbaPro
documentation](https://docs.continuum.io/numbapro/index).
