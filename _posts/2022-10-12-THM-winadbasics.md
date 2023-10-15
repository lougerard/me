---
title: Active Directory Basics 
author: CYB3RM3
name: CYB3RM3 | Active Directory Basics 
date: 2022-10-12 09:12:30 +0100
categories: [TryHackMe, Red Teaming]
tags: [Active Directory, Windows, AD, Server]
---

This room will introduce the basic concepts and functionality provided by Active Directory.

THM Room [https://tryhackme.com/room/winadbasics](https://tryhackme.com/room/winadbasics)


## TASK 1 : Introduction
### Click and continue learning! 
No Answer

## TASK 2 : Windows Domain
### In a Windows domain, credentials are stored in a centralised repository called... 
Answer : Active Directory

### The server in charge of running the Active Directory services is called...
Answer : Domain Controller

## TASK 3 : Active Directory
###  Which group normally administrates all computers and resources in a domain?
Answer : Domain Admins

###  What would be the name of the machine account associated with a machine named TOM-PC?
Answer : TOM-PC$

### Suppose our company creates a new department for Quality Assurance. What type of containers should we use to group all Quality Assurance users so that policies can be applied consistently to them?
Answer : Organizational Units

## TASK 4 : Managing Users in AD
### What was the flag found on Sophie's desktop? 

After setting up the delegation on reset password for philip, we can now change sophie password and initiate a force password change at next logon :

![SetADAccountPassword](/images/thm/winadbasics/winadbasics_1.png)
_SetADAccountPassword_

Then when login to sophie's account, we'll be prompted to change the password :

![Sophie Session](/images/thm/winadbasics/winadbasics_2.png)
_Sophie Session_

Once logged in, we can retreive the flag on the desktop :

![Flag](/images/thm/winadbasics/winadbasics_3.png)
_Flag_

Answer : THM{thanks_for_contacting_support}

### The process of granting privileges to a user over some OU or other AD Object is called...
Answer : delegation

## TASK 5 : Managing Computers in AD
### After organising the available computers, how many ended up in the Workstations OU?

![Computers](/images/thm/winadbasics/winadbasics_4.png)
_Computers_

Answer : 7

### Is it recommendable to create separate OUs for Servers and Workstations? (yay/nay)
Answer : YAY

## TASK 6 : Group Policies
###  What is the name of the network share used to distribute GPOs to domain machines?
Answer : SYSVOL

### Can a GPO be used to apply settings to users and computers? (yay/nay)
Answer : YAY

## TASK 7 : Authentication Methods

### Will a current version of Windows use NetNTLM as the preferred authentication protocol by default? (yay/nay) 
Answer : NAY

### When referring to Kerberos, what type of ticket allows us to request further tickets known as TGS?
Answer : Ticket Granting Tickets

### When using NetNTLM, is a user's password transmitted over the network at any point? (yay/nay)
Answer : NAY

## TASK 8 : Tress, Forests and Trusts
### What is a group of Windows domains that share the same namespace called? 
Answer : tree

### What should be configured between two domains for a user in Domain A to access a resource in Domain B?
Answer : A trust relationship

## TASK 9 : Conclusion
###  Click and continue learning! 
No Answer.
