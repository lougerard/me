---
title: Disk Analysis & Autopsy
author: CYB3RM3
name: CYB3RM3 | Disk Analysis & Autopsy
date: 2022-01-26 11:01:33 +0100
categories: [TryHackMe, Forensics]
tags: [Forensics, Investigation, Memory analysis, Autopsy]
---

Ready for a challenge? Use Autopsy to investigate artifacts from a disk image.

THM Room [https://tryhackme.com/room/autopsy2ze0](https://tryhackme.com/room/autopsy2ze0)

## TASK 1 : Windows 10 Disk Image
### What is the MD5 hash of the E01 image?

![MD5 Hash](/images/thm/autopsy2ze0/autopsy2ze0_1.png)
_MD5 Hash_

Answer : 3f08c518adb3b5c1359849657a9b2079

### What is the computer account name?

![Computer account name](/images/thm/autopsy2ze0/autopsy2ze0_2.png)
_Computer account name_

Answer : DESKTOP-0R59DJ3

### List all the user accounts. (alphabetical order)

![User accounts](/images/thm/autopsy2ze0/autopsy2ze0_3.png)
_User accounts_

You can ethier just rewrite all or export to csv and delete all irrelevelant informations before copy the names :

Answer : H4S4N,joshwa,keshav,sandhya,shreya,sivapriya,srini,suba

### Who was the last user to log into the computer?
From above capture, ordered by "date accessed".

Answer : sivapriya

### What was the IP address of the computer?

Found Look@lan program installed so i look inside his .ini file :

![Computer IP](/images/thm/autopsy2ze0/autopsy2ze0_4.png)
_Computer IP_

Answer : 192.168.130.216

### What was the MAC address of the computer? (XX-XX-XX-XX-XX-XX)
From above capture and adding "-" after all 2 char from %LANNIC%

Answer : 08-00-27-2c-c4-b9

### Name the network cards on this computer.
Searched for  keyword "ethernet" :

![Network cards](/images/thm/autopsy2ze0/autopsy2ze0_5.png)
_Network cards_

Answer : Intel(R) PRO/1000 MT Desktop Adapter

### What is the name of the network monitoring tool?
From previous investigations.

Answer : look@lan

### A user bookmarked a Google Maps location. What are the coordinates of the location?

![Google Maps location](/images/thm/autopsy2ze0/autopsy2ze0_6.png)
_Google Maps location_

Answer : 12°52'23.0"N 80°13'25.0"E

### A user has his full name printed on his desktop wallpaper. What is the user's full name?
Looking around the %AppData%\Microsoft\Windows\Themes directory for all users. Found the answer in Joshwa's folder :

![Desktop wallpaper](/images/thm/autopsy2ze0/autopsy2ze0_7.png)
_Desktop wallpaper_

Extracted this files then opened it :

![Desktop wallpaper Extracted](/images/thm/autopsy2ze0/autopsy2ze0_8.png)
_Desktop wallpaper Extracted_

Answer : Anto Joshwa

### A user had a file on her desktop. It had a flag but she changed the flag using PowerShell. What was the first flag?
Checked the powershell history for users :

![Flag 1](/images/thm/autopsy2ze0/autopsy2ze0_9.png)
_Flag 1_

Answer : flag{HarleyQuinnForQueen}

### The same user found an exploit to escalate privileges on the computer. What was the message to the device owner?

Found the exploit.ps1 on Shreya's Desktop :

![exploit.ps1](/images/thm/autopsy2ze0/autopsy2ze0_10.png)
_exploit.ps1_

![Flag 2](/images/thm/autopsy2ze0/autopsy2ze0_11.png)
_Flag 2_

Answer : Flag{I-hacked-you}

### 2 hack tools focused on passwords were found in the system. What are the names of these tools? (alphabetical order)
I used the keyword search to solve this one. Searching for common used tools like wdigest, mimikatz, lazagne etc...

Lazagne and mimikatz was found  on the machine :

![Lazagne](/images/thm/autopsy2ze0/autopsy2ze0_12.png)
_Lazagne_

![Mimikatz](/images/thm/autopsy2ze0/autopsy2ze0_13.png)
_Mimikatz_

Answer : lazagne,mimikatz

### There is a YARA file on the computer. Inspect the file. What is the name of the author?
Searched for ".yar" keyword and found a shortcut to a file on H4S4N desktop.

![Yara file](/images/thm/autopsy2ze0/autopsy2ze0_14.png)
_Yara file_

So i moved there and found a zip mimikatz_trunk. Extracted this one and unzipped it then it contain a yara file :

![Author](/images/thm/autopsy2ze0/autopsy2ze0_15.png)
_Author_

Answer : Benjamin DELPY (gentilkiwi)

### One of the users wanted to exploit a domain controller with an MS-NRPC based exploit. What is the filename of the archive that you found? (include the spaces in your answer)
When i checked the "recent document" from extracted content i found a interesting "zerologon" name :

![zerologon](/images/thm/autopsy2ze0/autopsy2ze0_16.png)
_zerologon_

Answer : 2.2.0 20200918 Zerologon encrypted.zip