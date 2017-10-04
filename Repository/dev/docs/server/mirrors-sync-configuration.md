Configuring your PyPI or Anaconda repository mirror
===================================================

NOTE: This documentation is for Anaconda Server 2.3.0+. For
documentation of older versions, please go
[here](mirrors-sync-configuration-2.2.html).

Before you begin
----------------

Before installing Anaconda Server 2.3.0 and using the updated features
listed below, you must install the supplemental cas-mirror package:

> conda install cas-mirror

Although some aspects of mirroring PyPI and the Anaconda repository
differ, the methodology for the specification of which packages to
mirror is identical. You can specify:

-   platforms (valid options are: 'linux-64', 'linux-32', 'osx-64',
    'win-32', and 'win-64')
-   pkg\_list
-   python\_versions (valid options are: 2.6, 2.7, 3.3, 3.4)
-   license\_blacklist (valid options are: AGPL, GPL2, GPL3, LGPL, BSD,
    MIT, Apache, PSF, Public-Domain, Proprietary and Other) \*
-   blacklist
-   whitelist

Other useful configuration options include:

-   remote\_url

    Specifies the remote URL from which the conda packages and the
    Anaconda and Miniconda installers are downloaded. The default value
    is: [<https://repo.continuum.io/>](https://repo.continuum.io/).

-   channels

    Specifies the remote channels from which conda packages
    are downloaded. The default is a list of the channels
    &lt;remote\_url&gt;/pkgs/free/ and &lt;remote\_url&gt;/pkgs/pro/

NOTE: the license\_blacklist feature is not available for PyPI due to
the non-standardization of license metadata for these packages.

All specification information should be included in the same file, and
can be passed to the anaconda-server-sync-pypi or
anaconda-server-sync-conda command via the --mirror-config argument:

    anaconda-server-sync-conda --mirror-config /etc/binstar/mirrors/conda.yaml
    anaconda-server-sync-pypi --mirror-config /etc/binstar/mirrors/pypi.yaml

Platform-specific mirroring
---------------------------

By default, the anaconda-server-sync-pypi and anaconda-server-sync-conda
tools will mirror all platforms. If you know that you will *not* need
all platforms, you will find it useful to save time and space by editing
the YAML file to specify the platform(s) you want mirrored:

    platforms:
      - linux-64
      - win-32

Package-specific mirroring
--------------------------

In some cases you may want to mirror only a small subset of the Anaconda
repository. Rather than blacklisting a long list of packages you do not
want mirrored you can instead simply enumerate the list of packages you
**do** want mirrored.

This argument **cannot** be used with the blacklist, whitelist or
license\_blacklist arguments. It can be used with the platform-specific
argument.

For example:

    pkg_list:
    - accelerate
    - pyqt
    - zope 

...will have the effect of mirroring only three packages: Accelerate,
PyQt & Zope. All other packages will be completely ignored.

Python version-specific mirroring
---------------------------------

A new feature in Anaconda Server 2.3.0 allows you to mirror the Anaconda
repository with a python version or versions specified.

For example:

    python_versions:
    - 3.3

...will have the effect of mirroring only Anaconda packages built for
Python3.3.

"License blacklist" mirroring
-----------------------------

As of Anaconda Server 2.3.0 the Anaconda mirroring script supports
license blacklisting for the following license families:

> -   AGPL
> -   GPL2
> -   GPL3
> -   LGPL
> -   BSD
> -   MIT
> -   Apache
> -   PSF
> -   Public-Domain
> -   Proprietary
> -   Other

For example:

    license_blacklist:
      - GPL2
      - GPL3
      - BSD

...will have the effect of mirroring all the packages in the repository
except those that are GPL2-, GPL3-, or BSD-licensed, because those three
licenses have been completely blacklisted.

NOTE: Older versions of Anaconda Mirror only support license
blacklisting for GPL. If you are using an older version of Anaconda
repository, use the documentation for [customizing your PyPI or Anaconda
repository mirror](mirrors-sync-configuration-2.2.html).

"Blacklist" mirroring
---------------------

The blacklist functions as an exclusive delineation. For example:

    blacklist:
      - bzip2
      - tk
      - openssl

...will have the effect of mirroring the entire Anaconda repository
*except* the bzip2, tk, and openssl packages.

"Whitelist" mirroring
---------------------

The whitelist functions in combination with either the
license\_blacklist or blacklist arguments, and re-adds packages that
were excluded by a previous argument.

For example:

    license_blacklist:
      - GPL2
      - GPL3
    whitelist:
      - readline

... will have the effect of mirroring the entire Anaconda repository
*except* any GPL2- or GPL3-licenses packages, but including readline,
despite the fact that it is GPL3-licensed.

Combining multiple mirror configurations
----------------------------------------

In some situations, you may find that combining two or more of the
arguments above is the simplest way to get the exact combination of
packages that you want.

The *platform* argument is evaluated prior to any other argument. For
example:

    platforms:
      - linux-64
    pkg_list:
      - dnspython
      - shapely
      - gdal

...will have the effect of mirroring ONLY linux-64 distributions of the
dnspython, shapely and gdal packages.

If the *license\_blacklist* and *blacklist* arguments are combined, the
*license\_blacklist* will be evaluated first, with the *blacklist* being
a supplemental modifier:

    license_blacklist:
      - GPL2
    blacklist:
      - pyqt

In this example, the mirror configuration will mirror all packages in
the repository, EXCEPT those which are GPL2-licensed and pyqt, despite
its GPL3 license, because it has been blacklisted.

If the *blacklist* and *whitelist* arguments are both employed, the
*blacklist* is evaluated first, with the *whitelist* functioning as a
modifier:

    blacklist:
     - accelerate
     - astropy
     - pygments
    whitelist:
     - accelerate

This mirror configuration mirrors all packages in the repository except
astropy and pygments. Despite being listed on the blacklist, accelerate
will be mirrored because it is subsequently listed on the whitelist.
