---
title: DNS in detail
author: CYB3RM3
name: CYB3RM3 | DNS in detail
date: 2023-10-15 16:15:15 +0100
categories: [TryHackMe, How The Web Works]
tags: [DNS, Intro, Pre Security]
---

Learn how DNS works and how it helps you access internet services.

THM Room : [https://tryhackme.com/room/dnsindetail](https://tryhackme.com/room/dnsindetail)


## TASK 1 What is DNS?
### What does DNS stand for?
Answer : Domain Name System

## TASK 2 Domain Hierarchy
### What is the maximum length of a subdomain?
Answer : 63

### Which of the following characters cannot be used in a subdomain ( 3 b _ - )?
Answer : _

### What is the maximum length of a domain name?
Answer : 253

### What type of TLD is .co.uk?
Answer : ccTLD

## TASK 3 Record Types
### What type of record would be used to advise where to send email?
Answer : MX

### What type of record handles IPv6 addresses?
Answer : AAAA

## TASK 4 Making A Request
### What field specifies how long a DNS record should be cached for?
Answer : TTL

### What type of DNS Server is usually provided by your ISP?
Answer : recursive

### What type of server holds all the records for a domain?
Answer :authoritative

## TASK 5 Practical
### What is the CNAME of shop.website.thm?
Answer : shops.myshopify.com

### What is the value of the TXT record of website.thm?
Answer : THM{7012BBA60997F35A9516C2E16D2944FF}

### What is the numerical priority value for the MX record?
Answer : 30

### What is the IP address for the A record of www.website.thm?
Answer : 10.10.10.10