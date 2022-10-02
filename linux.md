---
title: Unix/Linux commands
description: Git is a version-control system for tracking changes in computer files and coordinating work on those files among multiple people
created: 2018-07-18
updated: 2018-07-18
---

## Files
```sh
ls               # list all files
ls -al           # lists hidden files
cd <path>        # change directory to path
cd               # change to home
pwd              # shows current directory
mkdir <dirName>  # create a new directory with given name
cat <fileName>   # displays the file content
cat > <fileName> # creates a new file
rm <fileName>    # removes file with given name
du -sh *         # list directories with their total sizes 
df -h            # to see free disk space

```

## Files Permission
```sh
ls -l                              # to show file type and access permission
r                                  # read permission
w                                  # write permission
x                                  # execute permission
chown <user>                       # for changing the ownership of a file/directory
chown <user>: <group> <fileName>   # change the user as well as group for a file or directory
```

## tar/zip
-we use the tar command to compress and expand files from the command line. The syntax is shown below:

### Syntax
- tar [flags] destinationFileName sourceFileName

```sh
tar -zcvf foo.txt.tar.gz foo.txt
tar -xvf foo.txt.tar.gz

```
## Text Editor Options for Programmers

```c
Sublime Text     Atom        GNU Emacs 
Vim              Gedit       Notepadqq
Nano             VsCode      Brackets
```
