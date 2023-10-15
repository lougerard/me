---
title: Active Directory Hardening
author: CYB3RM3
name: CYB3RM3 | Active Directory Hardening
date: 2023-09-24 11:51:58 +0100
categories: [TryHackMe, Security Engineer]
tags: [AD, Active Directory, Hardening, Intro]
---

To learn basic concepts regarding Active Directory attacks and mitigation measures.

THM Room : [https://tryhackme.com/room/activedirectoryhardening](https://tryhackme.com/room/activedirectoryhardening)


## TASK 1 Introduction
###  I can successfully connect with the AD machine. 
No Answer.

## TASK 2 Understanding General Active Directory Concepts
### What is the root domain in the attached AD machine? 

![Root domain](/images/thm/activedirectoryhardening/ActiveDirectoryHardening_1.png)
_Root domain_

Answer : tryhackme.loc

## TASK 3 Securing Authentication Methods

### Change the Group Policy Setting in the VM, so it does not store the LAN Manager hash on the next password change.

![GPO](/images/thm/activedirectoryhardening/ActiveDirectoryHardening_2.png)
_GPO_

No Answer.

### What is the default minimum password length (number of characters) in the attached VM?

![Default Password Length](/images/thm/activedirectoryhardening/ActiveDirectoryHardening_3.png)
_Default Password Length_

Answer : 7

## TASK 4 Implementing Least Privilege Model
### Computers and Printers must be added to Tier 0 - yea/nay?

Computers and printers are non trustable.

Answer : NAY

### Suppose a vendor arrives at your facility for a 2-week duration task. Being a System Administrator, you should create a high privilege account for him - yea/nay?

He should always ask when elevated rights are needed for a member of system administrators.

Answer : NAY

## TASK 5 Microsoft Security Compliance Toolkit

### Find and open BaselineLocalInstall script in PowerShell editor - Can you find the flag?

```powershell
PS C:\Users\Administrator\Desktop\Scripts\Windows Server 2019 Security Baseline\Local_Script> cat .\BaselineLocalInstall.ps1 | findstr "Flag"
Flag : THM{00001}
```
{: .nolineno }

Aswer : THM{00001}

### Find and open MergePolicyRule script (Policy Analyser) in PowerShell editor - Can you find the flag?

```powershell
PS C:\Users\Administrator\Desktop\Scripts\PolicyAnalyzer\PolicyAnalyzer_40> cat .\Merge-PolicyRules.ps1 |findstr "Flag"
Flag : {THM00191}
```
{: .nolineno }

Aswer : {THM00191}

## TASK 6 Protecting Against Known Attacks
### Does Kerberoasting utilise an offline-attack scheme for cracking encrypted passwords - yea/nay?

"Kerberoasting is a common and successful post-exploitation technique for attackers to get privileged access to AD. The attacker exploits Kerberos Ticket Granting Service (TGS) to request an encrypted password, and then the attacker cracks it offline through various brute force techniques. These attacks are difficult to detect as the request is made through an approved user, and no unusual traffic pattern is generated during this process. You can prevent the attack by ensuring an additional layer of authentication through MFA or by frequent and periodic Kerberos Key Distribution Centre (KDC) service account password reset. You can learn more about the attack here."

Answer : YEA

### As per the generated report, how many users have the same password as aaron.booth?

![Same Passwords](/images/thm/activedirectoryhardening/ActiveDirectoryHardening_4.png)
_Same Passwords_

Answer : 186 


## TASK 7 Windows Active Directory Hardening Cheat Sheet
###  I have completed the room. 
No Answer.
