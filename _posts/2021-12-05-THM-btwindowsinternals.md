---
title: Core Windows Processes  
author: CYB3RM3
name: CYB3RM3 | Core Windows Processes   
date: 2021-12-05 15:02:20 +0100
categories: [TryHackMe, Windows]
tags: [Sysinternals, Windows]
---

Explore the core processes within a Windows operating system and understand what normal behaviour is. This foundational knowledge will help you identify malicious processes running on an endpoint!

THM Room [https://tryhackme.com/room/btwindowsinternals](https://tryhackme.com/room/btwindowsinternals)


## TASK 1 : Introduction
### I've read the intro and deployed the attached virtual machine. 
No Answer

## TASK 2 : TASK Manager 
### On to the next task... 
No Answer

## TASK 3 : System
### What PID should System always be? 
Answer : 4

## TASK 4 : System > smss.exe 
### What other two processes does smss.exe start in Session 1? (answer format: process1, process2) 
Answer : csrss.exe, winlogon.exe

## TASK 5 : csrss.exe
### What was the process which had PID 384 and PID 488? 
Answer : smss.exe

## TASK 6 : wininit.exe 
### Which process you might not see running if Credential Guard is not enabled? 
Answer : lsaiso.exe

## TASK 7 : wininit.exe > services.exe
### How many instances of services.exe should be running on a Windows system? 
Answer : 1

## TASK 8 : wininit.exe > services.exe > svchost.exe 
### What single letter parameter should always be visible in the Command line or Binary path? 
Answer : k

## TASK 9 : lsass.exe
### What is the parent process for LSASS?
Answer : wininit.exe

## TASK 10 : winlogon.exe 
### What is the non-existent parent process for winlogon.exe? 
Answer : smss.exe 

## TASK 11 : explorer.exe  
### What is the non-existent process for explorer.exe? 
Answer : userinit.exe

## TASK 12 : Conclusion
### Thanks for stopping by. 
No Answer