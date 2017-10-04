# README 

The purpose of this repository is to develop a set of curriculum materials for a training course on Continuum products. 

Initially, this content will be focused on the needs of one particular client, but hopefully can be reused for future training.

# Environment Set-up

* For both students and trainer, see the `../setup/` directory.
* Run the commands found in [../setup/SETUP_WINDOWS.txt](../SETUP_WINDOWS.txt) or [../setup/SETUP_LINUX_AND_MAC.txt](../SETUP_WINDOWS.txt) 

# Developer Files

For each topic area, such as `Conda/` there is a sub-directory call `dev/`, e.g. `Conda/dev/` that contains files for use by Trainers and Developers, but not to be distributed to students or clients. The `$root/dev/create_student_bundle.sh` prunes out all `dev/` directories and their contents when creating a ZIP archive of the training material.

# Course Plans

For each topic area, such as `Conda/` there is a `PLAN` file in the `dev/`  that detail which files to use and in what order, when teaching a particular section.
 
See the overview [./PLAN.md](./PLAN.md) to the root level or the repo, and within each subdirectory, you will find a `PLAN.md` file for teaching each specific section.

# Course Topics

Topics and best people to contact with questions:

* Conda: training team
* Navigator: David
* Numba/Accelerate: Stan, Siu 
* IOPro: Stan, Siu
* Anaconda Enterprise Notebooks: Ian Stokes-Rees, Duane Lawrence
* Anaconda Repository: Derek Ludwig, Duane Lawrence
* Bokeh: training team, Bryan, Fabio, bokeh-geo examples from Brendan
* DataShader: Bednar, Albert 
* Cluster: Kris Overholt


See [dev/TOPICS.md](./TOPICS.md) for detailed topic listing, subtopics, and material development status.

See [./dev/NARRATIVE.md](./NARRATIVE.md) for ideas about organizing the course, motivating and connecting the material.

# Material Development

The official outline of topics that need to be trained to the initial client is maintained here: Check these regularly for updates:

* [WPE Training project docs on Google Drive](https://drive.google.com/drive/folders/0B3MLKrmM7TwvWElFRjdpZWVXdW8)
* [Initial Course Outline](https://drive.google.com/a/continuum.io/file/d/0B3MLKrmM7TwvRU1jbURMM041dk0/view)
* [Material Tracker](https://docs.google.com/document/d/1_22RUbLgYd8pu4QvteNNYVKY803n56Croy5FLBG76g0/edit)

See [./MATERIAL_DEVELOPMENT.md](./MATERIAL_DEVELOPMENT.md) for ideas about developing raw material into training presentation material.

# Developer Workflow

Just a suggestion, so we have a coordinated collaboration and avoid difficult merge conflicts:

* create issues, one or more feature branch per issue, and associate PRs
* coordinate over flow-doc in the "Curriculum Development" flow.
* Separate directories for each high-level topic on the outline
* Keep data files compartmentalized, e.g. `/topic_item/data/`, for example:
    * `/Bokeh/data/`
    * `/Accelerate/data/`
* Try to limit content on a PR to a single sub-directory
* Assign PRs to indicate who is working on those files, branches 


### Git Pre-Commit Hooks

To start development, make a fresh clone of the repository:

```bash
git clone git@github.com:ContinuumIO/training-products.git
```

After cloning the repository, the first thing to do is run the setup script.

```bash
./tools/setup-for-git.sh
```

This script will verify and set-up various parts of your git config, including:

* verify the name and email address to be used for this repository
* install a `pre-commit` hook to check all code cell outputs in notebook files

The test of code cells is put in place so as to abort any commit if code cells are found to have output.
This prevents us from checking in huge images and files that are harder to diff.

## Git Commit Guidelines

- Keep each commit related to a single topic/theme.
- Do not mix disparate types of changes into a single commit. Otherwise, if you introduce a bug, it is then harder to find, and harder to prune out.
- Make multiple commits instead by only adding one or a few files with `git add` before each commit.
- Commit messages are searchable, so make your messages useful for searches, e.g. use simple text tagging such as adding "[Documentation]" or "[Numpy]" to your commit messages so that you can search for them, e.g. `git log | grep "[Documentation]" | wc -l`
- Review Tim Pope's [guidelines for Git commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).
- If you are closing an issue, take advantage of some GitHub features, like the
  possibility of [closing issues by putting specific words in the commit
  message](https://help.github.com/articles/closing-issues-via-commit-messages/).
- Make sure any Jupyter notebooks have their output cells emptied before
  committing (see instructions above).

Your changes are now ready for review.

## Create an Issue and a Feature Branch

For minor changes, these steps may not be needed, but for major changes, especially those that could potentially break the course build, consider working on and testing on a feature branch rather than working directly on the master branch. Here's a simple feature branch work-flow to demonstrate:


1. Create an issue in the GitHub issue tracker for the repo:
  * describe the feature you wish to add or modify
  * assign to yourself if you're starting the work immediately

2. Create a new feature branch by branching off of `master`

  * feature branch naming convention is `username/feature_branch_name`, where
  *  `username` is your GitHub username and
  *  `feature_branch_name` is some short description of what you are trying to do.

```bash
git checkout master
git pull  # always update master before branching
git checkout -b username/feature_branch_name master
```


# Calico Extensions in Jupyter

When editing Jupyter notebooks, use the *calico* notebook extensions for:

* adding tables-of-contents
* rearranging sections en masse
* adding section numbers

To install the calico notebook extensions, run the following shell commands:

For the entire system:

```bash
download_path=https://bitbucket.org/ipre/calico/downloads
sudo jupyter nbextension install $download_path/calico-spell-check-1.0.zip
sudo jupyter nbextension install $download_path/calico-document-tools-1.0.zip
sudo jupyter nbextension install $download_path/calico-cell-tools-1.0.zip
```

Alternatively, to install just your current user account:

```bash
download_path=https://bitbucket.org/ipre/calico/downloads
jupyter nbextension install --user $download_path/calico-spell-check-1.0.zip
jupyter nbextension install --user $download_path/calico-document-tools-1.0.zip
jupyter nbextension install --user $download_path/calico-cell-tools-1.0.zip
```

To enable the notebook extensions run the following shell commands:

```bash
jupyter nbextension enable calico-document-tools
jupyter nbextension enable calico-cell-tools
jupyter nbextension enable calico-spell-check
```

If you get an error message like the following:

```
FileNotFoundError: [Errno 2] No such file or directory: '/Users/albert/.jupyter/nbconfig'
```

...then run the following commands instead: note only modify the options on the first command:

```bash
jupyter nbextension --generate-config enable calico-document-tools
jupyter nbextension enable calico-cell-tools
jupyter nbextension enable calico-spell-check
```

Finally, restart your Jupyter notebook and the calico toolbar should appear at the top of every Jupyter notebook you open.

These steps only need to be done once in order that the calico tools be enabled for all Jupyter notebook sessions.

--
