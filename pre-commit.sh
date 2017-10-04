#!/bin/sh
set -o pipefail
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

# Redirect output to stderr.
exec 1>&2


top_dir="${GIT_DIR}/../"

# get the list of copied, added, modified .ipynb files
# deleted files are ignored
# any files or directories listed in $top_dir/.nocheck will be ignored
files=`git diff-index --name-only --diff-filter=ARCM --cached HEAD -- "*.ipynb" | awk -v top=$top_dir '{printf "%s%s",top,$1; for(i=2;i<=NF;i++) printf " %s",$i;print ""}'`

# if no .ipynb are going to be committed
# let the commit proceed
if [ $? -eq 1 ]
then
  exit 0
fi

ret=0

#check that the output has been stripped
$top_dir/check_output.py $files
let ret="ret + $?"

exit $ret
