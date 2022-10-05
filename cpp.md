---
title: C++ Programming language 
description: C++ Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-04-30
updated: 2020-04-30
---

C++ is a widely used middle-level programming language which is used in developing major operating systems( Windows, Linux, Android, Ubuntu, iOS etc), Games, databases and compilers etc.  

## Basics
* `cin >> x`: read value into the variable x from input stream
* `cout << x`: printf value to the output stream
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
|Boolean literals| true, false|

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
| Bitwise Operator| & , ^ , |
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

## Some frequently used data structures (c++ STL)

These data structures are present in built-in standard template library (STL) of C++ and are used very frequently. These data structures are needed to be included as the header files.

### Vectors
Vectors are same as dynamic arrays. They will be resized on element inseertions & deletions.

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
  
    return 0;
}

```
### Stacks 

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

### Queue

Queues are a type of container adaptors that operate in a first in first out (FIFO) type of arrangement. Elements are inserted at the back (end) and are deleted from the front

queue::empty()	Returns whether the queue is empty.

queue::size()	Returns the size of the queue.

queue::swap()	Exchange the contents of two queues but the queues must be of the same type, although sizes may differ.

queue::emplace()	Insert a new element into the queue container, the new element is added to the end of the queue.

queue::front()	Returns a reference to the first element of the queue.

queue::back()	Returns a reference to the last element of the queue.

queue::push(g) 	Adds the element ‘g’ at the end of the queue.

queue::pop() removes the element

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

### Priority Queue

Priority queues are data structures, in which the elements are in sorted order, either in max to min, or min to max.

Priority queue is the other name of Heap Data Stucture in c++.

There are two types of heap : 

1. Max - heap

2. Min - heap

By default, c++ creates max heap using priority queue.

Common opperations related to priority queue are : 

push() : to add element in priority queue

pop() : to remove element from priority queue

top() : to find the smallest / largest element in priority queue

empty() : to return whether heap is empty or not

size() : to find the size of heap


Time complexities : 

Push and pop takes O(logn) time for each operation because of internal sorting

top and empty takes O(1) time for each operation

```c

#include <iostream>
#include <priority_queue>
using namespace std

int main()
{
    // to create max heap:
    priority_queue<int> maxHeap;

    // to create min heap:
    priority_queue<int, vector<int>, greater<int> > minHeap;

    maxheap.push(4), maxHeap.push(2), maxHeap.push(7);
    maxheap.pop();

    while(!maxHeap.empty())
    {
        cout<<maxheap.top()<<endl;
        maxHeap.pop();
    }
    return 0;
}

```

### Set 

Set is a data structure in which elements are sorted in incresing order and duplicates are not present. So, baiscally it is used when we want unique elements in sorted order.

Basic operations : 

insert() : inserts an element in set

erase() : removes an element from set

find() : to search a specific element in set

empty() : returns whether set is empty or not

size() : to find the size of set

Time complexities : 

insert and erase takes O(logn) time because of internal sorting 

rest all opeations are O(1)

```c

#include <iostream>
#include <set>
using namespace std;

int main()
{
    set<int> set;

    set.insert(5);
    set.insert(3);
    set.insert(6);
    set.insert(2);
    set.insert(3);
    set.erase(5);
    cout<<set.size()<<endl;
    set.find(3) != set.end() ? cout<<"found"<<endl : cout<<"not found"<<endl;

    for(int x : set)
    {
        cout<<x<<endl;
    }

    return 0;
}

```

### unordered_set

Unordered set is a data structure in which only unique elements are present. It is a best way to remove duplicates. 

Basic operations : 

insert() : inserts an element in set

erase() : removes an element from set

find() : to search a specific element in set

empty() : returns whether set is empty or not

size() : to find the size of set

Time complexities : 

all opeations are O(1)

```c

#include <iostream>
#include <unordered_set>
using namespace std;

int main()
{
    unordered_set<int> u_set;

    u_set.insert(5);
    u_set.insert(3);
    u_set.insert(6);
    u_set.insert(2);
    u_set.insert(3);
    u_set.erase(5);
    cout<<u_set.size()<<endl;
    u_set.find(3) != u_set.end() ? cout<<"found"<<endl : cout<<"not found"<<endl;

    for(int x : u_set)
    {
        cout<<x<<endl;
    }
    return 0;
}

```

### multiset

multiset is a data structure similar to set but with one additional feature that it can contain dulpicates also. So, baiscally it is used when we want duplicates elements also in sorted order.

Basic operations : 

insert() : inserts an element in multiset

erase() : removes an element from multiset

find() : to search a specific element in multiset

empty() : returns whether multiset is empty or not

size() : to find the size of multiset

Time complexities : 

insert and erase takes O(logn) time because of internal sorting 

rest all opeations are O(1)

```c

#include <iostream>
#include <set>
using namespace std;

int main()
{
    multiset<int> m_set;

    m_set.insert(5);
    m_set.insert(3);
    m_set.insert(6);
    m_set.insert(2);
    m_set.insert(3);
    m_set.erase(5);
    cout<<m_set.size()<<endl;
    m_set.find(3) != m_set.end() ? cout<<"found"<<endl : cout<<"not found"<<endl;

    for(int x : m_set)
    {
        cout<<x<<endl;
    }

    return 0;
}

```

### Map

Map is a data structure used to store key value pairs, that too in sorted order with respect to keys.

Common operations :

erase() : removes an element from map

find() : to search a specific element in map

empty() : returns whether map is empty or not

size() : to find the size of map

Time complexities : 

inserting and removing pairs tame O(logn) time due to internal sorting.

Rest all operations are O(1).

```c

#include <iostream>
#include <map>
using nampspace std;

int main()
{
    map<int, string> mp;
    mp[2] = "Aditya";
    mp[4] = "Ajay";
    mp[3] = "Anshu";
    mp[3] = "Adarsh";

    for(auto x : mp)
    {
        cout<<x.first<<" "<<x.second<<endl;
    }
    return 0;
}

```

### unordered_map

It is similar to map, but the data are not sorted.

Common operations :

erase() : removes an element from map

find() : to search a specific element in map

empty() : returns whether map is empty or not

size() : to find the size of map

Time complexities : 

All operations take O(1) on average.

```c

#include <iostream>
#include <unordred_map>
using nampspace std;

int main()
{
    map<int, string> u_mp;
    u_mp[2] = "Aditya";
    u_mp[4] = "Ajay";
    u_mp[3] = "Anshu";
    u_mp[3] = "Adarsh";

    for(auto x : u_mp)
    {
        cout<<x.first<<" "<<x.second<<endl;
    }
    return 0;
}

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

sort(arr, arr+n); // sorting the array in ascending order
sort(arr, arr+n, greater<int>()); // sorting the array in descending order

vector<int> v;

v = {3,2,1};

sort(v.begin(), v.end()); // sorting in the vector in ascending order
sort(v.begin(), v.end(), greater<int>()); // sorting in the vector in descending order

}

```
## Header Files

|Name| Use|
|----|----|
|#include<stdio.h>   | It is used to perform input and output operations|
|#include<string.h>  | It is used to perform various string operations|
|#include<math.h>    | It is used to perform mathematical operations|
|#include<iomanip.h> | It is used to access set() and setprecision()|
|#include<signal.h>  | It is used to perform signal handling functions like sign|
|#include<stdarg.h>  | It is used to perform standard argument functions|
|#include<errno.h>   | It is used to perform error handling operations like errno|
|#include<fstream.h> | It is used to control the data to read from a file|
|#include<time.h>    | It is used to perform functions related to date() and time|
|#include<graphics.h>    | It is used include and facilitate graphical operations in program|
|#include<bits/stdc++.h>    |It is used to include all the standard library files|
