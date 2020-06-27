---
title: JShell 
description: JShell cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-04-26
updated: 2020-04-26
---
Jshell is Java’s first official REPL (READ-EVAL-PRINT-LOOP) tool which provides interactive use of Java Programming Language elements.

## Variables
When you evaluate any valid java expression, the result will be stored in the system defined variables.

### User-defined variables syntax:
```java
datatype variable name = value;
```
## Commands

* To launch Jshell tool
    ```sh
    jshell
    ```
* To exit Jshell
    ```sh
    exit
    ```
* To list all the declared variables.
    ```sh
    /vars
    /vars <variableName>
    /vars <variableSnippetId>
    /vars -start
    /vars -all
    ```
    ### Example:
    ```sh
    jshell> /vars
    |       String name = "OneCompiler"
    |       int id = 1
    ```

* To list all the declared Methods
    ```sh
    /methods
    /methods <methodName>
    /methods <methodSnippetId>
    /methods -start
    /methods -all
    ```

    ### Example:
    ```sh
    jshell> /methods
    |    double sum(int,int)
    ```

* To displays classes, interfaces, and enums 
    ```sh
    /types
    /types <typeName>
    /types <typeSnippetId>
    /types -start
    /types -all
    ```    
* To see a list all the snippets
    ```sh
    /list
    /list -all
    /list -start
    /list <snippetName>
    /list <snippetId>
    ```
* To save your snippets
    ```sh
    /save
    ```
* To personalize your startup entries
    ```sh
    /set start
    ```
* To get help about the list of the JShell commands.
    ```sh
    /help
    ```
* To edit code of a method
    ```sh
    /edit method-name
    ```
* To load Code from External Java File into REPL:
    ```sh
    /open filename.java
    ```
    You can also provide directory information along wwith filename.java if the file is present in different directory like `/open c:\\Documents\\filename.java`

* To Drop a Snippet
    ```sh
    /drop <snippetName>
    /drop <snippetId>
    ```