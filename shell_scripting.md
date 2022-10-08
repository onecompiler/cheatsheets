---
title: Shell Scripting
description: A shell script is a list of commands in a computer program that is run by the Unix shell which is a command line interpreter.
created: 2022-10-06
updated: 2022-10-06
---
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

# Agenda
- Getting Started with linux
- Command line essentials
- Shell script basics
- using variables
- Basic operators
- Shell loops

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

# Getting Started with Linux

## Why linux?
- Open source OS
- Access to source code
- Highly secure
- Runs Faster

## What is LINUX?

Linux is a Unix-like, open source amd community-developed operating system for which is capable of handling activiies from multiple users at the same time.

### Applications⬇️

#### Kernel
- CPU

- MEMORY

- Devices

## What is a Kernel?

The computer programs that allocate the system resources and coordinate all the details of the computer's internals is called the Operating System or the Kernel.Users communicate with the OS through a program called the Shell.


<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

# COMMAND LINE ESSENTIALS

At first we are gonna make a txt file with `nano` editor to list all the basic commands.
```
1. Open Git bash
2. Type "nano [file_name]" eg.(nano anushka.txt)
3. Now I have created a list of basic commands.
``` 

- cd
- pwd
- ls
- cp
- mv
- rm 
- echo
- cat
- less
- grep
- mkdir
- touch
- chmod
- man + help


4. Now save the file with `[ctrl+x,y,enter]`.

---
- # Uses :

1. cd  (change the directory)
2. pwd (show the current directory)
3. ls  (list all files of the directory)

4. ls -l (Long list format)
   - It shows more information of the files

5. clear (to clear the console)
6. cp (copy a file)
    - To copy a file, write `cp [file_name] [destination path]`
    - Now if I use "ls" command then we can see if the file is copied or not.

7. mv (move a file)
    - To move a file, write `mv [file_name] [destination path]`
8. rm (remove a file)
    - Use `rm [file_name]` to remove a file.
    
9. echo (print string)
10. cat (concatenate text file)
11. less (show the content of text file in a separate window)

- Press 'q' to exit from the separate window.

12. grep (grab data from a certain file)
13. mkdir (make a directory)
14. touch (create files in the current directory)

15. chmod (Change Mode)
     - chmod +r [file_name]
     - chmod +w [file_name]
     - chmod +x [file_name]
     
**Note:** Another form of writing **chmod** is 

## chmod ugo filename

- 0 = 0 = nothing
- 1 = 1 = execute
- 2 = 2 = write
- 3 = 2+1 = w+x
- 4 = 4 = read
- 5 = 4+1 = r+x
- 6 = 4+2 = r+w
- 7 = 4+2+1 = r+w+x

16. man+help (General Commands Manual)
      - Press 'h' to summary up commands.
      - Press 'q' when you want to exit.

---

| **Command Line Interface** | **Graphical User Interface** | 
| :------------------------- | :--------------------------- |
| 1) Console Representation  | 1) Graphical Representation  |
| 2) Difficult for Begineers | 2) Ease of Use |
| 3) Faster OS | 3) OS is slower | 
| 4) Granular Control | 4) Lesser Control |

## What is CLI?

Command Line Interface is a text-based interface used to interact with software and operating system by typing commands into the interface and receive a response in the same way.


<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

# SHELL SCRIPT BASICS
---

# What is Shell?
- The Shell is a Command Line Interpreter. It translate commands enter by the user and converts them into a language that is understood by kernel.

# What is Shell Script?
- The basic concept of shell script is a list of commands which are listed in the order of execution. A good shell script will hav comments precided by # sign.

![icons8-typing-64](https://user-images.githubusercontent.com/87390353/175568033-ff8c8645-b420-4277-bd12-db04f0098457.png)     ![icons8-translation-64](https://user-images.githubusercontent.com/87390353/175568043-d0f4a888-8529-4dee-a35a-53766e355251.png)   ![icons8-document-61](https://user-images.githubusercontent.com/87390353/175568080-a8d11b3c-f78d-4434-a152-420175f471ba.png)

---

| Bourne Shell Types | C Shell Types |
|--------------------|---------------|
|1. Bourne Shell      | C Shell |
|2. Korn Shell | TENEX/TOPS C Shell |
|3. Bourne-Again Shell | Z Shell |
|4. POSIX Shell | |


<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

# USING VARIABLES 

---
# What is Variable?
- A variable is a character string to which we assign a value. The value assigned could be a number, text, file name, device, or any other type of data. 

### Types:
- Local Variable:
    - A local variable is a variable that is present within the current instance of the shell. They are set at the command prompt.
- Environmental Variable:
    - An environmental variable is available to any child process of the shell. Some programs need environment variables in order to function correctly.
- Shell Variable:
    - A shell variable is a special variable that is set by the shell and is required by the shell in order to function corrently. Some of these variables are environment variables whereas others are local variables.


## Defining Variable:
--- 
- Scalar Variable:
   - It means you can take only single value in the variable.

- If we use readonly, it will show like this:

- If we use unset, it takes the value out of the list.

- Special Variable:
   - #$0
   - $#
   - $*
   - $@
   - $?
   - $$

- "$?" returns either 0 or 1. If your previous commands run succesfully then it will return 0, otherwise 1.

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

# BASIC OPERATORS 
---

- Arithmetic Operators
- Relational Operators
- Boolean Operators
- String Operators
- File Test Operators

---
- # Arithmetic Operators:

The following arithmetic operators are supported by Bourne Shell.

Assume variable a holds 10 and variable b holds 20 then-


| **Operator** | **Description** | **Example** |
| :----------- | :-------------- | :---------- |
| + (Addition) | Adds values on either side of the operator | `expr $a + $b` will give 30 |
| - (Subtraction) | Subtracts right hand operand from left hand operand | `expr $a - $b` will give -10 |
| * (Multiplication) | Multiplies values on either side of the operator | `expr $a \* $b` will give 200 |
| / (Division) | Divides left hand operand by right hand operand | `expr $b / $a` will give 2 |
| % (Modulus) | Divides left hand operand by right hand operand and returns remainder | `expr $b % $a` will give 0 |
| = (Assignment)	| Assigns right operand in left operand | a = $b would assign value of b into a |
| == (Equality) | Compares two numbers, if both are same then returns true. | [ $a == $b ] would return false. |
| != (Not Equality) | Compares two numbers, if both are different then returns true. | [ $a != $b ] would return true. |

---
- # Relational Operators:

Bourne Shell supports the following relational operators that are specific to numeric values. These operators do not work for string values unless their value is numeric.

For example, following operators will work to check a relation between 10 and 20 as well as in between "10" and "20" but not in between "ten" and "twenty".

Assume variable a holds 10 and variable b holds 20 then 

| **Operator** | **Description** | **Example** |
| :----------- | :-------------- | :---------- |
| -eq | Checks if the value of two operands are equal or not; if yes, then the condition becomes true. | [ $a -eq $b ] is not true. |
| -ne | Checks if the value of two operands are equal or not; if values are not equal, then the condition becomes true | [ $a -ne $b ] is true. |
| -gt | Checks if the value of left operand is greater than the value of right operand; if yes, then the condition becomes true. | [ $a -gt $b ] is not true. |
| -lt	| Checks if the value of left operand is less than the value of right operand; if yes, then the condition becomes true.	| [ $a -lt $b ] is true. |
| -ge | Checks if the value of left operand is greater than or equal to the value of right operand; if yes, then the condition becomes true. | [ $a -ge $b ] is not true. |
| -le	| Checks if the value of left operand is less than or equal to the value of right operand; if yes, then the condition becomes true. | [ $a -le $b ] is true. |

---
- # Boolean Operators:

The following Boolean operators are supported by the Bourne Shell.

Assume variable a holds 10 and variable b holds 20 then 

| **Operator** | **Description** | **Example** |
| :----------- | :-------------- | :---------- |
| !  | This is logical negation. This inverts a true condition into false and vice versa.	 | [ ! false ] is true. | 
| -o | This is logical OR. If one of the operands is true, then the condition becomes true. | [ $a -lt 20 -o $b -gt 100 ] is true. |
| -a |	 This is logical AND. If both the operands are true, then the condition becomes true otherwise false.	 | [ $a -lt 20 -a $b -gt 100 ] is false. |

---
- # String Operators:

The following string operators are supported by Bourne Shell.

Assume variable a holds "abc" and variable b holds "efg" then −

| **Operator** | **Description** | **Example** |
| :----------- | :-------------- | :---------- |
| =  |	Checks if the value of two operands are equal or not; if yes, then the condition becomes true. | [ $a = $b ] is not true.  |
| != | Checks if the value of two operands are equal or not; if values are not equal then the condition becomes true. | [ $a != $b ] is true.  |
| -z | Checks if the given string operand size is zero; if it is zero length, then it returns true. | [ -z $a ] is not true.  |
| -n |	Checks if the given string operand size is non-zero; if it is nonzero length, then it returns true.  | [ -n $a ] is not false.  |
| str | Checks if str is not the empty string; if it is empty, then it returns false. | [ $a ] is not false.  |

---
- # File Test Operators:

We have a few operators that can be used to test various properties associated with a Unix file.

Assume a variable file holds an existing file name "test" the size of which is 100 bytes and has read, write and execute permission on −

| **Operator** | **Description** | **Example** |
| :----------- | :-------------- | :---------- |
| -b file |	Checks if file is a block special file; if yes, then the condition becomes true.	| [ -b $file ] is false.  |
| -c file |	Checks if file is a character special file; if yes, then the condition becomes true.  |	[ -c $file ] is false.  |
| -d file |	Checks if file is a directory; if yes, then the condition becomes true.	| [ -d $file ] is not true.  |
| -f file |	Checks if file is an ordinary file as opposed to a directory or special file; if yes, then the condition becomes true. | [ -f $file ] is true.  |
| -g file |	Checks if file has its set group ID (SGID) bit set; if yes, then the condition becomes true.  |	[ -g $file ] is false.  |
| -k file |	Checks if file has its sticky bit set; if yes, then the condition becomes true.  |	[ -k $file ] is false.  |
| -p file |	Checks if file is a named pipe; if yes, then the condition becomes true. |	[ -p $file ] is false. |
| -t file |	Checks if file descriptor is open and associated with a terminal; if yes, then the condition becomes true.  | [ -t $file ] is false.  |
| -u file |	Checks if file has its Set User ID (SUID) bit set; if yes, then the condition becomes true. | [ -u $file ] is false. |
| -r file |	Checks if file is readable; if yes, then the condition becomes true.	 | [ -r $file ] is true. |
| -w file |	Checks if file is writable; if yes, then the condition becomes true. | [ -w $file ] is true. |
| -x file |	Checks if file is executable; if yes, then the condition becomes true. | [ -x $file ] is true. |
| -s file |	Checks if file has size greater than 0; if yes, then condition becomes true. | [ -s $file ] is true.  | 
| -e file |	Checks if file exists; is true even if file is a directory but exists.  |  [ -e $file ] is true.  |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

# SHELL LOOPS

---

- While Loop
- For Loop
- Until Loop
- Nested Loop
- Loop Control

You will use different loops based on the situation. For example, the while loop executes the given commands until the given condition remains true; the until loop executes until a given condition becomes true.

---

# Reference

This is a documentary repo on Shell Scripting by **Edureka**.
