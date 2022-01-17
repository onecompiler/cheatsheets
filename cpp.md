---
title: C++ Programming language 
description: C++ Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-04-30
updated: 2020-04-30
---

C++ is a widely used middle-level programming language which is used in developing major operating systems( Windows, Linux, Android, Ubuntu, iOS etc), Games, databases and compilers etc.  

## Basics
* `cin` >> x-- read value into the variable x from input stream
* `cout` << x -- printf value to the output stream
* `//` -- single line comments
* `/* */` -- Multi line comments

### Sample C program

```c
#include <iostream>
using namespace std;
int main() {
    cout << "Hello World!!";
    return 0;
}  
```
* `#include <iostream>` -- iostream is a inbuilt header library which allows you to deal with input and output objects like cout etc.
* `using namespace std` -- Specifies that the object and variable names can be used from standard library.
* `cout` -- to print the output.
* `main()` -- main function is the entry point of any C++ program.
* `return 0` -- To end the main function

#### How to compile a program in C++

Open your terminal, Navigate to the directory where you have saved your program. Consider firstprogram.cpp is the name of your program.

```c
sudo g++ -o firstprogram firstprogram.cpp
```

#### How to run a C++ program

```
./firstprogram
```

## Data types

| Types | Data-type|
|----|----|
|Basic | int, char, float, double, short, short int, long int etc |
|Derived | array, pointer etc |
|User Defined Data Type | structure, enum, Class, Union, Typedef |

## Variables

```c
data-type variable-name = value;
```
```c
int value = 10; // declaring int variable and assigning value 10 to it
char grade = 'A'; // declaring char variable and assigning value A to it
```
### Naming convention
* only letters (both uppercase and lowercase letters), digits and underscore(`_`).
* cannot contain white spaces
* First letter should be either a letter or an underscore(`_`).
* Variable type can't be changed
* Case sensitive

## Arrays

```c
data-type array-name[size]; // one-dimensional Array
data-type array-name[size][size]; // two-dimensional Array
```
### Example:
```c
int a[5] = {1,2,3,4,5};
int a[2][3] = {
                {1,2,3},
                {4,5,6}
              };
```
## Literals or Constants
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

## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %|
| comparision Operator| < , > , <= , >=, != , ==| 
| Bitwise Operator| & , ^ , | 
| Logical Operator| && , `||`, ! |
| Assignment Operator|= , += , -= , *= , /= , %=, <<=, >>=, &=, ^=, `|=` |
| Ternary Operator| ? : |
| sizeof operator| sizeof() |

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

## Enum

Enumeration data type is a user-defined data type in C++. `enum` keyword is used to declare a new enumeration types in C++. 

```c
enum name{constant1, constant2, constant3, ....... } var-list;
```
### Example
```c
enum month{January, February, March, April, May, June, July, August, September, October, November, December} name;
```

## Typedef
Typedef is used to explicitly define new data type names by using the keyword `typedef`. It defines a name for an existing data type but doesn't create a new data type. 

```c
typedef data-type name;
```
### Example
```c
typedef unsigned int distance;  // typedef of int 
```

## Vectors
Vectors are same as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatically by the container. Vector elements are placed in contiguous storage so that they can be accessed and traversed using iterators. In vectors, data is inserted at the end. Inserting at the end takes differential time, as sometimes there may be a need of extending the array. Removing the last element takes only constant time because no resizing happens. Inserting and erasing at the beginning or in the middle is linear in time.

 

Certain functions associated with the vector are:
Iterators

begin() – Returns an iterator pointing to the first element in the vector
end() – Returns an iterator pointing to the theoretical element that follows the last element in the vector
rbegin() – Returns a reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
rend() – Returns a reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)
cbegin() – Returns a constant iterator pointing to the first element in the vector.
cend() – Returns a constant iterator pointing to the theoretical element that follows the last element in the vector.
crbegin() – Returns a constant reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
crend() – Returns a constant reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)

```c
// C++ program to illustrate the
// iterators in vector
#include <iostream>
#include <vector>
  
using namespace std;
  
int main()
{
    vector<int> g1;
  
    for (int i = 1; i <= 5; i++)
        g1.push_back(i);
  
    cout << "Output of begin and end: ";
    for (auto i = g1.begin(); i != g1.end(); ++i)
        cout << *i << " ";
  
    cout << "\nOutput of cbegin and cend: ";
    for (auto i = g1.cbegin(); i != g1.cend(); ++i)
        cout << *i << " ";
  
    cout << "\nOutput of rbegin and rend: ";
    for (auto ir = g1.rbegin(); ir != g1.rend(); ++ir)
        cout << *ir << " ";
  
    cout << "\nOutput of crbegin and crend : ";
    for (auto ir = g1.crbegin(); ir != g1.crend(); ++ir)
        cout << *ir << " ";
  
    return 0;
}

```
