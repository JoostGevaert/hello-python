#!/bin/bash

# Purpose of this bash script: Force git to change line endings to LF
# When this problem occurs: When code is contributed cross-platform and/or when not all Windows contributers have correct git config core.autocrlf settings
# IMPORTANT: after force-fixing the line endings, create a .gitattributes file in the repo. This ensures line endings consistency in the future.
# How to use this script: create a fixle.sh file, paste this in and run it with bash (Window's git bash, WSL's bash, or Mac/Unix's bash).
# Source: https://gist.github.com/ajdruff/16427061a41ca8c08c05992a6c74f59e
# Explanation: https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/

#Set LF as your line ending default.
git config --global core.eol lf

#Set autocrlf to false to stop converting between windows style (CRLF) and Unix style (LF)
git config --global core.autocrlf false

#Save your current files in Git, so that none of your work is lost.
git add -A
git commit -m "Saving files before normalizing line endings"

# from https://stackoverflow.com/a/7068241
find . -type f -exec dos2unix {} \;

#Remove the index and force Git to rescan the working directory.
rm .git/index

#Rewrite the Git index to pick up all the new line endings.
git reset

#Show the rewritten, normalized files.
git status

#Add all your changed files back, and prepare them for a commit. This is your chance to inspect which files, if any, were unchanged.
git add -A
# It is perfectly safe to see a lot of messages here that read
# "warning: CRLF will be replaced by LF in file."

if test -f ".gitattributes"; then
    git add .gitattributes
else
    echo ".gitattributes does not exist. Create it!"
fi

#Commit the changes to your repository.
git commit -m "Normalize all line endings to LF"

#Revert core.eol setting to default
git config --global core.eol native
