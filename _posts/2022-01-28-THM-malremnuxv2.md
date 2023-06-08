---
title: MAL - REMnux - The Redux
author: CYB3RM3
name: CYB3RM3 | MAL - REMnux - The Redux
date: 2022-01-28 12:02:54 +0100
categories: [TryHackMe, Malware]
tags: [Malware, Malware analysis]
---

A revitalised, hands-on showcase involving analysing malicious macro's, PDF's and Memory forensics of a victim of Jigsaw Ransomware; all done using the Linux-based REMnux toolset apart of my Malware Analysis series

THM Room [https://tryhackme.com/room/malremnuxv2](https://tryhackme.com/room/malremnuxv2)

## TASK 1 : Introduction
### I'm all buckled up and ready to get started. 
No Answer.

## TASK 2 : Deploy
### I've deployed my instance
No Answer.

## TASK 3 : Analysing Malicious PDF's
###  How many types of categories of "Suspicious elements" are there in "notsuspicious.pdf" 
Repeating step in example ;

![Suspicious elements](/images/thm/malremnuxv2/malremnuxv2_1.png)
_Suspicious elements_

Answer : 3

### Use peepdf to extract the javascript from "notsuspicious.pdf". What is the flag?
Answer : THM{Luckily_This_Isn't_harmful}

### How many types of categories of "Suspicious elements" are there in "advert.pdf"

![advert.pdf](/images/thm/malremnuxv2/malremnuxv2_2.png)
_advert.pdf_

Answer : 6

### Now use peepdf to extract the javascript from "advert.pdf". What is the value of "cName"?

![cName](/images/thm/malremnuxv2/malremnuxv2_2.png)
_cName_

Answer : notsuspicious

## TASK 4 : Analysing Malicious Microsoft Office Macros
### What is the name of the Macro for "DefinitelyALegitInvoice.doc" 
Executing the following code :

```console
vmonkey DefinitelyALegitInvoice.doc
[...]
```
{: .nolineno }

![ViperMonkey](/images/thm/malremnuxv2/malremnuxv2_3.png)
_ViperMonkey_

![Defolegit](/images/thm/malremnuxv2/malremnuxv2_4.png)
_Defolegit_

We got the name of the macro.

Answer : Defolegit

### What is the URL the Macro in "Taxes2020.doc" would try to launch?

Doing the same method :

![Taxes2020.doc](/images/thm/malremnuxv2/malremnuxv2_5.png)
_Taxes2020.doc_

![notac2cserver.sh](/images/thm/malremnuxv2/malremnuxv2_6.png)
_notac2cserver.sh_

Answer : http://tryhackme.com/notac2cserver.sh

## TASK 5 : I Hope You Packed Your Bags
### What is the highest file entropy a file can have? 
Answer : 8

### What is the lowest file entropy a file can have?
Answer : 0

### Name a common packer that can be used for applications?
Answer : UPX

## TASK 6 : How's Your Memory?
###  Pretty interesting stuff!
No Answer.

## TASK 7 : Finishing Up
### Fin.
No Answer.

## TASK 8 : References & Further Reading Material 
### I'm curious to read up some more! 
No Answer.