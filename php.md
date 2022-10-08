---
title: PHP 
description: PHP cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-05-14
updated: 2022-10-08
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
$variable_name = value;  
```
## Constants

### Using define()

```php
define(name, value, case_insensitive)
```
* **name**: name of the constant
* **value**: value of the constant
* **case_insensitive**: Specifies whether the constant name should be case-insensitive or not. By default it is set to false.

```php
define("GREETING","Hello you! How are you today?");
echo constant("GREETING");
```

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
| str_repeat() |  echo str_repeat("Hello! Happy Learning!!", 4); |
| rtrim() |  echo rtrim("  Right space will be trimmed   "); |
| ltrim() |  echo rtrim("  left space will be trimmed   "); |
| strcmp() |  echo strcmp($string1,$string2); |

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

## Date
(PHP 4, PHP 5, PHP 7, PHP 8)
```php
date_default_timezone_set('America/Los_Angeles');// set default time zone( Useful while deploying to server)
$dateVal=date("F j, Y, g:i a"); // March 10, 2001, 5:16 pm

```

## File
| Function | Syntax | Description |
|----|----| ---- | 
| readfile() | readfile(myfile.txt) |  prints the contents of myfile.txt in browser|
| fopen(filename, mode) | fopen("myfile.txt", "r") | opens myfile.txt in read mode | 
| fread(file, length) | fread($fptr, filesize("myfile.txt")) | read file upto length and stores in file pointer | 
| fclose() | fclose($fptr) | The fclose() function closes an open file pointer |

## MySQLi Functions
These functions allow you to access MySQL database server.

| Function | Description|
|----|----|
| mysqli_connect() | It opens a non-persistent MySQL connection |
| mysqli_affected_rows() | It returns the number of affected rows |
| mysqli_connect_error() | It shows the Error description for the connection error | 
| mysqli_fetch_all() | It fetches all result rows as an array | 
| mysqli_fetch_array() | It fetches a result row as an associative, a numeric array, or both |
| mysqli_fetch_assoc() | It fetches a result row as an associative array |
| mysqli_fetch_row() | It fetches one row from a result set and returns it as an enumerated array | 
| mysqli_kill() | It kills a MySQL thread | 
| mysqli_close() | It closes a database connection |
| mysqli_query() | It runs any sql query from database in php |
| mysqli_num_rows() | It counts number of rows affected after running any sql query |

## Global Variables - Superglobals

| Variables | Usage|
|----|----|
| $_SERVER | $_SERVER['REQUEST_METHOD']	Returns the request method used to access the page (such as POST) |
| $_POST | $name = $_POST['fname'] collects value from a form(name='fname') and stores to $name after submitting an HTML form with method="post" |
| $_GET | $_GET can also collect data sent in the URL |
 