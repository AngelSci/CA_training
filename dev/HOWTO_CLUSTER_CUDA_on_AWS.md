# HOWTO CLUSTER CUDA on AWS


## AWS 

### Trainer Login to AWS

* The trainer will have a `user` log in just for themselves.
* Students will have the key/secret in a providers file and will NOT need log in credentials as they will not be logging into the web site.

* Login fields:
    * account = `continuum-training`
    * user = `<juser>`

### EC2 Dashboard on AWS

What is the quota?

* Yes, but it can be changed.
* AMI CPU: can have 80 of these under `continuum-training` AWS account
* AMI GPU: can have 2 of these under `continuum-training` AWS account
    * We'll raise this up to 22? before the class
    * at least one each, think about more

### EC2 spin up prep, keys

When you create an EC2 instance, you have to give it a key.

* Go to EC2 dashboard to create ssh keys
    * Key Pairs > Create Key Pairs
    * Generates a ZIP file containing, e.g.,
        * `jvestuto-training-keys.csv`
        * `jvestuto-training-pass.csv`
    * or get keys from another trainer

### AMI GPU

* Look at AMI webpage to make sure the AMI is set up for payment.
    * Amazon Linux AMI with NVIDIA GRID GPU Driver 
    * [AMI Description at AWS](https://aws.amazon.com/marketplace/pp/B00FYCDDTE)
    * g2.2xlarge at $0.65/hr
    * g2.8xlarge at $2.60/hr

## Installing acluster

With `acluster`, you install locally before doing `acluster ssh` to connect to the head node of your cluster on AWS.

So you need to create a local `conda` environment for `acluster` using `python=2.7`

```
conda create -n cluster27 python=2.7
```

Check to make sure that the anaconda mirror on AWS host is up-to-date
with whomever installed it.

Install anaconda-cluster, if you use <= 4 nodes, you don't need a license.

```
source activate cluster27
conda install -c anaconda-cluster anaconda-cluster
```

Currently version of `anaconda-cluster` is 1.4.2, but you can only install that if you are logged into `anaconda.org` and specify it by version. The default install as of 2016-July-19 is 1.4.1.

If you have an old `acluster` install, remove/move the directory

```
mv ~/.acluster ~/.acluster_old
```

First execution of `acluster` creates a new ```~/.acluster``` directory if none is there, so just run the help:

```
acluster --help
```

We should ship the entire `~/.acluster` directory to the students

## Configure acluster: Create a provider

A sample providers file (shown below) is included with a new
installation of Anaconda for cluster management and is located within
the `~/.acluster/providers.yaml` file.

Edit the file to fill in specifics, like so:

```
aws_east:
  cloud_provider: ec2
  keyname: cuda
  location: us-east-1
  private_key: ~/.ssh/cuda.pem
  secret_id: AKIAXXXXXX
  secret_key: XXXXXXXXXX
```

* the `secret_id` and `secret_key` fields are values associated with your AWS account, but not the AWS web log-in. When your AWS account is created by an admin, then MUST send you these two values for e.g. 'jvestuto' account so you can put them into the providers.yaml file. 
* If running as trainer, you should receive the values in a CSV file from Hunt, e.g., `jvestuto-training-keys.csv` file
* If you are setting up files for students, use the values for a different user account, aslso from Hunt, called `class1-training-keys.csv`
* key name must match what he saw in EC2 dash board when he created the account.
* The PEM file is not connected to those two `secret` fields and has no password tied to it. You can create one by logging into the AWS web site, but better to use the one from Hunt or Albert.
* PEM file must have `chmod 600` file permissions.
* PEM file should be placed under `~/.ssh/` since it is essentially an SSH key.
* can move the PEM file into the same directory as other files as long as the path is updated in the providers file
 
Refer to the config-provider page for more details about provider
settings, including security groups.

You can list the providers with the command:

```
acluster list providers
```

## Configure acluster: Create a profile

A sample profile is included with a new installation of Anaconda for
cluster management and is located in the `~/.acluster/profiles.d/my_profile.yaml`:

```
name: cuda
provider: aws_east
num_nodes: 4
node_id: ami-2e5e9c43
node_type: g2.2xlarge
user: ec2-user
```

Optionally add tags:

```
name: cuda
provider: aws_east
num_nodes: 4
node_id: ami-2e5e9c43
node_type: g2.2xlarge
user: ec2-user
aws:
  tags:
    - name: GPU-Test-Node
```


* `user: ec2-user` is set when the AMI was created, and `ec2-user` is just a fixed value for use by all trainers, so don't change it. Comes from "Usage instructions" on the EC2 site.
* check the `node_id` on the EC2 dash board to make sure because the AMI changes (every day?)
    * Go to AMI page [AMI Description at AWS](https://aws.amazon.com/marketplace/pp/B00FYCDDTE) 
    * Click "Continue" and look for AWS-East and look for "Launch from EC2 console"
* Refer to the config-profile page for more details about profile
settings.

You can list the profiles with the command:

```
acluster list profiles
```


## Create the cluster

After the provider and profile files are defined, you can create a
cluster using the command:

```
acluster create test-cluster --profile cuda
```

This will create your new cluster on Amazon EC2 and provision the
cluster nodes, which typically requires between 5 and 10 minutes. You
will see updates as the tasks and initialization steps are completed.

Go to the EC2 dash board to see the `test-cluster` nodes running under "instances" side bar tab. "Status check" column will be "hour glass" icons until the nodes are ready, and then will turn green.

If you can `acluster ssh` into the head node, you have confidence that the cluster is built and running:

```
acluster ssh
```

If the ssh times out, which it always does, you will have to do an initial step:

```
acluster install conda salt
```

These installs are called "plug-ins" instead of "packages". These are not conda packages. You have to install conda "plug-in" before you can use conda.

To list the plug-ins available install, do this:

```
acluster install
```

Check general information about the host GPU with the following command:

```
nvidia-smi
```

Or google the GPU card:

[http://databigdata.blogspot.com/2016/02/cuda-devicequery-on-grid-k520-on-aws.html](http://databigdata.blogspot.com/2016/02/cuda-devicequery-on-grid-k520-on-aws.html)

## Install plugins

Anaconda for cluster management supports multiple plugins such as Apache
Spark, Hadoop Distributed File System (HDFS), the Jupyter Notebook, and
more. These plugins can be installed on the cluster by using the
`acluster install` command.

For example, the following command can be used to install IPython
Notebook on the cluster:

```
acluster install notebook
```

The notebook will be available on `http://HEAD_NODE_IP:8888`. You
can open the respective URLs for many of these applications in your
browser using the `acluster open` command:

```
acluster open notebook
```

This notebook is running on the cluster head node. 

Password = `acluster`

Run the `acluster open` command to view a complete list of supported applications.

Now in the notebook check the version of python:

```
import sys
print sys.executable
print sys.version
```

## Conda install at the terminal

```
acluster conda install -c blob accelerate-distribute
```


acluster wants only channels on anaconda.org and not on a different anaconda repository list our AWS host. 

If you cannot successfully configure the AWS host as the repository to pull channels from, use this:

```
acluster conda install -c -c https://conda.anaconda.org/t/de-af9b221e-6836-47e7-a7b5-49695adc54ac/defusco accelerate-dldist accelerate-gensim accelerate-skimage
```

This is our first conda install. Note that you cannot do multiple conda envs on anaconda cluster, just a single "root" env.

```
acluster conda list
```

You'll get two outputs, one from each node.

## Upload files to cluster

```
acluster put my_archive.zip /opt/notebooks # destination path on AWS host
```

SSH into the head node and unzip, but leave everything in `/opt/notebooks`

## Test Accelerate Numba notebook

* `04_Accelerate_Numba.ipynb`
* Testing single node GPU usage

## Test Dask notebook

* `11_Accelerate_Dask_FFT.ipynb`
* With new version of anaconda-cluster 1.4.2, this should now work.

Install the dask "plug-in" for cluster, not a conda package.

```
acluster install dask
```

Check the status of any plug-in

```
acluster status dask
```

Open jupyter

```
acluster open notebook
```

Select the following Dask notebook: `11_Accelerate_Dask_FFT.ipynb`

Note, connecting to the scheduler is always IP of local host 127.0.0.1

Note, in the notebook, `scatter` is like `broadcast` in MPI. Distribute data across nodes.

## Lesson Plan

If you need to skip a notebook for time, skip `06_Accelerate_GPU_blob`

Destroy the cluster
-------------------

When you are finished, the following command can be used to destroy the
cluster and terminate all instances in it. It will prompt for
confirmation before destroying the cluster.

```
acluster destroy test-cluster
```
    
And check the EC2 dash board to see when the AWS cluster nodes are actually killed. You cannot launch additional nodes/clusters until these are destroyed.

