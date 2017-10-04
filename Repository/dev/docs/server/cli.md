Anaconda repository command line interface
==========================================

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

The info command displays useful system configuration information. In
order to install any of the packages below, you first need to add a
token protected channel to your `~/.condarc` file:

    conda config --add channels https://conda.binstar.org/t/<TOKEN>/anaconda-server/

Once you purchase Anaconda repository you will receive the `<TOKEN>`
from us.
