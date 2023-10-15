---
title: Linux Fundamentals Part 3
author: CYB3RM3
name: CYB3RM3 | Linux Fundamentals Part 3
date: 2023-10-15 16:48:15 +0100
categories: [TryHackMe, Linux Fundamentals]
tags: [Linux, Pre Security]
---

Power-up your Linux skills and get hands-on with some common utilities that you are likely to use day-to-day!

THM Room : [https://tryhackme.com/room/linuxfundamentalspart3](https://tryhackme.com/room/linuxfundamentalspart3)



## TASK 1 Introduction
###  Let's proceed! 
No Answer.

## TASK 2 Deploy Your Linux Machine
### I've logged into the Linux Fundamentals Part 3 machine using SSH and have deployed the AttackBox successfully! 
No Answer.

## TASK 3 Terminal Text Editors
### Create a file using Nano
No Answer.

### Edit "task3" located in "tryhackme"'s home directory using Nano. What is the flag?
Answer : THM{TEXT_EDITORS}

## TASK 4 General/Useful Utilities
### Ensure you are connected to the deployed instance (MACHINE_IP)
No Answer.

### Now, use Python 3's "HTTPServer" module to start a web server in the home directory of the "tryhackme" user on the deployed instance.
No Answer.

### Download the file http://MACHINE_IP:8000/.flag.txt onto the TryHackMe AttackBox. What are the contents?
Answer : THM{WGET_WEBSERVER}
### Create and download files to further apply your learning -- see how you can read the documentation on Python3's "HTTPServer" module. Use Ctrl + C to stop the Python3 HTTPServer module once you are finished.
No Answer.

## TASK 5 Processes 101

### Read me!
No Answer.

### If we were to launch a process where the previous ID was "300", what would the ID of this new process be?
Answer : 301

### If we wanted to cleanly kill a process, what signal would we send it?
Answer : SIGTERM

### Locate the process that is running on the deployed instance (MACHINE_IP). What flag is given?
Answer : THM{PROCESSES}

### What command would we use to stop the service "myservice"?
Answer : systemctl stop myservice

### What command would we use to start the same service on the boot-up of the system?
Answer : systemctl enable myservice

### What command would we use to bring a previously backgrounded process back to the foreground?
Answer : fg

## TASK 6 Maintaining Your System: Automation
### Ensure you are connected to the deployed instance and look at the running crontabs.
No Answer.

### When will the crontab on the deployed instance (MACHINE_IP) run?
Answer : @reboot

## TASK 7 Maintaining Your System: Package Management
### Since TryHackMe instances do not have an internet connection...this task only requires you to read through the material. 
No Answer.

## TASK 8 Maintaining Your System: Logs
### Look for the apache2 logs on the deployable Linux machine
No Answer.

### What is the IP address of the user who visited the site?
Answer : 10.9.232.111

### What file did they access?
Answer : catsanddogs.jpg

## TASK 9 Conclusions & Summaries
### Terminate the machine deployed in this room from task 2. 
No Answer.

### Continue your learning in other Linux-dedicated rooms
No Answer.