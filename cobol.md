---
title:COBOL
description:COBOL is used for writing application programs and we cannot use it to write system software. The applications like those in defense domain, insurance domain, etc. which require huge data processing make extensive use of COBOL.
created: 1959-04-25
updated: 2014-09-30
---

### Installation
> For Windows and Linux Users
|Link|Description|
|---|---|
|`http://downloads.hercules-390.eu/hercules-3.13.zip`|For Windows Users,This is a Mainframe Emulator for writing programs in COBOL|
|`http://downloads.hercules-390.eu/hercules-3.13.tar.gz`|For Linux Users,This is a Mainframe Emulator for writing programs in COBOL|

### Examples

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. hello 10 times.
PROCEDURE DIVISION.
PERFORM 10 TIMES
   DISPLAY "Hello"
END-PERFORM
STOP RUN
```
## Data types

|Value Type| Description|
|-----|-----|
|Data Name| refer to the storage space in the memory where the actual value is stored |
|Level Number| The level number specifies the hierarchy or levels of data entries/items.It is a a one-digit or two-digit integer between 01 and 49, or one of three special level-numbers: 66, 77, or 88|
|Picture Clause|It is used to specify the type and size of an elementary data item.The Picture character-string may contain a maximum of 90 characters. It consists of certain COBOL characters used as symbols|
|Value Clause|Value clause is an optional clause which is used to initialize the data items. The values can be numeric literal, alphanumeric literal, or figurative constant. It can be used with both group and elementary items.|


##Basic Verbs

###1.Accept Verb

*Accept verb is used to get data such as date, time, and day from the operating system or directly from the user.

```cobol
ACCEPT WS-STUDENT-NAME.
ACCEPT WS-DATE FROM SYSTEM-DATE.
```

###2.Display Verb                                            

*Display verb is used to display the output of a COBOL program.

```cobol
DISPLAY WS-STUDENT-NAME.
DISPLAY "System date is : " WS-DATE.
```
###3.Initialize Verb                                            

*Initialize verb is used to initialize a group item or an elementary item. Data names with RENAME clause cannot be initialized.                                                

```cobol                        
DISPLAY WS-STUDENT-NAME.
DISPLAY "System date is : " WS-DATE.
```

###4.Divide Verb                                           

*Divide verb is used for division operations.                                                

```cobol
DIVIDE A INTO B

DIVIDE A BY B GIVING C REMAINDER R
```


###5.Multiply Verb                                                 

*Multiply verb is used for multiplication operations.                                                                                                                                  

```cobol
MULTIPLY A BY B C

MULTIPLY A BY B GIVING E
```

###6.Add Verb                                           

*Add verb is used to add two or more numbers and store the result in the destination operand.

```cobol
ADD A B TO C D

ADD A B C TO D GIVING E

ADD CORR WS-GROUP1 TO WS-GROUP2
```

###7.Subtract Verb

*Subtract verb is used for subtraction operations.

```cobol
SUBTRACT A B FROM C D

SUBTRACT A B C FROM D GIVING E

SUBTRACT CORR WS-GROUP1 TO WS-GROUP2
```

##Conditional statements

###1.IF Condition Statement

*Syntax:Following is the syntax of IF condition statements −

```cobol
IF [condition] THEN
   [COBOL statements]
ELSE
   [COBOL statements]
END-IF.
```

###2.Relation Condition

*Relation condition compares two operands, either of which can be an identifier, literal, or arithmetic expression. Algebraic comparison of numeric fields is done regardless of size and usage clause.

```cobol
Syntax
Given below is the syntax of Relation condition statements −

[Data Name/Arithmetic Operation]

   [IS] [NOT] 

[Equal to (=),Greater than (>), Less than (<), 
Greater than or Equal (>=), Less than or equal (<=) ]

[Data Name/Arithmetic Operation]
```
###3.Sign Condition

*Sign condition is used to check the sign of a numeric operand. It determines whether a given numeric value is greater than, less than, or equal to ZERO.

```cobol
[Data Name/Arithmetic Operation] 

   [IS] [NOT] 

[Positive, Negative or Zero]

[Data Name/Arithmetic Operation]
```

###4.Class Condition

*Class condition is used to check if an operand contains only alphabets or numeric data. Spaces are considered in ALPHABETIC, ALPHABETIC-LOWER, and ALPHABETIC-UPPER.

```cobol
[Data Name/Arithmetic Operation>]

   [IS] [NOT] 

[NUMERIC, ALPHABETIC, ALPHABETIC-LOWER, ALPHABETIC-UPPER]

[Data Name/Arithmetic Operation]
```

###5.Condition-name Condition

*A condition-name is a user-defined name. It contains a set of values specified by the user. It behaves like Boolean variables. They are defined with level number 88. It will not have a PIC clause.

```cobol
88 [Condition-Name] VALUE [IS, ARE] [LITERAL] [THRU LITERAL].
```

###6.Negated Condition

*Negated condition is given by using the NOT keyword. If a condition is true and we have given NOT in front of it, then its final value will be false.

```cobol
IF NOT [CONDITION] 
   COBOL Statements
END-IF.
```

###7.Combined Condition

*A combined condition contains two or more conditions connected using logical operators AND or OR.

```cobol
IF [CONDITION] AND [CONDITION]
   COBOL Statements
END-IF.
````

##Loop Statements

###1.Perform Thru

*Perform Thru is used to execute a series of paragraph by giving the first and last paragraph names in the sequence. After executing the last paragraph, the control is returned back.

```cobol
PERFORM 
   DISPLAY 'HELLO WORLD'
END-PERFORM.
```

###2.Perform Until

*In ‘perform until’, a paragraph is executed until the given condition becomes true. ‘With test before’ is the default condition and it indicates that the condition is checked before the execution of statements in a paragraph.

```cobol
PERFORM A-PARA UNTIL COUNT=5

PERFORM A-PARA WITH TEST BEFORE UNTIL COUNT=5

PERFORM A-PARA WITH TEST AFTER UNTIL COUNT=5
```

###3.Perform Times

*In ‘perform times’, a paragraph will be executed the number of times specified.

```cobol
PERFORM A-PARA 5 TIMES.
```

###4.Perform Varying

*In perform varying, a paragraph will be executed till the condition in Until phrase becomes true.

```cobol
PERFORM A-PARA VARYING A FROM 1 BY 1 UNTIL A = 5.
```
