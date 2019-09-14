---
title: tail Linux Command
description: tail Linux Command is used to display tail end of a text file/ piped data.
created: 2019-09-13
updated: 2019-09-13
---

tail Linux Command is used to display tail end of a text file/ piped data.


## Syntax

```sh
tail [options] file-name
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
$ tail readme.txt
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

```
Note: head by default shows first 10 lines
```

### Showing last 2 lines

```sh
$ tail -n 2 readme.txt
line14
line15

```

### Showing last 5 lines

```sh
$ tail -n 5 readme.txt
line11
line12
line13
line14
line15
```

### Showing from multiple files
```sh
$ tail -n 2 readme.txt readme-2.txt
==> readme.txt <==
line14
line15

==> readme-2.txt <==
line14
```

### Showing from all files that are starting with readme
```sh
$ tail -n 2 readme*
==> readme-1.txt <==
line14
line15
==> readme-2.txt <==
line14
line15
==> readme.txt <==
line14
line15
```