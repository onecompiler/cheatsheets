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

---
![linux](https://user-images.githubusercontent.com/87390353/173860442-02a022af-fe38-4fea-8e07-a5e74ed30fd7.jpg)

---
![kernal](https://user-images.githubusercontent.com/87390353/173860860-6bbaedce-991c-4a2b-8db2-9f4ee1390b1b.jpg)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

![vg](https://user-images.githubusercontent.com/87390353/175115113-33e276c9-9d11-4b50-b6cb-8353f8ed3efe.jpg)

At first we are gonna make a txt file with `nano` editor to list all the basic commands.
```
1. Open Git bash
2. Type "nano [file_name]" eg.(nano anushka.txt)
3. Now I have created a list of basic commands.
```
![shell](https://user-images.githubusercontent.com/87390353/173865406-78b346c7-77b2-4b94-a4b7-aa0d6558daa4.jpg)

4. Now save the file with `[ctrl+x,y,enter]`.

---
- # Uses :

1. cd  (change the directory)
2. pwd (show the current directory)
3. ls  (list all files of the directory)



![command](https://user-images.githubusercontent.com/87390353/174104071-6d8d7ff5-2d31-4a84-840f-24905e63cd39.jpg)

---
4. ls -l (Long list format)
   - It shows more information of the files

    ![command2](https://user-images.githubusercontent.com/87390353/174108134-89c462e8-3dfa-44bc-80a4-641ec8f40bfc.jpg)

---
5. clear (to clear the console)
6. cp (copy a file)
    - To copy a file, write `cp [file_name] [destination path]`
    - Now if I use "ls" command then we can see if the file is copied or not.

![comm](https://user-images.githubusercontent.com/87390353/174112062-f04efa8e-83c1-4576-8950-b7332585820d.jpg)

---
7. mv (move a file)
    - To move a file, write `mv [file_name] [destination path]`
8. rm (remove a file)
    - Use `rm [file_name]` to remove a file.

![copy](https://user-images.githubusercontent.com/87390353/174138120-5fcaa0af-93ed-4ab4-9636-4b05f30a935b.jpg)

---
9. echo (print string)
10. cat (concatenate text file)
11. less (show the content of text file in a separate window)

![ss1](https://user-images.githubusercontent.com/87390353/174638478-82e965c3-d6ef-4a2d-98a3-c87ac21684b1.jpg)

![ss22](https://user-images.githubusercontent.com/87390353/174638507-7c64e8da-6655-4b68-9389-9533277721aa.jpg)

- Press 'q' to exit from the separate window.

---
12. grep (grab data from a certain file)
13. mkdir (make a directory)
14. touch (create files in the current directory)

![polo](https://user-images.githubusercontent.com/87390353/174640294-5ba973ea-f510-42a8-b606-51d85c63281f.jpg)

---
15. chmod (Change Mode)
     - chmod +r [file_name]
     - chmod +w [file_name]
     - chmod +x [file_name]
     
**Note:** Another form of writing **chmod** is 

   ![Screenshot (221)](https://user-images.githubusercontent.com/91726340/175812601-3ff7843f-7066-450e-83b8-0c3c39f816cd.png)
     
16. man+help (General Commands Manual)
      - Press 'h' to summary up commands.
      - Press 'q' when you want to exit.

---

![vg - Copy](https://user-images.githubusercontent.com/87390353/175115412-47b48657-5a6e-43a4-a34c-3e5d7f242bf3.jpg)

---

![cf](https://user-images.githubusercontent.com/87390353/175114664-e913df06-f5c0-4236-9bfa-a87f27a1f20c.jpg)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

![jii](https://user-images.githubusercontent.com/87390353/175563463-9f96ae09-675b-4acf-9fdf-cdcb4f595ed4.jpg)


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

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Example :

- At first we have opened two console side by side to see how it works more clearly.

### Input: 
![bash](https://user-images.githubusercontent.com/87390353/175571640-2d48644b-e2c9-4210-94b2-f00ba9d3b67d.jpg)

### Output:

![bash2](https://user-images.githubusercontent.com/87390353/175571647-d1faa127-e312-4d13-b0d2-93f2d60f1ae5.jpg)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

![kh](https://user-images.githubusercontent.com/87390353/175572512-74d1f6ce-8a9f-4559-a449-2a296fb3efb9.jpg)


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

![var1](https://user-images.githubusercontent.com/87390353/176923372-b988a8b5-34f8-4045-9de5-5e426d9a93d0.jpg)

- If we use readonly, it will show like this:

![var2](https://user-images.githubusercontent.com/87390353/176923398-76485f57-fa76-4539-a58e-4f4b05090407.jpg)

- If we use unset, it takes the value out of the list.

![var3](https://user-images.githubusercontent.com/87390353/176923437-690a1b2f-9108-406b-9d99-8b799b62bc0e.jpg)

---

- Special Variable:
   - #$0
   - $#
   - $*
   - $@
   - $?
   - $$

- Example:

![special](https://user-images.githubusercontent.com/87390353/176929660-44623106-6c48-41c4-9a40-a8ad98c176b2.jpg)

![sp](https://user-images.githubusercontent.com/87390353/176928438-84130218-b2f5-4207-a5aa-40d8c4f0e5a1.jpg)

- "$?" returns either 0 or 1. If your previous commands run succesfully then it will return 0, otherwise 1.

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

![basic](https://user-images.githubusercontent.com/87390353/176930799-7d3e24ac-f2e5-40aa-ad70-26a0c00fd4f5.jpg)

---
- Arithmetic Operators
- Relational Operators
- Boolean Operators
- String Operators
- File Test Operators

---
- # Arithmetic Operators:


![ap](https://user-images.githubusercontent.com/87390353/176931615-f467a82b-ab3f-495c-9928-be802d247392.jpg)

---
- # Relational Operators:

![re](https://user-images.githubusercontent.com/87390353/176931840-cf6c3777-80e1-4c5f-8d95-7c65369ebe29.jpg)

---
- # Boolean Operators:

![bo](https://user-images.githubusercontent.com/87390353/176932256-05a5e909-5e24-439c-8e73-ee8b593f8ad1.jpg)

---
- # String Operators:

![st](https://user-images.githubusercontent.com/87390353/176932522-4fe7b175-4486-443a-aef0-669d2c6ac3e6.jpg)

---
- # File Test Operators:

![f](https://user-images.githubusercontent.com/87390353/176933236-8e3ca807-b343-46aa-9189-a88a5a5255be.jpg)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

![loop](https://user-images.githubusercontent.com/87390353/180616832-6f14d5ee-5b4a-444b-9e24-d6d1e7f07d1d.jpg)

---

- While Loop
- For Loop
- Until Loop
- Nested Loop
- Loop Control

---

1. For loop example :

![for](https://user-images.githubusercontent.com/87390353/180636578-15091d3e-666e-436d-979a-ef6549f16b74.jpg)

---

2. While loop example :

![while](https://user-images.githubusercontent.com/87390353/180636875-9ab1f08d-f6d2-4f4a-8d5f-c4d74baa487e.jpg)

---

3. Until loop example :

![until](https://user-images.githubusercontent.com/87390353/180637336-c2ae8a39-275e-42bd-83c2-755c49357120.jpg)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="3000">

# Reference

This is a documentary repo on Shell Scripting by **Edureka**.
