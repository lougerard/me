---
title: Net Sec Challenge 
author: CYB3RM3
name: CYB3RM3 | Net Sec Challenge  
date: 2021-10-23 13:39:05 +0100
categories: [TryHackMe, Web]
tags: [Web, Nmap, Scan]
---

Practice the skills you have learned in the Network Security module.

THM Room [https://tryhackme.com/room/netsecchallenge](https://tryhackme.com/room/netsecchallenge)


## TASK 1 : Introduction 
### Launch the AttackBox and the target VM. 
No Answer

## TASK 2 : Challenge Questions
### What is the highest port number being open less than 10,000? 

```console
root@ip-10-10-113-145:~/Desktop# nmap -sC -vv 10.10.134.143

Starting Nmap 7.60 ( https://nmap.org ) at 2021-10-23 11:11 BST
[...]
22/tcp open ssh syn-ack ttl 64
80/tcp open http syn-ack ttl 64
| http-methods: 
|_ Supported Methods: OPTIONS GET HEAD POST
|_http-title: Hello, world!
139/tcp open netbios-ssn syn-ack ttl 64
445/tcp open microsoft-ds syn-ack ttl 64
8080/tcp open http-proxy syn-ack ttl 64
| http-methods: 
|_ Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
MAC Address: 02:DF:8A:CC:E6:79 (Unknown)
[...]
```
{: .nolinenno }

Answer : 8080

### There is an open port outside the common 1000 ports; it is above 10,000. What is it?

```console
root@ip-10-10-113-145:~/Desktop# nmap 10.10.134.143 -p 10000-20000

Starting Nmap 7.60 ( https://nmap.org ) at 2021-10-23 11:17 BST
Nmap scan report for ip-10-10-134-143.eu-west-1.compute.internal (10.10.134.143)
Host is up (0.00038s latency).
Not shown: 10000 closed ports
PORT      STATE SERVICE
10021/tcp open  unknown
MAC Address: 02:DF:8A:CC:E6:79 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 13.12 seconds
```
{: .nolinenno }

Answer : 10021

### How many TCP ports are open?
5 in first nmap + 1 in second nmap, so 6.

Answer : 6

### What is the flag hidden in the HTTP server header?

```console
root@ip-10-10-113-145:~/Desktop# telnet 10.10.134.143 80
Trying 10.10.134.143...
Connected to 10.10.134.143.
Escape character is '^]'.
GET / HTTP/1.1

HTTP/1.1 400 Bad Request
Content-Type: text/html
Content-Length: 345
Connection: close
Date: Sat, 23 Oct 2021 10:21:25 GMT
Server: lighttpd THM{web_server_25352}

<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
         "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
 <head>
  <title>400 Bad Request</title>
 </head>
 <body>
  <h1>400 Bad Request</h1>
 </body>
</html>
Connection closed by foreign host.
```
{: .nolinenno }

Answer : THM{web_server_25352}

### What is the flag hidden in the SSH server header?

```console
root@ip-10-10-113-145:~/Desktop# ssh -v 10.10.134.143
OpenSSH_7.6p1 Ubuntu-4ubuntu0.3, OpenSSL 1.0.2n  7 Dec 2017
debug1: Reading configuration data /etc/ssh/ssh_config
[...]
debug1: Local version string SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
debug1: Remote protocol version 2.0, remote software version OpenSSH_8.2p1 THM{946219583339}
debug1: match: OpenSSH_8.2p1 THM{946219583339} pat OpenSSH* compat 0x04000000
debug1: Authenticating to 10.10.134.143:22 as 'root'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
[...]
```
{: .nolinenno }

Answer : THM{946219583339}

### We have an FTP server listening on a nonstandard port. What is the version of the FTP server?

```console
root@ip-10-10-113-145:~/Desktop# telnet 10.10.134.143 10021
Trying 10.10.134.143...
Connected to 10.10.134.143.
Escape character is '^]'.
220 (vsFTPd 3.0.3)
USER eddie
331 Please specify the password.
PASS jordan
230 Login successful.
ls
500 Unknown command.
?
500 Unknown command.
help
214-The following commands are recognized.
 ABOR ACCT ALLO APPE CDUP CWD  DELE EPRT EPSV FEAT HELP LIST MDTM MKD
 MODE NLST NOOP OPTS PASS PASV PORT PWD  QUIT REIN REST RETR RMD  RNFR
 RNTO SITE SIZE SMNT STAT STOR STOU STRU SYST TYPE USER XCUP XCWD XMKD
 XPWD XRMD
214 Help OK.
status
500 Unknown command.
stat
211-FTP server status:
     Connected to ::ffff:10.10.113.145
     Logged in as eddie
     TYPE: ASCII
     No session bandwidth limit
     Session timeout in seconds is 300
     Control connection is plain text
     Data connections will be plain text
     At session startup, client count was 1
     vsFTPd 3.0.3 - secure, fast, stable
211 End of status
```
{: .nolinenno }

Answer : vsFTPd 3.0.3

### We learned two usernames using social engineering: eddie and quinn. What is the flag hidden in one of these two account files and accessible via FTP?

```console
root@ip-10-10-113-145:~/Desktop# ftp 10.10.134.143 10021
Connected to 10.10.134.143.
220 (vsFTPd 3.0.3)
Name (10.10.134.143:root): quinn
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-r--    1 1002     1002           18 Sep 20 08:27 ftp_flag.txt
226 Directory send OK.
ftp> ls -la
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 1002     1002         4096 Sep 20 08:36 .
drwxr-xr-x    2 1002     1002         4096 Sep 20 08:36 ..
-rw-r--r--    1 1002     1002          220 Sep 14 07:43 .bash_logout
-rw-r--r--    1 1002     1002         3771 Sep 14 07:43 .bashrc
-rw-r--r--    1 1002     1002          807 Sep 14 07:43 .profile
-rw-------    1 1002     1002          723 Sep 20 08:27 .viminfo
-rw-rw-r--    1 1002     1002           18 Sep 20 08:27 ftp_flag.txt
226 Directory send OK.
ftp> get ftp_flag.txt 
local: ftp_flag.txt remote: ftp_flag.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for ftp_flag.txt (18 bytes).
226 Transfer complete.
18 bytes received in 0.08 secs (0.2342 kB/s)
ftp> quit
root@ip-10-10-113-145:~/Desktop# cat ftp_flag.txt 
THM{321452667098}
```
{: .nolineno }

Answer : THM{321452667098}

### Browsing to http://10.10.134.143:8080 displays a small challenge that will give you a flag once you solve it. What is the flag?

```console
root@ip-10-10-113-145:~/Desktop# nmap -sN 10.10.134.143

Starting Nmap 7.60 ( https://nmap.org ) at 2021-10-23 12:31 BST
Stats: 0:01:02 elapsed; 0 hosts completed (1 up), 1 undergoing NULL Scan
NULL Scan Timing: About 73.17% done; ETC: 12:32 (0:00:23 remaining)
Nmap scan report for ip-10-10-134-143.eu-west-1.compute.internal (10.10.134.143)
Host is up (0.00041s latency).
Not shown: 995 closed ports
PORT     STATE         SERVICE
22/tcp   open|filtered ssh
80/tcp   open|filtered http
139/tcp  open|filtered netbios-ssn
445/tcp  open|filtered microsoft-ds
8080/tcp open|filtered http-proxy
MAC Address: 02:DF:8A:CC:E6:79 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 96.73 seconds
```
{: .nolineno }

The challenge was to find that the NULL Scan with nmap give the flag on the webpage http://10.10.134.143:8080 :

![Flag](/images/thm/netsecchallenge/netsecchallenge_1.png)
_Flag_

Answer : THM{f7443f99} 

## TASK 3 : Summary
### Time to continue your journey with a new module.
No Answer