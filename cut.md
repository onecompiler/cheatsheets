---
title: cut Linux Command
description: cut Linux Command is used to extract sections from each line of input or from a file. Extraction of line segments can be done by bytes (-b),  characters (-c), fields (-f) or by delimiter (-d)  tab character is the default delimiter.
created: 2019-09-11
updated: 2019-09-11
---

cut Linux Command is used to extract sections from each line of input or from a file. Extraction of line segments can be done by bytes (-b),  characters (-c), fields (-f) or by delimiter (-d)  tab character is the default delimiter.

## Segment types

|segment|description|
|---|---|
|-b| bytes|
|-c| characters |
|-f| fields|
|-d|delimiter. Note: tab is the default delimiter|


## Range specification
|Range|description|
|---|---|
|N| Nth|
|N-M| N to M|
|N-|N to end of line|
|-M|beginning to M|

Note: N, M counted from 1, not 0.

## Examples 

Lets say we have a file `foo.txt` with following content

```
abc-def-ghi-jkl
mno-pqr-stu-vwx
123-456-7890
```

```sh
$ cut -c 5-7 foo.txt 
def
pqr
456
```

```sh
$ cut -d "-" -f 1-2 foo.txt 
abc-def
mno-pqr
123-456
```

```sh
$ cut -c 5- foo.txt
def-ghi-jkl
pqr-stu-vwx
456-7890

```