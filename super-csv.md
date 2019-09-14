---
title: super-csv (Java Library)
description: Super CSV is a fast, programmer friendly CSV parsing library for Java. Using super-csv we can both read and write CSV files in Java. It is one of the popular CSV parsing librrary for java with downloads more than 19000+ times/month
created: 2019-06-25
updated: 2019-06-25
color: #60a3bc
---

Super CSV is a fast, programmer friendly CSV parsing library for Java. Using super-csv we can both read and write CSV files in Java. It is one of the popular CSV parsing librrary for java with downloads more than 19000+ times/month

## Installation
#### Maven
```xml
<!-- https://mvnrepository.com/artifact/net.sf.supercsv/super-csv -->
<dependency>
    <groupId>net.sf.supercsv</groupId>
    <artifactId>super-csv</artifactId>
    <version>2.4.0</version>
</dependency>
```
#### Gradle
```groovy
// https://mvnrepository.com/artifact/net.sf.supercsv/super-csv
compile group: 'net.sf.supercsv', name: 'super-csv', version: '2.4.0'
```

## Parsing a CSV file to pojo

#### CSV File content

```csv
id,name,age,email,married,joiningDate
1,foo,20,foo@gmail.com,Y,2019-01-31
2,bar,23,bar@gmail.com,Y,2019-02-10
3,var,22,var@gmail.com,N,2019-05-01
```

#### Pojo definition

```java
package com.example.supercsv;

import java.util.Date;

public class User {

    long id;
    String name;
    int age;
    String email;
    boolean married;
    Date joiningDate;

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public boolean isMarried() {
        return married;
    }

    public void setMarried(boolean married) {
        this.married = married;
    }

    public Date getJoiningDate() {
        return joiningDate;
    }

    public void setJoiningDate(Date joiningDate) {
        this.joiningDate = joiningDate;
    }

    @Override
    public String toString() {
        return "User [id=" + id + ", name=" + name + ", age=" + age + ", email=" + email + ", married=" + married
                + ", joiningDate=" + joiningDate + "]";
    }
    
}

```

#### Parsing Code

```java
package com.example.supercsv;

import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

import org.supercsv.cellprocessor.Optional;
import org.supercsv.cellprocessor.ParseBool;
import org.supercsv.cellprocessor.ParseDate;
import org.supercsv.cellprocessor.ParseInt;
import org.supercsv.cellprocessor.ParseLong;
import org.supercsv.cellprocessor.constraint.NotNull;
import org.supercsv.cellprocessor.ift.CellProcessor;
import org.supercsv.io.CsvBeanReader;
import org.supercsv.io.ICsvBeanReader;
import org.supercsv.prefs.CsvPreference;

public class ParseCsvToPojo {

    private static CellProcessor[] getProcessors() {

        final CellProcessor[] processors = new CellProcessor[] { new NotNull(new ParseLong()), // id
                new NotNull(), // name
                new NotNull(new ParseInt()), // age
                new NotNull(), // email
                new Optional(new ParseBool("Y", "N")), // married
                new ParseDate("yyyy-MM-dd") // joiningDate
        };

        return processors;
    }

    public static void main(String[] args) throws Exception {
        final String CSV_FILENAME = "/experimental/users.csv";

        ICsvBeanReader beanReader = null;
        try {
            beanReader = new CsvBeanReader(new FileReader(CSV_FILENAME), CsvPreference.STANDARD_PREFERENCE);

            final String[] header = beanReader.getHeader(true);
            final CellProcessor[] processors = getProcessors();

            List<User> users = new ArrayList<>();
            User user;
            while ((user = beanReader.read(User.class, header, processors)) != null) {
                users.add(user);
            }
            System.out.println("CSV Parsed successfully. Following are the results");
            System.out.println(users); 

        } finally {
            if (beanReader != null) {
                beanReader.close();
            }
        }

    }
}

```

#### Output

```java
CSV Parsed successfully. Following are the results
[User [id=1, name=foo, age=20, email=foo@gmail.com, married=true, joiningDate=Thu Jan 31 00:00:00 IST 2019], User [id=2, name=bar, age=23, email=bar@gmail.com, married=true, joiningDate=Sun Feb 10 00:00:00 IST 2019], User [id=3, name=var, age=22, email=var@gmail.com, married=false, joiningDate=Wed May 01 00:00:00 IST 2019]]
```