---
title: Network Device Hardening
author: CYB3RM3
name: CYB3RM3 | Network Device Hardening
date: 2023-09-24 12:43:37 +0100
categories: [TryHackMe, Security Engineer]
tags: [Network, Hardening, Intro]
---

Learn techniques for securing and protecting network devices from potential threats and attacks.

THM Room : [https://tryhackme.com/room/networkdevicehardening](https://tryhackme.com/room/networkdevicehardening)


## TASK 1 Introduction
###  I am ready to start the room. 
No Answer.

## TASK 2 Common Threat and Attack Vectors
### The device that is used to control and manage network resource is called?
Answer : network devices

### A threat vector that includes disruption of critical devices and services to make them unavailable to genuine users is called?
Answer : Denial of Service

## TASK 3 Common Hardening Techniques

### Suppose you are configuring a router; which of the following could be considered an insecure protocol:

A: HTTPS
B: FTP
C: SSH
D: IPsec

FTP should not be configure if FTPS is possible because it's insecure.

Answer : B

### The protocol for sending log messages to a centralised server for storage and analysis is called?

>"Syslog: A protocol to standardise the transfer of log messages, with the purpose of storing and analysing log messages to a central server."

Answer : Syslog

## TASK 4 Hardening Virtual Private Networks
### Update the config file to use cipher AES-128-CBC. What is the flag value linked with the cipher directive?
Modify the server.conf as requested.

```console
ubuntu@tryhackme:/etc/openvpn/server$ cat server.conf
local 10.0.1.1 //change that to your local machine IP
port 1194
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh.pem
auth SHA512 #Flag value: THM{AUTH_UPDATED_123}
tls-crypt tc.key
tls-version-min 1.2
topology subnet
server 10.8.0.0 255.255.255.0
push "redirect-gateway def1 bypass-dhcp"
ifconfig-pool-persist ipp.txt
push "dhcp-option DNS 1.1.1.1"
push "dhcp-option DNS 1.0.0.1"
push "block-outside-dns"
keepalive 10 120
cipher AES-128-CBC #Flag value: THM{CIPHER_UPDATED_1101}
user nobody
group nogroup
persist-key
persist-tun
verb 3
crl-verify crl.pem
explicit-exit-notify

```
{: .nolineno }

Answer : THM{CIPHER_UPDATED_1101}

### Update the config file to use auth SHA512. What is the flag value linked with the auth directive?
Answer : THM{AUTH_UPDATED_123}

### As per the config file, what is the port number for the OpenVPN server?
Answer : 1194

## TASK 5 Hardening Routers, Switches & Firewalls
### Update the password of the router to TryHackMe123.

Go to "system > adminsitration" to reset the password.

![Passsword Reset](/images/thm/networkdevicehardening/Networkhardening_0.png)
_Passsword Reset_


No Answer.

### What is the default SSH port configured for OpenWrt in the attached VM?
Go to "system > adminsitration > SSH Access" to view SSH configuration.

![SSH configuration](/images/thm/networkdevicehardening/Networkhardening_2.png)
_SSH configuration_

Answer : 

### Go through the General Settings option under the System tab in the attached VM. The administrator has left a special message in the Notes section. What is the flag value?

![Flag](/images/thm/networkdevicehardening/Networkhardening_1.png)
_Flag_

Answer : THM{SYSTEM101}

### What is the default system log buffer size value for the OpenWrt router in the attached VM?

![system log buffer size value](/images/thm/networkdevicehardening/Networkhardening_3.png)
_system log buffer size value_

Answer : 64

### What is the start priority for the script uhttpd?

![start priority](/images/thm/networkdevicehardening/Networkhardening_4.png)
_start priority_

Answer : 50

## TASK 6 Hardening Routers, Switches & Firewalls - More Techniques
### What is the name of the rule that accepts ICMP traffic from source zone WAN and destination zone as this device?

![allow-ping](/images/thm/networkdevicehardening/Networkhardening_5.png)
_allow-ping_

Answer : allow-ping

### What is the name of the rule that forwards data coming from WAN port 9001 to LAN port 9002? 

![THM-PORT](/images/thm/networkdevicehardening/Networkhardening_6.png)
_THM-PORT_

Answer : THM_PORT

### What is the version number for the available apk package?

![apk package](/images/thm/networkdevicehardening/Networkhardening_7.png)
_apk package_

Answer : 2.12.2-1

## TASK 7 Important Tools for Network Monitoring
###  Are network monitoring tools capable of detecting bandwidth bottlenecks? (yea/nay) 
Answer : YEA

## TASK 8 Conclusion
###  I have completed the room. 
No Answer.
