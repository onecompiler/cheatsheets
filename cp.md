---
title: cp Linux Command
description: cp stands for copy. This command is used to copy files or directories. cp command require at least two filenames in its arguments.
created: 2019-08-26
updated: 2019-08-26
---

`cp` stands for copy. This command is used to copy files or directories. cp command require at least two filenames in its arguments.

# Syntax 

```sh
cp [OPTION] SourcePath DestinationPath
```

# Options

|Option|Description|
|---|---|
|-a|archive files|
|-f|force copy by removing/overriding the destination file (if already present)|
|-i|interactive mode override (asks before overwrite)|
|-l|linkes the files instead copy|
|-L|follows symbolic links|
|-n|no file overwrite, if destination file already exists|
|-R|recursive copy (this includes hidden files)|
|-u|update mode i.e copy only when source is newer than dest|
|-v|verbose mode i.e prints more information|

### Example

```sh
$ cp file1.txt file2.txt
$ ls
file1.txt	file2.txt
```
