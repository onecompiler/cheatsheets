---
title: comm Linux Command
description: comm Linux Command compare two sorted files line by line and write to output, It requires two sorted files which it compares line by line.
created: 2019-08-26
updated: 2019-08-26
---

`comm` Linux Command compare two sorted files line by line and write to output, It requires two sorted files which it compares line by line.

# Syntax 

```sh
comm [OPTION]... FILE1 FILE2
```

# Options

|Option|Description|
|---|---|
|-1|suppress printing of the first column (lines unique to the first file)|
|-2|suppress printing of the second column (lines unique to the second file)|
|-3|suppress printing of the third column (lines common to both the files)|
|–-check-order|check's the input is correctly sorted, even if all the input lines are pairable|
|–-nocheck-order|do not check that the input is correctly sorted|
|–-output-delimiter=STR|separate columns with string STR|


### Example

```sh
$cat >file1.txt
one
two
three

$cat >file2.txt
one
three
four

$comm file1.txt file2.txt
		one
	three
	four
two
three
```
