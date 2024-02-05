---
title: Ada
description: Ada Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-06-24
updated: 2024-02-05
---

## Data types

* Strongly typed

| Types | Data-type|
|----|----|
|Basic | Integer, Character, Float, Long_Float, Short_Integer, Long_Integer, etc |
|Pointer | access |
|Composite | array, String |
|User Defined Data Type | record, enumeration, tagged type, variant record, range types, etc. |


### Naming convention
* First character in identifier is a letter, then letters (both uppercase and lowercase letters), digits and underscore(`_`).
* Case insensitive

## Arrays

```ada
array-name : array (Fist..Last) of element-type; -- one-dimensional Array
array-name : array (Fist1..Last1, First2..Last2) of element-type; -- two-dimensional Array
```
## String

It is an array of Character.

```ada
My_String := String := "abcde"; -- string declaration
```

## Literals or Constants
|Literal | Example|
|----|----|
|Integer Literal- decimal|255|
|Integer Literal- octal|8#377#|
|Integer Literal- hexadecimal|16#FF#|
|Float point Literal|53.0, 79e-6|
|Character literals| 'a', '1'|
|String literals| "OneCompiler", "Foo"|
|Boolean literals| True, False|

### Special characters
Special characters are defined as constans in `ASCII` or `Ada.Characters.Latin_1` package.
|Constant| Description|
|----|----|
|LF	| New line|
|CR	| Carriage Return|
|HT	| Horizontal tab|
|VT	| Vertical tab|
|NUL | Null character|

## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , `**` (exponentiation)|
| Relational Operator| < , > , <= , >=, /= , =|
| Logical Operator| `and` , `or`, `xor`, `not` |
| Assignment Operator| := |
| If expression| (if a then b else c) |

## Sample program

```ada
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
   Put_Line ("Hello, World!");
end Hello;
```
* `Ada.Text_IO` : package that contains routines for I/O of text.
* `with` : tells compiler that the package will be used.
* `use` : tells compiler that the package should be automatically searched and allows access to routines without using the fully qualified name.
* `procedure` : used to declare a procedure named Hello here.
* `Put_Line` : is a procedure for string output. 
* `--` : comment.

## Variables

```ada
varName : DataType := value;
```
## Constants
```ada
varName : constant DataType := value;
```
## Conditional Statements

### 1. If-else
```ada
if conditional-expr then 
    --code if above statement is true
elseif conditional-expr then 
    --code if above statement is true
end if;
```

### 2. Case
```ada
case expr is 
    when expr => --code
    when expr => --code
    ...
    when others => --code;
end case;
```
## Loops

### 1. Infinite loop:

This is the simplest loop

```ada
   Index := 1; --initialization
   loop                            
      --code
      exit when Index = n;
   end loop;
```
### 2. while loop

```ada
   Count := 1;    --initialization
   while Count < n loop  
      --code
   end loop;
```

### 3. for loop

```ada
for Index in 1..n loop          
   --code
end loop;
```
## Sub programs

Functions and procedures are collectively called as sub-programs.

### Syntax for procedures

```ada
procedure proc_name
   (X : in Integer ; Y : out Integer ; Z : in out Integer ) is
begin
   X := 10; −− it's an Error as you can’t modify an in parameter.
   Y := X; −− can modify Y as it's an out parameter.
   Z := Z + 1; −− can read and write as it's an in out parameter.
end proc_name;
```
### Syntax for functions

```ada
function function_name(parameter : parameter_type) return value is
begin
   --code
end function_name;
```
