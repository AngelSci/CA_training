Anaconda repository FAQ
=======================

How do I run Anaconda repository in an air gapped environment?
--------------------------------------------------------------

For your purchase of Anaconda Workgroup or Enterprise, Continuum can
provide either a USB flash drive or a link to a downloadable archive of
both the Anaconda repository software and a current copy of the entire
Anaconda package repository. After this archive has been transferred to
the target server on your protected network you will be able to install
the repository and load the packages into its configuration. Future
updates to the software and package repository can also be provided via
USB flash drive or download.

To get your USB flash drive or download link, submit a support ticket or
contact us at [priority support](https://support.continuum.io/). You can
also email support at the email address provided to you by your sales
representative.

How do I host/serve custom channels in addition to cas-mirror?
--------------------------------------------------------------

After you successfully mirror the Anaconda repository you will see that
the synced directory contains the following directory:

    /pkgs/linux-64

NOTE: You will see an additional subdirectory for each platform that you
included when editing your .cas-mirror file.

To add your own internal packages, add a new directory with a unique
name at the same directory level as the Anaconda repository pkgs
directory, with subdirectories for the platforms you want to support.

A sample directory structure can look like the following:

    /<mirror-directory>/pkgs/linux-64
    /<mirror-directory>/internal-pkgs/linux-64

After you create this directory or directories, upload your conda
package(s) to the appropriate subplatform directory of your
/&lt;mirror-directory&gt;/internal-pkgs/ directory.

Every time you add or update a package in your internal-pkgs directory,
you must run the conda index command on the directory. This will reindex
its contents:

    conda index /<mirror-directory>/internal-pkgs/linux-64

Finally, your users must configure this directory as an available conda
channel, just as you configured your default Anaconda repository
directories:

    conda config --add channels http://<mirror-directory.url>:8080/pkgs
    conda config --add channels http://<mirror-directory.url>:8080/internal-pkgs

How do I mirror and serve PyPI alongside the cas-mirror?
--------------------------------------------------------

The Anaconda repository includes functionality for [mirroring and
serving the PyPI repository](mirrors-pypi-repository.html) as part of
your installation.

How do I specify the order in which internal users check private channels, cas-mirror or the external Anaconda repo for package installation?
---------------------------------------------------------------------------------------------------------------------------------------------

Open the .condarc file and edit the order of the channels listed there
to indicate the order in which those channels should be used.

Open the \~/.condarc file in an editor:

    vim ~/.condarc

Change the order of your channels to change the search order:

    channels:
      - private-channel
      - http://<mirror-directory.url>:8080
      - https://conda.anaconda.org/t/<token>/<channel2>
      - http://conda.anaconda.org/<channel1>
      - defaults

The order of search is now:

1.  private-channel
2.  mirror-directory (local)
3.  private binstar channel2
4.  public binstar channel1
5.  default channels

When you are satisfied with the order of channel searching, save and
exit your editor.

Can I add a rule to \~/.condarc to make conda use a proxy for PyPI but not for our channels?
--------------------------------------------------------------------------------------------

If you are converting PyPI packages to conda packages and want to use a
proxy while doing so, you can add the following to your conda skeleton
command:

    HTTPS_PROXY=yourproxy conda skeleton pypi ...

How do I whitelist or blacklist certain packages?
-------------------------------------------------

Sometimes you do not want to replicate all the packages from the
Anaconda repository into your mirror. The cas-mirror tool includes
whitelist/blacklist functionality to manipulate your list of mirrored
packages in a variety of ways.

This is available through one of two configuration files:

a)  /etc/cas-mirror (as system configuration available to all users who
    have appropriate permissions, likely 0644)
b)  \~/.cas-mirror (for per user configuration)

When both files exist, the user \~/.cas-mirror file takes precedence
over the /etc/cas-mirror file.

From your local anaconda directory you can check current mirror settings
as follows:

    cd cas-mirror/
    ./cas-sync --show

If no configuration files are found, then the presented results are the
default settings of the script itself.

To customize your distribution, you have the following options:

-   **remote\_url** (the URL address to use as the source for the
    mirroring process)
-   **mirror\_dir** (the directory on the machine where the script is
    executed and where packages will be stored)
-   **platforms** (indicates what kind of platforms packages will
    be mirrored)
-   **license\_blacklist** (specifies what packages under listed here
    licenses that will be omitted)
-   **blacklist** (specifies the exact packages that will be omitted)
-   **whitelist** (specifies the exact packages that will always
    be mirrored)

NOTE: Configuration files are yaml files.

A fully working example can look like this (assuming \~/.cas-mirror in
your home directory):

    mirror_dir: /home/cas-mirror
    platforms:
      - linux-32
      - linux-64
    license_blacklist: GPL
    whitelist:
      - distribute
      - conda
    blacklist:
      - flask
      - readline

The cas-sync tool mirrors the default remote\_url (currently:
<http://repo.continuum.io>) in the /home/cas-mirror directory of the
machine where the cas-sync command is executed.

It only selects packages that are available for linux-32 and linux-64
platforms (for example, win-32 or win-64 packages will not be mirrored
at all).

From the ultimate list of packages that are mirrored, the tool:

-   Removes all packages that are under the GPL license so that every
    license except GPL is allowed
-   Removes any packages that are explicitly mentioned in the
    'blacklist' option, regardless of the platform or license-type
-   Adds packages explicitly mentioned in the 'whitelist' option to the
    list of packages that are mirrored

NOTE: Currently GPL licenses are the only license type that can be
license\_blacklisted.

NOTE: The whitelist option overrides license\_blacklist and blacklist,
so that a package listed here is mirrored even when under a GPL license
or if it appears in the 'blacklist' option.

REMEMBER: You do not *need* to set up each option manually. If you only
want to adjust one or two options, that is allowed. Untouched options
remain defined by the default setting.

The step-by-step algorithm that is used by the cas-mirror to create the
ultimate list of packages to mirror follows this procedure:

1.  Get a full list of packages from default\_url
2.  If the platforms option is present, only those packages available to
    the platforms listed here are left on the list
3.  If license\_blacklist is present, then all the packages subject to
    any of the licenses mentioned here are removed from the list
4.  If blacklist is present then all member packages explicitly
    mentioned here are removed from the list
5.  If whitelist is present then those assigned member packages are
    added to the list

After performing all of the above actions sequentially, the script
produces the ultimate list of packages that are mirrored in the next
step.

How do I build custom conda packages?
-------------------------------------

Because Anaconda repository relies on conda, any packages you want
served internally via the Anaconda repository must be built as conda
packages. If you are unfamiliar with the conda build process, please see
our [step-by-step
documentation](http://conda.pydata.org/docs/building/bpp.html).

How do I serve custom conda packages?
-------------------------------------

After you have created a custom conda package, you can serve it through
your cas-mirror as follows:

1.  Create a new directory (channel) inside your
    &lt;mirror-directory&gt; directory (example: our-pkgs)
2.  Create the corresponding platform sub-directories (example:linux-64)
    within that directory
3.  Copy the conda package(s) you built to the mirrored directory, in
    this case &lt;mirror-directory&gt;/our-pkgs/linux-64
4.  Run "conda index" within that directory
5.  Add the new channel to the condarc file for the machine that is
    designated to download the new packages, in this case &lt;internal
    IP&gt;/our-pkgs

Can I run a conda index while the cas-server is running?
--------------------------------------------------------

You can issue the conda index command while the cas-server is running.

How do I build cas-installer?
-----------------------------

Please see the [instructions for building the
cas-installer](cli-cas-installer.html#cas-installer).

You must first get a token from Continuum.

To get your token, submit a support ticket or contact us at [priority
support](https://support.continuum.io/). You can also email support at
the email address given to you by your sales representative.

After you have the token, run:

    export TOKEN=<your Anaconda Cloud token>
    conda config --add channels /t/$TOKEN/anaconda-server

To install the conda cas-installer tool run:

    conda install -n root cas-installer=1.3.2

Now you can build your own installers. Try making ‘my-installer.yaml’ as
follows, specifying that only python and conda are installed:

    name: my-installer
    version: 1.0
    channels: [ http://repo.continuum.io/pkgs/free/ ]
    specs: [python, conda]

Now run:

    cas-installer my-installer.yaml

This creates the file ‘my-installer-1.0-linux-64.sh’ that you can
distribute to others, who can then use it to install python and conda.
To add a license file to your installer, add the key ‘license\_file’ to
‘my-installer.yaml’:

    name: my-installer
    version: 1.0
    channels: [ http://repo.continuum.io/pkgs/free/ ]
    specs: [python, conda]
    license_file: my-license.txt

Finally, specify your own packages and/or channels:

    name: my-installer
    version: 1.0
    channels: [ http://repo.continuum.io/pkgs/free/, http://<mirror-directory.url>:8080 ]
    specs: [python, conda, my_package]

How do I stop timeouts when running cas-sync?
---------------------------------------------

Restart cas-sync. If this does not fix the issue, please contact
[priority support](https://support.continuum.io/).

How do I stop timeouts when uploading large files?
--------------------------------------------------

Increase the timeout threshold by opening the Anaconda repository
configuration file /etc/binstar/config.yaml and adding the following
configuration:

    gunicorn:
        timeout: 120

This sets the timeout threshold in seconds for file uploads to the
Anaconda repository. By default this threshold is 30, while the
configuration code in the above example resets it to 120.

How do I disable SSL checking on package installation?
------------------------------------------------------

By default, conda verifies SSL for any HTTPS URL that it uses to fetch
metadata or packages. If you do not want SSL-verification, disable it
with the following command:

    conda config --set ssl_verify false

This adds an entry to your .condarc file that disables SSL verification.

To disable it globally, add an entry to the “system” .condarc file,
which is tied to the Anaconda/Miniconda installation:

    conda config --set ssl_verify false --system

To re-enable SSL verification, run that same command, this time
replacing false with true.
