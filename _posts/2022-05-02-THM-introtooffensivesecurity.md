---
title: Intro to Offensive Security
author: CYB3RM3
name: CYB3RM3 | Intro to Offensive Security
date: 2022-05-02 19:53:26 +0100
categories: [TryHackMe, Introduction to Cyber Security]
tags: [Web, Introduction, Offensive Security, Red Team]
---

Hack your first website (legally in a safe environment) and experience an ethical hacker's job.

THM Room [https://tryhackme.com/room/introtooffensivesecurity](https://tryhackme.com/room/introtooffensivesecurity)


## TASK 1 : Hacking your first machine
### When you've transferred money to your account, go back to your bank account page. What is the answer shown on your bank balance page? 
The web bank app is :

![Demo App](/images/thm/introtooffensivesecurity/introtooffensivesecurity_1.png)
_Demo App_

Using gobuster to list the available directories :

```console
 ubuntu@tryhackme:~/Desktop$ gobuster -u http://fakebank.com -w wordlist.txt 

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://fakebank.com/
[+] Threads      : 10
[+] Wordlist     : wordlist.txt
[+] Status codes : 200,204,301,302,307,403
[+] Timeout      : 10s
=====================================================
2022/05/02 17:42:49 Starting gobuster
=====================================================
/images (Status: 301)
/bank-transfer (Status: 200)
=====================================================
2022/05/02 17:42:58 Finished
=====================================================
```
{: .nolineno }

We found a page for transfer of money :

![Bank-transfer](/images/thm/introtooffensivesecurity/introtooffensivesecurity_2.png)
_Bank-transfer_

Transfer $2000 tfrom account 2276 to our account (8881) :

![Bank-transfer used](/images/thm/introtooffensivesecurity/introtooffensivesecurity_3.png)
_Bank-transfer used_

![Bank-transfer used success](/images/thm/introtooffensivesecurity/introtooffensivesecurity_4.png)
_Bank-transfer used success_

Then checking again our account :

![Bank account](/images/thm/introtooffensivesecurity/introtooffensivesecurity_5.png)
_Bank account_

Answer : BANK-HACKED

### If you were a penetration tester or security consultant, this is an exercise you’d perform for companies to test for vulnerabilities in their web applications; find hidden pages to investigate for vulnerabilities.
No Answer.

### Terminate the machine by clicking the red "Terminate" button at the top of the page.
No Answer.

## TASK 2 : What is Offensive Security? 
### Read the above. 
No Answer

## TASK 3 : Careers in cyber security 
### Read the above, and continue with the next room!
No Answer.