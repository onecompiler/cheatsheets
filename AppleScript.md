---
name: AppleScript
about: AppleScript is a scripting language created by Apple Inc. that facilitates automated control over scriptable Mac applications.
title: AppleScript - [AppleScript]
labels: New Cheat Sheet
assignees: ''

---


Basic concepts

AppleScript was designed to be used as an accessible end-user scripting language, offering users an intelligent mechanism to control applications, and to access and modify data and documents. AppleScript uses Apple events, a set of standardized data formats that the Macintosh operating system uses to send information to applications, roughly analogous to sending XPath queries over XML-RPC in the world of web services.[3]: xxvi  Apple events allow a script to work with multiple applications simultaneously, passing data between them so that complex tasks can be accomplished without human interaction.[2] For example, an AppleScript to create a simple web gallery might do the following:

Open a photo in a photo-editing application (by sending that application an Open File Apple event).
1.Tell the photo-editing application to manipulate the image (e.g. reduce its resolution, add a border, add a photo credit)
2.Tell the photo-editing application to save the changed image in a file in some different folder (by sending that application a Save and/or Close Apple event).
3.Send the new file path (via another Apple event) to a text editor or web editor application
4.Tell that editor application to write a link for the photo into an HTML file.
5.Repeat the above steps for an entire folder of images (hundreds or even thousands of photos).
6.Upload the HTML file and folder of revised photos to a website, by sending Apple events to a graphical FTP client, by using built-in AppleScript commands, or by sending Apple events to Unix FTP utilities.
7.For the user, hundreds or thousands of steps in multiple applications have been reduced to the single act of running the script, and the task is accomplished in much less time and with no possibility of random human error. A large complex script could be developed to run only once, while other scripts are used again and again.

An application's scriptable elements are visible in the application's Scripting Dictionary (distributed as part of the application), which can be viewed in any script editor. Elements are generally grouped into suites, according to loose functional relationships between them. There are two basic kinds of elements present in any suite: classes and commands.

Classes are scriptable objects—for example, a text editing application will almost certainly have classes for windows, documents, and texts—and these classes will have properties that can be changed (window size, document background color, text font size, etc.), and may contain other classes (a window will contain one or more documents, a document will contain text, a text object will contain paragraphs and words and characters).
Commands, by contrast, are instructions that can be given to scriptable objects. The general format for a block of AppleScript is to tell a scriptable object to run a command.
All scriptable applications share a few basic commands and objects, usually called the Standard Suite—commands to open, close or save a file, to print something, to quit, to set data to variables—as well as a basic application object that gives the scriptable properties of the application itself. Many applications have numerous suites capable of performing any task the application itself can perform. In exceptional cases, applications may support plugins which include their own scripting dictionaries.

AppleScript was designed with the ability to build scripts intuitively by recording user actions. Such AppleScript recordability has to be engineered into the app—the app must support Apple events and AppleScript recording;[12] as Finder supports AppleScript recording, it can be useful for reference. When AppleScript Editor (Script Editor) is open and the Record button clicked, user actions for recordable apps are converted to their equivalent AppleScript commands and output to the Script Editor window. The resulting script can be saved and re-run to duplicate the original actions, or modified to be more generally useful.

Comments
Comments can be made multiple ways. A one-line comment can begin with 2 hyphens (--). In AppleScript 2.0, first released in Mac OS X Leopard, it may also begin with a number sign (#). This permits a self-contained AppleScript script to be stored as an executable text file beginning with the shebang line #!/usr/bin/osascript Example:
```
--This is a one line comment
```
# So is this! (in Mac OS X Leopard or later)
For comments that take up multiple lines, AppleScript uses parentheses with asterisks inside. Example:

(* This is a
multiple
line
comment *)
Hello, world!
In AppleScript, the traditional "Hello, World!" program could be written in many different forms, including:
```
display dialog "Hello, world!" -- a modal window with "OK" and "Cancel" buttons
-- or
display alert "Hello, world!" -- a modal window with a single "OK" button and an icon representing the app displaying the alert
-- or
say "Hello, world!" -- an audio message using a synthesized computer voice
```
AppleScript has several user interface options, including dialogs, alerts, and list of choices. (The character ¬, produced by typing ⌥ Option+return in the Script Editor, denotes continuation of a single statement across multiple lines.)

-- Dialog
```
set dialogReply to display dialog "Dialog Text" ¬
	default answer "Text Answer" ¬
	hidden answer false ¬
	buttons {"Skip", "Okay", "Cancel"} ¬
	default button "Okay" ¬
	cancel button "Skip" ¬
	with title "Dialog Window Title" ¬
	with icon note ¬
	giving up after 15
```
```
-- Choose from list
set chosenListItem to choose from list {"A", "B", "3"} ¬
	with title "List Title" ¬
	with prompt "Prompt Text" ¬
	default items "B" ¬
	OK button name "Looks Good!" ¬
	cancel button name "Nope, try again" ¬
	multiple selections allowed false ¬
	with empty selection allowed
``` 
```
-- Alert
set resultAlertReply to display alert "Alert Text" ¬
	as warning ¬
	buttons {"Skip", "Okay", "Cancel"} ¬
	default button 2 ¬
	cancel button 1 ¬
	giving up after 2
```
Each user interaction method can return the values of buttons clicked, items chosen or text entered for further processing. For example:

```
display alert "Hello, world!" buttons {"Rudely decline", "Happily accept"}
set theAnswer to button returned of the result
if theAnswer is "Happily accept" then
	beep 5
else
	say "Piffle!"
end if
```
Natural language metaphor
Whereas Apple events are a way to send messages into applications, AppleScript is a particular language designed to send Apple events. In keeping with the objective of ease-of-use for beginners, the AppleScript language is designed on the natural language metaphor, just as the graphical user interface is designed on the desktop metaphor. A well-written AppleScript should be clear enough to be read and understood by anyone, and easily edited. The language is based largely on HyperCard's HyperTalk language, extended to refer not only to the HyperCard world of cards and stacks, but also theoretically to any document. To this end, the AppleScript team introduced the AppleEvent Object Model (AEOM), which specifies the objects any particular application "knows".

The heart of the AppleScript language is the use of terms that act as nouns and verbs that can be combined. For example, rather than a different verb to print a page, document or range of pages (such as printPage, printDocument, printRange), AppleScript uses a single "print" verb which can be combined with an object, such as a page, a document or a range of pages.
```
print page 1

print document 2

print pages 1 thru 5 of document 2
```
Generally, AEOM defines a number of objects—like "document" or "paragraph"—and corresponding actions—like "cut" and "close". The system also defines ways to refer to properties of objects, so one can refer to the "third paragraph of the document 'Good Day'", or the "color of the last word of the front window". AEOM uses an application dictionary to associate the Apple events with human-readable terms, allowing the translation back and forth between human-readable AppleScript and bytecode Apple events. To discover what elements of a program are scriptable, dictionaries for supported applications may be viewed. (In the Xcode and Script Editor applications, this is under File → Open Dictionary.)

To designate which application is meant to be the target of such a message, AppleScript uses a "tell" construct:
```
tell application "Microsoft Word"
  quit
end tell
```
Alternatively, the tell may be expressed in one line by using an infinitive:
```
tell application "Microsoft Word" to quit
```
For events in the "Core Suite" (activate, open, reopen, close, print, and quit), the application may be supplied as the direct object to transitive commands:
```
quit application "Microsoft Word"
```
The concept of an object hierarchy can be expressed using nested blocks:
```
tell application "QuarkXPress"
  tell document 1
    tell page 2
      tell text box 1
        set word 5 to "Apple"
      end tell
    end tell
  end tell
end tell
```
The concept of an object hierarchy can also be expressed using nested prepositional phrases:

pixel 7 of row 3 of TIFF image "my bitmap"
which in another programming language might be expressed as sequential method calls, like in this pseudocode:

getTIFF("my bitmap").getRow(3).getPixel(7);
AppleScript includes syntax for ordinal counting, "the first paragraph", as well as cardinal, "paragraph one". Likewise, the numbers themselves can be referred to as text or numerically, "five", "fifth" and "5" are all supported; they are synonyms in AppleScript. Also, the word "the" can legally be used anywhere in the script in order to enhance readability: it has no effect on the functionality of the script.

Examples of scripts
A failsafe calculator:
```
tell application "Finder"
	-- Set variables
	set the1 to text returned of (display dialog "1st" default answer "Number here" buttons {"Continue"} default button 1)
	set the2 to text returned of (display dialog "2nd" default answer "Number here" buttons {"Continue"} default button 1)
	try
		set the1 to the1 as integer
		set the2 to the2 as integer
	on error
		display dialog "You may only input numbers into a calculator." with title "ERROR" buttons {"OK"} default button 1
		return
	end try
	
	-- Add?
	if the button returned of (display dialog "Add?" buttons {"No", "Yes"} default button 2) is "Yes" then
		set ans to (the1 + the2)
		display dialog ans with title "Answer" buttons {"OK"} default button 1
		say ans
	-- Subtract?	
	else if the button returned of (display dialog "Subtract?" buttons {"No", "Yes"} default button 2) is "Yes" then
		set ans to (the1 - the2)
		display dialog ans with title "Answer" buttons {"OK"} default button 1
		say ans
	-- Multiply?	
	else if the button returned of (display dialog "Multiply?" buttons {"No", "Yes"} default button 2) is "Yes" then
		set ans to (the1 * the2)
		display dialog ans with title "Answer" buttons {"OK"} default button 1
		say ans
	-- Divide?	
	else if the button returned of (display dialog "Divide?" buttons {"No", "Yes"} default button 2) is "Yes" then
		set ans to (the1 / the2)
		display dialog ans with title "Answer" buttons {"OK"} default button 1
		say ans
	else
		delay 1
		say "You haven't selected a function. The operation has cancelled."
	end if
	
end tell
```
A simple username and password dialog box sequence. Here, the username is John and password is app123:
```
tell application "Finder"
	set passAns to "app123"
	set userAns to "John"
	if the text returned of (display dialog "Username" default answer "") is userAns then
		display dialog "Correct" buttons {"Continue"} default button 1
		if the text returned of (display dialog "Username : John" & return & "Password" default answer "" buttons {"Continue"} default button 1 with hidden answer) is passAns then
			display dialog "Access granted" buttons {"OK"} default button 1
		else
			display dialog "Incorrect password" buttons {"OK"} default button 1
		end if
	else
		display dialog "Incorrect username" buttons {"OK"} default button 1
	end if
end tell
```
