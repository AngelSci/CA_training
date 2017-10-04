![toolbar](img/anaconda-logo.png)

# Navigator Glossary


## Anaconda

A downloadable free, open source, high performance, optimized Python and
R distribution with 100+ packages plus access to easily installing an
additional 620+ popular open source packages for data science including
advanced and scientific analytics. 

It also includes conda, an open source package, dependency and environment manager. Thousands more open source packages can be installed with the **conda** command. Available for Windows, OS X and Linux, all versions are supported by the community.

## Anaconda Cloud

A web-based repository hosting service in the cloud. Packages created
locally can be published to the cloud to be shared with others. Free
accounts on Anaconda Cloud can publish packages to be shared publicly.
Paid subscriptions to Anaconda Cloud can designate packages as private
to be shared with authorized users.

## Anaconda Navigator

A desktop graphical user interface (GUI) included in all versions of
Anaconda that allows you to easily manage conda packages, environments,
channels and notebooks without the need to use the command line
interface (CLI).

## Anaconda Pro, Enterprise and Workgroup

Anaconda that includes enterprise technical support for a specific
number of users, and indemnification for a select number of open source
packages. 

Anaconda Enterprise and Workgroup include collaborative notebooks, high performance scalability, Hadoop, interactive visualization, governance and security. See the [product comparison](https://www.continuum.io/anaconda-subscriptions).

## Channels

The locations of the repositories where conda looks for packages. Channels may point to an Anaconda Cloud repository, a private location on a remote or local repository that you or your organization created. 

The conda [channel](http://conda.pydata.org/docs/custom-channels.html) command has a default set of channels to search beginning with <https://repo.continuum.io/pkgs/> which users may override, for example, to maintain a private or internal channel. These default channels are referred to in conda commands and in the `.condarc` file by the channel name 'defaults'.

## Command Line Interface (CLI)

A program in which commands are entered as text, one line at a time, for a computer to execute. Sometimes referred to as a terminal program. Contrast with Graphical User Interface (GUI).

## Conda

A package and environment manager program bundled with Anaconda that installs and updates conda packages and their dependencies. Also lets you easily switch between conda environments on your local computer.

## Conda configuration file `.condarc`

A conda configuration file or `.condarc` file is an ***optional*** runtime
configuration file which allows advanced users to configure various
aspects of conda, such as which channels it searches for packages, proxy
settings, environment directories, etc.

## Conda environment

A folder or directory that contains a specific collection of conda packages and their dependencies, so they can be maintained and run separately without interference from each other. 

For example, you may use one conda environment for only Python 2 and Python 2 packages, and maintain another conda environment with only Python 3 and Python 3 packages. 

Environments can be specified via the command line or via an environment specification file with the name `your-environment-name.yml`.

## Conda package

A compressed file that contains everything that a software program needs in order to be installed and run (including system-level libraries, Python modules, executable programs, and/or other components) so you do not have to manually find and install each dependency separately. Managed with conda.

## Conda repository

A cloud-based repository that contains 720+ open source certified packages that are easily installed locally via the `conda install` command. Can be accessed by anyone using conda commands, or viewed directly at <https://repo.continuum.io/pkgs/>

## Graphical User Interface (GUI)

A program with graphic images, icons and menus in which commands are
entered by clicking with a mouse and/or entering text in form boxes. It
is a pretty and easy to use overlay to the same program that is run
using a command line interface or CLI. Examples are
Anaconda Navigator and Anaconda Mosaic.

## Miniconda

A minimal installer for conda. Like Anaconda, Miniconda is a free software package that includes the Anaconda distribution and the conda ; package and environment manager, but Miniconda does not include any packages other than those dependencies needed to install it. 

After Miniconda is installed, additional conda packages may be installed directly from the command line with `conda install`. See also Anaconda and
conda.

## Repository

Any storage location from which software software assets may be
retrieved and installed on a local computer. See also
Anaconda Repository and conda repository.

