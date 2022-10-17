

# Kotlin Basic CheatSheet 1
*Kotlin is a statically typed programming language for modern multiplatform applications.*



# Table of contents
1. [Introduction To Kotlin](#kt0)
2. [Basic Syntax](#kt1)
3. [Kotlin Comments](#ktcmt)
4. [Datatypes in Kotlin](#kt1.0)
5. [Mutability in Kotlin](#kt2)
6. [Variables in Kotlin](#kt3)
 


<div id='kt0'>

## Introduction to Kotlin
Kotlin is a modern, trending programming language that was released in 2016 by JetBrains.

It has become very popular since it is compatible with Java (one of the most popular programming languages out there), which means that Java code (and libraries) can be used in Kotlin programs.

Kotlin is used for:

* Mobile applications (specially Android apps)

* Web development

* Server side applications

* Data science

* And much, much more!


<div id='kt1'>

## Basic Syntax
 
  Create a Kotlin file called Main.kt  
     Use the following code to print "Hello World" to the screen:

      fun main(){
       println("Hello World")
       }

<div id='ktcmt'>  

## Kotlin Comments
Comments can be used to explain Kotlin code, and to make it more readable. 

It can also be used to prevent execution when testing alternative code.

* Single-line Comments

Single-line comments starts with two forward slashes (//).

Any text between // and the end of the line is ignored by Kotlin (will not be executed).

This example uses a single-line comment before a line of code:

// This is a comment
println("Hello World") 

**Output**

Hello World


* Multi-line Comments

Multi-line comments start with /* and ends with */.

Any text between /* and */ will be ignored by Kotlin.

This example uses a multi-line comment (a comment block) to explain the code:

/* The code below will print the words Hello World
to the screen, and it is amazing */
println("Hello World")

**Output**

Hello World



<div id='kt1.0'> 

## Datatypes in Kotlin 

In Kotlin, the type of a variable is decided by its value:

**Code Example**

`val myNum = 5             // Int`

`val myDoubleNum = 5.99    // Double`

`val myLetter = 'D'        // Char`

`val myBoolean = true      // Boolean`

`val myText = "Hello"      // String`

<div id='kt2'>
 
## Mutability in Kotlin 
Mutable – The contents of the list can be freely changed. 

Read-Only – The contents of the collection are not meant to be changed. However, the underlying data can be changed.

 Immutable – Nothing can change the contents of the collection.

`var mutableString: String = "Adam"`

`val immutableString: String = "Adam"`

`val inferredString = "Adam"`

<div id='kt3'>

## Variables in Kotlin 

Variables are containers for storing data values.

To create a variable, use var or val, and assign a value to it with the equal sign (=):

**Syntax**

`var variableName = value`

`val variableName = value`

**Example**

`var name = "John"`

`val birthyear = 1975`

`println(name)          // Print the value of name`

`println(birthyear)     // Print the value of birthyear`

**Output**

John 

1975