---
title: The Greenholt Phish
author: CYB3RM3
name: CYB3RM3 | The Greenholt Phish
date: 2022-01-01 17:56:18 +0100
categories: [TryHackMe, Web]
tags: [Web, Phishing]
---

Use the knowledge attained to analyze a malicious email. 

THM Room [https://tryhackme.com/room/phishingemails5fgjlzxc](https://tryhackme.com/room/phishingemails5fgjlzxc)

## TASK 1 : Just another day as a SOC Analyst.. 
For questions 1-4 and 9, we can get the responses directly viewing the email in Thunderbird :

![email.eml](/images/thm/phishingemails5fgjlzxc/phishingemails5fgjlzxc_1.png)
_email.eml_

### What is the email's timestamp? (answer format: dd/mm/yy hh:mm) 
Answer : 06/10/2020 5:58

### Who is the email from?
Answer : Mr. James Jackson

### What is his email address?
Answer : info@mutawamarine.com

###  What email address will receive a reply to this email? 
Answer : info.mutawamarine@mail.com

### What is the Originating IP?

![Header : From](/images/thm/phishingemails5fgjlzxc/phishingemails5fgjlzxc_2.png)
_Header : From_

Answer : 192.119.71.157

### Who is the owner of the Originating IP? (Do not include the "." in your answer.)

![ISP](/images/thm/phishingemails5fgjlzxc/phishingemails5fgjlzxc_3.png)
_ISP_

Using BD-IP <https://db-ip.com/>, we get the ISP.

Answer : Hostwinds LLC

### What is the SPF record for the Return-Path domain?

I check the retrun-path on Dmarcian :

![SPF](/images/thm/phishingemails5fgjlzxc/phishingemails5fgjlzxc_4.png)
_SPF_

Answer : v=spf1 include:spf.protection.outlook.com -all

### What is the DMARC record for the Return-Path domain?

I check the retrun-path on Dmarcian <https://dmarcian.com/spf-survey/> :

![DMARC](/images/thm/phishingemails5fgjlzxc/phishingemails5fgjlzxc_5.png)
_DMARC_

Answer : v=DMARC1; p=quarantine; fo=1

### What is the name of the attachment?

Answer : 

```console
SWT_#09674321____PDF__.cab
```
{: .nolineno }

### What is the SHA256 hash of the file attachment?

![Attachment SHA256](/images/thm/phishingemails5fgjlzxc/phishingemails5fgjlzxc_6.png)
_Attachment SHA256_

Answer : 2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f

### What is the attachments file size? (Don't forget to add "KB" to your answer, NUM KB)

![File Size](/images/thm/phishingemails5fgjlzxc/phishingemails5fgjlzxc_7.png)
_File Size_

I use VirusTotal with the hash to get the file size.

Answer : 400.26 KB

### What is the actual file extension of the attachment?
Answer : rar