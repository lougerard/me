---
title: Autopsy
author: CYB3RM3
name: CYB3RM3 | Autopsy
date: 2022-01-24 13:37:42 +0100
categories: [TryHackMe, Forensics]
tags: [Forensics, Investigation, Memory analysis, Autospy]
---

Learn how to use Autopsy to investigate artefacts from a disk image. Use your knowledge to investigate an employee who is being accused of leaking private company data.

THM Room [https://tryhackme.com/room/btautopsye0](https://tryhackme.com/room/btautopsye0)


## TASK 1 : Introduction
### You started the virtual machine.
No Answer

## TASK 2 : Installation
###  Read the above
No Answer

## TASK 3 : Workflow Overview
### Autopsy files end with which file extension? 
Looking into the folder with the sample case :

![Sample Case](/images/thm/btautopsye0/btautopsye0_1.png)
_Sample Case_

Answer : .aut

## TASK 4 : Data Sources
### In the above screenshot, what is the disk image format for SUSPECTHD? 

![SUSPECTHD](/images/thm/btautopsye0/btautopsye0_2.png)
_SUSPECTHD_

Answer : EnCase

## TASK 5 : Ingest Modules
### Read the above
No Answer.

## TASK 6 : The User Interface
### Read the above 
No Answer.

## TASK 7 : Data Analysis


### What is the full name of the operating system version?
Taking a look on the summary for the sample-case.dd :

![Summary](/images/thm/btautopsye0/btautopsye0_3.png)
_Summary_

Answer : Windows 7 Ultimate Service pack 1

### What percentage of the drive are documents? Include the % in your answer.
Answer : 40.8%

### The majority of file events occurred on what date? (MONTH DD, YYYY)

![File events](/images/thm/btautopsye0/btautopsye0_4.png)
_File events_

Answer : March 25,2015

### What is the name of an Installed Program with the version number of 6.2.0.2962?
To get quickly the answer for this one, i performed a keyword search with exact match on the version :

![Program name](/images/thm/btautopsye0/btautopsye0_5.png)
_Program name_

Answer : Eraser

### A user has a Password Hint. What is the value?
User infos can be seen in the "operating System user Account" section. Then i navigated from User ID to User ID and checked the informations so i found :

![Password Hint](/images/thm/btautopsye0/btautopsye0_6.png)
_Password Hint_

Answer : IAMAN

### Numerous SECRET files were accessed from a network drive. What was the IP address?
Another keyword search on "secret" :

![Secrets](/images/thm/btautopsye0/btautopsye0_7.png)
_Secrets_

![More Secrets](/images/thm/btautopsye0/btautopsye0_8.png)
_More Secrets_

Answer : 10.11.11.128

### What web search term has the most entries?

Go to Result > Extracted content > Web Search. On 63 results ther are 17 for information leakage cases :

![Leakage cases](/images/thm/btautopsye0/btautopsye0_9.png)
_Leakage cases_

Answer : information leakage cases

### What was the web search conducted on 3/25/2015 21:46:44?
Always in web search, i looked at the result order by date :

![anti-forensic tools](/images/thm/btautopsye0/btautopsye0_10.png)
_anti-forensic tools_

Answer : anti-forensic tools

### What binary is listed as an Interesting File?
Searched into flagged executable :

![Interesting File](/images/thm/btautopsye0/btautopsye0_13.png)
_Interesting File_

Answer : googledrivesync.exe

### What self-assuring message did the 'Informant' write for himself on a Sticky Note? (no spaces)
A quick search on google to find the location of stored Sticky notes on windows. There are stored in : appdata\Roaming\Microsoft\stiky notes then i look in the volume vol3 :

![Sticky notes](/images/thm/btautopsye0/btautopsye0_11.png)
_Sticky notes_

Answer : Tomorrow... Everything will be OK...

## TASK 8 : Visualization Tools
### What single letter parameter should always be visible in the Command line or Binary path? 
Open timeline then choose the right date an click on the result for this day :

![Timeline](/images/thm/btautopsye0/btautopsye0_12.png)
_Timeline_

Answer : 46

## TASK 9 : Conclusion 
###  Read the above
No Answer.