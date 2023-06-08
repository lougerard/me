---
title:  MAL - Strings
author: CYB3RM3
name: CYB3RM3 | MAL - Strings
date: 2022-01-27 12:42:17 +0100
categories: [TryHackMe, Malware]
tags: [Malware, Malware analysis]
---

Investigating "strings" within an application and why these values are important!

THM Room [https://tryhackme.com/room/malstrings](https://tryhackme.com/room/malstrings)


## TASK 1 : What are "strings"?
### What is the name of the account that had the passcode of "12345678" in the intellian example discussed above?
A quick search on google to find the CVE related to this : CVE-2020-8000 :

![Account Name](/images/thm/malstrings/malstrings_1.png)
_Account Name_

Answer : intellian

### What is the CVE entry disclosed by the company "Teradata" in their "Viewpoint" Application that has a password within a string?
Per NIST <https://nvd.nist.gov/vuln/detail/CVE-2019-6499>, the CVE related is :

![CVE](/images/thm/malstrings/malstrings_2.png)
_CVE_

Answer : CVE-2019-6499

### According to OWASP's list of "Top Ten IoT" vulnerabilities, name the ranking this vulnerability would fall within, represented as text.
Checking OWASP top 10 <https://owasp.org/www-pdf-archive/OWASP-IoT-Top-10-2018-final.pdf> from 2018 :

![OWASP](/images/thm/malstrings/malstrings_3.png)
_OWASP_

Answer : one

## TASK 2 : Practical: Extracting "strings" From an Application
### What is the correct username required by the "LoginForm"?
If you don't have strings.exe or strings64.exe on windows, download it from sysinternal tools :

```console
strings64.exe LoginForm.exe > result_string.txt

result_string.txt 
[...]
bad allocation
85@
Unknown exception
bad array new length
bad cast
cmnatic
TryHackMeMerchWhen
THM{Not_So_Hidden_Flag}
Welcome to the login portal!
Enter your Username: 
Input your password: 
Access Granted!
Wrong username or password!
pause
string too long
h5@
[...]
```
{: .nolineno }

Answer : cmnatic

### What is the required password to authenticate with?
Answer : TryHackMeMerchWhen

### What is the "hidden" THM{} flag?
Answer : THM{Not_So_Hidden_Flag}

## TASK 3 : Strings in the Context of Malware
### What is the key term to describe a server that Botnets recieve instructions from?
Read the text.

Answer : Command and Control

### Name the discussed example malware that uses "strings" to store the bitcoin wallet addresses for payment
Answer : Wannacry

## TASK 4 : Practical: Finding Bitcoin Addresses in Ransomware (Deploy!)


### List the number of total transactions that the Bitcoin wallet used by the "Wannacry" author(s)

By the link <https://live.blockcypher.com/btc/address/13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94/> given in the text :

![BLOCKCYPHER](/images/thm/malstrings/malstrings_4.png)
_BLOCKCYPHER_

Answer : 143

### What is the Bitcoin Address stored within "ComplexCalculator.exe"
Using stings.exe on ComplexCalculatorv2.exe :

![Bitcoin Address](/images/thm/malstrings/malstrings_5.png)
_Bitcoin Address_

Answer : 1LVB65imeojrgC3JPZGBwWhK1BdVZ2vYNC

## TASK 5 : Summary 
### What is the name of the toolset provided by Microsoft that allows you to extract the "strings" of an application?
Answer : sysinternals

### What operator would you use to "pipe" or store the output of the strings command?
Answer : >

### What is the name of the currency that ransomware often uses for payment?
Answer : bitcoin