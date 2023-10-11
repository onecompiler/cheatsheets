---
title: cd Linux Command
description: cd command is used to change the current working directory
created: 2019-08-21
updated: 2023-10-12
---

`cd` command is used to change the current working directory

## Changing to a directory with path 

```sh
cd /path/to/new/directory
```

## change directory to the root directory

```sh
 cd /
 ```
 
## Change to current logged in user's home directory

```sh
cd ~
```
```sh
cd
```

## Change to a directory whih is an immediatsub directy to you rcurrent directory

For example lets take following is your directory structure

```
├── images
├── movies
│   ├── action
│   └── comedy
└── music
```
and let's say you are in movies currently, so to go to action you can simply run the following command

```sh
cd action
```

```
├── images
├── 'My movies'
│   ├── action
│   └── comedy
└── music
```

```sh
cd My\ movies
```
## Going back to immediate parent directoty of current directoty 

```sh
cd ..
```
## change directory to the last working directory

```sh
 cd -
 ```