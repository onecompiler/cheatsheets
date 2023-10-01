---
title: Dart Programming language
description: Dart Programming language cheatsheet contains useful code syntax with examples which is really handy while coding in flutter.
created: 2022-11-11
updated: 2022-11-11
---

## Introducing the Environment

```dart
void main() {
	print('Hello World!');
}
```

## Drawing a Shape

- Code runs in the order it's written

```dart
print('   /|');
print('  / |');
print(' /  |');
print('/___|');
```

## Variables

```dart
int age = 70;
String name = "Mike";

print("There once was a man named ${name}");
print("He was ${age} years old");

age = 25

print("He really liked the name ${name}");
print("But didn't like being ${age}");

```

## Data Types

```dart
int age = 26
double gpa = 3.5
bool isRegisteredVoter = false
String name = "Mike"

print(name)
```

## Strings

```dart
String greeting = "Hello";
//                 01234

greeting.length();
greeting[0];
greeting.toUpperCase();
greeting.indexOf("e");
greeting.contains("llo");
greeting + " World!";
```

## Numbers

```dart
import 'dart:math';

int quantity = 300;
double price = 5.99;

quantity += 5

print( 5 + 3 )
print( 10 % 3 )
min(5, 6)
sqrt(144)
```

## Getting User Input

```dart
import 'dart:io';

print("What is your name")
String name = stdin.readLineSync()
print("Hello ${name}")
```

## Building a Basic Calculator

```dart 
print("Enter your first number:");
int num1 = int.parse(stdin.readLineSync());
print("Enter your first number:");
int num2 = int.parse(stdin.readLineSync());
print(num1 + num2);
```

## Building a madlibs game

```dart
print("Enter a color:");
String color = stdin.readLineSync();
print("Enter a plural noun:");
String pluralNoun = stdin.readLineSync();
print("Enter a celebrity:");
String celebrity = stdin.readLineSync();

print("Roses are ${color}");
print("${pluralNoun} are blue");
print("I love ${celebrity}");
```

## Lists

```dart
List<int> favNumbers = [4, 8, 15, 16, 23, 42];
//                      0, 1, 2,  3,  4,  5

favNumbers.length;
favNumbers[1];
favNumbers[2] = 5;
favNumbers.add(5);
favNumbers.indexOf(8);
favNumbers.contains(8);
favNumbers.remove(42);

print(favNumbers);
```

## Functions

```dart
void drawTriangle(){
  print('   /|');
  print('  / |');
  print(' /  |');
  print('/___|');
}

drawTriangle();
drawTriangle();
drawTriangle();
```

## Parameters & Arguments

```dart
void sayHi(String name, int age){
  print("Hello ${name}, you are ${age}");
}

sayHi("Mike", 26);
sayHi("Joe", 55);
```

## Return Statements

```dart
int addNumbers(int num1, int num2){
  return num1 + num2;
}

int answer = addNumbers(6, 7);
print(answer);
```

## Building a prompting function

```dart
String prompt(String promptText){
  print("${promptText}:");
  String answer = stdin.readLineSync();
  return answer;
}
```

## If Statements

- Read the prompt text from the website

I wake up
If I'm hungry 
  I eat breakfast 

I leave my house
if it's cloudy 
  I bring an umbrella 
otherwise 
  I bring sunglasses 

Im at a restaurant 
if I want meat 
  I order a steak 
otherwise if I want pasta 
  I order spaghetti & meatballs 
otherwise 
  I order a salad. 
  
```dart
bool isSmart = true;

if(isSmart){
  print("You are smart!")
} else {
  print("You need to study")
}

String name = "Mike";

if(name.contains("M")){
  print("you have an M in your name");
}
```

## &&/|| operators, elseif

```dart
bool isSmart = true;
bool isStudent = true;

if(isSmart && isStudent){
  print("You are a smart student!");
} else if (isSmart && !isStudent){
  print("You are a smart non-student!");
} else {
  print("You need to study");
}
```

## Building a better calculator

```dart
double promptNumber(){
  print("Enter a number:");
  return double.parse(stdin.readLineSync());
}

double num1 = promptNumber();

print("Operator (+,-,*,/):");
String operator = stdin.readLineSync();

double num2 = promptNumber();

if(operator == '+') print(num1 + num2);
else if(operator == '-') print(num1 - num2);
else if(operator == '*') print(num1 * num2);
else if(operator == '/') print(num1 / num2);
else print("invalid operator!");
```

## Switch Statements

```dart
switch(operator){
  case '+':
    print(num1 + num2);
    break;
  case '-':
    print(num1 - num2);
    break;
  case '/':
    print(num1 / num2);
    break;
  case '*':
    print(num1 * num2);
    break;
  default:
    print("invalid operator");
}
```

## While Loops

```dart
int i = 0;

while(i < 5){
  print(i);
  i++;
}
```

## Building a guessing game

```dart
String promptGuess(){
  print("Enter a guess:");
  return stdin.readLineSync();
}

String answer = 'michael scott';
String guess = '';

while(guess != answer){
  guess = promptGuess();
}

print("You Win!");
```

## For Loops

- First talk about how this is a common occurance

```dart
for(int i = 0; i < 10; i++){
  print(i);
}

List<String> friends = ["Jim", "Kevin", "Stanley"];

for(String friend in friends){
  print("Hello ${friend}");
}
```

## Drawing multiple triangles

```dart
String drawTriangle(int quantity){
  for(int i = 0; i < quantity; i++){
    print('   /|');
    print('  / |');
    print(' /  |');
    print('/___|');
  }
}

drawTriangle(5);
```

## Comments

```dart
// single line comment

/*
multi
line
comment
*/
```

## Classes & Objects

```dart
class Book {
	String title;
	String author;
	int noPages;
}

Book hp = Book();
hp.title = "Harry Potter";
hp.author = "JK Rowling";
hp.noPages = 500;

print(hp.author);
```

## Constructors

```dart
class Book {

	Book(String aTitle, String aAuthor, int aNoPages){
		this.title = aTitle;
		this.author = aAuthor;
		this.noPages = aNoPages;
	}

	String title;
	String author;
	int noPages;
}

Book hp = Book("Harry Potter", "JK Rowling", 500);

print(hp.author);
```

## Building a quiz

```dart
List<MathQuestion> questions = [
    MathQuestion('1 + 1', '2'),
    MathQuestion('2 - 7', '-5'),
  ];

  int score = 0;

  for(MathQuestion question in questions){
    String answer = prompt(question.prompt);
    if(answer == question.answer){
      print("Correct!");
      score++;
    } else {
      print("Incorrect!");
    }
  }

  print("You got ${score}/${questions.length} correct");
```


## Class Functions

```dart
class Student {
    String name;
    double gpa;
    Student(String name, double gpa){
      this.name = name;
      this.gpa = gpa;
    }

    bool hasHonors(){
      return this.gpa >= 3.5;
    }
  }
```