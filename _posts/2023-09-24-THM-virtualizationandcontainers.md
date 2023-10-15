---
title: Virtualization and Containers
author: CYB3RM3
name: CYB3RM3 | Virtualization and Containers
date: 2023-09-24 17:43:22 +0100
categories: [TryHackMe, Security Engineer]
tags: [Virtualization, Container, Intro]
---

Introduction to common virtualization technologies and applications.

THM Room : [https://tryhackme.com/room/virtualizationandcontainers](https://tryhackme.com/room/virtualizationandcontainers)


## TASK 1 Introduction
### Read the above and continue to the next task. 
No Answer.

## TASK 2 What is Virtualization
### Is scalability a primary benefit of virtualization? (Y/N)

>"But why is virtualization needed? For most organizations and individuals, virtualization comes from a need of the following:"

    1. Decrease expenses: Physical servers can be expensive, and virtualization can decrease the number of servers or other hardware, or even completely remove physical hardware from a company's infrastructure.
    2. Scale: Without properly implemented DevOps, it may be hard for a company to scale resources as server usage increases. Virtualization makes this process easier and can delegate a server's resources to virtual machines as needed based on usage.
    3. Efficiency: Like scaling, virtualization can also make it easier to decrease the resources allocated to a virtual machine if there is reduced usage.

Answer : Y

### What is the operating system of a virtual machine often referred to as?

>"The operating system installed in a virtual machine is known as a guest OS, as opposed to the host OS on which the virtualization engine is running."

Answer : guest OS

## TASK 3 Hypervisors
### What type of hypervisor is VirtualBox considered?

>"Examples of type 2 hypervisors include VMware Workstation, VMware Fusion, VirtualBox, Parallels, and QEMU."

Answer : type 2

### What are type 1 hypervisors also known as?

>"Type 1 hypervisors, also known as bare metal hypervisors, create an abstraction layer directly between hardware and virtual machines without a common operating system between them"

Answer : bare metal hypervisors

## TASK 4 Containers
### Are containers completely abstracted from the host operating system? (Y/N) 

>"Containers have a lot in common with virtual machines, but instead of being completely abstracted from the host operating system, containers share some properties with the host operating system. Containers have their own filesystem, a portion of computing resources (CPU, RAM), a process space, and more. "

Answer : N

## TASK 5 Docker
### What flag is obtained at 10.10.131.203:5000 after running the container?


```console
Could not chdir to home directory /home/thmuser: No such file or directory
$ docker run -p 5000:5000 -d cryillic/thm_example_app
792debddcc8f86fe408c21520dc0e5b7c55c16525770ca7fb255f32490e8633f
$ curl 10.10.131.203:5000
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Docker</title>
</head>
<body>
    <center><h1>THM{this_is_running_in_docker}</h1></center>
</body>
</html>$ 
```
{: .nolineno }

## TASK 6 Kubernetes
### Before proceeding, ensure all clusters are started by running minikube start.
No Answer.

### How many pods are running on the provided cluster?

```console 
$ kubectl get pods
NAME                              READY   STATUS    RESTARTS        AGE
hello-tryhackme-f79f667fd-lh87b   1/1     Running   1 (8m35s ago)   135d
```
{: .nolineno }

Answer : 1

### How many system pods are running on the provided cluster?

```console 
$ kubectl get pods -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS        AGE
default       hello-tryhackme-f79f667fd-lh87b    1/1     Running   1 (9m49s ago)   135d
kube-system   coredns-787d4945fb-wqxqr           1/1     Running   1 (9m48s ago)   135d
kube-system   etcd-minikube                      1/1     Running   1 (9m49s ago)   135d
kube-system   kube-apiserver-minikube            1/1     Running   1 (9m49s ago)   135d
kube-system   kube-controller-manager-minikube   1/1     Running   1 (9m49s ago)   135d
kube-system   kube-proxy-sqwx6                   1/1     Running   1 (9m48s ago)   135d
kube-system   kube-scheduler-minikube            1/1     Running   1 (9m48s ago)   135d
kube-system   storage-provisioner                1/1     Running   3 (8m5s ago)    135d
```
{: .nolineno }

Answer : 7

### What is the pod name on the provided cluster?
Answer : hello-tryhackme-f79f667fd-lh87b

### What is the deployment name on the provided cluster?

```console 
$ kubectl get deployments
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
hello-tryhackme   1/1     1            1           135d
```
{: .nolineno }

Answer : hello-tryhackme

### What port is exposed by the service in question 5?

```console 
$ kubectl get services
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
hello-tryhackme   NodePort    10.109.213.246   <none>        8080:31449/TCP   135d
kubernetes        ClusterIP   10.96.0.1        <none>        443/TCP          135d
```
{: .nolineno }

Answer : 8080

### How many replica sets are deployed on the provided cluster?

```console 
$ kubectl get rs
NAME                        DESIRED   CURRENT   READY   AGE
hello-tryhackme-f79f667fd   1         1         1       135d
```
{: .nolineno }

Answer : 1

### What is the replica set name on the provided cluster?
Answer : hello-tryhackme-f79f667fd

### What command would be used to delete the deployment from question 5?

Answer : kubectl delete deployment hello-tryhackme


## TASK 7 Conclusion
### Read the above and continue learning! 
No Answer.
