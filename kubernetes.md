---
Title: Kubernetes
Description: Functionalities of Kubernetes
created: 2022-10-03
updated: 2022-10-03
---

Kubernetes also known as K8s is an open source system for automating deployment,scaling and management of containerized applications. K8s makes it easier to manage applications and is a very essectial concept that every Software Developer needs to know.

## Common Kubectl Commands

```sh
kubectl cluster-info 
```sh
Display endpoint information about the master and services in the cluster.

```sh
kubectl version 
```sh
Displays the Kubernetes version running on the client and server systems

```sh
kubectl api-resources 
```sh
List the API resources that are available

```sh
kubectl config current-context 
```sh
Displays the current context available on the data storage

```sh
kubectl config view 
```sh
Used to get the configuration of the cluster

## Creating,Updating and Deleting a Resource

```sh
kubectl create namespace [namespace-name] 
```sh
To create a resource such as a service, deployment, job, or namespace, we use the kubectl create command

```sh
kubectl apply -f [service-name].yaml 
```sh
To apply or update a resource we use the kubectl apply command

```sh
kubectl delete -f pod.yaml
```sh
To remove resources from a file, we use the kubectl delete command











