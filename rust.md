---
title: Rust 
description: Rust cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2022-10-04
updated: 2022-10-05
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

## Strings

String literals in Rust are used when the value of a string is known at compile time.

```rs
fn main() {
   let site:&str="Working";
   let quality:&str = "Excellent";
   println!("site is : {} quality :{}",site,quality);
}
```
String literals are static by default. This means that string literals are guaranteed to be valid for the duration of the entire program.

## Arrays

Syntax for declaring,initializing and displaying an array in Rust.

```rs
fn main(){
   let arr1:[i32;4] = [10,20,30,40];
   let arr2:[i32;4] = [1,2,3,4];
   println!("array1 is {:?}",arr1);
   println!("array2 is :{}",arr2);
}
```

## Tuples

Tuples are a compound datatype and have a fixed length - once declared they cannot grow or shrink in size. Indexing in Tuples start from zero

```rs
fn main() {
   let tuple:(i32,f64,u8) = (-325,4.9,22);
   println!("integer is :{:?}",tuple.0);
   println!("float is :{:?}",tuple.1);
   println!("unsigned integer is :{:?}",tuple.2);
}
```

## Structures

A structure defines data as a key-value pair.The struct keyword is used to declare a structure. Since structures are statically typed, every field in the structure must be associated with a data type.

```rs
struct student {
   name:String,
   Grade:String,
   age:u32
}
fn main() {
   //initialize a structure
   let st1 = student {
      Grade:String::from("A+"),
      name:String::from("John"),
      age:20
   };
   let st2 = student{
      Grade:String::from("B+"),
      name:String::from("Jack"),
      age:19
   };
}
```

## Enums

In Rust programming, when we have to select a value from a list of possible variants we use enumeration data types. An enumerated type is declared using the enum keyword.

```rs
enum Roles {
   Developer,Designer
}
fn main() {
   let m1 = Roles::Developer;
   let m2 = Roles::Designer;

   println!("{:?}",m1);
   println!("{:?}",m2);
}
```


