---
title: My SQL 
description: MySQL cheatsheet contains most commonly used commands which are helpful while working with MySQL.
created: 2020-05-28
updated: 2020-05-28
---

## Connecting to Database using command-line client

```sql
mysql -u [username] -p [database];
```

* To exit from mysql command-line client
    ```sql
    exit;
    ```
## To creen console window on Linux

```sql
system clear;
```
## Database Commands

### Creating a database

```sql
CREATE DATABASE [IF NOT EXISTS] db_name;
```
### Use a database

```sql
USE db_name;
```
### Drop a database

```sql
DROP DATABASE [IF EXISTS] db_name;
```
### Show available databases in the working database server

```sql
SHOW DATABASE;
```
### Display all the tables present in the database

```sql
SHOW TABLES;
```
##  DDL Commands

### 1. CREATE 
* To Create a new Table in database

```sql
CREATE TABLE table_name (
                column1 datatype,
                column2 datatype,
                ....);
``` 
### 2. ALTER
* ALTER is used to add, delete, or modify columns in an existing table.
```sql 
ALTER TABLE Table_name ADD column_name datatype;
```
### 3. TRUNCATE
* TRUNCATE removes all rows from a table
```sql
TRUNCATE table table_name;
```
### 4. DROP
* DROP statement destroys the objects like an existing database, table, index, or view.

```sql 
DROP TABLE table_name;
```
### 5. RENAME 
```sql
RENAME TABLE table_name1 to new_table_name1; 
```
### 6. COMMENT

###  Single-Line Comments: 
 ```sql
  --Line1;
  ```
###   Multi-Line comments: 
 ```sql
    /* Line1,
    Line2 */
```

## DML Commands

### 1. INSERT  
```sql
INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
```
Note: Column names are optional.

### 2. SELECT 

```sql
SELECT column1, column2, ...
FROM table_name
[where condition]; 
```
### 3. UPDATE 

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition; 
```
### 4. DELETE 

```sql 
DELETE FROM table_name where condition;
```

## DCL Commands

### 1. GRANT
* It is used to give access to users to the database
```sql
GRANT privileges ON object TO user;
```
### 2. REVOKE
* It is used to remove the granted permissions
```sql
REVOKE privileges ON object FROM user;
```
## TCL commands

### 1. COMMIT
* It is used for storing the changes made by the user. 
```sql
COMMIT;
```
### 2. ROLLBACK  
* Used for reverting changes of the transaction
```sql
ROLLBACK;
```
## 3. SAVEPOINT
* Marking a point of transaction to which easy rollback is possible. 
```sql
SAVEPOINT savepoint_name;
ROLLBACK TO savepoint_name; 
```
How to delete a savepoint:
```sql
RELEASE SAVEPOINT savepoint_name;
```

## Indexes

### 1. CREATE INDEX

```sql
  CREATE INDEX index_name on table_name(column_name);
```
* To Create Unique index:

```sql
  CREATE UNIQUE INDEX index_name on table_name(column_name);
```
### 2. DROP INDEX

```sql
DROP INDEX index_name ON table_name;
```
## Views

### 1. Create a View
```sql
Creating a View:
CREATE VIEW View_name AS 
Query;
```

### 2. How to call view
```sql
SELECT * FROM View_name;
```
### 3. Altering a View
```sql
ALTER View View_name AS 
Query;
```
### 4. Deleting a View
```sql
DROP VIEW View_name;
```

## Triggers

### 1. Create a Trigger

```sql
CREATE TRIGGER trigger_name trigger_time trigger_event
    ON tbl_name FOR EACH ROW [trigger_order] trigger_body
/* where
trigger_time: { BEFORE | AFTER }
trigger_event: { INSERT | UPDATE | DELETE }
trigger_order: { FOLLOWS | PRECEDES } */
```

### 2. Drop a Trigger

```sql
DROP TRIGGER [IF EXISTS] trigger_name;
```

### 3. Show a Trigger 

```sql
SHOW TRIGGERS;
```

### 4. Show a Trigger using Pattern Matching

```sql
SHOW TRIGGERS LIKE pattern;
```

## Stored Procedures

### 1. Create a Stored Procedure

```sql
CREATE PROCEDURE sp_name(p1 datatype)
BEGIN
/*Stored procedure code*/
END;
```
### 2. How to call Stored procedure

```sql
CALL sp_name;
```
### 3. How to delete stored procedure
```sql
DROP PROCEDURE sp_name;
```

## Joins

### 1. INNER JOIN
```sql
SELECT * FROM TABLE1 INNER JOIN TABLE2 where condition;
```
### 2. LEFT JOIN
```sql
SELECT * FROM TABLE1 LEFT JOIN TABLE2 ON condition;
```
### 3. RIGHT JOIN

```sql
SELECT * FROM TABLE1 RIGHT JOIN TABLE2 ON condition;
```
### 4. CROSS JOIN

```sql
SELECT select_list from TABLE1 CROSS JOIN TABLE2;
```


## Cursors

When an MYSQL statement is processed, a memory area is created known as context area. A cursor is a pointer to this context area.

### There are two types of cursor 
#### 1. Implict cursor 
#### 2. Explict cursor


### Explict Cursor 
Explict cursors are used when you are exceuting a SELECT statement query that will return more than one row.

### The cursor works in four stages

### 1. Declaration of cursor:-
```sql
DECLARE cursor_name CURSOR FOR SELECT_statement;
```
### 2. Open Cusor
```sql
OPEN cursor_name;
```
### 3. Fetch the cursor
```sql
FETCH cursor_name INTO variables list;
```
### 4. Close the cursor
```sql
CLOSE cursor_name;
```
