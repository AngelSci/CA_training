Anaconda repository
===================

Manage third-party dependencies on your own terms, and streamline the
release cycle of your code. An internal, self-contained package mirror
installs securely behind your firewall and supports over 700 different
repositories, including PyPI, CRAN, conda, and the Anaconda repository.

Note: Anaconda repository was previously known as Anaconda server.

Administrator guide
-------------------

User guide
----------

Many enterprises have customized local instances of Anaconda repository,
and Continuum also makes an instance of Anaconda repository available
for public use at [Anaconda Cloud](http://anaconda.org). Documentation
for users of Anaconda Cloud and Anaconda repository is available at
/anaconda-cloud/index.

What's new in 2.18.0?
---------------------

The Anaconda repository 2.18.0 release is available to all Anaconda
repository customers as of June 1, 2016.

NOTE: If you have a subscription BUT do not have a license, contact
[support](http://continuum.io/support) to receive that license.
Otherwise contact [sales](https://www.continuum.io/contact-us) to
acquire it.

Administrators can update to the new Anaconda repository release via the
following commands:

    conda update binstar-server anaconda-client anaconda-build
    anaconda-server-db-setup --execute
    supervisorctl stop
    supervisorctl reload
    supervisorctl start all

Please contact your Priority Support provider or sales person for any
questions or problems regarding the release.

### Highlights of the update

-   New API endpoint `/user/{account}/downloads/{start}--{end}`
    summarizing download activity for an account
-   Build automatically scrolls to the bottom of the log when new lines
    are appended
-   Improved support for R packages
-   Link from license warning message to license configuration page
-   Builds can be triggered without being logged in to GitHub
-   Proxy compatible remote build worker address detection
-   Improved LDAP login support
-   Improved PIP package name lookups

