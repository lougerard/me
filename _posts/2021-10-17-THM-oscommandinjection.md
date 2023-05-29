---
title: Command Injection   
author: CYB3RM3
name: CYB3RM3 | Command Injection  
date: 2021-10-17 10:59:44 +0100
categories: [TryHackMe, Web]
tags: [Web, Injection]
---

Learn about a vulnerability allowing you to execute commands through a vulnerable app, and its remediations.

THM Room [https://tryhackme.com/room/oscommandinjection](https://tryhackme.com/room/oscommandinjection)


## TASK 1 : Introduction (What is Command Injection?) 
### Read me! 
No Answer

## TASK 2 : Discovering Command Injection  
### What variable stores the user's input in the PHP code snippet in this task? 
Answer : $title

### What HTTP method is used to retrieve data submitted by a user in the PHP code snippet?
Answer : GET

### If I wanted to execute the id command in the Python code snippet, what route would I need to visit?
Answer : /id

## TASK 3 : Exploiting Command Injection 
### What payload would I use if I wanted to determine what user the application is running as? 
Answer : whoami

### What popular network tool would I use to test for blind command injection on a Linux machine?
Answer : ping

### What payload would I use to test a Windows machine for blind command injection?
Answer : timeout

## TASK 4 : Remediating Command Injection   
### What is the term for the process of "cleaning" user input that is provided to an application? 
Answer : sanitisation

## TASK 5 : Practical: Command Injection (Deploy) 
### What user is this application running as? 
Firstly i tested the given example 127.0.0.1 and i got : 

![DiagnoseIT](/images/thm/oscommandinjection/oscommandinjection_1.png)
_DiagnoseIT_

Then i tried directly the payload "whoami" but it got filtered :

![Whoami](/images/thm/oscommandinjection/oscommandinjection_2.png)
_Whoami_

I finally escape the filter by prepend "ls&" to my payload to get the answer to the whoami :

![Whoami escaped](/images/thm/oscommandinjection/oscommandinjection_3.png)
_Whoami escaped_

Answer : www-data

### What are the contents of the flag located in /home/tryhackme/flag.txt?
I saw the input was filtered so an example payload here is : "ls&cat /home/tryhackme/flag.txt"

![Falg](/images/thm/oscommandinjection/oscommandinjection_4.png)
_Flag_

Answer : THM{COMMAND_INJECTION_COMPLETE}

## TASK 6 : Conclusion
### Terminate the vulnerable machine from task 5 
No Answer
