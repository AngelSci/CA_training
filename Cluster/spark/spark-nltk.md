How to do Natural Language Processing
=====================================

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/yceT9sj61vw" frameborder="0" allowfullscreen></iframe></center>
|
-

### Overview

This example provides a simple PySpark job that utilizes the [NLTK
library](http://www.nltk.org/). NLTK is a popular Python package for
natural language processing. This example will demonstrate the
installation of Python libraries on the cluster, the usage of Spark with
the YARN resource manager and execution of the Spark job.

### Who is this for?

This how-to is for users of a Spark cluster who wish to run Python code
using the YARN resource manager. This how-to will show you how to
integrate thrid-party Python libraries with Spark.

### Spark NLTK summary

1.  before-you-start4
2.  install-nltk
3.  run-nltk-job
4.  troubleshooting4
5.  further-info4

### Before you start

To execute this example, download the:
spark-nltk.py example script&lt;spark-nltk/spark-nltk.py&gt; or
spark-nltk.ipynb example notebook&lt;spark-nltk/spark-nltk.ipynb&gt;.

For this example you'll need Spark running with the YARN resource
manager. You can install Spark and YARN using an enterprise Hadoop
distribution such as [Cloudera
CDH](https://www.cloudera.com/products/apache-hadoop/key-cdh-components.html)
or [Hortonworks HDP](http://hortonworks.com/products/hdp/).

### Install NLTK

If you have permission to install packages with `acluster` you can
install NLTK as a conda package.

``` {.sourceCode .bash}
acluster conda install nltk
```

You should see output similar to this from each node, which indicates
that the package was successfully installed across the cluster:

``` {.sourceCode .text}
Node "ip-10-140-235-89.ec2.internal":
    Successful actions: 1/1
Node "ip-10-154-10-144.ec2.internal":
    Successful actions: 1/1
Node "ip-10-31-96-152.ec2.internal":
    Successful actions: 1/1
```

In order to use the full NLTK library, you will need to download the
data for the NLTK project. You can download the data on all cluster
nodes by using the `acluster cmd` command.

``` {.sourceCode .text}
acluster cmd 'sudo /opt/anaconda/bin/python -m nltk.downloader -d /usr/share/nltk_data all'
```

After a few minutes you should see output similar to this.

``` {.sourceCode .text}
Execute command "sudo /opt/anaconda/bin/python -m nltk.downloader -d /usr/share/nltk_data all" target: "*" cluster: "d"
    All nodes (x3) response: [nltk_data] Downloading collection 'all'
[nltk_data]    |
[nltk_data]    | Downloading package abc to /usr/share/nltk_data...
[nltk_data]    |   Unzipping corpora/abc.zip.
[nltk_data]    | Downloading package alpino to /usr/share/nltk_data...
[nltk_data]    |   Unzipping corpora/alpino.zip.
[nltk_data]    | Downloading package biocreative_ppi to
[nltk_data]    |     /usr/share/nltk_data...

....

[nltk_data]    |   Unzipping models/bllip_wsj_no_aux.zip.
[nltk_data]    | Downloading package word2vec_sample to
[nltk_data]    |     /usr/share/nltk_data...
[nltk_data]    |   Unzipping models/word2vec_sample.zip.
[nltk_data]    |
[nltk_data]  Done downloading collection all
```

### Running the Job

Here is the complete script to run the Spark + NLTK example in PySpark.

``` {.sourceCode .python}
# spark-nltk.py
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('spark-nltk')
sc = SparkContext(conf=conf)

data = sc.textFile('file:///usr/share/nltk_data/corpora/state_union/1972-Nixon.txt')

def word_tokenize(x):
    import nltk
    return nltk.word_tokenize(x)

def pos_tag(x):
    import nltk
    return nltk.pos_tag([x])

words = data.flatMap(word_tokenize)
print words.take(10)

pos_word = words.map(pos_tag)
print pos_word.take(5)
```

Let's walk through the above code example. First, we will create a
SparkContext. Note that Anaconda for cluster management will not create
a SparkContext by default. In this example, we use the YARN resource
manager.

``` {.sourceCode .python}
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('spark-nltk')
sc = SparkContext(conf=conf)
```

After a SparkContext is created, we can load some data into Spark. In
this case, the data file is from one of the example documents provided
by NLTK.

``` {.sourceCode .python}
data = sc.textFile('file:///usr/share/nltk_data/corpora/state_union/1972-Nixon.txt')
```

Next, we write a function that imports `nltk` and calls
`nltk.word_tokenize`. The function is mapped to the text file that was
read in the previous step.

``` {.sourceCode .python}
def word_tokenize(x):
    import nltk
    return nltk.word_tokenize(x)

words = data.flatMap(word_tokenize)
```

We can confirm that the `flatMap` operation worked by returning some of
the words in the dataset.

``` {.sourceCode .python}
print words.take(10)
```

Finally, NTLK's [POS-tagger](http://www.nltk.org/book/ch05.html) can be
used to find the part of speech for each word.

``` {.sourceCode .python}
def pos_tag(x):
    import nltk
    return nltk.pos_tag([x])

pos_word = words.map(pos_tag)
print pos_word.take(5)
```

Run the script on the Spark cluster using the
[spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html)
script. The output shows the words that were returned from the Spark
script, including the results from the `flatMap` operation and the
`POS-tagger`.

``` {.sourceCode .text}
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
15/06/13 05:14:29 INFO SparkContext: Running Spark version 1.4.0

[...]

['Address',
 'on',
 'the',
 'State',
 'of',
 'the',
 'Union',
 'Delivered',
 'Before',
 'a']

[...]

[[('Address', 'NN')],
 [('on', 'IN')],
 [('the', 'DT')],
 [('State', 'NNP')],
 [('of', 'IN')]]
```

### Troubleshooting

If something goes wrong consult the ../faq page.

### Further information

See the [Spark](https://spark.apache.org/) and
[PySpark](https://spark.apache.org/docs/latest/programming-guide.html)
documentation pages for more information.

For more information on NLTK see the
NLTK book &lt;http://www.nltk.org/book/&gt;.
