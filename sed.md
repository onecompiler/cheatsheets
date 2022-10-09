---
title: sed Linux Command
description: Sed is a stream editor.  A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline).
created: 2022-10-09
updated: 2022-10-09
---


Sed is a stream editor.  A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline)

## 1. Replace a word in the file

It will replace all the occurences of foo with bar in the example.md file

```sh
sed -i -e 's/foo/bar/' example.md 
```


## 2. Displaying file contents until string found

Print until a certain line is met in this case `begin api`

```sh
sed '/begin api/q'
```

## 3. Displaying file contents until string found except that line

Print until a certain line is met, except that line

```sh
sed '/^# begin/,$d'
```

## 4. Print everything after a given line

```sh
sed -n '/end api/,$p'
```

## 5. Print everything except matching

It will print all the lines except the lines in which the word is found

```sh
sed -n '/regex/d;'
```

## 6. Delete last line

Following command displays content of file1.txt in reverse order

```sh
sed -i '$ d' example.md 
```

## 7. Delete lines from 2 to 6

Following command displays content of -dashfile

```sh
sed 2,6d
```

## 8. upper case the first letter on every line

```sh
sed 's/[a-z]/\u&/'
```

## 9. Delete leading whitespace (spaces, tabs) from front of each line 

```sh
sed 's/^[ \t]*//' 
```

## 10. Reverse order of lines

```sh
sed '1!G;h;$!d'
```
