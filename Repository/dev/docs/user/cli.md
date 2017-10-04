Command Reference
=================

Anaconda client is the command line interface (CLI) to Anaconda Cloud,
and can be used for logging in, logging out, managing your account,
uploading files, generating access tokens, viewing tokens, and other
tasks as shown by running

anaconda -h

The full command reference is shown below.

anaconda
--------

Anaconda Cloud command line manager

**optional arguments:**

-h / --help

:   show this help message and exit

-V / --version

:   show program's version number and exit

**output:**

--show-traceback

:   Show the full traceback for chalmers user errors (default: tty)

--hide-traceback

:   Hide the full traceback for chalmers user errors

--verbose / -v

:   print debug information ot the console

--quiet / -q

:   Only show warnings or errors the console

--color

:   always display with colors

--no-color

:   never display with colors

**anaconda-client options:**

-t / --token TOKEN

:   Authentication token to use. May be a token or a path to a file
    containing a token

-s / --site SITE

:   select the anaconda-client site to use

**Commands:**

[auth](#Auth)

:   Manage Authorization Tokens

[channel](#Channel)

:   \[DEPRECATED in favor of label\] Manage your Anaconda Cloud channels

[config](#Config)

:   Binstar configuration

[copy](#Copy)

:   Copy packages from one account to another

[download](#Download)

:   Download notebooks from Anaconda Cloud

[groups](#Groups)

:   Manage Groups

[label](#Label)

:   Manage your Anaconda Cloud labels

[login](#Login)

:   Authenticate a user

[logout](#Logout)

:   Log out from Anaconda Cloud

[notebook](#Notebook)

:   Interact with notebooks in anaconda.org

[package](#Package)

:   Package utils

[remove](#Remove)

:   Remove an object from Anaconda Cloud

[search](#Search)

:   Search Anaconda Cloud

[show](#Show)

:   Show information about an object

[upload](#Upload)

:   Upload packages to Anaconda Cloud

[whoami](#Whoami)

:   Print the information of the current user

### Authentication

#### auth

Manage Authorization Tokens

**optional arguments:**

-h / --help

:   show this help message and exit

-n / --name NAME

:   A unique name so you can identify this token later. View your tokens
    at anaconda.org/settings/access

-o / --org / --organization ORGANIZATION

:   Set the token owner (must be an organization)

**token creation arguments:**

These arguments are only valid with the `--create` action

--strength STRENGTH

:   Create a token with STRENGTH of "strong" or "weak"

--strong

:   Create a longer token (default)

--weak / -w

:   Create a shorter token

--url URL

:   The url of the application that will use this token

--max-age MAX\_AGE

:   The maximum age in seconds that this token will be valid for

--scopes / -s

:   Scopes for token. For example if you want to limit this token to
    conda downloads only you would use --scopes "repo conda:download"

--out OUT

:   Output file

**actions:**

-x / --list-scopes

:   list all authentication scopes

-l / --list

:   list all user authentication tokens

-r / --remove NAME

:   remove authentication tokens

-c / --create

:   Create an authentication token

-i / --info / --current-info

:   Show information about the current authentication token

Manage Authentication tokens

See also:

-   [Using Anaconda Cloud
    Tokens](http://docs.anaconda.org/using.html#Tokens)

#### login

Authenticate a user

**optional arguments:**

--help / -h

:   show this help message and exit

--hostname HOSTNAME

:   Specify the host name of this login, this should be unique
    (default: ASUSN)

--username LOGIN\_USERNAME

:   Specify your username. If this is not given, you will be prompted

--password LOGIN\_PASSWORD

:   Specify your password. If this is not given, you will be prompted

#### whoami

Print the information of the current user

**optional arguments:**

-h / --help

:   show this help message and exit

[ ](#Informational)

### Informational

#### show

Show information about an object

**positional arguments:**

> SPEC
>
> :   Package written as USER\[/PACKAGE\[/VERSION\[/FILE\]\]\]
>
**optional arguments:**

-h / --help

:   show this help message and exit

Show information about an object

Examples:

    anaconda show continuumio
    anaconda show continuumio/python
    anaconda show continuumio/python/2.7.5
    anaconda show sean/meta/1.2.0/meta.tar.gz

#### search

Search Anaconda Cloud

**positional arguments:**

> NAME
>
> :   Search string
>
**optional arguments:**

-h / --help

:   show this help message and exit

-t / --package-type PACKAGE\_TYPE

:   only search for packages of this type

Search Anaconda Cloud for packages

[ ](#Config)

#### config

Binstar configuration

**optional arguments:**

--help / -h

:   show this help message and exit

--type TYPE

:   The type of the values in the set commands

**actions:**

--set \[u'name', u'value'\]

:   sets a new variable: name value

--get name

:   get value: name

--remove

:   removes a variable

--show

:   show all variables

--files / -f

:   show the config file names

**location:**

-u / --user

:   set a variable for this user

-s / --site

:   set a variable for all users on this machine

anaconda-client configuration

Get, Set, Remove or Show the anaconda-client configuration.

anaconda-client sites

anaconda-client sites are a mechanism to allow users to quickly switch
between Anaconda Cloud instances. This is primarily used for testing the
anaconda alpha site. But also has applications for the on-site [Anaconda
Enterprise](http://continuum.io/anaconda-server).

anaconda-client comes with two pre-configured sites `alpha` and
`binstar` you may use these in one of two ways:

-   Invoke the anaconda command with the `-s/--site` option e.g. to use
    the aplha testing site:

        anaconda -s alpha whoami

-   Set a site as the default:

        anaconda config --set default_site alpha
        anaconda whoami

Add a anaconda-client site

After installing [Anaconda
Enterprise](http://continuum.io/anaconda-server) you can add a site
named **site\_name** like this:

    anaconda config --set sites.site_name.url "http://<anaconda-enterprise-ip>:<port>/api"
    anaconda config --set default_site site_name

Site Options VS Global Options

All options can be set as global options - affecting all sites, or site
options - affecting only one site

By default options are set gobaly e.g.:

    anaconda config --set OPTION VALUE

If you want the option to be limited to a single site, prefix the option
with `sites.site_name` e.g.

    anaconda config --set sites.site_name.OPTION VALUE

Common anaconda-client configuration options

-   `url`: Set the anaconda api url (default:
    <https://api.anaconda.org>)
-   `verify_ssl`: Perform ssl validation on the https requests.
    verify\_ssl may be `True`, `False` or a path to a root CA pem file.

Toggle auto\_register when doing anaconda upload

The default is yes, automatically create a new package when uploading.
If no, then an upload will fail if the package name does not already
exist on the server.

    anaconda config --set auto_register yes|no

### Managing Packages

#### package

Anaconda Cloud package utilities

**positional arguments:**

> USER/PACKAGE
>
> :   Package to operate on
>
**optional arguments:**

-h / --help

:   show this help message and exit

**actions:**

--add-collaborator user

:   username of the collaborator you want to add

--list-collaborators

:   list all of the collaborators in a package

--create

:   Create a package

**metadata arguments:**

--summary SUMMARY

:   Set the package short summary

--license LICENSE

:   Set the package license

--license-url LICENSE\_URL

:   Set the package license url

**privacy:**

--personal

:   Set the package access to personal This package will be available
    only on your personal registries

--private

:   Set the package access to private This package will require
    authorized and authenticated access to install

#### upload

Upload packages to Anaconda Cloud

**positional arguments:**

> FILES
>
> :   Distributions to upload
>
**optional arguments:**

--help / -h

:   show this help message and exit

--channel / -c CHANNELS

:   \[DEPRECATED\] Add this file to a specific channel. Warning: if the
    file channels do not include "main",the file will not show up in
    your user channel

--label / -l

:   Add this file to a specific label. Warning: if the file labels do
    not include "main",the file will not show up in your user label

--no-progress

:   Don't show upload progress

--user / -u USER

:   User account, defaults to the current user

--no-register

:   Don't create a new package namespace if it does not exist

--register

:   Create a new package namespace if it does not exist

--build-id BUILD\_ID

:   Anaconda Cloud Build ID (internal only)

--interactive / -i

:   Run an interactive prompt if any packages are missing

--fail / -f

:   Fail if a package or release does not exist (default)

--force

:   Force a package upload regardless of errors

**metadata options:**

--package / -p PACKAGE

:   Defaults to the package name in the uploaded file

--version / -v VERSION

:   Defaults to the package version in the uploaded file

--summary / -s SUMMARY

:   Set the summary of the package

--package-type / -t PACKAGE\_TYPE

:   Set the package type, defaults to autodetect

--description / -d DESCRIPTION

:   description of the file(s)

--thumbnail THUMBNAIL

:   Notebook's thumbnail image

<!-- -->

    anaconda upload CONDA_PACKAGE_1.bz2
    anaconda upload notebook.ipynb
    anaconda upload environment.yml

##### See Also

-   [Uploading a Conda
    Package](http://docs.anaconda.org/using.html#Uploading)
-   [Uploading a PyPI
    Package](http://docs.anaconda.org/using.html#UploadingPypiPackages)

#### label

Manage your Anaconda Cloud channels

**optional arguments:**

--help / -h

:   show this help message and exit

--organization / -o ORGANIZATION

:   Manage an organizations labels

--copy LABEL LABEL

:   Copy a label

--list

:   list all labels for a user

--show LABEL

:   Show all of the files in a label

--lock LABEL

:   Lock a label

--unlock LABEL

:   Unlock a label

--remove LABEL

:   Remove a label

#### copy

Copy packages from one account to another

**positional arguments:**

> SPEC
>
> :   Package - written as user/package/version\[/filename\] If filename
>     is not given, copy all files in the version
>
**optional arguments:**

-h / --help

:   show this help message and exit

--to-owner TO\_OWNER

:   User account to copy package to (default: your account)

--from-channel FROM\_CHANNEL

:   \[DEPRECATED\]Channel to copy packages from

--to-channel TO\_CHANNEL

:   \[DEPRECATED\]Channel to put all packages into

--from-label FROM\_LABEL

:   Label to copy packages from

--to-label TO\_LABEL

:   Label to put all packages into

Anaconda-Build
--------------

Anaconda build client for continuous integration, testing and building
packages

**optional arguments:**

-h / --help

:   show this help message and exit

-V / --version

:   show program's version number and exit

**output:**

--show-traceback

:   Show the full traceback for chalmers user errors (default: tty)

--hide-traceback

:   Hide the full traceback for chalmers user errors

-v / --verbose

:   print debug information ot the console

-q / --quiet

:   Only show warnings or errors the console

--color

:   always display with colors

--no-color

:   never display with colors

**anaconda-client options:**

-t / --token TOKEN

:   Authentication token to use. May be a token or a path to a file
    containing a token

-s / --site SITE

:   select the anaconda-client site to use

**Commands:**

[backlog](cli.html#Backlog)

:   Run a build worker to build jobs off of a anaconda build queue

[build](cli.html#Build)

:   Anaconda build client for continuous integration, testing and
    building packages

[init](cli.html#Init)

:   Initialize Build file

[keyfile](cli.html#Keyfile)

:   \[Advanced\] Not documented yet

[keyfiles](cli.html#Keyfiles)

:   \[Advanced\] Not documented yet

[list](cli.html#List)

:   list the builds for package

[list-all](cli.html#List-All)

:   list the builds for package

[queue](cli.html#Queue)

:   Inspect build queue

[resubmit](cli.html#Resubmit)

:   Resubmit build

[results](cli.html#Results)

:   \[Advanced\] Attach results to build

[save](cli.html#Save)

:   Save build info to be triggered later

[submit](cli.html#Submit)

:   Submit a directory or github repo for building

[tail](cli.html#Tail)

:   Tail the build output of build number X.Y

[trigger](cli.html#Trigger)

:   Trigger a build that has been saved

[worker](cli.html#Worker)

:   Anaconda build client for continuous integration, testing and
    building packages

|

Anaconda Build command

To get started with anaconda build run:

    anaconda build init  anaconda build submit .  

See also:

-   [Anaconda Build](/building.html)

| | [ ](cli.html#SubmittingBuilds)

### Submitting Builds

[ ](cli.html#Submit)

#### submit

Submit a directory or github repo for building

**positional arguments:**

PATH

:   filepath or github url to submit

**optional arguments:**

-h / --help

:   show this help message and exit

--git-url GIT\_URL

:   The github url with valid .binstar.yml file to clone

-n / --dry-run

:   Parse the build file but don't submit

--no-progress

:   Don't show progress bar

--dont-git-ignore

:   Don't ignore files from .gitignore

--queue QUEUE

:   Build on this queue

**filters:**

--buildhost BUILDHOST

:   The host name of the intended build worker

--dist DIST

:   The os distribution of intended build worker (e.g centos, ubuntu)
    Use 'anaconda build queue' to view the workers

--platform PLATFORM

:   The platform to run (e.g linux-64, win-64, osx-64, etc) (default:
    all the platforms in the .binstar.yaml file)

**build control:**

--channel

:   \[DEPRECATED\] Upload targets to this channel

--label

:   Upload targets to this label

--test-only / --no-upload

:   Don't upload the build targets to Anaconda Cloud, but run everything
    else

-p / --package USER/PACKAGE

:   The Anaconda Cloud package namespace to upload the build to

--sub-dir SUB\_DIR

:   The sub directory within the git repository (github url
    submits only)

**tail:**

--tail / -f

:   Do 'tail -f on each sub-build log or each of the sub-builds given in
    '--sub-builds'

--sub-builds / -s

:   If --tail or -f is given, then tail sub-builds in '--sub-builds '
    Otherwise with --tail or -f, tail -f all sub-builds

|

Build command

Submit a build from your local path or via a git url:

See also:

-   [Submit A Build](/build.html#SubmitABuild)
-   [Submit A Build From Github](/build.html#GithubBuilds)

|

[ ](cli.html#Save)

#### save

Save build info to be triggered later

**positional arguments:**

URL

:   The http github url to the repo

**optional arguments:**

-h / --help

:   show this help message and exit

-p / --package USER/PACKAGE

:   The Anaconda Cloud package namespace to upload the build to

--sub-dir SUB\_DIR

:   The sub directory within the git repository (github url
    submits only)

--channel

:   \[DEPRECATED\] Upload targets to this channel

--label

:   Upload targets to this label

--queue QUEUE

:   Build on this queue

--email

:   Anaconda Cloud usernames or email addresses to email when the build
    completes

|

Save build info to be triggered later

See also:

-   [Save and Trigger Your Builds](/build.html#SaveAndTriggerYourBuilds)

|

[ ](cli.html#Trigger)

#### trigger

Trigger a build that has been saved

**positional arguments:**

USER/PACKAGE

:   The Anaconda Cloud package to trigger a build on

**optional arguments:**

-h / --help

:   show this help message and exit

--channel

:   \[DEPRECATED\] Upload targets to this channel

--label

:   Upload targets to this label

--queue QUEUE

:   Build on this queue

--branch BRANCH

:   Branch to build

**filters:**

--buildhost BUILDHOST

:   The host name of the intended build worker

--dist DIST

:   The os distribution of intended build worker (e.g centos, ubuntu)
    Use 'anaconda build queue' to view the workers

--platform PLATFORM

:   The platform to run (e.g linux-64, win-64, osx-64, etc) (default:
    all the platforms in the .binstar.yaml file)

--test-only / --no-upload

:   Don't upload the build targets to Anaconda Cloud, but run everything
    else

**tail:**

--tail / -f

:   Do 'tail -f on each sub-build log or each of the sub-builds given in
    '--sub-builds'

--sub-builds / -s

:   If --tail or -f is given, then tail sub-builds in '--sub-builds '
    Otherwise with --tail or -f, tail -f all sub-builds

|

Trigger a build that has been saved

See also:

-   [Save and Trigger Your Builds](/build.html#SaveAndTriggerYourBuilds)

| | [ ](cli.html#HostingBuildMachines)

### Hosting Build machines

[ ](cli.html#Queue)

#### queue

Build Queue

**positional arguments:**

USERNAME/QUEUENAME

:   Specify a queue to perform an operation on

**optional arguments:**

-h / --help

:   show this help message and exit

-r / --remove

:   Remove the queue specified with the -q/--queue option

-c / --create

:   Create a new queue

--remove-worker WORKER\_ID

:   Remove a worker from a queue

|

[ ](cli.html#Worker)

#### worker

None

**optional arguments:**

-h / --help

:   show this help message and exit

**Commands:**

[deregister](cli.html#Deregister)

:   Deregister a build worker to build jobs off of a binstar build queue

[docker\_run](cli.html#Docker_Run)

:   Run a build worker in a docker container to build jobs off of a
    binstar build queue

[list](cli.html#List)

:   List build workers and queues

[register](cli.html#Register)

:   Register a build worker to build jobs off of a binstar build queue

[run](cli.html#Run)

:   Run a build worker to build jobs off of a binstar build queue

|

Anaconda Build command

To get started with anaconda worker run:

    anaconda worker register USER/QUEUE -n NAME  anaconda worker run NAME  

See also:

-   [Anaconda Build](/build-config.html#BuildWorkers)

|

[ ](cli.html#DockerWorker)

#### docker-worker

|
