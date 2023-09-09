---
title: Red Team Threat Intel  
author: CYB3RM3
name: CYB3RM3 | Red Team Threat Intel 
date: 2022-04-02 12:52:00 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, Threat Intelligence]
---

Apply threat intelligence to red team engagements and adversary emulation.

THM Room [https://tryhackme.com/room/redteamthreatintel](https://tryhackme.com/room/redteamthreatintel)


## TASK 1 : Introduction


### Read the above and continue to the next task. 

No Answer
## TASK 2 : What is Threat Intelligence


### Read the above and continue to the next task. 

No Answer
## TASK 3 : Applying Threat Intel to the Red Team
###  Read the above and continue to the next task. 

 No Answer 
## TASK 4 : The TIBER-EU Framework


### Read the above and continue to the next task. 

No Answer.
## TASK 5 : TTP Mapping


### Read the above and use MITRE ATT&CK Navigator to answer the questions below using a Carbanak layer.

No Answer.

### How many Command and Control techniques are employed by Carbanak?

Find Carbanak on mitre : here <https://mitre-attack.github.io/attack-navigator//#layerURL=https%3A%2F%2Fattack.mitre.org%2Fgroups%2FG0008%2FG0008-enterprise-layer.json>

![Carbanak](/images/thm/redteamthreatintel/redteamthreatintel_1.png)
_Carbanak_

Answer : 2

### What signed binary did Carbanak use for defense evasion?

![Signed Binary](/images/thm/redteamthreatintel/redteamthreatintel_2.png)
_Signed Binary_

Answer : rundll32

### What Initial Access technique is employed by Carbanak?

Answer : valid account

## TASK 6 : Other Red Team Applications of CTI 


### Read the above and continue to the next task. 

No Answer.
## TASK 7 : Creating a Threat Intel Driven Campaign

### Open the provided ATT&CK Navigator layer and identify matched TTPs to the cyber kill chain. Once TTPs are identified, map them to the cyber kill chain in the static site. To complete the challenge, you must submit one technique name per kill chain section. Once the chain is complete and you have received the flag, submit it below.

![Flag](/images/thm/redteamthreatintel/redteamthreatintel_3.png)
_Flag_

Answer : THM{7HR347_1N73L_12_4w35om3}

### What web shell is APT 41 known to use?

From APT41 <https://attack.mitre.org/groups/G0096/> :

![ASPXSpy](/images/thm/redteamthreatintel/redteamthreatintel_4.png)
_ASPXSpy_

Answer : ASPXSpy

### What LOLBAS (Living Off The Land Binaries and Scripts) tool does APT 41 use to aid in file transfers?

![certutil](/images/thm/redteamthreatintel/redteamthreatintel_5.png)
_certutil_

Answer : certutil

### What tool does APT 41 use to mine and monitor SMS traffic?

![MESSAGETAP](/images/thm/redteamthreatintel/redteamthreatintel_6.png)
_MESSAGETAP_

Answer : MESSAGETAP

## TASK 8 : Conclusion 
### Read the above and continue learning! 

No Answer.