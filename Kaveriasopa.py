Showing Output To User
The print function is used to display or print output as follows

print("Content that you wanna print on screen")
Taking Input From the User
The input function is used to take input from the user as follows:

var1 = input("Enter your name: ")
Empty List
This method allows you to create an empty list

my_list = []
Empty Dictionary
By putting two curly braces, you can create a blank dictionary

my_dict = {}
range Function
range function returns a sequence of numbers, eg, numbers starting from 0 to n-1 for range(0, n)

range(int_value)

Comments
Comments are used to make the code more understandable for programmers, and they are not executed by compiler or interpreter.

Single line comment
# This is a single line comment
Multi-line comment
'''This is a
multi-line
comment'''
Escape Sequence
An escape sequence is a sequence of characters; it doesn't represent itself (but is translated into another character) when used inside string literal or character. Some of the escape sequence characters are as follows:

Newline
Newline Character

\n
Backslash
It adds a backslash

\\
Single Quote
It adds a single quotation mark

\'
Tab
It gives a tab space

\t
Backspace
It adds a backspace

\b
Octal value
It represents the value of an octal number

\ooo
Hex value
It represents the value of a hex number

\xhh
Carriage Return
Carriage return or \r will just work as you have shifted your cursor to the beginning of the string or line.

\r

Strings
Python string is a sequence of characters, and each character can be individually accessed using its index.

String
You can create Strings by enclosing text in both forms of quotes - single quotes or double quotes.

variable_name = "String Data"
Slicing
Slicing refers to obtaining a sub-string from the given string. The following code will include index 1, 2, 3, and 4 for the variable named var_name

var_name[1 : 5]
isalnum() method
Returns True if all the characters in the string are alphanumeric, else False

string_variable.isalnum()
isalpha() method
Returns True if all the characters in the string are alphabets

string_variable.isalpha()
isdecimal() method
Returns True if all the characters in the string are decimals

string_variable.isdecimal()
isdigit() method
Returns True if all the characters in the string are digits

string_variable.isdigit()
islower() method
Returns True if all characters in the string are lower case

string_variable.islower()
isspace() method
Returns True if all characters in the string are whitespaces

string_variable.isspace()
isupper() method
Returns True if all characters in the string are upper case

string_variable.isupper()
lower() method
Converts a string into lower case equivalent

string_variable.lower()
upper() method
Converts a string into upper case equivalent

string_variable.upper()
strip() method
It removes leading and trailing spaces in the string

string_variable.strip()
List
A List in Python represents a list of comma-separated values of any data type between square brackets.

var_name = [element1, element2, ...]
index method
Returns the index of the first element with the specified value

list.index(element)
append method
Adds an element at the end of the list

list.append(element)
extend method
Add the elements of a given list (or any iterable) to the end of the current list

list.extend(iterable)
insert method
Adds an element at the specified position

list.insert(position, element)
pop method
Removes the element at the specified position and returns it

list.pop(position)
remove method
The remove() method removes the first occurrence of a given item from the list

list.remove(element)
clear method
Removes all the elements from the list

list.clear()
count method
Returns the number of elements with the specified value

list.count(value)
reverse method
Reverses the order of the list

list.reverse()
sort method
Sorts the list

list.sort(reverse=True|False)

Tuples
Tuples are represented as comma-separated values of any data type within parentheses.

Tuple Creation
variable_name = (element1, element2, ...)
Lets talk about some of the tuple methods:

count method
It returns the number of times a specified value occurs in a tuple

tuple.count(value)
index method
It searches the tuple for a specified value and returns the position.

tuple.index(value)
Sets
A set is a collection of multiple values which is both unordered and unindexed. It is written in curly brackets.

Set Creation: Way 1
var_name = {element1, element2, ...}
Set Creation: Way 2
var_name = set([element1, element2, ...])
Set Methods
Lets talk about some of the methods of sets:

add() method
Adds an element to a set

set.add(element)
clear() method
Remove all elements from a set

set.clear()
discard() method
Removes the specified item from the set

set.discard(value)
intersection() method
Returns intersection of two or more sets

set.intersection(set1, set2 ... etc)
issubset() method
Checks if a set is a subset of another set

set.issubset(set)
pop() method
Removes an element from the set

set.pop()
remove() method
Removes the specified element from the set

set.remove(item)
union() method
Returns the union of two or more sets

set.union(set1, set2...)
Dictionaries
The dictionary is an unordered set of comma-separated key:value pairs, within {}, with the requirement that within a dictionary, no two keys can be the same.

Dictionary
<dictionary-name> = {<key>: value, <key>: value ...}
Adding Element to a dictionary
By this method, one can add new elements to the dictionary

<dictionary>[<key>] = <value>
Updating Element in a dictionary
If a specified key already exists, then its value will get updated

<dictionary>[<key>] = <value>
Deleting an element from a dictionary
del keyword is used to delete a specified key:value pair from the dictionary as follows:

del <dictionary>[<key>]
Dictionary Functions & Methods
Below are some of the methods of dictionaries

len() method
It returns the length of the dictionary, i.e., the count of elements (key: value pairs) in the dictionary

len(dictionary)
clear() method
Removes all the elements from the dictionary

dictionary.clear()
get() method
Returns the value of the specified key

dictionary.get(keyname)
items() method
Returns a list containing a tuple for each key-value pair

dictionary.items()
keys() method
Returns a list containing the dictionary's keys

dictionary.keys()
values() method
Returns a list of all the values in the dictionary

dictionary.values()
update() method
Updates the dictionary with the specified key-value pairs

dictionary.update(iterable)
Conditional Statements
The if, elif and else statements are the conditional statements in Python, and these implement selection constructs (decision constructs).

if Statement
if(conditional expression):
    statements
if-else Statement
if(conditional expression):
    statements
else:
    statements
if-elif Statement
if (conditional expression):
    statements
elif (conditional expression):
    statements
else:
    statements
Nested if-else Statement
if (conditional expression):
    if (conditional expression):
        statements
    else:
        statements
else:
    statements
Loops in Python
A loop or iteration statement repeatedly executes a statement, known as the loop body, until the controlling expression is false (0).

For Loop
The for loop of Python is designed to process the items of any sequence, such as a list or a string, one by one.

for <variable> in <sequence>:
    statements_to_repeat
While Loop
A while loop is a conditional loop that will repeat the instructions within itself as long as a conditional remains true.

while <logical-expression>:
    loop-body
Break Statement
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

for <var> in <sequence>:
    statement1
    if <condition>:
        break
    statement2
statement_after_loop
Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur.

for <var> in <sequence>:
    statement1
    if <condition> :
        continue
    statement2
    statement3
    statement4
Functions
A function is a block of code that performs a specific task. You can pass parameters into a function. It helps us to make our code more organized and manageable.

Function Definition
def my_function(parameters):
    pass #statements
File Handling
File handling refers to reading or writing data from files. Python provides some functions that allow us to manipulate data in the files.

open() function
var_name = open("file name", "opening mode")
close() function
var_name.close()
read () function
The read functions contains different methods, read(),readline() and readlines()

read() #return one big string
It returns a list of lines

readlines() #returns a list
It returns one line at a time

readline #returns one line at a time
write function
This function writes a sequence of strings to the file.

write() #Used to write a fixed sequence of characters to a file
It is used to write a list of strings

writelines()
append() function
The append function is used to append to the file instead of overwriting it. To append to an existing file, simply open the file in append mode by using 'a' as the second argument of open() as follows:

file = open("Hello.txt", "a")
Exception Handling
An exception is an unusual condition that results in an interruption in the flow of a program.

try and except
A basic try-catch block in python. When the try block throws an error, the control goes to the except block.

try:
    [Statement body block]
    raise Exception()
except Exception as e:
    [Error processing block]
Object Oriented Programming (OOPS)
It is a programming approach that primarily focuses on using objects and classes. The objects can be any real-world entities.

class
The syntax for writing a class in python

class class_name:
    pass #statements
class with a constructor
The syntax for writing a class with the constructor in python

class:

    # Default constructor
    def _init_(self):
        self.name = "CodeWithHarry"

    # A method for printing data members
    def print_me(self):
        print(self.name)
Creating an object
Instantiating an object can be done as follows:

<object-name> = <class-name>(<arguments>)
filter function
The filter function allows you to process an iterable and extract those items that satisfy a given condition

filter(function, iterable)
issubclass function
Used to find whether a class is a subclass of a given class or not as follows

issubclass(obj, classinfo) # returns true if obj is a subclass of classinfo
Iterators and Generators
Here are some of the advanced topics of the Python programming language like iterators and generators
