---
title: Red Team Engagements
author: CYB3RM3
name: CYB3RM3 | Red Team Engagements 
date: 2022-02-19 17:24:46 +0100
categories: [TryHackMe, Red Team Fundamentals]
tags: [Red Team, Engagements]
---

Learn the steps and procedures of a red team engagement, including planning, frameworks, and documentation.

THM Room [https://tryhackme.com/room/redteamengagements](https://tryhackme.com/room/redteamengagements)


## TASK 1 : Introduction
### Read the above and continue to the next task. 
No Answer

## TASK 2 : Defining Scope and Objectives
### Read the example client objectives and answer the questions below. 
No Answer

### Below is an example of the client objectives of a mature organization with a strong security posture.
Example 1 - Global Enterprises:

Objectives:

    Identify system misconfigurations and network weaknesses.
        Focus on exterior systems.
    Determine the effectiveness of endpoint detection and response systems.
    Evaluate overall security posture and response.
        SIEM and detection measures.
        Remediation.
        Segmentation of DMZ and internal servers.

Use of white cards is permitted depending on downtime and length.
    Evaluate the impact of data exposure and exfiltration.

Scope:

    System downtime is not permitted under any circumstances.
        Any form of DDoS or DoS is prohibited.
        Use of any harmful malware is prohibited; this includes ransomware and other variations.
    Exfiltration of PII is prohibited. Use arbitrary exfiltration data.
    Attacks against systems within 10.0.4.0/22 are permitted.
    Attacks against systems within 10.0.12.0/22 are prohibited.
    Bean Enterprises will closely monitor interactions with the DMZ and critical/production systems.
        Any interaction with "*.bethechange.xyz" is prohibited.
        All interaction with "*.globalenterprises.thm" is permitted.

No Answer

### What CIDR range is permitted to be attacked?
Answer : 10.0.4.0/22

### Is the use of white cards permitted? (Y/N)
Answer : y

### Are you permitted to access "*.bethechange.xyz?" (Y/N)
Answer : n

## TASK 3 : Rules of Engagement
### Download the sample rules of engagement from the task files. Once downloaded, read the sample document and answer the questions below.

No Answer.

### How many explicit restriction are specified?

![Explicit Restriction](/images/thm/redteamengagements/redteamengagements_1.png)
_Explicit Restriction_

Answer : 3

### What is the first access type mentioned in the document?

![Access](/images/thm/redteamengagements/redteamengagements_2.png)
_Access_

Answer : phishing

### Is the red team permitted to attack 192.168.1.0/24? (Y/N)
Answer : n

## TASK 4 : Campaign Planning
### Read the above and move on to engagement documentation. 
No Answer.

## TASK 5 : Engagement Documentation
### Read the above and move on to the upcoming engagement specific tasks. 
No Answer.

## TASK 6 : Concept of Operations
### Read the example CONOPS and answer the questions below.

No Answer.

### Based on customer security posture and maturity, the TTP of the threat group: FIN6, will be employed throughout the engagement.

No Answer.

### How long will the engagement last?

![Engagement duration](/images/thm/redteamengagements/redteamengagements_3.png)
_Engagement duration_

Answer : 1 month

### How long is the red cell expected to maintain persistence?

![Persistence duration](/images/thm/redteamengagements/redteamengagements_4.png)
_Persistence duration_

Answer : 3 weeks

### Answer : lsaiso.exe

![Tool](/images/thm/redteamengagements/redteamengagements_5.png)
_Tool_

Answer : Cobalt Strike

## TASK 7 : Resource Plan

### Navigate to the "View Site"  button and read the provided resource plan. Once complete, answer the questions below.

![Resource Plan](/images/thm/redteamengagements/redteamengagements_6.png)
_Resource Plan_

No Answer.

### When will the engagement end?
Answer : 11/14/2021

### What is the budget the red team has for AWS cloud cost?
Answer : $1000

### Are there any miscellaneous requirements for the engagement? (Y/N)
Answer : n

## TASK 8 : Operations Plan
### Navigate to the "View Site"  button and read the provided operations plan. Once complete, answer the questions below. 

![Operations Plan](/images/thm/redteamengagements/redteamengagements_7.png)
_Operations Plan_

No Answer.

### What phishing method will be employed during the initial access phase?
Answer : spearphishing

### What site will be utilized for communication between the client and red cell?
Answer :  vectr.io

### If there is a system outage, the red cell will continue with the engagement. (T/F)
Answer : F

## TASK 9 : Mission Plan
### Navigate to the "View Site"  button and read the provided mission plan. Once complete, answer the questions below. 

![Mission Plan](/images/thm/redteamengagements/redteamengagements_8.png)
_Mission Plan_

No Answer.

### When will the phishing campaign end? (mm/dd/yyyy)
Answer : 10/23/2021

### Are you permitted to attack 10.10.6.78? (Y/N)
Answer : N

### When a stopping condition is encountered, you should continue working and determine the solution yourself without a team lead. (T/F)
Answer : F

## TASK 10 : Conclusion 
### Read the above and continue learning! 
No Answer.
