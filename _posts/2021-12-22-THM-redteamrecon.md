---
title: Red Team Recon  
author: CYB3RM3
name: CYB3RM3 | Red Team Recon 
date: 2021-12-22 15:18:49 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, Reconnaissance]
---

Learn how to use DNS, advanced searching, Recon-ng, and Maltego to collect information about your target.

THM Room [https://tryhackme.com/room/redteamrecon](https://tryhackme.com/room/redteamrecon)

## TASK 1 : Introduction
### We suggest you start the AttackBox and experiment with every command and tool we demonstrate. 
No Answer

## TASK 2 : Taxonomy of Reconnaissance  
### Ensure you have a clear understanding of the different types of recon activities before proceeding. 
No Answer

## TASK 3 : Built-in Tools
### When was thmredteam.com created (registered)? (YYYY-MM-DD) 

```console
root@ip-10-10-52-65:~# whois thmredteam.com
   Domain Name: THMREDTEAM.COM
   Registry Domain ID: 2643258257_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.namecheap.com
   Registrar URL: http://www.namecheap.com
   Updated Date: 2021-10-13T20:54:46Z
   Creation Date: 2021-09-24T14:04:16Z
   Registry Expiry Date: 2022-09-24T14:04:16Z
   Registrar: NameCheap, Inc.
   Registrar IANA ID: 1068
   Registrar Abuse Contact Email: abuse@namecheap.com
   Registrar Abuse Contact Phone: +1.6613102107
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Name Server: KIP.NS.CLOUDFLARE.COM
   Name Server: UMA.NS.CLOUDFLARE.COM
   DNSSEC: unsigned
```
{: .nolineno }

Answer : 2021-09-24



### To how many IPv4 addresses does clinic.thmredteam.com resolve?

```console
C:\Users\Administrateur>nslookup clinic.thmredteam.com
Serveur :   one.one.one.one
Address:  1.1.1.1

Réponse ne faisant pas autorité :
Nom :    clinic.thmredteam.com
Addresses:  2606:4700:3034::ac43:d4f9
          2606:4700:3034::6815:5da9
          104.21.93.169
          172.67.212.249
```
{: .nolineno }

Answer : 2

### To how many IPv6 addresses does clinic.thmredteam.com resolve?
Answer : 2

## TASK 4 : Advanced Searching 
### How would you search using Google for xls indexed for http://clinic.thmredteam.com?
Answer : filetype:xls site:clinic.thmredteam.com-

### How would you search using Google for files with the word passwords for http://clinic.thmredteam.com?
Answer : passwords site:clinic.thmredteam.com

## TASK 5 : Specialized Search Engines 
### What is the shodan command to get your Internet-facing IP address?
Answer : shodan myip

## TASK 6 : Recon-ng  
### How do you start recon-ng with the workspace clinicredteam? 
Answer : recon-ng -w clinicredteam

### How many modules with the name virustotal exist?

```console
[recon-ng][thmredteam] > marketplace search virustotal
[*] Searching module index for 'virustotal'...

  +---------------------------------------------------------------------------------+
  |               Path               | Version |     Status    |  Updated   | D | K |
  +---------------------------------------------------------------------------------+
  | recon/hosts-hosts/virustotal     | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/netblocks-hosts/virustotal | 1.0     | not installed | 2019-06-24 |   | * |
  +---------------------------------------------------------------------------------+

  D = Has dependencies. See info for details.
  K = Requires keys. See info for details.
```
{: .nolineno }

Answer : 2

### There is a single module under hosts-domains. What is its name?

```console
[recon-ng][thmredteam] > marketplace info hosts-domains

  +--------------------------------------------------------------------------------------+
  | path          | recon/hosts-domains/migrate_hosts                                    |
  | name          | Hosts to Domains Data Migrator                                       |
  | author        | Tim Tomes (@lanmaster53)                                             |
  | version       | 1.1                                                                  |
  | last_updated  | 2020-05-17                                                           |
  | description   | Adds a new domain for all the hostnames stored in the 'hosts' table. |
  | required_keys | []                                                                   |
  | dependencies  | []                                                                   |
  | files         | ['suffixes.txt']                                                     |
  | status        | not installed                                                        |
  +--------------------------------------------------------------------------------------+
```
{: .nolineno }

Answer : migrate_hosts

###  censys_email_address is a module that “retrieves email addresses from the TLS certificates for a company.” Who is the author? 

```console
[recon-ng][thmredteam] > marketplace info censys_email_address

  +-----------------------------------------------------------------------------------------------------------------------------------+
  | path          | recon/companies-contacts/censys_email_address                                                                     |
  | name          | Censys emails by company                                                                                          |
  | author        | Censys Team                                                                                                       |
  | version       | 2.0                                                                                                               |
  | last_updated  | 2021-05-11                                                                                                        |
  | description   | Retrieves email addresses from the TLS certificates for a company. Updates the 'contacts' table with the results. |
  | required_keys | ['censysio_id', 'censysio_secret']                                                                                |
  | dependencies  | ['censys>=2.0.0']                                                                                                 |
  | files         | []                                                                                                                |
  | status        | not installed                                                                                                     |
  +-----------------------------------------------------------------------------------------------------------------------------------+

```
{: .nolineno }

Answer : Censys Team

## TASK 7 : Maltego

### What is the name of the transform that queries NIST’s National Vulnerability Database? 

![NIST](/images/thm/redteamrecon/redteamrecon_1.png)
_NIST_

Answer : NIST NVD


### What is the name of the project that offers a transform based on ATT&CK?

![MISP Project 1](/images/thm/redteamrecon/redteamrecon_2.png)
_MISP Project 1_

![MISP Project 2](/images/thm/redteamrecon/redteamrecon_3.png)
_MISP Project 2_

Answer : MISP Project 

## TASK 8 : Summary
### The different tools and websites presented in this room provide the basics necessary to tackle further reconnaissance work.
No Answer