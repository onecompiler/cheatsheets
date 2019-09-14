---
title: Gson (Java Library)
description: Gson is a Java Library which is used to convert Java Objects to JSON strings and back. Gson library provides toJson() and fromJson() methods using which users can serialize /deserialize Java objects to and back from JSON Strings
created: 2019-06-25
updated: 2019-06-25
color: #0984e3
---

Gson is a Java Library which is used to convert Java Objects to JSON strings and back. Gson library provides `toJson()` and `fromJson()` methods using which users can serialize /deserialize Java objects to and back from JSON Strings.

## Installation
#### Maven
```xml
<!-- https://mvnrepository.com/artifact/com.google.code.gson/gson -->
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.8.5</version>
</dependency>
```
#### Gradle
```groovy
// https://mvnrepository.com/artifact/com.google.code.gson/gson
compile group: 'com.google.code.gson', name: 'gson', version: '2.8.5'
```


## Java Object to JSON String
```java
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import com.google.gson.Gson;

public class GsonObjectToJSONExample {
    public static void main(String[] args) {

        Gson gson = new Gson();

        Map<String, Object> javaObject = new HashMap<>();

        javaObject.put("aNumber", 1);
        javaObject.put("aString", "foo");
        javaObject.put("aBoolean", true);
        javaObject.put("aList", Arrays.asList("red", "green", "blue"));

        String jsonString = gson.toJson(javaObject);

        System.out.println(jsonString);

    }
}
```
### Output: 
```json
{"aNumber":1,"aBoolean":true,"aString":"foo","aList":["red","green","blue"]}
```

## JSON String to Java Object
```java
import java.util.Map;

import com.google.gson.Gson;

public class GsonJsonToObjectExample {
    public static void main(String[] args) {

        Gson gson = new Gson();
        String jsonString = "{\"aNumber\":1,\"aBoolean\":true,\"aString\":\"foo\",\"aList\":[\"red\",\"green\",\"blue\"]}";

        Map javaObject = gson.fromJson(jsonString, Map.class);

        System.out.println("aList: " + javaObject.get("aList"));
        System.out.println("aNumber: " + javaObject.get("aNumber"));

    }
}
```
### Output: 
```sh
aList: [red, green, blue]
aNumber: 1.0
```