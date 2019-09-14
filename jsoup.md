---
title: Jsoup (Java Library)
description: Jsoup is a Java library used for data extcration and manipulation using DOM, CSS,and jquery etc.
created: 2019-08-05
updated: 2019-08-05
color: #0984e3
---

Jsoup is a Java library used for data extcration and manipulation using DOM, CSS,and jquery etc.

## Installation
#### Maven
```xml
<!-- https://mvnrepository.com/artifact/org.jsoup/jsoup -->
<dependency>
    <groupId>org.jsoup</groupId>
    <artifactId>jsoup</artifactId>
    <version>1.12.1</version>
</dependency>
```
#### Gradle
```groovy
// https://mvnrepository.com/artifact/org.jsoup/jsoup
compile group: 'org.jsoup', name: 'jsoup', version: '1.12.1'
```

## Parsing From String example

```java
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.File;
import java.io.IOException;
import java.net.URL;

public class JsoupParse {

    public static void main(String args[]) throws IOException {
        String html = "<html><head><title>One Compiler</title></head>"
            + "<body><p>Welcome to one compiler jsoup cheatsheat.</p></body></html>";
        Document stringDoc = Jsoup.parse(html);
        //Update file path before execution
        Document fileDocument =  Jsoup.parse(new File("Path to your html file"), "UTF-8"); //throws IOException
    }
}
```

## Parsing Data from web url example

1. Jsoup.connect(String url) with get() method creates a connection and gets data, any error occurs while getting data IOException is thrown which should be handled.

```java
Document document = Jsoup.connect("http://onecompiler.com/posts").get();
```

2. Also we can build connections by using certain specifications as shown below:

```java
Document document = Jsoup.connect("http://onecompiler.com/posts").userAgent("Mozilla")
            .cookie("auth", "axvtu23d").timeout(3000).get();
```

## Parsing Html body fragment example

```java
String html = "<p>Welcome to one compiler jsoup cheatsheat.</p>";
Document stringDoc = Jsoup.parseBodyFragment(html);
```

## DOM methods to find elements:

```java
Element element = document.getElementById("__next");
Elements elements = document.getElementsByClass("homepage--section");
Elements element = document.getElementsByAttribute("src");
Element links = document.getElementsByTag("a");
```

## CSS Selectors to find elements:

Find elements using id ex: #__next
```java
Elements elements = document.select("#__next");
```

Find elements using class ex: .homepage--section
```java
Elements elements = document.select(".homepage--section");
```
Find elements using tagname ex: a
```java
Elements elements = document.select("a");
```

Find elements using named attribute ex: `[href]`
```java
Elements elements = document.select("[href]");
```

Find elements using named attribute and its value `[attr=val]` ex: `a[class=homepage--section]`
```java
Elements elements = document.select("a[class=homepage--section]");
```

Find elements using named attribute and its value `[attr=val]` ex: `a[class=homepage--section]`
```java
Elements elements = document.select("a[class=homepage--section]");
```

Find elements by using named attribute and its value with prefix `[attr^=prefixvalue]` ex: `a[class^=home]`
```java
Elements elements = document.select("a[class^=home]");
```

Find elements by using named attribute and its value with suffix `[attr$=suffixvalue]` ex: `img[alt$=image]`
```java
Elements elements = document.select("img[alt$=image]");
```

Find elements using named attribute which contains given value `[attr*=value]` ex: `img[alt*=image]`
```java
Elements elements = document.select("img[alt*=image]");
```

Find elements using named attribute marches to given regex `[attr~=regex]` ex: `img[src~=.(png|jpeg)]`
```java
Elements elements = document.select("img[src~=.(png|jpeg)]");
```

Find elements that match any of the selectors mentioned with comma separated. ex: `div, .clasname, a[href]`
```java
Elements elements = document.select(".homepage ,a[href], img[src~=.(png|jpeg)]");
```

Find elements that contain given text and search is case insensitive. ex: `div:contains(compiler)`
```java
Elements elements = document.select("div:contains(compiler)");
```

Find elements that matches given regular expression. ex: `div:matches(compiler)`
```java
Elements elements = document.select("div:matches((?i)compiler)");
```

Find elements that contains given text and search is case insensitive. ex: `div:containsOwn(compiler)`
```java
Elements elements = document.select("div:containsOwn(compiler)");
```

Find elements that matches given regular expression. ex: `div:matchesOwn((?i)compiler)`
```java
Elements elements = document.select("div:matchesOwn((?i)compiler)");
```

Find elements by that matches given regular expression. ex: `div:containsOwn(compiler)`
```java
Elements elements = document.select("div:matchesOwn((?i)compiler)");
```

## Modify Html text content of Elements:

1. We can modify/add text content to existing html using text setter .text(String text), .prepend(String addPrefix), .append(String addSuffix) methods of Element:
```java
Element element = document.select(".__next");
element.text("One Compiler"); 
element.prepend("Welcome to ");
element.append("Platform.");
```

## Add Attributes to Elements:

1. We can set a attribute to multiple Elements.
```java
document.select("a[href]").attr("alt", "logo name");
```
2. We can set a attribute Element like:
```java
doc.select("div.jss15").attr("title", "one compiler");
```

## Set Html of an Element:

1. We can modify/add html content to existing html using html setter .html(String html), .prepend(String addPrefix), .append(String addSuffix) methods of Element:
```java
Element element = doc.select("div.homepage--section").first();
element.html("<p><b>One Compiler</b></p>");
element.prepend("<p><b>Welcome to </b></p>");
element.append("<p><b>Platform.</b></p>");
```