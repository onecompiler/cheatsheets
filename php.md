---
title: PHP 
description: PHP cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-05-14
updated: 2020-05-14
---

## Basics

### Sample Program

```php
<?php
	echo "Hello, world!!!!"
?>
```
* **echo** : echo is used to output data to the console/screen.
* **print** : print is also used to output data to the screen. Both `echo` and `print` are more or less same with small differences, echo doesn't have a return value but print has a return value. echo can have multiple arguments but print takes only one argument. Echo is faster than print comparatively. 
* **fscanf** : fscanf is used to read input from console
* **//** : single line comment
* **\#** : Single line comment
* **/\* \*/** : Multi line comment

## Data Types

PHP is a loosely typed language and hence you no need to declare variables with data types.

However, below are the different datatypes in PHP.

| Data type | Usage|
|----|----|
| Integer |$x = 999999;|
| String | $str = "Hello World"|
| Float | $x = 79.53|
| Boolean | $isAvailable = TRUE;|
| Array | $arr = array("iPhone", 1000, TRUE);|
| Object | $obj = new className();|
| Null| $str = null;|
| Resource|$conn = mysqli_connect(localhost,"root","userName","password");|

## Variables

```php
$variable-name = value;  
```
## Constants

### Using define()

```php
define(name, value, case-insensitive)
```
* **name**: name of the constant
* **value**: value of the constant
* **case-insensitive**: Specifies whether the constant name should be case-insensitive or not. By default it is set to false.

### Using const keyword

```php
const MESSAGE = "Happy learning!";
```

## String Functions

|String Function| Usage|
|----|----|
| strlen() | echo strlen("One Compiler");|
| str_word_count() | echo str_word_count("Hello world! Happy Learning!!"); |
| strrev() | echo strrev("One Compiler"); |
| str_replace() | echo str_replace("bar", "Foo", "Good morning bar!"); |
| strpos() |  echo strpos("Hello world! Happy Learning!!", "appy"); |

## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %, ++, --|
| comparision Operator| < , > , <= , >=, != , ==| 
| Logical Operator| && , \|\|, ! |
| Assignment Operator|= , += , -= , *= , /= , %= |
| Conditional Operator| ? : |

## Arrays

```php
$arrName = array(values..);
```
### 1. Indexed arrays

```php
$directions = array("East", "West", "North", "South");
```

### 2. Associative arrays
```php
$capitals = array("Japan" => "Tokyo", "India" => "New Delhi","United Kingdom" => "London","United States" => "Washington, D.C.","China" => "Beijing");
```

### 3. Multi dimensional arrays

```php
// two-dimensional array
$num = array(
  array(1,2,3),
  array(4,5,6),
  array(7,8,9)
  );
```

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

### 3. If-else-if 

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
### 2. Foreach

```php
foreach ($array as $value) {
  //code 
}
```
### 3. While

```java
while(condition){  
//code 
}  
```

### 4. Do-while

```java
do{  
//code 
}while(condition); 
```
## Functions

```php
function functionName() { // defining a function
  //code
}

functionName (parameters); //calling a function 
```