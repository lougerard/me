---
title: Web Application Security
author: CYB3RM3
name: CYB3RM3 | Web Application Security
date: 2022-05-02 19:27:53 +0100
categories: [TryHackMe, Web]
tags: [Web, Introduction]
---

Hack your first website (legally in a safe environment) and experience an ethical hacker's job.

THM Room [https://tryhackme.com/room/introwebapplicationsecurity](https://tryhackme.com/room/introwebapplicationsecurity)


## TASK 1 : Introduction
### What do you need to access a web application? 
Answer : Browser

## TASK 2 : Web Application Security Risks 
### You discovered that the login page allows an unlimited number of login attempts without trying to slow down the user or lock the account. What is the category of this security risk?

![Identification](/images/thm/introwebapplicationsecurity/introwebapplicationsecurity_1.png)
_Identification_

Answer : Identification and Authentication Failure

### You noticed that the username and password are sent in cleartext without encryption. What is the category of this security risk?

![Cryptographic](/images/thm/introwebapplicationsecurity/introwebapplicationsecurity_2.png)
_Cryptographic_

Answer : Cryptographic Failures

## TASK 3 : Practical Example of Web Application Security 
###  Check the other users to discover which user account was used to make the malicious changes and revert them. After reverting the changes, what is the flag that you have received?
Open the button "view site" :

![Example 1](/images/thm/introwebapplicationsecurity/introwebapplicationsecurity_3.png)
_Example 1_

I saw i can change the user_id in the "You activity" tab, so i tried numbers from 0 to 11

![Example 2](/images/thm/introwebapplicationsecurity/introwebapplicationsecurity_4.png)
_Example 2_

When arrived at number 9, i got the user who modified the site :

![Example 3](/images/thm/introwebapplicationsecurity/introwebapplicationsecurity_5.png)
_Example 3_

Let's revert all the changes :

![Example 4](/images/thm/introwebapplicationsecurity/introwebapplicationsecurity_6.png)
_Example 4_

Here we go, this is the flag.

Answer : THM{IDOR_EXPLORED}