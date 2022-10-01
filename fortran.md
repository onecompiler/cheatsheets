---
title: Fortran
description: Fortran cheatsheet contains useful code syntax with examples which is really handy while coding.
created: 2020-06-29
updated: 2020-06-29
---

## Sample program

```fortran
program hello
  character :: name
  read *, name
  print *, "Hello ", name
end program hello
```
* **program** : All Fortran programs start with the keyword `program` followed by program name
* **character :: name** : declaring a character variable named name
* **read** : to read the data from console
* **print** : to display the data to console
* **end program** : All Fortran programs end with the keyword `end program` followed by program name
* **!** : Comment

## Data Types

| Data type | Description | Usage|
|-----|-----|-----|
|Integer | To store integer variables|integer :: x|
|Real | To store float values | real :: x|
|Complex | To store complex numbers| complex :: x,y|
|Logical | To store boolean values True or false| logical :: x=.True. , logical :: x = .FALSE.|
|Character| To store characters and strings | character :: x|

## Variables

```
data type :: variable_name
```
### Example

```fortran
   ! declaring variables
   integer :: marks      ! Integer variable
   character(len=30) :: name ! string variable of length 30 characters
   
   !assigning values to variables
   marks = 60
   name = "Foo"  
```
## Derived Data types

```fortran
!Type Declaration
   type typeName      
      !declarations
   end type typeName

!Declaring type variables
   type(typeName) :: type-varName

!accessing the components of the derived type
   
   type-varName%type-declaration-variable = value
```
## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , **|
| Relational Operator| < , > , <= , >=, /= , ==|
| Logical Operator| .and. , .or. , .not. , .eqv. , .neqv.|

## Arrays

### Syntax

```fortran
data-type, dimension (x,y) :: array-name
```

### Example
```fortran
integer, dimension(3,3) :: cube
```
## Conditional Statements
### 1. If

```fortran
if (logical-expression) then      
   !Code  
end if
```

### 2. If-Else

```fortran
if (logical-expression) then     
   !code when the condition is true
else
   !code when the condition fails
end if
```

### 3. Case

```fortran
[name:] select case (regular-expression) 
   case (value1)          
   ! code for value 1          
   ... case (value2)           
   ! code for value 2           
   ...       
   case default          
   ! default code          
   ...   
end select [name]
```

## Loops

### 1. Do

```fortran
do i = start, stop [,step]    
   ! code
end do
```
### 2. Do-While

```fortran
do while (condition) 
   !Code
end do
```

## Function

A function is a procedure which returns a single value. 

```fortran
function functionName(arguments)  
  ! code 
end function [functionName]
```
### Calling a function
```fortran
functionName(arguments)  
```
## Sub-routines

Subroutine is a procedure which does not return a value.

```fortran
subroutine name(arguments)
  ! code  
end subroutine [name]
```

### Calling a Sub-routine
```fortran
call subroutineName(arguments)  
```
