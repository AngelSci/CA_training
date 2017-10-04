Mirroring a PyPI repository
===========================

Before you begin
----------------

You need to have already completed [installing and configuring your
Anaconda Server instance](install.html). Due to the size of the Anaconda
repository, it is important that you have configured a file storage
location with sufficient disk space. If necessary please see the
[instructions for setting the file storage
location](install.html#configure-the-server).

The full PyPI mirror requires approximately 120GB.

The mirror command
------------------

To create a PyPI mirror run:

    binstar-sync-pypi

This will load all of the packages on pypi.python.org into the \~pypi
binstar user account.

Verify that this is working by opening your browser to
<http://your.anaconda.server/pypi/~pypi>

Alternately, you may not wish to mirror all packages. To mirror a subset
of the total repository, specify which platforms you want to include, or
use the whitelist, blacklist or license\_blacklist functionality to
control which packages are mirrored:

> binstar-sync-pypi --mirror-config /etc/binstar/mirrors/pypi.yaml

If necessary, refer to more information on [whitelist, blacklist and
license\_blacklist functionality](mirrors-sync-configuration.html).

Configure pip
-------------

To configure pip to use this new mirror you must edit your
\~/.pip/pip.conf file:

    [global]
    index-url = http://your.anaconda.server:<port>/pypi/~pypi/simple
