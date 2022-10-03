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
ls -l                              	# to show file type and access permission
r                                  	# read permission (4)
w                                  	# write permission (2)
x                                  	# execute permission (1)
chown <user>                       	# for changing the ownership of a file/directory
chown <user>: <group> <fileName>   	# change the user as well as group for a file or directory
chmod <mode> <filename>				# change the permissions of a file/directory
```

## tar/zip
- Use the tar command to compress and expand files from the command line. The syntax is shown below:

### Syntax
- tar [options] [archive-file] [file or directory to be archived] 

```sh
tar -zcvf foo.txt.tar.gz foo.txt	# Create a zipped archive-file
tar -tvf foo.txt.tar.gz				# List archive files
tar -xvf foo.txt.tar.gz				# Extracting archive-file

Options:
-c 	# Creates Archive 
-x 	# Extract the archive 
-f 	# creates archive with given filename 
-t 	# displays or lists files in archived file 
-u 	# archives and adds to an existing archive file 
-v 	# Displays Verbose Information 
-A 	# Concatenates the archive files 
-z 	# zip, tells tar command that creates tar file using gzip 
-j 	# filter archive tar file using tbzip 
-W 	# Verify a archive file 
-r 	# update or add file or directory in already existed .tar file
```
