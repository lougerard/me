---
title: Metasploit - Introduction
author: CYB3RM3
name: CYB3RM3 | Metasploit - Introduction
date: 2021-09-25 21:37:52 +0100
categories: [TryHackMe, Web]
tags: [Web, metasploit, msf]
---

An introduction to the main components of the Metasploit Framework. 
THM Room [https://tryhackme.com/room/metasploitintro](https://tryhackme.com/room/metasploitintro)


## TASK 1 : Introduction to Metasploit
### No answer needed
No Answer

## TASK 2 : Main Components of Metasploit
### hat is the name of the code taking advantage of a flaw on the target system ?
Answer : Exploit

### What is the name of the code that runs on the target system to achieve the attacker's goal ?
Answer : Payload

### What are self-contained payloads called ?
Answer : Singles

### Is "windows/x64/pingback_reverse_tcp" among singles or staged payload ?
Answer : Singles

## TASK 3 : Msfconsole
### How would you search for a module related to Apache ?
Anwser : search Apache

### Who provided the auxiliary/scanner/ssh/ssh_login module ?

```console
msf5 > info auxiliary/scanner/ssh/ssh_login 

       Name: SSH Login Check Scanner
     Module: auxiliary/scanner/ssh/ssh_login
    License: Metasploit Framework License (BSD)
       Rank: Normal

Provided by:
  todb <todb@metasploit.com>

[...]
```
{: .nolineno }

Anwser : todb

## TASK 4 : Working with modules 
### How would you set the LPORT value to 6666 ?
Answer : set LPORT 6666

### How would you set the global value for RHOSTS  to 10.10.19.23 ?
Answer : setg RHOSTS 10.10.19.23

### What command would you use to clear a set payload?
Answer : unset PAYLOAD

### What command do you use to proceed with the exploitation phase?
Answer : exploit

## TASK 5 : Summary    
### No answer needed.
No Answer