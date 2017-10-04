# Using Adam with AWS

How to install things locally so that you can spin up an AWS cluster and then deploy Anaconda platform components to it, such as Repository, Notebooks, Mosaic, etc.

* [adam docs](https://docs.continuum.io/anaconda-adam/)

## Install Adam with conda

Installing Adam with conda:

```bash
conda install adam -c anaconda-adam
```

Verify install...

```bash
adam info
```

This last command will also display whether adam detected any valid license files. which are needed to deploy the Anaconda platform components. If you do not have a product license file, contact it-help@continuum.io

## License file

A product license file is required to be acquired separately and then located in a specific file path, in order to allow one to provision any of the Anaconda component plug-ins such as Repository and AEN.

Obtain an Anaconda product license file from it-help@continuum.io

The contents should look something like this:

```bash
cat license_bundle_20160707161854.txt

[{"product": "Anaconda Enterprise Repository"

...

"Trial", "email": "dev@continuum.io"}]
```

There are two paths wherein you may need to store this license file:

```
# If you install adam using conda
~/.continuum/license-blob.txt
```

or 

```
# If you install adam using the installer reference in the docs:
~/adam/licenses/license-blob.txt
```


## acluster Credentials as template

Keep your Anaconda Cluster config just for comparison. You'll need some values found therein.

```bash
cp ~/.acluster/providers.yaml ~/backups/acluster/
cp -R ~/.acluster/profiles.d ~/backups/acluster/
```

For comparison, look at this Anaconda Cluster `providers` file:

```bash
cat ~/.acluster/providers.yaml

aws_east:
  cloud_provider: ec2
  keyname: cuda
  location: us-east-1
  private_key: ~/.ssh/cuda.pem
  secret_id: ABCD1234
  secret_key: WXYZ5678
```


## Create an AWS credential file


Read the [Continuum docs on using AWS credentials with adam.](https://docs.continuum.io/anaconda-adam/install-cloud#configure-aws-credentials)

Create an AWS credential file. Here is what your AWS credential file should look like:

```bash
cat ~/.aws/credentials

[default]
aws_access_key_id = ABCD1234
aws_secret_access_key = WXYZ5678
region = us-east-1
```

Note the `aws_access_key_id` and `aws_secret_access_key` are the same as what you had in the Anaconda Cluster file `~/.acluster/providers.yaml` for `secret_id` and `secret_key`, respectively.

## Create a cluster profile

Here is what you're cluster profile file should look like:

```bash
cat ~/.continuum/adam/profile.d/my-cluster.yaml

name: my-cluster
provider: ec2

ec2:
  username: ec2-user
  port: 22
  keypair: ~/.ssh/cuda.pem

security:
  flush_iptables: false
  selinux_context: false
  selinux_permissive: false
```

Note that the `cuda.pem` file (file-root can be anything, e.g. `blob.pem`) was created on the EC2 dash-board while logged-in under the `continuum-training` group, as user `jvestuto`.

## Spin up your AWS cluster

```bash
# Note: Use a RHEL or CentOS AMI if you want to install AEN later! Otherwise, AEN install will complain that RPMs and not debian packages. 

adam ec2 -n my-cluster up --keyname cuda --keypair ~/.ssh/cuda.pem --ami ami-2051294a
```

If you see the following, your cluster is up and running:

```bash
+----------------+--------------+
| Node IP        | Conda module |
+----------------+--------------+
| 54.173.216.172 | True         |
| 54.196.184.235 | True         |
| 54.211.228.83  | True         |
| 52.205.253.188 | True         |
+----------------+--------------+
```

## SSH into your cluster

Just a test...

```bash
adam ssh -n my-cluster
```

For demonstration purposes, it will be useful to log-in remotely, and take a look around before you provision the Anaconda distribution.

```bash
which python
python --verion
# etc
```


## Installing Anaconda distribution

After creating a cluster, you can install a centrally managed version of Anaconda on the cluster nodes:

```bash
$ adam provision -n my-cluster anaconda
```


## Installing Anaconda Platform component interface packages locally

Anaconda component interface packages are available in the `anaconda-adam` channel:

```bash
conda search "adam" -c anaconda-adam
```

Install the component package interfaces locally will then later enable you to deploy the associated Anaconda component plug-ins to your cluster: 

```bash
conda install -c anaconda-adam adam-accelerate
conda install -c anaconda-adam adam-dask
conda install -c anaconda-adam adam-enterprise-notebooks
conda install -c anaconda-adam adam-mosaic
conda install -c anaconda-adam adam-notebook
conda install -c anaconda-adam adam-repository

```

## Installing Anaconda Component plug-ins on AWS Cluster

```bash
$ adam enterprise-notebooks -n my-cluster install
```

## Accessing AEN on AWS Cluster


```bash
adam enterprise-notebooks -n my-cluster open
```


## Destroy your AWS cluster

```bash
adam ec2 -n my-cluster destroy
```


```bash
(adam) [jvestuto:~ ] $ adam ec2 -n my-cluster destroy

2016-08-05 15:47:52,192 - adam.config - DEBUG - Loading cluster from ~/.continuum/adam/cluster.d/my-cluster.yml
2016-08-05 15:47:52,200 - adam.config - INFO - Validating cluster: ~/.continuum/adam/cluster.d/my-cluster.yml
The following EC2 intances are going to be terminated: 
['i-0a0e191d045477fb1', 'i-01a7fd82298a25f64', 'i-0eb4b59ec6a7c3ac9', 'i-009afc26f84466197']

Are you sure you want to destroy the cluster? [y/N]: y

Terminating instances: 
['i-0a0e191d045477fb1', 'i-01a7fd82298a25f64', 'i-0eb4b59ec6a7c3ac9', 'i-009afc26f84466197']
2016-08-05 15:48:00,197 - adam.ec2 - DEBUG - Terminating instances: 
['i-0a0e191d045477fb1', 'i-01a7fd82298a25f64', 'i-0eb4b59ec6a7c3ac9', 'i-009afc26f84466197']
Do you want to remove the `my-cluster` file? [y/N]: y

2016-08-05 15:49:08,657 - adam.config - DEBUG - Loading cluster from ~/.continuum/adam/cluster.d/my-cluster.yml

(adam) [jvestuto:~ ] $
```






