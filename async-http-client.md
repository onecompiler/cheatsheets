---
title: Async Http Client (Java Library)
description: Async Http Client is a high performant Http and WebSocket client library for Java. Async Http Client built on top of Netty and it provides asyc APIs for executing http requests.
created: 2019-06-25
updated: 2019-06-25
color: #0984e3
---


Async Http Client is a high performant Http and WebSocket client library for Java. Async Http Client built on top of Netty and it provides asyc APIs for executing http requests.

## Installation
#### Maven
```xml
<!-- https://mvnrepository.com/artifact/org.asynchttpclient/async-http-client -->
<dependency>
    <groupId>org.asynchttpclient</groupId>
    <artifactId>async-http-client</artifactId>
    <version>2.10.0</version>
</dependency>
```
#### Gradle
```groovy
// https://mvnrepository.com/artifact/org.asynchttpclient/async-http-client
compile group: 'org.asynchttpclient', name: 'async-http-client', version: '2.10.0'
```

## GET example

```java
import static org.asynchttpclient.Dsl.asyncHttpClient;

import org.asynchttpclient.AsyncHttpClient;
import org.asynchttpclient.ListenableFuture;
import org.asynchttpclient.Response;

public class AsyncHttpGetExample {
    public static void main(String[] args) {

        AsyncHttpClient asyncHttpClient = asyncHttpClient();

        try {
            ListenableFuture<Response> responseFuture = asyncHttpClient.prepareGet("https://httpbin.org/get").execute();
            Response res = responseFuture.get(); // or handle asynchronously
            System.out.println(res.getResponseBody());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                asyncHttpClient.close();
            } catch (Exception closingException) {
                // Ignore
            }
        }

    }
}
```

## POST Example

```java
import static org.asynchttpclient.Dsl.asyncHttpClient;
import static org.asynchttpclient.Dsl.post;

import java.util.concurrent.Future;

import org.asynchttpclient.AsyncHttpClient;
import org.asynchttpclient.Request;
import org.asynchttpclient.Response;

public class AsyncHttpPostExample {
    public static void main(String[] args) {

        AsyncHttpClient asyncHttpClient = asyncHttpClient();
        try {
            String body = "{\n" + 
                    "    \"foo\" : \"bar\"\n" + 
                    "}";
            Request request = post("https://httpbin.org/post").setBody(body).build();
            Future<Response> responseFuture = asyncHttpClient.executeRequest(request);
            Response res = responseFuture.get(); // or handle asynchronously
            System.out.println(res.getResponseBody());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                asyncHttpClient.close();
            } catch (Exception closingException) {
                // Ignore
            }
        }

    }
}

```


