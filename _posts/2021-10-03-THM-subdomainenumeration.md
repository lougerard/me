---
title: Subdomain Enumeration 
author: CYB3RM3
name: CYB3RM3 | Subdomain Enumeration 
date: 2021-10-03 12:13:39 +0100
categories: [TryHackMe, Web]
tags: [Web, Subdomain]
---

THM Room [https://tryhackme.com/room/subdomainenumeration](https://tryhackme.com/room/subdomainenumeration)


## TASK 1 : Brief
### What is a subdomain enumeration method beginning with B?
Answer : Brute Force

### What is a subdomain enumeration method beginning with O?
Answer : OSINT

### What is a subdomain enumeration method beginning with V?
Answer : Virtual Host

## TASK 2 : OSINT - SSL/TLS Certificates
### What domain was logged on crt.sh at 2020-12-26? 

![crt.sh](/images/thm/subdomainenumeration/subdomainenumeration_1.png)
_crt.sh_

Answer : store.tryhackme.com

## TASK 3 : OSINT - Search Engines
### What is the TryHackMe subdomain beginning with B discovered using the above Google search?
Just searched -site:www.tryhackme.com  site:*.tryhackme.com on google :

![Google Dork](/images/thm/subdomainenumeration/subdomainenumeration_2.png)
_Google Dork_

Answer : blog.tryhackme.com

## TASK 4 : DNS Bruteforce 
### What is the first subdomain found with the dnsrecon tool?

![dnsrecon](/images/thm/subdomainenumeration/subdomainenumeration_3.png)
_dnsrecon_

Answer : api.acmeitsupport.thm

## TASK 5 : OSINT - Sublist3r 
###  What is the flag value from the X-FLAG header? 

```console
user@thm:~$ ./sublist3r.py -d acmeitsupport.thm

          ____        _     _ _     _   _____
         / ___| _   _| |__ | (_)___| |_|___ / _ __
         \___ \| | | | '_ \| | / __| __| |_ \| '__|
          ___) | |_| | |_) | | \__ \ |_ ___) | |
         |____/ \__,_|_.__/|_|_|___/\__|____/|_|

         # Coded By Ahmed Aboul-Ela - @aboul3la

[-] Enumerating subdomains now for acmeitsupport.thm
[-] Searching now in Baidu..
[-] Searching now in Yahoo..
[-] Searching now in Google..
[-] Searching now in Bing..
[-] Searching now in Ask..
[-] Searching now in Netcraft..
[-] Searching now in Virustotal..
[-] Searching now in ThreatCrowd..
[-] Searching now in SSL Certificates..
[-] Searching now in PassiveDNS..
[-] Searching now in Virustotal..
[-] Total Unique Subdomains Found: 2
web55.acmeitsupport.thm
www.acmeitsupport.thm
user@thm:~$ 
```
{: .nolineno }

Answer : web55.acmeitsupport.thm

## TASK 6 : Virtual Hosts 
### What is the first subdomain discovered?

```console
root@ip-10-10-79-200:~# ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.48.198 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.48.198
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt
 :: Header           : Host: FUZZ.acmeitsupport.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

18                      [Status: 200, Size: 2395, Words: 503, Lines: 52]
2                       [Status: 200, Size: 2395, Words: 503, Lines: 52]
19                      [Status: 200, Size: 2395, Words: 503, Lines: 52]
17                      [Status: 200, Size: 2395, Words: 503, Lines: 52]
10                      [Status: 200, Size: 2395, Words: 503, Lines: 52]
accounts                [Status: 200, Size: 2395, Words: 503, Lines: 52]
[...]
adkit                   [Status: 200, Size: 2395, Words: 503, Lines: 52]
ad                      [Status: 200, Size: 2395, Words: 503, Lines: 52]
adam                    [Status: 200, Size: 2395, Words: 503, Lines: 52]
activestat              [Status: 200, Size: 2395, Words: 503, Lines: 52]
administrators          [Status: 200, Size: 2395, Words: 503, Lines: 52]
ads                     [Status: 200, Size: 2395, Words: 503, Lines: 52]
```
{: .nolineno }

All those are false positive so we need to exclude all results with a size 2395 :

```console
root@ip-10-10-79-200:~# ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.48.198 -fs 2395

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.48.198
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt
 :: Header           : Host: FUZZ.acmeitsupport.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response size: 2395
________________________________________________

delta                   [Status: 200, Size: 51, Words: 7, Lines: 1]
yellow                  [Status: 200, Size: 56, Words: 8, Lines: 1]
:: Progress: [1907/1907] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```
{: .nolineno }

Answer : delta

### What is the second subdomain discovered?
Answer : yellow