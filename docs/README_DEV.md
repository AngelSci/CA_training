# README_DEV

This README contains the development set-up and workflow guidelines for contributing to repository.

## Python Environment

Use the environment file `environment_py35.yml` to generate a conda environment called `coursework_py35`.

```bash
conda env create -f environment_py35.yml
source activate coursework_py35
```

## Git Pre-Commit Hooks

To start development, make a fresh clone of the repository:

```bash
git clone git@github.com:ContinuumIO/training-course-intro.git
```

After cloning the repository, run the setup script.

```bash
cd ./training-course-intro
./setup-for-git.sh
```

This script will verify and set-up various parts of your git config, including:

* verify the name and email address to be used for this repository
* install a `pre-commit` hook to check all code cell outputs in notebook files

The test of code output cells is put in place so as to prevent a commit if code cells are found to have output. This prevents us from checking in large images and files that are harder to diff.

## Create an Issue and a Feature Branch

For minor changes, these steps may not be needed, but for large changes and new feature or content development, working and testing on a feature branch is ideal, rather than working directly on the master branch. Here's a simple feature branch work-flow to demonstrate:


1. Create an issue in the GitHub issue tracker for the repository:
  * a single issue can be used to track multiple feature branches that contribute to the same feature development.
  * describe the feature you wish to add or modify
  * assign to yourself if you're starting the work immediately

2. Create a new feature branch by branching off of `master`
  * Do this in your local clone of the repository
  * feature branch naming convention is `username/feature_branch_name`, where
      *  `username` is your GitHub username and
      *  `feature_branch_name` is some short description of what you are trying to do. 
      *  Helps to put an issue number in the name, so branch clean up is easier.
      * example: `vestuto/issue_99_update_readme`.
  * Notice, there's nothing special about the username or the `/`, it's just a convention for the humans to keep things sorted. Git doesn't care.

```bash
git checkout master
git pull  # always update master before branching
git checkout -b vestuto/issue_99_update_readme master
```

## Basic Git Process: Edit/Add/Commit/Push

Make your changes and commit them to your local feature branch.

For example, say you change files `file1`, `file2`.

```bash
# Make changes to files
echo "Hello World" >> file1
echo "Goodnight Moon" >> file2

# Make sure you know your branch and your status
git status
git branch -av

# Stage your changes to the index tree
git add file1 file2

# Make a commit.
# Editor will open: Write your message, save, and close editor
git commit

# Push commits to GitHub (use `-u` only for initial push)
git push -u origin vestuto/issue_99_update_readme
```

After the first push, create a PR on the GitHub webpage for the repo.

* Shortly after you have pushed a new branch, when you next visit the GitHub page for the repo, a option will appear to create a new pull request for the feature branch. 
* Create the PR, Update the description, and assign it to yourself.
* When you are ready for someone else to review and potentially add commits to the branch, assign the PR to them.
* Use PR assignment and personal communication to avoid ugly merge conflicts.

## Git Commit Guidelines

- Keep each commit related to a single topic/theme. Chunk your commits so that if you need to undo one change, you don't have to untangle it from others that aren't related.
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


## Reviewing a Feature Branch

Assuming someone else has created a feature branch called `vestuto/issue_99` and pushed it to a repo on GitHub. The following section demonstrates how to pull their feature branch into your local git repository so you can test it locally.

If there is a PR, make sure you coordinate with the author to avoid ugly merge conflicts. Use the RP assignment to indicate who is currently working on the branch.

### Simple recipe:

1. Fetch all branch updates: `git fetch --all`
2. Find the name of the branch to review: `git branch -rv`
3. Setup local tracking and checkout the feature branch to review: `git checkout vestuto/issue_99`

### Detailed recipe:

1. Update your local repo, fetching all feature branches

    ```bash
    git fetch --all
    ```

2. Inspect the remote tracking branches to make sure the feature branch is there

    ```bash
    git branch -rv
    ```

3. Create a local tracking branch to track the remote tracking branch.
   This step is not required unless you have branch name collisions

    ```bash
    git branch --track vestuto/issue_99 remotes/origin/vestuto/issue_99
    ```
4. Confirm that your local branch is tracking the remote branch

    ```bash
    git branch -vv
    ```

5. Checkout the local tracking branch

    ```bash
    git checkout vestuto/issue_99
    ```

6. Diff the local feature branch against the local master branch

    ```bash
    git diff master vestuto/issue_99
    ```

7. If this review is part of a merge request, and you have finished reviewing the feature branch, go to GitHub and approve merge request.

8. If after your initial review, the original developer of the feature pushes additional updates to the feature branch, you need to fetch all those updates and merge them form your remote tracking branch into your local tracking branch to review them:

    ```bash
    git fetch --all
    git checkout issue_99
    git merge origin/vestuto/issue_99 vestuto/issue_99
    ```
9. Once the merge request has been approved on the remote server, that feature branch will be merged into master branch, and then deleted. After this happens, you'll want to prune the feature branch from your local repository:

    ```bash
    git fetch --prune
    git branch -d vestuto/issue_99
    ```

## Clean up After Merge

If you have not been cleaning out old merged features branches that no one uses anymore, here's how:

```bash
# Delete local branches that have been merged
git branch -D $(git branch --merged | tail -n +2)

# Clean out local repo remotes no longer on origin
git remote prune origin
```

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

