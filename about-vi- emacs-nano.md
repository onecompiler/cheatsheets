#### This is a cheat sheet about some of the famous command line text editor.These are very important to know as these help in development and text editors are the integral part of day to day life of editors. And if you work with remote server using SSH then it will come handy to edit code or text file available on the server.

  

#### In this we will talk about:
- Vim

- Emacs

- Nano

  

### let's get started

  
  
  

## 1.Vim

`vim` is a very popular file editor, especially among programmers. It's actively developed and frequently updated, and there's a very big community around it.

`vi` in modern systems is just an alias to vim , which means `vi` i`m` proved. You start it by running `vi` on the command line.

You can specify a filename at invocation time to edit that specific file:

```Bash

vi test.txt

```

You have to know that Vim has 2 main modes:

- command (or normal) mode

- insert mode

  

When you start the editor, you are in command mode. You can't enter text like you expect from a GUI-based editor. You have to enter insert mode. You can do this by pressing the i key. Once you do so, the `-- INSERT --` word appear at the bottom of the editor.

  

Now you can start typing and filling the screen with the file contents.

You can move around the file with the arrow keys, or using the `h` -`j` -`k` - `l` keys. `h-l` for left-right,`j-k` for down-up. Once you are done editing you can press the esc key to exit insert mode, and go back to **command mode**.

  

At this point you can navigate the file, but you can't add content to it (and be careful which keys you press as they might be commands).

One thing you might want to do now is **saving the file**. You can do so by pressing : (colon), then w .

You can **save and quit** pressing : then w and q : :wq

You can **quit without saving**, pressing : then q and ! : :q!

You can **undo** and edit by going to command mode and pressing u . You can **redo** (cancel an undo) by pressing `ctrl-r` .

  

Those are the basics of working with Vim. From here starts a rabbit hole we can't go into in this little introduction.

I will only mention those commands that will get you started editing with Vim:

- pressing the x key deletes the character currently highlighted

- pressing A goes at the end of the currently selected line

- press 0 to go to the start of the line

- go to the first character of a word and press d followed by w to delete that word. If you follow it with e instead of w , the white space before the next word is preserved

- use a number between d and w to delete more than 1 word, for example use d3w to delete 3 words forward

- press d followed by d to delete a whole entire line.

- Press d followed by $ to delete the entire line from where the cursor is, until the end

To find out more about Vim try running `vimtutor` command,which sholud be already installed in your system.

  
  
  

## 2.Emacs

`emacs` is an awesome editor and it's historically regarded as the editor for UNIX systems. Famously vi vs emacs flame wars and heated discussions caused many unproductive hours for developers around the world. emacs is very powerful.

  

it is` not usually installed in the some linux distro. so,you can install it using

```Bash

Sudo apt-get install emacs

```

  

You can open a new emacs session simply by invoking `emacs` in the command line.

  

You can also edit an existing file calling `emacs <filename>`.You can start editing and once you are done, press `ctrl-x` followed by `ctrl-w` . You confirm the folder and Emacs tell you the file exists, asking you if it should overwrite it Answer `y` , and you get a confirmation of success.

  

You can exit Emacs pressing `ctrl-x` followed by`ctrl-c` . Or `ctrl-x` followed by`c` (keep ctrl pressed).

  

There is a lot to know about Emacs. More than I am able to write in this little introduction. I encourage you to open Emacs and press` ctrl-h`  `r` to open the built-in manual and `ctrl-h`  `t` to open the official tutorial.

  

#### Copy,cut and paste shortcuts:

  

- **ctrl-d :** Cut the character at the position of cursor.

- **ESC d :** Cut the word till next blank space from the current position.

- **ctrl-k :** Cut till end of the line from current position.

- **ctrl-@ :** Mark the current position as beginning for copy.

- **ESC w :** copy area between mark and cursor to paste.

- **ctrl-y :** Yank or Paste the recently copied or cut characters at the current position of cursor.

**Moving cursor:**

- **ctrl-a :** Beginning of the line.

- **ctrl-e :** End of line.

- **ctrl-f :** Move forward by one character.

- **ctrl-b :** Move back by one character.

- **ctrl-n :** Move cursor to next line.

- **ctrl-p :** Cursor to previous line.

- **ESC > :** End of the buffer.

- **ESC < :** Starting of the buffer.

- **ESC f :** Move forward by one word.

- **ESC b :** Move back by one word.

  
  

**Miscellaneous shortcuts:**

  

- **ctrl-z :** Stop Emacs and quit immediately without confirmation(All changes in buffer are lost).

- **ctrl-g :** Cancel current command and revert back from command mode.

- **ctrl-x u :** undo the last command.

- **ctrl-x ctrl-c :** Save and quit.

- **ctrl-h i :** Help in Emacs- describes emacs shortcuts and commands.

  

**Search and Replace:**

- **ctrl-s :** Search forward- prompts for a search terms and search it in the buffer from current cursor position to the end of the buffer.

- **ctrl-r :** Search backwards/reverse- prompts for a search term and search from current position to the beginning of the buffer.

- **ESC % :** Replace- prompts for a search term and a replacement term and replaces the first occurrence of the word in buffer after cursor.

## 3.nano

This is a another powerful command line text editor.This is also powerful and quite a useful text editor.

  

Mostly linux distro and macOS already have this editor installed.that you can chcek using:

```Bash

nano --version

```

if you see that tell you the version then it is already installed in case if doesn't show then you can install using this:

```Bash

sudo apt-get install nano

```

The main syntax to open Nano and to edit a certain file is:

```Bash

nano filename

```

However, if you are in another folder, and you want to open a file (**demo.txt**) in **/path/to/directory**, you can enter this line instead:

```Bash

nano /path/to/directory/demo.txt

```

If you enter a file name and that file is not present in the directory, Nano will create a new file. Meanwhile, if you only execute the nano command without specifying the file name, the Nano text editor will create an empty untitled file and ask for a name when you exit the editor.

  

After running the **nano** command, a new window will pop up where you can freely edit the file. Just use the arrow keys on your keyboard to move the cursor around the text.

  

At the bottom of the window, you can find some shortcuts to use with the Nano editor. The “^” (caret) means that you must press **CTRL** (Windows) or **control** (macOS) to use the chosen command. Here are a few examples.

  

- Press **CTRL + O** to save the changes made in the file and continue editing.

- To exit from the editor, press **CTRL + X**. If there are changes, it will ask you whether to save them or not. Input **Y** for **Yes**, or **N** for **No**, then press **Enter**. But if there are no changes, you will exit the editor right away.

  

### Basic Nano Text Editor Commands

  

We have compiled the most useful commands to help you utilize the Nano text editor more effectively.

  



**Command** |  Explanation
------------------|-----------------------------------------
**CTRL + A**                 |Lets you jump to the beginning of the line.
**CTRL + G**|A  **Help**  window will pop out and show you all the available commands.
**CTRL + E**                |Lets you to jump to the end of the line.
**CTRL + Y**|Scrolls page down
**CTRL + V**| Scrolls page up
**CTRL + O**|To save the file. Nano will ask you to edit or verify the desired file name.
**CTRL + W**|Search for a specified phrase in your text. Press  **ALT + W** to search for the same phrase again.
**CTRL + K**|It cuts the entire selected line to the  **cut buffer**  (similar to clipboard).
**CTRL + U**|To paste the text from the cut buffer into the selected line.
**CTRL + J**|Justifies the current paragraph.
**CTRL + C**|Shows the current cursor position in the text (line/column/character).
**CTRL + R**|Opens a file and inserts it at the current cursor position.
**CTRL + X**|To exit Nano text editor. It prompts a save request if you made any changes to the file.
__"CTRL + \"__|Replaces string or a regular expression.
**CTRL + T**|Invokes the spell checker, if available.
**CTRL + _** |Lets you go to the specified line and column number.
**ALT + A**|To select text. You can combine this command with  **CTRL + K**  to cut a specific part of the text to the cut buffer.
