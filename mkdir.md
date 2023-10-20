---
title: mkdir Linux Command
description: mkdir Linux Command is used to create new directory. Along with Linux systems mkdir is also available in most of the popular operating systems.
created: 2019-09-13
updated: 2023-10-20
---

mkdir Linux Command is used to create new directory. Along with Linux systems mkdir is also available in most of the popular operating systems.

## Syntax

```sh
mkdir [name-of-directory(s)]
```
## Option

|Option|Description|
|---|---|
|-m| Set file mode (as in chmod), not a=rwx - umask |
|-p| Make parent directories as needed|
|-v| Verbose - Print a message for each created directory|


## Example

```sh
mkdir d1 # creates directory with name d1
```

```sh
mkdir d2 d3 d4 # creates directories d2, d3 and d4
```
```sh
mkdir d1/d2/d3 # creates folder d1, then d2 inside d1 and then finally d3 inside d2
```