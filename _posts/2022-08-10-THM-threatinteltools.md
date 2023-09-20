---
title: Threat Intelligence Tools 
author: CYB3RM3
name: CYB3RM3 | Threat Intelligence Tools 
date: 2022-08-10 12:07:22 +0100
categories: [TryHackMe, Red Team]
tags: [Threat Intel, Tools, Phishing]
---

Explore different OSINT tools used to conduct security threat assessments and investigations.

THM Room [https://tryhackme.com/room/threatinteltools](https://tryhackme.com/room/threatinteltools)


## TASK 1 : Room Outline
### Read the description! Continue to the next task. 
No Answer

## TASK 2 : Threat Intelligence
### I've read on Threat Intel and the classifications 
No Answer

## TASK 3 : UrlScan.io
###  What is TryHackMe's Cisco Umbrella Rank? 
Looking on the provided screenshot : 

![urlscan.io](/images/thm/threatinteltools/threatinteltool_0.png)
_urlscan.io_

Answer : 345612

### How many domains did UrlScan.io identify?
Answer : 13

### What is the main domain registrar listed?
Answer : NAMECHEAP INC

### What is the main IP address identified?
Answer : 2606:4700:10::ac43:1b0a

## TASK 4 : Abuse.ch
### The IOC 212.192.246.30:5555 is linked to which malware on ThreatFox?

Going to ThreatFox website <https://threatfox.abuse.ch/export/> to look for all data IP:PORT :

![ThreatFox](/images/thm/threatinteltools/threatinteltool_2.png)
_ThreatFox_

then exported then data :

![Exported JSON](/images/thm/threatinteltools/threatinteltool_3.png)
_Exported JSON_

Unzipping the downloaded zip file, we get a JSON file in which we can look for our IP:PORT (212.192.246.30:5555)

![Malware Katana](/images/thm/threatinteltools/threatinteltool_4.png)
_Malware Katana_

Answer : Katana

### Which malware is associated with the JA3 Fingerprint 51c64c77e60f3980eea90869b68c58a8 on SSL Blacklist?

We can search for this on SSL Blaclist <https://sslbl.abuse.ch/ja3-fingerprints/> and copy paste the fingerprint in the search bar :

![SSL Blacklist](/images/thm/threatinteltools/threatinteltool_5.png)
_SSL Blacklist_

Answer : Dridex

### From the statistics page on URLHaus, what malware-hosting network has the ASN number AS14061?

Navigating to URLHaus <https://urlhaus.abuse.ch/> in the statistics tab :

![URLHaus](/images/thm/threatinteltools/threatinteltool_6.png)
_URLHaus_

![DIGITALOCEAN](/images/thm/threatinteltools/threatinteltool_7.png)
_DIGITALOCEAN_

We found the AS14061 as DIGITALOCEAN-ASN

Answer : DIGITALOCEAN-ASN

### Which country is the botnet IP address 178.134.47.166 associated with according to FeodoTracker?

Visitting FeodoTracker website <https://feodotracker.abuse.ch/> in the browse tab :

![FEODO](/images/thm/threatinteltools/threatinteltool_8.png)
_FEODO_

We can search for our requested IP address to find our answer :

![FEODO](/images/thm/threatinteltools/threatinteltool_9.png)
_FEODO_

Answer : Georgia
## TASK 5 : PhishTool
### What organisation is the attacker trying to pose as in the email?

Opening the first email we can see a phishing email obout LinkedIn :

![LinkedIn](/images/thm/threatinteltools/threatinteltool_10.png)
_LinkedIn_

Answer : LinkedIn

### What is the senders email address?

From above screenshot, we can see the sender email address.

Answer : darkabutla@sc500.whpservers.com

### What is the recipient's email address?

From above screenshot, we can see the recepient email address.

Answer : cabbagecare@hotsmail.com

### What is the Originating IP address? Defang the IP address.

We can search the originated IP address of the sender in the source of the email :

![email1](/images/thm/threatinteltools/threatinteltool_11.png)
_email1_

Answer : 204[.]93[.]183[.]11

### How many hops did the email go through to get to the recipient?

From the source in the obove screenshot, we can count the number of hops with the "received: " tag.

Answer : 4

## TASK 6 : Cisco Talos Intelligence
### What is the listed domain of the IP address from the previous task?
We can search for the sender IP address in the Talos Reputation Center <https://talosintelligence.com/reputation_center> to find the domain :

![Talos](/images/thm/threatinteltools/threatinteltool_12.png)
_Talos_

Answer : scnet.net

### What is the customer name of the IP address?

The customer name can be found in the Whois tab :

![Talos Whois](/images/thm/threatinteltools/threatinteltool_13.png)
_Talos Whois_

![CustName](/images/thm/threatinteltools/threatinteltool_14.png)
_CustName_

Answer : Complete Web Reviews

## TASK 7 : Scenario 1
### How many instances of services.exe should be running on a Windows system? 
Opening the email :

![email2](/images/thm/threatinteltools/threatinteltool_15.png)
_email2_

Answer : chris.lyons@supercarcenterdetroit.com

### From Talos Intelligence, the attached file can also be identified by the Detection Alias that starts with an H...

To find the alias starting with an "H", we can search for the SHA256 of the file attached in the email in the Talos File Reputation <https://talosintelligence.com/talos_file_reputation>:

Firstly, retreive the SHA256 from the email attached file's properties :

![email2 attachment SHA256](/images/thm/threatinteltools/threatinteltool_16.png)
_email2 attachment SHA256_

Then search this digest in the Talos reputation center :

![email2 SHA256 Search](/images/thm/threatinteltools/threatinteltool_17.png)
_email2 SHA256 Search_

![Worm.Gen](/images/thm/threatinteltools/threatinteltool_18.png)
_Worm.Gen_

Answer : HIDDENEXT/Worm.Gen

## TASK 8 : Scenario 2
### What is the name of the attachment on Email3.eml? 
In the email, we can see the attached file name :

![email3](/images/thm/threatinteltools/threatinteltool_19.png)
_email3_

Answer : Sales_Receipt 5606.xls

### What malware family is associated with the attachment on Email3.eml?

In the same way for scenario 1, we can get the SHA256 from the file :

![email3 SHA256](/images/thm/threatinteltools/threatinteltool_20.png)
_email3 SHA256_

Then search for this one in the Talos File Reputation :

![dridex](/images/thm/threatinteltools/threatinteltool_21.png)
_dridex_

Answer : dridex

## TASK 9 : Conclusion

###  Read the above and completed the room 

No Answer.