---
title: Bypassing UAC
author: CYB3RM3
name: CYB3RM3 | Bypassing UAC
date: 2022-04-03 20:51:36 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, UAC]
---

Learn common ways to bypass User Account Control (UAC) in Windows hosts.

THM Room [https://tryhackme.com/room/bypassinguac](https://tryhackme.com/room/bypassinguac)


## TASK 1 : Introduction
### Click and continue learning! 
No Answer

## TASK 2 : User Account Control (UAC)
### What is the highest integrity level (IL) available on Windows?
Answer : System

### What is the IL associated with an administrator's elevated token?
Answer : high

### What is the full name of the service in charge of dealing with UAC elevation requests?
Answer : Application Information Service

## TASK 3 : UAC: GUI based bypasses
###  What flag is returned by running the msconfig exploit? 

Viewing the process "msconfig.exe" with processHacker :

![Process Hacker](/images/thm/bypassinguac/bypassinguac_1.png)
_Process Hacker_

Then launching a IL (Integrity Level) high command prompt inherited from msconfig :

![msconfig](/images/thm/bypassinguac/bypassinguac_2.png)
_msconfig_

We have now an system command prompt and can query the flag :

![msconfig Flag](/images/thm/bypassinguac/bypassinguac_3.png)
_msconfig Flag_

Answer : THM{UAC_HELLO_WORLD}

### What flag is returned by running the azman.msc exploit?

azman.exe runs with IL high by default too :

![azman.exe](/images/thm/bypassinguac/bypassinguac_4.png)
_azman.exe_

Then in the help menu, the view source of "help topic" open notepad.exe with the same inherited IL :

![Azman Help](/images/thm/bypassinguac/bypassinguac_5.png)
_Azman Help_

![View Source](/images/thm/bypassinguac/bypassinguac_6.png)
_View Source_

![IL notepad Spawn](/images/thm/bypassinguac/bypassinguac_7.png)
_IL notepad Spawn_

We can now open cmd.exe from the System32 folder with the High IL :

![System cmd](/images/thm/bypassinguac/bypassinguac_8.png)
_System cmd_

![System cmd 2](/images/thm/bypassinguac/bypassinguac_9.png)
_System cmd 2_

And now we can query the flag :

![azman.exe Flag](/images/thm/bypassinguac/bypassinguac_10.png)
_azman.exe Flag_

Answer : THM{GUI_UAC_BYPASSED_AGAIN}

## TASK 4 : UAC: Auto-Elevating Processes
### What flag is returned by running the fodhelper exploit?

Following the explained steps we can add a specific registry key so the fodhelper.exe will check the user configuration in the registry, not the System one :

![fodhelper.exe](/images/thm/bypassinguac/bypassinguac_11.png)
_fodhelper.exe_

Then quering the flag :

![fodhelper.exe Flag](/images/thm/bypassinguac/bypassinguac_12.png)
_fodhelper.exe Flag_

Answer : THM{AUTOELEVATE4THEWIN}

## TASK 5 : UAC: Improving the Fodhelper Exploit to Bypass Windows Defender
### What flag is returned by running the fodhelper-curver exploit? 
Same process than previously, but bypassing the windows defender security :

![Bypass windefend](/images/thm/bypassinguac/bypassinguac_13.png)
_Bypass windefend_

Answer : THM{AV_UAC_BYPASS_4_ALL}

## TASK 6 : UAC: Environment Variable Expansion
### What flag is returned by running the DiskCleanup exploit? 

![DiskCleanup](/images/thm/bypassinguac/bypassinguac_14.png)
_DiskCleanup_

Answer : THM{SCHEDULED_TASKS_AND_ENVIRONMENT_VARS}

## TASK 7 : Automated Exploitation

### Click and continue learning!

No Answer.
## TASK 8 : Conclusion 
###  Click and continue learning!

No Answer.