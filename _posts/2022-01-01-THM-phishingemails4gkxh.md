---
title: Phishing Prevention
author: CYB3RM3
name: CYB3RM3 | Phishing Prevention
date: 2022-01-01 16:18:31 +0100
categories: [TryHackMe, Web]
tags: [Web, Phishing]
---

Learn how to defend against phishing emails.

THM Room [https://tryhackme.com/room/phishingemails4gkxh](https://tryhackme.com/room/phishingemails4gkxh)


## TASK 1 : Introduction
### What is the MITRE ID for Software Configuration? 
Answer : M1054

## TASK 2 : SPF (Sender Policy Framework)  
### What is the best SPF rule if you wish to ensure the domain sends no mail at all? 
The answer to this question is not the one expected. As per dmarcian, blocking a domain from sending email results in adding -all to the spf without ip registered in the SPF record :

![SPF](/images/thm/phishingemails4gkxh/phishingemails4gkxh_1.png)
_SPF_

So i tried the others possibilities to get the "valid" answer.

Answer : v=spf1 ~all

### What is the meaning of the -all tag?
Answer : fail

## TASK 3 : DKIM (DomainKeys Identified Mail) 
###  Which email header shows the status of whether DKIM passed or failed? 
Look in a email header where dkim is set up or on the screenshot from the question.

Answer : authentication-results

## TASK 4 : DMARC (Domain-Based Message Authentication, Reporting, and Conformance)
### Which DMARC policy would you use not to accept an email if the message fails the DMARC check? 
Answer : p=reject

## TASK 5 : S/MIME (Secure/Multipurpose Internet Mail Extensions) 
### What is nonrepudiation? (The answer is a full sentence, including the ".") 

![S/MIME](/images/thm/phishingemails4gkxh/phishingemails4gkxh_2.png)
_S/MIME_

Go to the S/MIME link in the task.

Answer : The uniqueness of a signature prevents the owner of the signature from disowning the signature.

## TASK 6 : SMTP Status Codes
### What Wireshark filter can you use to narrow down the packet output using SMTP status codes?
Answer : smtp.response.code

### Per the network traffic, what was the message for status code 220? (Do not include the status code (220) in the answer)

![SMTP Response](/images/thm/phishingemails4gkxh/phishingemails4gkxh_3.png)
_SMTP Response_

Answer : 

```console
<domain> Service ready
```
{: .nolineno }

### One packet shows a response that an email was blocked using spamhaus.org. What were the packet number and status code? (no spaces in your answer)

![SMTP Response Blocked](/images/thm/phishingemails4gkxh/phishingemails4gkxh_4.png)
_SMTP Response Blocked_

Answer : 156,553

### Based on the packet from the previous question, what was the message regarding the mailbox?
Answer : mailbox name not allowed

###  What is the status code that will typically precede a SMTP DATA command?
Checking the link <https://www.mailersend.com/blog/smtp-codes> provided for SMTP status code :

![SMTP Response Codes](/images/thm/phishingemails4gkxh/phishingemails4gkxh_5.png)
_SMTP Response Codes_

Answer : 354

## TASK 7 : SMTP Traffic Analysis 
### What port is the SMTP traffic using?
Answer : 25

###  How many packets are specifically SMTP?

![SMTP](/images/thm/phishingemails4gkxh/phishingemails4gkxh_6.png)
_SMTP_

Answer :  512

### What is the source IP address for all the SMTP traffic?
Answer : 10.12.19.101

### What is the filename of the third file attachment?

![File Attachment](/images/thm/phishingemails4gkxh/phishingemails4gkxh_7.png)
_File Attachment_

Answer : attachment.scr

### How about the last file attachment?
Answer : .zip

## TASK 8 : SMTP and C&C Communication
###  Per MITRE ATT&CK, which software is associated with using SMTP and POP3 for C2 communications? 

![Zebrocy](/images/thm/phishingemails4gkxh/phishingemails4gkxh_8.png)
_Zebrocy_

Answer : Zebrocy
## TASK 9 : Conclusion

### Per the playbook, what framework was used for the IR process? 

Looking at the pdf file for incidence response for phishing case :

![Useful Links](/images/thm/phishingemails4gkxh/phishingemails4gkxh_9.png)
_Useful Links_

Answer : NIST