---
title: F#
description: F# Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-06-27
updated: 2020-06-27
---

## Sample program

```fs
open System
let name = Console.ReadLine()
Console.Write("Hello 0.\n", name)         
```
* **open** : used to import namespaces
* **let** : used to declare a variable. 
* **Console.ReadLine()** : to read input data from console
* **Console.Write()** : prints output data to the console
* **`//`** : single line comment
* `(*` Multi

    Line

    comments `*)`

F# does not have any specific entry point, F# compiler executes all the statements from top to bottom.

## Data Types

### Integer Data types
| Data type | Description | Size|Range|
|-----|-----|-----|----|
|sbyte|8-bit signed integer|1 byte|-128 to 127|
|byte|8-bit unsigned integer|1 byte|0 to 255|
|int16|16-bit signed integer|2 bytes|-32768 to 32767|
|unit16|16-bit unsigned integer|2 bytes|0 to 65,535|
|int/int32|32-bit signed integer|4 bytes|-2,147,483,648 to 2,147,483,647|
|uint32|32-bit unsigned integer|4 bytes|0 to 4,294,967,295|
|int64|64-bit signed integer|8 bytes|	-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|
|uint64|64-bit unsigned integer|8 bytes|0 to 18,446,744,073,709,551,615|
|bigint|arbitrary precision integer|At least 4 bytes|Integers|

### Float Data types
| Data type | Description | Size|Range|
|-----|-----|-----|----|
|float32|32-bit signed floating point number|4 bytes|±1.5e-45 to ±3.4e38|
|float|64-bit signed floating point number|8 bytes|	±5.0e-324 to ±1.7e308|
|decimal|128-bit signed floating point number|16 bytes|±1.0e-28 to ±7.9e28|

### Text and Boolean Data types
| Data type | Description | Size|Range|
|-----|-----|-----|----|
|char|single character|2 bytes|U+0000 to U+ffff|
|string|Text|20 + (2 * length of the string) bytes| 0 to up to 2 billion characters|
|bool|Stores either true or false|1 byte|True or false|

## Variables

```javascript
let variable_name:data-type = value
```
### Mutable variable declaration

```javascript
let mutable variable_name:data-type = value
```
## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %, **|
| comparision Operator| < , > , <= , >=, <> , ==|
| Bitwise Operator| &&& , ^^^ , \|\|\|, ~~~, <<<, >>>|
| Boolean Operator| && , `\|\|`, not |

## List

List is an ordered, immutable set of elements of the same type.

Lists can be defined in mutiple ways:
```javascript
let list1 = [1; 2; 3; 4; 5 ]

//or

let list2 = 1::2::3::4::5::[];;

// or

let list3 = [1:5] 
```
## Tuples

Tuples are collection of data of the same or different types.

```c
let directions =( "east", "west", "north", "south" ) // tuple of string type
let info = ( "foo", 123, true) // tuple of mixed types
```

## Maps

Map is a collection of key-value pairs.

```c
Map.empty. (* Creating an empty Map *)
      Add("India", "Hindi").
      Add("US", "English").
      Add("France", "French").
      Add("Japan", "Japanese");
```

## Conditional Statements

### 1. If
```java
if conditional-expression then
   // code
```
### 2. If-Else
```java
if conditional-expression then
   // code
else 
   // code
```
### 3. Nested If-Else

```java
if conditional-expression then
  // code
elif conditional-expression then
   // code
elif conditional-expression then
   // code
...
else
   // code
```

## Loops

### 1. For

#### For..to
Iteration occurs in ascending order.

```java
for var = start-expression to end-expression do
  // code  
```

#### For...down-to
Iteration occurs in descending order.

```java
for var = start-expression downto end-expression do
  // code  
```
#### For..in

```java
for pattern in enumerable-collection-expr do
   // code
```

### Example
```javascript
let listItems = [1,2,3,4,5]
for x in listItems do
   printfn "%d" x
``` 

### 2. While

```java
while condition-expr do   
 // code 
```

## Function

### How to define a function

```javascript
let [inline] function-name parameter-list [ : return-type ]
   = function-body
```

### How to call a function

```javascript
let Var = function-name parameter-list
```