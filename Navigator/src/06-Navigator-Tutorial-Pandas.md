![toolbar](img/anaconda-logo.png)

# Using Anaconda Navigator with Pandas

Pandas is a common data science tool in Python for data manipulation and
analysis. In this how-to we'll show you how to use Anaconda Navigator to
set up and begin working with Pandas in your choice of Terminal, Python,
IPython, or Jupyter Notebook. The steps are similar for installing and
opening nearly any package.

## Who is this for?

Anyone who wants to easily install and configure collections of python
packages for analytics using a simple GUI tool, Anaconda Navigator.

## Before you start

You should already have Anaconda installed. Navigator is
automatically installed when you install or update Anaconda. If you have
an older version of Anaconda, update with the command
`conda update anaconda`.

## Summary of steps

1.  Open Navigator and go to the Environments tab.
2.  Create a new environment.
3.  Install Pandas in the new environment.
4.  Begin working with Pandas in your choice of Terminal, Python,
    IPython, or Jupyter Notebook.

# Instructions

1.  Open Anaconda Navigator. Look on your desktop or your programs menu
    for “Navigator” and click it to open. You will see Navigator has
    four left tabs: Home, Environments, Learning and Community. Click
    Environments to open that tab.
2.  Create a new environment. In your list of Anaconda environments
    select “Create” (if this is your first time creating an Anaconda
    environment, you will see only root in your environment list as
    shown in the screenshot below.)

![image](img/navigator-pandas1.png)

When prompted, give the environment a descriptive name like Pandas, and
select a Python version to run it. In this screenshot we have selected
Python 2.7.

![image](img/navigator-pandas2.png)

Now your new environment named Pandas appears in the list below root. To
begin managing your new environment, select it by clicking the name so
that it is highlighted with a green background.

Now that you have selected your environment, in the right-hand pane you
can see a list of all packages installed in that environment. As shown
at the bottom of the screenshot below, there are currently 59 packages
in the Pandas environment.

![image](img/navigator-pandas3.png)

3.  Install Pandas in the new environment. If you were to search this
    new environment for the Pandas Python package in the “Search” box in
    the upper right, it would return no results. Try it if you like.

To install Pandas into this environment, from the drop down menu above
the Packages pane, select “ALL” to search for it in all channels. See
the screenshot below.

![image](img/navigator-pandas4.png)

Now when you type Pandas in the search box, it will appear as a package
available for installation.

![image](img/navigator-pandas5.png)

Select this package by clicking on the package name, and put a check
next to the name "pandas" to mark it for installation. Next you select
the version. For the purposes of this example, let’s install a specific
version, 0.17.1 (optional).

![image](img/navigator-pandas6.png)

Now that you have selected the version, two buttons appear below the
Packages pane: Apply and Clear. To finish the installation, click the
Apply button.

![image](img/navigator-pandas7.png)

As Navigator begins installing Pandas and all of its dependencies, a
progress bar appears at the bottom below the Packages pane. This can
take a moment as it locates and installs these dependencies.

After the installation process is complete, your new environment is
immediately ready for your use.

4.  Begin working with Pandas. To begin using your new environment,
    click the left Environments tab to go back to the Environments pane,
    then click on the small button next to the environment name. This
    allows you to begin working with Pandas in your choice of Terminal,
    Python, IPython, or Jupyter Notebook. Refer to the documentation for
    each of those programs for more help.

![image](img/navigator-pandas8.png)

# Learn More about Pandas

-   10 Minutes to Pandas:
    <http://pandas.pydata.org/pandas-docs/stable/10min.html>
-   Pandas Cookbook:
    <http://pandas.pydata.org/pandas-docs/stable/cookbook.html>

# Additional help

If you have any problems, please feel free to reach out for help from
the community on the [Anaconda mailing
list](https://groups.google.com/a/continuum.io/forum/#!forum/anaconda).

## Anaconda Navigator documentation

See the complete [Anaconda Navigator documentation](navigator) for
detailed instructions and tutorials.

## Bug reports

If at any point you think you have found a bug, feel free to create an
issue in the [Anaconda Issues repository](https://github.com/ContinuumIO/anaconda-issues).

