---
title: grep Linux Command
description: grep is a Linux command line utility to search plain text datasets using regular expressions. 
created: 2019-09-13
updated: 2019-09-13
---

grep is a Linux command line utility to search plain text datasets using regular expressions. 


## Syntax

```sh
grep [options] search-pattern [file(s)]
```

## Examples

Lets take following file as an example to perform grep operations

```sh
$ cat readme.txt
Hello World line1
Hello World line2
Hello World line3
Hello World line4
Hello World line5

```

```sh
$ grep 5 readme.txt
Hello World line5
```

```sh
$ grep line4 readme.txt
Hello World line4
```

```sh
$ grep Hello readme.txt
Hello World line1
Hello World line2
Hello World line3
Hello World line4
Hello World line5
```

```sh
$ grep -i hello readme.txt
Hello World line1
Hello World line2
Hello World line3
Hello World line4
Hello World line5
```

```
Note: -i is to ignore case
```