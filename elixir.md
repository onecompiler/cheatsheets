---
title: Elixir
description: Elixir programming language cheatsheet contains useful code syntax which is handy while coding.
created: 2020-06-28
updated: 2020-06-28
---
## Sample program

```elixir
IO.puts "Hello, World!"
```
* **IO.puts** : To print output data to the console
* **#** : comment

## Variables
Variables must be declared and assigned a value.

```elixir
variable-name = value
```
## Data types

| Data type| Usage| Description|
|----|----|----|
| Numeric| x = 21 | Elixir supports not only integer and float values but also a number can be defined in octal, hexadecimal and binary bases.|
| Atom| :true | Atoms are constant values whose name is same as their value|
| Boolean | : false, :true| Either true or false, usually declared as atoms|
| Strings| "Hello"| Strings are enclosed in double quotes(" ") and multi line strings are enclosed in triple double quotes(""" """)|
| Lists| \['a', 10, :true\]| Lists are used to store different types of values and are represented in square brackets []|
| Tuples| {'apple', 100, :false} | Similar to Lists and are represented in curly brackets {}. Tuples are good for accessing the values and lists are good for insertion and deletion of values|

## Reserved Keywords

|||||||
|----|----|----|----|----|----|
| after | and | catch | do | inbits | true|
| inlist | nil | else | end | not |  when|
| or| false | fn | in | rescue |   xor |


## Operators
| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , div, rem|
| comparision Operator| < , > , <= , >=, !=, !==, === , ==|
| Bitwise Operator| &&& , ^^^ , \|\|\|, ~~~, <<<, >>>|
| Boolean Operator| and , or, not, &&, \|\|, ! |

## Conditional Statements

### 1. If

```elixir
if condition do
  #Code 
end
```
### 2. If-Else

```elixir
if condition do
  #Code 
else
  #code
end
```
### 3. Case

```elixir
case value do
  value-1 -> #code if value matches value-1
  value-2 -> #code if value matches value-2
  value-3 -> #code if value matches value-3
  ...
  _ -> #code if value does not match any of the above and is similar to default in switch
end
```

## Loops
### 1. Unless

```elixir
unless condition do
  #Code 
end
```

### 2. Unless-Else

```elixir
unless condition do
  #Code if condition fails
else
  #Code if condition satisfies
end
```
### 3. Cond

```elixir
cond do
  condition-1 -> #code if condition is true
  condition-2 -> #code if condition is true
  ...
  true -> #code if none of the above are true
end
```

## List

List is a collection of data of the same or different types and are stored in memory as linked lists.

```elixir
["foo", 123, true]
```

|List Functions| Description|
|----|----|
| length()| returns the length of a list|
| ++ | used to concatenate two lists by adding list items|
| -- | used to concatenate two lists by substracting list items|
| hd(list)| to get the first element of the list|
| tl(list)| to get last element of the list|
|  delete(list, item) | to delete an item from the list|
| delete_at(list, index) | to delete an item at given index from the list|
|insert_at(list, index, value)| to insert given item at specific index of a list|

## Tuples

Tuples are collection of data of the same or different types and are stored contiguously in memory.

```elixir
tuple = {:foo, :bar}
Tuple.append(tuple, :john) # appends an item to tuple
```

## Maps

Map is a collection of key-value pairs.

```elixir
map = %{1 => :one, 2 => :two, 3 => :three, 4 => :four, 5 => :five}
```

## Functions

Function is a sub-routine which contains set of statements. 

1. Anonymous Functions:

Anonymous functions are functions with no name and they use  `fn..end` constructs.

2. Named functions:

Assign names to functions so that they can be called easily. Always named functions are defined in modules.

```elixir
defmodule ModuleName do
  def function_name(parameter1, parameter2) do
    #code 
  end
end
```
