Cloud-based Cluster Setup
=========================

Anaconda for cluster management can launch and bootstrap clusters on a
variety of cloud services. We currently support [Amazon
EC2](https://aws.amazon.com/ec2/). Other providers such as Microsoft
Azure, Rackspace, Google Cloud Platform, and others are on our roadmap.
If you are interested in using a cloud provider that is not listed here,
please contact us at <sales@continuum.io>.

Cloud configuration involves the use of `profiles` and `providers`.
Splitting configurations allows users to easily share and distribute
specific cluster configurations (`profiles`), while retaining private
authentication credentials (`providers`).

1. Provider Setup
-----------------

Authentication and cloud definitions are managed in a single provider
file on the client machine: `~/.acluster/providers.yaml`. A provider
file can contain multiple providers with different settings and
credentials.

A sample providers file is included with a new installation of Anaconda
for cluster management and is located within the
`~/.acluster/providers.yaml` file on the client machine. You can edit
the contents of this file to reflect the settings and credentials for
your cloud provider.

An example `~/.acluster/providers.yaml` file with a provider named
`aws_east` that is configured for Amazon EC2 is shown below:

``` {.sourceCode .yaml}
aws_east:
  cloud_provider: ec2
  keyname: my-private-key
  location: us-east-1
  private_key: ~/.ssh/my-private-key.pem
  secret_id: AKIAXXXXXX
  secret_key: XXXXXXXXXX
```

Note that you will need access to ports 22, 4505, and 4506 from the
client machine to the cluster nodes to provision the cluster via SSH and
Salt.

Refer to the config-provider page for more details about provider
settings, including security groups.

**Linux or Mac:** You should set the permissions of `providers.yaml`
file to `0600`.

2. Profile Setup
----------------

The settings for each cluster are managed in a profile file.

A sample profile is included with a new installation of Anaconda for
cluster management and is located in the `~/.acluster/profiles.d/`
directory on the client machine. You can edit the contents of this file
to reflect the settings for your cluster.

An example profile located at `~/.acluster/profiles.d/profile_name.yaml`
and named `profile_name` that is configured to use the `aws_east`
provider is shown below:

``` {.sourceCode .yaml}
name: profile_name
provider: aws_east
num_nodes: 4
node_id: ami-d05e75b8  # Ubuntu 14.04, us-east-1 region
node_type: m3.large
user: ubuntu
```

Anaconda for cluster management supports and is tested with the
following Linux-based AMIs on Amazon EC2 (us-east-1 region), which can
be set as the `node_id`:

  OS              AMI             User
  --------------- --------------- ---------
  Ubuntu 12.04    ami-08faa660    ubuntu
  Ubuntu 14.04    ami-d05e75b8    ubuntu
  CentOS 6.6      ami-d89fb7b0    root

For more information on AMIs that are available in other Amazon EC2
regions, refer to the [Amazon EC2
documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html)
or the [Ubuntu Amazon EC2 AMI
Locator](https://cloud-images.ubuntu.com/locator/ec2/).

Refer to the config-profile page for more details about profile
settings.

3. Create Cluster
-----------------

Use the following command to launch a cluster with the specified
profile:

    $ acluster create demo_cluster --profile profile_name

**Note**: Replace `demo_cluster` with the name of your cluster, and
`profile_name` with the name of your profile.

After this command is executed, the cloud-based cluster will be created,
and you will see updates as the tasks and initialization steps are
completed.

A typical launch takes between 5 and 10 minutes, and has output similar
to the following:

    $ acluster create demo_cluster --profile profile_name
    Creating cluster
    Number of existing nodes: 0
    Number of requested nodes: 4
    Licensed nodes: 16
    License is valid for the current number of nodes.
    INFO: Creating new cluster "demo_cluster" with profile "profile_name"
    INFO: Creating 4 instances
    INFO: Instances configuration:
    INFO:   Name: demo_cluster
    INFO:   Security Group: ['all-open']
    INFO:   Number of Nodes: 4
    INFO:   Type: <NodeSize: id=m3.large, name=Large Instance, ram=7168
            disk=32000 bandwidth=None price=0.14 driver=Amazon EC2 ...>
    INFO:   Location: us-east-1
    INFO:   Additional Tags {'billingProject': 'anaconda-cluster'}
    INFO: Successfully created instances
    INFO: Cluster info: {'ips': ['54.81.228.35', '54.167.198.242',
          '54.145.107.208', '54.166.207.40'], 'user': 'ubuntu',
          'ids': ['i-29818d89', 'i-2c818d8c', 'i-2e818d8e', 'i-2f818d8f'],
          'name': u'demo_cluster'}
    Saving cluster file
    Cluster "demo_cluster": 4 nodes
    Number of existing nodes: 4
    Number of requested nodes: 0
    Licensed nodes: 16
    License is valid for the current number of nodes.
    Checking ssh connection
    INFO: Checking SSH connection
    Checking sudo
    Bootstraping conda
    INFO: Installing miniconda
    INFO: Anaconda URL: https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
    INFO: Checking conda installation
    INFO: Checking conda installation
    Bootstraping salt
    INFO: Setting up Salt master and Minions
    INFO: Creating conda env for salt
    INFO: Installing salt
    INFO: Settings grains/roles
    INFO: Head roles: []
    INFO: Compute roles: []
    Starting salt
    INFO: Flushing iptables rules
    INFO: Setting SELinux to permissive
    INFO: Starting salt-master daemon
    INFO: Starting salt-minion daemon
    Checking salt connection
    Uploading formulas
    INFO: Uploading formulas to head
    INFO: Uploading profile
    Syncing formulas
    Done

The cluster is now ready for use.

View the troubleshooting\_faq if you encounter errors while creating a
cluster.

4. Destroy Cluster
------------------

If you want to destroy a cluster, use the following command:

    $ acluster destroy demo_cluster

**Note**: Replace the name `demo_cluster` above with the actual name of
your cluster.

After issuing the above command, you will be prompted to confirm
termination of the specified cluster.
