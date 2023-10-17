---
title: Network Services 2
author: CYB3RM3
name: CYB3RM3 | Network Services 2
date: 2023-10-17 07:11:15 +0100
categories: [TryHackMe, Network Exploitation Basics]
tags: [Network, Enumeration, Misconfiguration, Complete Beginner]
---

Enumerating and Exploiting More Common Network Services & Misconfigurations

THM Room : [https://tryhackme.com/room/networkservices2](https://tryhackme.com/room/networkservices2)


## TASK 1 Get Connected
### Ready? Let's get going!
No Answer.

## TASK 2 Understanding NFS
### What does NFS stand for?
Answer : Network File System

### What process allows an NFS client to interact with a remote directory as though it was a physical device?
Answer : Mounting

### What does NFS use to represent files and directories on the server?
Answer : file handle

### What protocol does NFS use to communicate between the server and client?
Answer : RPC

### What two pieces of user data does the NFS server take as parameters for controlling user permissions? Format: parameter 1 / parameter 2
Answer : user id / group id

### Can a Windows NFS server share files with a Linux client? (Y/N)
Answer : Y

### Can a Linux NFS server share files with a MacOS client? (Y/N)
Answer : Y

### What is the latest version of NFS? [released in 2016, but is still up to date as of 2020] This will require external research.
Answer : 4.2

## TASK 3 Enumerating NFS
### Conduct a thorough port scan scan of your choosing, how many ports are open?
Answer : 7

### Which port contains the service we're looking to enumerate?
Answer : 2049

### Now, use /usr/sbin/showmount -e [IP] to list the NFS shares, what is the name of the visible share?
Answer : /home

### Then, use the mount command we broke down earlier to mount the NFS share to your local machine. Change directory to where you mounted the share- what is the name of the folder inside?
Answer : cappucino

### Have a look inside this directory, look at the files. Looks like  we're inside a user's home directory...
No Answer.

### Interesting! Let's do a bit of research now, have a look through the folders. Which of these folders could contain keys that would give us remote access to the server?
Answer : .ssh

### Which of these keys is most useful to us?
Answer : id_rsa

### Can we log into the machine using ssh -i <key-file> <username>@<ip> ? (Y/N)
Answer : Y

## TASK 4 Exploiting NFS
### First, change directory to the mount point on your machine, where the NFS share should still be mounted, and then into the user's home directory.
No Answer.

### Download the bash executable to your Downloads directory. Then use "cp ~/Downloads/bash ." to copy the bash executable to the NFS share. The copied bash shell must be owned by a root user, you can set this using "sudo chown root bash"
No Answer.

### Now, we're going to add the SUID bit permission to the bash executable we just copied to the share using "sudo chmod +[permission] bash". What letter do we use to set the SUID bit set using chmod?
Answer : s

### Let's do a sanity check, let's check the permissions of the "bash" executable using "ls -la bash". What does the permission set look like? Make sure that it ends with -sr-x.
Answer : -rwsr-sr-x

### Now, SSH into the machine as the user. List the directory to make sure the bash executable is there. Now, the moment of truth. Lets run it with "./bash -p". The -p persists the permissions, so that it can run as root with SUID- as otherwise bash will sometimes drop the permissions.
No Answer

### Great! If all's gone well you should have a shell as root! What's the root flag?
Answer : THM{nfs_got_pwned}

## TASK 5 Understanding SMTP
### What does SMTP stand for?
Answer : Simple Mail Transfer Protocol

### What does SMTP handle the sending of? (answer in plural)
Answer : emails

### What is the first step in the SMTP process?
Answer : SMTP handshake

### What is the default SMTP port?
Answer : 25

### Where does the SMTP server send the email if the recipient's server is not available?
Answer : smtp queue

### On what server does the Email ultimately end up on?
Answer : POP/IMAP

### Can a Linux machine run an SMTP server? (Y/N)
Answer : Y

### Can a Windows machine run an SMTP server? (Y/N)
Answer : Y

## TASK 6 Enumerating SMTP
### First, lets run a port scan against the target machine, same as last time. What port is SMTP running on?
Answer : 25

### Okay, now we know what port we should be targeting, let's start up Metasploit. What command do we use to do this? If you would like some more help or practice using Metasploit, TryHackMe has a module on Metasploit that you can check out here: https://tryhackme.com/module/metasploit
Answer : msfconsole

### Let's search for the module "smtp_version", what's it's full module name?
Answer : auxiliary/scanner/smtp/smtp_version

### Great, now- select the module and list the options. How do we do this?
Answer : options

### Have a look through the options, does everything seem correct? What is the option we need to set?
Answer : RHOSTS

### Set that to the correct value for your target machine. Then run the exploit. What's the system mail name?
Answer : polosmtp.home

### What Mail Transfer Agent (MTA) is running the SMTP server? This will require some external research.
Answer : Postfix

### Good! We've now got a good amount of information on the target system to move onto the next stage. Let's search for the module "smtp_enum", what's it's full module name?
Answer : auxiliary/scanner/smtp/smtp_enum

### We're going to be using the "top-usernames-shortlist.txt" wordlist from the Usernames subsection of seclists (/usr/share/wordlists/SecLists/Usernames if you have it installed). Seclists is an amazing collection of wordlists. If you're running Kali or Parrot you can install seclists with: "sudo apt install seclists" Alternatively, you can download the repository from here. What option do we need to set to the wordlist's path?
Answer : USER_FILE

### Once we've set this option, what is the other essential paramater we need to set?
Answer : RHOSTS

### Now, run the exploit, this may take a few minutes, so grab a cup of tea, coffee, water. Keep yourself hydrated!
No Answer.

### Okay! Now that's finished, what username is returned?
Answer : administrator

## TASK 7 Exploiting SMTP
### What is the password of the user we found during our enumeration stage?
Answer : alejandro

### Great! Now, let's SSH into the server as the user, what is contents of smtp.txt
Answer : THM{who_knew_email_servers_were_c00l?}

## TASK 8 Understanding MySQL
### What type of software is MySQL?
Answer : relational database management system

### What language is MySQL based on?
Answer : SQL

### What communication model does MySQL use?
Answer : client-server

### What is a common application of MySQL?
Answer : back end database

### What major social network uses MySQL as their back-end database? This will require further research.
Answer : Facebook

## TASK 9 Enumerating MySQL
### As always, let's start out with a port scan, so we know what port the service we're trying to attack is running on. What port is MySQL using?
Answer : 3306

### Good, now- we think we have a set of credentials. Let's double check that by manually connecting to the MySQL server. We can do this using the command "mysql -h [IP] -u [username] -p"
No Answer.

### Okay, we know that our login credentials work. Lets quit out of this session with "exit" and launch up Metasploit.
No Answer.

### We're going to be using the "mysql_sql" module. Search for, select and list the options it needs. What three options do we need to set? (in descending order).
Answer : PASSWORD/RHOSTS/USERNAME

### Run the exploit. By default it will test with the "select version()" command, what result does this give you?
Answer : 5.7.29-0ubuntu0.18.04.1

### Great! We know that our exploit is landing as planned. Let's try to gain some more ambitious information. Change the "sql" option to "show databases". how many databases are returned?
Answer : 4

## TASK 10 Exploiting MySQL
### First, let's search for and select the "mysql_schemadump" module. What's the module's full name?
Answer : auxiliary/scanner/mysql/mysql_schemadump

### Great! Now, you've done this a few times by now so I'll let you take it from here. Set the relevant options, run the exploit. What's the name of the last table that gets dumped?
Answer : x$waits_global_by_latency

### Awesome, you have now dumped the tables, and column names of the whole database. But we can do one better... search for and select the "mysql_hashdump" module. What's the module's full name?
Answer : auxiliary/scanner/mysql/mysql_hashdump

### Again, I'll let you take it from here. Set the relevant options, run the exploit. What non-default user stands out to you?
Answer : carl

### Another user! And we have their password hash. This could be very interesting. Copy the hash string in full, like: bob:*HASH to a text file on your local machine called "hash.txt". What is the user/hash combination string?
Answer : carl:*EA031893AA21444B170FC2162A56978B8CEECE18

### Now, we need to crack the password! Let's try John the Ripper against it using: "john hash.txt" what is the password of the user we found?
Answer : doggie

### Awesome. Password reuse is not only extremely dangerous, but extremely common. What are the chances that this user has reused their password for a different service? What's the contents of MySQL.txt
Answer : THM{congratulations_you_got_the_mySQL_flag}

## TASK 11 Further Learning
### Congratulations! You did it!
No Answer.