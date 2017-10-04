Anaconda repository requirements and verification
=================================================

Hardware requirements
---------------------

-   Physical server or virtual machine
-   CPU: 2 x 64-bit 2 2.8GHz 8.00GT/s CPUs or better.
    Verify architecture&lt;directive-1&gt;
-   Memory: minimum RAM size of 32GB (or 16GB RAM with 1600 MHz
    DDR3 installed) and minimum of 2 2.8GHz 8.00GT/s CPUs for a typical
    installation with 50 regular users. Verify memory&lt;directive-6&gt;
-   Storage: Recommended minimum of 100GB, or 300GB if you are planning
    to mirror both the Anaconda repository (approx. 90GB) and/or the
    PyPI repository (approx. 100GB), or at least 1TB for an air gapped
    environment; additional space is recommended if the repository will
    be used to store packages built by the customer.
    Verify storage&lt;directive-2&gt;
-   Internet access to download the files from Anaconda Cloud or a USB
    drive containing all of the files you need with alternate
    instructions for air gapped installations.

Software requirements
---------------------

-   Linux environment (installations have been tested on Redhat, CentOS
    6.7, and Ubuntu 12.04+). Verify Linux version&lt;directive-7&gt;
-   Client environment may be Linux, Windows, or OS X
-   Ubuntu users may need to install cURL.
    Verify cURL access&lt;directive-3&gt;
-   MongoDB version 2.6+ installed as root and running.
    Verify MongoDB installation&lt;directive-4&gt;

Security requirements
---------------------

-   Root access or sudo capabilities.
    Verify root access and sudo privileges&lt;directive-5&gt;
-   Ability to make (optional) iptables modifications
-   SELinux policy edit privileges. (note that SELinux does not have to
    be disabled for Anaconda repository operation)

Network requirements (TCP ports)
--------------------------------

-   Inbound TCP 8080 (Anaconda repository)
-   Inbound TCP 22 (SSH)
-   Outbound TCP 443 (Anaconda Cloud)
-   Outbound TCP 25 (SMTP)
-   Outbound TCP 389/636 (LDAP(s))
-   Your [Anaconda.org](https://anaconda.org/) (Anaconda repository in
    the cloud) account username, password and installation token
    provided to you by Continuum at the time of purchase. If you did not
    receive your token, please contact your sales representative
    or Priority Support team &lt;http://continuum.io/support&gt;.

Hardware verification
---------------------

### Machine architecture

Anaconda repository is built to operate only on 64-bit computers. To
verify that you have a 64-bit or x86\_64 computer, in your terminal
window print the machine architecture with this command:

    arch

This command prints to the screen whether your system is 32-bit ("i686")
or 64-bit ("x86\_64").

### Memory requirements

You need a minimum RAM size of 32GB (or 16GB RAM with 1600 MHz DDR3
istalled).

On the command line type:

    free -m

This will return the free memory size in MB.

### Storage requirements: minimum hard drive or virtual environment size

Check your available disk space with the built-in Linux utility df, with
the -h parameter for human readable format:

    df -h

Software verification
---------------------

### Other versions of the Linux environment

Please [contact us by filing a GitHub
issue](https://github.com/Anaconda-Platform/support/issues) if you have
problems with a version other than Redhat, CentOS, or Ubuntu. Prompts
may vary slightly depending on your version.

### cURL access for Ubuntu users

RedHat Linux and CentOS have cURL pre-installed, but Ubuntu does not.

Verify cURL access in your terminal window:

    curl --version

If cURL is not found, Ubuntu users can use the Advanced Packaging Tool
(APT) to get and install cURL:

    sudo apt-get install curl

TIP: If you already have Miniconda or Anaconda installed, in all
versions of Linux you can use the conda command:

    conda install curl

### MongoDB version 2.4+ installed as root and running

MongoDB version 2.4 or higher is required. Check for existence of
MongoDB and its version number:

    mongod --version

If you get a "not found" message or if the MongoDB version is 2.3 or
earlier, then install MongoDB 2.4 or higher using the [official
installation
instructions](http://docs.mongodb.org/manual/administration/install-on-linux/).
Remember to install as root with the sudo command.

MongoDB must always be running before Anaconda repository can be
started. Start MongoDB:

    sudo service mongod start

Verify that MongoDB is running:

    mongo --eval 'db.serverStatus().ok'

Security verification
---------------------

### Root access and sudo privileges

The Anaconda repository installation process cannot be completed without
root access. Test to verify that you have sudo privileges:

    sudo -v

Enter your root password when prompted and click ENTER.

If you receive a message like the following, contact your system
administrator for root access:

    Sorry, user [username] may not run sudo on [hostname].

Did you find what you needed on this page?
------------------------------------------

Please [let us
know](https://github.com/Anaconda-Platform/support/issues).
