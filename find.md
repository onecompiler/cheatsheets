---
title: find Linux Command
description: find Linux Command is used to locate files in directories. By default find looks for files in current directory.
created: 2019-09-13
updated: 2019-09-13
---

find Linux Command is used to locate files in directories. By default find looks for files in current directory.


## Syntax

```sh
find [option(s)] [Path] [expression]
```

|Option|Description|
|---|---|
|-P| Not follow symbolic links (default behaviour) |
|-L|Follow symbolic links|
|-H|Follow symbolic links only while processing command line arguments|

## Examples

Consider the following directory structure 

```sh
$ tree
.
├── images
│   ├── cat.png
│   ├── dog.png
│   ├── moon.png
│   └── sun.png
├── movies
│   ├── action
│   │   ├── bar.mp4
│   │   └── foo.mp4
│   └── comedy
├── music
│   ├── song1.mp3
│   └── song2.mp3
└── readme.txt

5 directories, 9 files
```

```
find . -name cat.png
./images/cat.png
```

```
find . -name cat*
./images/cat.png
```

```
find . -name *.png
./images/dog.png
./images/moon.png
./images/cat.png
./images/sun.png
```