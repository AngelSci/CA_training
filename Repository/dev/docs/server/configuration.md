Client configuration
====================

The Anaconda Client gives you the ability to upload packages to your
on-site Anaconda repository and provides highly granular access control
capabilities. Here is how to configure your client to use your local
repository instead of Anaconda Cloud.

Anaconda client configuration
-----------------------------

On each machine that will access your on-site Anaconda repository, run
this command as the machine's local user:

    anaconda config --set url http://your.server.name:<port>/api

Or to set the default repo on a system wide basis, run this command:

    anaconda config --set url http://your.server.name:<port>/api --site

The system level config file will only be used if no user level config
file is present.

To show the system and user config file locations and configuration
settings:

    anaconda config --show

Conda configuration
-------------------

To access conda packages from your Anaconda repository, add the channel
to your system .condarc configuration file. This configures conda to use
a local onsite Anaconda repository as the default instead of the public
Anaconda.org.

If you are using the anaconda mirror, run the following:

    conda config --add default_channels http://your.server.name:<port>/conda/anaconda --system

Next, on each machine that will access your on-site Anaconda repository,
tell conda to expand any channel aliases to use your on-site Anaconda
repository. Edit your file \$PREFIX/.condarc (the system .condarc) to
manually add:

    channel_alias: http://<your.server.name:8080/conda

Users can then add individual accounts to their .condarc file by running
the following command:

    conda config --add channels USERNAME

NOTE: Use the --system option to add it to the global .condarc.

For more information, please see:

-   [Channel
    alias](http://conda.pydata.org/docs/install/central.html#channel-alias-channel-alias)
-   [Default
    channels](http://conda.pydata.org/docs/install/central.html#default-channels-default-channels)

pip configuration
-----------------

To install pypi packages from your Anaconda repository, add your channel
to your \~/.pip/pip.conf configuration file.

Edit the file and add an extra-index-url entry to the global config
section:

    [global]
    extra-index-url = http://your.server.name:<port>/pypi/<username>/simple

Kerberos
--------

If you have enabled Kerberos authentication as described in the advanced
installation guide, your browser and anaconda-client should be able to
authenticate to Anaconda repository using Kerberos.

In OS X/Unix, configure the file `/etc/krb5.conf`:

    [libdefaults]
    default_realm = YOUR.DOMAIN

    [realms]
    YOUR.DOMAIN = {
      kdc = your.kdc.server
    }

    [domain_realm]
    your.anaconda.server = YOUR.DOMAIN

If your configuration is correct, you should be able to authenticate
using the command-line tool `kinit`:

    kinit jsmith
    anaconda login

### Browser Setup

Many browsers do not present your Kerberos credentials by default, to
prevent leaking credentials to untrusted parties. In order to use
Kerberos authentication, you must white-list Anaconda repository as a
trusted party to receive credentials.

You must restart your browser after configuring the whitelist in order
for changes to be reflected.

#### Safari

Safari requires no configuration - it will automatically present your
credentials without white-listing.

#### Chrome

The `AuthServerWhitelist` policy must be set to `your.anaconda.server`
-this will allow Chrome to present credentials to Anaconda Repository
with the hostname `your.anaconda.server`. Depending on your DNS
configuration, DisableAuthNegotiateCnameLookup may also be required -
this will prevent Chrome from canonicalizing the hostname before
generating a service name.

To configure on OS X:

    defaults write com.google.Chrome AuthServerWhitelist "your.anaconda.server"

On Linux:

    mkdir -p /etc/opt/chrome/policies/managed
    mkdir -p /etc/opt/chrome/policies/recommended
    chmod -w /etc/opt/chrome/policies/managed
    echo '{"AuthServerWhitelist": "your.anaconda.server"}' > /etc/opt/chrome/policies/managed/anaconda_repo_policy.json

On Windows, use Group Policy objects to set the "Authentication server
whitelist" setting to "your.anaconda.server".

For more information, see Chrome's [SPNEGO
authentication](http://www.chromium.org/developers/design-documents/http-authentication)
and [administration](https://www.chromium.org/administrators)
documentation.

#### Firefox

-   Navigate to the configuration page `about:config`
-   Search for "negotiate"
-   Set the configuration item `network.negotiate-auth.trusted-uris` to
    `your.anaconda.server`

#### Internet Explorer

-   Open the menu item *Internet Options &gt; Tools &gt; Advanced Tab*
-   In the *Security* section, select "Enable Integrated Windows
    Authentication"

