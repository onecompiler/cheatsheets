---
title: ps Linux Command
description: ps (processes status) Linux Command is used to show information about running processes
created: 2019-09-13
updated: 2019-09-13
---

ps (processes status) Linux Command is used to show information about running processes


## Syntax

```sh
ps [Option(s)]
```

## Examples


#### Display current shell process 
```sh
$ ps
  PID TTY           TIME CMD
64639 ttys000    0:00.05 -bash
```

#### Display all processes information

```sh
ps -A
```
OR
```sh
ps -e
```

#### Display all processes as full-format listing

```sh
ps -ef
```

#### Display user running processes

```sh
ps -x
```

#### Display process information by PID

```sh
ps -pf 1234
```

#### Display multiple processes information by PIDs

```sh
ps -pf 1234,1235,1236
```

#### Searching for a process with name

```sh
 ps -ef | grep chrome
```

```sh
 ps -ef | grep java
```

```sh
 ps -ef | grep nodejs
```