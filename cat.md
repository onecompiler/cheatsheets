---
title: cat Linux Command
description: cat command is used to create, read & concatenate files in Linux/ Unix machines
created: 2019-08-21
updated: 2022-10-05
---

`cat` command is used to create, read & concatenate files in Linux/ Unix machines. 

## 1. Creating a file with content
Lets create a file with name `file1.txt` and put following three lines of content into it. 

First you need to run the following command to create a file

```sh
cat >file1.txt
```
When you press enter after the above command, it waits for the file content input. You can give multi line input and once you are done you need to press `CTRL + D` to save and exit. 


## 2. Displaying file contents 
Following command shows the content of given file
```sh
cat file1.txt
```
## 3. Display content from multiple files
Following command shows content from file1.txt followed by content from file2.txt

```sh
cat file1.txt file2.txt
```

## 4. Copy the contents of one file to another file
Following command copies content from file1.txt to file2.txt

```sh
cat file1.txt > file2.txt
```

## 5. Append the contents of one file to the end of another file
Following command appends content of file1.txt to the end of file2.txt

```sh
cat file1.txt >> file2.txt
```

## 6. Display content in reverse order
Following command displays content of file1.txt in reverse order

```sh
tac file1.txt
```

## 7. Open dashed files
Following command displays content of -dashfile

```sh
cat -- "-dashfile"
```

## 8. If the file has a lot of content and can’t fit in the terminal
```sh
cat "filename" | more
```

## 9. Merge the contents of multiple files
```sh
cat "filename1" "filename2" "filename3" > "merged_filename"
```

## 10. Display Line Numbers before every line 

Following command prefixes line numbers before each line from content

```sh
cat -n file1.txt
```
Following is an example for that 

```sh
$ cat -n file1.txt
     1	line-1
     2	line-2
     3	line-3
     4	line-4
```

## 11. Display content with More & Less Options
If a file having a large number of content that won’t fit in the output terminal and the screen scrolls up very fast, we can use parameters more and less with the cat command as shown below.

```sh
cat song.txt | more
cat song.txt | less
```

## More Options

|Option| Description|
|---|---|
|`-e`|Shows `$` at the end of the content|
|`-t`|To see tabs in file, this shows tabs with `^I`|
|`-s`|Removes repeated empty lines in content|
|`-E`|Highlights the end of line|
