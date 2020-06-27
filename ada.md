---
title: Ada
description: Ada Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-06-24
updated: 2020-06-24
---

## Sample program

```ada
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
		Put_Line ("Hello, World!");
end Hello;
```
* **ada.text_io** : package that contains routines for i/o of text
* **with** - tells compiler that the package will be used
* **use** : tells compiler that the package should be automatically searched and allows access to routines without using the fully qualified name
* **procedure** : used to declare a procedure named Hello here.
* **Put_line** : is a procedure for string output. 
* **--** : comment

## Variables

```ada
varName : DataType := value
```
## Constants
```ada
varName : Constant DataType := value
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
begin
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

### Syntax for procedure

```ada
procedure proc-name
(X : in Integer ; Y : out Integer ; Z : in out Integer ) is
begin
X := 10; −− it's an Error as you can’t modify an in parameter.
Y := X; −− can modify Y as it's an out parameter.
Z := Z + 1; −− can read and write as it's an in out parameter.
end proc-name;
```
### Syntax for functions

```ada
function function_name(declaration) return value is
begin
--code
end function-name;
```
