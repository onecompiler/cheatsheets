---
title: Docker
description: Useful Docker commands and Terms
created: 2018-10-22
updated: 2022-10-02
---

## Important Terms
|Term|Meaning|
|---|---|
|Layer|Read-only files to provision the system|
|Image|Read-only layer that is the base of an image|
|Container|A runnable instance of the image|
|Registry/hub|A central place where images reside|
|Docker machine|A VM to run Docker containers|
|Docker Compose|A VM to run multiple containers as a system|

## Build
To build an image from the Docker file and tag it 
```sh
docker build -t app_name :1.0 .
```
To list all the images that are locally stored
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

## Prune
```sh
docker system prune     # prune all docker resources
docker system prune -f     # prune all resources with force (without prompt)
docker image prune      # to clean an unused/dangling image
docker image prune -a      # to remove an image that is not used in a container
docker swarm leave      # to leave a swarm
docker stack rm stack_name # to remove a swarm
```
Remove a swarm
```sh
docker stack rm stack_name
```
Leave a swarm
```sh
docker swarm leave
```
## Dockerfile syntax

```sh
FROM ubuntu:16.04   # from base image
RUN apt-get update    # execute commands
ADD local_directory /
EXPOSE 8080

```

## Services
```sh
docker service ls # to list all services running in a swarm
docker stack services stack_name # to see all running services
docker service logs stack_name service_names # to see all service logs
docker service scale stack_name_service_name= replicas #to scale a service across qualified nodes
```
