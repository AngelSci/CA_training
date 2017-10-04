Customizing your PyPI or Anaconda repository mirror - v 2.2.0 or earlier
========================================================================

Although some aspects of mirroring PyPI and the Anaconda repository
differ, the methodology for the specification of which packages to
mirror is identical. You can specify:

-   platforms (valid options are: 'linux-64', 'linux-32', 'osx-64',
    'win-32', and 'win-64')
-   whitelist
-   blacklist
-   license\_blacklist (the only valid option at this time is 'GPL')

All specification information should be included in the same file, and
can be passed to the binstar-sync-pypi or binstar-sync-conda command via
the --mirror-config argument:

    binstar-sync-conda --mirror-config /etc/binstar/mirrors/conda.yaml
    binstar-sync-pypi --mirror-config /etc/binstar/mirrors/pypi.yaml

Platform-specific mirroring
---------------------------

By default, the binstar-sync-pypi and binstar-sync-conda tools will
mirror all platforms. If you know that you will *not* need every
platform, you will find it useful to save time and space by editing the
sync-configuration.txt file to specify the platform(s) you want
mirrored:

    platforms:
      - linux-64
      - win-32

"Whitelist" Mirroring
---------------------

If your .yaml file contains a 'whitelist' argument, *only* the packages
enumerated under whitelist will be synced to your repository.

The file must contain a newline separated list of packages:

    whitelist:
      - dnspython
      - shapely
      - gdal

"Blacklist" Mirroring
---------------------

Although the whitelist is an inclusive delineation, the blacklist
functions as an exclusive delineation. For example:

    blacklist:
      - bzip2
      - tk
      - openssl

...will have the effect of mirroring the entire Anaconda repository
*except* the bzip2, tk, and openssl packages.

"License Blacklist" Mirroring
-----------------------------

Currently, only blacklisting GPL packages is supported:

    license_blacklist:
      - GPL

In this example, the mirror will copy all the packages in the repository
except those which are GPL-licensed, because the entire GPL license has
been license\_blacklisted.

Combining Multiple Mirror Configurations
----------------------------------------

In some situations, you may find that combining two or more of the
arguments above is the simplest way to get exactly the packages you
want.

The *platform* argument is evaluated before whitelist, blacklist or
license\_blacklist arguments. For example:

    platforms:
      - linux-64
    whitelist:
      - dnspython
      - shapely
      - gdal

...would have the effect of mirroring ONLY linux-64 distributions of the
dnspython, shapely and gdal packages.

The combination of both *whitelist* and *blacklist* functionality is an
unlikely scenario, because their impact is complementary. It is
recommended that you employ the argument that requires the enumeration
of the least number of packages. Use *whitelist* if you want to install
fewer than half the packages in the repository, and *blacklist* if you
want to install more than half the total packages.

If the *whitelist* and *license\_blacklist* arguments are both employed,
the *license\_blacklist* will be evaluated first, with the *whitelist*
functioning as a modifier. In this way packages which have been
initially blacklisted can be added back in.:

    license_blacklist:
      - GPL
    whitelist:
      - pyqt

This mirror configuration will copy ALL packages in the repository,
except those that are GPL-licensed, and will subsequently copy PyQt,
despite its GPL license, because it has been whitelisted.
