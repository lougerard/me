---
title: The Lay of the Land
author: CYB3RM3
name: CYB3RM3 | The Lay of the Land
date: 2022-02-03 00:52:49 +0100
categories: [TryHackMe, Red Teaming]
tags: [LOTL, Windows]
---

Learn about and get hands-on with common technologies and security products used in corporate environments; both host and network-based security solutions are covered.

THM Room [https://tryhackme.com/room/thelayoftheland](https://tryhackme.com/room/thelayoftheland)



## TASK 1 : Introduction
### Let's start learning! 
No Answer

## TASK 2 : Deploy the VM
### Let's discuss the common network infrastructure in the next task! 
No Answer

## TASK 3 : Network Infrastructure
###  Read the above!
Open ports (not full image) :

![Open ports](/images/thm/thelayoftheland/thelayoftheland_1.png)
_Open ports_

And the ARP table :

![ARP table](/images/thm/thelayoftheland/thelayoftheland_2.png)
_ARP table_

No Answer.

## TASK 4 : Active Directory (AD) environment
### Before going any further, ensure the attached machine is deployed and try what we discussed. Is the attached machine part of the AD environment? (Y|N)
Systeminfo command gives us many informations :

![Systeminfo](/images/thm/thelayoftheland/thelayoftheland_3.png)
_Systeminfo_

![Systeminfo](/images/thm/thelayoftheland/thelayoftheland_4.png)
_Systeminfo_

The info we are looking for can be filtered by piping the output with the "findstr" command :

![Domain](/images/thm/thelayoftheland/thelayoftheland_5.png)
_Domain_

Answer : Y

### If it is part of an AD environment, what is the domain name of the AD?
Answer : thmredteam.com

## TASK 5 : Users and Groups Management
### Use the Get-ADUser -Filter * -SearchBase command to list the available user accounts within THM OU in the thmredteam.com domain. How many users are available?
We can use the following crafted query in powershell :

```powershell
Get-ADUser -Filter * -SearchBase "OU=THM,DC=THMREDTEAM,DC=COM"
```
{: .nolineno }

![Get-ADUser](/images/thm/thelayoftheland/thelayoftheland_6.png)
_Get-ADUser_

Answer : 6

### Once you run the previous command, what is the UserPrincipalName (email) of the admin account?
Answer : thmadmin@thmredteam.com

## TASK 6 : Host Security Solution #1
### Enumerate the attached Windows machine and check whether the host-based firewall is enabled or not! (Y|N)
We can verify if host-based firewall is enabled by the comand :

```powershell
Get-NetFirewallProfile | Format-Table Name, Enabled
```
{: .nolineno }

![Get-NetFirewallProfile](/images/thm/thelayoftheland/thelayoftheland_7.png)
_Get-NetFirewallProfile_

Answer : N

### Using PowerShell cmdlets such Get-MpThreat can provide us with threats details that have been detected using MS Defender. Run it and answer the following: What is the file name that causes this alert to record?
Executing the command Get-MpThreat, we have in this case :

![Get-MpThreat](/images/thm/thelayoftheland/thelayoftheland_8.png)
_Get-MpThreat_

Answer : powerview.ps1

### Enumerate the firewall rules of the attached Windows machine. What is the port that is allowed under the THM-Connection rule?
We can checked the firewall rules with this command :

```powershell
Get-NetFirewallRule | select DisplayName, Enabled, Description
```
{: .nolineno }

Unfortunetely, this return lots of results :

![Get-NetFirewallRule](/images/thm/thelayoftheland/thelayoftheland_9.png)
_Get-NetFirewallRule_

To get a quick response we can pipe the output by searching the information we have : THM-Connection

```powershell
Get-NetFirewallRule | select DisplayName, Enabled, Description | findstr "THM-Connection"
```
{: .nolineno }

![THM-Connection](/images/thm/thelayoftheland/thelayoftheland_10.png)
_THM-Connection_

Answer : lsaiso

### In the next task, we will keep discussing the host security solution. I'm ready!
No Answer.

## TASK 7 : Host Security Solution #2
### We covered some of the common security endpoints we may encounter during the red team engagement. Let's discuss the network-based security solutions in the next task!
Verify if sysmon is installed and which events are log on the compromised endpoint :

![Host Security Solution](/images/thm/thelayoftheland/thelayoftheland_11.png)
_Host Security Solution_

No Answer

## TASK 8 : Network Security Solutions
### Read the above!
No Answer.

## TASK 9 : Applications and Services
###  Finally, we can see it is listening on port 8080. Now try to apply what we discussed and find the port number for THM Service. What is the port number?
I started with the command wmic to search in the installed applications with the keyword "THM" but it failed so just searched for service with "THM" filter in findstr.  Then i looked for the id or the process and finally the port on which it's listening :

![THM Service port number](/images/thm/thelayoftheland/thelayoftheland_12.png)
_THM Service port number_

Answer : 13337

### Visit the localhost on the port you found in Question #1. What is the flag?

Just curl the localhost :

```console
curl 127.0.0.1:13337
```
{: .nolineno }

![Flag 1](/images/thm/thelayoftheland/thelayoftheland_13.png)
_Flag 1_

Answer : THM{S3rv1cs_1s_3numerat37ed}

### Now enumerate the domain name of the domain controller, thmredteam.com, using the nslookup.exe, and perform a DNS zone transfer. What is the flag for one of the records?

Let's look on dns record with nslookup :

![Flag 2](/images/thm/thelayoftheland/thelayoftheland_14.png)
_Flag 2_

Answer : THM{DNS-15-Enumerated!}

## TASK 10 : Conclusion 
### Hope you enjoyed the room and keep learning! 
No Answer.