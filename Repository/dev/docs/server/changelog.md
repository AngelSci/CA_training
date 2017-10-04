Anaconda repository changelog
=============================

Anaconda repository 2.18.0 - 2016-06-01
---------------------------------------

Added

-   API: add an endpoint `/user/{account}/downloads/{start}--{end}` that
    provides an aggregated summary of download activity for an account.
-   BUILD: automatically scroll to the bottom of log when new lines are
    appended
-   REPO: improve support for R packages
-   WEB: license warning message includes a link to the license
    configuration page

Fixed

-   Users do not need to be logged into GitHub to trigger builds
-   BUILD: remote address for workers will be detected correctly when
    running behind a proxy (\#2036)
-   API: LDAP users logging in for the first time via anaconda login are
    created correctly.
-   PIP v8.1.2 fixed package name lookup

Anaconda repository 2.17.0 - 2016-04-18
---------------------------------------

Added

-   Queue administration page that displays build worker details and
    history (\#1847)
-   An additional configuration file can be specified with the
    environment variable `ANACONDA_SERVER_CONFIG` or the command line
    argument `--config-file`
-   Configuration files in the directory `$PREFIX/etc/anaconda-server/`
    will now be automatically loaded
-   Better logging for login logic
-   Failed logins are now recorded in the security log
-   `docs.anaconda.org` content is now bundled with Anaconda Repository
-   New privacy policy
-   Project's API
-   Show notebooks with nbpresent metadata as presentations (\#1583)
-   Can now view different versions of notebooks (\#1764)
-   Complete list of current settings on /admin/deployment (\#1928)
-   Decorator to validate params in a requests. (\#1970)
-   `api.anaconda.org` returns `conda_url`, `pypi_url` and
    `main_url` (\#1984)
-   `keyname` is displayed for superusers on the file details modal,
    allowing an administrator to locate a file on disk (\#1985)

Fixed

-   Editing package description should not add extra whitespace (\#1710)
-   Starred packages owned by other users will appear on the
    dashboard (\#1706)
-   Notebook output that is too wide will display a scroll-bar (\#1581)
-   Cleaned up styling on CI settings page (\#1713)
-   Security log details modal should appear for non-administrator users
-   More graceful handling of notebook rendering failure (\#1548)
-   GitHub OAuth flow in the user settings page (\#1931)
-   Changed conda install instructions to use short channel name
-   Group API exceptions when viewing group members (\#1959)
-   Fixed error in sample enterprise config file (\#1968)

Changed

-   Renamed "upvotes" to "favorites" (\#1707)
-   adjusted helptext for conda install from specific user
    channel (\#1914)

Anaconda repository 2.16.6 - 2016-03-28
---------------------------------------

-   Clean up build workers that have been idle too long (\#1749)
-   Add SMTP support for sending email (\#1747)
-   Add remote address of build workers to queue status (\#1743)
-   Toggleable sections in build log output
-   Render progress bars in build log correctly
-   Fix organization page redirects
-   Improve search performance for "type:pypi" query (\#1808)
-   Fix duplicated build item when resubmitting via CLI (\#1805)
-   Fix sorting of file sizes (\#1783)
-   Fix small issue in package files page

Anaconda repository 2.16.0 - 2016-02-25
---------------------------------------

-   Kerberos Authentication Support
-   Several small fixes
-   Performance improvements

Anaconda repository 2.15.5 - 2016-02-06
---------------------------------------

-   Minor fixes and improvements
-   Made build a separate component from the server
-   Added license code
-   Improved UI
-   Better support for labels
-   Improved performance on user profiles / security pages

Anaconda repository 2.14.1 - 2016-01-20
---------------------------------------

-   Re-enabled the anaconda copy command
-   Release renaming "channels" to "labels"
-   Implemented new UI enhancements that included a new user dashboard
-   Performed additional bug fixes

Anaconda repository 2.13.1 - 2016-01-12
---------------------------------------

-   Implemented "My upvotes" page
-   Added UI improvements to notebooks
-   Implemented error logging fixes
-   Performed additional bug fixes

Anaconda repository 2.12.3 - 2015-12-22
---------------------------------------

-   Implemented UI Improvements to align with Anaconda branding, making
    A-Cloud easier to use
-   Added confirmation after sending a message to support from the
    "contact us" page
-   Removed left nav on dashboard
-   Moved channel manager to the apps dropdown
-   Made it easier for Academic users to access features by adding
    extended subdomain access for institutions
-   Created a landing page for bug reporting to help A-Cloud users
    better self-select which repo for issue logging

Anaconda repository 2.11 - 2015-12-09
-------------------------------------

-   Implemented UI Improvements
-   Fixed minor issues
-   Improved user profile
-   Improved password validation
-   Updated plans and pricing pages

Anaconda repository 2.10 - 2015-11-13
-------------------------------------

-   Implemented UI Improvements

Anaconda repository 2.9 - 2015-09-28
------------------------------------

-   Implemented Upgrade/Setup script
-   Offered free MKL Optimizations and free IOPro Addons for academic
    use
-   Added command line scripts for user name changes
-   Allowed port number configuration
-   The Anaconda Server will subsequently be referred to as Anaconda
    repository

Anaconda Server 2.8 - 2015-08-27
--------------------------------

-   Added support for Jupyter 4.0
-   Made passwords configurable
-   Supplied better error messages

Anaconda Server 2.7 - 2015-07-28
--------------------------------

-   Implemented a new environment page
-   Offered new channel features

Anaconda Server 2.6 - 2015-07-23
--------------------------------

-   Added support for [conda noarch packages](noarch-packages.html).
-   Exposed additional distribution attributes via the API
-   Changed Anaconda Server's underlying webserver from tornado to
    gunicorn

Anaconda Server 2.3 - 2015-04-24
--------------------------------

-   [Increased specificity](mirrors-sync-configuration.html) when
    mirroring the Anaconda repository including more robust
    license-blacklisting capacity and new python version-filtering
    capacity
-   Implemented the ability to [upload iPython
    notebooks](notebooks.html) to your Anaconda Server user account

Anaconda Server 2.2 - 2015-04-17
--------------------------------

-   Improved the user interface for channel-based interactions, which
    allowed users to manage multiple package and channel interactions
    from a single dashboard
-   Performed additional unit testing
-   Due to a lack of backwards compatibility, this release locks the
    following two versions of the dependency packages:

    > -   flask-wtf=0.8.4
    > -   werkzeug=0.9.6

Update instructions for current and past versions
-------------------------------------------------

Updating to 2.18:

    conda update binstar-server anaconda-client anaconda-build
    anaconda-server-db-setup --execute
    supervisorctl stop
    supervisorctl reload
    supervisorctl start all

To 2.17:

    conda update binstar-server anaconda-client anaconda-build
    anaconda-server-db-setup --execute
    supervisorctl stop
    supervisorctl reload
    supervisorctl start all

To 2.16:

    conda update binstar-server anaconda-client anaconda-build
    anaconda-server-db-setup --execute
    supervisorctl restart all

To 2.15:

    conda update binstar-server anaconda-client anaconda-build
    anaconda-server-db-setup --execute
    supervisorctl restart all

To 2.14:

    conda update binstar-server anaconda-client anaconda-build
    anaconda-server-db-setup --execute
    supervisorctl restart all

To 2.13:

    conda update binstar-server anaconda-client anaconda-build
    anaconda-server-db-setup --execute
    anaconda-server-config --config-file /etc/binstar/config.yaml --set LABEL_NAME "'channel'"
    supervisorctl restart all

To 2.12:

    conda update binstar-server anaconda-client anaconda-build
    anaconda-server-db-setup --execute
    supervisorctl restart all

To 2.9:

    conda update binstar-static binstar-server cas-mirror
    anaconda-server-db-setup --execute
    supervisorctl restart all

To 2.8:

    conda update binstar-static binstar-server cas-mirror
    anaconda-server-db-setup --execute
    supervisorctl restart all

To 2.6.0:

    conda update binstar-server
    conda install cas-mirror

To 2.5.1:

    conda update binstar-server

To 2.3:

    conda update binstar-server
    conda install cas-mirror

To 2.2:

    conda update binstar-server
