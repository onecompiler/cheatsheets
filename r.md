---
title: R 
description: R cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-05-11
updated: 2022-10-09
---

R is very popular for data analytics which was created by Ross Ihaka and Robert Gentleman in 1993. Many big companies like Google, Facebook, Airbnb etc uses this language for data analytics.

## Basics

### Sample program

```java
print("Hello, World!")
```
* **print** -- It is used to display the data to the console.
* **cat** -- you can also use cat to display data to console.
* **#** -- is used to comment a line in R and it does not support multi-line comments.

## Data types

There are six data types of the atomic vectors:

| Data type | Description | Usage |
|----|----|----|
|Numeric|To represent decimal values| x=1.84|
|Integer| To represent integer values, L tells to store the value as integer| x=10L|
|Complex| To represent complex values | x = 10+2i|
|Logical| To represent boolean values, true or false | x = TRUE|
|Character| To represent string values | x <- "One compiler"|
| raw | Holds raw bytes||

## Variables

```c
var-name = value
var-name <- value
value -> var-name
```
### Example
```java
var_logical <- FALSE  # Logical variable
  
var_numeric -> 797 # Numeric variable
  
var_integer = 53L  # integer variable
  
var_complex <- 5+2i  # complex variable
  
var_char<- "One Compiler"  # character variable
  
var_raw <- charToRaw("Hello World")  # raw variable
```
## Operators
| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %%, ^|
| Relational Operator| < , > , <= , >=, != , ==|
| Logical Operator| &, \|, && , \|\|, ! |
| Assignment Operator|= , ->, ->>, <-, <<- |
| Misc Operators| :, %in%, %*%|

## Strings

`'` or `"` are used to enclose strings in R.

```java
str1 <- "Hello World!"
print(str1)
str2 <- 'Happy learning!!'
print(str2)
```
|String Function| Description|
|----|----|
| paste() | Strings are concatenated using paste() function|
| format() | This function is used to format Numbers and strings  to a specific style.|
| nchar() | This function is used to count the number of characters including spaces in the given string.|
| substring() | This function is used to extract part of a string|
| toupper() | Converts given string to uppercase|
| tolower() | Converts given string to lowercase|

## Vectors

Vectors are considered as basic R objects.

### Single Element Vectors

```java
x <- "s" #Character type atomic vector
x <- 53.2 #double type atomic vector
x <- 79L #integer type atomic vector
x <- TRUE # Logical type atomic vector
x <- 2+5i# complex type atomic vector
x <- charToRaw('OneCompiler') #  raw type atomic vector.
```
### 2. Multiple Elements vector

```java
x <- 1:10 # Creating a sequence from 1 to 10 using colon
x <- 5.5:10.5 # Creating a sequence of decimal values using colon
x <- seq(1, 5, by = 0.5) # creating sequence using seq()
x <- c('hello', 0, 3, TRUE) # mixed type vector
```

## Lists
List is a R-Object which can contain elements of different types. list() function is used to create a list.  

```r
emp_list <- list( c("Foo","Bar", "Alex", "Mark"), c(1,2,3,4)) # creating a list

names(emp_list) <- c("Names","Id") # assigning name to the list items

print(emp_list)
```
## Arrays
`array()` function is used to create an array in R.

```java
arrayName <- array(data, dim= (rowSize, columnSize, matrices, dimNames))  
```
* **data** : data is an input vector
* **rowSize** : defines no of row elements array can store
* **columnSize** : defines no of column elements array can store
* **dimNames** : specifies row and column names
* **matrices** : array can consists of multi-dimensional matrices

### Example

```py
x <- c(1,2,3)
y <- c(4,5,6,7,8,9)

arr <- array(c(x,y),dim=c(3,3,3)) # 3 rows, 3 columns and 3 matrices

print(arr[,,3]) # prints 3rd matrix

print(arr[2,,2]) # prints 2nd row in second matrix

print(arr[3,3,1]) # prints 3rd row 3rd column element of 1st matrix
```
## Matrix

Matrix is a two-dimensional rectangular data set. Elements of a matric will be of same atomic type. 
```r
matrix(data, rowSize, columnSize, byrow, dimnames)
```
* **data** : data is an input vector
* **rowSize** : defines no of row elements array can store
* **columnSize** : defines no of column elements array can store
* **byrow** : If it is set to TRUE then the input vector elements are arranged by row.
* **dimNames** : specifies row and column names

## Factors

Factor is a data object which is used to take a limited number of different values and categorize them into multiple levels.

```py
factorData<- factor(inputVector) #`factor()` function is used to convert a vector into factor.
is.factor(factorData) # `is.factor()` is used to check whether the input given is a factor or not.
```
## Data Frames
Data Frame is a data object which has like a 2D array like structure where column contains value of a variable and row contains one set of values from each column.

* Column names should be non-empty.
* Row names should be unique.
* Data in a data frame can contain different types of data like a factor, numeric, or character type.
* Every column will have same number of data items.

`frame()` function is used to create a data frame.

### Example
```r
student.data <- data.frame(
   studentID = c (101:104), 
   firstName = c("Foo","Bar","Alex","Mark"),
   marksPercentage = c(97.2,79.2,53.9,87.3), 
   
   joiningDate = as.Date(c("2010-06-01", "2010-06-10", "2010-06-04", "2010-06-02")),
   stringsAsFactors = FALSE
)
print(student.data)
```
## conditional statements
### 1. If
```py
if(conditional-expression)
{
    # code
}
```
### 2. If-else

```py
if(conditional-expression)
{
    # code
} else {
    # code
}
```
### 3. Switch

```py
switch(expression, case-1, case-2, case-3....)   
```

## Loops
### 1. For

```py
for (value in vector) {
  # code
}
```
### 2. While

```py
while(condition){  
#code
}  
```
### 3. Repeat

```py
repeat { 
   #code
   if(condition) {
      break
   }
}
```
## Functions

Function is a sub-routine which contains set of statements.

```py
function_name <- function(arg1, arg2, ...) { # defining a function
  #code 
}

function_name(arguments) # calling a function
```
### Example 
```py
sum <- function(x, y) {
  cat("Sum:", x+y)
}

sum(10, 20)
```
## Matrix operations 

### 1. Is Something a Matrix
```py
is.matrix(A)               # Returns a boolean value 
```

### 2. Addition of two matrices 
```py
A <- matrix(c(2,3,-2,1,2,2),3,2)
B <- matrix(c(1,4,-2,1,2,1),3,2)
C <- A + B                # Returns a sum matrix
```

### 3. Subtraction of two matrices 
```py
A <- matrix(c(2,3,-2,1,2,2),3,2)
B <- matrix(c(1,4,-2,1,2,1),3,2)
D <- A - B                # Returns a difference matrix
```

### 4. Matrix multiplication 
```py
A <- matrix(c(2,3,-2,1,2,2),3,2)
B <- matrix(c(1,4,-2,1,2,1),2,3)
C <- A %*% B            # Returns a multiplied matrix
```

### 5. Multiplication by a scalar
```py
c <- 3
c*A                     # Returns a matrix multiplied with a constant
```

### 6. Transpose of a Matrix 
```py
AT <- t(A)              # Returns a transosed matrix
```

### 7. Inverse of a Matrix 
```py
AI <- solve(A)          # Returns a inverse of a matrix
```

### 8. Determinant of a Matrix
```py
v <- det(A)             # Returns a determinant value of matrix
```

### 9. Dimension of a Matrix 
```py
dim(A)                  # Returns the dimension of matrix
```

### 10. Number of rows
```py
nrow(A)                 # Return number of rows of matrix 'A'
```

### 11. Number of columns
```py
ncol(A)                 # Returns number of columns of matrix 'A'
```

### 12. Horizontal concatnation
```py
A <- matrix(c(2,3,-2,1,2,2),3,2)
B <- matrix(c(1,3,2,1,4,2),3,2)
C <- cbind(A,B)        # Returns concatenated matrix
```

### 13. Vertical concatenation
```py
A <- matrix(c(2,3,-2,1,2,2),3,2)
B <- matrix(c(1,3,2,1,4,2),3,2)
C <- rbind(A,B)        # Returns concatenated matrix
```

## Apply functions

Apply functions are a family of functions in base R which allow you to repetitively perform an action on multiple chunks of data. 

### 1. apply function 
```py
apply(X, MARGIN, FUNCTION)
```
- **X** : Array of matrix
- **MARGIN** : Where to apply (row = 1, col = 2)
- **FUNCTION** : Function you want to use

### 2. lapply function 
```py
lapply(X, FUNCTION, …)
```
- **X** : Vector or a list
- **FUNCTION** : Function to use

### 3. sapply function 
```py
sapply(X, FUNCTION, …, simplify = TRUE, USE.NAMES = TRUE)
```
- **X** : Vector or a list
- **FUNCTION** : Function to use
- Extra arguments have default values

### 4. vapply function 
```py
vapply(X, FUNCTION, FUNCTION.VALUE, …, USE.NAMES = TRUE)
```
- **X** : Vector or a list
- **FUNCTION** : Function to use
- Extra arguments have default values
