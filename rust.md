---
title: Rust 
description: Rust cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2022-10-04
updated: 2020-10-04
---

## Basics

### Sample program
```rust
fn main(){
   println!("Hello World");
}
```
* `//` : Single line Comment
* /* This is a Multi-line comment */

## Variables


Begins with `let` 
```rust
let a = "hello";
```
### Mutable
```rust
fn main() {
    let mut a:i32 = 10;
    println!("{}",a);
    a = 20;
    println!("{}",a);
}
```

## Constants
Begins with `const` 
```rust
const USER_LIMIT:i32 = 100;    // Declare a integer constant
const PI:f32 = 3.14;           //Declare a float constant
```

## Operators
|Type|Operators|
|----|----|
| Arithmetic Operators| + , - , * , / , %  |
| Relational Operators| == , != , > , >= , < , <= |
| Bitwise Operators| & , ^ , \| , << , >> |
| Logical Operators| && , \|\| , ! |


## Conditional Statements

### 1. If

```rust
if conditional-expression {
    #code
}
```
### 2. If-else

```rust
if conditional-expression {
    #code
}
else {
    #code
}
```
### 3. Nested If-else

```rust
if conditional-expression {
    #code
}
else if conditional-expression {
    #code
}
else {
    #code
}
```

## Loops

### 1. For

```rust
for temp_variable in lower_bound..upper_bound {
   #code
}
```

### 2. While

```rust
while conditional-expression {
   #code
}
```

## Methods

```rust
fn function_name(param1,param2..paramN) {
   #code
}
```
### Example
```rust
fn fn_hello(){
   println!("hello from function fn_hello ");
}

fn main(){
   //calling a function
   fn_hello();
}
```
