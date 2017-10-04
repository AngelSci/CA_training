# Anaconda Environments

## overview

Anaconda Enterprise Notebeooks runs on <a href="https://store.continuum.io/cshop/anaconda" target="_blank">Anaconda</a>.  Anaconda supports multiple versions of Python and associated packages.  An environment generally includes one version of Python and some set of associated packages.


### Creating
Use the conda utility to create new environments within your Anaconda Enterprise Notebeooks account. In Anaconda Enterprise Notebeooks, all new environments created with conda will automatically include python, ipython and pip. You will need to specify any other packages you want included in your new environment.

_Note: By default, conda will create the environment in your home directory.  If your new environment is in your home directory, it is only available to you.  If your new environment is on the project drive, then all team members will have access to it._

Examples:

To create a new environment named mypy with python, numpy, pip and ipython installed in your home directory:

	(Using the Terminal Application)
	[your_username@MyNewProject MyNewProject]$ conda create -n mypy numpy

	To make this new environment your default environment in your terminal:
	[your_username@MyNewProject MyNewProject]$ source activate mypy

    To deactivate this environment:
	[your_username@MyNewProject MyNewProject]$ source deactivate


To create a new environment named newenv with python, pip, ipython, numpy and scipy installed on your project drive:

	(Using the Terminal Application)
	[your_username@my-project my_project]$ mkdir envs
	[your_username@my-project my_project]$ conda create -p /projects/your_username/my_project/envs/newenv numpy scipy

    To make this new environment your default environment in your terminal:
	[your_username@my-project my_project]$ source activate /projects/your_username/my_project/envs/newenv

    To deactivate this environment:
	[your_username@my-project my_project]$ source deactivate

See the conda documentation for more information: <a href="http://docs.continuum.io/conda/index.html" target="_blank">conda</a>

### Customizing

If you need a Python module that Anaconda Enterprise Notebeooks doesn't include by default, you can easily install additional packages into your Anaconda Enterprise Notebeooks environments using standard tools.

_Note: You cannot install packages into the default Anaconda environment. You must create your own environment and install the new packages into that environment._

Anaconda Enterprise Notebeooks is built on Anaconda, so you have several options for installing additional Python modules: conda, pip, and easy_install.

conda is the package management tool that comes with Anaconda. With conda, you can install new modules or upgrade existing modules that are part of the Anaconda package library. See the [documentation](http://docs.continuum.io/conda/index.html) on conda for details.

If you prefer to use pip or easy_install, you can do so on the command line in Anaconda Enterprise Notebeooks just like you would on your local system. You can also uninstall using this method.


See this blog for more information: <a href="http://continuum.io/blog/wakari_custom_envs" target="_blank">Custom Python Environments in Anaconda Enterprise Notebeooks</a>.
