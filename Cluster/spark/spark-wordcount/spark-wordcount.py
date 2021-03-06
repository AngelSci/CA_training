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
