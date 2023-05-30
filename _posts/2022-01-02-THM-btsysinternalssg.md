---
title: Sysinternals
author: CYB3RM3
name: CYB3RM3 | Sysinternals
date: 2022-01-02 12:18:17 +0100
categories: [TryHackMe, Windows]
tags: [Windows, System]
---

Learn to use the Sysinternals tools to analyze Windows systems or applications.

THM Room [https://tryhackme.com/room/btsysinternalssg](https://tryhackme.com/room/btsysinternalssg)


## TASK 1 : Introduction
### When did Microsoft acquire the Sysinternals tools? 
Answer : 2006

### I deployed the attached virtual machine and I'm ready to move on...
No Answer

## TASK 2 : Install the Sysinternals Suite
### What is the last tool listed within the Sysinternals Suite? 
Answer : ZoomIt

## TASK 3 : Using Sysinternals Live
###  What service needs to be enabled on the local host to interact with live.sysinternals.com? 
Answer : webclient

## TASK 4 : File and Disk Utilities
### There is a txt file on the desktop named file.txt. Using one of the three discussed tools in this task, what is the text within the ADS? 

```console
C:\Users\Administrator\Desktop>streams file.txt -accepteula

streams v1.60 - Reveal NTFS alternate streams.
Copyright (C) 2005-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Users\Administrator\Desktop\file.txt:
         :ads.txt:$DATA 26

C:\Users\Administrator\Desktop>notepad .\file.txt:ads.txt
```
{: .nolineno }

![file.txt:ads.txt](/images/thm/btsysinternalssg/btsysinternalssg_1.png)
_file.txt:ads.txt_

Answer : I am hiding in the stream.

## TASK 5 : Networking Utilities
### Using WHOIS tools, what is the ISP/Organization for the remote address in the screenshots above? 
Using whois or other online tools.

Answer : Microsoft Corporation

## TASK 6 : Process Utilities
### Run Autoruns and inspect what are the new entries in the Image Hijacks tab compared to the screenshots above. 
No Answer

### What entry was updated?

![Autoruns](/images/thm/btsysinternalssg/btsysinternalssg_2.png)
_Autoruns_

Answer : taskmgr.exe

### What is the updated value?
Answer : c:\tools\sysint\procexp.exe

## TASK 7 : Security Utilities 
### You will check out the Sysmon room if you haven't done so already... 
No Answer

## TASK 8 : System Information
### Moving along...
No Answer 

## TASK 9 : Miscellaneous
### Run the Strings tool on ZoomIt.exe. What is the full path to the .pdb file? 

```console
c:\Tools\sysint>strings .\ZoomIt.exe | findstr /i zoomit.pdb*
C:\agent\_work\112\s\Win32\Release\ZoomIt.pdb
```
{: .nolineno }

Answer : C:\agent\_work\112\s\Win32\Release\ZoomIt.pdb

## TASK 10 : Conclusion
### I will definitely look into Sysinternals more in-depth and add this to my arsenal...  
No Answer 