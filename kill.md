---
title: kill Linux Command
description: kill Linux Command is used to send signals to running processes.
created: 2019-09-13
updated: 2019-09-13
---

kill Linux Command is used to send signals to running processes.


## Syntax

```sh
kill [SIGNAL] PID
```

## Examples

```sh
kill -9 3829 #=> kills process with id 3829
```

## Options

`kill -l` command display all available options with kill

### Note: Following are from Ubuntu 16.04

|Signal|Description|
|---|---|
|1| SIGHUP|
|2| SIGINT|
|3| SIGQUIT|
|4| SIGILL|
|5| SIGTRAP|
| 6| SIGABRT|
| 7| SIGBUS|
| 8| SIGFPE|
| 9| SIGKILL|
|10| SIGUSR1|
|11| SIGSEGV|
|12| SIGUSR2|
|13| SIGPIPE|
|14| SIGALRM|
|15| SIGTERM|
|16| SIGSTKFLT|
|17| SIGCHLD|
|18| SIGCONT|
|19| SIGSTOP|
|20| SIGTSTP|
|21| SIGTTIN|
|22| SIGTTOU|
|23| SIGURG|
|24| SIGXCPU|
|25| SIGXFSZ|
|26| SIGVTALRM|
|27| SIGPROF|
|28| SIGWINCH|
|29| SIGIO|
|30| SIGPWR|
|31| SIGSYS|
|34| SIGRTMIN|
|35| SIGRTMIN+1|
|36| SIGRTMIN+2|
|37| SIGRTMIN+3|
|38| SIGRTMIN+4|
|39| SIGRTMIN+5|
|40| SIGRTMIN+6|
|41| SIGRTMIN+7|
|42| SIGRTMIN+8|
|43| SIGRTMIN+9|
|44| SIGRTMIN+10|
|45| SIGRTMIN+11|
|46| SIGRTMIN+12|
|47| SIGRTMIN+13|
|48| SIGRTMIN+14|
|49| SIGRTMIN+15|
|50| SIGRTMAX-14|
|51| SIGRTMAX-13|
|52| SIGRTMAX-12|
|53| SIGRTMAX-11|
|54| SIGRTMAX-10|
|55| SIGRTMAX-9|
|56| SIGRTMAX-8|
|57| SIGRTMAX-7|
|58| SIGRTMAX-6|
|59| SIGRTMAX-5|
|60| SIGRTMAX-4|
|61| SIGRTMAX-3|
|62| SIGRTMAX-2|
|63| SIGRTMAX-1|
|64| SIGRTMAX|

### Note: Following are from MacOS

|Signal|Description|
|---|---|
| 1| SIGHUP|
| 2| SIGINT|
| 3| SIGQUIT|
| 4| SIGILL|
| 5| SIGTRAP|
| 6| SIGABRT|
| 7| SIGEMT|
| 8| SIGFPE|
| 9| SIGKILL|
|10| SIGBUS|
|11| SIGSEGV|
|12| SIGSYS|
|13| SIGPIPE|
|14| SIGALRM|
|15| SIGTERM|
|16| SIGURG|
|17| SIGSTOP|
|18| SIGTSTP|
|19| SIGCONT|
|20| SIGCHLD|
|21| SIGTTIN|
|22| SIGTTOU|
|23| SIGIO|
|24| SIGXCPU|
|25| SIGXFSZ|
|26| SIGVTALRM|
|27| SIGPROF|
|28| SIGWINCH|
|29| SIGINFO|
|30| SIGUSR1|
|31| SIGUSR2|