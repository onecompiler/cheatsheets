---
title: Haskell
description: Quick reference to Haskell cheat sheet which will increase your productivity as it contains useful syntax and is very handy while coding. 
created: 2020-06-25
updated: 2020-06-25
---

## Sample program

```java
main = do  
    name <- getLine  
    putStrLn ("Hello " ++ name ++ ", Happy learning!")
```
* ***main*** : entry point of the program
* ***getLine*** : reads input data from Console
* ***putStrLn*** : prints data to the console.
* `--` : Single line comment
* `{-` Multi

    Line

    comment `-}`

## Data types

| Data-type | Description |
|----|----|
|Numbers| Haskell is intelligent to identify numbers without specifying data type|
|Characters| Haskell is intelligent to identify characters and strings without specifying data type|
|Tuple|To declare multiple values in a single data type. Tuples are represented in single paranthesis. For example (10,20,'apple')|
|Boolean|To represent boolean values, true or false|
|List|To declare same type of values in a single data type. Lists are represented in square braces.For example `[1,2,3]` or `['a','b','c','d']|

## Reserved keywords

||||
|----|----|----|----|
| case | class | data| deriving| 
| do | else | if |import|
| in | infix | infixl | infixr|
| instance | let | of | module|
| newtype | then | type | where

## Operators

|Type|Operators|
|----|----|
| Arithmetic Operators| + , - , * , / , % , **, &&, \|\|, not |
| Comparision Operators| == , /= , > , >= , < , <= |
| Bitwise Operators| & , ^ , \| , ^ , ~ , << , >> , >>>|
| Function Operators| \, ., \||
| List Operators | \[...,...\], ++, :, !!, .. , \\, <-|
| Monad Operators| :, ->, ::, =>, (), >>, >>=, >@>,(..)|
| Pattern Operators | _, ~, !, @|

## Conditional Statements

###  If-Else 

```java
if conditional-expression
  then true statements 
  else false statements
```
### Case
```java
 case exp of
     Pattern1  -> action1
     Pattern2  -> action2
     _         -> else_action
```

## Tuples

Tuples are used to group data of different types(similar type is also allowed)

```java
(item1,item2,[itemn…])
```
### Example
```java
(1, "John", 35.2, true)
```
## Lists

Lists are usually used to group data of similar types
```java
[item1, item2,[itemn]]
```
### Example

```java
[1,2,3,4,5,6,7,8,9,10]
[1..10]
```
Both the above gives the same meaning as you can also use range to define lists

Some of the common list operations

|List Operations| Description|
|----|----|
|list1+list2| to append two lists list1+list2|
| list1!!n | to return element n from list1|
| head/last list1| to retrieve the first/last element of the list1|
| sum list1| to get the sum of all list elements present in list1|
| prod list1| to get the product of all list elements  present in list1|
| reverse list1 | to reverse the elements present in list1|

## Functions

### How to define and call a Function

```java
functionname :: data type [-> datatype] -> data type -- function definition 
--code

functionname(variable) -- calling a function
```
### Examples
```java
multiply :: Integer -> Integer -> Integer   --declaration of a function 
multiply x1 x2 =  x1 * x2                       --definition of a function

main = do 
   putStrLn "Multiplication value is:"  
   print(multiply 10 5)    --calling a function
```