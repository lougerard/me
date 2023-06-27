---
title: Common Attacks
author: CYB3RM3
name: CYB3RM3 | Common Attacks
date: 2022-02-19 00:05:50 +0100
categories: [TryHackMe, Security]
tags: [Security, Awareness]
---

With practical exercises see how common attacks occur, and improve your cyber hygiene to stay safer online.

THM Room [https://tryhackme.com/room/commonattacks](https://tryhackme.com/room/commonattacks)


## TASK 1 : Information Introduction
### Let's get started!0
No Answer

## TASK 2 : Common Attacks Social Engineering
### Read the task information and watch the attached videos
No Answer

### What was the original target of Stuxnet?

![Stuxnet](/images/thm/commonattacks/commonattacks_1.png)
_Stuxnet_

Answer : the Iran nuclear programme

## TASK 3 : Common Attacks Social Engineering: Phishing
###  Click the green "View Site" button at the top of this task if you haven't already done so.
No Answer.

### What is the flag?
First phishing/safe email, link and showed-link are different :

![Phshing 1](/images/thm/commonattacks/commonattacks_2.png)
_Phshing 1_

![Phshing 1 link](/images/thm/commonattacks/commonattacks_3.png)
_Phshing 1 link_

Second one is phishing too. Misspelling in the email address and suspicious attachment ;

![Phshing 2](/images/thm/commonattacks/commonattacks_4.png)
_Phshing 2_

![Phshing 2 link](/images/thm/commonattacks/commonattacks_5.png)
_Phshing 2 link_

Third one is safe :

![Phshing 3](/images/thm/commonattacks/commonattacks_6.png)
_Phshing 3_

![Phshing 3 link](/images/thm/commonattacks/commonattacks_7.png)
_Phshing 3 link_

And last one is phishing because of file attachment from untrsuted sender or not expected :

![Phshing 4](/images/thm/commonattacks/commonattacks_8.png)
_Phshing 4_

![Phshing 4 link](/images/thm/commonattacks/commonattacks_9.png)
_Phshing 4 link_

Answer : THM{I_CAUGHT_ALL_THE_PHISH}

## TASK 4 : Common Attacks Malware and Ransomware
### [ Research ] What currency did the Wannacry attackers request payment in?

![Wannacry](/images/thm/commonattacks/commonattacks_10.png)
_Wannacry_

Answer : bitcoin

## TASK 5 : Common Attacks Passwords and Authentication
### Put yourself in the shoes of a malicious hacker. You have managed to dump the password database for an online service, but you still have to crack those hashes! Click the green button at the start of the task to deploy the interactive hash brute-forcer!
No Answer.

### Copy the list of passwords into the "Password List" field of the hash cracker, then click "Go"!
No Answer.

### The hash cracker should find the password that matches the target hash very quickly. What is the password?
Putting password list in the box, all MD5 will be computed and compared to the real password MD5 :

![Hash Cracker](/images/thm/commonattacks/commonattacks_11.png)
_Hash Cracker_

![Flag password](/images/thm/commonattacks/commonattacks_12.png)
_Flag password_

Answer : TryHackMe123!

### In the next task we will look at some of the common account protection measures, as well as how to generate secure passwords.
No Answer.

## TASK 6 : Staying Safe Multi-Factor Authentication and Password Managers
### Where you have the option, which should you use as a second authentication factor between SMS based TOTPs or Authenticator App based TOTPs (SMS or App)?

![MFA](/images/thm/commonattacks/commonattacks_13.png)
_MFA_

Answer : APP

## TASK 7 : Staying Safe Public Network Safety

### Deploy the interactive content by clicking the green button at the top of the task.
No Answer.

### The interactive content for this task demonstrates what can happen if information is sent over a potentially unsafe network with various types of encryption (or lack thereof). There is no flag for this task, but you are encouraged to try each of the different scenarios, mixing and matching the options provided in the control box at the bottom right of the screen.
No VPN nor HTTPS :

![No VPN nor HTTPS](/images/thm/commonattacks/commonattacks_14.png)
_No VPN nor HTTPS_

HTTPS without VPN :

![HTTPS without VPN](/images/thm/commonattacks/commonattacks_15.png)
_HTTPS without VPN_

PN without HTTPS :

![VPN without HTTPS](/images/thm/commonattacks/commonattacks_16.png)
_VPN without HTTPS_

VPN and HTTPS :

![VPN and HTTPS](/images/thm/commonattacks/commonattacks_17.png)
_VPN and HTTPS_

No Answer.

## TASK 8 : Staying Safe Backups
### What is the minimum number of up-to-date backups you should make?

![Backup golden rules](/images/thm/commonattacks/commonattacks_18.png)
_Backup golden rules_

Answer : 3

### Of these, how many (at minimum) should be stored in another location?
Answer : 1

## TASK 9 : Staying Safe Updates and Patches
###  (Optional) Complete the Blue room on TryHackMe to see the brutal effects of the Eternal Blue exploit in action against an unpatched machine for yourself!
No Answer. ALready did eternal blue room from THM but unfortunetly, i didn't do a write up for it. Maybe later...

## TASK 10 : Information Conclusion 
### I have completed the Common Attacks room!
No Answer.