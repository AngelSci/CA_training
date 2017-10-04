![toolbar](img/anaconda-logo.png)

# What problem does Navigator solve?

* Many scientific packages require specific versions of programs in order
to run. 
* These other programs are called *dependencies*. 
* The Conda Package Management System, and now Anaconda Navigator, allow you to create isolated *environments* so the programs will not interfere with other programs you have created, and you can install the exact programs needed.

# Why use Navigator?

* For those who may prefer Graphical User Interface (GUI) over a Command Line Interface (CLI), Anaconda Navigator serves as an alternative to conda. 
* Anaconda Navigator is an easy, point-and-click way to use packages and
environments so you don't have to use Conda commands in a terminal
window. 
* You can use it to find the packages you want, install them in an
environment, and run the packages and update them, all inside Navigator.

# Navigator basic workflow

* Create and activate a new environment for the package you want to use.
* Search for and install the package you want.
* Open and use the package.

## Step 1: Create and activate a new environment for the package you want to use.

* Let's say your professor told you to get BioPython, a popular library
for biologists. 
* A quick online search reveals that, like most packages written in Python, it's available for Windows, OS X and Linux, 32-bit and 64-bit, and all versions of Python back to 2.6. 
* We'll create an environment using the newest version of Python, 3.5.

**NOTE:** Why choose Python 3.5? It's the latest and recommended version
of Python to use.

In Anaconda Navigator...

* go to the Environments side tab
* then click the bottom *Create* Button.
* The "Create new environment" dialog box appears:

![image](img/navigator-tutorial01.png)

* Give your environment a memorable name, here we called ours "biopy"
* Select Python 3.5
* Click the *OK* Button. 
* Navigator creates the new environment and activates (switches to) it, as shown by the highlighted green bar:

![image](img/navigator-tutorial02.png)

**NOTE:** All actions take place in the active environment, shown by the
highlighted green bar. In the above image the "biopy" environment is
active.

## Step 2: Search for and install the package you want.

Let's now search for the `biopython` package:

* Select *ALL* to search for all possible packages
* Then type the name of the package you want in the search box. 
* In the search results list, put a check next to the package you want to install:

![image](img/navigator-tutorial03.png)

From the drop-down menu that appears, select *Mark for installation*:

![image](img/navigator-tutorial04.png)

To begin installing, click the *APPLY* Button on the bottom right:

![image](img/navigator-tutorial04b.png)

When it asks you if you want to proceed, click the *OK* Button.

Anaconda Navigator gets all the dependent files you need and installs
them in your new environment.

## Step 3: Open and use the package.

Now let's use the package we've installed:

* On your "biopy" environment name which is still highlighted (if not,
click to highlight it)
* Click the arrow to bring up the menu of choices to open your package:

![image](img/navigator-tutorial05.png)

* Here we have selected *Open Terminal*.
* A terminal window will appear, type jupyter-notebook to open Jupyter Notebook in a new browser window or tab.

* To exit Jupyter Notebook...
    * close all notebook-related tabs or windows in your web browser
    * in the terminal displaying notebook messages, press **ctrl-c** and answer "Y" \[for "yes"\] to stop the
notebook process
    * then type exit and press "Enter" to exit the terminal.

--