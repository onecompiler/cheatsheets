---
title: cksum Linux Command
description: cksum Linux command is used to generate checksum value for a file or stream of data. cksum reads files given in its arguments and calculates checksum, if no arguments provided then it reads the standard input.
created: 2019-08-25
updated: 2019-08-25
---

`cksum` Linux command is used to generate checksum value for a file or stream of data. cksum reads files given in its arguments and calculates checksum, if no arguments provided then it reads the standard input.

# Syntax 

```sh
cksum [OPTION]... [FILE]...
```

### Example

```sh
$ cksum readme.txt 
2116921653 13 readme.txt
```

```
2116921653 13 readme.txt
|          |  |__ file name 
|          |
|          |_____ file size in bytes
|
|________________ Checksum value

```