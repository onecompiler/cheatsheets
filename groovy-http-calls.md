---
title: Groovy Http calls
description: Example GET, POST Http calls in Groovy with out using any special library
created: 2019-08-14
updated: 2019-08-14
color: #286b86
---

Example GET, POST Http calls in Groovy with out using any special library

## GET Calls

```java
def get = new URL("https://httpbin.org/get").openConnection(); 

def postResponseCode = get.getResponseCode();
def postResponseData = get.getInputStream().getText();

println "Response Code: ${postResponseCode}"
println "Response Data: ${postResponseData}"
```
Fork code: https://onecompiler.com/groovy/3ux954nea

## POST Calls

```java
def post = new URL("https://httpbin.org/post").openConnection(); 
def body = 
'''
{
  "foo" : "bar",
  "age" : 20
}
'''

post.setRequestMethod("POST")
post.setDoOutput(true)
post.setRequestProperty("Content-Type", "application/json")
post.getOutputStream().write(body.getBytes("UTF-8"));

def postResponseCode = post.getResponseCode();
def postResponseData = post.getInputStream().getText();

println "Response Code: ${postResponseCode}"
println "Response Data: ${postResponseData}"
```
Fork code: https://onecompiler.com/groovy/3ux94sz4p