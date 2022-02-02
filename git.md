---
title: Git
description: Git is a version-control system for tracking changes in computer files and coordinating work on those files among multiple people
created: 2018-07-18
updated: 2021-02-02
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
```

## Commits 

```sh
git add .                           # Add all files
git commit -m "commit message"      # commit 
git status                          # Shows the modified files in working directory which are staged for next commit
git reset [fileName]                # Unstages file while retaining changes in present working directory
git stash                           # to keep uncommitted changes (both staged and unstaged) for later use
```

## Inspect 

```sh
git diff                            # Shows diff of what is changed but not staged
git diff --staged                   # Shows diff of what is staged but not committed
git diff branch2...branch1          # Shows diff of what is in branch1 that is not in branch2
```

## Update

```sh
git remote -v         # to view see the actual URLs for each alias
git remote add [aliasName] [url]       # to create a new connection record to a remote repository with a local alias
git remote rm [aliasName]                       # Removes aliasName
git fetch [alias]                  # to download contents from a remote repository
git push [remote] [branch]         # to upload local repository content to a remote repository
git push [remote] --force          # to forcefully upload your local repository content to remote, Use this command only when you are very sure
git pull                           # to update the local version of a repository from a remote
```
