---
title: Phishing Analysis Tools  
author: CYB3RM3
name: CYB3RM3 | Phishing Analysis Tools
date: 2021-12-31 14:31:55 +0100
categories: [TryHackMe, Web]
tags: [Web, Phishing]
---

Learn the tools used to aid an analyst to investigate suspicious emails. 

THM Room [https://tryhackme.com/room/phishingemails3tryoe](https://tryhackme.com/room/phishingemails3tryoe)


## TASK 1 : Introduction
### Read the above. 
No Answer

## TASK 2 : What information should we collect? 
### Read the above. 
No Answer

## TASK 3 : Email header analysis 
###  What is the official site name of the bank that capitai-one.com tried to resemble?
Googling capitai one bank and the result capitalone.com come at first and seems quite goodlooking !

Answer : capitalone.com

## TASK 4 : Email body analysis### ###  
### How can you manually get the location of a hyperlink? 
Answer : Copy Link Location

## TASK 5 : Malware Sandbox
### Read the above. 
No Answer

## TASK 6 : PhishTool 
###  Look at the Strings output. What is the name of the EXE file?

![PhishTool](/images/thm/phishingemails3tryoe/phishingemails3tryoe_1.png)
_PhishTool_

Answer : 454326_PDF.exe

## TASK 7 : Phishing Case 1 

![email3.eml](/images/thm/phishingemails3tryoe/phishingemails3tryoe_2.png)
_email3.eml_

### What brand was this email tailored to impersonate?
Answer : Netflix

### What is the From email address?
View source of email and paste it to to an email header analyzer like Message Header Analyzer from Microsoft : <https://mha.azurewebsites.net/>.

![Header Analyzer](/images/thm/phishingemails3tryoe/phishingemails3tryoe_3.png)
_Header Analyzer_

Answer : JGQ47wazXe1xYVBrkeDg-JOg7ODDQwWdR@JOg7ODDQwWdR-yVkCaBkTNp.gogolecloud.com

### What is the originating IP? Defang the IP address.  
We got the ip from the last question. We just need to defand the ip with CyberChef for example.

Answer : 209[.]85[.]167[.]226

### From what you can gather, what do you think will be a domain of interest? Defang the domain.
Answer : etekno[.]xyz

### What is the shortened URL? Defang the URL.
Copy link location and the "update account now" button then defand the shortened URL.

Answer : hxxps[://]t[.]co/yuxfZm8KPg?amp=1

## TASK 8 : Phishing Case 2 
###  What is this analysis classified as?

![Any Run](/images/thm/phishingemails3tryoe/phishingemails3tryoe_4.png)
_Any Run_

Answer : Suspicious activity

### What is the name of the PDF file?
Check point 1 of the sceenshot.

Answer : Payment-updateid.pdf

### What is the SHA 256 hash for the PDF file?

![Hash](/images/thm/phishingemails3tryoe/phishingemails3tryoe_5.png)
_Hash_

Answer : cc6f1a04b10bcb168aeec8d870b97bd7c20fc161e8310b5bce1af8ed420e2c24

### What two IP addresses are classified as malicious? Defang the IP addresses. (answer: IP_ADDR,IP_ADDR)
Checking inn the DNS request, i found 2 suspicious ip :

![DNS Requests](/images/thm/phishingemails3tryoe/phishingemails3tryoe_6.png)
_DNS Requests_

Answer : 2[.]16[.]107[.]24,2[.]16[.]107[.]49

### What Windows process was flagged as Potentially Bad Traffic?

![Threats](/images/thm/phishingemails3tryoe/phishingemails3tryoe_7.png)
_Threats_

Answer : svchost.exe

## TASK 9 : Phishing Case 3


###  What is this analysis classified as?

![cbj200620039539.xlsx](/images/thm/phishingemails3tryoe/phishingemails3tryoe_8.png)
_cbj200620039539.xlsx_

Answer :  Malicious activity

### What is the name of the Excel file?

![Filename](/images/thm/phishingemails3tryoe/phishingemails3tryoe_9.png)
_Filename_

Answer : CBJ200620039539.xlsx

### What is the SHA 256 hash for the file?
Check previous question.

Answer : 5f94a66e0ce78d17afc2dd27fc17b44b3ffc13ac5f42d3ad6a5dcfb36715f3eb

### What domains are listed as malicious? Defang the URLs & submit answers in alphabetical order. (answer: URL1,URL2,URL3)

![DNS Requests](/images/thm/phishingemails3tryoe/phishingemails3tryoe_10.png)
_DNS Requests_

Answer : biz9holdings[.]com,findresults[.]site,ww38[.]findresults[.]site

### What IP addresses are listed as malicious? Defang the IP addresses & submit answers from lowest to highest. (answer: IP1,IP2,IP3)

![Connections](/images/thm/phishingemails3tryoe/phishingemails3tryoe_11.png)
_Connections_

Answer : 75[.]2[.]11[.]242,103[.]224[.]182[.]251,204[.]11[.]56[.]48

### What vulnerability does this malicious attachment attempt to exploit?

![Vulnerability](/images/thm/phishingemails3tryoe/phishingemails3tryoe_12.png)
_Vulnerability_

Answer : CVE-2017-11882

## TASK 10 : Conclusion
### Read the above. 
No Answer