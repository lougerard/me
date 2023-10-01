---
title: Evading Logging and Monitoring
author: CYB3RM3
name: CYB3RM3 | Evading Logging and Monitoring
date: 2022-10-30 12:05:23 +0100
categories: [TryHackMe, RedTeam]
tags: [Evasion, SOC, RedTeam]
---

Learn how to bypass common logging and system monitoring, such as ETW, using modern tool-agnostic approaches.

THM Room [https://tryhackme.com/room/monitoringevasion](https://tryhackme.com/room/monitoringevasion)


## TASK 1 : Introduction
### Read the above and continue to the next task.
No Answer

## TASK 2 : Event Tracing
### What ETW component will build and configure sessions? 

![Controllers](/images/thm/monitoringevasion/monitoringevasion_1.png)
_Controllers_

Answer : Controllers

### What event ID logs when a user account was deleted?
Quick google search <https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4726> :

![4726](/images/thm/monitoringevasion/monitoringevasion_2.png)
_4726_

![4726](/images/thm/monitoringevasion/monitoringevasion_3.png)
_4726_

Answer : 4726

## TASK 3 : Approaches to Log Evasion
###  How many total events can be used to track event tampering?  

 "Assuming an attacker did destroy all of the logs before they were forwarded, or if they were not forwarded, how would this raise an alert? An attacker must first consider environment integrity; if no logs originate from a device, that can present serious suspicion and lead to an investigation. Even if an attacker did control what logs were removed and forwarded, defenders could still track the tampering"

![Event ID](/images/thm/monitoringevasion/monitoringevasion_4.png)
_Event ID_

Answer : 4

### What event ID logs when the log file was cleared?

![Event ID 104](/images/thm/monitoringevasion/monitoringevasion_5.png)
_Event ID 104_

Answer : 104

## TASK 4 : Tracing Instrumentation
### Read the above and continue to the next task. 
No Answer.

## TASK 5 : Reflection for Fun and Silence
### What reflection assembly is used? 

![PSEtwLogProvider](/images/thm/monitoringevasion/monitoringevasion_6.png)
_PSEtwLogProvider_

Answer : PSEtwLogProvider

### What field is overwritten to disable ETW?

![m_enabled](/images/thm/monitoringevasion/monitoringevasion_7.png)
_m enabled_

When we try this in the provided target machine, we can see that our command "whoami" logs no more events.

![m_enabled](/images/thm/monitoringevasion/monitoringevasion_8.png)
_m enabled_

Answer : m_enabled

## TASK 6 : Patching Tracing Functions
### What is the base address for the ETW security check before it is patched? 
From the disassembly of the function "EtwEventWrite" we get the base address :

```console
779f2459 33cc		###  xor	ecx, esp
779f245b e8501a0100	###  call	ntdll!_security_check_cookie
779f2460 8be5		###  mov	esp, ebp
779f2462 5d		###  pop	ebp
779f2463 c21400		###  ret	14h
```
{: .nolineno }

Answer : 779f245b

### What is the non-delimited opcode used to patch ETW for x64 architecture?

 "To neuter the function, an attacker can write the opcode bytes of ret14h, c21400 to memory to patch the function."

Answer : c21400

## TASK 7 : Providers via Policy

### How many total events are enabled through script block and module providers? 

![Events Enabled](/images/thm/monitoringevasion/monitoringevasion_9.png)
_Events Enabled_

Answer : 2

### What event ID will log script block execution?
From previous question : 4104

Answer : 4104

## TASK 8 : Group Policy Takeover
### What event IDs can be disabled using this technique? (lowest to highest separated by a comma) 

![Events disabled](/images/thm/monitoringevasion/monitoringevasion_10.png)
_Events disabled_

Answer : 4103,4104

### What provider setting controls 4104 events?

Answer : EnableScriptBlockLogging

## TASK 9 : Abusing Log Pipeline
### What type of logging will this method prevent? 

 "Within PowerShell, each module or snap-in has a setting that anyone can use to modify its logging functionality. From the Microsoft docs, “When the LogPipelineExecutionDetails property value is TRUE ($true), Windows PowerShell writes cmdlet and function execution events in the session to the Windows PowerShell log in Event Viewer.” An attacker can change this value to $false in any PowerShell session to disable a module logging for that specific session. The Microsoft docs even note the ability to disable logging from a user session, “To disable logging, use the same command sequence to set the property value to FALSE ($false).”"

Answer : module logging

### What target module will disable logging for all Microsoft utility modules?

![Microsoft.PowerShell.Utility](/images/thm/monitoringevasion/monitoringevasion_11.png)
_Microsoft.PowerShell.Utility_

Answer : Microsoft.PowerShell.Utility

## TASK 10 : Real World Scenario
### Enter the flag obtained from the desktop after executing the binary. 

![Executing binary](/images/thm/monitoringevasion/monitoringevasion_12.png)
_Executing binary_

After many tries, it seems that something goes wrong with the room, so i decide to search strings in the exe file and found the flag not obfuscated in it :

```console
PS C:\Users\Administrator\Desktop> Select-String -Path .\agent.exe -Pattern 'T.*H.*M.*{.*}' -AllMatches | % {$_.Matches}


Groups   : {0}
Success  : True
Name     : 0
Captures : {0}
Index    : 67
Length   : 261
Value    : t - W i n d o w s - S y s m o n / O p e r a t i o n a l '* [ S y s t e m / E v e n t I D = 1 ]  =T r a f f i c   h a l t e d ,   y o u   g o t
            c a u g h t  5E r r o r   r e a d i n g   t h e   l o g : { 0 }  1T H M { 5 1 l 3 n 7 _ l 1 k 3 _ 4 _ 5 n 4 k 3 }
```
{: .nolineno }

Answer : THM{51l3n7_l1k3_4_5n4k3}

## TASK 11 : Conclusion   
### Read the above and continue learning! 
No Anwser.