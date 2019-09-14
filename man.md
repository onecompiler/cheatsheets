---
title: man Linux Command
description: man Linux Command is used to display human friendly manual page of a given command.
created: 2019-09-13
updated: 2019-09-13
---

man Linux Command is used to display human friendly manual page of a given command.

## Syntax

```sh
man [ option(s) ] [ COMMAND ]
```

## Example

```sh
$ man head
HEAD(1)                   BSD General Commands Manual                  HEAD(1)

NAME
     head -- display first lines of a file

SYNOPSIS
     head [-n count | -c bytes] [file ...]

DESCRIPTION
     This filter displays the first count lines or bytes of each of the speci-
     fied files, or of the standard input if no files are specified.  If count
     is omitted it defaults to 10.

     If more than a single file is specified, each file is preceded by a
     header consisting of the string ``==> XXX <=='' where ``XXX'' is the name
     of the file.

EXIT STATUS
     The head utility exits 0 on success, and >0 if an error occurs.

SEE ALSO
     tail(1)

HISTORY
     The head command appeared in PWB UNIX.

BSD                              June 6, 1993                              BSD
```

```sh
Note: To quit than man press `Shift` + `:` then type q
```
