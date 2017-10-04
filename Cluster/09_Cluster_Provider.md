Provider settings
=================

The following provider settings can be used to define settings for
creating cloud-based or bare-metal clusters. The `providers.yaml` file
can contain credentials and settings for multiple providers.

Provider settings
-----------------

### cloud\_provider

Name of the cloud provider (`ec2`, `none`). Use `none` for bare-metal
clusters.

``` {.sourceCode .yaml}
cloud_provider: ec2
```

### keyname (optional)

Name of the key to authenticate with the cluster nodes. This setting is
used with a cloud provider.

``` {.sourceCode .yaml}
keyname: my-private-key
```

### location (optional)

Region or location to use with a cloud provider.

``` {.sourceCode .yaml}
location: us-east-1
```

### private\_key

Path to the private SSH key on the client machine.

``` {.sourceCode .yaml}
private_key: ~/.ssh/my-private-key.pem
```

### secret\_id (optional)

Secret ID to authenticate with a cloud provider.

``` {.sourceCode .yaml}
secret_id: AKIA***************
```

### secret\_key (optional)

Secret key to authenticate with a cloud provider.

``` {.sourceCode .yaml}
secret_key: RXE*************************************
```

### security\_group (optional)

Security Group to use with a cloud provider. Note that this is the
"Group Name" in the AWS Console, not the "Name" or "Group ID". Note that
you will need access to ports 22, 4505, and 4506 from the client machine
to the cluster nodes to provision the cluster via SSH and Salt. If this
parameter is not specified, then a default Security Group will be
created for you, called `anaconda-cluster-default`, with all ports open.

``` {.sourceCode .yaml}
security_group: my-security-group
```

Sample providers file
---------------------

Below is a sample providers file located in the
`~/.acluster/providers.yaml` file that is configured with all required
and optional settings. The `providers.yaml` file can contain credentials
and settings for multiple providers. The sample providers file shown
below defines two providers named `aws_east` and `bare_metal` for
cloud-based and bare-metal clusters, respectively.

``` {.sourceCode .yaml}
aws_east:
  cloud_provider: ec2
  keyname: my-private-key
  location: us-east-1
  private_key: ~/.ssh/my-private-key.pem
  secret_id: AKIAXXXXXX
  secret_key: XXXXXXXXXX
  security_group: my-security-group

bare_metal:
  cloud_provider: none
  private_key: ~/.ssh/my-private-key
```
