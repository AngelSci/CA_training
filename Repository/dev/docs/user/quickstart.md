Quickstart
==========

[ ](#FindDownloadAndInstallPackages)

Find, download and install packages
-----------------------------------

[ ](#SearchForAPublicPackage)

### Search for a public package

[Anaconda Cloud](http://www.anaconda.org) hosts hundreds of useful
Python packages for a wide variety of applications. You don't need an
Anaconda Cloud account, or to be logged in, to search for public
packages, download and install them. You need an account only to access
[private packages](using.html#PrivatePackages) without a
[token](using.html#Tokens), or to build and share your packages with
others.

1.  In the top search box, type part or all of the name of a program you
    are searching for and press Enter.
2.  Packages that match your search string are displayed. Click the
    package name to see more information.

[ ](#RefineYourSearchResults)

### Refine your search results

You can filter search results using three filter controls:

-   All packages, conda only or PyPI only
-   All types, Public and/or Private (only available if you are
    logged in)
-   Platforms: All, Source, Linux-32, Linux-64, Noarch, OSX-64,
    Win-32, Win-64.

"Source" packages are source code only, not yet built for any specific
platform.

"Noarch" packages are built to work on all platforms.

[ ](#DownloadAndInstallAPackageFromAnacondaCloud)

### Download and install a package from Anaconda Cloud

After you have located a package and clicked on the name, the detail
page displays specific install instructions for the current operating
system. Copy and paste the full command into your terminal window.

NOTE: For the following examples to work, you need to have
[conda](http://conda.pydata.org/docs/download.html) downloaded and
installed.

EXAMPLE: To download and install a package with conda, run:

    conda install -c username packagename

Conda expands "username" to a URL such as
"<https://anaconda.org/username>" based on the settings in the .condarc
file. Anaconda Cloud users can use the defaults, and Anaconda Enterprise
repository users can [configure the
repository](https://docs.continuum.io/anaconda-repository/configuration)
or [configure
conda](http://conda.pydata.org/docs/config.html#set-a-channel-alias-channel-alias)
to use their local installation.

[ ](#BuildAndUploadPackages)

Build and upload packages
-------------------------

Open an Anaconda Cloud account to upload packages, to access private
packages without a token and/or to build packages for operating systems
other than the one you are using. To build private packages, upgrade to
a paid account.

To build and upload packages, install the Anaconda Client command line
interface (CLI) and Anaconda Build. Open a Terminal window and enter:

    conda install anaconda-client anaconda-build

Next, log into your Anaconda Cloud account. In your terminal window,
enter the following:

    anaconda login

At the prompt, enter your Anaconda Cloud username and password.

Next, choose the package you would like to build. For this quickstart,
you can download our test package:

    git clone https://github.com/Anaconda-Server/anaconda-client
    cd anaconda-client/example-packages/conda/

To build your test package, first install conda-build and turn off
automatic anaconda-client uploading, then run the conda build command:

    conda install conda-build
    conda config --set anaconda_upload no
    conda build .

Check your path to where the newly built file was placed so you can use
it in the next step:

    conda build . --output

Finally, log into your Anaconda Cloud account if you haven't already,
and upload your newly built test package to your Anaconda Cloud account:

    anaconda login
    anaconda upload /your/path/conda-package.tar.bz2

For detailed information, see the [Conda
packages](using.html#CondaPackages) section.

[ ](#ShareNotebooks)

Share notebooks
---------------

Upload a [Jupyter notebook](http://jupyter.org/) (formerly IPython
notebook) to Anaconda Cloud:

    anaconda upload my-notebook.ipynb

An HTML version of the notebook will be at:

    http://notebooks.anaconda.org/<USERNAME>/my-notebook

Anyone can download it:

    anaconda download username/my-notebook

[ ](#ShareEnvironments)

Share environments
------------------

Save a [conda environment](http://conda.pydata.org/docs/using/envs.html)
and upload it to Anaconda Cloud:

    conda env export -n my-environment -f my-environment.yml
    conda env upload -f my-environment.yml

A list of your uploaded environments is at:

    http://envs.anaconda.org/<USERNAME>

Anyone can download and install your environment from Anaconda Cloud:

    conda env create user/my-environment
    source activate my-environment
