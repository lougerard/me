---
title: Network Security Protocols
author: CYB3RM3
name: CYB3RM3 | Network Security Protocols
date: 2023-09-24 17:09:15 +0100
categories: [TryHackMe, Security Engineer]
tags: [Network, Intro]
---

Learn about secure network protocols at the different layers of the OSI model.

THM Room : [https://tryhackme.com/room/networksecurityprotocols](https://tryhackme.com/room/networksecurityprotocols)


## TASK 1 Introduction
###  Ensure you satisfy the room prerequisites to ensure maximum benefits of the topics presented in this room. 
No Answer.

## TASK 2 Application Layer
### What is the default port for HTTPS?
Answer : 443

### In a passive FTP connection, what does the client send the first command over the command channel?

>"In passive connection mode, the client establishes the control and data connections. The client sends the PASV command to the server over the command channel; the server sends a random port to the client. As soon as the client receives the port number, the client establishes a connection to the provided port number so that the server can initiate the data transfer to the client."

Answer : PASV

### Use the SSL Shopper website to check the SSL certificate of TryHackMe.

![SSl Shopper](/images/thm/networksecurityprotocols/networksecurity_2.png)
_SSl Shopper_

No Answer.

### Open the SuperTool website, select the Test Email Server option, and check the SMTP Security for smtp.gmail.com.

![SMTP Security](/images/thm/networksecurityprotocols/networksecurity_1.png)
_SMTP Security_

No Answer.

## TASK 3 Application Layer - More Secure Protocols
### What does PGP stand for?

>"PGP (Pretty Good Privacy) is an encryption program created by Phil Zimmerman. OpenPGP is an open standard for signing and encrypting files and email messages and is detailed in RFC 4880. GnuPG (Gnu Privacy Guard), or simply GPG, is a free and open-source implementation of the OpenPGP standard. In brief, GnuPG allows you to sign and encrypt your data and communications."

Answer : Pretty Good Privacy

### What does GPG stand for?
Answer : Gnu Privacy Guard

### What command would you use to generate a key pair using gpg?
Answer : gpg --gen-key

### Consider the following three clients:

    1. rlogin
    2. telnet
    3. ssh

Provide the number of the client that encrypts the traffic.

Answer : 3

## TASK 4 Presentation and Session Layers
### Does the hello message during the SSL handshake include the TLS version (yea/nay)?

>"1.Client Hello Message: The client sends a hello message to the server; it includes the client TLS version and the cypher suite that the client supports, in addition to random bytes."

Answer : YEA

### During the client initiation process of SOCKS5, what is the SOCKS version if the client sends the first 5 bytes (0x05)?

>"Client A connects with the SOCKS5 proxy and sends the first byte (0x05) to the proxy where “5” is the SOCKS version."

Answer : 5

### Click the View Site button at the top of the task to launch the static site in split view. What is the flag after completing the exercise?

![exercise](/images/thm/networksecurityprotocols/networksecurity_3.png)
_exercise_

![Flag](/images/thm/networksecurityprotocols/networksecurity_4.png)
_Flag_

Answer : THM{GOT_THE_SSLKEY}

## TASK 5 Network Layer
### What does ESP stand for?

>"2. Encapsulating Security Payload (ESP): Provides authentication, integrity, and confidentiality."

Answer : Encapsulating Security Payload

### Which protocol does the Cisco VPN client use to establish a VPN connection?
Answer : ipsec

### Which protocol does the OpenVPN project use for encryption and authentication?

>"Although SSL was created to secure HTTP traffic, SSL/TLS has found its way to establish secure VPN connections with OpenVPN. Using various tools and libraries built around TLS, OpenVPN offers different authentication and encryption mechanisms to establish VPN connections."

Answer : SSL/TLS

## TASK 6 Conclusion
### Ensure that you have read and taken notes of the ideas presented in this room. 
No Answer.
