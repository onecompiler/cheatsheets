---
title: chmod Linux Command
description: chmod stands for "change mode". It is used to change the permissions to files/ directories
created: 2019-08-24
updated: 2019-08-24
---

chmod stands for "change mode". It is used to change the permissions to files/ directories

# Syntax
```sh
chmod [options] <permissions> <file_name> 
```

### Example 
```sh
chmod 777 foo.txt
```

# Permissions 
Following are the four possible digits and their respective permissions

|Digit| Permission|
|---|---|
|4|read|
|2|write|
|1|execute|
|0|no permission|

Users can also sumup these digits and can use like following 

|Derived Digits| Permission|
|---|---|
|7| 4+2+1 = read + write + execute|
|6| 4+2 = read + write|
|5| 4+1 = read + execute|
|3| 2+1 = write + execute|

# Permissions for user, group, others
Owner of the file can set different permissions for user, group & others 

### Example
```sh
chmod u=rwx,g=rx,o=r foo.sh # this is same as chmod 754 foo.sh
```

```
u = user
g = group
o = others

r = read
w = write
x = execute
```
