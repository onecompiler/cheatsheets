---
title: Lua
description: Lua Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-06-23
updated: 2020-06-23
---

## Sample program

```lua
name = io.read("*a")
print ("Hello ", name)
```
* **io.read** : to read the data from console
* **print** : to output the data to console. 
* **--** : comment
* `--[[` Multi

    Line

    comments `--]]`


## Variables

* Lua is a dynamically typed language and hence only the values will have types not the variables.

### Examples

```c
-- global variables, variables are by default global
x = 10

-- local variables

local x = 30
```

## Data types

|Value Type| Description|
|-----|-----|
|number| Represents numbers|
|string| Represents text|
|nil|Differentiates values whether it has data or not|
|boolean|Value can be either true or false|
|function|Represents a sub-routine|
|userdata|Represents arbitary C data|
|thread|Represents independent threads of execution.|
|table|Can hold any value except nil|

## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %, -|
| comparision Operator| < , > , <= , >=, ~=, ==|
| Logical Operator| and , or, not |
| Misc Operator | .. , # |

There are no ++, --, ternary operators in lua

## String methods

|Method| Description|
|----|----|
| str1 .. str2| String concatenation|
|string.len(str) | To get the length of a string|
| string.gsub(str, "t1", "t2")| Used to Replace t1 with t2 in the string str|
|string.find(str, txt)| Searches for txt in str string and returns it's index|
|string.upper(str)| to change the str to upper case|
|string.lower(str)| to change the str to lower case|

## Conditional statements

### 1. If

```c
if conditional-expression then
--code
end
```

### 2. If-else

```lua
if conditional-expression then
   --code
elseif conditional-expression then
    --code
else
    --code
end
```
There is no switch in Lua

## Loops

### 1. While

```c
while(condition)
do
--code
end
```
### 2. Repeat-Until

```c
repeat
   --code
until( condition )
```

### 3. For

```c
for init,max/min value, increment
do
   --code
end
```

##  Functions

```lua
[function_scope] function function_name( argument1, argument2, argument3........, argumentn)
--code
return params with comma seperated
end
```
### Example

```lua
function sum(x,y)
	sum=x+y
	return sum
end

print(sum(10,20)) 
```