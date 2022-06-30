---
title: C Programming language
description: C Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-04-25
updated: 2020-04-25
---

## Basics

* scanf("%d", &x) -- read value into the variable x from input stream
* Printf("%d",x) -- printf value to the output stream
* gets(str) -- reads a line from input stream into a variable
### Sample C program

```c
#include <stdio.h>    
int main(){    
printf("Hello World!!");    
return 0;   
}  
```
* `#include` is a keyword which is used to include the library file `<stdio.h>`. 
* `<stdio.h>` library file is used to read the data from terminal and to display the data on terminal. It has several in-built functions like printf(), scanf() etc.
* `main()` function is the entry point of any C program.
* `printf and scanf` are inbuilt library functions which are used for input and output in C language. They are defined in `stdio.h` header file.
* `return 0` is used to terminate the main() function and returns the value 0
* `//` -- single line comment
* `/* comments */` -- Multi line comment

## Data types

| Types | Data-type|
|----|----|
|Basic | int, char, float, double|
|Derived | array, pointer, structure, union|
|Enumeration | enum|
|Void |	void|

### 1. Basic Data types
| Data type | Description | Range | Memory Size| Format specifier|
|----|----|----|----|----|
| int| used to store whole numbers|-32,768 to 32,767|2 bytes| %d|
|short int| used to store whole numbers|-32,768 to 32,767| 2 bytes|%hd|
|long int| used to store whole numbers|	-2,147,483,648 to 2,147,483,647| 4 bytes|%li|
|float| used to store fractional numbers|6 to 7 decimal digits| 4 bytes|%f|
|double| used to store fractional numbers|15 decimal digits| 8 bytes|%lf|
|char|used to store a single character|one character|1 bytes|%c|

### 2. Derived Data types

Arrays:
```c
data-type array-name[size];
```
Pointers:

```c
datatype *pointername;
```
Structures: 

```c
struct structure_name {

   member definition;
   member definition;
   ...
   member definition;
} [one or more structure variables]; 

struct structure_name variable name;
```

### 3. Enumeration Data types

```c
enum name{constant1, constant2, constant3, ....... };
```
### 4. Void Data types

Void specifies that there is no return value. Generally used when function returns no value, pointer with type as void represents the address of an object but not it's type.

## Variables

### Syntax:
```c
data-type variable-name = value;
```
### Example:
```c
int x = 10; // declaring int variable and assigning value 10 to it
char grade = 'A'; // declaring char variable and assigning value A to it
```
## Literals
|Literal | Example|
|----|----|
|Integer Literal- decimal|255|
|Integer Literal- octal|0377|
|Integer Literal- hexadecimal|0xFF|
|Float point Literal|53.0f, 79.02|
|Character literals| 'a', '1'|
|String literals| "OneCompiler", "Foo"|

### Escape sequences
|Escape sequence| Description|
|----|----|
|\n	| New line|
|\r	| Carriage Return|
|\?	| Question mark|
|\t	| Horizontal tab|
|\v	| Vertical tab|
|\f	|Form feed|
|\\	| Backslash|
|\'	| Single quotation|
|\"	| Double quotation|
|\0 | Null character|
|\b	|Back space|

## Arrays

### One dimentional Array:

```c
data-type array-name[size];
```
### Example
```c
int a[5] = {1,2,3,4,5};
```

### Two dimensional array:

```c
data-type array-name[size][size];
```
### Example
```c
int a[2][3] = {
                {1,2,3},
                {4,5,6}
              };
```
## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %|
| comparision Operator| < , > , <= , >=, != , ==|
| Bitwise Operator| & , ^ , \||
| Logical Operator| && , `\|\|`, ! |
| Assignment Operator|= , += , -= , *= , /= , %=, <<=, >>=, &=, ^=, `\|=` |
| Ternary Operator| ? : |
| sizeof operator| sizeof() |

## Keywords(reserved words)

```c
auto         double      int        struct
break        else        long       switch
case         enum        register   typedef
char         extern      return     union
const        float       short      unsigned
continue     for         signed     void
default      goto        sizeof     volatile
do           if          static     while
```
## Identifiers

Identifiers are user defined names for variables, functions and arrays.

### Rules:
* They must be less than or equal to 31 characters.
* No special characters.
* Must start with a letter or under score.
* Can contain letters, digits, or underscore only.

## Strings

Strings are an array of characters ended with null character. Enclosed in double quotes.

```c
    char str[]="onecompiler";
```
## Constants

Constants are the fixed values. They can be declared in two ways as shown below:

``` c
const datatype <constant-name> = <constant-value>;
```
```c
#define <constant-name> <constant-value>
```
## Special characters
* `{}` : specifies start and end of code blocks
* `[]` : used for arrays
* `()` : used for functions
* `,` : used to seperate variables, constants etc
* `*` : used for pointers
* `#` : used as a macro processor.

## Conditional Statements

### 1. If
```c
if(conditional-expression)
{
    //code
}
```
### 2. If-else

```c
if(conditional-expression)
{
    //code
} else {
    //code
}
```
### 3. If-else-if ladder

```c
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
### 4. Switch

```c
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
```c
for(Initialization; Condition; Increment/decrement){  
//code  
} 
```
### 2. While
```c
while(condition){  
//code 
}  
```
### 3. Do-While
```c
do{  
//code 
} while(condition); 
```

## Functions

Function is a sub-routine which contains set of statements.

```c
// declaring a function
return_type function_name(parameters);

// defining a function
return_type function_name(parameters){  
//code
}

// calling a function
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

## Unions

Union is a user-defined datatype similar to structs which allows to store different data types in the same memory location. In Unnions, one member can contain a value at any given time.

```c
union union_name {
   member definition;
   member definition;
   ...
   member definition;
} [one or more union variables];  

union union_name variable name; // Declaring Union Variables
```

## File handling

File operations like create, update, read, and deleting files which are stored on the local file system can be performed in C.

```c
FILE *fptr; //declaring a pointer of type File
fptr = fopen("filename",mode); //opening a file
fscanf(fptr, "format specifier", data); //read a file
fprintf(fptr, "format specifier", data); //write a file
fclose(fptr);
```

|Mode | Description|
|----|----|
|r|	Opens for reading.|
|rb| Opens for reading in binary mode.|
|r+| Opens for both reading and writing.|
|w|	Opens for writing. |
|wb| Opens for writing in binary mode.|
|a|	Opens for append. |
|ab| Opens for append in binary mode.|
|w+| Opens for both reading and writing.|
|wb+| Opens for both reading and writing in binary mode.|
|rb+| Opens for both reading and writing in binary mode.|
|a+| Opens for both reading and appending.|
|ab+| Opens for both reading and appending in binary mode.|

## Expressions in C
An expression is a formula in which operands are linked to each other by 
the use of operators to compute a value. An operand can be a function 
reference, a variable, an array element or a constant.
Let's see an example:
  a-b;
In the above expression, minus character (-) is an operator, and a, and b 
are the two operands.
There are four types of expressions exist in C:
o Arithmetic expressions
o Relational expressions
o Logical expressions
o Conditional expressions

Each type of expression takes certain types of operands and uses a specific 
set of operators. Evaluation of a particular expression produces a specific 
value.
For example:
  x = 9/2 + a-b;
The entire above line is a statement, not an expression. The portion after 
the equal is an expression.

## 1) Arithmetic Expressions
An arithmetic expression is an expression that consists of operands and 
arithmetic operators. An arithmetic expression computes a value of type 
int, float or double.
When an expression contains only integral operands, then it is known as 
pure integer expression when it contains only real operands, it is known as 
pure real expression, and when it contains both integral and real operands, 
it is known as mixed mode expression.

## 2) Relational Expressions
o A relational expression is an expression used to compare two operands.
o It is a condition which is used to decide whether the action should be taken or 
not.
o In relational expressions, a numeric value cannot be compared with the string 
value.
o The result of the relational expression can be either zero or non-zero value. 
Here, the zero value is equivalent to a false and non-zero value is equivalent 
to true

## 3) Logical Expressions
o A logical expression is an expression that computes either a zero or non-zero 
value.
o It is a complex test condition to take a decision

## 4) Conditional Expressions
o A conditional expression is an expression that returns 1 if the condition is true 
otherwise 0.
o A conditional operator is also known as a ternary operator.
