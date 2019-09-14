---
title: ls Linux Command
description: ls command used to list files and folders in a given directory, If no directory provided it shows from current directoty
created: 2019-08-21
updated: 2019-08-21
---

ls command used to list files and folders in a given directory, If no directory provided it shows from current directoty

Lets take following is your directory structure as an example to go through different commands with ls

```
$ tree ./
./
├── images
│   ├── cat.png
│   ├── dog.png
│   ├── moon.png
│   └── sun.png
├── movies
│   ├── action
│   │   ├── bar.mp4
│   │   └── foo.mp4
│   └── comedy
├── music
│   ├── song1.mp3
│   └── song2.mp3
└── readme.txt

5 directories, 9 files
```


## 1. list files and folders from current directory

```sh
ls
```

#### Output
```sh
$ ls
images		movies		music		readme.txt
```

## 2. list detailed informaiton of files and folders from current directory

```sh
ls -l
```

#### Output
```sh
$ ls -l
total 0
drwxr-xr-x  7 userName  wheel  224 Aug 21 19:31 images
drwxr-xr-x  5 userName  wheel  160 Aug 21 19:23 movies
drwxr-xr-x  4 userName  wheel  128 Aug 21 19:33 music
-rw-r--r--  1 userName  wheel    0 Aug 21 19:34 readme.txt
```

## 3. Include hidden files in the result

```sh
ls -a
```

## 4. Show human friendly file sizes 

```sh
ls -h
```

## 5. List files and folders from a given directory

```sh
ls movies/action/
```
#### Output

```sh
$ ls movies/action/
bar.mp4	foo.mp4
```


## 6. Combining options
You can run the ls command by combining multiple options like following

```sh
ls -alh
```