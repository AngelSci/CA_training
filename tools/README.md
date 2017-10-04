# Deep Dive Course
Follow the guidelines for [Generic Course Development](https://github.com/ContinuumIO/Training/wiki/Generic-Course-Development-Strategy)

## Lesson plans
See the [docs](./docs) directory.

## Notebooks
The notebooks are provided as self-paced lecture and exercise notebooks starting with [Visualization.ipynb](./Visualization.ipynb)

Use the provided [environment.yml](./environment.yml) file to generate a conda environment.

## Tools
The [tools](./tools) directory provides scripts for notebook maintenance and course delivery.

## Development Guidelines
The sections below indicate recommended practices for developing notebooks, making commits and submitting Pull Requests.

## Calico Extensions in Jupyter

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

### Git Pre-Commit Hooks

To start development, make a fresh clone of the repository:

```bash
git clone git@github.com:ContinuumIO/training-deepdive-visualization.git
```

After cloning the repository, the first thing to do is run the setup script.

```bash
cd ./training-deepdive-visualization
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
  * examples: `vestuto/issue_99` or `vestuto/improving_readme` or `vestuto/issue_99_improving_readme`.

```bash
git checkout master
git pull  # always update master before branching
git checkout -b username/feature_branch_name master
```
