Command line interface
======================

The Anaconda repository product from Continuum Analytics consists of a
number of components, that can be installed and used individually. This
page describes how to install and use them.

As a convention, all packages and commands which are part of the
Anaconda repository product, share the common 'cas' prefix, which is
short for Continuum Anaconda Server.

All packages are installed using the `conda` command, which is part of
the Miniconda installer. The packages only support 64-bit Linux. This is
how you install the 64-bit Miniconda:

    wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
    bash Miniconda-latest-Linux-x86_64.sh

> ...

You will need to reboot the terminal before you can use conda commands.
Ther conda file is a binary that resides in \~/miniconda2/bin and
"Prepending PATH=/root/miniconda2/bin to PATH in /root/.bashrc"
indicates that the directory has been added to the PATH variable in the
terminal. Every terminal has a PATH, which is the list of places it
looks for programs when you try to use a command such as conda.

Type:

    conda info

> ...

The info command displays useful system configuration information. In
order to install any of the packages below, you first need to add a
token protected channel to your `~/.condarc` file:

    conda config --add channels <token URL>

Once you purchase Anaconda repository you will receive the `<token URL>`
from us.

cas-mirror
----------

The mirror tool allows easily setting up a mirror of the Anaconda
repository within your organization. The following `conda` command
installs the mirror tool:

    conda install cas-mirror

Installing cas-mirror will make these commands available:

    cas-sync --help
    cas-server --help

The first command `cas-sync` is used to bring the local mirror of the
Anaconda repository up-to-date with our remote servers. To configure the
location of the mirror on your file system, check the output of:

    cas-sync --config

and, if necessary, create a configuration file (either `~/.cas-mirror`
or system-wise `/etc/cas-mirror`) which contains the desired location of
the local mirror on the filesystem, the platforms which should be
mirrored, as well as an optional blacklist of packages (the names of
packages which should not be mirrored, e.g. :

    mirror_dir: /home/data/mirror
    remote_url: ""  # where to get miniconda and anaconda installers -- blank to skip
    # possible platforms are: linux-64, linux-32, osx-64, win-32, win-64
    platforms:
      - linux-64
      - win-32
    blacklist:
      - dnspython
      - shapely
      - gdal

Once you are happy with the mirror directory (which may be the default),
you can run:

    cas-sync

Running this command for the first time will take many hours, because
the entire Anaconda repository is being downloaded. Subsequent runs will
take significantly less time. To serve the Anaconda repository over
HTTP, you can run:

    cas-server

The port on which the repository is being served may be changed using
the `--port` option. Note that you will need to run `cas-server` as root
when you intend to serve on port 80.

More extensive information about the cas-mirror tool's functionality and
configurable options is available
[here](mirrors-sync-configuration.html).

cas-installer
-------------

A token from Continuum is required to install cas-installer, and you
should have received it when your organization purchased Anaconda
Server, Workgroup or Enterprise. If you no longer have access to your
token, submit a support ticket or contact us at [priority
support](https://support.continuum.io/). You can also email support at
the email address given to you by your sales representative.

When you have the token, run:

    export TOKEN=<your Anaconda Cloud token>
    conda config --add channels /t/$TOKEN/anaconda-server

This tool allows you to create an installer for a conda environment. It
is important that the cas-installer package is installed into the "root"
conda environment (not "root" user). The following command ensures that
this happens:

    conda install -n root cas-installer=1.3.2

Once installed, the `cas-installer` command will be available:

    cas-installer -h

The command takes an installer specification file as its argument, which
specifies the name of the installer, the conda channel to pull packages
from, the conda packages included in the installer etc. Here is an
example:

    # ----------------- required -----------------
    # name
    name: test

    # channels to pull packages from
    # The &channels creates a backreference so that it can be reused as
    # *channels in the conda_default_channels section below.
    channels: &channels
      - http://repo.continuum.io/pkgs/free/

    # specifications
    specs:
      - python
      - grin

    # ----------------- optional -----------------
    # platform e.g. linux-32, osx-64, win-32 defaults to current platform
    #platform: linux-64

    # The conda default channels which are used when running a conda which
    # was installed be the cas-installer created (requires conda (3.6.2 or
    # greater) in the specifications). The *channels is a YAML reference to
    # &channels above.  It inserts all the channels from the channels key, so
    # that they do not have to be typed twice.
    conda_default_channels: *channels

    # installer filename
    #installer_filename: grin.sh

    # default install prefix
    default_prefix: /opt/anaconda

For Windows, the tool creates nsis-based `.exe` installers, which can
only be created on a Windows platform, although the architecture may be
different. For Unix, the tool creates bash-based `.sh` installer, which
can only be created on Unix (Linux, Mac OS X) systems.
