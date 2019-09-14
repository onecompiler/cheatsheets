---
title: OkHttp (Java Library)
description: OkHttp is a Http client for Java based applications. It supports GZIP compression and its one of the popular http client for Android applications.
created: 2019-06-25
updated: 2019-06-25
color: #0984e3
---


OkHttp is a Http client for Java based applications. It supports GZIP compression and its one of the popular http client for Android applications.

## Installation
#### Maven
```xml
<!-- https://mvnrepository.com/artifact/com.squareup.okhttp3/okhttp -->
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
    <version>3.14.2</version>
</dependency>
```
#### Gradle
```groovy
// https://mvnrepository.com/artifact/com.squareup.okhttp3/okhttp
compile group: 'com.squareup.okhttp3', name: 'okhttp', version: '3.14.2'
```

## GET example

```java
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class OkHttpGetExample {
    public static void main(String[] args) {

        OkHttpClient client = new OkHttpClient();

        try {
            Request request = new Request.Builder().url("https://httpbin.org/get").build();
            Response response = client.newCall(request).execute();
            String res = response.body().string();
            System.out.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
```

## POST Example

```java
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class OkHttpPostExample {
    
    public static final MediaType JSON = MediaType.get("application/json; charset=utf-8");
    
    public static void main(String[] args) {
        
        
        OkHttpClient client = new OkHttpClient();

        try {
            String body = "{\n" + 
                    "    \"foo\" : \"bar\"\n" + 
                    "}";
            Request request = new Request.Builder().url("https://httpbin.org/post").post(RequestBody.create(JSON, body)).build();
            Response response = client.newCall(request).execute();
            String res = response.body().string();
            System.out.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}

```


