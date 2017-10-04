How to perform a word count on text data in HDFS
================================================

Overview
--------

This example counts the number of words in text files that are stored in
HDFS.

Who is this for?
----------------

This how-to is for users of a Spark cluster who wish to run Python code
using the YARN resource manager that reads and processes files stored in
HDFS.

Spark Wordcount Summary
-----------------------

1.  before-you-start3
2.  load-hdfs-data
3.  run-hdfs-job
4.  troubleshooting3
5.  further-info3

Before you start
----------------

To execute this example, download the
spark-wordcount.py example script&lt;spark-wordcount/spark-wordcount.py&gt;
and the download-data.py script&lt;spark-wordcount/download-data.py&gt;.

For this example, you'll need Spark running with the YARN resource
manager and the Hadoop Distributed File System (HDFS). You can install
Spark, YARN, and HDFS using an enterprise Hadoop distribution such as
[Cloudera
CDH](https://www.cloudera.com/products/apache-hadoop/key-cdh-components.html)
or [Hortonworks HDP](http://hortonworks.com/products/hdp/).

You will also need valid [Amazon Web Services](http://aws.amazon.com/)
(AWS) credentials.

Load HDFS data
--------------

First, we will load the sample text data into the HDFS data store. The
following script will transfer sample text data (approximately 6.4 GB)
from a public Amazon S3 bucket to the HDFS data store on the cluster.

Download the
download-data.py script&lt;spark-wordcount/download-data.py&gt; to your
cluster and Insert your Amazon AWS credentials in the `AWS_KEY` and
`AWS_SECRET` variables.

``` {.sourceCode .python}
import subprocess

AWS_KEY = ''
AWS_SECRET = ''

s3_path = 's3n://{0}:{1}@blaze-data/enron-email'.format(AWS_KEY, AWS_SECRET)
cmd = ['hadoop', 'distcp', s3_path, 'hdfs:///tmp/enron']
subprocess.call(cmd)
```

Note: The `hadoop distcp` command might cause HDFS to fail on smaller
instance sizes due to memory limits.

Run the `download-data.py` script on the Spark cluster.

``` {.sourceCode .bash}
python download-data.py
```

After a few minutes, the text data will be in the HDFS data store on the
cluster and ready for analysis.

Running the Job
---------------

Download the
spark-wordcount.py example script&lt;spark-wordcount/spark-wordcount.py&gt;
to your cluster. This script will read the text files downloaded in step
2 and count all of the words.

``` {.sourceCode .python}
# spark-wordcount.py
from pyspark import SparkConf
from pyspark import SparkContext

HDFS_MASTER = 'HEAD_NODE_IP'

conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('spark-wordcount')
conf.set('spark.executor.instances', 10)
sc = SparkContext(conf=conf)

distFile = sc.textFile('hdfs://{0}:9000/tmp/enron/*/*.txt'.format(HDFS_MASTER))

nonempty_lines = distFile.filter(lambda x: len(x) > 0)
print 'Nonempty lines', nonempty_lines.count()

words = nonempty_lines.flatMap(lambda x: x.split(' '))

wordcounts = words.map(lambda x: (x, 1)) \
                  .reduceByKey(lambda x, y: x+y) \
                  .map(lambda x: (x[1], x[0])).sortByKey(False)

print 'Top 100 words:'
print wordcounts.take(100)
```

Replace the `HEAD_NODE_IP` text with the IP address of the head node.

Run the script on your Spark cluster using
[spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html)
The output shows the top 100 words from the sample text data that were
returned from the Spark script.

``` {.sourceCode .text}
54.237.100.240: Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
15/06/13 04:58:42 INFO SparkContext: Running Spark version 1.4.0

[...]

15/06/26 04:32:03 INFO YarnScheduler: Removed TaskSet 7.0, whose tasks have all completed, from pool
15/06/26 04:32:03 INFO DAGScheduler: ResultStage 7 (runJob at PythonRDD.scala:366) finished in 0.210 s
15/06/26 04:32:03 INFO DAGScheduler: Job 3 finished: runJob at PythonRDD.scala:366, took 18.124243 s
[(288283320, ''), (22761900, '\t'), (19583689, 'the'), (13084511, '\t0'), (12330608, '-'),
(11882910, 'to'), (11715692, 'of'), (10822018, '0'), (10251855, 'and'), (6682827, 'in'),
(5463285, 'a'), (5226811, 'or'), (4353317, '/'), (3946632, 'for'), (3695870, 'is'),
(3497341, 'by'), (3481685, 'be'), (2714199, 'that'), (2650159, 'any'), (2444644, 'shall'),
(2414488, 'on'), (2325204, 'with'), (2308456, 'Gas'), (2268827, 'as'), (2265197, 'this'),
(2180110, '$'), (1996779, '\t$0'), (1903157, '12:00:00'), (1823570, 'The'), (1727698, 'not'),
(1626044, 'such'), (1578335, 'at'), (1570484, 'will'), (1509361, 'has'), (1506064, 'Enron'),
(1460737, 'Inc.'), (1453005, 'under'), (1411595, 'are'), (1408357, 'from'), (1334359, 'Data'),
(1315444, 'have'), (1310093, 'Energy'), (1289975, 'Set'), (1281998, 'Technologies,'),
(1280088, '***********'), (1238125, '\t-'), (1176380, 'all'), (1169961, 'other'), (1166151, 'its'),
(1132810, 'an'), (1127730, '&'), (1112331, '>'), (1111663, 'been'), (1098435, 'This'),
(1054291, '0\t0\t0\t0\t'), (1021797, 'States'), (971255, 'you'), (971180, 'which'), (961102, '.'),
(945348, 'I'), (941903, 'it'), (939439, 'provide'), (902312, 'North'), (867218, 'Subject:'),
(851401, 'Party'), (845111, 'America'), (840747, 'Agreement'), (810554, '#N/A\t'), (807259, 'may'),
(800753, 'please'), (798382, 'To'), (771784, '\t$-'), (753774, 'United'), (740472, 'if'),
(739731, '\t0.00'), (723399, 'Power'), (699294, 'To:'), (697798, 'From:'), (672727, 'Date:'),
(661399, 'produced'), (652527, '2001'), (651164, 'format'), (650637, 'Email'), (646922, '3.0'),
(645078, 'licensed'), (644200, 'License'), (642700, 'PST'), (641426, 'cite'), (640441, 'Creative'),
(640089, 'Commons'), (640066, 'NSF'), (639960, 'EML,'), (639949, 'Attribution'),
(639938, 'attribution,'), (639936, 'ZL'), (639936, '(http://www.zlti.com)."'), (639936, '"ZL'),
(639936, 'X-ZLID:'), (639936, '<http://creativecommons.org/licenses/by/3.0/us/>'), (639936, 'X-SDOC:')]
```

Troubleshooting
---------------

If something goes wrong consult the ../faq page.

Further information
-------------------

See the [Spark](https://spark.apache.org/) and
[PySpark](https://spark.apache.org/docs/latest/programming-guide.html)
documentation pages for more information.
