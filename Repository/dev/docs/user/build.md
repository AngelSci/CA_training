Anaconda Build
==============

[ ](#Overview)

Overview
--------

[ ](#HowAnacondaBuildWorks)

### How Anaconda Build works

The **Anaconda Build System** provides **Continuous Integration**
powered by **conda** and **conda environments** for all platforms,
through a simple yet powerful interface.

The build process follows an **Anaconda Build Recipe** (a set of
instructions specified in a `.binstar.yml` file), which includes the
(conda) test environments to use, build instructions and additional
scripts to be executed. A **Build Recipe** does not require the creation
of a **conda package** as a final product. However, creating **conda
packages** and uploading them to Anaconda Cloud provides a seamless and
comprehensive workflow for the maintenance and distribution of packages.

[ ](#WhyUseAnacondaBuild)

### Why use Anaconda Build?

There are several use cases for which Anaconda Build can be used to
provide an efficient packaging workflow. A user may:

-   Have a series of packages and want to compile them into conda
    packages so it's easy for other users to conda install those
    packages from the first user's channel on Anaconda Cloud.
-   Be part of a workgroup or team using a GitHub repository that has
    basic Continuous Integration needs that can be centralized with
    Anaconda Cloud so other potential users can easily download their
    open source packages for different platforms.
-   Be part of an organization that needs to build and distribute
    cross-platform conda packages across OS X, Windows and Linux.

[ ](#SystemComponents)

### System components

The **Anaconda Cloud Build System** is based on three main components:

[ ](#BuildQueues)

#### Build queues

The **Build Queues** receive build job requests from users and assign
these requests to the different available workers. Queues are hosted on
**Anaconda Cloud**.

Each Anaconda Cloud user may use the public Linux-64 build queue
provided by Anaconda Cloud. New build queues can be created by
organizations on Anaconda Cloud.

When an organization creates a queue no groups have access to it, and
the organization can grant access to that queue to one or more groups.
The organization can create groups, add organizations and individual
users to a group or remove them, and can turn on or off a group's access
to a queue.

[ ](#Workers)

#### Workers

These are machines that perform the actual build instructions and
testing specified in the **Anaconda Build Recipe**. They are often
Amazon Web Services (AWS) instances. Different workers can be created
for different platforms including:

-   Windows 32/64
-   Linux 32/64
-   OS X 64

Note: By default only Linux-64 build workers are available for public
use with Anaconda Cloud. For access to additional platforms you can add
your own build workers on your local machine, in virtual machines (VMs)
or on cloud computing providers such as AWS.

[ ](#Users)

#### Users

Users are responsible for creating and launching anaconda builds from
the command line interface into a (previously created) build queue.

To enable a user to use a queue other than the Anaconda Cloud public
Linux-64 queue, the organization that created the queue must add the
user to a group and grant that group access to the queue.

[ ](#BuildsInAnacondaCloud)

Builds in Anaconda Cloud
------------------------

[ ](#Prerequisites)

### Prerequisites

Before using the Anaconda Build System:

1.  Create an account on Anaconda Cloud at
    [anaconda.org](https://anaconda.org/)
2.  Install [Anaconda](https://www.continuum.io/downloads) or
    [Miniconda](http://conda.pydata.org/miniconda.html)
3.  Install conda build, Anaconda Client and Anaconda Build:
    `conda install conda-build anaconda-client anaconda-build`
4.  Log in to Anaconda Cloud from the command line using Anaconda
    Client: `anaconda login`
5.  (**Optional**) Create an organization to be able to create new
    queues, at
    [anaconda.org/new/organization](https://anaconda.org/new/organization)

[ ](#SubmitABuild)

### Submit a build

[ ](#CreateAPackage)

#### Create a package

If you are not familiar with anaconda-client, create a package first.
This will be the namespace or the context of the build.

    mkdir conda_build_test
    cd conda_build_test
    anaconda package --create USERNAME/conda_build_test

[ ](#CreateABuildConfig)

#### Create a build config

Let's create a simple build config file and submit an empty build job to
illustrate the basic steps.

The `.binstar.yml` file holds the Anaconda Build Recipe for how to build
and test your package. It tells the build system which platforms to
build on, which environment variables to use and which scripts to
execute.

To add a `.binstar.yml` file to your working directory, run
`anaconda build init` in your working directory.

Note: This should be the same directory as your `meta.yaml` file if you
are building a conda package.

Once this is complete you should be able to submit your first build that
will print `This is my anaconda build!`

    anaconda build init
    anaconda build submit .
    anaconda build tail -f USERNAME/conda_build_test 1

We have just created an empty package with a single Build Recipe
instruction, namely printing `This is my anaconda build!`.

[ ](#CreateCondaPackage)

#### Create conda package

Let's create a conda package to show that anaconda build can do some
actual work.

You need to add a `meta.yaml` file and modify your `.binstar.yml` file
so it contains the following keys:

.binstar.yml

    package: conda_build_testscript:  - conda build .build_targets: conda

|

YAML

meta.yaml

    package:  name: conda_build_test  version: 0.0.1build:  number: 1  script:    - echo "This is my anaconda build with conda"requirements:  run:    - pythonabout:  summary: This is an anaconda build test!

|

YAML

Note: Please see our publicly available [Conda
Recipes](https://github.com/conda/conda-recipes).

[ ](#SubmitYourCondaBuild)

#### Submit your conda build

Once your have created the `meta.yaml` file you can test that your conda
build runs locally with [conda
build](http://conda.pydata.org/docs/build.html).

Submitting this build is the same as the first:

    conda build .
    anaconda build submit .
    anaconda build tail -f USERNAME/conda_build_test 2

[ ](#InstallYourNewCondaPackage)

#### Install your new conda package

By default Anaconda Cloud puts all new packages in a `dev` label in your
account. See [Using labels in the development
cycle](using.html#UsingLabelsInTheDevelopmentCycle) for a more in depth
example on how to use labels.

    conda install -c USERNAME/label/dev conda_build_test

[ ](#GithubBuilds)

### GitHub builds

[ ](#CreateAGitRepo)

#### Create a git repo

Let's use the package you have created in the [submit a
build](#SubmitABuild) example. First [create a new github
repository](https://github.com/new). You will then need to push the
files to github.

First: [create a new github repository](https://github.com/new)

    git init
    git add * .binstar.yml
    git commit -m "first commit"
    git remote add origin https://github.com/GITHUB_USERNAME/conda_build_test.git
    git push -u origin master

[ ](#SubmitTheBuild)

#### Submit the build

Once the package source is pushed to github you can submit a build via a
github url.

    anaconda build submit https://github.com/GITHUB_USERNAME/conda_build_test

[ ](#SaveAndTriggerYourBuilds)

### Save and trigger your builds

Once you have [submitted a build from github](#GithubBuilds) you may
want to save your build configuration, especially if you are using
[extra options](/cli.html#Submit) like `-p`, `--sub-dir`, `--label`,
`--queue` or `--email`.

You can [save](/cli.html#Save) these options to Anaconda Cloud and
[trigger](/cli.html#Trigger) them later.

Note: Using the anaconda build save command affects the Continuous
Integration (CI) section of the package settings on Anaconda Cloud. For
example, running an "anaconda build save" command that uses the
"--label" flag will update the label used by CI services. The CI section
of the package settings can be seen by going to the package's page on
Anaconda Cloud and choosing "Settings" and then "Continuous
Integration", or by examining the package's binstar.yaml file.

    anaconda build save -p USERNAME/conda_build_test https://github.com/GITHUB_USERNAME/conda_build_test --label dev
    anaconda build trigger USERNAME/conda_build_test

It is also possible to trigger a build on a specific queue, build host,
repository branch, and/or distribution. For information on options, see

    anaconda build trigger --help

Here is an example of triggering a build on a queue, repository branch,
and centos distribution:

    anaconda build trigger USERNAME/conda_build_test --dist centos --branch master --queue USERNAME/QUEUENAME

[ ](#ContinuousIntegrationRunABuildOnGitPush)

### Continuous Integration: run a build on git push

Once you have saved a build you can view the information on the website
at

`https://anaconda.org/USERNAME/conda_build_test/settings/ci`

To get to this page, navigate to your package
(`https://anaconda.org/USERNAME/conda_build_test`). Then choose
`settings` and `Continuous Integration`.

![Continuous Integration page](/img/cloud-ci.png)

Click "Edit". The fields we care about for enabling continuous
integration are:

branches to test

This is a python regular expression (regex) describing what branches
should trigger builds in `test-only` mode. No files will be uploaded to
Anaconda Cloud.

branches to upload

This is a python regex describing what branches should trigger builds
that also upload the resulting [build\_targets](#Build_Targets).

\*\* This can cause many files to accumulate in your account. Use
carefully.

Add Webhook

If checked Anaconda Cloud will add a [github
webhook](https://developer.github.com/webhooks/) with the value
[<https://api.anaconda.org/github-hook>](https://api.anaconda.org/github-hook)
to your github package.

For this example:

-   Set `Test Branches` to `refs/heads/.*`, which matches all
    git branches.
-   Leave `Upload Branches` empty.
-   Make sure `Add Webhook` is checked.

You should see an active webhook at the end of this process.

![Webhook Continuous Integration page](/img/cloud-webhook-ci.png)

Now, test that the web hook is correct by pushing an empty commit.

    git commit -m "Trigger build" --allow-emptygit push # This should give enough time to let github send the webhooksleep 10 anaconda build list-all USERNAME/conda_build_test

|

Bash

To debug webhooks, first submit your build again with [anaconda-client
trigger](#SaveAndTriggerYourBuilds). This should highlight the issue
with your build.

If `anaconda trigger` works, but the webhook still does not, go to
github and inspect the webhook requests and responses.

[ ](#BuildConfiguration)

Build configuration
-------------------

[ ](#ConfigurationFileTags)

### Configuration file tags

Each package you build will have a build config file in its root
directory named `.binstar.yml`. If you are not already familiar with the
build process, please begin by reading this guide on [how to submit a
build](#SubmitABuild).

This yaml file contains a number of tags to control the way a build is
run. Every tag is optional, and all tags can be written as a single
command or as a list.

    tag: single_command# ORtag:  - some_command  - another_command

|

YAML

[ ](#Script)

#### script

Define the main script to run on the build machine:

    script: echo "hello world!"

|

YAML

Script may also be a list:

    script:  - some_command  - another_command

|

YAML

[ ](#Before_ScriptAndAfter_Script)

#### before\_script and after\_script

You can also define scripts to be run before and after the main script:

    before_script: some_commandafter_script:  another_command

|

YAML

For the `after_script` tag the environment variable
[BINSTAR\_BUILD\_RESULT](#EnvironmentVariables) will be made available
as either *success* or *failure*.

[ ](#After_SuccessAndAfter_Failure)

#### after\_success and after\_failure

If you use the after\_success or after\_failure tags, one or the other
of them will run after the [script](#Script) tags depending on if the
build was a success or a failure. **Build errors are not caught**.

    after_success:  - echo Yay!after_failure:  - echo Oops?

|

YAML

[ ](#Build_Targets)

#### build\_targets

These files will be uploaded to your Anaconda Cloud package. These are
files that will be uploaded to Anaconda Cloud with [anaconda
upload](/cli.html#Upload).

You may use the key words `conda` or `pypi`:

    build_targets: conda

Or a file or glob of files:

    build_targets: /opt/anaconda/my-package.tar.bz2

|

YAML

[ ](#Platform)

#### platform

This selects the platforms for which you wish to build your packages.

**Please note:** by default only `linux-64` build-workers are available
for public use on Anaconda Cloud. You can [add your own build
workers](#LaunchingABuildWorker) if you need access to additional
platforms.

To see which platforms are available to you, issue the [anaconda build
queue](/cli.html#Queue) command:

    $ anaconda build queueUsing anaconda-server api site https://api.anaconda.org build/binstar/public           [] + Worker hostname:docker-2        platform:linux-64        dist:centos   - Id 54b57d3ee1dad10a4987f6cd   - Last seen 5 seconds ago   - binstar-build v0.10.3 (binstar v0.10.1) + Worker hostname:docker-2        platform:linux-64        dist:centos   - Id 54b989d1e1dad10da34074d6   - Last seen 10 seconds ago   - binstar-build v0.10.3 (binstar v0.10.1)

|

Bash

The anaconda-build cli has the capacity to support the following
platforms:

    platform:  - linux-32  - linux-64  - osx-32  - osx-64  - win-32  - win-64

|

YAML

The items in the `platform` tag describe the first of the three axes of
the [build matrix](#BuildMatrix).

[ ](#Engine)

#### engine

Sets the initial conda packages you want to build with:

    engine:  - python=2 nodejs=0.10  - python=3

|

YAML

Note that the first item `python=2 nodejs=0.10` is not a list. In this
build item both packages python and nodejs will be available.

The items in the `engine` tag describe the second of the three axes of
the [build matrix](#BuildMatrix).

The environment variables CONDA\_PY and CONDA\_NPY are set based on the
presence of Python or numpy in the engine tag.

[ ](#Env)

#### env

An export of environment variables for the sub-build:

    env:  - FOO=BAR  - ANACONDA=GREAT JENKINS=OK

|

YAML

The items in the `env` tag describe the third of the three axes of the
[build matrix](#BuildMatrix).

[ ](#Install_Channels)

### install\_channels

If any channels need to be added to conda for the installation, they can
be included in install\_channels.

This shows the install\_channels configured for building R packages.

    install_channels:   - r   - defaults

|

YAML

If private packages are required in your build, make sure to include a
[token](reference.html#Token) in the channel configuration.

This shows the install\_channels configured for building a package that
depends on jsmith's private packages.

    install_channels:  - t/TOKEN/jsmith  - defaults

|

YAML

[ ](#Quiet)

### quiet

The `quiet` key in `.binstar.yml` can reduce the amount of superfluous
printing to the build logs. For example, if you see installation
messages similar to the following ones in your build log, you can redact
these messages by using the `quiet` key.

    Fetching packages ...    ncurses-5.9-1.   0% |                              | ETA:  --:--:--   0.00  B/s    ncurses-5.9-1.   2% |                               | ETA:  0:00:00  36.09 MB/s    ncurses-5.9-1.   4% |#                              | ETA:  0:00:00  54.15 MB/s    ncurses-5.9-1.   6% |##                             | ETA:  0:00:00  66.78 MB/s    ncurses-5.9-1.   9% |##                             | ETA:  0:00:00  76.02 MB/s

|

Text only

More specifically, the following usage of `quiet` in the `.binstar.yml`
file will redact from the build log any message that ends with `\r`:

    quiet: True

|

YAML

[ ](#BuildMatrix)

### Build matrix

When you submit one `.binstar.yml` file many sub-builds are launched,
one for each combination of the values of the [platform](#Platform),
[engine](#Engine) and [env](#Env) tags.

The build matrix is formed by combining `[platform * engine * env]` to
get the sub-builds.

The following configuration will run 8 sub builds:

    platform:  - linux-32  - linux-64engine:  - python=2  - python=3env:  - CXX=g++  - CXX=clang++

|

YAML

1.  platform: `linux-64` engine: `python=2` env: `CXX=g++`
2.  platform: `linux-64` engine: `python=2` env: `CXX=clang++`
3.  platform: `linux-64` engine: `python=3` env: `CXX=g++`
4.  platform: `linux-64` engine: `python=3` env: `CXX=clang++`
5.  platform: `linux-32` engine: `python=2` env: `CXX=g++`
6.  platform: `linux-32` engine: `python=2` env: `CXX=clang++`
7.  platform: `linux-32` engine: `python=3` env: `CXX=g++`
8.  platform: `linux-32` engine: `python=3` env: `CXX=clang++`

[ ](#MultipleBuildMatrices)

#### Multiple build matrices

Sometimes it is not best to define one large build matrix. For example,
if you are running a build on Windows, the matrix:

    platform:  - win-32  - linux-32env:  - MSVC=2008  - MSVC=2010  - CC=gccscript:    build.sh

|

YAML

would not work, because the configurations
`platform: linux-32 env: MSVC=2008` and
`platform: linux-32 env: MSVC=2010` don't make sense. Instead, you can
concatenate sub-builds using [yaml document
separators](http://yaml.org/spec/1.0/#id2489959).

Yaml documents are separated by `---`.

    platform: linux-32env: CC=gccscript: build.sh--- # New Build Matrixplatform: win-32env:  - MSVC=2008  - MSVC=2010script: build.bat

|

YAML

This would now produce the correct sub-builds.

[ ](#ExcludingAnItemInTheMatrix)

#### Excluding an item in the matrix

You can exclude a sub-build entry from a matrix with the exclude tag.

    platform:  - linux-32  - linux-64engine:  - python=2  - python=3script: conda build .---platform: linux-32engine: python=3exclude: true

|

YAML

Now the sub-build: `platform: linux-32 engine: python=3` will not be
submitted.

[ ](#EnvironmentVariables)

### Environment variables

BINSTAR\_BUILD

:   The build number as MAJOR.MINOR

BINSTAR\_BUILD\_MAJOR

:   The major build number

BINSTAR\_BUILD\_MINOR

:   The minor build number

BINSTAR\_ENGINE

:   the engine from the engine tag

BINSTAR\_PLATFORM

:   the platform from the platform tag

BINSTAR\_BUILD\_RESULT

:   This is set after the [script](#Script) tag is run

CONDA\_PY

:   The conda python version from the engine tag

CONDA\_NPY

:   The conda numpy version from the engine tag

[ ](#BuildWorkers)

Build workers
-------------

This section contains advanced information on configuring builds on the
[Anaconda Cloud](http://anaconda.org) platform. If you are not already
familiar with the build process, begin by reading this guide on [how to
submit a build](#SubmitABuild).

NOTE: Anaconda build defaults to the linux-64 platform, and [Anaconda
Cloud](http://anaconda.org) provides free linux-64 workers. If you do
**not** need to build for other platforms, you can complete package
builds using only [Anaconda Cloud](http://anaconda.org). Further, all
Anaconda Cloud accounts allow you to attach one free worker. If you need
more workers or workers on other platforms, you will need to [create an
organization](/using.html#CreatingOrganizations) and [upgrade to a paid
plan](https://anaconda.org/about/pricing).

Anaconda build workers allow you to run your builds on your own
machines. A build worker can run on any machine that supports bash
(posix) or batch (win32).

To follow along with this tutorial, you will need to [install the build
cli](/using.html#InstallingAnacondaClientAndAnacondaBuild).

[ ](#CreateABuildQueue)

### Create a build queue

The first thing you will need to do is create a build queue. A build
queue holds submitted builds until a build worker is ready to remove the
build and run it. At present, when you submit a job the default build
queue is `binstar/public`.

To create your queue run:

    anaconda build queue --create USERNAME/QUEUENAME

|

Bash

Where `USERNAME` is your [Anaconda Cloud](http://anaconda.org) username
and `QUEUENAME` is an alphanumeric name of your choice. For more
information see [configuring your build
queues](#ConfiguringBuildQueues).

[ ](#LaunchingABuildWorker)

### Launching a build worker

Before you can begin using the queue you created, you will need to
attach a build-worker to the queue. The basic build worker runs on your
machine (Linux, OS X or Windows) as the current user (see [security
considerations](#SecurityConsiderations)) and accepts jobs from the
build queue that you specify.

In order to avoid the build-worker waiting on user input for conda
commands, conda must be configured not to prompt for confirmation. Run
the following command to set the configuration correctly:

    conda config --set always_yes true

|

Bash

A worker needs to be registered before it can be run. This command
registers a worker for the queue USERNAME/QUEUE and outputs the worker's
id and other arguments to a yaml file in \~/.workers/ with the worker's
id as the yaml filename.

    anaconda worker register USERNAME/QUEUE

|

Bash

To see other options for registering workers, try

    anaconda worker register --help

|

Bash

The register step should print out a worker id you can use to run a
worker. This command will start a worker with a `worker_id`:

    anaconda worker run <worker-id-from-register-step>

|

Bash

That's it! You can now submit a job to your queue and your new build
worker will pick it up and build it:

    anaconda build submit ./my-build --queue USERNAME/QUEUENAME

|

Bash

NOTE: You must leave your build worker process running in order to
submit builds to it. You may wish to attach build workers to your queue
using a nohup command or similar.

Finally, after killing the anaconda build worker process, it is required
to deregister the worker, unless you plan to start the worker again with
the same worker id and configuration. The deregister step can be done
with:

    anaconda worker deregister <worker-id-from-register-step>

|

Bash

If you need to deregister a worker, then check your Anaconda server
instance's /settings/build-queue page to remove the worker or list the
workers you have registered with this command:

    anaconda worker list

|

Bash

There is an option for listing only the workers registered from the
current hostname:

    anaconda worker list --this-host-only

|

Bash

Registered workers can also be filtered by queue or organization with
one of these commands:

    anaconda worker list --queue USERNAME/QUEUE

|

Bash

Or:

    anaconda worker list --org ORGNAME

|

Bash

Review all help for register, run, deregister, and list with:

    anaconda worker -h

|

Bash

[ ](#RunningWorkersInTheBackground)

### Running workers in the background

The [Chalmers process control
system](https://github.com/Anaconda-Server/chalmers) can be used to run
build workers in the background across all platforms. Please see the
readme file in that repository for further information.

[ ](#ConfiguringBuildQueues)

### Configuring build queues

By default your build worker will run builds on your `binstar/public`
queue. You may change this in two ways:

1.  Use the `--queue` option when issuing a `anaconda build` [submit,
    save or trigger](cli.html#SubmittingBuilds) command:

        anaconda build submit ./my-build --queue USERNAME/QUEUENAME

    |

    Bash

2.  Specify a default queue for your build workers. This will affect all
    builds for your account. You can do this by visiting
    [anaconda.org/settings/build-queue](https://anaconda.org/settings/build-queue)
    and clicking the **Set as Default** option for the queue you would
    like to use.

[ ](#ShareYourBuildQueue)

#### Share your build queue

Once a build queue is created, you can control who may submit jobs to
it. For build queues associated with an organization rather than an
individual user, the default behavior is that only organization owners
may submit jobs to the queue.

To share access to your queue:

1.  Navigate your browser to
    [anaconda.org/settings/build-queue](https://anaconda.org/settings/build-queue).
    If you are an owner in multiple organizations, be sure to select the
    correct one in the drop-down in the upper right corner of the page.
2.  Click on the \*\* icon of the queue you want to share.
3.  Add the user by name (individual accounts) or by group
    (organization accounts).

[ ](#SecurityConsiderations)

### Security considerations

Because build workers run on your machine, using the current user
account, there are a few security considerations associated with
launching a build worker. Remember the build worker runs user-defined
build scripts from the jobs that are submitted to it.

We recommend you:

1.  Consider who you are giving access to your build queue.
2.  Remember that the `anaconda build worker` builds are permanent, and
    make sure users cannot accidentally change the state of your
    build machine.

[ ](#ExecutingBuildsInADockerContainer)

### Executing builds in a Docker container

The anaconda build cli includes the ability to build in a docker
container:

    ::

> docker pull binstar/linux-64 anaconda worker register
> USERNAME/QUEUENAME \# prints worker-id anaconda worker docker\_run
> &lt;worker-id&gt; --image binstar/linux-64

|

Bash
