---
title: head Linux Command
description: head Linux Command is used to display beginning of a text file/ piped data.
created: 2019-09-13
updated: 2019-09-13
---

head Linux Command is used to display beginning of a text file/ piped data.


## Syntax

```sh
head [options] file-name
```

## Examples

For example consider the following file

```sh
$ cat readme.txt 
line1
line2
line3
line4
line5
line6
line7
line8
line9
line10
line11
line12
line13
line14
line15
```

```sh
$ head readme.txt
line1
line2
line3
line4
line5
line6
line7
line8
line9
line10 
```

```
Note: head by default shows first 10 lines
```

### Showing first 2 lines

```sh
$ head -n 2 readme.txt
line1
line2
```

### Showing first 5 lines

```sh
$ head -n 5 readme.txt
line1
line2
line3
line4
line5
```

### Showing from multiple files
```sh
$ head -n 2 readme.txt readme-2.txt
==> readme.txt <==
line1
line2

==> readme-2.txt <==
line1
line2
```

### Showing from all files that are starting with readme
```sh
$ head -n 2 readme*
==> readme-2.txt <==
line1
line2

==> readme-3.txt <==
line1
line2

==> readme.txt <==
line1
line2

```