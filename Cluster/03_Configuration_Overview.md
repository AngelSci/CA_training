Configuration
=============

After installing Anaconda for cluster management and running any
`acluster` command, the `~/.acluster` directory is created, along with a
sample `provider` file located in `~/.acluster/providers.yaml` and a
sample `profile` file located in `~/.acluster/profiles.d/`.

An example of an `~/.acluster` directory with multiple clusters and
profiles is shown below:

```
    /home/user/.acluster
    ├── clusters.d
    │   ├── cluster1.yaml
    │   ├── cluster2.yaml
    │   ├── cluster3.yaml
    ├── profiles.d
    │   ├── profile1.yaml
    │   ├── profile2.yaml
    └── providers.yaml
```

The `profiles.d` directory contains information about cluster setups,
including the number and type of nodes, plugins, and other settings.

The `providers.yaml` file contains information about cloud providers.

The `clusters.d` directory contains information about clusters that are
currently running.

For more information about profile and provider settings, refer to the
following pages:
    * config-profile
    * config-provider
