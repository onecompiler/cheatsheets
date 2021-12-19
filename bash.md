---
title: Bash shell
description: Bourne-Again SHell, an `sh`-compatible command-line interpreter.
created: 2021-12-19
updated: 2021-12-19
---

## Sample program

```bash
#!/usr/bin/env bash

echo "Hello from Bash!"
```

## I/O commands

Print a string with trailing `\n`:

```bash
echo "Hello from Bash!"
# or
printf "%s\n" "Hello from Bash!"
```

Read a string to a variable:

```bash
read my_variable
```

- [Echo Command in Linux with Examples](https://linuxize.com/post/echo-command-in-linux-with-examples/)
- [Bash printf Command](https://linuxize.com/post/bash-printf-command/)

## Variables

### Defining and erasing

Declare a global/local variable:

```bash
declare my_variable="Hello from Bash!"
local my_variable="Hello from Bash!"
```

Remove a variable:

```bash
unset my_variable
```

### Incrementing and decrementing

Increment/decrement a variable:

```bash
((my_variable++))
((my_variable--))
```

- [How to Increment and Decrement Variable in Bash (Counter)](https://linuxize.com/post/bash-increment-decrement-variable/)

## Arithmetic

### Integer manipulations

Calculate a number sum:

```bash
$((1 + 2))
```

| Operator            | Performs       |
| ---                 | ---            |
| `+`                 | Addition       |
| `-`                 | Subtraction    |
| `*`                 | Multiplication |
| `/`                 | Division       |
| `%`                 | Modulo         |
| `**`                | Exponentiation |

### Float manipulations

Calculate a number sum:

```bash
awk 'BEGIN { print 1.0 + 2.0 }'
```

| Operator            | Performs       |
| ---                 | ---            |
| `+`                 | Addition       |
| `-`                 | Subtraction    |
| `*`                 | Multiplication |
| `/`                 | Division       |
| `%`                 | Modulo         |
| `**`                | Exponentiation |

- [Awk Command in Linux with Examples](https://linuxize.com/post/awk-command/)

## String manipulation

Match a string against a regular expresion:

```bash
[[ 'Hello from Bash!' =~ 'Bash' ]]
```

Remove a shortest/longest matching pattern from beggining:

```bash
my_variable=${my_variable#*=}
my_variable=${my_variable##*=}
```

Remove a shortest/longest matching pattern from ending:

```bash
my_variable=${my_variable%*=}
my_variable=${my_variable%%*=}
```

Remove a matching pattern from everywhere:

```bash
my_variable=${my_variable//Bash/bash}
```

> Extended regular expressions described.

| Pattern             | Matches                   |
| ---                 | ---                       |
| `x?`                | Zero or one `x` chars     |
| `x*`                | Any count `x` chars       |
| `x+`                | One or more  `x` chars    |
| `x{n}`              | n times `x` chars         |
| `x{n,m}`            | n to m times `x` chars    |
| `x{n,}`             | n or more times `x` chars |
| `[xy]`              | `x` or y char             |
| `[^xy]`             | not `x` or y char         |

## Conditionals

Compare two variables:

```bash
if [[ $my_variable -lt $another_variable ]]; then
  ···
elif [[ $my_variable -eq $another_variable ]]; then
  ···
else
  ···
fi
```

| Integer operator    | Meaning                                   |
| ---                 | ---                                       |
| `-lt`               | [L]ess [t]han                             |
| `-eq`               | [Eq]ual                                   |
| `-gt`               | [G]reater [t]han                          |
| `-le`               | [L]ess than or [e]qual to                 |
| `-ge`               | [G]reater than or [e]qual to              |
| `-ne`               | [N]ot [E]qual                             |

| String operator     | Meaning                                   |
| ---                 | ---                                       |
| `==`                | [Eq]ual                                   |
| `!=`                | [N]ot [E]qual                             |

| File operator       | Meaning                                   |
| ---                 | ---                                       |
| `-f`                | [F]ile exists                             |
| `-d`                | [D]irectory exists                        |
| `-r`                | File or directory exists and [r]eadable   |
| `-w`                | File or directory exists and [w]ritable   |
| `-x`                | File or directory exists and e[x]ecutable |

- [Bash if..else Statement](https://linuxize.com/post/bash-if-else-statement/)

## Loops

Iterate over a number range:

```bash
for i in {1,10}; do
  ...
done
```

- [Bash For Loop](https://linuxize.com/post/bash-for-loop/)

## Command substitution

Replace a command invocation with it's stdout output:

```bash
$(expr $my_variable + 1)
```

## Process substitution

Replace a command invocation with a temporary file name with a command stdout output:

```bash
<(expr $my_variable + 1)
```

## Functions

### Defining and erasing

Declare a function:

```bash
my_function() {
  ···
}
```

Remove a function:

```bash
unset my_function
```

- [Bash Functions](https://linuxize.com/post/bash-functions/)