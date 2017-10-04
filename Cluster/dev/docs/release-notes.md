Release notes
=============

Below is a summary of features, bug fixes, and improvements for each
Anaconda for cluster management release.

**Anaconda for cluster management 1.4.1**

Features:

-   Renamed `distributed` plugin to `dask`
-   Enabled `notebook` and `dask` plugins to be installed alongside
    existing Hadoop installations
-   Added `conda` profile plugin setting for `ssl_verify`

**Anaconda for cluster management 1.4.0**

Features:

-   Added setting for `channel_alias` for improved integration with
    Anaconda Repository

Bug Fixes:

-   Fixed provisioning on Windows client machines
-   Fixed issue with profile setting for `conda` access control lists
-   Fixed issue with certain plugin status checks
-   Fixed issue with Storm plugin installation

Backend improvements:

-   Improved management and configurability of `distributed` plugin
-   Updated version of Apache Libcloud dependency (0.20.1)
-   Updated to accept new license format (backwards compatible with
    existing licenses)
-   Removed deprecated `acluster submit` command due to inconsistencies
    with environments
-   Removed `acluster defaultenv` and `acluster setenv` commands due to
    inconsistencies with environments
-   Consolidated sample profile to a single profile

**Anaconda for cluster management 1.3.3**

Bug Fixes:

-   Fixed SSH private key permissions check

Backend improvements:

-   Implemented Salt ACL functionality
-   Implemented Salt PAM authentication
-   Removed sudo requirement after install

**Anaconda for cluster management 1.3.2**

Bug Fixes:

-   Fixed installation prefix and default channel documentation and
    tests

Backend improvements:

-   Improved detection of plugin installations and plugin status
    messages

**Anaconda for cluster management 1.3.1**

Features:

-   Updated plugin: Spark 1.6
-   Added option to disable creation of `/etc/profile.d/conda.sh` on
    cluster nodes

Bug Fixes:

-   Fixed R path for Jupyter Notebook
-   Fixed issue with Amazon EC2 block device mapping
-   Fixed issue with configuration of default conda channels
-   Improved warnings for misconfigured SSH keys
-   Improved error message when AWS Key Pair is missing

Backend improvements:

-   Added configurable download URLs for plugins (used for airgap
    installations): Elasticsearch, Logstash, Kibana, Storm
-   Added deprecated warning for `acluster submit` command due to
    inconsistencies with environments
-   Added detection for enterprise Hadoop installations and warns before
    installing conflicting services
-   Configured HDFS for short-circuit reads by default
-   Pinned versions of dependencies in conda recipe

**Anaconda for cluster management 1.3.0**

Features:

-   Simplified bare-metal cluster setup using profile/provider instead
    of clusters.d
-   Added ability to specify conda packages and environments in profile
    plugin settings
-   Switched to system-wide .condarc file for users on cluster nodes
-   Added centralized logging via Elasticsearch, Logstash, and Kibana
    plugins
-   Added `--no-browser` option for `acluster open` command
-   Added license information to `acluster info`
-   Removed optional `security_group` setting from `providers.yaml`
    template and documentation
-   Added `vpc_id` setting for Amazon EC2 to use with default security
    group
-   Improved documentation for bare-metal and cloud-based cluster
    creation
-   Added more information about requirements, FAQs, and known issues to
    documentation

Bug Fixes:

-   Improved error messages for cloud providers, security groups, and
    when no clusters are defined
-   Fixed error when command output contained Unicode characters
-   Fixed repeated prompts when installing multiple plugins

Backend improvements:

-   Added test for SSH connectivity during bare-metal cluster creation
-   Added detection/removal of orphaned clusters upon `acluster destroy`
-   Added detection/installation of missing sudo/bzip2 packages upon
    cluster creation

**Anaconda for cluster management 1.2.2**

Features:

-   Moved bare metal cluster setup to profile and provider files
-   Ability to specify private IPs for VPC clusters on Amazon EC2

**Anaconda for cluster management 1.2.1**

Features:

-   Updated plugin: Spark 1.5.1
-   Consistent output when listing clusters and profiles
-   New blog post and updated documentation

Bug Fixes:

-   Removed duplicate error messages
-   Fixed notebook plugin formulas

**Anaconda for cluster management 1.2.0**

Features:

-   Dedicated salt/supervisor environments
-   New cluster profile (no nesting)
-   Documentation updates
-   Improvements to CLI output

Bug Fixes:

-   Storm plugin
-   Notebook plugin
-   Logstash plugin
-   Kibana plugin
-   Elasticsearch plugin
-   Windows Fixes: push/submit

Backend improvements:

-   Refactor status/stop/restart and plugin loading
-   Refactor connection object
-   Multiple backends (initial work)

**Anaconda for cluster management 1.1.0**

-   Improved Jenkins testing
-   Added Storm plugin
-   Added Elasticsearch/Logstash/Kibana plugins (ELK stack)
-   Added Dask plugin
-   Fixes for single-node installations
-   Profile updates
-   Add setting for AWS Tags
-   Added security options (SELinux/iptables)
-   Added setting for notebook password

**Anaconda for cluster management 1.0.0**

-   CLI rewrite
-   Aggregated and improved CLI messaging
-   Backend library refactoring
-   Salt-packaging refactoring
-   Easier bare-metal installation
-   Added option for streaming output
-   Fixed issue with Ganglia on Ubuntu
-   Windows/libcloud Compatibility
-   Added licensing with new CLI
-   Conda remote fixes
-   Install Anaconda/Miniconda from custom url

