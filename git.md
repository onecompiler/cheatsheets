---
title: Git
description: Git is a version-control system for tracking changes in computer files and coordinating work on those files among multiple people
created: 2018-07-18
updated: 2018-07-18
---


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
```

## Commits

```sh

 git add .                           # Add all files
 git commit -m "commit message"      # commit 

```

## MISC

```sh
git config --global user.email "foo@bar.com"        # Global user email
git config --global user.name "Foo Bar"             # Global user name

git config user.email "foo@bar.com"        # repo specific user email
git config user.name "Foo Bar"             # repo specific user name

git remote rm origin                       # Rmoves origin
git remote add origin https://github.com/foo/bar.git # Add origin
```
