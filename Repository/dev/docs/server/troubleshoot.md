Troubleshooting your Anaconda repository installation
=====================================================

I Cannot connect to the server on port x
----------------------------------------

This could be because you are behind a firewall. Check if your iptables
rules are blocking your ports:

    iptables -L -n

If a rule blocks a port you want to use then you must allow the port:

    sudo iptables -t nat -F
    sudo iptables -A INPUT -p tcp -m tcp --dport <PORT> -j ACCEPT
    sudo service iptables save
    sudo service iptables restart

"No environment named "search" exists in C:\\Anaconda\\envs" when using "anaconda search" on Windows
----------------------------------------------------------------------------------------------------

If anaconda-client is not yet installed and you try to search for a
package on anaconda.org using the 'anaconda' command you may receive the
following error message:

    C:\Users\username>anaconda search -t conda packagename
    No environment named "search" exists in C:\Anaconda\envs

This error occurs because the Windows version of Anaconda contains an
anaconda.bat file, that is used for setting environment paths and
switching environments, and if anaconda-client is not installed this
batch file is called instead. Once you install anaconda-client the
anaconda search command should work again:

    conda install anaconda-client
    anaconda search -t conda packagename
