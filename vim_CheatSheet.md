---
title: Vim
description: Vim is a text editor for Unix that comes with Linux, BSD, and macOS
created: 2022-10-09
updated: 2022-10-12
---

### Exiting

```sh
:qa				# Close all files
:qa!			# Close all files, abandon changes
:w				# Save
:wq / :x		# Save and close file
:q				# close file
:q!				# Close file, abandon changes
ZZ				# Save and quit
ZQ				# Quit without checking changes
```
### Exiting insert mode

```sh
Esc / <C-[>		# Exit insert mode
<C-C>			# Exit insert mode, and abort current command
```

### Visual mode

```sh
v				# Enter visual mode
V				# Enter visual line mode
<C-V>			# Enter visual block mode
d / x			# Delete selection
s				# Replace selection
```

### Navigating

```sh
h j k l			# Arrow keys
<C-U> / <C-D>	# Half-page up/down
<C-B> / <C-F>	# Page up/down
b / w			# Previous/next word
ge / e			# Previous/next end of word
fc				# Go forward to character c
Fc				# Go backward to character c
gg				# First line
G				# Last line
zz				# Center this line
zb				# Bottom this line
n				# Next matching search pattern
N				# Previous match
*				# Next whole word under cursor
^				# Start of line (after whitespace)
```

### Editing

```sh
a				# Append
A				# Append from end of line
i				# Insert
o				# Next line
O				# Previous line
S				# Delete line and insert
C				# Delete until end of line and insert
<C-R>			# Redo changes
```

### Clipboard

```sh
x				# Delete character
dd				# Delete line (Cut)
yy				# Yank line (Copy)
"*p / "+p		# Paste from system clipboard
"*y / "+y		# Paste to system clipboard
```

### Jumping

```sh
<C-O>			# Go back to previous location
<C-I>			# Go forward
gf				# Go to file in cursor
```

### Counters

```sh
<C-A>			# Increment number
<C-X>			# Decrement
```

### Spell Checking

```sh
]s				# Move to next misspelled word after the cursor
[s				# Move to previous misspelled word before the cursor
z=				# Suggest spellings for the word under/after the cursor
zg				# Add word to spell list
zw				# Mark word as bad/mispelling
```

