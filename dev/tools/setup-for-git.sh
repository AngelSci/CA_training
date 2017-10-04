#!/usr/bin/env bash

# Run this script to set up your clone of ContinuumIO/Training for development.

# Set up user name and email address
setup_git_user() {
  read -ep "Please enter your full name, e.g. 'John E. Doe': " name
  echo "Name: '$name'"
  git config user.name "$name"
  read -ep "Please enter your email address, e.g. 'john@doe.com': " email
  echo "Email address: '$email'"
  git config user.email "$email"
}

# Infinite loop until confirmation information is correct
for (( ; ; ))
do
  # Display the final user information.
  gitName=$(git config user.name)
  gitEmail=$(git config user.email)
  echo "Your commits to this repo will have the following author information:

  $gitName <$gitEmail>
"
  read -ep "Is the name and email address above correct? [Y/n] " correct
  if [ "$correct" == "n" ] || [ "$correct" == "N" ]; then
    setup_git_user
  else
    break
  fi
done


# Make sure we are inside the repository.
cd "$(echo "$0"|sed 's/[^/]*$//')"


##setup the hooks
gitroot=`git rev-parse --git-dir`
echo
echo "Copying the pre-commit.sh script"
set -x
cd $gitroot/hooks
ln -s ../../tools/pre-commit.sh $gitroot/hooks/pre-commit
set +x



cat << EOF

Setting up some useful git aliases for you. This can be used by typing git and
the alias name. You can inspect all aliases in this script, or by reading
.git/config in your clone.

  prepush          - view a short form of the commits about to be pushed,
                     relative to origin/master

EOF

git config alias.prepush 'log --graph --stat origin/master..'
git_branch="\$(git symbolic-ref HEAD | sed -e 's|^refs/heads/||')"

