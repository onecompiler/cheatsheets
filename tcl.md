---
title: TCL
description: Quick reference to TCL cheat sheet which contains useful syntax and is very handy while coding. 
created: 2020-06-26
updated: 2020-06-26
---

## Sample program

```c
set name [gets stdin]
puts "Hello $name"
```
* ***set*** : To set data to a variable
* ***gets stdin*** : to read input data from Console
* ***puts*** : prints data to the console.
* `#` : Single line comment

## Variables

```c
set name onecompiler
```
## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %|
| comparision Operator| < , > , <= , >=, != , ==|
| Bitwise Operator| & , ^ , \|, <<, >>|
| Logical Operator| && , `\|\|`, ! |
| Ternary Operator| ? : |

## Conditional Statements

### 1. If-Else

```c
if(conditional-expression) {
   #code
} else {
   #code
}
```

### 2. Switch

```c
switch(conditional-expression) {    
value1 {     
 # code
}    
value1 {     
 # code
}    
...
default {
# code
} 
```

## Loops

### 1. For

```c
for{start}{test}{next}{  
  # code  
} 
```
### 2. While

```c
while(condition) {  
 # code 
}  
```

## Arrays

```c
set ArrayName(Index) value
```
## Lists

```c
set listName { i1 i2 i3 .. in }
# or
set listName [list i1 i2 i3]
# or 
set listName [split "items which separated by a character" split_character]
```

## Dictionary

Dictionary is a collection of key-value pairs.

```c
dict set dictName key value
# or 
dict create dictName key1 value1 key2 value2 .. keyn valuen
```
## Procedures

```c
proc procedureName {arguments} {
   # code
}
```

## File Handling

### Opening a file

```c
open fileName Mode
```

|Mode|Description|
|----|----|
|"r"  |  Read-only(default mode)|
|"r+" |  Read-write, File must be present already. |
|"w"  |  Write-only |
|"w+" |  Read-write, creates new file if file doesn't exist|
|"a"  |  Write-only, appends data at the end of file if file exists else creates a new file|
|"a+" |  Read-write,  read data from beginning but appends data at the end of file if file exists else creates a new file|

### Closing a file

```c
close fileName
```
### Writing to a file

```c
puts $filename "data to write to the file"
```