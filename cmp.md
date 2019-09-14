---
title: cmp Linux Command
description: cmp Linux command is used to compare 2 files byte by byte. It reports the byte, line number where the first difference is found. If no difference, no output will return. The optional SKIP1 and SKIP2 specify the number of bytes to skip at the beginning of each file (zero if nothing specified).
created: 2019-08-26
updated: 2019-08-26
---

`cmp` Linux command is used to compare 2 files byte by byte. It reports the byte, line number where the first difference is found.
If no difference, no output will return. The optional SKIP1 and SKIP2 specify the number of bytes to skip at the beginning of each file (zero if nothing specified).

# Syntax 

```sh
cmp [OPTION]... FILE1 [FILE2 [SKIP1 [SKIP2]]]
```

# Basic Command syntax
```sh
cmp [OPTION]... FILE1 FILE2
```

### Example

```sh
$ cmp file1.txt file2.txt
file1.txt file2.txt differ: char 2, line 1
```
