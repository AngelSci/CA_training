![toolbar](img/anaconda-logo.png)

# Anaconda Navigator: Introduction

## What is Navigator?

**Anaconda Navigator** is a desktop graphical user interface included in Anaconda that allows you to easily manage **conda packages, environments and channels** without the need to use the command line.

A **conda package** is a compressed file that contains system-level
libraries, Python or other modules, executable programs, or other
components. Examples of conda packages pre-installed in Navigator
include Jupyter Notebook, QTConsole, and Spyder. Hundreds more can be
installed following the instructions below.

A **conda environment** is a directory that contains a specific
collection of conda packages that you have installed. For example, you
may have one environment with NumPy 1.11 and its dependencies, and
another environment with NumPy 1.10 for testing. If you change one
environment, your other environments are not affected.

A **conda channel** is a URL to directories containing conda
packages. The same package with the same version number from two separate channels need not be the same: custom binaries may have been compiled in a unique way that differs from how a conda package of the same name was built in another. Be mindful of which channel you are installing from!


## System Requirements

-   Navigator supports the same platforms that the Anaconda Distribution
    supports, including Windows XP and newer 32 or 64-bit, Ubuntu or
    Kubuntu 14.04 32-or 64-bit, or OS X 64-bit
-   Python 2.7, 3.4 or 3.5

```bash
# Check your Python version:
import sys
sys.version
```

## How to get Anaconda Navigator

Anaconda Navigator is automatically installed when users download and
install Anaconda.

If you already have Anaconda or Miniconda running on your system, you
can install Anaconda Navigator with the following command:

```bash
conda install anaconda-navigator
```



# Using Anaconda Navigator

## Starting Navigator

When you install Anaconda, an **icon to launch Anaconda Navigator** is automatically added to your programs menu and/or your Desktop.

It is also possible to launch it from a **terminal or command prompt** with
the following command:

```bash
anaconda-navigator
```

## Updating Navigator

Every time Anaconda Navigator starts it checks if a new version is
available. If it finds a new one a dialog box will pop up where you can
chose to update or keep your current version.

## Navigator Interface

When you first start Navigator, you will see the **Home**, but there are other components. Each one can be selected by clicking the corresponding tab on the left-hand column:

-   **Home** where you can install, upgrade, and launch applications.
-   **Environments** allows you to manage channels, environments
    and packages.
-   **Learning** shows a long list of learning resources in several
    categories: webinars, documentation, videos and training.
-   **Community** where you can connect to other users through events,
    forums and social media

## Home

The **Home** page displays a grid of applications that are available to
manage with Navigator. Each has a gear icon in the top right corner to
**Update**, **Remove**, or **Install a specific version** of that
application.

The first time you open Navigator, three popular Python apps are already
installed: [Jupyter
notebook](https://jupyter.readthedocs.org/en/latest/),
[qtconsole](https://ipython.org/ipython-doc/3/interactive/qtconsole.html),
and [Sypder](https://pythonhosted.org/spyder/).

![image](img/navigator-home.png)

**NOTE:** Applications installed and launched from the Home tab are
installed into the environment named "root".

With conda you can create, export, list, remove, and update environments
that have different versions of Python and/or packages installed in
them. Switching or moving between environments is called **activating**
the environment.

## Environments

The **Environments** tab allows you to manage installed environments,
packages and channels. The left column lists the environments. The right
column lists packages for the current environment; depending on the
selected option it can show *Installed*, *Not Installed*, *Upgradable*,
*Downgradable* and *All* packages.

![image](img/navigator-environments.png)

-   **Activate** or start up an environment. First you have to select it
    by clicking its name from the left column list of environments then
    click its "Start" icon. From the drop-down box that appears, choose
    whether to Open the environment in a Terminal window, Open in a
    Python interpreter, Open with a Jupyter Console or Open with a
    Jupyter Notebook; this will activate the environment and run the
    selected option.
-   **Search** environments on your computer by typing its name in the
    *Search Environments* box. Incremental search will show those whose
    name partially matches the current text in the search box.
-   **Create** a new environment by clicking the *Create* button, then
    give it a descriptive name, optionally select a version of Python,
    and click the *Ok* button.
-   **Clone** a copy of an existing environment by selecting its name,
    giving the new environment a descriptive name, then clicking the
    *Clone* button.
-   **Remove** an environment by selecting it, then clicking the
    *Remove* button.
-   **Manage Packages** using the filtering options. *Installed* and
    *Search Packages* filter the list so only those packages already
    installed which match the text in the search box will show up. A
    different set of packages will appear depending on the option
    selected from the drop-down box: *Not Installed*, *Upgradable*,
    *Downgradable* or *All*. A partial incremental search is performed
    on the package names and the package descriptions. The tick box to
    the left of each package can be used to mark it for installation,
    removal, or reinstallation to another specific version. After
    marking the packages to be modified click *Apply* to make the
    changes or *Clear* to reset all marks.
-   **Channels** See a list of channels. From the dialog you can *Add*
    or *Remove* and *Update channels*. **NOTE:** The changes here affect
    the whole conda installation and not just the selected environment.
-   **Update package index...** updates the list of all packages which
    are available in any of the enabled channels. Each of these packages
    may be installed into any environment.

To learn more about advanced package, environment and channel management
from a terminal see their corresponding documentation:
[packages](http://conda.pydata.org/docs/using/pkgs.html),
[environments](http://conda.pydata.org/docs/using/envs.html).

***TIP:*** If there are misaligned elements or if after installing a new
application or package it doesn't appear select the Home tab and click
the ***Refresh*** button on the top right to reload the interface.

## Learning

Learn more about Anaconda Navigator, the Anaconda platform, and open
data science. Select *Webinars*, *Documentation*, *Video*, and/or
*Training*, then click any item to have it open in a browser window.

![image](img/navigator-learning.png)

## Community

Learn more about the events, forums and social networking relating to
Anaconda Navigator. Select *Events*, *Forum* and/or *Social*, then click
any item to have it open in a browser window.

***TIP:*** Join the Anaconda forum to get help from the community in
learning Anaconda and Anaconda Navigator.

![image](img/navigator-learning.png)

For free community support, please considering joinning the [Anaconda Mailing List](https://groups.google.com/a/continuum.io/forum/?fromgroups#!forum/anaconda).

Please report bugs on the [Anaconda GitHub issue
tracker](https://github.com/ContinuumIO/anaconda-issues/issues).

## Anaconda Navigator Menu

Additional controls are available through your system menu bar for the application.

-   Depending on your system (Windows, OS X, Linux) and version of Anaconda, the additional controls may appear under a Menubar labeled either **File** or **Navigator**.
-   **File -&gt; Preferences** (or e.g. **Navigator -&gt; Preferences** on OS X) allows you to reset the Anaconda API
    domain and conda domain, allows you to select or deselect whether to
    provide personally non-identifiable information to help improve the
    product, and to select or deselect whether to show
    application environments. These preferences may all be reset back to
    defaults by clicking the *Reset to defaults* button.
-   **File -&gt; Quit** to exit Navigator. A confirmation dialog box
    will appear, there you can tick the *Don't show again* box to exit
    without confirmation the next time.
-   **Help -&gt; Online Documentation** Links to this documentation,
    which can be accessed from any web browser. Help -&gt; About
    Displays information about Anaconda Navigator, including a link for
    bug reports and feature requests. Help -&gt; Logs Viewer allows you
    to review the logs of everything you have done in Anaconda Navigator
    since you started this session. There are two or more files that can
    be selected from the drop-down list: *navigator.log* that refers to
    the actual application logs and *condamanager.log* which refers to
    logs on the specific conda-manager component. As the application is
    used more log files are created with a number appended to the name.
    More recent log files have a higher number.
-   **Services** (OS X Only) Links to your computer’s system
    preferences menu.
-   **Hide Python** (OS X Only) Hides your Anaconda Navigator window.
-   **Hide Others** (OS X Only) Hides all windows except your Anaconda
    Navigator window.
-   **Show All** (OS X Only) Brings back all windows including your
    Anaconda Navigator window

## Sign in to Anaconda Cloud

For your convenience in locating packages and channels available only on Anaconda Cloud, sign in for seamless transition between your computer and Anaconda Cloud. 

![image](img/navigator-signin.png)

If you are already logged into Anaconda Cloud this appears as, “signed in as \[username\]”.


# Next Steps

The follow content is found in additional files within this lesson.

## Navigator Workflow

Learn the general steps of a Navigator workflow for creating environments, installing packages, and using them.

## Navigator Exercises

These are specific examples that demonstrate how Navigator can be used in a variety of analysis work flows.

## Navigator with Pandas

This is a specific demonstration of using Anaconda Navigator with the Pandas module for data analysis.

## Navigator Glossary

This glossary provides definitions and descriptions for all the terms used throughout this lesson.


--
***Anaconda Navigator is copyright 2016 Continuum Analytics, Inc. May be
copied and distributed freely only as part of an Anaconda or Miniconda
installation.***
