---
title: Java String API
description: Sequence of characters represent String. In Java programs all string literals such as "onec", are implemented as instances of java.lang.String class.
created: 2019-08-10
updated: 2019-08-10
---

## Create a String
```java
String string = "One Compiler";                 // Using literal
String string2 = new String("One Compiler");     // Using new Keyword

char[] characters = {'a', 'b', 'c', 'd'};
String string3 = new String(characters);         //Gives output as "abcd" 

byte[] characters = {65, 66, 67, 68};
String string3 = new String(characters);         //Gives output as "ABCD" 
```

## String Comparison
```java
String string = "One Compiler";                 
String string2 = new String("One Compiler");     

// Following methods returns boolean value.
string == string2;                  // (==) Compares address of the values
string.equals(string2)              // (equals) Compares the actual values
string.equalsIgnoreCase(string2)    // (equalsIgnoreCase) Compares values and also ignores case
string.contentEquals(string2)       // (contentEquals) Checks for same Sequence of characters values against the other string

//Following methods return int value
string.compareToIgnoreCase(string2)  // (compareToIgnoreCase) Returns 0 if values are equal ignoring case, Returns < 0 if the string is lexicographically less than the other string, Returns > 0 if the string is lexicographically greater than the other string
string.compareTo(string1)            // (compareTo) Returns 0 if values are equal, Returns < 0 if the string is lexicographically less than the other string, Returns > 0 if the string is lexicographically greater than the other string
```

concat(): Append two strings 
```java
String string = "Welcome to ";  
String string1 = "One Compiler"; 
string.concat(string1) // returns Welcome to One Compiler
```

contains(): Checks whether string contains given value or not and return boolean value
```java
String string = "One Compiler"; 
string.contains("One")  //returns true
```

join(): Returns a combined string with given values/array and specified delimiter in between.
```java
String.join(",", "audi", "bmw", "cadillac", "kwid")  //returns audi,bmw,cadillac,kwid
String[] array = {"Welcome", "to", "One", "Compiler"};
String.join("-",array);       //returns Welcome-to-One-Compiler
```

length(): Returns the length of the string.
```java
String string = "One Compiler"; 
string.length()   //returns 12
```

indexOf(): Returns the first occurrence of specified character in given string
```java
String string = "One Compiler";
string.indexOf("C");  //returns 4
```

lastIndexOf(): Returns the last occurrence of specified character in a given string
```java
String string = "One Compiler";
string.lastIndexOf("e");  //returns 10
```

replace(): Replaces all the occurrences of specified character/charsequence with given character/charsequence.
```java
String string = "One Compiler";
string.replace("e", "r");  //returns Onr Compilrr
```

replaceAll(): Replaces all the occurrences matching specified regex with given string.
```java
String string = "One Compiler";
string.replaceAll("\\s", "");  //returns OneCompiler
```

split(): Returns char array by splitting given string based on given regex.
```java
String string = "Welcome to One Compiler";
String[] splitArray = string.split("\\s");
for(String word : splitArray) {  
    System.out.println(word);   
}

output:
Welcome
to
One
Compiler
```

split(): Returns char array by splitting given string based on given regex and specified split limit.
```java
String string = "Welcome to One Compiler";
String[] splitArray = string.split("\\s", 2);
for(String word : splitArray) {  
    System.out.println(word);   
}

output:
Welcome
to One Compiler
```




hashCode(): Returns the hashCode of given string
```java
String string = "One Compiler";
string.hashCode();  //returns 599566681
```

isEmpty(): Returns boolean value, returns true when given string is empty else returns false
```java
String string = "";
string.isEmpty();  //returns true

String string = "one";
string.isEmpty();  //returns false

String string = null;
string.isEmpty();  //throws java.lang.NullPointerException
```



codePointAt(): Returns unicode of the character of the specified index  
```java
String string = "One Compiler"; 
string.codePointAt(1)   //returns 110
```

charAt(): Returns the character of the specified index
```java
String string = "One Compiler";
string.charAt(5) //returns o
```

codePointBefore(): Returns the unicode of the character before specified index
```java
String string = "One Compiler";
string.codePointBefore(5) //returns 67
```

codePointCount(): It accepts two parameters i.e., startIndex and endIndex and returns the number unicode values found between two specified indexes.
```java
String string = " o n e compiler";
string.codePointCount(0, 5) //returns 5
```

copyValueOf(): Returns string from the array of characters 
```java
char[] characters = {'a', 'q', 'c', 'i', 'r', 'w'};
String string = "";
string.copyValueOf(characters, 0, 3); // returns "aqc"
```
valueOf(): It converts different types of values into string

endsWith(): Returns true if string ends with given value else returns false
```java 
String string = "One Compiler";
string.endsWith("ler") //returns true
string.endsWith("sss") //returns false
```

startsWith(): Returns true if string starts with given value else returns false
```java 
String string = "One Compiler";
string.startsWith("One") //returns true
string.startsWith("sss") //returns false
```

startsWith(String prefix, int offset): Returns true if string starts with given prefix index starting with offset else returns false
```java 
String string = "One Compiler";
string.startsWith("One", 0) //returns true
string.startsWith("One", 2) //returns false
```

substring(int beginIndex): Returns characters from a string from specified index
```java 
String string = "One Compiler";
string.substring(2);  //returns e Compiler
```

substring(int beginIndex, int endIndex): Returns characters from a string between specified start and end indexes
```java 
String string = "One Compiler";
string.substring(4, 8);  //returns Comp
```

toCharArray(): Returns char array of the string.
```java 
String string = "One";
for(Character s : string.toCharArray()) {
    System.out.println(s);
}

output:
O
n
e
```

toLowerCase(): Returns given string in lower case
```java 
String string = "One Compiler";
string.toLowerCase();  //returns one compiler
```

toUpperCase(): Returns given string in upper case
```java 
String string = "One Compiler";
string.toUpperCase();  //returns ONE COMPILER
```

trim(): Returns string by removing leading and trailing spaces i.e., It removes unicode value '\u0020' from a beginning and ending of a given string 
```java 
String string = "  One Compiler";
string.trim();  //returns One Compiler
```


## Java 8 Streams of string join/append 

Collectors.joining(): Returns a concatenated string from stream
Collectors.joining(CharSequence delimiter): Returns a concatenated string separated by delimiter
Collectors.joining(CharSequence delimiter,  CharSequence prefix, CharSequence suffix ): Returns a concatinated string separated by delimiter as well as appending specified prefix and suffix

```java
Stream<String> stream = Arrays.asList("audi", "bmw", "cadillac", "dodge").stream();  
String string = stream.collect(Collectors.joining());    //Returns audibmwcadillacdodge   
string = stream.collect(Collectors.joining(","));      //audi,bmw,cadillac,dodge
string = words.collect(Collectors.joining(",", "{", "}"));    //{audi,bmw,cadillac,dodge} 
```


## Java 11 String API Additions

repeat(): Repeats the string content
```java
String string = "Ra ".repeat(2) + "Ramone";
System.out.println(string);

output:
Ra Ra Ramone
```

strip(): Returns a string with all leading and trailing whitespaces removed
```java
System.out.println(("\n\t  hi   \u2005".strip()));

output:
hi
```

isBlank(): Returns true if the string is empty or contains only whitespace. Otherwise, it returns false
```java
System.out.println(("\n\t\u2005  ".isBlank()));

output:
true
```

lines(): Returns a Stream of lines extracted from the string, separated by line terminators
```java
String multilineStr = "This is\n \n a practice\n line.";
long lineCount = multilineStr.lines().count();
System.out.println(lineCount);

output:
4
```

