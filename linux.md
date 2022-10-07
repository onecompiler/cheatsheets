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
## System Info
```sh
date          # Show the current date and time
cal           # Show this month's calender
uptime        # Show current uptime
w             # Display who is on line
whoami        # Who you are logged in as
finger user   # Display information about user
uname -a      # Show kernel information
man command   # Show the manual for command
df            # Show the disk usage
du            # Show directory space usage
free          # Show memory and swap usage
```

## Shortcuts
```sh
ctrl+c       # Halts the current command
ctrl+z       # Stops the current command, resume with fg in the foreground or bg in the background
ctrl+d       # Logout the current session, similar to exit
ctrl+w       # Erases one word in the current line
ctrl+u       # Erases the whole line
ctrl+r       # Type to bring up a recent command
!!           # Repeats the last command
exit         # Logout the current session
```

