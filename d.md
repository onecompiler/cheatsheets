---
title: D Programming language
description: D Programming language cheatsheet contains useful code syntax with examples which is really handy while coding.
created: 2020-06-30
updated: 2020-06-30
---

## Sample program

```d
import std.stdio;

void main()
{
		writeln("Hello, World!");
}
```
* **import** : import is used to load system libraries into your program
* **std.stdio** : std.stdio is a library module which handles data input and output.
* **main()** : starting of the program which determines the order of execution
* **writeln** : to display data to console
* `/*` Multi line comments `*/`
* `//` : Single line comment

## Data types

| Data type | Description | Range | Size|
|---|---|---|---|
| int| used to store whole numbers|-2,147,483,648 to 2,147,483,647|4 bytes|
|short| used to store whole numbers|-32,768 to 32,767| 2 bytes|
|long| used to store whole numbers|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807| 8 bytes|
|byte| used to store whole numbers|-128 to 127| 1 byte|
|float| used to store fractional numbers|1.17549e-38 to 3.40282e+38| 4 bytes|
|double| used to store fractional numbers|2.22507e-308 to 1.79769e+308| 8 bytes|
|ifloat| used to store imaginary value type of float|1.17549e-38i to 3.40282e+38i| 4 bytes|
|idouble| used to store imaginary value type of double|2.22507e-308i to 1.79769e+308i| 8 bytes|
|cfloat| used to store complex number type made of two floats|1.17549e-38+1.17549e-38i to 3.40282e+38+3.40282e+38i| 8 bytes|
|cdouble| used to store complex number type made of two doubles|2.22507e-308+2.22507e-308i to 1.79769e+308+1.79769e+308i| 16 bytes|
|bool| can either store true or false |either true or false| 1 byte|
|char|used to store a single character|one character| 1 byte|


## Variables

### Syntax
```d
datatype variable-names;
```
## Strings

```java
char[15]  msg1 = "Hello World!"; 

/* or */
string msg2 = "Happy learning";

string msg3 = msg1~" "~msg2; //string concatenation

int length = msg3.length // gives length of the string
```

## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %, ++, --|
| comparision Operator| < , > , <= , >=, != , ==|
| Bitwise Operator| & , ^ , \|, ~, <<,>>|
| Logical Operator| && , \|\|, ! |
| Assignment Operator|= , += , -= , *= , /= , %=, <<=, >>=, &=, ^=, \|= |
| Misc Operator| sizeof(), &, *, ? : |

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
### 4. Nested-If

```java
if(conditional-expression-1) {    
     //code    
          if(conditional-expression-2) {  
             //code
             if(conditional-expression-3) {
                 //code
             }  
    }    
}
```
### 5. Switch
```java
switch(conditional-expression){    
case value1:    
 //code    
 break;  //optional  
case value2:    
 //code    
 break;  //optional  
...    
    
default:     
 //code to be executed when all the above cases are not matched;    
} 
```

## Loops

### 1. For
```java
for(Initialization; Condition; Increment/decrement){  
//code  
} 
```

### 2. While
```java
while(condition){  
//code 
}  
```
### 3. Do-While
```java
do{  
//code 
}while(condition); 
```
## Arrays

```
data-type array-name [ array-size ];
```

## Functions

```c
//defining a function
return_type function_name(parameters) {  
  //code
}

//calling a function
function_name (parameters)

```

## Pointers

Pointer is a variable which holds the memory information(address) of another variable of same data type.

```c
datatype *pointername;
```
### Example
```c
int x = 10, *ptr;

/*ptr = x; // Error because ptr is adress and x is value
*ptr = &x;  // Error because x is adress and ptr is value */

ptr = &x; // valid because &x and ptr are addresses
*ptr = x; // valid because both x and *ptr values 
```
## Structures

Structure is a user-defined data type where it allows you to combine data of different data types.

```c
struct structure_name {

   member definition;
   member definition;
   ...
   member definition;
} [one or more structure variables]; 

struct structure_name variable name; //declaring structure variables
```

## Enum

Enumeration data type is a user-defined data type and `enum` keyword is used to declare a new enumeration types. 

```c
enum name{constant1, constant2, constant3, ....... };
```
### Example
```c
enum month{January, February, March, April, May, June, July, August, September, October, November, December} name;
```

