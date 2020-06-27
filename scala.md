---
title: Scala 
description: Quick reference to scala cheat sheet which will increase your productivity as it contains useful syntax and is very handy while coding. 
created: 2020-06-25
updated: 2020-06-25
---

## Sample program

```java
object HelloWorld {
	def main(args: Array[String]): Unit = {
	println("Hello, World!")
	}
}
```
* ***object*** :  Object is a instance of a class. In Scala, everything is considered as objects.
* ***def*** : def is used for function declaration
* ***main*** : entry point of the program
* ***println*** : prints data to the console.
* `//` : Single line comment
* `/*` Multi
    Line
    comment `*/`

## Data types

| Data type | Description | Range | Size|
|---|---|---|---|
| int| used to store whole numbers|-2,147,483,648 to 2,147,483,647|4 bytes|
|short| used to store whole numbers|-32,768 to 32,767| 2 bytes|
|long| used to store whole numbers|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807| 8 bytes|
|byte| used to store whole numbers|-128 to 127| 1 byte|
|float| used to store fractional numbers|6 to 7 decimal digits| 4 bytes|
|double| used to store fractional numbers|15 decimal digits| 8 bytes|
|boolean| can either store true or false |either true or false| 1 bit|
|char|used to store a single character|one character|2 bytes|
|string | used to store strings|sequence of characters|2bytes per character|

## Variables

```java
var varName = value
val  varName = value
varName = value
var varName : DataType = value
```

## Operators

|Type|Operators|
|----|----|
| Arithmetic Operators| + , - , * , / , %  |
| Comparision Operators| == , != , > , >= , < , <= |
| Bitwise Operators| & , ^ , \| , ^ , ~ , << , >> , >>>|
| Logical Operators| && , \|\| , !|
| Assignment Operators|= , += , -= , *= , /= , %= , &= , ^= , \|= , <<= , >>= |

## Conditional Statements

### 1. If

```java
if(conditional-expression)
{
    //code
}
```
### 2. If-else

```java
if(conditional-expression)
{
    //code
} else {
    //code
}
```
### 3. If-else-if ladder

```java
if(conditional-expression-1)
{
    //code
} else if(conditional-expression-2) {
    //code
} else if(conditional-expression-3) {
    //code
}
....
else {
    //code
}
```
## Loops

### 1. For

```java
for(var <- range){  
//code  
} 
```
### 2. For loop Using until 

```java
for( var <- initialValue until maxValue ){  
    //code  
}
```

### 3. For loop filtering

```java
for( var <- initialValue until maxValue if condition){  
  //code
}
```
### 4. For loop for collections like lists, sequence etc

```java
for( varName <- Collections){             
  //code
}
```
### 5. While

```java
while(condition){  
//code 
}  
```
### 6. Do-while

```java
do{  
//code 
}while(condition); 
```

## Arrays
Array is a collection of similar data which is stored in continuous memory addresses.

### Declaring 1-D array

```java
var arrayName:Array[datatype] = new Array[datatype](size)

//or

var arrayName = new Array[datatype](size)
```

### Declaring 2-D array

```java
var arrName = ofDim[datatype](rowsize,colSize)
```
### Example

```java
 var arr1 = Array(1, 2, 3, 4, 5)
```

## Functions

### How to declare a Function

```java
def functionName ([argumentsList]) : [return type]
```
### How to define a Function
```java
def functionName ([argumentsList]) : [return type] [=] {
   // code
   return [expr]
}
```
### How to call a Function

```java
function_name (argumentsList)
```