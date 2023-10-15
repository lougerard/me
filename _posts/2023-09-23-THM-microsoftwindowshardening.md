---
title: Microsoft Windows Hardening
author: CYB3RM3
name: CYB3RM3 | Microsoft Windows Hardening
date: 2023-09-23 12:41:15 +0100
categories: [TryHackMe, Security Engineer]
tags: [Windows, Hardening]
---

To learn key attack vectors used by hackers and how to protect yourself using different hardening techniques.

THM Room : [https://tryhackme.com/room/microsoftwindowshardening](https://tryhackme.com/room/microsoftwindowshardening)


## TASK 1 Introduction
### Can you connect and log in to the machine? 
No Answer.

## TASK 2 Understanding General Concepts

### What is the startup type of App Readiness service in the services panel?
Answer : Manual

### Open Registry Editor and find the key “tryhackme”. What is the default value of the key? 
Answer : {THM_REG_FLAG}

### Open the Diagnosis folder and go through the various log files. Can you find the flag?
Answer : {THM_1000710}
 
### Open the Event Viewer and play with various event viewer filters like Information, Error, Warning etc. Which error type has the maximum number of logs?
No Answer.

## TASK 3 Identity & Access Management

### Find the name of the Administrator Account of the attached VM.
Answer : Harden

### Go to the User Account Control Setting Panel (Control Panel > All Control Panel Items > User Accounts). What is the default level of Notification? 
Answer : Always Notify

### How many standard accounts are created in the VM?
Answer : 0

## TASK 4 Network Management

### Open Windows Firewall and click on Monitoring in the left pane - which of the following profiles is active? Domain, Private, Public?
Answer : Private


### Find the IP address resolved for the website tryhack.me in the Virtual Machine as per the local hosts file.

```console
PS C:\Users\Harden> ping tryhack.me

Pinging tryhack.me [192.168.1.140] with 32 bytes of data:
Control-C
```
{: .nolineno }

Or in the hosts file :

```console
PS C:\Users\Harden> cat C:\Windows\System32\drivers\etc\hosts
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost
        192.168.1.140   tryhack.me
```
{: .nolineno }

Answer : 192.168.1.140


### Open the command prompt and enter arp -a. What is the Physical address for the IP address 255.255.255.255?

```console
PS C:\Users\Harden> arp -a 

Interface: 10.10.171.142 --- 0x5
  Internet Address      Physical Address      Type
  10.10.0.1             02-c8-85-b5-5a-aa     dynamic
  10.10.255.255         ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
```
{: .nolineno }

Answer : ff-ff-ff-ff-ff-ff

## TASK 5 Application Management

### Windows Defender Antivirus is configured to exclude a particular extension from scanning. What is the extension?

![Exclusion](/images/thm/microsoftwindowshardening/microsofthardening_1.png)
_Exclusion_

Answer : .ps

### A Word document is received from an unknown email address. It is best practice to open it immediately on your personal computer (yay/nay).
Answer : NAY

### What is the flag you received after executing the Office Hardening Batch file?

```console
PS C:\Users\Harden\Desktop> .\office.bat

C:\Users\Harden\Desktop>sc start WinDefend
[SC] StartService FAILED 1056:

An instance of the service is already running.


C:\Users\Harden\Desktop>setx /M MP_FORCE_USE_SANDBOX 1
ERROR: Access to the registry path is denied.

C:\Users\Harden\Desktop>"C:\Program Files"\"Windows Defender"\MpCmdRun.exe -SignatureUpdate
Signature update started . . .
ERROR: Signature Update failed with hr=80070652
CmdTool: Failed with hr = 0x80070652. Check C:\Users\Harden\AppData\Local\Temp\MpCmdRun.log for more information

C:\Users\Harden\Desktop>powershell.exe Set-MpPreference -PUAProtection enable
Set-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Set-MpPreference -PUAProtection enable
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Set-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Set-MpPreference


C:\Users\Harden\Desktop>reg add "HKCU\SOFTWARE\Microsoft\Windows Defender" /v PassiveMode /t REG_DWORD /d 2 /f
The operation completed successfully.

C:\Users\Harden\Desktop>powershell.exe Set-MpPreference -MAPSReporting Advanced
Set-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Set-MpPreference -MAPSReporting Advanced
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Set-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Set-MpPreference


C:\Users\Harden\Desktop>powershell.exe Set-MpPreference -SubmitSamplesConsent 0
Set-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Set-MpPreference -SubmitSamplesConsent 0
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Set-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Set-MpPreference


C:\Users\Harden\Desktop>reg add "HKCU\SYSTEM\CurrentControlSet\Policies\EarlyLaunch" /v DriverLoadPolicy /t REG_DWORD /d 3 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids D4F940AB-401B-4EFC-AADC-AD5F3C50688A -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids D4F940AB-401B-4EFC- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids 75668C1F-73B5-4CF0-BB93-3ECF5CB7CC84 -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids 75668C1F-73B5-4CF0- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids 92E97FA1-2EDF-4476-BDD6-9DD0B4DDDC7B -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids 92E97FA1-2EDF-4476- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids 3B576869-A4EC-4529-8536-B80A7769E899 -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids 3B576869-A4EC-4529- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids 5BEB7EFE-FD9A-4556-801D-275E5FFC04CC -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids 5BEB7EFE-FD9A-4556- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids BE9BA2D9-53EA-4CDC-84E5-9B1EEEE46550 -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids BE9BA2D9-53EA-4CDC- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids D3E037E1-3EB8-44C8-A917-57927947596D -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids D3E037E1-3EB8-44C8- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2 -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids 9e6c4e1f-7d60-472f- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4 -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids b2b3f03d-6a65-4f7b- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids 7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids 7674ba52-37eb-4a4f- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids e6db77e5-3df2-4cf1-b95a-636979351e5b -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids e6db77e5-3df2-4cf1- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>powershell.exe Add-MpPreference -AttackSurfaceReductionRules_Ids d1e49aac-8f56-4280-b9ba-993a6d77406c -AttackSurfaceReductionRules_Actions Enabled
Add-MpPreference : You don't have enough permissions to perform the requested operation.
At line:1 char:1
+ Add-MpPreference -AttackSurfaceReductionRules_Ids d1e49aac-8f56-4280- ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (MSFT_MpPreference:root\Microsoft\...FT_MpPreference) [Add-MpPreference],
   CimException
    + FullyQualifiedErrorId : HRESULT 0xc0000142,Add-MpPreference


C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\12.0\Publisher\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\12.0\Word\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\14.0\Publisher\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\14.0\Word\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\15.0\Outlook\Security" /v markinternalasunsafe /t REG_DWORD /d 0 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\15.0\Word\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\15.0\Excel\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\15.0\PowerPoint\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\15.0\Word\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\15.0\Publisher\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\16.0\Outlook\Security" /v markinternalasunsafe /t REG_DWORD /d 0 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\16.0\Word\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\16.0\Excel\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\16.0\PowerPoint\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\16.0\Word\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\16.0\Publisher\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\19.0\Outlook\Security" /v markinternalasunsafe /t REG_DWORD /d 0 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\19.0\Word\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\19.0\Excel\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\19.0\PowerPoint\Security" /v blockcontentexecutionfrominternet /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\19.0\Word\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Policies\Microsoft\Office\19.0\Publisher\Security" /v vbawarnings /t REG_DWORD /d 4 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Microsoft\Office\14.0\Word\Options" /v DontUpdateLinks /t REG_DWORD /d 00000001 /f
The operation completed successfully.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Microsoft\Office\14.0\Word\Options\WordMail" /v DontUpdateLinks /t REG_DWORD /d 00000001 /f
The operation completed successfully.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Microsoft\Office\15.0\Word\Options" /v DontUpdateLinks /t REG_DWORD /d 00000001 /f
The operation completed successfully.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Microsoft\Office\15.0\Word\Options\WordMail" /v DontUpdateLinks /t REG_DWORD /d 00000001 /f
The operation completed successfully.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Microsoft\Office\16.0\Word\Options" /v DontUpdateLinks /t REG_DWORD /d 00000001 /f
The operation completed successfully.

C:\Users\Harden\Desktop>reg add "HKCU\Software\Microsoft\Office\16.0\Word\Options\WordMail" /v DontUpdateLinks /t REG_DWORD /d 00000001 /f
The operation completed successfully.

C:\Users\Harden\Desktop>reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization" /v DODownloadMode /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config\" /v DODownloadMode /t REG_DWORD /d 1 /f
ERROR: Access is denied.

C:\Users\Harden\Desktop>echo "Microsoft Office Hardened Successfully - Here is your Flag {THM_1101110}"
"Microsoft Office Hardened Successfully - Here is your Flag {THM_1101110}"

C:\Users\Harden\Desktop>pause
Press any key to continue . . .
```
{: .nolineno }

Answer : {THM_1101110}

## TASK 6 Storage Management

### A security engineer has misconfigured the attached VM and stored a BitLocker recovery key in the same computer. Can you read the last six digits of the recovery key?

```console
PS C:\Users\Harden\Desktop> cd ..\Documents\
PS C:\Users\Harden\Documents> ls


    Directory: C:\Users\Harden\Documents


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-ar---         6/28/2021   4:24 AM           1348 BitLocker Recovery Key AC9D5655-F7CA-4D1D-902F.TXT
-a----         5/30/2022   4:29 AM         194888 USBDeview.exe


PS C:\Users\Harden\Documents> cat '.\BitLocker Recovery Key AC9D5655-F7CA-4D1D-902F.TXT'
BitLocker Drive Encryption recovery key

To verify that this is the correct recovery key, compare the start of the following identifier with the identifier value displayed on your PC.

Identifier:

        AC9D5655-F7CA-4D1D-902F-1B6087118138

If the above identifier matches the one displayed by your PC, then use the following key to unlock your drive.

Recovery Key:

        132858-327525-689172-680790-354607-080454-642268-377564

If the above identifier doesn't match the one displayed by your PC, then this isn't the right key to unlock your drive.
Try another recovery key, or refer to https://go.microsoft.com/fwlink/?LinkID=260589 for additional assistance.
```
{: .nolineno }

Answer : 377564

### How many characters does the BitLocker recovery key have in the attached VM?

It have 8 section of 6 characters.

Answer : 48

### A backup file is placed on the Desktop of the attached VM. What is the extension of that file?

```console
PS C:\Users\Harden\Desktop> ls


    Directory: C:\Users\Harden\Desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         6/28/2022   8:00 AM             22 MyWindowsBackup.bkf
-a----         6/27/2022   4:09 AM          10446 office.bat
```
{: .nolineno }

Answer : .bkf

## TASK 7 Updating Windows
### What is the CVE score for the vulnerability CVE ID CVE-2022-32230? 

Quick googling for CVE-2022-32230.

Answer :  7.8

## TASK 8 Cheatsheet for Hardening Windows
### I have completed the room. 
No Answer.
