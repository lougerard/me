---
title: Phishing Analysis Fundamentals  
author: CYB3RM3
name: CYB3RM3 | Phishing Analysis Fundamentals  
date: 2021-12-29 19:02:03 +0100
categories: [TryHackMe, Web]
tags: [Web, Phishing]
---

Learn all the components that make up an email. 

THM Room [https://tryhackme.com/room/phishingemails1tryoe](https://tryhackme.com/room/phishingemails1tryoe)


## TASK 1 : Introduction
### Read the above and launch the attached VM. 
No Answer

## TASK 2 : The Email Address 
### Email dates back to what time frame? 
Answer : 1970s

## TASK 3 : Email Delivery
### What port is classified as Secure Transport for SMTP? 
Answer : 465

### What port is classified as Secure Transport for IMAP?
Answer : 993

### What port is classified as Secure Transport for POP3?
Answer : 995

## TASK 4 : Email Headers 
### What email header is the same as "Reply-to"?
Answer : Return-Path

### Once you find the email sender's IP address, where can you retrieve more information about the IP?
Answer : http://www.arin.net

## TASK 5 : Email Body
### In the above screenshots, what is the URI of the blocked image? 
Answer : https://i.imgur.com/LSOtDI.png

### In the above screenshots, what is the name of the PDF attachment?
Answer : Payment-updateid.pdf

### In the attached virtual machine, view the information in email2.txt and reconstruct the PDF using the base64 data. What is the text within the PDF?
Remove unwanted parts in the email2.txt 

![Unwanted Section](/images/thm/phishingemails1tryoe/phishingemails1tryoe_1.png)
_Unwanted Section_

![Unwanted Section End](/images/thm/phishingemails1tryoe/phishingemails1tryoe_2.png)
_Unwanted Section End_

Then open terminal and run :

```console
ubuntu@ip-10-10-45-176:~/Desktop/Email Samples$ base64 -d test.txt > test.pdf
```
{: .nolineno }

![Reconstructed PDF](/images/thm/phishingemails1tryoe/phishingemails1tryoe_3.png)
_Reconstructed PDF_

Answer : THM{BENIGN_PDF_ATTACHMENT}

## TASK 6 : Types of Phishing 
The next 4 questions is an analyse of the email3.eml :

![email3.eml](/images/thm/phishingemails1tryoe/phishingemails1tryoe_4.png)
_email3.eml_

### What trusted entity is this email masquerading as?
Check point 1 of the sceenshot.

Answer : Home Depot

### What is the sender's email?
Check point 2 of the sceenshot.

Answer : support@teckbe.com

### What is the subject line?
Check point 3 of the sceenshot.

Answer : Order Placed : Your Order ID OD2321657089291 Placed Successfully

### What is the URL link for - CLICK HERE? (Enter the defanged URL)
To get the URL, right click on the "click here" hyperlink then choose "save link". Paste the link on CyberChef and you get the defanged URL :

![Defang URL](/images/thm/phishingemails1tryoe/phishingemails1tryoe_5.png)
_Defang URL_

Answer : 

```console
hxxp[://]t[.]teckbe[.]com/p/?j3=EOowFcEwFHl6EOAyFcoUFVTVEchwFHlUFOo6lVTTDcATE7oUE7AUFo==
```
{: .nolineno }

## TASK 7 : Conclusion
### What is BEC? 
Answer : Business Email Compromise