---
title: Linux System Hardening
author: CYB3RM3
name: CYB3RM3 | Linux System Hardening
date: 2023-09-23 11:21:20 +0100
categories: [TryHackMe, Security Engineer]
tags: [Linux, Hardening, Intro]
---

Learn how to improve the security posture of your Linux systems.

THM Room : [https://tryhackme.com/room/linuxsystemhardening](https://tryhackme.com/room/linuxsystemhardening)


## TASK 1 Introduction
###  Ensure that you satisfy the room prerequisites. 
No Answer.

## TASK 2 Physical Security
### What command can you use to create a password for the GRUB bootloader?

>"We can consider adding a GRUB password depending on the Linux system we want to protect. Many tools help achieve that. One tool is grub2-mkpasswd-pbkdf2, which prompts you to input your password twice and generates a hash for you. The resulting hash should be added to the appropriate configuration file depending on the Linux distribution (examples: Fedora and Ubuntu). This configuration would prevent unauthorised users from resetting your root password. It will require the user to supply a password to access advanced boot configurations via GRUB, including logging in with root access."

Answer : grub2-mkpasswd-pbkdf2

### What does PBKDF2 stand for?

Quick google search.

Answer : Password-Based Key Derivation Function 2

## TASK 3 Filesystem Partitioning and Encryption

### What does LUKS stand for?

>"There are various software systems and tools that provide encryption to Linux systems. Since many modern Linux distributions ship with LUKS (Linux Unified Key Setup), let’s cover it in more detail."

Answer : Linux Unified Key Setup

### We cannot attach external storage to the VM, so we have created a /home/tryhackme/secretvault.img file instead. It is encrypted with the password 2N9EdZYNkszEE3Ad. To access it, you need to open it using cryptsetup and then mount it to an empty directory, such as myvault. What is the flag in the secret vault?

```console
tryhackme@ip-10-10-251-28:~$ sudo cryptsetup luksOpen secretvault.img myVaultDrive
Enter passphrase for secretvault.img: 
tryhackme@ip-10-10-251-28:~$ sudo ls -l /dev/mapper/myVaultDrive and cryptsetup -v status myVaultDrive
ls: cannot access 'and': No such file or directory
ls: cannot access 'cryptsetup': No such file or directory
ls: cannot access 'status': No such file or directory
ls: cannot access 'myVaultDrive': No such file or directory
lrwxrwxrwx 1 root root 7 Sep 23 09:34 /dev/mapper/myVaultDrive -> ../dm-0
tryhackme@ip-10-10-251-28:~$ sudo mount /dev/mapper/myVaultDrive myvault
tryhackme@ip-10-10-251-28:~$ ls
myvault  secretvault.img
tryhackme@ip-10-10-251-28:~$ cd myvault/
tryhackme@ip-10-10-251-28:~/myvault$ ls
lost+found  task3_flag.txt
tryhackme@ip-10-10-251-28:~/myvault$ cat task3_flag.txt 
THM{LUKS_not_LUX}
tryhackme@ip-10-10-251-28:~/myvault$
```
{: .nolineno }

Answer : THM{LUKS_not_LUX}

## TASK 4 Firewall

### There is a firewall running on the Linux VM. It is allowing port 22 TCP as we can ssh into the machine. It is allowing another TCP port; what is it?

```console
tryhackme@ip-10-10-251-28:~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere                  
14298/udp                  ALLOW       Anywhere                  
12526/tcp                  ALLOW       Anywhere                  
22/tcp (v6)                ALLOW       Anywhere (v6)             
14298/udp (v6)             ALLOW       Anywhere (v6)             
12526/tcp (v6)             ALLOW       Anywhere (v6)             

tryhackme@ip-10-10-251-28:~$ 
```
{: .nolineno }

Answer : 12526

### What is the allowed UDP port?
Answer : 14298

## TASK 5 Remote Access
###  What flag is hidden in the sshd_config file? 

```console
tryhackme@ip-10-10-251-28:~$ cat /etc/ssh/sshd_config | grep "THM{"
# THM{secure_SEA_shell}
```
{: .nolineno }

Answer : THM{secure_SEA_shell}

## TASK 6 Securing User Accounts
### One way to disable an account is to edit the passwd file and change the account’s shell. What is the suggested value to use for the shell?

>"We should do the same for local services. In other words, we should set the shell to sbin/nologin for all the local service accounts such as www-data, mongo, and nginx, to name a few. The reason is that these services need accounts to run on the system but would never need to log in and access a shell. Any of these services could perhaps have an RCE (Remote Code Execution) vulnerability, and by setting the shell to nologin, we can at least prevent interactive logins for the account of the affected service."

Answer : sbin/nologin

### What is the name of the RedHat and Fedora systems sudoers group?

"Other distributions, such as RedHat and Fedora, refer to the sudoers group as wheel. Consequently, you would need to issue the following command:"

Answer : wheel

### What is the name of the sudoers group on Debian and Ubuntu systems?
Answer : sudo

### Other than tryhackme and ubuntu, what is the username that belongs to the sudoers group?

```console
tryhackme@ip-10-10-251-28:~$ cat /etc/group | grep sudo
sudo:x:27:ubuntu,tryhackme,blacksmith
```
{: .nolineno }

Answer : blacksmith

## TASK 7 Software and Services
### Besides FTPS, what is another secure replacement for TFTP and FTP? 

>"Instead of Telnet, the SSH protocol is now widely available. For example, the Secure File Transfer Protocol (SFTP) protocol provides a great alternative to the TFTP protocol. The critical point is that a secure alternative is selected and used."

Answer : SFTP

## TASK 8 Update and Upgrade Policies

### What command would you use to update an older Red Hat system?

>"You can update a RedHat or Fedora system using the following:

    dnf update on newer releases (Red Hat Enterprise Linux 8 and later)
    yum update on older releases (Red Hat Enterprise Linux 7 and earlier)
"

Answer : yum update

### What command would you use to update a modern Fedora system?

Answer : dnf update

### What two commands are required to update a Debian system? (Connect the two commands with &&.)

Answer : apt upgrade && apt update

### What does yum stand for?

Let's check on google : 

>"Yum, pour Yellowdog Updater Modified, est l’ancien gestionnaire de paquets des distributions GNU/Linux Fedora Linux, CentOS et Red Hat Enterprise Linux. Il a originellement été créé par Yellow Dog Linux. Il permet de gérer l’installation et la mise à jour des logiciels installés sur une distribution" <https://fr.wikipedia.org/wiki/Yellowdog_Updater,_Modified>

Answer : Yellowdog Updater Modified

### What does dnf stand for?

>"DNF or Dandified YUM[4][5][6] is the next-generation version of the Yellowdog Updater, Modified (yum), a package manager for .rpm-based Linux distributions. DNF was introduced in Fedora 18 in 2013;[7] it has been the default package manager since Fedora 22 in 2015,[8] Red Hat Enterprise Linux 8,[9] and OpenMandriva,[10] and is also an alternative package manager for Mageia. " <https://en.wikipedia.org/wiki/DNF_(software)>

Answer : Dandified YUM

### What flag is hidden in the sources.list file?

```console
tryhackme@ip-10-10-251-28:~$ cat /etc/apt/sources.list | grep "THM{"
# THM{not_Advanced_Persistent_Threat}
```
{: .nolineno }

Answer : THM{not_Advanced_Persistent_Threat}

## TASK 9 Audit and Log Configuration
### What command can you use to display the last 15 lines of kern.log?
Answer : tail -n 15 kern.log

### What command can you use to display the lines containing the word denied in the file secure?
Answer : grep secure denied

## TASK 10 Conclusion and Final Notes 
###  Ensure that you have taken note of all the commands presented in this room. 
No Answer.