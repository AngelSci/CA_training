# Jupyter Notebook Application

### Overview

The Jupyter Notebook application allows the creation and editing of documents that include both the input and output of a Python script.  Once created, these documents may be easily shared with others.
Documents are also discoverable within the Terminal and Workbench apps.  By default, Jupyter Notebooks are saved in the project directory and not your home directory.

![wakariui](img/jupyter_main.png)

_Note: Anaconda Enterprise Notebooks uses Jupyter notebook version 4.1.  Jupyter's documentation can be found <a href="http://jupyter.readthedocs.org/en/latest/">here</a>._

The Jupyter Notebook can be accessed from your project's main page, in the list of applications.

![wakariui](img/finding_ipython.png)

### Creating Notebooks

New notebook documents are created using the New Notebook button at the top right of the page.

Notebooks act as an in-browser Python environment, with syntax highlighting and output within the document.

Code written in each cell can be run by pressing shift and enter simultaneously.  Output will appear immediately below the code, and a new cell will appear below that.

![wakariui](img/sample_notebook.png)

Once created, notebooks will appear on the dashboard.  If you don't see it, use the Refresh button in the top right.

![wakariui](img/dashboard.png)

Opening the Terminal app, your created notebook will appear in the project directory.

![wakariui](img/terminal_notebook.png)

Finding your notebook is much the same in the Workbench.

![wakariui](img/workbench_notebook.png)

### Using the Notebook Extensions

Anaconda Enterprise Notebooks now provides some extensions helping the Jupyter notebook users to auto
synchronize their environments, lock the content of their notebooks, use a
simple revision control mechanism to achieve efficient versioning of their work
is a very simple way and interact with the conda and Anaconda ecosystem

####Synchronize your environments.

Now, we detect your environments at the notebook initialization and synchronize
those with the Jupyter machinery, letting us to offer you all these
environments as "kernel"-like options. In this way, you can change environments
inside a unique notebook session without the need to fire several instances
using each of your selected environments. You can also now trigger `R-kernels`
if your project environment have `R` installed.

![wakariui](img/extensions_kernels.png)

In Anaconda Enterprise Notebooks the "auto" kernel points to the new environment named `default`. 


####Locking

The multi-user capability in the Anaconda Enterprise Notebooks Enterprise experience is also present when multiple users try to work in the same notebook file. Because the Jupyter notebook does not have real-time collaboration yet, we work in a simple file-based locking mechanism to avoid overwriting between multiple users. In this way, a user can "lock" the notebook which is working on and if some other users try to save the notebook with their own changes, the save capability
will be disable, and they can not overwrite the locked notebook. They have to "steal" the lock just pressing a specific button in the toolbar.

![wakariui](img/extensions_locker.png)

**Note**: This is a "soft locking model", so everyone can take the lock and save their work.

###Revision Control Mechamism (RCM)

The revision control mechanism extension is a simple model to make version control over the ipynb files (Jupyter notebook files). It is a nbextension (js-based extension) actually using the internal Jupyter machinery to perform its tasks.

The model behind the extension is a simple "linear" model on the surface but a more complex git-based branched model under the hood. The "latest wins" strategy is used so there is no merging conflict by design.

![wakariui](img/extensions_rcm.png)

The RCM nbextension provides essentially 3 buttons to perform 3 actions:

* Status: This option let you know the revision point where you are now. Also, it lets you see a diff between the current revision point and the latest changes introduced by you, but not yet commited.

![wakariui](img/extensions_rcm_status.png)

* Checkout: This option trigger a modal view presenting you a tree-based view of the previous revision points (representing the evolution of your history) and give you 3 option:

    * Checkout a previous revision point. To do this, you have to select the desired revision point a press the "OK" button. That action will load the Jupyter notebook webapp with a "new" notebook file which is actually the "state" of that notebook in the selected revision point.
    * Make a diff comparison. If you select two previous revision points in the current modal view, you can make a diff using the selected points and the result will be presented as a diff view, after you press the "View diff" button.
    * Cancel, to close the current modal view.

![wakariui](img/extensions_rcm_checkout.png)

* Commit: This option lets you "commit" the current changes (I mean persist the changes in the current VCS supporting the extension, `git` in this case). In this way, you keep a permanent record of the changes introduced and you don't have to be worried about data/information lost. You have a new modal view asking for a commit message. After writing the message, you commit actually pressing the "OK" button.

![wakariui](img/extensions_rcm_commit.png)

**Note**: The diff functionality: it is actually difficult to diff the ipynb content because of the reason exposed above, but to partially avoid that problem the ipynb notebook  is "flattened" to get rid of some of the metadata information and be able to efficiently diff the actual cell content, keeping
some additional contextual info still present, ie. the cell prompt number. Then we use the python diff library to actual get the diff content and present the result to the user in a codemirror instance.

###Conda integration

We now provide a new extension called `nb_conda` provides Conda environment and package access extension from within Jupyter.

![wakariui](img/extensions_conda.png)

####Conda tab in the Jupyter file browser

This extensions adds a Conda tab to the Jupyter file browser. Selecting the Conda tab will display:

* A list of the Conda environments that current exist
* The list of Conda packages available in currently configured channels (http://conda.pydata.org/docs/config.html#channel-locations-channels)
* The list of packages installed in the selected environment.

You can click on the name of an environment to select it. That will allow you to:

* see the packages installed in the environment
* install new packages from the available package list
* check for updates on selected (or all) packages
* update selected (or all) packages in the environment.

####Creating New Environments

There are two ways to create an environment:

* Create a new environment Use the New Environment button at the top of the page, and select Python 2, Python 3, or R to create a base environment with the corresponding packages.
**Note**: if you want to run a Jupyter python kernel in the new environment, you must also install the ipykernel package in the environment.

* Clone an existing environment Click the clone button next to an environment in the list, and enter the desired name of the new environment.

####Conda in the Notebook view

This extension adds a Conda Packages item to the Kernel menu. Selecting this item displays the list of Conda packages in the environment associated with the running kernel, and the list of available packages. You can perform the same actions as in the Conda tab, but only against the current environment.

###Anaconda Cloud integration
You can now easily upload your notebook to Anaconda Cloud with a simple button at the notebook UI

![wakariui](img/extensions_anacondacloud.png)

Your AEN can be configured to upload to your Anaconda Enterprise Repository instead of Anaconda Cloud.