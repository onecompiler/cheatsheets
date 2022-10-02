---
title: C++ Programming language 
description: C++ Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-04-30
updated: 2020-04-30
---

C++ is a widely used middle-level programming language which is used in developing major operating systems( Windows, Linux, Android, Ubuntu, iOS etc), Games, databases and compilers etc.  

## Basics
* `cin >> x`: read value into the variable x from input stream
* `cout << x`: print value to the output stream
* `//`: single line comments
* `/* */`: Multi line comments

```c
#include <iostream>
using namespace std;
int main() {
    cout << "Hello World!!";
    return 0;
}  
```
* `#include <iostream>`: iostream is a inbuilt header library which allows you to deal with input and output objects like cout etc.
* `using namespace std`: Specifies that the object and variable names can be used from standard library.
* `cin`: to accept input from standard input device i.e keyboard.
* `cout`: to print the output.
* `main()`: main function is the entry point of any C++ program.
* `return 0`: To end the main function

#### How to compile a program in C++

Open your terminal, Navigate to the directory where you have saved your program. Consider firstprogram.cpp is the name of your program.

```c
sudo g++ -o firstprogram firstprogram.cpp
```

#### How to run a C++ program

```
./firstprogram
```

## Data types

| Types | Data-type|
|----|----|
|Basic | int, char, float, double, short, short int, long int etc |
|Derived | array, pointer etc |
|User Defined Data Type | structure, enum, Class, Union, Typedef |

## Variables

```c
data-type variable-name = value;
```
```c
int value = 10; // declaring int variable and assigning value 10 to it
char grade = 'A'; // declaring char variable and assigning value A to it
```
### Naming convention
* only letters (both uppercase and lowercase letters), digits and underscore(`_`).
* cannot contain white spaces
* First letter should be either a letter or an underscore(`_`).
* Variable type can't be changed
* Case sensitive

## Arrays

```c
data-type array-name[size]; // one-dimensional Array
data-type array-name[size][size]; // two-dimensional Array
```
### Example:
```c
int a[5] = {1,2,3,4,5};
int a[2][3] = {
                {1,2,3},
                {4,5,6}
              };
```
## Literals or Constants
|Literal | Example|
|----|----|
|Integer Literal- decimal|255|
|Integer Literal- octal|0377|
|Integer Literal- hexadecimal|0xFF|
|Float point Literal|53.0f, 79.02|
|Character literals| 'a', '1'|
|String literals| "OneCompiler", "Foo"|

### Escape sequences
|Escape sequence| Description|
|----|----|
|\n	| New line|
|\r	| Carriage Return|
|\?	| Question mark|
|\t	| Horizontal tab|
|\v	| Vertical tab|
|\f	|Form feed|
|\\	| Backslash|
|\'	| Single quotation|
|\"	| Double quotation|
|\0 | Null character|
|\b	|Back space|

## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %|
| comparision Operator| < , > , <= , >=, != , ==|
| Bitwise Operator| & , ^ , `\|` |
| Logical Operator| && , `\|\|`, ! |
| Assignment Operator|= , += , -= , *= , /= , %=, <<=, >>=, &=, ^=, `\|=` |
| Ternary Operator| ? : |
| sizeof operator| sizeof() |

## Conditional Statements

### 1. If
```c
if(conditional-expression)
{
    //code
}
```
### 2. If-else

```c
if(conditional-expression)
{
    //code
} else {
    //code
}
```
### 3. If-else-if ladder

```c
if(conditional-expression-1)
{
    //code
} else if(conditional-expression-2) {
    //code
} else if(conditional-expression-3) {
    //code
}
....
else {
    //code
}
```
### 4. Switch

```c
switch(conditional-expression){    
case value1:    
 //code    
 break;  //optional  
case value2:    
 //code    
 break;  //optional  
...    
    
default:     
 //code to be executed when all the above cases are not matched;    
} 
```
## Loops

### 1. For
```c
for(Initialization; Condition; Increment/decrement){  
//code  
} 
```
### 2. While
```c
while(condition){  
//code 
}  
```
### 3. Do-While
```c
do{  
//code 
} while(condition); 
```

## Functions

Function is a sub-routine which contains set of statements.

```c
// declaring a function
return_type function_name(parameters);

// defining a function
return_type function_name(parameters){  
//code
}

// calling a function
function_name (parameters)
```

## Pointers

Pointer is a variable which holds the memory information(address) of another variable of same data type.

```c
datatype *pointername;
```
### Example
```c
int x = 10, *ptr;

/*ptr = x; // Error because ptr is adress and x is value
*ptr = &x;  // Error because x is adress and ptr is value */

ptr = &x; // valid because &x and ptr are addresses
*ptr = x; // valid because both x and *ptr values 
```
## Structures

Structure is a user-defined data type where it allows you to combine data of different data types.

```c
struct structure_name {

   member definition;
   member definition;
   ...
   member definition;
} [one or more structure variables]; 

struct structure_name variable name; //declaring structure variables
```

## Classes

A class in C++ is the building block that leads to Object-Oriented programming. It is a user-defined data type, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A C++ class is like a blueprint for an object.

```c
class MyClass {       // The class
  public:             // Access specifier
    int myNum;        // Attribute (int variable)
    string myString;  // Attribute (string variable)

    void print() {
        cout<<myNum;  // Method (function)
    }
};
```

## Enum

Enumeration data type is a user-defined data type in C++. `enum` keyword is used to declare a new enumeration types in C++. 

```c
enum name{constant1, constant2, constant3, ....... } var-list;
```
### Example
```c
enum month{January, February, March, April, May, June, July, August, September, October, November, December} name;
```

## Typedef
Typedef is used to explicitly define new data type names by using the keyword `typedef`. It defines a name for an existing data type but doesn't create a new data type. 

```c
typedef data-type name;
```
### Example
```c
typedef unsigned int distance;  // typedef of int 
```

## Sort one-line

Sorting is one of the most basic functions applied to data. It means arranging the data in a particular fashion, which can be increasing or decreasing. There is a builtin function in C++ STL by the name of sort(). 
This function internally uses IntroSort. In more details it is implemented using hybrid of QuickSort, HeapSort and InsertionSort.

```c

#include<iostream>
#include<algorithm>
using namespace std;

int main(){

int arr[] = {3,2,1};
int n = 3 ; // size of the array

sort(arr, arr+n); // sorting the array

vector<int> v;

v = {3,2,1};

sort(v.begin(), v.end()); // sorting in the vector

}

```
## Header Files

|Name| Use|
|----|----|
|#include<bits/stdc++.h>   | It contains all the libraries present in C++|
|#include<stdio.h>   | It is used to perform input and output operations|
|#include<string.h>  | It is used to perform various string operations|
|#include<math.h>    | It is used to perform mathematical operations|
|#include<iomanip.h> | It is used to access set() and setprecision()|
|#include<signal.h>  | It is used to perform signal handling functions like sign|
|#include<stdarg.h>  | It is used to perform standard argument functions|
|#include<errno.h>   | It is used to perform error handling operations like errno|
|#include<fstream.h> | It is used to control the data to read from a file|
|#include<time.h>    | It is used to perform functions related to date() and time|

## Standard Template Library(STL)

## Containers

Containers store objects and data. There are different type of containers which are used based on the requirement. Some of the commonly used containers are:

## Vector
Vectors are same as dynamic arrays. They will be resized on element insertions & deletions.

Functions associated with the vector are:

Following functions return iterator 
begin() 
end() 
rbegin() 
rend() 
cbegin() 
cend() 
crbegin() 
crend() 

```c
#include <iostream>
#include <vector>
  
using namespace std;
  
int main()
{
    vector<int> v1;
  
    for (int i = 1; i <= 10; i++)
        v1.push_back(i);
  
    cout << "Output of begin and end: ";
    for (auto i = v1.begin(); i != v1.end(); ++i)
        cout << *i << " ";

    for (auto i: v1)
        cout << i << " ";
  
    return 0;
}

```
## Stack

Stacks are a type of container adaptors with LIFO(Last In First Out) type of working, where a new element is added at one end (top) and an element is removed from that end only.

The functions associated with stack are: 
empty() – Returns whether the stack is empty – Time Complexity : O(1) 
size() – Returns the size of the stack – Time Complexity : O(1) 
top() – Returns a reference to the top most element of the stack – Time Complexity : O(1) 
push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1) 
pop() – Deletes the top most element of the stack – Time Complexity : O(1) 

```c

#include <iostream>
#include <stack>
using namespace std;
int main() {
	stack<int> stack;
	stack.push(21);
	stack.push(22);
	stack.push(24);
	stack.push(25);
	
	stack.pop();
	stack.pop();

	while (!stack.empty()) {
		cout << ' ' << stack.top();
		stack.pop();
	}
}

```

## Queue

Queues are a type of container adaptors that operate in a first in first out (FIFO) type of arrangement. Elements are inserted at the back (end) and are deleted from the front.

empty() - Returns whether the queue is empty.
size() - Returns the size of the queue.
swap() - Exchange the contents of two queues but the queues must be of the same type, although sizes may differ.
emplace() - Insert a new element into the queue container, the new element is added to the end of the queue.
front() - Returns a reference to the first element of the queue.
back() - Returns a reference to the last element of the queue.
push(g) - Adds the element ‘g’ at the end of the queue.
pop() removes the element

```c

#include <iostream>
#include <queue>
using namespace std;
int main() {
	queue<int> q;
	q.push(21);
	q.push(22);
	q.push(24);
	q.push(25);
	
	q.pop();
	q.pop();

	while (!q.empty()) {
		cout << ' ' << q.front();
		q.pop();
	}
}

```

## Priority Queue

Priority queues are specifically designed such that the first element of the queue is either the greatest or the smallest of all elements in the queue and elements are in non increasing order.

push(g) - Adds the element ‘g’ at the top of the priority queue.
pop() - Removes the element from the top.
empty() - Returns whether the priority_queue is empty.
size() - Returns the size of the priority_queue.
top()  - Returns a reference to the top element of the priority_queue.

### Max heap

It contains elements in the priority queue in decreasing order. It means that the maximum element will always be at the top of the priority queue. 

```c
#include <iostream>
#include <queue>
using namespace std;
int main() {
	priority_queue<int> pq;
	pq.push(1);
	pq.push(2);
	pq.push(4);
	pq.push(3);
	
	pq.pop();
	pq.pop();

	while (!pq.empty()) {
		cout << ' ' << pq.top();
		pq.pop();
	}
}

```

### Min Heap

It contains elements in the priority queue in non-decreasing order. It means that the minimum element will always be at the top of the priority queue. 

```c
#include <iostream>
#include <queue>
using namespace std;
int main() {
	priority_queue<int, vector<int>, greater<int>> pq;
	pq.push(5);
	pq.push(2);
	pq.push(4);
	pq.push(1);
	
	pq.pop();
	pq.pop();

	while (!pq.empty()) {
		cout << ' ' << pq.top();
		pq.pop();
	}
}

```

### Set

Sets are a type of container in which each element has to be unique. The values are stored in a specific sorted order.

insert(g) - Adds a new element ‘g’ to the set.
erase(g) - Removes the value ‘g’ from the set.
size() – Returns the number of elements in the set.
empty() – Returns whether the set is empty.
begin() – Returns an iterator to the first element in the set.
end() – Returns an iterator to the element that follows the last element in the set.

```c
#include <iostream>
#include <set>
using namespace std;
int main() {
	set<int> st;
	st.insert(40);
    st.insert(30);
    st.insert(60);
    st.insert(20);
    st.insert(50);

    // printing set st
	for (i = st.begin(); i != st.end(); i++) {
        cout << *i << " ";
    }

    //another way to print
    for (auto i: st) {
        cout << i << " ";
    }
}

```

### Map

Maps are type of containers that store elements in a mapped fashion. Each element has a key value and a mapped value. No two mapped values can have the same key values.

insert(keyvalue, mapvalue) – Adds a new element to the map.
erase(g)– Removes the key-value ‘g’ from the map.
begin() – Returns an iterator to the first element in the map.
end() – Returns an iterator to the element that follows the last element in the map.
size() – Returns the number of elements in the map.
empty() – Returns whether the map is empty.
clear() – Removes all the elements from the map.

```c
#include <iostream>
#include <map>
using namespace std;
int main() {
	map<int, int> mp;
	mp.insert({1, 40});
    mp.insert({2, 30});
    mp.insert({3, 60});
    mp.insert({4, 20});
    mp.insert({5, 50});

    mp[6] = 10;   // another way of inserting a value in a map

    // printing map mp
	for (i = mp.begin(); i != mp.end(); i++) {
        cout << " " << i->first << " " << i->second << endl;
    }

    for (auto i: mp) {
        cout << " " << i.first << " " << i.second << endl;
    }
}

```

## Algorithms

The header algorithm defines a collection of functions specially designed to be used on a range of elements. They act on containers and provide means for various operations for the contents of the containers. Some of the commonly used algorithms are:

### Sorting
```c
sort(start_address, end_address);          //sorts an array/vector in non-decreasing order
```

### Searching
```c
binary_search(start_address, end_address, key);          //returns true if a key is present in an array/vector
```

### Reverse 
```c
reverse(start_address, end_address);          //reverses an array/vector from start addresss to end address     
```

### Swap
```c
swap(first_element, second_element);          //swaps two elements with each other
```

### Max Element
```c
*max_element(start_address, end_address);          //returns the maximum element present in an array/vector
```

### Min Element
```c
*min_element(start_address, end_address);          //returns the minimum element present in an array/vector
```

### Sum
```c
*accumulate(start_address, end_address, initial_sum);          //returns the sum of an array/vector
```

### Count
```c
*count(start_address, end_address, x);          //count the number of times 'x' appear in an array/vector
```

### Find
```c
*find(start_address, end_address, x);          //find the first occurence of 'x' in an array/vector
```

### Upper Bound
```c
*upper_bound(start_address, end_address, x);          //returns iterator pointing to the first element which is not less than 'x'
```

### Lower Bound
```c
*lower_bound(start_address, end_address, x);          //returns iterator pointing to the first element which is just greater than 'x'
```

### Next Permutation
```c
*next_permutation(start_address, end_address);          //returns true if next permuation of an array/string exists
```