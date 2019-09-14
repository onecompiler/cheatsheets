---
title: alias Linux Command
description: alias command is used to create our own commands (command shortcuts) so that we don't have to remember/ type repeatedly used/ lengthy commands.  
created: 2019-08-23
updated: 2019-08-23
---

`alias` command is used to create our own commands (command shortcuts) so that we don't have to remember/ type repeatedly used/ lengthy commands.

# Creating an alias 
Following is the syntax for creating an `alias`

```sh
alias name=value
```
where the `name` is the new name you want to assign and `value` is the actual command.
Lets take a realtime usecase so that we can understand easily. 
We will type `ls -al` frequently to list all files in a directory. Lets assign an alias `files` to the command so that you can simply type `files` instead typing `ls -al`. Following command creats the alias with name `files` for `ls- al`

```sh
alias files='ls -al'
```

After runnng the about command we can simply type `files` to list all files & directories, instead typing `ls -al`

# Listing all created aliases 

Following command lists all created aliases

```sh
alias -p
```
### Example 

```sh
$ alias -p
alias files='ls -al'
```

# Deleting an alias
We can delete an alias with name using following command

```sh
unalias <alians_name>
```

# Deleting all aliases
Following command removes all aliases that are created 

```sh
unalias -a
```