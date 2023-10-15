---
title: Secure Network Architecture
author: CYB3RM3
name: CYB3RM3 | Secure Network Architecture
date: 2023-09-17 19:30:25 +0100
categories: [TryHackMe, Network and System Security]
tags: [Network, Architecture, Intro, Security Engineer]
---

Learn about and implement security best practices for network environments.

THM Room : [https://tryhackme.com/room/introtosecurityarchitecture](https://tryhackme.com/room/introtosecurityarchitecture)


## TASK 1 Introduction
###  Read the above and continue to the next task. 
No Answer.

## TASK 2 Network Segmentation
### How many trunks are present in this configuration?
Count Bridges : br0, br1, br2 and br3

Answer : 4

### What is the VLAN tag ID for interface eth12?

```console
 Port eth6
            tag: 30
            Interface eth6
        Port eth12
            tag: 30
            Interface eth12
```
{: .nolineno }

Answer : 30

## TASK 3 Common Secure Network Architecture
### From the above table, what zone would a user connecting to a public web server be in?
Answer : external
### From the above table, what zone would a public web server be in?
Answer : DMZ
### From the above table, what zone would a core domain controller be placed in?
Answer : restricted

## TASK 4 Network Security Policies and Controls
### According to the corresponding ACL policy, will the first packet result in a drop or accept? 
Answer : accept

### According to the corresponding ACL policy, will the second packet result in a drop or accept?
Answer : drop

## TASK 5 Zone-Pair Policies and Filtering
## TASK 6 Validating Network Traffic

### Does SSL inspection require a man-in-the-middle proxy? (Y/N)
Answer : Y

### What platform processes data sent from an SSL proxy?

>"Once intercepted, the proxy will decrypt the traffic and send it to be processed by a UTM (Unified Threat Management) platform."

Answer : Unified Threat Management

## TASK 7 Addressing Common Attacks

### Where does DHCP snooping store leased IP addresses from untrusted hosts?

>"Although DHCP is a layer three protocol, DHCP snooping operates on the switch at layer two. The switch will store untrusted hosts with leased IP addresses in a DHCP Binding Database. The database is used to validate traffic and can be used by other protocols, such as dynamic ARP inspection, which we will cover later in this task."

Answer : DHCP Binding Database

### Will a switch drop or accept a DHCPRELEASE packet?
Answer : drop

### Does dynamic ARP inspection use the DHCP binding database? (Y/N)
Answer : y

### Dynamic ARP inspection will match an IP address and what other packet detail?
Answer : mac address

## TASK 8 Conclusion
###  Read the above and continue learning! 
No Answer.

