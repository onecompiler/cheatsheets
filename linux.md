---
title: Unix/Linux commands
description: Git is a version-control system for tracking changes in computer files and coordinating work on those files among multiple people
created: 2018-07-18
updated: 2018-07-18
---

## Files
```sh
ls              # list all files
ls -al          # lists hidden files
cd <path>       # change directory to path
cd              # change to home
pwd             # shows current directory
mkdir <dirName> # create a new directory with given name
rm <fileName>   # removes file with given name
du -sh *        # list directories with their total sizes 
df -h           # to see free disk space
```

## tar/zip
tar -zcvf foo.txt.tar.gz foo.txt
tar -xvf foo.txt.tar.gz
