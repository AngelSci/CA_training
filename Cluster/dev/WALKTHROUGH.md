# install anaconda-cluster

```
conda create -n cluster python=2
activate cluster
conda install -c anaconda-cluster anaconda-cluster
```

# setup provider

* Need key from AWS console
* Secret from Hunt


`.acluster/providers.yaml`

```
aws_west:
  cloud_provider: ec2
  keyname: spark-training
  location: us-west-2
  private_key: ~/.ssh/YOUR-PRIVATE-KEY.pem
  secret_id: YOUR_ID
  secret_key: YOUR_KEY
```

# setup profile

* Choose the right id
* How big?
* 4 nodes without license


`.acluster/profiles.d/spark_training.yaml`

```
name: spark_training
node_id: ami-9abea4fb
node_type: m3.medium
num_nodes: 4
provider: aws_west
user: ubuntu
```

# create the cluster

```
acluster create my_cluster --profile spark_training
```

About 10 minutes

# install jupyter

this is for serial execution on the head node.

```
acluster install notebook
acluster open notebook
```


# spark

It may take a while to install spark and yarn


```
acluster install spark-yarn
```

## cli spark jobs

Prepare a py script like this one

spark-basic.py

```python
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)

def mod(x):
    import numpy as np
    return (x, np.mod(x, 2))

rdd = sc.parallelize(range(1000)).map(mod).take(10)
print rdd
```

```
acluster conda install numpy
```

Copy file to cluster

```
acluster put script.py /home/ubuntu
```

SSH to the head node

```
anaconda ssh
```

Submit the script

```
PYSPARK_PYTHON=/opt/anaconda/bin/python spark-submit spark-basic.py
```

## parallel notebooks

TBD
