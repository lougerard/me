---
title: Sysmon
author: CYB3RM3
name: CYB3RM3 | Sysmon
date: 2022-01-07 00:05:22 +0100
categories: [TryHackMe, Windows]
tags: [Windows, Sysmon]
---

Learn how to utilize Sysmon to monitor and log your endpoints and environments.

THM Room [https://tryhackme.com/room/sysmon](https://tryhackme.com/room/sysmon)


## TASK 1 : Introduction
### Complete the prerequisites listed above and jump into task 2. 
No Answer

## TASK 2 : Sysmon Overview
### Read the above and become familiar with the Sysmon Event IDs. 
no Answer.

## TASK 3 : Installing and Preparing Sysmon
###  Deploy the machine and start Sysmon.  
No ANswer.

## TASK 4 : Cutting out the Noise
### Read the above and practice filtering events. 
No Answer.

### How many event ID 3 events are in C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Filtering.evtx?
We need to use the filter '*/System/EventID=3' and count the result with the Measure-Object function in Powershell :

```powershell
PS C:\Users\THM-Analyst\Desktop\Tools\Sysmon> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Filtering.evtx -FilterXPath '*/System/EventID=3' | Measure-Object

Count : 73591
Average :
[...]
```
{: .nolineno }

Answer : 73,591

### What is the UTC time created of the first network event in C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Filtering.evtx?
We need to search for the 1st event (-Oldest) of EventID=3 :

```powershell
PS C:\Users\THM-Analyst\Desktop\Tools\Sysmon> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Filtering.evtx -FilterXPath '*/System/EventID=3'-Oldest -MaxEvents 1 | fl


TimeCreated  : 1/6/2021 1:35:52 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 3
Message      : Network connection detected:
               RuleName: RDP
               UtcTime: 2021-01-06 01:35:50.464
               ProcessGuid: {6cd1ea62-b76c-5fef-1100-00000000f500}
               ProcessId: 920
               Image: C:\Windows\System32\svchost.exe
               User: NT AUTHORITY\NETWORK SERVICE
               Protocol: tcp
               Initiated: false
               SourceIsIpv6: false
               SourceIp: 95.141.198.234
               SourceHostname: -
               SourcePort: 20032
               SourcePortName: -
               DestinationIsIpv6: false
               DestinationIp: 10.10.98.207
               DestinationHostname: THM-SOC-DC01.thm.soc
               DestinationPort: 3389
               DestinationPortName: ms-wbt-server
```
{: .nolineno }

Answer : 2021-01-06 01:35:50.464

## TASK 5 : Hunting Metasploit

### Read the above and practice hunting Metasploit with the provided event file. 
Some commands i tried :

```powershell
PS C:\Users\THM-Analyst\Desktop\Tools\Sysmon> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Hunting_Metasploit.evtx -FilterXPath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=4444'

   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
1/5/2021 2:21:32 AM              3 Information      Network connection detected:...



PS C:\Users\THM-Analyst\Desktop\Tools\Sysmon> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Hunting_Metasploit.evtx -FilterXPath '*/EventData/Data=4444'

   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
1/5/2021 2:21:32 AM              3 Information      Network connection detected:...
1/5/2021 1:58:26 AM              1 Information      Process Create:...


PS C:\Users\THM-Analyst\Desktop\Tools\Sysmon> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Hunting_Metasploit.evtx -FilterXPath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=5555'

   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
1/5/2021 2:21:32 AM              3 Information      Network connection detected:...
```
{: .nolineno }

No Answer.

## TASK 6 : Detecting Mimikatz
### Read the above and practice detecting Mimikatz with the provided evtx.

```powershell
PS C:\Windows\system32> Get-WinEvent -Path "C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Hunting_Mimikatz.evtx" -FilterXPath '*/System/EventID=10 and */EventData/Data[@Name="TargetImage"] and */EventData/Data="C:\Windows\system32\lsass.exe"' | fl


TimeCreated  : 1/5/2021 3:22:52 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 10
Message      : Process accessed:
               RuleName: -
               UtcTime: 2021-01-05 03:22:52.581
               SourceProcessGUID: {6cd1ea62-db8c-5ff3-8b07-00000000f500}
               SourceProcessId: 3604
               SourceThreadId: 4292
               SourceImage: C:\Users\THM-Threat\Downloads\mimikatz.exe
               TargetProcessGUID: {6cd1ea62-b769-5fef-0c00-00000000f500}
               TargetProcessId: 744
               TargetImage: C:\Windows\system32\lsass.exe
               GrantedAccess: 0x1010
               CallTrace: C:\Windows\SYSTEM32\ntdll.dll+9f644|C:\Windows\System32\KERNELBASE.dll+212ae|C:\Users\THM-Thr
               eat\Downloads\mimikatz.exe+bcbda|C:\Users\THM-Threat\Downloads\mimikatz.exe+bcfb1|C:\Users\THM-Threat\Do
               wnloads\mimikatz.exe+bcb19|C:\Users\THM-Threat\Downloads\mimikatz.exe+84f28|C:\Users\THM-Threat\Download
               s\mimikatz.exe+84d60|C:\Users\THM-Threat\Downloads\mimikatz.exe+84a93|C:\Users\THM-Threat\Downloads\mimi
               katz.exe+c39a9|C:\Windows\System32\KERNEL32.DLL+17974|C:\Windows\SYSTEM32\ntdll.dll+5a0b1
```
{: .nolineno }

No Answer.

## TASK 7 : Hunting Malware
### Read the Above and practice hunting rats and C2 servers with back connect ports.  

```powershell
PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Hunting_Rats.evtx -FilterXPath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=8080' -MaxEvents 1 | fl


TimeCreated  : 1/5/2021 4:44:35 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 3
Message      : Network connection detected:
               RuleName: -
               UtcTime: 2021-01-05 04:44:33.963
               ProcessGuid: {6cd1ea62-ed72-5ff3-c107-00000000f500}
               ProcessId: 6200
               Image: C:\Users\THM-Threat\Downloads\bigbadrat.exe
               User: THM\THM-Threat
               Protocol: tcp
               Initiated: true
               SourceIsIpv6: false
               SourceIp: 10.10.98.207
               SourceHostname: THM-SOC-DC01.thm.soc
               SourcePort: 52859
               SourcePortName: -
               DestinationIsIpv6: false
               DestinationIp: 10.13.4.34
               DestinationHostname: ip-10-13-4-34.eu-west-1.compute.internal
               DestinationPort: 8080
               DestinationPortName: -
```
{: .nolineno }

No Answer

## TASK 8 : Hunting Persistence
### Read the above and practice hunting persistence techniques. along... 
First we need to check EventID possible like file created (EventID 11) or registry event  (EventID 12/13/14). And with the help of Get-WinEvent :

```powershell
PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\T1023.evtx -FilterXPath '*/System/EventID=11 and */EventData/Data[@Name="RuleName"] and */EventData/Data="T1023"'

   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/21/2020 5:50:27 PM           11 Information      File created:...
12/21/2020 5:50:27 PM           11 Information      File created:...

PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\T1023.evtx -FilterXPath '*/System/EventID=11 and */EventData/Data[@Name="RuleName"] and */EventData/Data="T1023"' -MaxEvents 1 | fl

TimeCreated : 12/21/2020 5:50:27 PM
ProviderName : Microsoft-Windows-Sysmon
Id : 11
Message : File created:
 RuleName: T1023
 UtcTime: 2020-12-21 17:50:27.760
 ProcessGuid: {b79b1e30-e015-5fe0-4408-00000000f500}
 ProcessId: 6736
 Image: C:\Windows\system32\notepad.exe
 TargetFilename: C:\Users\THM-Threat\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\persist.exe
 CreationUtcTime: 2020-12-21 17:50:27.682
```
{: .nolineno }

For the registry example, we need to set up the RuleName to "T1060,RunKey", the name from the TargetObjet in the RuleGroup and tkae EventId for registry like 13.

```powershell
PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\T1060.evtx -FilterXPath '*/System/EventID=13 and */EventData/Data[@Name="RuleName"] and */EventData/Data="T1060,RunKey"'


   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/21/2020 7:44:33 PM           13 Information      Registry value set:...
12/21/2020 7:44:22 PM           13 Information      Registry value set:...
12/21/2020 7:44:15 PM           13 Information      Registry value set:...
12/21/2020 7:43:57 PM           13 Information      Registry value set:...
12/21/2020 7:43:48 PM           13 Information      Registry value set:...

PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\T1060.evtx -FilterXPath '*/System/EventID=13 and */EventData/Data[@Name="RuleName"] and */EventData/Data="T1060,RunKey"' -MaxEvents 1 | fl


TimeCreated  : 12/21/2020 7:44:33 PM
ProviderName : Microsoft-Windows-Sysmon
Id           : 13
Message      : Registry value set:
               RuleName: T1060,RunKey
               EventType: SetValue
               UtcTime: 2020-12-21 19:44:33.887
               ProcessGuid: {b79b1e30-f938-5fe0-7c08-00000000f500}
               ProcessId: 1808
               Image: C:\Windows\regedit.exe
               TargetObject: HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Persistence
               Details: %%windir%%\system32\malicious.exe
```
{: .nolineno }

No Answer

## TASK 9 : Detecting Evasion Techniques
### Read the above and practice detecting evasion techniques 
To detecting Remote Threads, we'll use the EventID 8 :

```powershell
PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Detecting_RemoteThreads.evtx -FilterXPath '*/System/EventID=8'


   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...
7/3/2019 8:39:30 PM              8 Information      CreateRemoteThread detected:...


PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Detecting_RemoteThreads.evtx -FilterXPath '*/System/EventID=8' -MaxEvents 1 | fl


TimeCreated  : 7/3/2019 8:39:30 PM
ProviderName : Microsoft-Windows-Sysmon
Id           : 8
Message      : CreateRemoteThread detected:
               RuleName:
               UtcTime: 2019-07-03 20:39:30.254
               SourceProcessGuid: {365abb72-0c16-5d1d-0000-00108b721100}
               SourceProcessId: 3092
               SourceImage: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
               TargetProcessGuid: {365abb72-1256-5d1d-0000-0010fb1a1b00}
               TargetProcessId: 1632
               TargetImage: C:\Windows\System32\notepad.exe
               NewThreadId: 3148
               StartAddress: 0x00540000
               StartModule:
               StartFunction:
```
{: .nolineno }

No Answer.

## TASK 10 : Practical Investigations 
### Investigation 1
#### What is the full registry key of the USB device calling svchost.exe in Investigation 1? 
Registry is EventID 12/13/14 so let's take a look at those ID's ! EventID 12 and 14 return "no event found" but got lucky with EventID 13 :

```powershell
PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-1.evtx -FilterXPath '*/System/EventID=13' | fl

TimeCreated  : 3/6/2018 6:57:51 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 13
Message      : Registry value set:
               RuleName: SetValue
               EventType: 2018-03-06 06:57:51.007
               UtcTime: {2ca4c7ef-396e-5a9e-0000-001007c50000}
               ProcessGuid: 616
               ProcessId: 0
               Image: HKLM\System\CurrentControlSet\Enum\WpdBusEnumRoot\UMB\2&37c186b&0&STORAGE#VOLUME#_??_USBSTOR#DISK&VEN_SANDISK&PROD_U3_CR
               UZER_MICRO&REV_8.01#4054910EF19005B3&0#\FriendlyName
               TargetObject: U
               Details: %8
```
{: .nolineno }

Answer :

```console
HKLM\System\CurrentControlSet\Enum\WpdBusEnumRoot\UMB\2&37c186b&0&STORAGE#VOLUME#_??_USBSTOR#DISK&VEN_SANDISK&PROD_U3_CRUZER_MICRO&REV_8.01#4054910EF19005B3&0#\FriendlyName
```
{: .nolineno }

#### What is the device name when being called by RawAccessRead in Investigation 1?
Googling the RawAccessRead EventID 9 :

```powershell
PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-1.evtx -FilterXPath '*/System/EventID=9' -MaxEvents 1 | fl

TimeCreated  : 3/6/2018 6:57:51 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 9
Message      : RawAccessRead detected:
               RuleName: 2018-03-06 06:57:51.070
               UtcTime: {2ca4c7ef-396f-5a9e-0000-0010a06d0100}
               ProcessGuid: 1388
               ProcessId: 0
               Image: \Device\HarddiskVolume3
               Device: %6
```
{: .nolineno }

Answer : \Device\HarddiskVolume3

#### What is the first exe the process executes in Investigation 1?
Process creation has EventId 1 and get the first event "-MaxEvents 1" :

```powershell
PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-1.evtx -FilterXPath '*/System/EventID=1' -MaxEvents 1 | fl

TimeCreated  : 3/6/2018 6:57:51 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 1
Message      : Process Create:
               RuleName: 2018-03-06 06:57:51.132
               UtcTime: {2ca4c7ef-3bef-5a9e-0000-001081120e00}
               ProcessGuid: 3348
               ProcessId: 0
               Image: 6.1.7600.16385 (win7_rtm.090713-1255)
               FileVersion: Windows Calculator
               Description: Microsoft® Windows® Operating System
               Product: Microsoft Corporation
               Company: calc.exe
               OriginalFileName: C:\Windows\system32\
               CommandLine: WIN-7JKBJEGBO38\q
               CurrentDirectory: {2ca4c7ef-396f-5a9e-0000-002001500100}
               User: 0x15001
               LogonGuid: 1
               LogonId: 0x0
               TerminalSessionId: 0
               IntegrityLevel: {2ca4c7ef-3bef-5a9e-0000-0010a5110e00}
               Hashes: 4024
               ParentProcessGuid: C:\Windows\System32\rundll32.exe
               ParentProcessId: 0
               ParentImage: %21
               ParentCommandLine: %22
```
{: .nolineno }

Answer : rundll32.exe

### Investigation 2

I firstly tried EventID 3 and got the second part of the answers for investigation 2. Then after opened the log in event viewer i realised that a second interesting EventID was triggered : EventID 1 :

```powershell
PS C:\Users\THM-Analyst> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-2.evtx -FilterXPath '*/System/EventID=1' | fl


TimeCreated  : 6/15/2019 7:14:32 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 1
Message      : Process Create:
               RuleName:
               UtcTime: 2019-06-15 07:14:32.622
               ProcessGuid: {365abb72-9ad8-5d04-0000-0010c08c1000}
               ProcessId: 3892
               Image: C:\Windows\System32\dllhost.exe
               [...]

TimeCreated  : 6/15/2019 7:13:42 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 1
Message      : Process Create:
               RuleName:
               UtcTime: 2019-06-15 07:13:42.278
               ProcessGuid: {365abb72-9aa6-5d04-0000-00109c850f00}
               ProcessId: 652
               Image: C:\Windows\System32\mshta.exe
               FileVersion: 11.00.9600.16428 (winblue_gdr.131013-1700)
               Description: Microsoft (R) HTML Application host
               Product: Internet Explorer
               Company: Microsoft Corporation
               OriginalFileName: "C:\Windows\System32\mshta.exe" "C:\Users\IEUser\AppData\Local\Microsoft\Windows\Temporary Internet
               Files\Content.IE5\S97WTYG7\update.hta"
               CommandLine: C:\Users\IEUser\Desktop\
               CurrentDirectory: IEWIN7\IEUser
               User: {365abb72-98e4-5d04-0000-0020a4350100}
               LogonGuid: 0x135a4
               LogonId: 0x1
               TerminalSessionId: 0
               IntegrityLevel: SHA1=D4F0397F83083E1C6FB0894187CC72AEBCF2F34F,MD5=ABDFC692D9FE43E2BA8FE6CB5A8CB95A,SHA256=949485BA939953642714A
               E6831D7DCB261691CAC7CBB8C1A9220333801F60820,IMPHASH=00B1859A95A316FD37DFF4210480907A
               Hashes: {365abb72-9972-5d04-0000-0010f0490c00}
               ParentProcessGuid: 3660
               ParentProcessId: 0
               ParentImage: "C:\Program Files\Internet Explorer\iexplore.exe" C:\Users\IEUser\Downloads\update.html
               ParentCommandLine: %22
```
{: .nolineno }

#### What is the full path of the payload in Investigation 2?
Answer : C:\Users\IEUser\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5\S97WTYG7\update.hta

#### What is the full path of the file the payload masked itself as in Investigation 2?
Answer :C:\Users\IEUser\Downloads\update.html

#### What signed binary executed the payload in Investigation 2?

```powershell
PS C:\Windows\system32> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-2.evtx -FilterXPath '*/System/EventID=3' | fl


TimeCreated  : 6/15/2019 7:13:44 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 3
Message      : Network connection detected:
               RuleName:
               UtcTime: 2019-06-15 07:13:42.577
               ProcessGuid: {365abb72-9aa6-5d04-0000-00109c850f00}
               ProcessId: 652
               Image: C:\Windows\System32\mshta.exe
               User: IEWIN7\IEUser
               Protocol: tcp
               Initiated: true
               SourceIsIpv6: false
               SourceIp: 10.0.2.13
               SourceHostname: IEWIN7
               SourcePort: 49159
               SourcePortName:
               DestinationIsIpv6: false
               DestinationIp: 10.0.2.18
               DestinationHostname:
               DestinationPort: 4443
               DestinationPortName:
```
{: .nolineno }

Answer : C:\Windows\System32\mshta.exe

#### What is the IP of the adversary in Investigation 2?
Answer : 10.0.2.18

#### What back connect port is used in Investigation 2?
Answer : 4443

### Investigation 3.1
#### What is the IP of the suspected adversary in Investigation 3.1?
C2 server hit in my mind for EventID 3 :

```powershell
PS C:\Users\THM-Analyst> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-3.1.evtx -FilterXPath '*/System/EventID=3' -MaxEvents 1| fl

TimeCreated  : 2/12/2018 9:15:59 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 3
Message      : Network connection detected:
               RuleName: 2018-02-12 09:15:58.664
               UtcTime: {b231f4ab-5a53-5a81-0000-0010c752ef01}
               ProcessGuid: 12224
               ProcessId: 0
               Image: DESKTOP-O153T4R\q
               User: tcp
               Protocol: true
               Initiated: false
               SourceIsIpv6: 172.16.199.179
               SourceIp: DESKTOP-O153T4R.localdomain
               SourceHostname: 54923
               SourcePort: 0
               SourcePortName: false
               DestinationIsIpv6: 172.30.1.253
               DestinationIp: empirec2
               DestinationHostname: 80
               DestinationPort: 0
               DestinationPortName: %18
```
{: .nolineno }

Answer : 172.30.1.253

#### What is the hostname of the affected endpoint in Investigation 3.1?
Answer : DESKTOP-O153T4R

#### What is the hostname of the C2 server connecting to the endpoint in Investigation 3.1?
Answer : empirec2

#### Where in the registry was the payload stored in Investigation 3.1?
Looking for registry event with EventID 12/13/14 :

```powershell
PS C:\Users\THM-Analyst> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-3.1.evtx -FilterXPath '*/System/EventID=13' -MaxEvents 1| fl

TimeCreated  : 2/12/2018 9:15:57 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 13
Message      : Registry value set:
               RuleName: SetValue
               EventType: 2018-02-12 09:15:57.046
               UtcTime: {b231f4ab-5a53-5a81-0000-0010c752ef01}
               ProcessGuid: 12224
               ProcessId: 0
               Image: HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe\Debugger
               TargetObject: "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -c "$x=$((gp HKLM:Software\Microsoft\Network
               debug).debug);start -Win Hidden -A \"-enc $x\" powershell";exit;
               Details: %8
```
{: .nolineno }

Answer : HKLM\SOFTWARE\Microsoft\Network\debug

#### What PowerShell launch code was used to launch the payload in Investigation 3.1?

```powershell
PS C:\Users\THM-Analyst> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-3.1.evtx -FilterXPath '*/System/EventID=13' -MaxEvents 1| fl

TimeCreated  : 2/12/2018 9:15:57 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 13
Message      : Registry value set:
               RuleName: SetValue
               EventType: 2018-02-12 09:15:57.046
               UtcTime: {b231f4ab-5a53-5a81-0000-0010c752ef01}
               ProcessGuid: 12224
               ProcessId: 0
               Image: HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe\Debugger
               TargetObject: "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -c "$x=$((gp HKLM:Software\Microsoft\Network
               debug).debug);start -Win Hidden -A \"-enc $x\" powershell";exit;
               Details: %8
```
{: .nolineno }

Answer :

```powershell
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -c "$x=$((gp HKLM:Software\Microsoft\Network debug).debug);start -Win Hidden -A \"-enc $x\" powershell";exit;
```
{: .nolineno }

### Investigation 3.2
#### What is the IP of the adversary in Investigation 3.2?
After looking at event viewer :

```powershell
PS C:\Users\THM-Analyst> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-3.2.evtx -FilterXPath '*/System/EventID=3' | fl

TimeCreated  : 2/5/2018 7:08:55 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 3
Message      : Network connection detected:
               RuleName: 2018-02-05 07:08:53.923
               UtcTime: {b231f4ab-f2e9-5a77-0000-0010cb670802}
               ProcessGuid: 11020
               ProcessId: 0
               Image: DESKTOP-O153T4R\q
               User: tcp
               Protocol: true
               Initiated: false
               SourceIsIpv6: 172.168.103.167
               SourceIp: DESKTOP-O153T4R.SSG-350M
               SourceHostname: 52984
               SourcePort: 0
               SourcePortName: false
               DestinationIsIpv6: 172.168.103.188
               DestinationIp: ACA867BC.ipt.aol.com
               DestinationHostname: 80
               DestinationPort: 0
               DestinationPortName: %18
```
{: .nolineno }

Answer : 172.168.103.188

#### What is the full path of the payload location in Investigation 3.2?

```powershell
PS C:\Users\THM-Analyst> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-3.2.evtx -FilterXPath '*/System/EventID=1' | fl

TimeCreated  : 2/5/2018 7:08:53 AM
[...]

TimeCreated  : 2/5/2018 7:08:53 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 1
Message      : Process Create:
               RuleName: 2018-02-05 07:08:53.750
               UtcTime: {b231f4ab-0305-5a78-0000-00101b276402}
               ProcessGuid: 8992
               ProcessId: 0
               Image: 10.0.16299.15 (WinBuild.160101.0800)
               FileVersion: Task Scheduler Configuration Tool
               Description: Microsoft® Windows® Operating System
               Product: Microsoft Corporation
               Company: "C:\WINDOWS\system32\schtasks.exe" /Create /F /SC DAILY /ST 09:00 /TN Updater /TR
               "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NonI -W hidden -c \"IEX
               ([Text.Encoding]::UNICODE.GetString([Convert]::FromBase64String($(cmd /c ''more < c:\users\q\AppData:blah.txt'''))))\""
               OriginalFileName: C:\Users\q\
               CommandLine: DESKTOP-O153T4R\q
               CurrentDirectory: {b231f4ab-a303-5a66-0000-002087720500}
               User: 0x57287
               LogonGuid: 1
               LogonId: 0x0
               TerminalSessionId: 0
               IntegrityLevel: {b231f4ab-f2e9-5a77-0000-0010cb670802}
               Hashes: 11020
               ParentProcessGuid: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
               ParentProcessId: 0
               ParentImage: %21
               ParentCommandLine: %22

TimeCreated  : 2/5/2018 7:08:53 AM
[...]
```
{: .nolineno }

Answer : c:\users\q\AppData:blah.txt

#### What was the full command used to create the scheduled task in Investigation 3.2?

Answer : 

```powershell
"C:\WINDOWS\system32\schtasks.exe" /Create /F /SC DAILY /ST 09:00 /TN Updater /TR                "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NonI -W hidden -c \"IEX                ([Text.Encoding]::UNICODE.GetString([Convert]::FromBase64String($(cmd /c ''more < c:\users\q\AppData:blah.txt'''))))\""
```
{: .nolineno }

#### What process was accessed by schtasks.exe that would be considered suspicious behavior in Investigation 3.2?

![Sysmon 10](/images/thm/sysmon/sysmon_1.png)
_Sysmon 10_

Answer : lsass.exe

### Investigation 4
#### What is the IP of the adversary in Investigation 4?

```powershell
PS C:\Users\THM-Analyst> Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Investigations\Investigation-4.evtx -FilterXPath '*/System/EventID=3' | fl

[...]
TimeCreated  : 2/14/2018 9:51:56 AM
ProviderName : Microsoft-Windows-Sysmon
Id           : 3
Message      : Network connection detected:
               RuleName: 2018-02-14 09:51:55.108
               UtcTime: {b231f4ab-03e3-5a84-0000-001082172a00}
               ProcessGuid: 7412
               ProcessId: 0
               Image: NT AUTHORITY\SYSTEM
               User: tcp
               Protocol: true
               Initiated: false
               SourceIsIpv6: 172.16.199.179
               SourceIp: DESKTOP-O153T4R.localdomain
               SourceHostname: 49867
               SourcePort: 0
               SourcePortName: false
               DestinationIsIpv6: 172.30.1.253
               DestinationIp: empirec2
               DestinationHostname: 80
               DestinationPort: 0
               DestinationPortName: %18
[...]
```
{: .nolineno }

Answer : 172.30.1.253

#### What port is the adversary operating on in Investigation 4?
Answer : 80

#### What C2 is the adversary utilizing in Investigation 4?
Answer : empire