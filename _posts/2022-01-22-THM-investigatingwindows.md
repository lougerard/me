---
title: Investigating Windows
author: CYB3RM3
name: CYB3RM3 | Investigating Windows
date: 2022-01-22 16:06:50 +0100
categories: [TryHackMe, Investigation]
tags: [Forensics, Windows, Investigation]
---

A windows machine has been hacked, its your job to go investigate this windows machine and find clues to what the hacker might have done.

THM Room [https://tryhackme.com/room/investigatingwindows](https://tryhackme.com/room/investigatingwindows)

## TASK 1 : Investigating Windows
### Whats the version and year of the windows machine?
Answer : windows server 2016

### Which user logged in last?
Write a little powershell script <https://community.spiceworks.com/topic/2025022-find-last-user-logged-into-a-machine-via-powershell> lastloguser.ps1 :

```powershell
$com=read-host "Enter Computer name here"
Get-WmiObject -Class Win32_NetworkLoginProfile -ComputerName $com | 
Sort-Object -Property LastLogon -Descending | 
Select-Object -Property * -First 1 | 
Where-Object {$_.LastLogon -match "(\d{14})"} | 
Foreach-Object { New-Object PSObject -Property @{ Name=$_.Name;LastLogon=[datetime]::ParseExact($matches[0], "yyyyMMddHHmmss", $null)}}
```
{: .nolineno }

Execute and enter the Hostname of the computer at prompted : EC2AMAZ-I8UHO76 :

```powershell
./lastloguser.ps1
```
{: .nolineno }

Answer : Administrator

### When did John log onto the system last? Answer format: MM/DD/YYYY H:MM:SS AM/PM
Using "net user" command :

```console
C:\Users>net user john | findstr "log"
Last logon                   3/2/2019 5:48:32 PM
```
{: .nolineno }

Answer : 03/02/2019 5:48:32 PM

### What IP does the system connect to when it first starts?
Let's check a particular registry entry for start up actions :

```console
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
```
{: .nolineno }

![CurrentVersion\Run](/images/thm/investigatingwindows/investigatingwindows_1.png)
_CurrentVersion\Run_

Answer : 10.34.2.3

### What two accounts had administrative privileges (other than the Administrator user)? Answer format: username1, username2
Checking the local Administrator group with net command :

![Local Administrator Group](/images/thm/investigatingwindows/investigatingwindows_2.png)
_Local Administrator Group_

Answer : Jenny, Guest

### Whats the name of the scheduled task that is malicous.
Open the task scheduler then looking around the few tasks. One of them seems suspect with it's name : "Clean file system" so i looked its actions tab :

![Task Scheduler](/images/thm/investigatingwindows/investigatingwindows_3.png)
_Task Scheduler_

This task is launching a netcat listener to open port 1348

Answer : Clean file system

### What file was the task trying to run daily?
As we can see on above screenshot, this task launch a powershell script : nc.ps1

Answer : nc.ps1

### What port did this file listen locally for?
As we can see on above screenshot too, the listening port is 1348

Answer : 1348

### When did Jenny last logon?

![Jenny](/images/thm/investigatingwindows/investigatingwindows_4.png)
_Jenny_

Answer : Never

### At what date did the compromise take place? Answer format: MM/DD/YYYY
The suspects elements in the C:\TMP folder are  all dated from 03/02/2019 :

![C:\TMP](/images/thm/investigatingwindows/investigatingwindows_5.png)
_C:\TMP_

Answer : 03/02/2019

### At what time did Windows first assign special privileges to a new logon? Answer format: MM/DD/YYYY HH:MM:SS AM/PM
I searched for the "Special privileges" Windows Event ID and found 4672 on Microsoft documentation <https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4672>.

Looking around the time of the attack, the first event is :

![Special privileges](/images/thm/investigatingwindows/investigatingwindows_6.png)
_Special privileges_

Answer : 03/02/2019 04:04:49 PM

### What tool was used to get Windows passwords?
Looking at mim-out.txt :

![mim-out.txt](/images/thm/investigatingwindows/investigatingwindows_7.png)
_mim-out.txt_

Answer : mimikatz

### What was the attackers external control and command servers IP?
Looking for redirection of dns traffic in the hosts windows file :

![hosts](/images/thm/investigatingwindows/investigatingwindows_8.png)
_hosts_

Answer : 76.32.97.132

### What was the extension name of the shell uploaded via the servers website?
The windows server website (IIS) has content stored in C:\inetpub\wwwroot :

![C:\inetpub\wwwroot](/images/thm/investigatingwindows/investigatingwindows_9.png)
_C:\inetpub\wwwroot_

Answer : .jsp

### hat was the last port the attacker opened?
In order to communicate with the Control and Command Server (see question above) the hacker had set up a firewall rules :

![Inbound Firewall Rules](/images/thm/investigatingwindows/investigatingwindows_10.png)
_Inbound Firewall Rules_

Answer : 1337

### Check for DNS poisoning, what site was targeted?
DNS record can be manage in the Windows Hosts file :

![hosts](/images/thm/investigatingwindows/investigatingwindows_11.png)
_hosts_

Answer : google.com