---
title: SCP (secure copy) command
description: SCP command is used to securely copy files btween two locations i.e local to a remote location or remote location to local, you can also transfer from one remote location to another remote location. 
created: 2019-06-20
updated: 2019-06-20
color: #7f8c8d
---


SCP command is used to securely copy files btween two locations i.e local to a remote location or remote location to local, you can also transfer from one remote location to another remote location.

## Local to remote location
```sh
scp /path/to/local/file user@remote_host:/path/in/remote/location
```

## Remote location to local
```sh
scp user@remote_host:/path/in/remote/location /path/to/local/file 
```

## Copying multiple files
```sh
scp /path/to/local/file1 /path/to/local/file2 user@remote_host:/path/in/remote/location
```

## Copying entire directory 
```sh
scp -r /path/to/local/directory user@remote_host:/path/in/remote/location
```

## SCP Options
|Option|Description|Example|
|---|---|---|
|`-C`|Force SCP to compress data|`scp -C foo.txt ubuntu@1.1.1.1:/home/ubuntu/ `|
|`-r`|recursively copy files from directories||
|`-v`|verbose mode to see transfer details|`scp -v foo.txt ubuntu@1.1.1.1:/home/ubuntu/ `|
|`-l`|limit the bandwidth|`scp -l 100 foo.txt ubuntu@1.1.1.1:/home/ubuntu/ `|