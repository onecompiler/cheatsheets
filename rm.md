---
title: rm Linux Command
description: rm (remove) Linux Command is used to remove objects such as files, directories, symbolic links, device nodes, pipes and sockets from the file system. 
created: 2019-09-13
updated: 2019-09-13
---

rm (remove) Linux Command is used to remove objects such as files, directories, symbolic links, device nodes, pipes and sockets from the file system.


## Syntax

```sh
rm [Option(s)] [File(s) to remove]
```

## Examples

#### Removing a single file
```sh
rm file1.txt #=> removes file1.txt
```

#### Removing multiple files
```sh
rm file1.txt file2.txt #=> removes file1.txt and file2.txt
```

#### Interactive deletion

```sh
rm -i readme.txt
remove readme.txt? Y 
```

#### Force deletion (Removes even if the file is write protected)

```sh
rm readme.txt
```

#### Delete recusively

```sh
rm -r *
```