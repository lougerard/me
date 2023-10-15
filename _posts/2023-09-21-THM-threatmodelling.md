---
title: Threat Modelling
author: CYB3RM3
name: CYB3RM3 | Threat Modelling
date: 2023-09-21 12:41:15 +0100
categories: [TryHackMe, Threats and Risks]
tags: [Threat, Vulnerability, Model, Security Engineer]
---

Building cyber resiliency and emulation capabilities through threat modelling.

THM Room : [https://tryhackme.com/room/threatmodelling](https://tryhackme.com/room/threatmodelling)


## TASK 1 Introduction
###  Let's start modelling threats! 
No Answer.

## TASK 2 Threat Modelling Overview
### What is a weakness or flaw in a system, application, or process that can be exploited by a threat?

>"Vulnerability : A weakness or flaw in a system, application, or process that may be exploited by a threat to cause harm. It may arise from software bugs, misconfiguration, or design flaws."

Answer : vulnerability

### Based on the provided high-level methodology, what is the process of developing diagrams to visualise the organisation's architecture and dependencies?

>"2. Asset Identification:
Develop diagrams of the organisation's architecture and its dependencies. It is also essential to identify the importance of each asset based on the information it handles,  such as customer data, intellectual property, and financial information"

Answer : Asset Identification

### What diagram describes and analyses potential threats against a system or application?

>"An attack tree is a graphical representation used in threat modelling to systematically describe and analyse potential threats against a system, application or infrastructure. It provides a structured, hierarchical approach to breaking down attack scenarios into smaller components. Each node in the tree represents a specific event or condition, with the root node representing the attacker's primary goal."

Answer : Attack Tree

## TASK 3 Modelling with MITRE ATT&CK
### What is the technique ID of "Exploit Public-Facing Application"?

![T1190](/images/thm/threatmodelling/threat_1.png)
_T1190_

Answer : T1190

### Under what tactic does this technique belong?
Answer : Initial Access

## TASK 4 Mapping with ATT&CK Navigator

### How many MITRE ATT&CK techniques are attributed to APT33?

![T1190 Tehcniques](/images/thm/threatmodelling/threat_2.png)
_T1190 Techniques_

Answer : 31

### Upon applying the IaaS platform filter, how many techniques are under the Discovery tactic?

![T1190 Discovery tactics](/images/thm/threatmodelling/threat_3.png)
_T1190 Discovery tactics_

Answer : 13

## TASK 5 DREAD Framework
### What DREAD component assesses the potential harm from successfully exploiting a vulnerability?

>"Damage : The potential harm that could result from the successful exploitation of a vulnerability. This includes data loss, system downtime, or reputational damage."

Answer : damage

### What DREAD component evaluates how others can easily find and identify the vulnerability?

>"Discoverability : The ease with which an attacker can find and identify the vulnerability considering whether it is publicly known or how difficult it is to discover based on the exposure of the assets (publicly reachable or in a regulated environment)."

Answer : Discoverability

### Which DREAD component considers the number of impacted users when a vulnerability is exploited?

>"Affected Users : The number or portion of users impacted once the vulnerability has been exploited."

Answer : Affected Users

## TASK 6 STRIDE Framework

### What foundational information security concept does the STRIDE framework build upon?

>"As you can see, the table above also provides what component of the CIA triad is violated. The STRIDE framework is built upon this foundational information security concept."

Answer : CIA triad

### What policy does Information Disclosure violate?

Information Disclosure	| Unauthorised access to sensitive information, such as personal or financial data. |  Confidentiality

Answer : Confidentiality

### Which STRIDE component involves unauthorised modification or manipulation of data?

Tampering |	Unauthorised modification or manipulation of data or code. | Integrity

Answer : Tampering

### Which STRIDE component refers to the disruption of the system's availability?

Denial of Service	| Disruption of the system's availability, preventing legitimate users from accessing it.	| Availability

Answer : Denial of Service

### Provide the flag for the simulated threat modelling exercise.

![exercise](/images/thm/threatmodelling/threat_4.png)
_exercise_

![exercise](/images/thm/threatmodelling/threat_5.png)
_exercise_

![exercise](/images/thm/threatmodelling/threat_6.png)
_exercise_

![exercise](/images/thm/threatmodelling/threat_7.png)
_exercise_

![exercise](/images/thm/threatmodelling/threat_8.png)
_exercise_

![exercise](/images/thm/threatmodelling/threat_9.png)
_exercise_

Answer : THM{m0d3ll1ng_w1th_STR1D3}

## TASK 7 PASTA Framework
### In which step of the framework do you break down the system into its components?

>"3.Decompose the Application
Break down the system into its components, identifying entry points, trust boundaries, and potential attack surfaces. This step also includes mapping out data flows and understanding user roles and privileges within the system."

Answer : Decompose the Application

### During which step of the PASTA framework do you simulate potential attack scenarios?

>"6.Analyse the Attacks
Simulate potential attack scenarios and evaluate the likelihood and impact of each threat. This step helps determine the risk level associated with each identified threat, allowing security teams to prioritise the most significant risks."

Answer : Analyse the Attacks

### In which step of the PASTA framework do you create an inventory of assets?

>"2.Define the Technical Scope
Create an inventory of assets, such as hardware, software, and data, and develop a clear understanding of the system's architecture, dependencies, and data flows."
Answer : Define the Technical Scope

### Provide the flag for the simulated threat modelling exercise.
Strat planning > system arch > sofware dev > information secu > start planning

![exercise 2](/images/thm/threatmodelling/threat_10.png)
_exercise 2_

![exercise 2](/images/thm/threatmodelling/threat_11.png)
_exercise 2_

![exercise 2](/images/thm/threatmodelling/threat_12.png)
_exercise 2_

![exercise 2](/images/thm/threatmodelling/threat_13.png)
_exercise 2_

![exercise 2](/images/thm/threatmodelling/threat_14.png)
_exercise 2_

![exercise 2](/images/thm/threatmodelling/threat_15.png)
_exercise 2_

![exercise 2](/images/thm/threatmodelling/threat_16.png)
_exercise 2_

![exercise 2](/images/thm/threatmodelling/threat_17.png)
_exercise 2_

Answer :  THM{c00k1ng_thr34ts_w_P4ST4}


## TASK 8 Conclusion
###  I have completed the Threat Modelling room.
No Answer.

