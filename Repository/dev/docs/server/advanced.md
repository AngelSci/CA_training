Advanced Installation Options
=============================

Enable HTTPS
------------

Before you start:

Purchase an SSL certificate and download the ssl `*.cert` file and ssl
`*.key` file.

NOTE: If security is not an issue, for testing you may set up a
self-signed SSL certificate. See <http://www.selfsignedcertificate.com/>
.

Save the ssl `*.cert` file and an ssl `*.key` file in your home
directory.

Configure the server to use those keys and the correct ports:

    anaconda-server-config --set ssl_options.keyfile ~/localhost.key
    anaconda-server-config --set ssl_options.certfile ~/localhost.cert
    anaconda-server-config --set port 8443
    anaconda-server-config --set redirect_http_port 8080

Restart your server for the changes to take effect:

    supervisorctl restart all

To test, navigate to the site using https in the address bar.

NOTE: If you use a self-signed SSL certificate, your web browser will
issue a warning that the website certificate cannot be verified.

Using Standard Ports
--------------------

### HTTP

The easiest way to enable clients to access an Anaconda repository
server on standard ports is to configure the server to redirect traffic
received on standard HTTP port 80 to the standard Anaconda repository
HTTP port 8080:

    sudo iptables -t nat -F
    sudo iptables -t nat -A OUTPUT -d localhost -p tcp --dport 80 -j REDIRECT --to-ports 8080
    sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080

### HTTPS

To use HTTPS, redirect traffic from standard HTTPS port 443 to standard
Anaconda repository HTTPS port 8443:

    sudo iptables -t nat -A OUTPUT -d localhost -p tcp --dport 443 -j REDIRECT --to-ports 8443
    sudo iptables -t nat -I PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 8443

NOTE: See also "Enable HTTPS" above.

Connect to an Existing MongoDB Database
---------------------------------------

If you already have a mongodb server running, you can connect to it by
setting the MONGO\_URL config variable:

    anaconda-server-config --set MONGO_URL 'mongodb://<hostname>'

NOTE: For more information, see the [MongoDB Connection String URI
Format](http://docs.mongodb.org/manual/reference/connection-string/)
manual.

Configure Anaconda repository to use LDAP
-----------------------------------------

Open the Anaconda repository configuration file /etc/binstar/config.yaml
and add the following configuration to enable Lightweight Directory
Access Protocol (LDAP) support:

    LDAP: {
      # Replace with company LDAP server
      'URI': 'ldap://<ldap.company.com>',

      # Replace <uid=%(username)s,ou=People,dc=company,dc=com> with your company specific LDAP Bind/Base DN
      # Bind directly to this Base DN.
      'BIND_DN': '<uid=%(username)s,ou=People,dc=company,dc=com>',

      # Map ldap keys into application specific keys
      'KEY_MAP': {
          'name':'cn',
          'company': 'o',
          'location':'l',
          'email': 'mail',
        },
    }

Update the **URI** with the location of your LDAP server and
**BIND\_DN** with the values specific to your LDAP server. Change the
**KEY\_MAP** keys with the associated values for your LDAP server.

Run the flask-ldap-login-check command to verify LDAP connectivity:

    flask-ldap-login-check binstar.wsgi:app --username 'jsmith' --password 'abc123DEF'

NOTE: Replace jsmith and abc123DEF with your actual LDAP username and
password.

To apply the changes, restart the Anaconda repository server:

    supervisorctl restart all

Open a new browser window and navigate to your local Anaconda repository
installation:

    http://your.anaconda.server

NOTE: Replace "your.anaconda.server" with your actual Anaconda
repository server IP address or domain name.

You can now log in using your LDAP credentials.

Configure Anaconda repository to use Active Directory
-----------------------------------------------------

Microsoft Active Directory is a server program that provides directory
services and uses the open industry standard Lightweight Directory
Access Protocol (LDAP).

Open the Anaconda repository configuration file /etc/binstar/config.yaml
and add the following configuration to enable Active Directory support:

    LDAP : {
        'URI': 'ldap://<ldap.server.url>',

        # This BIND_DN/BIND_PASSORD default to '', this is shown here for
        # demonstrative purposes. To enable Autorized Bind, insert the AD
        # BIND_DN and BIND_AUTH password for and authorized AD user.
        #
        #e.g. 'BIND_DN': '<cn=Authorized User,cn=users,dc=company,dc=local>',
        #e.g. 'BIND_AUTH': '<AuthUsrPassword>',

        # The values '' perform an anonymous bind so we may use search/bind method
        'BIND_DN': '',
        'BIND_AUTH': '',

        # Adding the USER_SEARCH field tells the flask-ldap-login that we
        # are using the search/bind method
        'USER_SEARCH': {'base': '<cn=users,dc=company,dc=local>', 'filter': 'sAMAccountName=%(username)s'},

        # Map ldap keys into application specific keys
        'KEY_MAP': {
            'name':'cn',
            'company': 'o',
            'location':'l',
            'email': 'userPrincipalName',
            },
    }

Update the *URI* &lt;ldap.server.url&gt; with the location of your
Active Directory server, *BIND\_DN* with the values specific to your
Active Directory server and the *BIND\_AUTH* with the password of the
user specified in the *BIND\_DN*. Change the **KEY\_MAP** keys with the
associated values from your Active Directory server.

To apply the changes, restart the Anaconda repository server:

    supervisorctl restart all

Run the flask-ldap-login-check command to verify Active Directory
connectivity:

    flask-ldap-login-check binstar.wsgi:app --username 'jsmith' --password 'abc123DEF'

NOTE: Replace jsmith and abc123DEF with your actual Active Directory
username and password.

You will see a response similar to the following:

    [anaconda.server] Started Site
    Got userdata for jsmith
    {'company': None, 'email': None, 'location': None, 'name': 'Jane Smith'}

Open your browser and navigate to your local Anaconda repository
installation:

    http://your.anaconda.server

NOTE: Replace "your.anaconda.server" with your actual Anaconda
repository IP address or domain name.

You can now log in with Active Directory.

Enable TLS on LDAP/Active Directory
-----------------------------------

Microsoft Active Directory is a server program that provides directory
services and uses the open industry standard Lightweight Directory
Access Protocol (LDAP).

To enable a secure Transport Layer Security (TLS) connection, add the
following to the LDAP configuration section of the file
\`/etc/binstar/config.yaml\`:

    LDAP={  ....

      'START_TLS': True,
      'OPTIONS': { 'OPT_PROTOCOL_VERSION': 3,
                   'OPT_X_TLS_DEMAND': True,
                   'OPT_X_TLS_REQUIRE_CERT': 'OPT_X_TLS_NEVER',
                   'OPT_X_TLS_CACERTFILE': '/path/to/certfile')
                  }
        ....
    }

LDAP and TLS Configuration Options
----------------------------------

### URI

Start by setting URI to point to your server. The value of this setting
can be anything that your LDAP library supports. For instance, openldap
may allow you to give a comma- or space-separated list of URIs to try in
sequence.

### BIND\_DN

The distinguished name to use when binding to the LDAP server (with
`BIND_AUTH`). Use the empty string (the default) for an anonymous bind.

### BIND\_AUTH

The password to use with `BIND_DN`.

### USER\_SEARCH

A dict that will locate a user in the directory. The dict object must
contain the required entries `base` and `filter` and may contain the
optional entry `scope`.

-   base: The base DN to search.
-   filter: Should contain the placeholder `%(username)s` for
    the username.
-   scope: One of `LDAP_SCOPE_BASE`, `LDAP_SCOPE_ONELEVEL`, or
    `LDAP_SCOPE_SUBTREE`.

For example:

``` {.sourceCode .yaml}
{'base': 'dc=example,dc=com', 'filter': 'uid=%(username)s'}
```

### KEY\_MAP

This is a dict mapping application context to ldap. An application may
expect user data to be consistent and not all ldap setups use the same
configuration:

``` {.sourceCode .yaml}
'application_key': 'ldap_key'
```

For example:

``` {.sourceCode .none}
KEY_MAP={'name': 'cn', 'company': 'o', 'email': 'mail'}
```

### START\_TLS

If `True`, each connection to the LDAP server will call `start_tls_s()`
to enable TLS encryption over the standard LDAP port. There are a number
of configuration options that can be given to `OPTIONS` that affect the
TLS connection. For example, `OPT_X_TLS_REQUIRE_CERT` can be set to
`OPT_X_TLS_NEVER` to disable certificate verification, perhaps to allow
self-signed certificates.

### OPTIONS

This stores LDAP specific options. For example:

``` {.sourceCode .yaml}
LDAP:
    OPTIONS:
        OPT_PROTOCOL_VERSION: 3
        OPT_X_TLS_REQUIRE_CERT: 'OPT_X_TLS_NEVER'
```

### TLS (secure LDAP)

To enable a secure TLS connection you must set `START_TLS` to True.
There are a number of configuration options that can be given to
`OPTIONS` that affect the TLS connection. For example,
`OPT_X_TLS_REQUIRE_CERT` `OPT_X_TLS_NEVER` disables certificate
verification, perhaps to allow self-signed certificates.

``` {.sourceCode .yaml}
LDAP:
    START_TLS: true
    OPTIONS:
        OPT_PROTOCOL_VERSION: 3
        OPT_X_TLS_DEMAND: true
        OPT_X_TLS_REQUIRE_CERT: 'OPT_X_TLS_NEVER'
        OPT_X_TLS_CACERTFILE: '/path/to/certfile'
```

Configure Anaconda repository to use Kerberos
---------------------------------------------

Kerberos is an authentication protocol designed to allow nodes
communicating over an insecure network to verify identity. Anaconda
repository can use Kerberos to authenticate users.

The Kerberos protocol uses timestamps to prevent replay attacks on
expired credentials, so the Network Time Protocol (NTP) service must be
set up and working correctly.

Several aspects of Kerberos rely on name service. Your Domain Name
System (DNS) entries and your hosts must have the correct information.
The `hostname` command and the configuration file `/etc/hostname` must
reflect the fully-qualified domain name (FQDN) of the machine. The
configuration file `/etc/hosts` must include an entry with the FQDN, to
allow reverse-DNS lookups to be performed.

To allow clients to authenticate against Anaconda repository, create a
principal for the service with a private key that identifies the
service. Create a service principal `HTTP/your.anaconda.server`, and
create the keytab containing this principal to
`/etc/binstar/http.keytab`:

``` {.sourceCode .bash}
SERVER_NAME=your.anaconda.server
```

If you are using MIT Kerberos:

``` {.sourceCode .bash}
kadmin -q "addprinc HTTP/${SERVER_NAME}"
kadmin -q "ktadd -k /etc/binstar/http.keytab HTTP/${SERVER_NAME}"
chown binstar:binstar /etc/binstar/http.keytab
chmod 600 /etc/binstar/http.keytab
```

If you are using Active Directory:

-   Open **Active Directory Users and Computers**
-   Select the **Users** container
-   Select the menu item **Action** &gt; **New** &gt; **User**
-   In the **New Object - User** dialog, fill in the user information.
    In this example, we use `your-anaconda-server` as the login.
-   In the next dialog, select the options **Password never expires**
    and **User cannot change password**
-   Right-click on the newly created user, and select **Properties**
-   In the **Properties** dialog, select the **Account** tab, and ensure
    the **Do not require Kerberos preauthentication** option is selected
-   Open an *Administrative* prompt and run:

``` {.sourceCode .bash}
ktpass -princ HTTP/your.anaconda.server@YOUR.DOMAIN -out http.keytab -pass "*" -mapUser your-anaconda-server -ptype KRB5_NT_PRINCIPAL
```

-   Copy the newly created file `http.keytab` to
    `/etc/binstar/http.keytab` on your Anaconda repository server.

To enable Kerberos authentication on Anaconda repository, add the
configuration options to `/etc/binstar/config.yaml`:

``` {.sourceCode .yaml}
AUTH_TYPE: KERBEROS
KRB5_KTNAME: /etc/binstar/http.keytab
```

To diagnose possible issues, enable logging for the Kerberos
authentication component. To enable logging, modify the `LOGGING` stanza
in `/etc/binstar/config.yaml` to include:

``` {.sourceCode .yaml}
LOGGING:
  # ...
  loggers:
    # ...
    flask_kerberos_login:
      handlers:
      - console
      level: INFO
      propagate: true
```

### Kerberos Configuration Options

`AUTH_TYPE` : string

:   Configures the authentication scheme used for Anaconda Repository.
    Set to `KERBEROS` to enable Kerberos authentication. Default:
    `NATIVE`.

`KRB5_KTNAME` : string

:   The file path of the keytab containing the service principal for
    Anaconda Repository. Default: `/etc/krb5.keytab`.

`KRB5_SERVICE_NAME` : string

:   The service type used to identify the service principal for
    Anaconda Repository. *HTTP* in
    `HTTP/your.anaconda.server@YOUR.REALM`. Default: `HTTP`.

`KRB5_HOSTNAME` : string

:   The hostname used to identify the service principal for
    Anaconda Repository. *your.anaconda.server* in
    `HTTP/your.anaconda.server@YOUR.REALM`. Default: the hostname of the
    machine on which Anaconda Repository is running.


