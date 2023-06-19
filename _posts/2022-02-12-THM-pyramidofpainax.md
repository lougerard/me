---
title: Pyramid Of Pain 
author: CYB3RM3
name: CYB3RM3 | Pyramid Of Pain 
date: 2022-02-12 14:29:59 +0100
categories: [TryHackMe, SOC]
tags: [Pyramid of Pain]
---

Learn what is the Pyramid of Pain and how to utilize this model to determine the level of difficulty it will cause for an adversary to change the indicators associated with them, and their campaign. 

THM Room [https://tryhackme.com/room/pyramidofpainax](https://tryhackme.com/room/pyramidofpainax)



## TASK 1 : Introduction
### Read the above. 
No Answer

## TASK 2 : Hash Values (Trivial)
### Provide the ransomware name for the hash '63625702e63e333f235b5025078cea1545f29b1ad42b1e46031911321779b6be' using open-source lookup tools 
Using online tool like Virustotal <https://www.virustotal.com/gui/home/upload> :

![Hash](/images/thm/pyramidofpainax/pyramidofpainax_1.png)
_Hash_

Answer : Conti

## TASK 3 : IP Address (Easy)
###  What is the ASN for the third IP address observed? 
Using the link to any.run, it give me the information.

![ASN Any.Run](/images/thm/pyramidofpainax/pyramidofpainax_2.png)
_ASN from Any.Run_

I get the same info first by checking the IP in Hurricane Electric <https://bgp.he.net/AS34011> :

![ASN Hurricane Electric](/images/thm/pyramidofpainax/pyramidofpainax_3.png)
_ASN from Hurricane Electric_

Answer : Host Europe GmbH

### What is the domain name associated with the first IP address observed?

![Domain name](/images/thm/pyramidofpainax/pyramidofpainax_4.png)
_Domain name_

Answer : craftingalegacy.com

## TASK 4 : Domain Names (Simple)
### Go to this report <https://app.any.run/tasks/a66178de-7596-4a05-945d-704dbf6b3b90> on app.any.run and provide the first malicious URL request you are seeing, you will be using this report to answer the remaining questions of this task.
The first malicious URL is the first DNS request :

![Malicious URL](/images/thm/pyramidofpainax/pyramidofpainax_5.png)
_Malicious URL_

Answer : craftingalegacy.com

### What term refers to an address used to access websites?
The translation for human readable of IP address : Domain Name

Answer : Domain Name

### What type of attack uses Unicode characters in the domain name to imitate the a known domain?

![Attack type](/images/thm/pyramidofpainax/pyramidofpainax_6.png)
_Attack type_

Answer : Punycode attack

### Provide the redirected website for the shortened URL using a preview: https://tinyurl.com/bw7t8p4u

Let's check which website this URL redirect to :

```console
ME@PC:~$ curl https://tinyurl.com/bw7t8p4u
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="refresh" content="0;url='https://tryhackme.com/'" />

        <title>Redirecting to https://tryhackme.com/</title>
    </head>
    <body>
        Redirecting to <a href="https://tryhackme.com/">https://tryhackme.com/</a>.
    </body>
</html>ME@PC:~$
```
{: .nolineno }

Answer : https://tryhackme.com/

## TASK 5 : Host Artifacts (Annoying)
### What is the suspicious IP the victim machine tried to connect to in the screenshot above?  

![Suspicious IP](/images/thm/pyramidofpainax/pyramidofpainax_7.png)
_Suspicious IP_

Answer : 35.214.215.33

### Use the tools introduced in task 2 and provide the name of the malware associated with the IP address
Searching for the hash in online tool Virustotal :

![Hash](/images/thm/pyramidofpainax/pyramidofpainax_8.png)
_Hash_

![Malware name](/images/thm/pyramidofpainax/pyramidofpainax_9.png)
_Malware name_

Answer : emotet

### Using your OSINT skills, what is the name of the malicious document associated with the dropped binary?

Cheking informations given and the name of the binary i searched the MD5 on VirusTotal :

![Malicious document](/images/thm/pyramidofpainax/pyramidofpainax_10.png)
_Malicious document_

Answer : G_jugk.Exe

### Use your OSINT skills and provide the name of the malicious document associated with the dropped binary 

Checking for that binary on google  (hint), i found an any.run report <https://any.run/report/e2d2ebafc33d7c7819f414031215c3669bccdfb255af3cbe0177b2c601b0e0cd/90b76d7b-8df6-43c5-90ec-d4bbcfb4fa19> :

![Googling malicious document](/images/thm/pyramidofpainax/pyramidofpainax_11.png)
_Googling malicious document_

This gives me the name of the file ossociated with the binary :

![Malicious document filename](/images/thm/pyramidofpainax/pyramidofpainax_12.png)
_Malicious document filename_

Answer : CMO-100120 CDW-102220.doc

## TASK 6 : Network Artifacts (Annoying)
### What browser uses the User-Agent string shown in the screenshot above? 

![Browser](/images/thm/pyramidofpainax/pyramidofpainax_13.png)
_Browser_

Answer : internet explorer

### How many POST requests are in the screenshot from the pcap file?

![POST](/images/thm/pyramidofpainax/pyramidofpainax_14.png)
_POST_

Answer : 6

## TASK 7 : Tools (Challenging)
### Provide the method used to determine similarity between the files  

"Fuzzy hashing is also a strong weapon against the attacker's tools. Fuzzy hashing helps you to perform similarity analysis - match two files with minor differences based on the fuzzy hash values. One of the examples of fuzzy hashing is the usage of SSDeep <https://ssdeep-project.github.io/ssdeep/index.html>; on the SSDeep official website, you can also find the complete explanation for fuzzy hashing. "

Answer : Fuzzy hashing

### Provide the alternative name for fuzzy hashes without the abbreviation

Per SSDeep <https://ssdeep-project.github.io/ssdeep/index.html>:

![SSDeep](/images/thm/pyramidofpainax/pyramidofpainax_15.png)
_SSDeep_

Answer : context triggered piecewise hashes

## TASK 8 : TTPs (Tough)
### Navigate to ATT&CK Matrix webpage. How many techniques fall under the Exfiltration category? 
Per MITRE | ATT&CK <https://attack.mitre.org/> main page :

![MITRE](/images/thm/pyramidofpainax/pyramidofpainax_16.png)
_MITRE_

Answer : 9

### Chimera is a China-based hacking group that has been active since 2018. What is the name of the commercial, remote access tool they use for C2 beacons and data exfiltration?
I looked up for Chimera in the search bar then searched for exfiltration on the Chimera page result :

![C2](/images/thm/pyramidofpainax/pyramidofpainax_17.png)
_C2_

Answer : Cobalt Strike

## TASK 9 : Practical: The Pyramid of Pain
### Complete the static site. 
Flag not poping with right answer : looked at forum = "Seems that Task 9 is having some issues"

No Answer.

## TASK 10 : Conclusion 
### Read the above.

No Answer.