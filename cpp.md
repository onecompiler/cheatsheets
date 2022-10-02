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

### Sample C program

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

## Vectors
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
## Stacks 

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
## The C++ Standard Template Library (STL)

The Standard Template Library (STL) is a set of C++ template classes to provide common programming data structures and functions such as lists, stacks, arrays, etc. It is a library of container classes, algorithms, and iterators. It is a generalized library and so, its components are parameterized.
STL has 4 components:



1.Algorithms
2.Containers
3.Functions
4.Iterators


### Algorithms

- The header algorithm defines a collection of functions specially designed to be used on a range of elements. They act on containers and provide means for various --   operations for the contents of the containers.




1. Algorithm
   - Sorting
   - Searching
   - Important STL Algorithms
   - Useful Array algorithms
   - Partition Operations


2 .Numeric
   - Valarray class
   - Containers


### Containers


- Container classes store objects and data. There are in total seven standards "first-class" container classes and three container adaptor classes and only seven - ---  header files that provide access to these containers or container adaptors.



1. Sequence Containers:
 implement data structures that can be accessed in a sequential manner.
   - vector
   - list
   - deque
   - arrays
   - forward_list( Introduced in C++11)


2.Container Adaptors:
provide a different interface for sequential containers.
  
  - queue
  - priority_queue
  - stack


3.Associative Containers:
implement sorted data structures that can be quickly searched (O(log n) complexity).
   
  - set
  - multiset
  - map
  - multimap


4.Unordered Associative Containers:
implement unordered data structures that can be quickly searched
  
  - unordered_set (Introduced in C++11)
  - unordered_multiset (Introduced in C++11)
  - unordered_map (Introduced in C++11)
  - unordered_multimap (Introduced in C++11)
 
 ![image](https://user-images.githubusercontent.com/75524307/193427187-e93cca0d-4923-4954-a541-b579577eaae2.png)


## Most Useful Algorithms Functions


### Non-modifying sequence operations 

std :: all_of  : Test condition on all elements in range
std :: any_of  : Test if any element in range fulfills condition
std :: none_of : Test if no elements fulfill condition
std :: for_each : Apply function to range
std :: find : Find value in range
std :: find_if : Find element in range
std :: find_if_not : Find element in range (negative condition)
std :: find_end : Find last subsequence in range
std :: find_first_of : Find element from set in range
std :: adjacent_find : Find equal adjacent elements in range
std :: count : Count appearances of value in range
std :: count_if : Return number of elements in range satisfying condition
std :: mismatch : Return first position where two ranges differ
std::equal : Test whether the elements in two ranges are equal
std :: is_permutation : Test whether range is permutation of another
std :: search : Search range for subsequence
std :: search_n : Search range for element
 
 ### Modifying sequence operations

- std :: copy :  Copy range of elements
- std :: copy_n : Copy elements
- std :: copy_if : Copy certain elements of range
- std :: copy_backward : Copy range of elements backward
- std::move : Move range of elements
- std :: move_backward :  Move range of elements backward
- std :: swap : Exchange values of two objects
- std ::swap_ranges : Exchange values of two ranges
- std :: iter_swap : Exchange values of objects pointed to by two iterators
- std ::transform : Transform range
- std ::replace : Replace value in range
- std ::replace_if : Replace values in range
- std :: replace_copy : Copy range replacing value
- std :: replace_copy_if : Copy range replacing value
- std ::fill : Fill range with value
- std :: fill_n : Fill sequence with value
- std ::generate : Generate values for range with function
- std ::generate_n : Generate values for sequence with function
- std ::remove : Remove value from range
- std :: remove_if : Remove elements from range
- remove_copy : Copy range removing value
- remove_copy_if : Copy range removing values
- std ::unique : Remove consecutive duplicates in range

   ### Partition Operations

- std :: is_partitioned : Test whether range is partitioned
- std :: partition : Partition range in two
- std :: stable_partition : Partition range in two – stable ordering
- partition_copy : Partition range into two
- partition_point : Get partition point

   ### Sorting


- std :: sort : Sort elements in range
- std :: stable_sort : Sort elements preserving order of equivalents
- std :: partial_sort : Partially sort elements in range
- std :: partial_sort_copy : Copy and partially sort range
- std :: is_sorted : Check whether range is sorted
- std :: is_sorted_until : Find first unsorted element in range
- std :: nth_element : Sort element in range

### Binary search (operating on partitioned/sorted ranges)

- std :: lower_bound : Return iterator to lower bound
- std :: upper_bound : Return iterator to upper bound
- std :: equal_range : Get subrange of equal elements
- std :: binary_search : Test if value exists in sorted sequence

  ### Merge (operating on sorted ranges)

- std :: merge : Merge sorted ranges
- std :: inplace_merge : Merge consecutive sorted ranges
- std :: includes : Test whether the sorted range includes another sorted range
- std :: set_union : Union of two sorted ranges
- std :: set_intersection : Intersection of two sorted ranges
- std :: set_difference : Difference of two sorted ranges
- std :: set_symmetric_difference : Symmetric difference of two sorted ranges

 ### Heap Operations

- std :: push_heap : Push element into heap range
- std :: pop_heap : Pop element from heap range
- std :: make_heap : Make heap from range
- std :: sort_heap : Sort elements of heap
- std :: is_heap : Test if range is heap
- std :: is_heap_until : Find first element not in heap order
- std :: max : Return the largest
- std :: minmax : Return smallest and largest elements
- std :: min_element : Return smallest element in range
- std :: max_element : Return largest element in range
- std :: minmax_element : Return smallest and largest elements in range


  ### Other Operations

- std :: lexicographical_compare : Lexicographical less-than comparison
- std :: next_permutation : Transform range to next permutation
- std :: prev_permutation : Transform range to previous permutation

## Associative Containers

### Set 

- Sets are a type of associative container in which each element has to be unique because the value of the element identifies it. The values are stored in a specific sorted order i.e. either ascending or descending.

- Syntax:

set<datatype> setname;
Datatype:

-Set can take any data type depending on the values, e.g. int, char, float, etc.


-Example:

set<int> val; // defining an empty set
set<int> val = {6, 10, 5, 1}; // defining a set with values
Note: set<datatype, greater<datatype>> setname; is used for storing values in a set in descending order.
	  
	
### Properties
	
 - Storing order - The set stores the elements in sorted order.
 - Values Characteristics - All the elements in a set have unique values.
 - Values Nature - The value of the element cannot be modified once it is added to the set, though it is possible to remove and then add the modified value of that        element. Thus, the values are immutable.
 - Search Technique - Sets follow the Binary search tree implementation.
 - Arranging order - The values in a set are unindexed.
Note: To store the elements in an unsorted(random) order,  unordered_set() can be used.


### Some Basic Functions Associated with Set: 

- begin() - Returns an iterator to the first element in the set.
- end() - Returns an iterator to the theoretical element that follows the last element in the set.
- size() - Returns the number of elements in the set.
- max_size() - Returns the maximum number of elements that the set can hold.
- empty() - Returns whether the set is empty.
- The time complexities for doing various operations on sets are:

Insertion of Elements - O(log N)
Deletion of Elements - O(log N)
	
### Map

Maps are associative containers that store elements in a mapped fashion. Each element has a key value and a mapped value. No two mapped values can have the same key values.

*Some basic functions associated with Map: 

- begin() - Returns an iterator to the first element in the map.
- end() - Returns an iterator to the theoretical element that follows the last element in the map.
- size() - Returns the number of elements in the map.
- max_size() - Returns the maximum number of elements that the map can hold.
- empty() - Returns whether the map is empty.
- pair insert(keyvalue, mapvalue) - Adds a new element to the map.
- erase(iterator position) - Removes the element at the position pointed by the iterator.
- erase(const g)- Removes the key-value 'g' from the map.
- clear() - Removes all the elements from the map.
	
	
 ### Multimap 

It is similar to a map with the addition that multiple elements can have the same keys. Also, it is NOT required that the key-value and mapped value pair have to be unique in this case. One important thing to note about multimap is that multimap keeps all the keys in sorted order always. These properties of multimap make it very much useful in competitive programming.
	
*Some Basic Functions associated with multimap: 

- begin() - Returns an iterator to the first element in the multimap
- end() - Returns an iterator to the theoretical element that follows last element in the multimap
- size() - Returns the number of elements in the multimap
- max_size() - Returns the maximum number of elements that the multimap can hold
- empty() - Returns whether the multimap is empty
- pair<int,int> insert(keyvalue,multimapvalue) - Adds a new element to the multimap


  ### Unordered Sets


- An unordered_set is implemented using a hash table where keys are hashed into indices of a hash table so that the insertion is always randomized. All operations on the unordered_set takes constant time O(1) on an average which can go up to linear time O(n) in worst case which depends on the internally used hash function, but practically they perform very well and generally provide a constant time lookup operation. 
- The unordered_set can contain key of any type – predefined or user-defined data structure but when we define the key of type user define the type, we need to specify our comparison function according to which keys will be compared.

- insert()- Insert a new {element} in the unordered_set container.
- begin()- Return an iterator pointing to the first element in the unordered_set container.
- end()- Returns an iterator pointing to the past-the-end-element.
- count()- Count occurrences of a particular element in an unordered_set container.
- find()- Search for an element in the container.
- clear()- Removes all of the elements from an unordered_set and empties it.
- cbegin()- Return a const_iterator pointing to the first element in the unordered_set container.
- cend()- Return a const_iterator pointing to past-the-end element in the unordered_set container or in one of it’s bucket.
- bucket_size()- Returns the total number of elements present in a specific bucket in an unordered_set container.
- erase()- Remove either a single element or a range of elements ranging from start(inclusive) to end(exclusive).
- size()- Return the number of elements in the unordered_set container.
- swap()- Exchange values of two unordered_set containers.
- emplace()- Insert an element in an unordered_set container.
- max_size()- Returns maximum number of elements that an unordered_set container can hold.
- empty()- Check if an unordered_set container is empty or not.
	
	
	
### Unordered Multiset
	

-The internal implementation of unordered_multiset is same as that of unordered_set and also uses hash table for searching, just the count value is associated with each value in former one. Due to hashing of elements it has no particular order of storing the elements so all element can come in any order but duplicate element comes together. All operation on unordered_multiset takes constant time on average but can go upto linear in worst case. 
	
- insert()- Inserts new elements in the unordered_multiset. Thus increases the container size.
- begin()- Returns an iterator pointing to the first element in the container or to the first element in one of its bucket.
- end()- Returns an iterator pointing to the position immediately after the last element in the container or to the position immediately after the last element in one of its bucket.
- empty()- It returns true if the unordered_multiset container is empty. Otherwise, it returns false.
- find()- Returns an iterator which points to the position which has the element val.
- cbegin()- Returns a constant iterator pointing to the first element in the container or to the first element in one of its bucket.
- cend()- Returns a constant iterator pointing to the position immediately after the last element in the container or to the position immediately after the last element in one of its bucket.
- equal_range()- Returns the range in which all the elements are equal to a given value.
- emplace()- Inserts a new element in the unordered_multiset container.
- clear()- Clears the contents of the unordered_multiset container.
- count()- Returns the count of elements in the unordered_multiset container which is equal to a given value.
- size()- The size() method of unordered_multiset is used to count the number of elements of unordered_set it is called with.
- max_size- The max_size() of unordered_multiset takes the maximum number of elements that the unordered_multiset container is able to hold.
- swap()- Swaps the contents of two unordered_multiset containers.
- erase() - Used to remove either a single element or, all elements with a definite value or, a range of elements ranging from start(inclusive) to end(exclusive).
	



### Unordered_map 


unordered_map is an associated container that stores elements formed by the combination of key-value and a mapped value. The key value is used to uniquely identify the element and the mapped value is the content associated with the key. Both key and value can be of any type predefined or user-defined. 

Internally unordered_map is implemented using Hash Table, the key provided to map are hashed into indices of a hash table that is why the performance of data structure depends on hash function a lot but on an average, the cost of search, insert and delete from the hash table is O(1). 
	
### Methods of unordered_map : 

- at(): This function in C++ unordered_map returns the reference to the value with the element as key k.
- begin(): Returns an iterator pointing to the first element in the container in the unordered_map container
- end(): Returns an iterator pointing to the position past the last element in the container in the unordered_map container
- bucket(): Returns the bucket number where the element with the key k is located in the map.
- bucket_count: bucket_count is used to count the total no. of buckets in the unordered_map. No parameter is required to pass into this function.
- bucket_size: Returns the number of elements in each bucket of the unordered_map.
- count(): Count the number of elements present in an unordered_map with a given key.
- equal_range: Return the bounds of a range that includes all the elements in the container with a key that compares equal to k.
- find(): Returns iterator to element.
- empty(): checks whether container is empty in the unordered_map container.
- erase(): erase elements in the container in the unordered_map container.
