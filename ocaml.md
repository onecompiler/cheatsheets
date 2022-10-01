---
title: Ocaml 
description: Ocaml Programming language cheatsheet gives you a quick reference to code syntax with examples makes it handy while coding.
created: 2020-07-01
updated: 2020-07-01
---


## sample program

```ocaml
print_string "Hello world!"
```

* **print_string** : is used to print the given string
* `(*` Single line comments `*)`
*  `(*` Multi
    
    `*` line
 
     `*` comment.
     
    ` *)`

## Data types

| Classification | Data-types |
|----|----|
| Basic data types| int, float, bool, char, string, unit.|
| Sophisticated data types| tuples, arrays, lists, sets, hash tables, queues, stacks, data streams.|

## Variables

```ocaml
let varible-names = value
```
### Example
```ocaml
let a = 100;
```
## Conditional Statements

### 1. If

```ocaml
if boolean-condition then (* code if condition is true *)
```

### 2. If-else
```ocaml
if boolean-condition then (* code if condition is true*) else (* code if condition is false*)
```

## Loops
### 1. While

```ocaml
while boolean-condition do
  (* code *)
done
```

### 2. For

```ocaml
for var = start-value to end-value do
  (* code *)
done
  
for var = start-value downto end-value do
  (* code *)
done
```

## Lists
```ocaml
let listName= [item1;item2;item3]
```

## Tuple
```ocaml
let tupleName  : datatype * datatype * ... = (value, value, ...);;
```

## Functions

### How to define a function

```ocaml
let funcName (arguments) =
    (* code *)
```

### Call a function

```ocaml
funcName arguments
```
### Example
```ocaml
(* Defining the function*)
let sum a b =
 (a+b)

(* calling a function)
sum 3 7
```