---
title: echo Linux Command
description: echo Linux Command used to output text to screen. This is available in most of the operating systems along with Linux systems.
created: 2019-09-12
updated: 2019-09-12
---

echo Linux Command used to output text to screen. This is available in most of the operating systems along with Linux systems.


## Syntax

```sh
echo [option(s)] [string(s)]
```

## Examples

```sh
echo Hello World! #=> Hello World!
```

```sh
x=5
echo $x #=> 5
```

```sh
x=8
echo x value is $x #=> x value is 8
```

```sh
echo Hello \nWorld! #=> Hello
                    #   World!
```
`Note: \n is for new line`

```sh
echo Hello \tWorld! #=> Hello   World!
```
`Note: \t is for tab

```sh
echo * #=> Prints files and folders of current directory
```

```sh
echo *.txt #=> Prints all .txt files from current directory
```

- Using option new Line ‘\n‘ and horizontal tab ‘\t‘ simultaneously.
```sh
$ echo -e "\n\Onecompiler \n\tis \n\ta \n\tcommunity \n\tof \n\tNerds" 

	Onecompiler
	is 
	a 
	community 
	of
	Nerds 
```
