---
title: SSRF  
author: CYB3RM3
name: CYB3RM3 | SSRF  
date: 2021-10-11 19:32:07 +0100
categories: [TryHackMe, Web]
tags: [Web, SSRF]
---

Learn how to exploit Server-Side Request Forgery (SSRF) vulnerabilities, allowing you to access internal server resources.
THM Room [https://tryhackme.com/room/ssrfqi](https://tryhackme.com/room/ssrfqi)


## TASK 1 : What is an SSRF?
### What does SSRF stand for?
Answer : Server Side Request Forgery

### As opposed to a regular SSRF, what is the other type?
Answer : Blind

## TASK 2 : SSRF Examples

### What is the flag from the SSRF Examples site?
I tried :

```console
https://website.thm/item/2?server=server.website.thm/flag?id=9
```
{: .nolineno }

But it return a 404. We need to escape to rest of the remaining path with &x= ; The request is now : 

```console
https://website.thm/item/2?server=server.website.thm/flag?id=9&x=
```
{: .nolineno }

Answer : THM{SSRF_MASTER}

## TASK 3 : Finding an SSRF 
### What website can be used to catch HTTP requests from a server?
Answer : requestbin.com

## TASK 4 : Defeating Common SSRF Defenses
### What method can be used to bypass strict rules?
Answer : Open Redirect

### What IP address may contain sensitive data in a cloud environment?
Answer : 169.254.169.254

### What type of list is used to permit only certain input?
Answer : Allow List

### What type of list is used to stop certain input?
Answer : Deny List

## TASK 5 : SSRF Practical  
### What is the flag from the /private directory?

First, you need to create an account then set up an avatar.

Afterwards, you can edit the HMTL calue for the radio button to x/../private and update your avatar :

![Setup Avatar](/images/thm/ssrfqi/ssrfqi_1.png)
_Setup Avatar_

![Blank Avatar](/images/thm/ssrfqi/ssrfqi_2.png)
_Blank Avatar_

You normally have a blank avatar and when you inspect the source code you'll see a base64 encode url for the avatar :

![Base64 flag](/images/thm/ssrfqi/ssrfqi_3.png)
_Base64 flag_

Decoding from Base64 the string "VEhNe1lPVV9XT1JLRURfT1VUX1RIRV9TU1JGfQ==" give you the flag.

```console
┌──(kaliuser㉿kali)-[~]
└─$ echo "VEhNe1lPVV9XT1JLRURfT1VUX1RIRV9TU1JGfQ==" | base64 -d 
THM{YOU_WORKED_OUT_THE_SSRF}
```
{: .nolineno }

Answer : THM{YOU_WORKED_OUT_THE_SSRF}