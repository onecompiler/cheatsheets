---
title: wc Linux Command
description: wc (word count) Linux Command is used to read standurd input or a list of files and generates new lines count  or word count or byte count.
created: 2019-09-13
updated: 2019-09-13
---

wc (word count) Linux Command is used to read standurd input or a list of files and generates new lines count  or word count or byte count.


## Syntax

```sh
wc [Option(s)] [file(s)]
```


## Options

|Option| Description|
|---|---|
|-l| prints lines count|
|-c|prints byte count|
|-m|prints character count|
|-L|prints length of longest line|
|-w|prints word count|

## Examples

Lets take a file `readme.txt` with following content 

```sh
$ cat readme.txt
Hello World line-1
Hello World line-2
Hello World line-3
Hello World line-4
Hello World line-5
Hello World line-6
Hello World line-7
Hello World line-8
Hello World line-9
Hello World line-10
```

#### Print lines count of a file
```sh
wc -l readme.txt #=>  10 readme.txt
```

#### Print words count of a file

```sh
wc -w readme.txt #=> 30 readme.txt
```

#### Print character count of a file
```sh
wc -c readme.txt #=> 191 readme.txt
```