---
title: Dockerfile Syntax
description: Dockerfile Syntax
created: 2019-09-15
updated: 2019-09-15
---

## FROM

Syntax
```sh
FROM <image>:<tag>
```
Example
```sh
FROM ubuntu:16.04
```

## ENV

Syntax
```sh
ENV <key> <value>
```

Example
```sh
ENV JAVA_HOME       /usr/lib/jvm/java-8-oracle
```

## RUN

Syntax
```sh
RUN <command>
```

Example
```sh
RUN apt-get update
```

## EXPOSE

Syntax
```sh
EXPOSE <port> [<port> ...]
```

Example
```sh
EXPOSE 8080 9200
```
## COPY

Syntax
```sh
COPY <src> [<src> ...] <dest>
```

Example
```sh
COPY file1.txt /opt/app/file1.txt
```

## ADD

Syntax
```sh
ADD <src> [<src> ...] <dest>
```

Example
```sh
ADD file1.txt /opt/app/file1.txt
ADD jdk-8u120-linux-x64.tar.gz /usr/local/  # ADD unzips for you
ADD http://example.com/app.tar.xz /opt/app/ # ADD also support urls
```

## VOLUME
Syntax
```sh
VOLUME </path/from/host> </path/from/docker-container>
```

Example
```sh
VOLUME /data /mongodb/db/data
```

## WORKDIR
Sets working directory where other commands run
Syntax 
```sh
WORKDIR <path>
```

Example
```sh
WORKDIR /opt/app
```

## CMD
Syntax 
```sh
CMD <command> [<command> ...]
```

Example
```sh
CMD ['node' 'index.js']
```
