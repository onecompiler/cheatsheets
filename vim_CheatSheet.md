
	
	#Insert mode
		i
	
	#Insert after cursor
        	a
	
	#Create blank line below & insert
        	o

	#Normal mode
		esc key

	#Write changes
		:w

	#Quit without saving changes
		:q!

	#Write and quit
		:wq

	#Enter visual mode to select characters
		v

	#Enter visual mode to select line
		V

	#Cut(Delete) selected text
		d

	#Cut current line
		dd

	#Copy(Yank) selected text
		y

	#Copy current line
		y$

	#Paste after cursor
		p

	#Paste before cursor
		P

	#Undo vim action
		u

	#Redo vim action
		ctrl + r

	#Open a bash session from Vim
		:! bash

	#Exit a bash session to go back to Vim
		exit

	#Turn word-wrap on/off
        	:set wrap
        	:set nowrap	

	#Turn line numbers on/off
        	:set number
        	:set nonumber

	#Open multiple files in new tabs (from bash prompt)
        	vim -p <file1> <file2> ...

	#Quick switch to next tab
        	gt

	#Quick switch to previous tab
        	gT

	#Save tab session to file
        	:mksession <session_filename.vim>

	#Load saved tab session (from bash prompt)
        	vim -S <session_filename.vim>

	#Search and replace all patterns found in file
		:%s/<pattern match>/<replace with>/g
	
