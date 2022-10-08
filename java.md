---
title: Java
description: Java Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-04-28
updated: 2020-04-28
---

Java is a very popular programming language. Java can be used to develop anything and almost everything like web applications, web servers, application servers, mobile applications and so on. 

## Basics

### Sample Java program
```java
import java.util.Date;

public class HelloWorld {
    public static void main(String[] args) {
        Date now = new Date();
        System.out.println("Hello World!");
        System.out.println("now: " + now);
    }
}
```
* **import** - used to import java libraries
* **class keyword** - to declare a class in java.
* **public keyword** - access modifier represents visibility. Public is visible to all.
* **static keyword** - no need to create an object to invoke the static method. There is no need to create an object to invoke the main method and it's invoked by JVM and saves memory.
* **void** - return type of the method and it doesn't return any value.
* **main** - starting point of the program.
* **String[] args** - for command line arguments
* **System.out.println()** - used to print statement. 

### To Compile a Java program
Go to Command prompt and navigate to the folder where java files are stored.


```cmd
javac example.java
```
### To Run Java program

```cmd
java example 
```

### Comments

`//` - single line comment

`/* */` - multi line comment

`/**  *  */` - documentation comment

## Data types

Two groups of data types

### 1. Primitive data types

| Data type | Description | Range | Size|
|---|---|---|---|
| int| used to store whole numbers|-2,147,483,648 to 2,147,483,647|4 bytes|
|short| used to store whole numbers|-32,768 to 32,767| 2 bytes|
|long| used to store whole numbers|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807| 8 bytes|
|byte| used to store whole numbers|-128 to 127| 1 byte|
|float| used to store fractional numbers|6 to 7 decimal digits| 4 bytes|
|double| used to store fractional numbers|15 decimal digits| 8 bytes|
|boolean| can either store true or false |either true or false| 1 bit|
|char|used to store a single character|one character|2 bytes|

### Examples
```java
int a = 99999; 
short b = 999; 
long c = 99999999999L;
byte d = 99;
double e = 99.99d;
boolean f = true;
char g = 'A';
```
### 2. Non-Primitive data types

Non-primitive data types specifies the complex data values. For example, strings, arrays and classes can be referred as Non-primitive data types.

## Variables
```java
data-type variable-name = value;
```
### Naming convention of variables

* Case sensitive.
* Must should begin with a `lower case letter`. For second word should be a capital like this: firstName, pinCode etc.
* Cannot contain white spaces like first name. 
* special characters like `$` and `_` can be used to begin a variable name.

### Types of Variables

* Local Variables
* Instance Variables
* Static Variables

```java
Class Sum {
    int n1 = 10; // value of Instance  Variables are are instance specific.
    static int n2 = 20; //static variable is Common for all the instances of the class.
    void sum(){
        int n3 = 30; //local variable and they are Inside the body of a method.
        int total = n1+n2+n3;
    }
}
```
## Data Conversions

* String to Number
    ```java
    int i = Intege­r.p­ars­eIn­t(­str);
    double d = Double.pa­rse­Dou­ble­(s­tr);
    ```
* Other types to String
    ```java
    String str = String.va­lue­Of(­va­l);
    ```
## Operators

| Operator type | Description|
|----|-----|
| Arithmetic Operator|+ , - , * , / , %|
| comparision Operator| < , > , <= , >=, != , ==|
| Bitwise Operator| & , ^ , \|, <<, >>, >>>|
| Logical Operator| && , `\|\|`, ! |
| Assignment Operator|= , += , -= , *= , /= , %= |
| Auto-increment and Auto-decrement Operators| ++ , -- |
| Ternary Operator| ? : |

## Final Keyword in JAVA

Final keyword in java is a non-access modifier. It is used to restrict user from making any change in variable, method and classes.

### 1. Final Variable
If any variable is declared with keyword final, then the value of final variable can't be change, i.e. it becomes constant.

### Example

```java
class Student{
  //final variable
  final int id=50;
  void get_id(){
    id=100;
  }
  public static void main(String[] args){
    Student obj=new Student();
    obj.get_id();
  }
}
```

### 2. Final Method
If any method is declared with keyword final, then it can't be overridden.

### Example

```java
class Fruit{
  //final method
  final void run(){
    System.out.println("Inside Fruit Class");
  }
}
class Apple extends Fruit{
  void run(){
    System.out.println("Inside Apple Class");
  }
  public static void main(String[] args){
    Apple obj=new Apple();
    obj.run();
  }
}
```

### 3. Final Class 
If any class is declared with keyword final, then it can't be inherited.

### Example

```java
//final class
final class Fruit{
}
class Apple extends Fruit{
  void run(){
    System.out.println("Inside Apple Class");
  }
  public static void main(String[] args){
    Apple obj=new Apple();
    obj.run();
  }
}
```


## Arrays

Array is a collection of similar data which is stored in continuous memory addresses.

```java
// one dimensional array
data-type[] array-name; 
    OR
data-type array-name[];

// two dimensional array
data-type[][] array-name; 
```
### Example
```java
String[] mobiles = {"iPhone", "Samsung", "OnePlus"};
for (int i = 0; i < mobiles.length; i++) {
  System.out.println(mobiles[i]);
}
mobiles[1] = "Oppo"; // change an array element


```
## Conditional Statements

### 1. If

```java
if(conditional-expression)
{
    //code
}
```
### 2. If-else

```java
if(conditional-expression)
{
    //code
} else {
    //code
}
```
### 3. If-else-if ladder

```java
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
### 4. Nested-If

```java
if(conditional-expression-1) {    
     //code    
          if(conditional-expression-2) {  
             //code
             if(conditional-expression-3) {
                 //code
             }  
    }    
}
```
### 5. Switch
```java
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
```java
for(Initialization; Condition; Increment/decrement){  
//code  
} 
```

### 2. While
```java
while(condition){  
//code 
}  
```
### 3. Do-While
```java
do{  
//code 
}while(condition); 
```
## Collections
|Collection|Description|
|-----|-----|
|Set| Set is a collection of elements which can not contain duplicate values. Set is implemented in HashSets, LinkedHashSets, TreeSet etc|
|List| List is a ordered collection of elements which can have duplicates. Lists are classified into ArrayList, LinkedList, Vectors|
|Queue| FIFO approach, while instantiating Queue interface you can either choose LinkedList or PriorityQueue.|
|Deque| Deque(Double Ended Queue) is used to add or remove elements from both the ends of the Queue(both head and tail)|
|Map| Map contains key-values pairs which don't have any duplicates. Map is implemented in HashMap, TreeMap etc.|

## ArrayList

The ArrayList class is a resizable array, which can be found in the java.util package.

### Example

```java

    import java.util.ArrayList;

public class Main {
  public static void main(String[] args) {
    ArrayList<String> cars = new ArrayList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    System.out.println(cars);
  }
}

```

## HashSet

A HashSet is a collection of items where every item is unique, and it is found in the java.util package:
 
 ###  Example
 
 ```java
 
 import java.util.HashSet;

public class Main {
  public static void main(String[] args) {
    HashSet<String> cars = new HashSet<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("BMW");
    cars.add("Mazda");
    System.out.println(cars);
  }
}
 
 ```
 
 ## HashMap
 
  A HashMap however, store items in "key/value" pairs, and you can access them by an index of another type (e.g. a String).
  
  ```java
  
  import java.util.HashMap;

public class Main {
  public static void main(String[] args) {
    // Create a HashMap object called capitalCities
    HashMap<String, String> capitalCities = new HashMap<String, String>();

    // Add keys and values (Country, City)
    capitalCities.put("England", "London");
    capitalCities.put("Germany", "Berlin");
    capitalCities.put("Norway", "Oslo");
    capitalCities.put("USA", "Washington DC");
    System.out.println(capitalCities);
  }
}
  
  ```

## String Methods
| Method| Description| Example|
|----|----|----|
|char charAt(int index)|returns char value at the specific index| str.charAt(0) //prints o|
|int compareTo(String str)| to compare two strings lexicographically | Str1.compareTo(Str2) //returns 0 if str1 and str2 are equal|
|int length()|returns string length| str.length()|
|static String format(String format, Object... args)|returns a formatted string.| String.format("String is %s",str); |
|String substring(int beginIndex, int endIndex)| to return substring from given begin index to end index.| str.substring(0,3) //prints one|
|String substring(int beginIndex)| to return substring from given begin index| str.substring(3) //prints compiler|
|boolean contains(CharSequence s)|returns true or false after matching the sequence given in the string| str.contains("compiler") // returns true|
|static String join(CharSequence delimiter, CharSequence... elements)|returns a joined string.| String.join("..","Hello","Happy", "Learning"); //returns Hello..Happy..Learning|
|boolean equals(Object another)|checks the equality of string with another and returns true if they are equal.| str1.equals(str2);|
|boolean isEmpty()|to check if the given string is empty.|  str.isEmpty() // returns false|
|String concat(String str)|concatenates the provided string with the another string.| str.concat(" is used to compile code online")|
|String replace(char old, char new)|replaces all occurrences of the specified char value with new char value.|str.replace('r','t');|
|String replace(CharSequence old, CharSequence new)|replaces all occurrences of the specific CharSequence with new one.|str.replace('one','Online');|
|static String equalsIgnoreCase(String another)|compares another string with out considering case.| str1.equalsIgnoreCase(str2)|
|String[] split(String regex, int limit)|returns a split string matching regex and limit. here limit is optional| str.split("\\s")//splits string based on whitespaces|
|int indexOf(String substring, int fromIndex)|returns the specified substring index starting with given index. here index is optional| str.indexOf("compiler",2);|
|String toLowerCase()|returns a string in lowercase.|str.toLowercase();|
|String toUpperCase()|returns a string in uppercase.|str.toUpperCase();|
|String trim()|removes beginning and trailing spaces of a given string.|str.trim();|
|boolean endsWith(String chars)|Checks whether a string ends with the specified character(s).|str.endsWith("Hel")|

## OOPS

### 1. Class

Class is the blueprint of an object and `class` keyword is required to create a class.

```java
class class_name {  
    fields;  
    methods;  
}
```

### 2. Object

Object is a basic unit in OOP, and is an instance of the class.

```java
class_name obj_name;
```
### 3. Abstraction

Data abstraction is a technique which provides only the required data to be visible or accessible to outside world. 
`abstract` keyword is used for classes and methods. 


```java

abstract class Mobiles { // abstract class
  public abstract void features();   // abstract method
  public void method-name() {
    //code
  }
}
```
### 4. Encapsulation

Encapsulation is a mechanism to protect private hidden from other users. It wraps the data and methods as a single bundle. `private` is the keyword used to declare the variables or methods as private. You can make public `set` and `get` methods to access private variables.

### 5. Polymorphism

Polymorphism gives the meaning many forms, usually it occurs when multiple classes are present and have been inherited.

```java
class Child-class extends Parent-Class {
//code
}
```
### Constructor

Constructor is a special type of method.
Every class has atleast one constructor.
Without Constructor, object from the class cannot be created, that's why constructor is mandatory in every class.
Name of the constructor should be the name of the class.
Constructor has no return type.

```java
public class AA {   //beg of class
    public void AA() {  //default constructor
    //code
   }
 }
 ```
