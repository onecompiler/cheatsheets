---
Title: Rust programming language
Description: Rust language cheatsheet contains useful code snippets with explanations that describe each of the features
Created: 2022-10-04
Updated: 2022-10-04
---

Rust is a modern systems programming language developed by the Mozilla Corporation and is intended to be a language for highly concurrent and highly secure systems

### Simple Rust Program

```rs
fn
main(){
   println!("Rust says Hello to TutorialsPoint !!");
}
```
The above program defines a function main fn main().The fn keyword is used to define a function. The main() is a predefined function that acts as an entry point to the program.
The println! is used to print the string in Rust

### Datatypes

```rs
fn main() {
   let stri = "Rust";  // string type
   let deci = 7.9;                 // float type
   let flag = true;          // boolean type
   let ans = 23;  //integer type
   let character = 'a';  //character type
}
```

### Variables

The data type is optional while declaring a variable in Rust. The data type is inferred from the value assigned to the variable.
```rs
fn main() {
   let load = 40_000;
   let percent = 23.45;
   let chance= 'b';
}
```
Variables are immutable by default. Prefix the variable name with mut keyword to make it mutable.


### Operators

The major operators in Rust are as follows −

Arithmetic
Bitwise
Relational
Logical

The various Arithmetic Operators are +(Addition), -(Subtraction),* (Multiplication), / (Division) and % (Modulo)

Bitwise operators used in Rust are & (Bitwise AND) , | (Bitwise OR) , ^ (Bitwise XOR), ! (Bitwise NOT)

Relational Operators used in Rust are >, <, >=, <=, ==, !=

Logical Operators used in Rust are && , || and !.

### Strings

String literals in Rust are used when the value of a string is known at compile time.

```rs
fn main() {
   let site:&str="Working";
   let quality:&str = "Excellent";
   println!("site is : {} quality :{}",site,quality);
}
```
String literals are static by default. This means that string literals are guaranteed to be valid for the duration of the entire program.

### Conditional Statements

#### If-else statement:

```rs
fn main(){
   let num = 2;
   if num > 0 {
      println!("number is positive") ;
   }
}
```
The if…else construct evaluates a condition before a block of code is executed. If the Boolean expression evaluates to true, then the block of code inside the if statement will be executed, otherwise the else part is executed.

#### Nested If statement:

```rs
fn main() {
   let num = 2 ;
   if num > 0 {
      println!("{} is positive",num);
   } else if num < 0 {
      println!("{} is negative",num);
   } else {
      println!("{} is neither positive nor negative",num) ;
   }
}
```
The Nested if condition is used to check multiple conditions.

### Loops

#### For loop

```rs
fn main(){
   for x in 1..10{ // 10 is not inclusive
      println!("x is {}",x);
   }
}
```
The for loop executes the code block for a specified number of times

#### While loop

```rs
fn main(){
   let mut x = 10;
   while x > 0{
      x-=1;
      println!("x value is {}",x);
   }
}
```
The while loop executes the instructions each time the condition specified evaluates to true

### Arrays

Syntax for declaring,initializing and displaying an array in Rust.

```rs
fn main(){
   let arr1:[i32;4] = [10,20,30,40];
   let arr2:[i32;4] = [1,2,3,4];
   println!("array1 is {:?}",arr1);
   println!("array2 is :{}",arr2);
}
```

### Structures

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


