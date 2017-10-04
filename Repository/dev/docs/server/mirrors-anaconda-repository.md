Mirroring an Anaconda repository
================================

Before you begin
----------------

You need to have already completed [installing and configuring your
Anaconda Server instance](install.html). Due to the size of the Anaconda
repository, it is important that you have configured a file storage
location with sufficient disk space. If necessary please see the
[instructions for setting the file storage
location](install.html#configure-the-server).

The full Anaconda mirror requires approximately 90GB.

The mirror command
------------------

You can mirror some or all of the contents of the [Anaconda
repository](http://docs.continuum.io/anaconda/pkg-docs.html) using the
anaconda-server-sync-conda command:

    anaconda-server-sync-conda

This will mirror all of the packages from the Anaconda repository into
the anaconda binstar user account.

Verify that this is working by opening your browser to
<http://>&lt;anaconda.server.addr&gt;/anaconda/

Alternately, you may not wish to mirror all packages. To mirror a subset
of the total repository, specify which platforms you want to include, or
use the whitelist, blacklist or license\_blacklist functionality to
control which packages are mirrored:

    anaconda-server-sync-conda --mirror-config /etc/binstar/mirrors/conda.yaml

If necessary, refer to more information on [whitelist, blacklist and
license\_blacklist functionality](mirrors-sync-configuration.html).

### In an air-gapped environment:

To mirror the Anaconda repository in an air-gapped environment, using a
system with no internet access, you create a local copy of the Anaconda
repository using a USB drive provided by Continuum, and point
anaconda-server-sync-conda to the extracted tarball.

First, mount the USB drive and extract the tarball. In this example we
will extract to \`/tmp\`:

    $ cd /tmp
    $ tar xvf <path to>/mirror.tar

Now you have a local Anaconda repository located at /tmp/mirror/pkgs.
This repository can be mirrored. Edit /etc/binstar/mirrors/conda.yaml to
contain:

    channels:
      - /tmp/mirror/pkgs

And then run the above command:

    $ anaconda-server-sync-conda --mirror-config /etc/binstar/mirrors/conda.yaml

This will mirror the contents of the local Anaconda repository to your
Anaconda Server installation under the username 'anaconda.'

Configure conda
---------------

Having created the mirror, you will still need to configure conda to
search for packages here rather than on the default Anaconda repository.
You can do that by editing your \~/.condarc file to add the appropriate
channel:

    channels:
        - http://<anaconda.server.ipaddress>:<port>/conda/anaconda/

NOTE: This configuration change can be made at the user level or via an
[administrative](http://conda.pydata.org/docs/admin.html) conda file, to
force all internal users to use your local Anaconda mirror rather than
querying the Anaconda repository.
