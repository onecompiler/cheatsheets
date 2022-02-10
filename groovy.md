---
title: Groovy
description: Groovy cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-05-05
updated: 2020-05-05
---

## Basics

### Sample Program

```java
println "Hello World!"
```
* `println` -- inbuilt library function which are used to display the output.
* `//` -- single line comment
* `/* comments */` -- Multi line comment

## Data types

| Data type | Description | Example|
|----|----|----|
| int| used to represent whole numbers| int x = 99999|
|short| used to represent whole numbers| short x = 999 |
|long| used to represent whole numbers| long x = 99999999999L |
|float| used to represent fractional numbers| float x = 22.79f|
|double| used to represent fractional numbers|double x = 99.99d|
|char|used to represent a single character|char grade = 'A'|
|boolean| used to represent Boolean data either true or false| boolean isAvailable = true|
|byte| Used to represent a byte value| byte x = 99 |
|string | used to represent a series of characters| string msg = "Happy learning!" |

### Example

```java
int int_var = 99999 // integer variable
short short_var = 999 // short variable
long long_var = 99999999999L // long variable
float float_var = 22.79f // float variable
double double_var = 99.99d // double variable
char char_var = 'A' // char variable
boolean isAvailable = true // boolean variable
byte byte_var  = 99 // byte variable
String msg = "Happy learning!" // String variable
```

## Variables

There are three ways to declare variables in Groovy.

1. Native syntax similar to Java

```java
data-type variable-name = value;
```
2. Using def keyword

```java
def variable-name = value;
```
3. Variables in groovy do not require a type definition.

```java
variable-name = value; // no type definition is required
```

## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operators|+ , - , * , / , %|
| comparision Operators| < , > , <= , >=, != , ==|
| Bitwise Operators| & , ^ , \||
| Logical Operators| && , \|\|, ! |
| Assignment Operators|= , += , -= , *= , /= , %=|

## Strings

```java
String string-var = value; 
```
value should be enclosed in either single quotes `’`, double quotes `“`, or triple quotes `“””` or forward slash `/` or dollar-forward slash `$/`.

```java
String str = "Happy learning!"; 
String str2 = 'Hello World';
String str3 = """Hey
Good 
Morning"""
```
## Lists
List is like stack which is used to store  collection of data items.

```java
def list1 = [ ] // empty list

def list2 = [ 1,2,3,4,5] // integer list

def list3 = ["Hello", "World"] //string list

def list4 = ["happy", 16] // list with different data
```
### Methods

|List methods | Description|
|----|----|
| add() | to append the new value to the end of this List.|
| contains() | Returns true if the list contains the given value.|
| get() | to get the element at the specified position from the List.|
| isEmpty() | Returns true if the given List is empty|
| minus() | to create a new List with the elements of the original list by removing those specified in the collection|
| plus() | to create a new List with the elements of the original list by adding those specified in the collection|
| pop() | to remove the last item from the List |
| remove() | to removes an element at the specified position in the List.|
| reverse() | to create a new List which is the reverse of the elements of the given List|
| size() | to get number of elements present in the List.|
| sort() | Returns a sorted copy of the given List.|

## Maps

A Map is an unordered collection of Key Value Pairs
```java
def map1 = [‘Name’ : ‘OneCompiler’, ‘Category’ : ‘Learning’]
def map2 = [:] // empty map
```
### Methods
| Method name | Description|
|----|----|
| containsKey() | Used to check if a key is present in a given Map|
| get() | Looks for the key in the map and returns it's corresponding value.If there is no match then returns null|
| keySet() | to obtain set of keys in the given Map.|
| put() | used to associate the given value with the key specified in the Map. If already value is present for that key, then the old value gets replaced by the new value.|
| size() | Returns the number of key-value pairs present in the Map.|
| values() | Returns a collection view of the values present in the Map.|

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

### 1. While
```java
while(condition){  
//code 
}  
```
### 2. For
```java
for(Initialization; Condition; Increment/decrement){  
//code  
} 
```

### 3. For..in

```java
for (var in range) {
  //code
}
```

## Groovy closures

```java
{ [closureParameters -> ] statements }
```
### Examples
```java
{ x++ }         // only statement                                 

{ -> x++ }     // statement with no parameters                                  

{ name -> println name }  // statement with one closure parameter  with no type definition                         

{ String name, int id ->   // statement with two closure parameter has type definition                          
    println "hi ${name}, your id is ${id}" 
}
```
### Groovy Closure Methods

| Method name | Description |
|----|----|
| any() & every() | Iterates through each element of a collection checking whether given criteria is valid for at least one element.|
| find() | Finds the first value in a collection which matches the given criteria. |
| findAll() | Finds all values in a collection which matches the given criteria.|
| collect() | Iterates through a collection and converts each element into a new value using the closure as the transformer.|

## Method

Method is a sub-routine which contains set of statements which increases re-usuability and modularity.

```java
def methodName(parameters) {  // defining a method
   //Method code 
}

methodName(parameters); // calling a method
```