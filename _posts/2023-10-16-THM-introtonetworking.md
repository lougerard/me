---
title: Introductory Networking
author: CYB3RM3
name: CYB3RM3 | Introductory Networking
date: 2023-10-16 07:35:15 +0100
categories: [TryHackMe, Network Exploitation Basics]
tags: [Networking, Intro, Complete Beginner]
---

An introduction to networking theory and basic networking tools

THM Room : [https://tryhackme.com/room/introtonetworking](https://tryhackme.com/room/introtonetworking)


## TASK 1 Introduction
### Let's get started!
No Answer.

## TASK 2 The OSI Model: An Overview
### Which layer would choose to send data over TCP or UDP?
Answer : 4

### Which layer checks received information to make sure that it hasn't been corrupted?
Answer : 2

### In which layer would data be formatted in preparation for transmission?
Answer : 2

### Which layer transmits and receives data?
Answer : 1

### Which layer encrypts, compresses, or otherwise transforms the initial data to give it a standardised format?
Answer : 6

### Which layer tracks communications between the host and receiving computers?
Answer : 5

### Which layer accepts communication requests from applications?
Answer : 7

### Which layer handles logical addressing?
Answer : 3

### When sending data over TCP, what would you call the "bite-sized" pieces of data?
Answer : Segmetns

### [Research] Which layer would the FTP protocol communicate with?
Answer : 7

### Which transport layer protocol would be best suited to transmit a live video?
Answer : UDP

## TASK 3 Encapsulation
### How would you refer to data at layer 2 of the encapsulation process (with the OSI model)?
Answer : Frames

### How would you refer to data at layer 4 of the encapsulation process (with the OSI model), if the UDP protocol has been selected?
Answer : Datagrams

### What process would a computer perform on a received message?
Answer : De-encapsulation

### Which is the only layer of the OSI model to add a trailer during encapsulation?
Answer : Data Link

### Does encapsulation provide an extra layer of security (Aye/Nay)?
Answer : Aye


## TASK 4 The TCP/IP Model
### Which model was introduced first, OSI or TCP/IP?
Answer : TCP/IP

### Which layer of the TCP/IP model covers the functionality of the Transport layer of the OSI model (Full Name)?
Answer : Transport

### Which layer of the TCP/IP model covers the functionality of the Session layer of the OSI model (Full Name)?
Answer : Application

### The Network Interface layer of the TCP/IP model covers the functionality of two layers in the OSI model. These layers are Data Link, and?.. (Full Name)?
Answer : Physical

### Which layer of the TCP/IP model handles the functionality of the OSI network layer?
Answer : Internet

### What kind of protocol is TCP?
Answer : Connection-based

### What is SYN short for?
Answer : Synchronise

### What is the second step of the three way handshake?
Answer : SYN/ACK

### What is the short name for the "Acknowledgement" segment in the three-way handshake?
Answer : ACK

## TASK 5 Networking Tools Ping
### What command would you use to ping the bbc.co.uk website?
Answer : ping bbc.co.uk

### Ping muirlandoracle.co.uk . What is the IPv4 address?
Answer : 217.160.0.152

### What switch lets you change the interval of sent ping requests?
Answer : -i

### What switch would allow you to restrict requests to IPv4?
Answer : -4

### What switch would give you a more verbose output?
Answer : -v

## TASK 6 Networking Tools Traceroute
### Use traceroute on tryhackme.com . Can you see the path your request has taken?
No Answer.

### What switch would you use to specify an interface when using Traceroute?
Answer : -i

### What switch would you use if you wanted to use TCP SYN requests when tracing the route?
Answer : -T

### [Lateral Thinking] Which layer of the TCP/IP model will traceroute run on by default (Windows)?
Answer : Internet

## TASK 7 Networking Tools WHOIS
### Perform a whois search on facebook.com
No Answer.

### What is the registrant postal code for facebook.com?
Answer : 94025

### When was the facebook.com domain first registered (Format: DD/MM/YYYY)?
Answer : 29/03/1997

### Perform a whois search on microsoft.com .(Note: If you fail to read the above instruction and consequently get the wrong answer for the next question, don't expect a helpful response if you report it as a bug...)
No Answer.

### Which city is the registrant based in?
Answer : Redmond

### [OSINT] What is the name of the golf course that is near the registrant address for microsoft.com?
Answer : Bellevue Golf Course

### What is the registered Tech Email for microsoft.com?
Answer : msnhst@microsoft.com

## TASK 8 Networking Tools Dig
### What is DNS short for?
Answer : Domain Name System

### What is the first type of DNS server your computer would query when you search for a domain?
Answer : Recursive

### What type of DNS server contains records specific to domain extensions (i.e. .com, .co.uk*, etc)*? Use the long version of the name.
Answer : Top-Level Domain

### Where is the very first place your computer would look to find the IP address of a domain?
Answer : Local Cache

### [Research] Google runs two public DNS servers. One of them can be queried with the IP 8.8.8.8, what is the IP address of the other one?
Answer : 8.8.4.4

### If a DNS query has a TTL of 24 hours, what number would the dig query show?
Answer : 86400

## TASK 9 Further Reading
### Read the final thoughts
No Answer.