Maintenance and configuration concerns
======================================

Run Anaconda repository on an alternate port
--------------------------------------------

To run Anaconda repository on a port other than the standard port 8080,
modify the usual instructions by adjusting the port numbers in your
iptables configuration&lt;troubleshoot&gt; and specifying the correct
port in your supervisord.conf file.

Recommended general maintenance
-------------------------------

To maintain an Anaconda repository installation, perform all of these
tasks regularly:

-   Review the error logs
-   Back up the file system
-   Back up the database
-   Update the anaconda-server package with the
    `conda update anaconda-server` command

