---
title: Perl
description: Perl Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-05-02
updated: 2020-05-02
---

Perl(Practical Extraction and Report Language) is especially designed for text processing by Larry Wall. Perl is a high level programming language and hence one can easily undertand Perl as the programs are in simple english.

## Basics

### Sample program

```perl
print "Hello World!!"; # to display "Hello World!!"
```

* `print` -- to print the data given
* `#` -- single line comments

## Data types

Perl has three basic data types: 

1. Scalars
2. Arrays 
3. Hashes 

```perl
$var-name =value; #scalar-variable
@arr-name = (values); #Array-variables
%hashes = (key-value pairs); # Hash-variables 
```

In Perl, there is no need to explicitly declare variables to reserve memory space. When you assign a value to a variable, declaration happens automatically.

## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %, **|
| comparision Operator| < , > , <= , >=, != , ==|
| Bitwise Operator| & , ^ , \|, ~, <<, >>|
| Logical Operator| && , \|\|, ! |
| Assignment Operator|= , += , -= , *= , /= , %=, <<=, >>=, &=, ^=, \|= |
| Quote Operator| q{ }, qq{ }, qx{ } |

## String Functions

Below are some of the useful string functions in Perl.

| String Function |	Description|
|----|----|
|length| This function is used to return the number of characters of a given string|
|substr| This method is used to modify a substring in a string|
|index|	Searches for a substring in the given string and returns the position of the first occurrence of the substring if found|
|rindex| Similar to index but searches for a substring from right to left|
|reverse| This function is used to reverse a string|
|lc| This function is used to convert the specified string to lowercase|
|uc| This function is used to convert the specified string to uppercase|
|crypt|	This function is used to encrypt password|
|q/string/|	used to create single-quoted strings|
|qq/string/| used to create double-quoted strings|
|chr| to return ASCII or UNICODE character of a number|
|hex| used to convert a hexadecimal string to it's equivalent decimal value|
|oct| used to convert an octal number to it's equivalent decimal value|
|ord| returns the ASCII value of the first character of a string|
|sprintf| Formats string  provided by the user and returns the formatted string to be used with print()|
 
## Lists

List is a series of scalar values separated by commas and enclosed in round brackets. Lists are immutable.

```perl
(); # empty list

(1,2,3,4,5); # integer list

("Hello", "World"); #string list

("happy", 16) # list with different types of data
```

## Hashes

Hash is an unordered set of key/value pairs. They are preceded by `%`. 

```perl
%nationalGame = (Australia => 'Cricket',
Japan => 'Wrestling',
NewZealand => 'Rugby',
USA => 'Baseball',
England => 'Cricket');
```

## Arrays

Array is a variable which gives dynamic storage for a list.

```perl
my @fruits = qw(Apple Orange Grapes Kiwi Watermelon Banana);
```
### Array Operations

|Array Operations| Description|
|----|----|
| $count| returns the number of elements in the array|
| $# | returns the highest index of an array|
| push() | appends one or more elements to the end of an array |
|unshift() | adds one or more elements to the front of the array |
| pop() | removes the last element from the end of an array|
| sort() | used to sort an array in alphabetical or numerical order. |

## Conditional Statements

### 1. If

```perl
if(conditional-expression)
{
    #code
}
```
### 2. If-else

```perl
if(conditional-expression)
{
    #code
} else {
    #code
}
```
### 3. If-else-if ladder

```perl
if(conditional-expression-1)
{
    #code
} elsif(conditional-expression-2) {
    #code
} elsif(conditional-expression-3) {
    #code
}
....
else {
    #code
}
```

### 4. Nested-If

Nested-Ifs represents if block within another if block. 
```perl
if(conditional-expression-1) {    
     #code    
          if(conditional-expression-2) {  
             #code
             if(conditional-expression-3) {
                 #code
             }  
    }    
}
```
### 5. Unless

Unless is similar to If and is equivalent to `if-not`. 

```perl
statement unless(condition-expression);

#or

unless(condition-expression){
   #code 
}
```
### 6. Unless-else

```perl
unless(condition-expression){
  # unless code
}else{
  # else code
}
```
### 7. Given

Given is similar to Switch in other programming languages. 

```perl
given(conditional-expression){    
when(value1){#code}
when(value2){#code}
when(value3){#code}
...
} 
```
## Loops

### 1. For

```perl
for(Initialization; Condition; Increment/decrement){  
#code  
} 

#or

for (range){
  #code
}
```

### 2. While

```perl
while(condition){  
#code 
}  
```

### 3. Do-while

```perl
do{  
#code 
} while(condition); 
```

### 4. Until

```perl
until(conditional-expression){
   # code
}
```
### 5. Do-Until

```perl
do{
   # code
}until(condition-expression)
```
## Classes and Objects

### Class

```perl
package className; 
```

### Objects

```perl
$object = new className( Attributes);
```
### Methods

```perl
sub methodName{
  #code
}
```
## Sub-routines

```perl
sub SubName  [PROTOTYPES] [ATTRIBUTES] { # defining a sub-routine
  #code
}

&SubName; # calling a sub-routine
#or
SubName(argument-list); # calling a sub-routine, argument-list is optional
```
### Example

```perl
sum(10,20);

sub sum() {
   $sum = 0;

   foreach $item (@_) {
      $sum += $item;
   }
print "sum is: $sum"
  
}
```
## Files

### Opening a file

```perl
open(filehandle,mode,filename)
```
|Mode|Symbol|
|----|----|
|read|	< |
|write|	> |
|append| >>|

#### Example
```perl
open(FH, '<', 'c:\sample.txt');
```
### Closing a file
```perl
close(FH);
```
|File test Operator| Description|
|----|----|
|-r| checks if the file is readable|
|-w| checks if the file is writable|
|-x| checks if the file is executable|
|-o| checks if the file is owned by effective uid.|
|-T| checks if the file is an ASCII text file.|
|-B| checks if the file is a binary file.|
|-e| checks if the file exists.|
|-z| checks if the file is empty.|
|-s| checks if the file has nonzero size.|
|-f| checks if the file is a plain file.|
|-d| checks if the file is a directory.|
|-l| checks if the file is a symbolic link.|
|-p| checks if the file is a named pipe (FIFO.|
|-S| checks if the file is a socket.|
|-b| checks if the file is a block special file.|
|-c| checks if the file is a character special file.|