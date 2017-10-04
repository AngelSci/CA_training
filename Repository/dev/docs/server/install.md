Install/Uninstall Anaconda repository
=====================================

Installation assistance is included with your purchase of Anaconda
repository. If you have any questions during installation, please
contact your sales representative or [Priority Support
team](http://continuum.io/support).

Your server must meet the requirements for hardware, software, security,
and network. Please review and verify all your
Anaconda repository requirements &lt;requirements&gt; before beginning
your installation.

Install summary
---------------

1.  Install MongoDB 2.6
2.  Create the Anaconda repository administrator account
3.  Install Miniconda
4.  Use Miniconda to download and install Anaconda repository enterprise
    packages
5.  Configure Anaconda Repository
6.  Start and log on to Anaconda Repository
7.  Set up automatic restart on reboot, fail or error
8.  Client configuration
9.  Install Anaconda Repository license
10. (Optional) Mirror installers for Anaconda and Miniconda
11. (Optional) Adjust IPTables to accept requests on port 80
12. Mirror Anaconda Cloud

1. Install MongoDB 2.6
----------------------

In a terminal window, create the yum repo file as the root user:

    RPM_CDN="https://820451f3d8380952ce65-4cc6343b423784e82fd202bb87cf87cf.ssl.cf1.rackcdn.com"
    curl -O $RPM_CDN/nginx-1.6.2-1.el6.ngx.x86_64.rpm 
    curl -O $RPM_CDN/mongodb-org-tools-2.6.8-1.x86_64.rpm 
    curl -O $RPM_CDN/mongodb-org-shell-2.6.8-1.x86_64.rpm 
    curl -O $RPM_CDN/mongodb-org-server-2.6.8-1.x86_64.rpm 
    curl -O $RPM_CDN/mongodb-org-mongos-2.6.8-1.x86_64.rpm 
    curl -O $RPM_CDN/mongodb-org-2.6.8-1.x86_64.rpm

NOTE: Ubuntu users use apt-get instead of yum.

### MongoDB for Redhat and CentOS 6.7+

Install MongoDB:

    sudo yum install -y mongodb-org*

Start MongoDB:

    sudo service mongod start

Verify that MongoDB is running:

    sudo service mongod 
    Usage: /etc/init.d/mongod COMMAND

### MongoDB for Ubuntu 12.04+

Install MongoDB:

    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list

    sudo apt-get update

    sudo apt-get install -y mongodb-org=2.6.9 mongodb-org-server=2.6.9 mongodb-org-shell=2.6.9 mongodb-org-mongos=2.6.9 mongodb-org-tools=2.6.9

Start MongoDB:

    sudo service mongod start

You will receive verification that MongoDB is running:

    start: Job is already running: mongod

Note: If you don't specify a version like 2.6.9, apt-get will install
the latest stable version, which is 3.x.

### Additional MongoDB resources

For additional MongoDB installation information see
<https://docs.mongodb.org/manual/>

2. Create the Anaconda repository administrator account
-------------------------------------------------------

Anaconda repository was formerly known as Binstar. In a terminal window,
create a new user account for Anaconda repository named binstar, and
switch to this new account:

    sudo useradd -m binstar

The binstar user is the default for installing Anaconda repository. Any
username can be used.

NOTE: The use of the root user is discouraged.

Create the following three Anaconda repository directories:

Anaconda repository config directory:

    sudo mkdir -m 0770 /etc/binstar

Anaconda repository logging directory:

    sudo mkdir -m 0770 /var/log/anaconda-server

Anaconda repository package storage directory:

    sudo mkdir -m 0770 -p /opt/anaconda-server/package-storage

Asssign the binstar user ownership of these directories:

    sudo chown -R binstar:binstar /etc/binstar
    sudo chown -R binstar:binstar /var/log/anaconda-server
    sudo chown -R binstar:binstar /opt/anaconda-server/package-storage

Switch to the Anaconda repository administrator account:

    sudo su - binstar

3. Install Miniconda
--------------------

Miniconda gives us access to Python and the 'conda' command to install
Anaconda repository.

Download and install Miniconda, following the prompts in the
installation routine:

    curl 'http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh' > Miniconda.sh

Run the Miniconda.sh script:

    bash Miniconda.sh

Review and accept the license terms:

    Welcome to Miniconda 3.16.0 (by Continuum Analytics, Inc.)
    In order to continue the installation process, please review the license agreement.
    Please, press ENTER to continue. 

Once you have reviewed the license terms, approve them:

    Do you approve the license terms? [yes|no] yes

Accept the default location or specify an alternative:

    Miniconda will now be installed into this location:

> /home/binstar/miniconda2 -Press ENTER to confirm the location
>
> :   -Press CTRL-C to abort the installation -Or specify a different
>     location below \[/home/binstar/miniconda2\] &gt;&gt;&gt;" \[Press
>     ENTER\] PREFIX=/home/binstar/miniconda2 installing:
>     python-2.7.10-0 ... Python 2.7.10 :: Continuum Analytics, Inc.
>     creating default environment... installation finished.
>
At the end of the installation routine, update the binstar user's path
(prepending /home/binstar/miniconda2) by answering yes at the prompt to
add the install location to your path:

    Do you wish the installer to prepend the Miniconda install location to PATH in your /home/binstar/.bashrc ? [yes|no]

Type "yes" and press ENTER.

For the new path changes to take effect, exit and restart your terminal
session, or source your .bashrc, or start a new bash shell:

    source ~/.bashrc

OR:

    bash

Update conda:

    conda update conda

4. Download and install Anaconda repository enterprise packages
---------------------------------------------------------------

Now you can use conda to install the Anaconda repository Command Line
Interface (CLI) client, which is named anaconda-client.

First install anaconda-client, the CLI for Anaconda repository:

    conda install anaconda-client

Next install the Anaconda repository channel from Anaconda Cloud. Use
the "conda config" command to edit the binstar user's \~/.condarc file
to include the token-locked <https://anaconda.org> channel provided to
you by Continuum:

    export TOKEN="your Anaconda Cloud token"
    conda config --add channels https://conda.anaconda.org/t/$TOKEN/binstar/
    conda config --add channels https://conda.anaconda.org/t/$TOKEN/anaconda-server/

NOTE: If you have a subscription BUT do not have a license, contact
[support](http://continuum.io/support) to receive that license.
Otherwise contact [sales](https://www.continuum.io/contact-us) to
acquire it.

NOTE: Replace "your Anaconda Cloud token" with your Continuum support
token that you received from Continuum Support. This adds the correct
channels to conda by updating the /home/binstar/.condarc file.

Finally install the Anaconda repository Enterprise Package
binstar-server via conda:

    conda install binstar-server

5. Configure Anaconda repository
--------------------------------

Now initialize the web server, choose the package storage location, and
create the first user.

a.  Initialize the web server and indicate the filepath for the package
    storage location:

        anaconda-server-config --init
        anaconda-server-config --set fs_storage_root /opt/anaconda-server/package-storage

NOTE: The location for file storage can be any location owned by the
binstar user that you created in Step 4.

b.  If you are not using LDAP or Kerberos authentication, create an
    initial superuser account for Anaconda repository:

        anaconda-server-create-user --username "superuser" --password "yourpassword" --email "your@email.com" --superuser

NOTE: Replace "superuser" with a username of your choice, "yourpassword"
with a password of your choice, and <%22you@youremail.com>" with an
email address where you wish to receive system email notifications.

NOTE: To ensure the bash shell does not process any of the characters in
this password, limit the password to lower case letters, upper case
letters and numbers, with no punctuation. After setup the password can
be changed with the web interface.

c.  Initialize the Anaconda repository database:

        anaconda-server-db-setup --execute

NOTE: When upgrading Anaconda repository for each future version, you
will first install the new version, then run:

    anaconda-server-db-setup --execute

again, and then restart the server.

NOTE: More configuration options can be controlled with one or more
.yaml configuration files. Anaconda repository reads configuration files
from `/etc/anaconda-server/*.yaml`, then
`$PREFIX/etc/anaconda-server/*.yaml`, then from the path specified in
the environment variable `ANACONDA_SERVER_CONFIG` if it is set and the
command line argument `--config-file` was not used, then from the path
specified in the command line argument `--config-file` if it was used.
All configuration is merged, and options from files read earlier are
overwritten by files read later. If there are multiple files in the same
directory, they may be read in any order.

6. Start and log on to Anaconda server
--------------------------------------

Now you are ready to start Anaconda repository and then log on using
your browser.

a.  Start the new Anaconda repository on the Anaconda repository port:

        anaconda-server --port 8080

b.  Open your browser and log onto Anaconda repository by visiting
    <http://your.anaconda.server:8080/> using the superuser account you
    created in step 5 above.
c.  If you are using LDAP or Kerberos authentication, modify your user
    "jsmith" to be a superuser:

        anaconda-server-admin set-superuser "jsmith"

7. Set up automatic restart on reboot, fail or error
----------------------------------------------------

a.  Run the anaconda-server-install-supervisord-config.sh script to
    configure supervisord management of the Anaconda server and worker
    processes:

        anaconda-server-install-supervisord-config.sh

b.  Then create the following entry in the binstar user’s crontab:

        @reboot /home/binstar/miniconda2/bin/supervisord

This will generate the /home/binstar/miniconda2/etc/supervisord.conf
file.

c.  Verify that the server is running with:

        supervisorctl status

If installed correctly, you see:

    binstar-server RUNNING   pid 10831, uptime 0:00:05
    binstar-worker RUNNING   pid 2784, uptime 1:45:56

8. Client configuration
-----------------------

Follow the configuration instructions so you can use one or more clients
to communicate with the server.

9. Install Anaconda Repository License file
-------------------------------------------

In your browser, go to <http://your.anaconda.server:8080>. Follow the
onscreen instructions to upload the license file that you received in an
email from your sales representative.

Contact your sales representative or support representative if you
cannot find or have any questions about your license.

After uploading the license file, you will see the login page. Log in
using the superuser user and password that you created in Step 5 above.

TIP: You can view the current license information and upload a new
license file by visiting the URL
<http://your.anaconda.server:8080/admin/license>.

Alternate license install: Copy the license file directly into the
/home/binstar/.continuum directory.

10. (Optional) Mirror installers for Anaconda and Miniconda
-----------------------------------------------------------

Miniconda and Anaconda installers can be served by Anaconda repository
via the static directory located at
/home/binstar/miniconda2/lib/python2.7/site-packages/binstar/static/extras.
This is required for Anaconda Cluster integration. To serve up the
latest Miniconda installers for each platform, download them and copy
them to the extras directory:

    # miniconda installers
    mkdir -p /tmp/extras
    pushd /tmp/extras
    URL="https://repo.continuum.io/miniconda/"
    versions="Miniconda3-latest-Linux-x86_64.sh Miniconda3-latest-MacOSX-x86_64.sh Miniconda3-latest-Windows-x86.exe Miniconda3-latest-Windows-x86_64.exe Miniconda-latest-Linux-x86_64.sh Miniconda-latest-MacOSX-x86_64.sh Miniconda-latest-Windows-x86.exe Miniconda-latest-Windows-x86_64.exe
    "
    for installer in $versions
    do 
        curl -O $URL$installer
    done

    # anaconda installers
    URL="https://repo.continuum.io/archive/"
    versions="Anaconda3-2.4.1-Linux-x86_64.sh Anaconda3-2.4.1-MacOSX-x86_64.pkg Anaconda3-2.4.1-MacOSX-x86_64.sh Anaconda3-2.4.1-Windows-x86.exe Anaconda3-2.4.1-Windows-x86_64.exe Anaconda2-2.4.1-Linux-x86_64.sh Anaconda2-2.4.1-MacOSX-x86_64.pkg Anaconda2-2.4.1-MacOSX-x86_64.sh Anaconda2-2.4.1-Windows-x86.exe Anaconda2-2.4.1-Windows-x86_64.exe"
    for installer in $versions
    do 
        curl -O $URL$installer
    done

    # Move installers into static directory
    popd
    cp -a /tmp/extras /home/binstar/miniconda2/lib/python2.7/site-packages/binstar/static

Users can download the installers by using curl:

    # Fill in server name, port, and specific installer for your platform
    curl -s -O http://<your server>:8080/static/extras/Miniconda-latest-Linux-x86_64.sh

11. (Optional) Adjust IPTables to accept requests on port 80
------------------------------------------------------------

Enable clients to access an Anaconda repository on standard ports by
configuring the server to redirect traffic received on standard HTTP
port 80 to the standard Anaconda repository HTTP port 8080.

NOTE: These commands assume the default state of IPTables which is "on"
and allowing inbound SSH access on port 22. This is the factory default
state for CentOS 6.7. If this default has been changed you can reset it
as follows:

    sudo iptables -L 

CAUTION: Mistakes with IPTables rules can render a remote machine
inaccessible.

a.  Allow inbound access to tcp port 80:

        sudo iptables -I INPUT -i eth0 -p tcp --dport 80 -m comment --comment "# Anaconda Server #" -j ACCEPT

b.  Allow inbound access to tcp port 8080:

        sudo iptables -I INPUT -i eth0 -p tcp --dport 8080 -m comment --comment "# Anaconda Server #" -j ACCEPT

c.  Redirect inbound requests to port 80 to port 8080:

        sudo iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -m comment --comment "# Anaconda Server #" -j REDIRECT --to-port 8080

d.  Display the current iptables rules:

        iptables -L -n
        Chain INPUT (policy ACCEPT)
        target     prot opt source               destination         
        ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:8080 /* # Anaconda Server # */ 
        ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:80 /* # Anaconda Server # */ 
        ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED 
        ACCEPT     icmp --  0.0.0.0/0            0.0.0.0/0           
        ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           
        ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           state NEW tcp dpt:22 
        REJECT     all  --  0.0.0.0/0            0.0.0.0/0           reject-with icmp-host-prohibited 

        Chain FORWARD (policy ACCEPT)
        target     prot opt source               destination         
        REJECT     all  --  0.0.0.0/0            0.0.0.0/0           reject-with icmp-host-prohibited 

        Chain OUTPUT (policy ACCEPT)
        target     prot opt source               destination  

NOTE: the PREROUTING (nat) IPTables chain is not displayed by default.
To show it, use:

    iptables -L -n -t nat
    Chain PREROUTING (policy ACCEPT)
    target     prot opt source               destination         
    REDIRECT   tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpt:80 /* # Anaconda Server # */ redir ports 8080 

    Chain POSTROUTING (policy ACCEPT)
    target     prot opt source               destination         

    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination       

e.  Save the running iptables configuration to /etc/sysconfig/iptables:

        sudo service iptables save

12. Mirror Anaconda Cloud
-------------------------

Packages can be mirrored from Anaconda Cloud to the local Anaconda
repository via one of two methods: direct download, or via USB drive
provided by Continuum Analytics. This document describes the direct
download method. Separate instructions are included with a USB drive.

Install the CAS-Mirror package, which is required to create the mirror:

    conda install cas-mirror

Mirror the Anaconda Cloud repository:

    anaconda-server-sync-conda

This command will mirror the anaconda.org repository to the
/opt/anaconda-server/package-storage directory.

NOTE: Due to the size of the Anaconda Cloud repo and depending on the
available Internet bandwidth, the mirror process can take hours.

Uninstall Anaconda repository
-----------------------------

To delete Anaconda repository, do the following:

1.  Check the file storage path by running the following command:

        anaconda-server-config --get fs_storage_root

2.  Delete the appropriate MongoDB database.
3.  Delete the contents of /etc/binstar.
4.  Delete the contents of the Anaconda repository file storage path.
5.  Remove the following conda packages:

-   binstar-server
-   cas-mirror
-   cas-installer

You may want to make a backup for security reasons. Refer to this site
for suggestions on mongo backups:
<https://docs.mongodb.org/manual/reference/program/mongodump/>

For additional help
-------------------

Your organization receives [priority
support](http://continuum.io/support) with your purchase of Anaconda
repository. Please email support at the email address given to you by
your sales representative.

Advanced topics
---------------

Did you find what you needed on this page?
------------------------------------------

Please [let us
know](https://github.com/Anaconda-Platform/support/issues).
