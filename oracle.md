Basic queries:-
1.) CREATE TABLE - The create table statement is used to create a new table in the database.

Syntax:- CREATE TABLE table_name(col1_name data_type,col2_name data_type,..,colN_name data_type);

2.) SELECT - The select statement is used to fetch records from database.

Syntax:- SELECT * FROM table_name;


3.) INSERT - The insert statement is used to insert records into table.

Syntax:- INSERT into table_name values(value1, value2,.., valuen);

4.) UPDATE - The update statement is used to update records of a table.

Syntax:- UPDATE table_name set col1_name="exp1", col2_name="exp2" WHERE [condition]

5.)WHERE - The where statement is used to filter the records of a table.

Syntax:-SELECT * FROM table_name where col_name=value;

6.)DELETE - The delete statement is used to delete the records of a table from database.

Syntax:-DELETE FROM table_name WHERE col_name=value;

7.)TRUNCATE - The truncate statement is used to remove records of a table.

Syntax:-TRUNCATE table table_name;

8.)DROP - The truncate statement is used to drop a table.

Syntax:-DROP table table_name;

9.)DISTINCT - The Distinct clause is used to remove the duplicate records from the result set.

Syntax:-SELECT DISTINCT expression FROM table_name WHERE [condition];

10.)GROUP BY - The Group By clause is used with SELECT statement to collect data from multiple records and group the results by one or more columns.

Syntax:-SELECT col_name FROM table_name WHERE condition GROUP BY col_name(s);

11.)ORDER BY - The Order By clause is used to sort the records in result set

Syntax:-SELECT * FROM table_name WHERE condition ORDER BY expression [ASC|DESC];

12.)VIEW - It is basically a virtual table which is stored in Oracle data dictionary.

Syntax:-CREATE VIEW view_name AS SELECT col_1,col_2...col_n FROM table_name WHERE [condition];

13.)UNION - The UNION operator is used to combine the result sets of two or more Oracle SELECT statements.

Syntax:-SELECT exp_1,..exp_n FROM table_1 WHERE condition UNION SELECT exp_1,..exp_n FROM table_2 WHERE condition;

Note:-Each SELECT statement within the UNION operator must have the same number of fields in the result sets with similar data types

14.)INTERSECT - The INTERSECT operator is used to pick the common records from compound SELECT queries.

Syntax:-SELECT exp_1,..exp_n FROM table_1 WHERE condition INTERSECT SELECT exp_1,..exp_n FROM table_2 WHERE condition;

Oracle Joins:-
Join statement is used to combine data or rows from two or more tables based on a common field between them.Different types of Joins are:

1.)INNER JOIN - The INNER JOIN returns all rows from multiple tables where the join condition is met.
innerjoin.png
Syntax:-SELECT col_1,..col_n from table_1 INNER JOIN ON table_1.col = table2.col

2.)LEFT OUTER JOIN - The LEFT OUTER JOIN returns all the rows of the table on the left side of the join and matching rows for the table on the right side of join.
leftjoin.png
Syntax:-SELECT table1.col1, table1.col2, table2.col1,… FROM table1 LEFT JOIN table2 ON condition;

3.)RIGHT OUTER JOIN - The RIGHT OUTER JOIN returns all the rows of the table on the right side of the join and matching rows for the table on the left side of join.
right-outer.png
Syntax:-SELECT table1.col1, table1.col2, table2.col1,… FROM table1 RIGHT JOIN table2 ON condition;

4.)*FULL OUTER JOIN - The FULL OUTER JOIN returns all rows from the left-hand table and right-hand table. *
fulljoin.png
Syntax:-SELECT table1.col1, table1.col2, table2.col1,… FROM table1 FULL JOIN table2 ON condition;

5.)SEMI JOINS - A semi-join between two tables returns one copy of each row in first table where one or more matches are found in the second table.
Syntax:-SELECT col1, col2 FROM table1 WHERE id IN (SELECT table1_id FROM table2 WHERE condition)

SQL KEYS:-
KEYS in the database helps you to identify a tuple(row) in a relation(table).
It allows you to establish a relationship between tables and also identify the relationships between tables. There are no. of keys in database like **super key, primary key, foreign key, composite key, unique key, alternate key, etc.

1.)PRIMARY KEY - A column of a table is said to be a primary key if it uniquely identifies each row in that table.

Syntax:-CREATE TABLE table_name(column1 datatype CONSTRAINT constraint_name PRIMARY KEY, column2 datatype [ NULL | NOT NULL ],...);

Note:- None of the fields that are part of the primary key can contain a NULL value.

2.)*FOREIGN KEY - A foreign key is a column that is used to link two tables together.
*

Syntax:-CREATE TABLE table_name(col1 datatype null/not null,col2 datatype null/not null,... CONSTRAINT fkey_column FOREIGN KEY (col1, col2, ...col_n)
REFERENCES parent_table (col1, col2, ... col_n)
);

3.)COMPOSITE KEY - It is the combination of two or more columns in a table that can be used to uniquely identify each row in the table.

Syntax:-CREATE TABLE table_name(col_1 datatype_1, col datatype_2,...
PRIMARY KEY (col_1, col_2, ...));

4.)UNIQUE KEY -It is a set of one or more than one column of a table that uniquely identifies a record in a database table.

Syntax:-CREATE TABLE table_name(col_1 datatype_1 NOT NULL UNIQUE, col_2 datatype_2,...col_n datatype_n);







