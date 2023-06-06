---
title: RedLine
author: CYB3RM3
name: CYB3RM3 | RedLine
date: 2022-01-24 11:25:00 +0100
categories: [TryHackMe, Forensics]
tags: [Forensics, Investigation, Memory analysis]
---

Learn how to use Redline to perform memory analysis and to scan for IOCs on an endpoint. 

THM Room [https://tryhackme.com/room/btredlinejoxr3d](https://tryhackme.com/room/btredlinejoxr3d)

## TASK 1 : Introduction
### Who created Redline? 
Answer : FireEye

## TASK 2 : Data Collection
### What data collection method takes the least amount of time?
As we can read in the text : Standard Collector

Answer : Standard Collector

### You are reading a research paper on a new strain of ransomware. You want to run the data collection on your computer based on the patterns provided, such as domains, hashes, IP addresses, filenames, etc. What method would you choose to run a granular data collection against the known indicators?
Answer : IOC Search Collector

### What script would you run to initiate the data collection process? Please include the file extension.

![RunRedlineAudit.bat](/images/thm/btredlinejoxr3d/btredlinejoxr3d_1.png)
_RunRedlineAudit.bat_

Answer : RunRedlineAudit.bat

### If you want to collect the data on Disks and Volumes, under which option can you find it? 

![Redline Options](/images/thm/btredlinejoxr3d/btredlinejoxr3d_2.png)
_Redline Options_

Answer : disk enumeration

### What cache does Windows use to maintain a preference for recently executed code?
As per User Guide <https://www.fireeye.com/content/dam/fireeye-www/services/freeware/ug-redline.pdf> and looking for "Cache" keyword :

![Prefetch Cache](/images/thm/btredlinejoxr3d/btredlinejoxr3d_3.png)
_Prefetch Cache_

Answer : Prefetch

## TASK 3 : The Redline Interface
### Where in the Redline UI can you view information about the Logged in User?

![system information](/images/thm/btredlinejoxr3d/btredlinejoxr3d_4.png)
_system information_

Answer : system information

## TASK 4 : Standard Collector Analysis
### Provide the Operating System detected for the workstation.

![Operating System](/images/thm/btredlinejoxr3d/btredlinejoxr3d_5.png)
_Operating System_

Answer : Windows Server 2019 Standard 17763

### Provide the BIOS Version for the workstation.

![BIOS](/images/thm/btredlinejoxr3d/btredlinejoxr3d_6.png)
_BIOS_

Answer : Xen 4.2.amazon

### What is the suspicious scheduled task that got created on the victim's computer? 

![Scheduled Task](/images/thm/btredlinejoxr3d/btredlinejoxr3d_7.png)
_Scheduled Task_

Answer : MSOfficeUpdateFa.ke

### Find the message that the intruder left for you in the task.

![Full Detailed Information](/images/thm/btredlinejoxr3d/btredlinejoxr3d_8.png)
_Full Detailed Information_

Answer : THM-p3R5IStENCe-m3Chani$m

### There is a new System Event ID created by an intruder with the source name "THM-Redline-User" and the Type "ERROR". Find the Event ID #.
Go to event log then search source name in the filter :

![Event Logs](/images/thm/btredlinejoxr3d/btredlinejoxr3d_9.png)
_Event Logs_

Answer : 546

### Provide the message for the Event ID.

![Event ID Message](/images/thm/btredlinejoxr3d/btredlinejoxr3d_10.png)
_Event ID Message_

Answer : Someone cracked my password. Now I need to rename my puppy-++-

### It looks like the intruder downloaded a file containing the flag for Question 8. Provide the full URL of the website.

![File Download History](/images/thm/btredlinejoxr3d/btredlinejoxr3d_11.png)
_File Download History_

Answer : https://wormhole.app/download-stream/gI9vQtChjyYAmZ8Ody0AuA

### Provide the full path to where the file was downloaded to including the filename.
Answer : C:\Program Files (x86)\Windows Mail\SomeMailFolder\flag.txt

### Provide the message the intruder left for you in the file.

![Flag](/images/thm/btredlinejoxr3d/btredlinejoxr3d_12.png)
_Flag_

Answer : THM{600D-C@7cH-My-FR1EnD}

## TASK 5 : IOC Search Collector
### What is the actual filename of the Keylogger?

![Keylogger Filename](/images/thm/btredlinejoxr3d/btredlinejoxr3d_13.png)
_Keylogger Filename_

Answer : psylog.exe

### What filename is the file masquerading as?
Answer : THM1768.exe

### Who is the owner of the file?
Answer : WIN-2DET5DP0NPT\charles

### What is the file size in bytes?
Answer : 35400

### Provide the full path of where the .ioc file was placed after the Redline analysis, include the .ioc filename as well

![Full Path](/images/thm/btredlinejoxr3d/btredlinejoxr3d_14.png)
_Full Path_

Answer : c:\charles\Desktop\Keylogger-IOCSearch\IOCs\keylogger.ioc

## TASK 6 : IOC Search Collector Analysis
### Provide the path of the file that matched all the artifacts along with the filename. 
Run the IOC you create on the session in C:\Users\Administrator\Documents\Analysis :

![IOC Report](/images/thm/btredlinejoxr3d/btredlinejoxr3d_15.png)
_IOC Report_

Answer : C:\Users\Administrator\AppData\Local\Temp\8eJv8w2id6IqN85dfC.exe

### Provide the path where the file is located without including the filename.
Answer : C:\Users\Administrator\AppData\Local\Temp

### Who is the owner of the file?

![Owner](/images/thm/btredlinejoxr3d/btredlinejoxr3d_16.png)
_Owner_

Answer : BUILTIN\Administrators

### Provide the subsystem for the file.
Checked for "more info" :

![Subsystem](/images/thm/btredlinejoxr3d/btredlinejoxr3d_17.png)
_Subsystem_

Then it gives you :

![Passthehash](/images/thm/btredlinejoxr3d/btredlinejoxr3d_18.png)
_Passthehash_

Answer : Windows_CUI

### Provide the Device Path where the file is located.
Answer : \Device\HarddiskVolume2

### Provide the hash (SHA-256) for the file.
Copied the md5 (c590a84b8c72cf18f35ae166f815c9df) from the result and pasted it on Virustotal  then go to detail tab to get the SHA256 result :

![Virustotal](/images/thm/btredlinejoxr3d/btredlinejoxr3d_19.png)
_Virustotal_

Answer : 57492d33b7c0755bb411b22d2dfdfdf088cbbfcd010e30dd8d425d5fe66adff4

### The attacker managed to masquerade the real filename. Can you find it having the hash in your arsenal? 

Checinkg the others informations on Virustotal gives you the answer :


Answer : psexec.exe
## TASK 7 : Endpoint Investigation
## TASK 8 : Conclusion 