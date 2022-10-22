---
title: SQL Cheatsheet
description: Contains syntaxes & examples to help new comers get comfortable with using SQL.
created: 2022-10-01
updated: 2022-10-09
---

## Creation & Insertion

Creating a new table :

```SQL
CREATE TABLE <table name> (
		<column name> <data type>,
		<column name> <data type>,
		.
		.
		.
		<column name> <data type>
);
```

Inserting values into a table :

```SQL
INSERT INTO <table name> VALUES (<val1>,<val2>,....,<valn>);
```

Inserting values in some columns :

```SQL
INSERT INTO <table name>(<column name>,<column name>)
VALUES (<val1>,<val2>);
```

Data type is important i.e for strings use quotes (ex : ‘python’ instead of python)

Create table from existing table :

```SQL
CREATE TABLE <table name> AS(
	SELECT <column name>,<column name>
	FROM <table name>
);
```

## Visualization

To get description of a table :

```SQL
DESCRIBE <table name>
```

or (DESC command runs on only the software system// doesn’t run on editors)

```SQL
DESC <table name>
```

## Selection

To get all values :

```SQL
SELECT * FROM <table name> ;
```

To get specific columns :

```SQL
SELECT <column name>, <column name> FROM <table name> ;
```

This can also be achieved by :

```SQL
SELECT ALL <column name> FROM <table name>
```

To get used to specify the number of records in return:

```SQL
SELECT <column_name>
FROM <table name>
WHERE condition
LIMIT number;
```

To get all unique values from a column :

```SQL
SELECT DISTINCT <column name> FROM <table name> ;
```

## Where Conditionals

To select specific rows with a condition :

```SQL
SELECT <column name>
FROM <table name>
WHERE <condition>
```

Example :
Fetching rows with score greater than 85.

```SQL
SELECT marks
FROM student_marks
WHERE score > 85 ;
```

### Relational Operators

```SQL
=,>,<,>=,<=,<>
```

Example :
Fetching rows where city is not New York.

```SQL
SELECT * FROM citydata
WHERE city <> 'New York' ;
```

### Logical Operators

```SQL
||, &&, !
```

|| -> Or
&& -> And
! -> Not
The default order is → 1)NOT, 2)AND and 3)OR use parenthesis to override.

Example :

1. Fetch students who failed in math and english.

```SQL
SELECT studentname FROM studentdata
WHERE math = 'Fail' && english = 'Fail';
```

2. Fetch boys who failed in math and english.

```SQL
SELECT studentname FROM studentdata
WHERE (math = 'Fail' && english = 'Fail') && gender = 'Male';
```

### Iterating over a list

```SQL
SELECT <column name>
FROM <table name>
WHERE <column name> <condition> IN (<val1>,<val2>,...<val3>)
```

Example :
Fetch names from student in class 8,9 & 10.

```SQl
SELECT studentname
FROM studentdata
WHERE class IN (8,9,10);
```

### Pattern Matching

1. Starting with 'x' :

```SQL
SELECT <column name>
FROM <table name>
WHERE <column name> LIKE 'x%';
```

2. Ending with 'x' :

```SQL
SELECT <column name>
FROM <table name>
WHERE <column name> LIKE '%x';
```

Can also use NOT LIKE instead of LIKE.

Examples :

1. Fetch names of students starting with ‘A’.

```SQL
SELECT studentname
FROM studentdata
WHERE name LIKE "A%";
```

2. Fetch names which have 3 letters.

```SQL
SELECT studentname
FROM studentdata
WHERE name like "___";
```

-> 3 underscores.

## Manipulation

Delete all records :

```SQL
DELETE FROM <table name>
```

Delete with a condition :

```SQl
DELETE FROM <table name> WHERE <condition>
```

Example :

1. Delete ‘Yash’ student data.

```SQL
DELETE FROM studentdata WHERE studentname= "Yash";
```

Update values in a column :

```SQL
UPDATE <table name>
SET <column name> = <val1>, <column name> = <val2>
WHERE <condition>;
```

Example :

1. Update student grade if passed math (scored more than 80).

```SQL
UPDATE studentdata
SET maths = "Pass"
WHERE maths > 80;
```

Add a new column by using ALTER :

```SQl
ALTER TABLE <table name>
ADD <column name> <data type>;
```

Dropping a table :
Gets rid of the table.

```SQl
DROP TABLE <table name>;
```

Truncating a table :
Gets rid of the data inside the table, preserving its structure.

```SQl
TRUNCATE TABLE <table name>;
```

## Constraints

```SQL
UNIQUE, PRIMARY KEY, DEFAULT, CHECK, FOREIGN KEY, NOT NULL, CREATE INDEX
```

Unique → Repetition of values forbidden

Primary Key → same as unique, cannot take NULL value. Only 1 Primary key in a table

Default → sets a pre defined value if value not entered.

Check → Limits value.

Foreign Key → Is a unique/primary key in a different table, but referenced in another.

Not Null -> It ensures that a column does not have a null value.

Create Index → It is used to create and retrieve data from the database very quickly.

## Group By Clause

Used with different functions like COUNT, AVG, etc..

```SQL
SELECT <column name> FROM <table name>
WHERE <condition>
GROUP BY <column name>
```

Example :
Get count of all students in each stream

```SQL
SELECT COUNT(fname)
FROM studentdata
GROUP BY stream;
```

## Order By Clause

ASC → Ascending order (Default)

DESC → Descending order

```SQL
SELECT <column name>, <column name>
FROM <table name>
ORDER BY <column name>, <column name> ASC <|DESC>;
```

Example :
Fetch all students and arrange them according to their age, in a descending order.

```SQL
SELECT fname,lname
FROM studentdata
ORDER BY age DESC;
```

Can use both simultaneously like :

```SQL
SELECT fname,lname
FROM studentdata
ORDER BY marks ASC, age DESC;
```

Can also order categorical columns in an alphabetical order.

## Searching for NULL values

```SQL
SELECT <column name>, <column name>
FROM <table name>
WHERE <column name> IS NULL;
```

Example :
Getting the first & last names where the age is a NA value.

```SQL
SELECT fname, lname
FROM studentdata
WHERE age IS NULL;
```

Can also use the IS NOT NULL instead of IS NULL keyword, like this :

```SQL
SELECT <column name>, <column name>
FROM <table name>
WHERE <column name> IS NOT NULL;
```

## Joins in SQL

INNER JOIN

This query will return all of the records in the left table (table A) that have a matching record in the right table (table B)
Example :

```SQL
SELECT [select_list]
FROM Table_A A
INNER JOIN Table_B B
ON A.Key = B.Key

-- shortcut for inner join using , operator
SELECT [select_list]
FROM Table_A A,Table_B B
ON A.Key = B.Key
-- , basically means cross product and if condition given as per condition
```

LEFT JOIN
This query will return all of the records in the left table (table A) regardless if any of those records have a match in the right table (table B). It will also return any matching records from the right table.

Example:

```SQL
SELECT [select_list]
FROM Table_A A
LEFT JOIN Table_B B
ON A.Key = B.Key
```

RIGHT JOIN
This query will return all of the records in the right table (table B) regardless if any of those records have a match in the left table (table A). It will also return any matching records from the left table

Example

```SQL
SELECT [select_list]
FROM Table_A A
RIGHT JOIN Table_B B
ON A.Key = B.Key
```

OUTER JOIN
This Join can also be referred to as a FULL OUTER JOIN or a FULL JOIN. This query will return all of the records from both tables, joining records from the left table (table A) that match records from the right table (table B)
Example:

```SQL
SELECT [select_list]
FROM Table_A A
FULL OUTER JOIN Table_B B
ON A.Key = B.Key
```

LEFT OUTER JOIN
This query will return all of the records in the left table (table A) that do not match any records in the right table (table B).
Example:

```SQL
SELECT [select_list]
FROM Table_A A
LEFT JOIN Table_B B
ON A.Key = B.Key
WHERE B.Key IS NULL
```

RIGHT OUTER JOIN
This query will return all of the records in the right table (table B) that do not match any records in the left table (table A).
Example:

```SQL
SELECT [select_list]
FROM Table_A A
RIGHT JOIN Table_B B
ON A.Key = B.Key
WHERE A.Key IS NULL
```

## Sql Data Control Language

DCL Commands are used to control access to the database and the data associated to it. And it is highly used inforcing Data Security.

We have commands for managing user like :

- Create User

```SQL
CREATE USER <Username> IDENTIFIED BY <password>
```

- Delete User

```SQL
 DROP USER <Username>
```

- GRANT

```SQL
GRANT SELECT / INSERT / DELETE / UPDATE / All privileges on <Table_Name> FROM <Username>/Public;
```

- REVOKE

```SQL
REVOKE SELECT / INSERT / DELETE / UPDATE / All privileges on <Table_Name> FROM <Username>/Public;
```
