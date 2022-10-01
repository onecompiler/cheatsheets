---
title: Git
description: Git is a version-control system for tracking changes in computer files and coordinating work on those files among multiple people
created: 2018-07-18
updated: 2022-10-01
---


### Configuration

```sh
git config --global user.email "foo@bar.com"        # Global user email
git config --global user.name "Foo Bar"             # Global user name

git config user.email "foo@bar.com"        # repo specific user email
git config user.name "Foo Bar"             # repo specific user name

git config --list                          # To check your settings
```

#### Create a repo

```sh
git init hello-world-repo
```

#### Clone a repo

```sh
git clone [url]
```

## Branches

```sh
git branch                  # list all local branches
git branch [branch-name]    # creates a new branch with given name
git checkout [branch-name]  # switch to given branch 
git merge [branch]          # merge the specified branch’s history into the current one
git log                     # Shows current branch's commit history
git log -p                  # Display the full diff of each commit
git log --stat              # Include which files were altered and the relative number of lines altered

```

## Commits 

```sh
git add .                           # Add all files
git commit -m "commit message"      # commit 
git status                          # Shows the modified files in working directory which are staged for next commit
git reset [fileName]                # Unstages file while retaining changes in present working directory
git stash                           # to keep uncommitted changes (both staged and unstaged) for later use
git reflog                          # Shows a log of changes to the local repository's HEAD
```

## Inspect 

```sh
git diff                            # Shows diff of what is changed but not staged
git diff --staged                   # Shows diff of what is staged but not committed
git diff branch2...branch1          # Shows diff of what is in branch1 that is not in branch2
git diff HEAD                       # Shows difference between working directory and last commit
git diff --cached                   # Shows difference between staged changes and last commit
```

## Update

```sh
git remote -v                      # to view see the actual URLs for each alias
git remote add [aliasName] [url]   # to create a new connection record to a remote repository with a local alias
git remote rm [aliasName]          # Removes aliasName
git fetch [alias]                  # to download contents from a remote repository
git push [remote] [branch]         # to upload local repository content to a remote repository
git push [remote] --force          # to forcefully upload your local repository content to remote, Use only when you are very sure
git pull                           # to update the local version of a repository from a remote
```

## Stash

```sh
git stash push "add style to our site"  # Save your local modifications to a new stash entry
git stash list                          # List the stash entries that you currently have
git stash pop stash@{0}                 # Remove a single stashed state from the stash list and apply it on top of the current working tree state
git stash clear                         # Remove all stashed entries
```

## Rebase main branch into feature branch

```sh
git checkout feature
git fetch origin main
git rebase origin/main
```

## Squash multiple commits into one
```sh
git rebase -i HEAD~4            # Squash last 4 commits. This command will open up default editor then replace "pick" on the second and subsequent commits with "squash".
git rebase --root -i            # Squash all commits. This command will open up default editor then replace "pick" on the second and subsequent commits with "squash".
```

## Semantic commit messages

```sh
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.

feat: (new feature for the user, not a new feature for build script)
fix: (bug fix for the user, not a fix to a build script)
docs: (changes to the documentation)
style: (formatting, missing semi colons, etc; no production code change)
refactor: (refactoring production code, eg. renaming a variable)
test: (adding missing tests, refactoring tests; no production code change)
chore: (updating grunt tasks etc; no production code change)
```

example:

```sh
feat(dev): prevent racing of requests

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.

Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Reviewed-by: Z
Refs: #123
```
