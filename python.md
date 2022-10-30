---
title: Python
description: Python cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-04-24
updated: 2022-10-30
---

## Basics

### display
```py
print("hello world")
```
### comments

* `#` is used to comment a line in Python
* You can also comment using a docstring format[```Multiline
                                                comment```]

## Data Types

|Category|Data Type|
|----|-----|
|Text |str|
|Number|int, float, complex|
|Boolean|bool|
|Binary|bytes, bytearray, memoryview|
|Set|set, frozenset|
|Sequence|list, tuple, range|
|Mapping|dict|
|None|NoneType|

* type() is used to know the data type of a variable

### Data casting

|Constructor function| desc|
|-----|----|
|int()| constructs an integer from any form of data like string, float or integer|
|float()|constructs a float number from any form of data like string, float or integer|
|str()|constructs a string from any form of data like string, float or integer|

## Type Casting

In Python, Type casting or type converion is the method to convert one data-type to another data-type.
Basically there are 2 types of type casting:

1:Implicit
This method of type casting is performed by the machine or the python interpreter itself. There is no need to define externally.

2:Explicit
In this method of type casting,the user performs the changes by using the predefined functions externally.There can be a loss of data in this type of type conversion

## Variables

In Python, declaring variables is not required. Means you don't need to specify whether it is an integer or string etc as Python is a dynamically typed language.

## Operators

|Type|Operators|
|----|----|
| Arithmetic Operators| +  -  *  /  %  **  //|
| Comparision Operators| ==  !=   >  >=  <  <=|
| Bitwise Operators| &  ^  \| ^ ~ << >> |
| Logical Operators| &&  \|\| ! |
| Assignment Operators|=  +=  -=  *=  /=  %=  **=  //=|
| Membership Operators| in, not in |
| Identity Operators | is, is not|


## Functions

```py
# declaring a function
def function-name(parameters){ # here parameters are optional
    #code
}
function-name(parameters); # calling a function
```
## Collections

### 1. List

List is ordered collection of items and are mutable `[]` are used to represent lists. 

### Example
```py
mylist1=["iPhone","Pixel","Samsung"]
print(mylist1[0]) # prints iPhone
print(mylist1[7]) # throws IndexError : list index out of range
print(mylist1[-1]) # prints Samsung
```

Using List() to declare a list.
```py
mylist2=list()
mylist2.append("iPhone") # adds iPhone to the end of list
mylist2.append("Pixel") # adds Pixel to the end of list
mylist2.append("Samsung") # adds Samsung to the end of list
print(mylist2[0]) # prints iPhone
print(mylist2[7]) # throws IndexError : list index out of range
print(mylist2[-1]) # prints Samsung
```
### Operations

|Operation|Description|
|----|----|
|lst.append(val)| add an item to list at end|
|lst.extend(seq)| add sequence of items to list at end|
|lst.insert(index,val)| insert an item at given index|
|lst.remove(val) | remove first item with value val|
|lst.pop(`[index]`)→value| remove & return item at index|
|lst.sort()| sort the given list items|
|lst.reverse() |reverse the given list items|
|lst.count() |Returns the number of elements with the specified value|
|lst.clear() |Removes all the elements from the list|
|lst.index() |Returns the index of the first element with the specified value|
|lst.copy() |Returns a copy of the list|

### 2. Tuple

Tuple is ordered collection of items and are immutable `()` are used to represent Tuples.

### Example

```py
myTuple = ["iPhone","Pixel","Samsung"]
print(myTuple[0]) # prints iPhone
print(myTuple[7]) # throws IndexError: tuple index out of range
print(myTuple[-1]) # prints Samsung
```

### 3. Set

Set is unordered collection of items and it is unindexed. `{}` are used to represent sets.
**Note**- to create an empty set use the built-in set() function. If we write new_set = {} this will create a dictionary instead of a set.

### Example

```py
mySet = {"iPhone", "Pixel", "Samsung"}
mySet.add('OnePlus')
print(mySet) # prints {'iPhone', 'Samsung', 'OnePlus', 'Pixel'}
```
### Operations

|Method | Description | Usage |
|----|----|----|
|add() | to add an element to the set |mySet.add('value')|
|clear()| to remove all the elements from the set | mySet.clear()|
|pop() | to remove last element from the set| mySet.pop()|
|remove() | to remove a specified element from the set|mySet.remove("value")|
|del()| to delete a set| del myset|
|copy()	| to return a copy of the set| copySet = mySet.copy()|
|union() |	to return a set containing the union of sets|  mySet3 = mySet1.union(mySet2)|
|update() | to update the set with the union of this set and others| mySet1.update(mySet2)|

### 4. Dictionary
Dictionary is a collection of key value pairs which is unordered, can be changed, and indexed. They are written in curly brackets with key - value pairs. 
**Note**- From Python 3.6 new Dict() method implementation had made it possible for maintaining the order of the key-value pairs added in the respective             order.
### Example
```py
mydict = {
    "brand" :"iPhone",
    "model": "iPhone 11"
}
val = mydict["brand"]
print(val) # prints iPhone
```
|Operation|Description|
|----|----|
|`d[key]`=value| To add a new key-value pair to dictionary or to change it's value if key is existing|
|d.copy()| Returns a copy of the dictionary|
|d.keys()|Returns a list containing all the dictionary's keys|
|d.values()|Returns a list of all the values in the dictionary|
|d.items()|Removes the element with the specified key|
|d.clear()| To empty the dictionary items.|
|del `d[key]`| To remove an item from a dictionary.
|d.pop(key)|To remove an item from a dictionary.|
|d.popitem()|removes the item that was last inserted into the dictionary|
|d.get(key)| Returns the value of the specified key|
|d.setdefault(key)|Returns the value of the specified key. If the key does not exist then returns the default value provided|
|d.fromkeys(key,value)| Returns a dictionary with specified keys and values|

## Conditional Statements

### 1. If

```py
if conditional-expression :
    #code
```
### 2. If-else
```py
if conditional-expression :
    #code
else :
    #code
```
### 3. If-elif-else Ladder

```py
if conditional-expression :
    #code
elif conditional-expression :
    #code
else :
    #code
```
### 4. Try Except

The try block lets you test a block of code for errors. The except block lets you handle the error.
```py
try:
    print(1/0)
except:
    print("You can't divide by zero!")
```

The finally block lets you execute code, regardless of the result of the try- and except blocks.
```py
try:
    print(x)
except:
    print("Variable x is not defined")
finally:
    print("The program is finished.")
```

You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error.
```py
a = input("Digit a number: ")
try:
    b = [i for i in range(int(a))]
    print(b[3])
except ValueError:
    print("You didn't digit a number.")
except IndexError:
    print("Your list have less than 4 numbers.")
finally:
    print("Python is cool.")
```

## Loops

### 1. For
For loop is used to iterate over arrays(list, tuple, set, dictionary) or strings.

### Syntax
```py
for variable in arrays :
    #code
```
### 2. While
```py
while condition  
    #code 
```
## Useful String Methods
||||
|----|----|----|
|str.strip()|str.lower()|str.upper()|
|str.replace("str to be replaced","new string to replace")|str.split("seperator")|len(str)|
|+ for concatenation|str.count(substr)|str.find(substr)|
|str.index(substr, start, end)|str.join(array)|str.partition(substr)|
|str.zfill(len)|str.swapcase()|str.isdecimal()|
|str.isdigit()|str.islower()|str.isupper()|
|str.endswith(value, start, end)|str.startswith(value, start, end)|str.isspace()|

## Python with Mongodb

Install a python driver `pymongo` to connect with MongoDB. 
### Create Database
```py
import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = db["sample"]
```
### Create collection 
```py
import pymongo
db = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = db["sample"]

mycln = mydb["details"]
```
### Insert
```py
#insert a single document
doc = mycln.insert_one(mydict)
# insert multiple documents
mylist =[
    {"name": "foo", "age": 20},
    {"name": "bar", "age": 25},
    {"name": "apple", "age": 30}
]
doc1 = mycln.insert_many(mylist)
```
### Read
```py
#to return all the documents
for doc in mycln.find():
  print(doc)

# to return first occurence
doc1=mycln.find_one()
print(doc1)
```
### Update
```py
# to update a single document
mycln.update_one({"name" : "foo"}, {"$set":{"age": 23}})
```
### Delete
```py
# to delete a single document
doc1 = mycln.delete_one({"name" : "foo"})
```
## Python with Files

### Create
Use open() function with `c` or `a` or `w` as mode.

```py
file = open("myfile.txt","c")
```
### Read
Use open() function with `r` as mode.

```py
file = open("myfile.txt","r")
print(file.read())
```
### Update or Append
Use open() function with  `a` or `w` as mode.

```py
file = open("myfile.txt","a")
file.write("Happy learning!!")
file.close()
```
### Delete

For deleting files, you must import os module and use `os.remove()` function.
```py
import os
os.remove(filename)
```
### nested list --list within list
<!-- easily accessible elements using indexes -->
L=['a',['bb','cc'],'d']
L[1][1]=0
print(L)
<!-- prints  ['a',['bb',0],'d'] -->
