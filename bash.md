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

## Common I/O commands

```bash
echo "Hello from Bash!" # Print string with trailing \n
printf "%s\n" "Hello from Bash!" # Print string with trailing \n
```

```bash
read my_variable # Read string to a variable
```

## Variables

### Defining and erasing

```bash
declare my_variable="Hello from Bash!" # Declare a global variable
local my_variable="Hello from Bash!" # Declare a local variable
```

```bash
unset my_variable # Unset a variable
```

### Incrementing and decrementing

```bash
((my_variable++)) # Increment a variable
((my_variable--)) # Decrement a variable
```

## Arithmetic

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

## String manipulation

```bash
grep --quiet 'Bash' <<< 'Hello from Bash!'
```

```bash
sed 's/Bash/bash/' <<< 'Hello from Bash!'
```

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

| Class               | Description         |
| ---                 | ---                 |
| `\w`                | Word character      |
| `\d`                | Digit character     |
| `\W`                | Not word character  |
| `\D`                | Not digit character |

## Conditionals

```bash
if [[ $my_variable -lt $another_variable ]]; then
  ···
elif [[ $my_variable -eq $another_variable ]]; then
  ···
else
  ···
fi
```

| Operator            | Meaning                                   |
| ---                 | ---                                       |
| `-lt`               | [L]ess [t]han                             |
| `-eq`               | [Eq]ual                                   |
| `-gt`               | [G]reater [t]han                          |
| `-le`               | [L]ess than or [e]qual to                 |
| `-ge`               | [G]reater than or [e]qual to              |
| `-ne`               | [N]ot [E]qual                             |
| `-f`                | [F]ile exists                             |
| `-d`                | [D]irectory exists                        |
| `-r`                | File or directory exists and [r]eadable   |
| `-w`                | File or directory exists and [w]ritable   |
| `-x`                | File or directory exists and e[x]ecutable |

## Loops

```bash
for i in {1,10}; do
  ...
done
```

## Command substitution

```bash
declare my_variable=$(expr $my_variable + 1)
```

## Functions

### Defining and erasing

```bash
my_function() {
  ···
}
```

```bash
unset my_function
```
