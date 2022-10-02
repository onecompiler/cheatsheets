---
title: Go programming language
description: Go language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-05-01
updated: 2022-10-01
---

Go language is an open-source, statically typed programming language by Google. Go is highly recommended for creation of highly scalable and available web applications.

## Basics

### Sample Go program

```go
package main
import "fmt"

func main() {
	fmt.Printf("Go Hello, World!")
}
```
* `package` -- package declaration which is mandatory for all Go programs.
* `import "fmt"` -- used to import built-in fmt package.
* `func main()` -- function is the starting point of execution of any Go program.
* `fmt.printf` -- inbuilt library function which is used to print the given message.
* `fmt.Scanf` -- inbuilt library function which is used to read the data.
*  `//` --  to comment a single line
* `/**/` -- to comment multiple lines

## Variables

### Declaring Variables
```go
var variable-name data-type
```
### Assigning value to variables
```go
variable-name := value // It's not mandatory to declare a variable when you use this.
```
### Example
```go
var i int  // declaring int variable at functional level
j := 99 // short assignment without var declaration
```
## Data types

### 1. Numeric Data types

#### Integer Data types
| Data type | Description | Size|Range|Alias|
|-----|-----|-----|----|----|
|uint8|8-bit unsigned integer|1 byte|0 to 255|byte|
|int8|8-bit signed integer|1 byte|-128 to 127|*N/A*|
|int16|16-bit signed integer|2 bytes|-32768 to 32767|*N/A*|
|unit16|16-bit unsigned integer|2 bytes|0 to 65,535|*N/A*|
|int32|32-bit signed integer|4 bytes|-2,147,483,648 to 2,147,483,647|int (on 32 bit systems), rune|
|uint32|32-bit unsigned integer|4 bytes|0 to 4,294,967,295|uint (on 32 bit systems)|
|int64|64-bit signed integer|8 bytes|	-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|int (on 64 bit systems)|
|uint64|64-bit unsigned integer|8 bytes|0 to 18,446,744,073,709,551,615|uint (on 64 bit systems)|

#### Float Data types

| Data type | Description | Size | Alias |
|-----|-----|-----|-----|
|float32|32-bit signed floating point number|4 bytes|*N/A*|
|float64|64-bit signed floating point number|8 bytes|float|
|complex64|Number has float32 real and imaginary parts|8 bytes|*N/A*|
|complex128|Number has float64 real and imaginary parts|16 bytes|*N/A*|


### 2. Boolean Data types

| Data type | Description | Size|Range|
|-----|-----|-----|----|
|bool|Stores either true or false|1 byte|True or false|


### 3. String Data types
| Data type | Description |
|-----|-----|
|string|Sequence of characters|
|rune|Alias for uint32 but also represent single character in string|

### Example
```go
var (
	integer uint32 = 4294967295
	flt float64 = 3.14
    complexNum complex128 = cmplx.Sqrt(8 - 6i)
    str string = "Hello World"
    rne rune = 'A'
    boolean bool = true
)
```
## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %|
| comparision Operator| < , > , <= , >=, != , ==|
| Bitwise Operator| & , ^ , \|, &^, <<, >>|
| Logical Operator| && , \|\|, ! |
| Assignment Operator|= , += , -= , *= , /= , %=, <<=, >>=, &=, ^=, \|= |

## String Functions
| Function name | Description|
|----|----|
|len(str)| to return the length of string str|
|strings.Compare(a, b) | Compares two strings a and b lexically and returns `0` if the both strings are equal and `1` if string 1 is greater than string 2 and `-1` if string 1 is less than string 2.|
|strings.Contains(str, substr)| returns true if substring is found in the string str|
|strings.ToUpper(str)| to change the str to Upper Case|
|strings.ToLower(str)| to change the str to lower Case|
|strings.HasPrefix(str,"prefix")| returns true if the string str is starting with a prefix |
|strings.HasSuffix(str,"suffix")|  returns true if the string str is ending with a suffix |
|strings.Index(str, substr)| searches for a particular text within a string and returns it's index. If not found then it will returns -1.|
|strings.Join(stringSlice []string, sep string)| contanates the elements of an slice with seperators|
|strings.Count(str, sep string)| returns the count of number of non-overlapping instances of a character/string/text in string|

## Arrays

### Syntax
```go
var array-name[size] data-type; // declaration of an array
array-name := [size] data-type {value0,value1,…,value_size-1} // assigning values to array
```
### Example
```go
var fruits [3] string //Declaring a string array of size 3
fruits[0] = "Mango"
fruits[1] = "Apple"
fruits[2] = "Orange"
arr := [...] int {1,2,3,4,5} //Declaring a integer array of size 5
```

## Conditional Statements

### 1. If
```go
if (conditional-expression) {
    //code
}
```
### 2. If-else

```go
if (conditional-expression) {
    //code
} else {
    //code
}
```
### 3. If-else-if ladder

```go
if (conditional-expression-1) {
    //code
} else if (conditional-expression-2) {
    //code
} else if (conditional-expression-3) {
    //code
}
....
else {
    //code
}
```
### 4. Switch

```go
switch (conditional-expression) {
case value1:
    //code
    break;  //optional
case value2:
    //code
    break;  //optional

...

default:
    //code to be executed when all the above cases are not matched;
}
```
## Loops

### 1. For
```go
for (Initialization; Condition; Increment/decrement) {
    //code
}
```
### 2. while

Go doesn't have `while` as a keyword, you can use `for` instead.

```go
for (condition) {
    //code
}
```
### 3. Do-While
Go doesn't have `do...while` you can improvised using for.

```go
for (true) {
    //code
    if(!conditional-expression) {
        break;
    }
}
```

## Functions

```go
func function_name(parameters) return_type { // defining a function
  //code
}
function_name(parameters) // calling a function
```

## Pointers

```go
var pointername *datatype;
```

### Example

```go
num := 10;
var ptr *int;   // pointer variable
ptr = &num;
```

## Structures

```go
type structure_name struct { // defining a structure

   member definition;
   member definition;
   ...
   member definition;
}

var structure-variable structure-name //declaring a structure variable
```
## Slice
A slice can be formed from an array using a low and high bound indices which are separated by a colon:

```go
array-name[lowIndex : highIndex]
```
* Slices never store any data
* Slices just describes the section of an array
* If you modify the elements present in a Slice, it's corresponding array elements also will see changes.
* If you omit high or low bounds while slicing, Go automatically use their defaults instead. The default values for low bound is zero and for the high bound is the length of the slice.
* Slice can be created by using built-in function `make`. The below creates a slice `[0 0 0 0 0]`

## Maps

Maps is an unordered collection of key and its value.

```go
var map-name map[key-data-type]value-data-type //declaring a map
map-name = make(map[key-data-type]value-data-type) //defining a map
```
## Concurrency

Go supports concurrent execution of tasks using Goroutines and Channels.

### Go-routines

Advantage of Go-routines is that the control will not wait for the execution of function to complete. It will just call the function and continue to execute the rest of the code. Function execution will happen in concurrent with the rest of code execution.

```go
go function-name([arguments])
```
### Channels

Channels are like medium where we send values from one goroutine to another.

#### Declaring a channel

```go
var channel-name chan Data-Type
```
or

```go
channel-name := make(chan Data-Type)
```
## Generics

Generics allow you to declare and use functions or types that are written to work with any of a set of types provided by calling code. *(Generics are only present in **Go 1.18 or later**. Prior versions of Go do not have generics.)* 

```go
//For a function, you can declare the types you want to work with by the following template:
//func Signature[MyTypes type1 | type2 | type3...] (value MyTypes) {
}
```
### Example
```go

func ReverseSlice[GenericTypes int | string | bool](slice []GenericTypes) {
	leftIndex := 0
	rightIndex := len(slice) - 1
	for leftIndex < rightIndex {
		slice[leftIndex], slice[rightIndex] = slice[rightIndex], slice[leftIndex]
		leftIndex++
		rightIndex--
	}
}

	stringSlice := []string{"Foo", "Bar", "Baz"}
	intSlice := []int{1, 2, 3}
	boolSlice := []bool{true, false, false}
	
	ReverseSlice(stringSlice) //[Baz Bar Foo]
	ReverseSlice(intSlice)    //[3 2 1]
	ReverseSlice(boolSlice)   //[false false true]


```
You can also declare the types you're working with via an Interface as well! Building off the same example above...
```go
type MyTypes interface {
int | string | bool
}

func ReverseSlice[GenericTypes MyTypes](slice []GenericTypes) {
//...
}
```
