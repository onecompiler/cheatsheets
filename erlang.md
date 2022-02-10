---
title: Erlang 
description: Erlang cheatsheet gives you a quick reference to code syntax with examples makes it handy while coding.
created: 2020-07-02
updated: 2020-07-02
---

## Sample program

```c
-module(helloworld).
-export([start/0]).
start() ->
		io:fwrite("Hello World!").
```
* **module** : It is used to add a namespace like in other programming language. 
* **export** : Any function which is defined in the program can be used by using export function. `/0` means that `start` function accepts 0 parameters.
* **start()** : start() is a function
* **io** : io is an module which has io all the required Input and Output functions.
* **fwrite** : to output data to the console.
* **%** : Used to provide comments

## Variables
Variables syntax is as follows

```c
variable-name = value
```
## Data types

| Data type| Usage| Description|
|----|----|----|
| Numeric| start() -> `io:fwrite("~w",[10+10])`. | Erlang supports both integer and float values.|
| Atom| start() -> io:fwrite(true) | Atoms should start with lower case leters and can contain  lowercase and uppercase characters, numbers, `_` and `@`. You can also put atom in single quotes|
| Boolean | start() ->  io:fwrite(10 =< 8)| Output will be either true or false based on the values given|
| Bit String|  str = <<10,20>>| Strings are enclosed in << >> and are used to store untyped memory|
| Lists| `[1,2,3]`| Lists is a compound data type with Variable number of elements.|
| Tuples| t = {apple, 100, {orange,50}} | Tuple is a compound data type with fixed number of elements.|
|Map| map = #{name=>onecompiler,message=>Learning}| Map is a compound data type with a variable number of key-value pairs|

## Operators
| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , rem, div|
| Relational Operator| < , > , <= , >=, /= , ==|
| Logical Operator| and, or, not, xor |
| Bitwise Operator | band, bor, bnot, bxor|

## Conditional Statements

### 1. If-Else

```c
if
condition ->
   true-statement;
true ->
   false-statement
end.
```

### 2. Case

```c
case value of
   value1 -> statement1;
   value2 -> statement2;
   valuen -> statementn
end.
```
### Note:
As Erlang is a functional programming language, there are no direct constructs for while, for and other loops. Recursion is the technique followed to implement loops in Erlang. 

## Function

### Defining a function
```c
FunctionName(Pattern1… PatternN) ->
%code
```
### Calling a function
```c
FunctionName(Pattern1… PatternN)
```
