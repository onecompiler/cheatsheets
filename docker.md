---
title: Docker
description: Docker Build, Ship and Run commands
created: 2018-10-22
updated: 2022-10-01
---

## Build
Building an image from Dockerfile 
```sh
docker build -t app_name:1.0 .
```
List all images
```sh
docker images
```

## Ship
Push docker image
```sh
docker push user_id/my_image
```
## Run
Run docker image
```sh
docker run -p 8001:8001 -it  app_name:1.0
```

List all running containers
```sh
docker ps
```

Kill a running container

```sh
docker kill container_name/ container_id 
```

## Container

List running containers

```
docker container ls
```

List all containers even stopped once

```
docker container ls -a
```

Start and stop a container

```
docker start container_name 
docker stop container_name
```

Create a image from a running container

```
docker container commit container_id image_name
```

Delete all stopped containers

```
docker container prune
```

Get all details related to the container

```
docker inspect container_id
```



## Prune

```sh
docker system prune     # prune all docker resources
docker system prune -f  # prune all resources with force (without prompt)
```

## Dockerfile syntax

```sh
FROM ubuntu:16.04 # from base image
RUN apt-get update # execute commands
ADD local_directory /
EXPOSE 8080

```
