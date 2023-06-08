---
title:  MAL - Malware Introductory 
author: CYB3RM3
name: CYB3RM3 | MAL - Malware Introductory 
date: 2022-01-27 11:08:05 +0100
categories: [TryHackMe, Malware]
tags: [Malware, Malware analysis]
---

The start of a series of rooms covering Malware Analysis...

THM Room [https://tryhackme.com/room/malmalintroductory](https://tryhackme.com/room/malmalintroductory)



## TASK 1 : What is the Purpose of Malware Analysis?
### Ah, now I kinda understand...
No Answer

## TASK 2 : Understanding Malware Campaigns
### What is the famous example of a targeted attack-esque Malware that targeted Iran?
Just googling the info if you don't remember it ! Per Wikipedia :

![Stuxnet](/images/thm/malmalintroductory/malmalintroductory_1.png)
_Stuxnet_

Answer : Stuxnet

### What is the name of the Ransomware that used the Eternalblue exploit in a "Mass Campaign" attack?
Idem, per Wikipedia <https://en.wikipedia.org/wiki/EternalBlue> :

![WannaCry](/images/thm/malmalintroductory/malmalintroductory_2.png)
_WannaCry_

Answer : WannaCry

## TASK 3 : Identifying if a Malware Attack has Happened
###  Name the first essential step of a Malware Attack?
Answer : delivery

### Now name the second essential step of a Malware Attack?
Answer : execution

### What type of signature is used to classify remnants of infection on a host?
Answer : host-based signatures

### What is the name of the other classification of signature used after a Malware attack?
Answer : Network-based signatures

## TASK 4 : Static Vs. Dynamic Analysis
### I understand the two broad categories employed when analysing potential malware!
No Answer.

## TASK 5 : Discussion of Provided Tools & Their Uses
### Lets proceed
No Answer.

## TASK 6 : Connecting to the Windows Analysis Environment (Deploy)
### I've logged in!
No Answer.

## TASK 7 : Obtaining MD5 Checksums of Provided Files
### The MD5 Checksum of aws.exe 
Right click on the exe file then properties and File Hashes tab. 

Answer : D2778164EF643BA8F44CC202EC7EF157

### The MD5 Checksum of Netlogo.exe
Answer : 59CB421172A89E1E16C11A428326952C

### The MD5 Checksum of vlc.exe
Answer : 5416BE1B8B04B1681CB39CF0E2CAAD9F

## TASK 8 : Now lets see if the MD5 Checksums have been analysed before
### Does Virustotal report this MD5 Checksum / file aws.exe as malicious? (Yay/Nay)
Answer : NAY

### Does Virustotal report this MD5 Checksum / file Netlogo.exe as malicious? (Yay/Nay)
Answer : NAY

### Does Virustotal report this MD5 Checksum / file vlc.exe as malicious? (Yay/Nay)
Answer : NAY

## TASK 9 : Identifying if the Executables are obfuscated / packed
###  What does PeID propose 1DE9176AD682FF.dll being packed with? 

![PeID](/images/thm/malmalintroductory/malmalintroductory_3.png)
_PeID_

Answer : Microsoft Visual C++ 6.0 DLL

### What does PeID propose AD29AA1B.bin being packed with?
Answer : Microsoft Visual C++ 6.0

## TASK 10 : What is Obfuscation / Packing?
### What packer does PeID report file "6F431F46547DB2628" to be packed with?

![Packer](/images/thm/malmalintroductory/malmalintroductory_4.png)
_Packer_

Answer : FSG 1.0 -> dulek/xt

## TASK 11 : Visualising the Differences Between Packed & Non-Packed Code
### Cursed obfuscation!
No Answer.

## TASK 12 : Introduction to Strings
### What is the URL that is outputted after using "strings"

![strings](/images/thm/malmalintroductory/malmalintroductory_5.png)
_strings_

Answer : practicalmalwareanalysis.com

### How many unique "Imports" are there?

![Unique imports](/images/thm/malmalintroductory/malmalintroductory_6.png)
_Unique imports_

Answer : 5

## TASK 13 : Introduction to Imports
### How many references are there to the library "msi" in the "Imports" tab of IDA Freeware for "install.exe" 

![Imports](/images/thm/malmalintroductory/malmalintroductory_7.png)
_Imports_

Answer : 9

## TASK 14 : Practical Summary 
### What is the MD5 Checksum of the file?
To answer this, click properties of the exe file then go to the file hash tab. You can also use the "md5sum <file>" function in linux terminal if you have access to.

![ComplexCalculator](/images/thm/malmalintroductory/malmalintroductory_8.png)
_ComplexCalculator_

Answer : F5BD8E6DC6782ED4DFA62B8215BDC429

### Does Virustotal report this file as malicious? (Yay/Nay)

![Virustotal](/images/thm/malmalintroductory/malmalintroductory_9.png)
_Virustotal_

Answer : YAY

### Output the strings using Sysinternals "strings" tool.
### What is the last string outputted?

Open cmd in the folder where sysinternalsSuite String.exe file is then :

```console
strings.exe "C:\Users\Analysis\Desktop\Tasks\Task 14\ComplexCalculator.exe"
[...]
>&>P>_>
?9?H?Q?^?v?
0h1l1p1t1
2 2
d:h:
```
{: .nolineno }

Answer : d:h:

### What is the output of PeID when trying to detect what packer is used by the file?

![PeID](/images/thm/malmalintroductory/malmalintroductory_10.png)
_PeID_

Answer : Nothing found