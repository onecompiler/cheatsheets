---
title: mv Linux Command
description: mv (move) Linux Command is used to move one or more file/directories from one place to another. This also used to rename files/directories
created: 2019-09-13
updated: 2019-09-13
---

mv (move) Linux Command is used to move one or more file/directories from one place to another. This also used to rename files/directories

## Syntax

```sh
mv [Option(s)] [source] [destination]
```

## Options

|Option|Description|
|---|---|
|-i| Interactively move|
|-f|Force override destination|

## Example

#### Renaming a file 

```sh
mv readme.txt readme-v2.txt
```

#### Moving file to user home folder

```
mv readme.txt ~/
```

#### Moving file to given destination directory

```sh
mv readme.txt /path/to/destination/
```