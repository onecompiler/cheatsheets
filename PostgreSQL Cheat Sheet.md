# PostgreSQL Cheat Sheet
PostgreSQL (psql) commands in one page for the SQL REPL from [postgresql.org](https://www.postgresql.org/docs/10/static/index.html).


## Basics
| Name | Description |
|------|-------------|
| `psql` | Connect to the database. |
| `psql -d <db> -U <user>` | Connect to localhost `db` as `user` name. |
| `psql create database <db>` | Create database with `db` name. |
| `create role <pg_user> with LOGIN ENCRYPTED PASSWORD <password>` | Create a user `pg_user` with `password`. |
| `create database <db> owner <user>;` | Create a database with name `db` which belongs to `user`.
| `create extension if not exists "uuid-ossp";` | Create useful extension with functions like `uuid_generate_v4`. [full doc](https://www.postgresql.org/docs/current/static/uuid-ossp.html)
| `create extension if not exists "hstore";` | Create useful extension [hstore](https://www.postgresql.org/docs/current/static/hstore.html).
| `revoke all on database <db> from public;` |
| `grant connect on database <db> to <user>;` |
| `grant all on database <db> to <user>;` |
| `alter role <user> set search_path = <schemaname>;` |


## General Purpose
| Name | Description |
|------|-------------|
| `\q` | Quit from psql. |
| `\?` | All commands of psql. |
| `\l+` | Lists all the databases with size. |
| `\c db_name` | Connect to database `db_name`. |
| `\dn` | List all schemas. |
| `\dt schema_name.*` | List all tables in `schema_name`. |
| `\d table_name` | List columns on table. |
| `\df` | List functions |
| `\dv` | List views. |
| `\x auto` | Super pretty query output for long rows. |
| `\t` | Turn off/on output header and row count. |
| `\h` | Help menu. |
| `\e` | Open an editor defined by your EDITOR environment variable, and put the most recent command entered in psql into the buffer. If it's vim editor use `shift + :` and tap `q` to quite or `wq` to resolve query. More vim [commands](https://vim.rtorr.com/). |
| `\ef [function]` | Open an editor, and put the function into the buffer. Without a function, it provides a convenient template for creating a new function. |
| `\s` | Print out your psql history to STDOUT. |
| `\timing` | Show timing for query execution. |


Hope you would be cool and efficient with this little cheat sheet.

Help me to fill out the rest of these useful commands if you think that might be helpful for you.

## Config

```
$ cat ~/.psqlrc
\set ECHO none
\set PROMPT1 '%n@%/%R%# %x '
\x auto
\set ON_ERROR_STOP on
\set ON_ERROR_ROLLBACK interactive

\pset null '¤'
\pset linestyle 'unicode'

\pset unicode_border_linestyle single
\pset unicode_column_linestyle single
\pset unicode_header_linestyle double

set intervalstyle to 'postgres_verbose';

\setenv LESS '-iMFXSx4R'
\set ECHO all
```

## Generating and inserting fake data

```psql
CREATE TABLE some_table (id bigserial PRIMARY KEY, a float);​
SELECT create_distributed_table('some_table', 'id');​​​

INSERT INTO some_table (a) SELECT random() * 100000 FROM generate_series(1, 1000000) i;    -- 2 secs  (40MB)​
INSERT INTO some_table (a) SELECT random() * 100000 FROM generate_series(1, 10000000) i;   -- 20 secs (400MB)​
INSERT INTO some_table (a) SELECT random() * 100000 FROM generate_series(1, 100000000) i;  -- 300 secs (4GB)​
INSERT INTO some_table (a) SELECT random() * 100000 FROM generate_series(1, 1000000000) i; -- 40 mins (40GB)​
```
