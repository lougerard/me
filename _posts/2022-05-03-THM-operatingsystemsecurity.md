---
title: Operating System Security
author: CYB3RM3
name: CYB3RM3 | Operating System Security
date: 2022-05-03 20:35:53 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, Privesc, Linux]
---

This room introduces users to operating system security and demonstrates SSH authentication on Linux.

THM Room [https://tryhackme.com/room/operatingsystemsecurity](https://tryhackme.com/room/operatingsystemsecurity)


## TASK 1 : Introduction to Operating System Security 
### Which of the following is not an operating system?
        AIX
        Android
        Chrome OS
        Solaris
        Thunderbird

Thunderbird is an email application.

Answer : Thunderbird

## TASK 2 : Common Examples of OS Security 
### Which of the following is a strong password, in your opinion?
        iloveyou
        1q2w3e4r5t
        LearnM00r
        qwertyuiop

The passwords 1, 2 and 4 are in the list of top 20 most common passwords.

Answer : LearnM00r

## TASK 3 : Practical Example of OS Security 

### Based on the top 7 passwords, let’s try to find Johnny’s password. What is the password for the user johnny?

Lest connect in SSH, then tried the top 7 common passwords to find Johnny's password :

```console
root@ip-10-10-224-97:~# ssh sammie@10.10.47.189
The authenticity of host '10.10.47.189 (10.10.47.189)' can't be established.
ECDSA key fingerprint is SHA256:IFP+sTfHTDm72Ta2zfK9XjKASr30+ya4ic/ApEIziio.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.47.189' (ECDSA) to the list of known hosts.
sammie@10.10.47.189's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-100-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue  3 May 18:28:03 UTC 2022

  System load:  0.33              Processes:             113
  Usage of /:   54.2% of 6.53GB   Users logged in:       0
  Memory usage: 22%               IPv4 address for eth0: 10.10.47.189
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Wed Mar  2 08:00:25 2022 from 10.20.30.1
sammie@beginner-os-security:~$ ls
country.txt  draft.md  icon.png  password.txt  profile.jpg
sammie@beginner-os-security:~$ cat password.txt 
sammie
dragon
sammie@beginner-os-security:~$ cat country.txt 
UK
sammie@beginner-os-security:~$ su johnny
Password: 
su: Authentication failure
sammie@beginner-os-security:~$ su johnny
Password: 
su: Authentication failure
sammie@beginner-os-security:~$ su johnny
Password: 
su: Authentication failure
sammie@beginner-os-security:~$ su johnny
Password: 
su: Authentication failure
sammie@beginner-os-security:~$ su johnny
Password: 
su: Authentication failure
sammie@beginner-os-security:~$ su johnny
Password: 
su: Authentication failure
sammie@beginner-os-security:~$ su johnny
Password: 
johnny@beginner-os-security:/home/sammie$ 
```
{: .nolineno }

The last one, "abc123", works !

Answer : abc123

### Once you are logged in as Johnny, use the command history to check the commands that Johnny has typed. We expect Johnny to have mistakenly typed the root password instead of a command. What is the root password?

using the history command for Johnny :

```console
johnny@beginner-os-security:/home/sammie$ history
    1  ls
    2  vi notes.txt
    3  mv notes.txt coffee.txt
    4  vi cheese.txt
    5  wget -c https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png
    6  ls
    7  su - root
    8  happyHack!NG
    9  su - root
   10  whoami
   11  ls
   12  cat coffee.txt 
   13  whoami
   14  pwd
   15  date
   16  exit
   17  clear
   18  history
```
{: .nolineno }

Answer : happyHack!NG

### While logged in as Johnny, use the command su - root to switch to the root account. Display the contents of the file flag.txt in the root directory. What is the content of the file?

Using the root password to find the flag :

```console
johnny@beginner-os-security:/home/sammie$ su - root
Password: 
root@beginner-os-security:~# ls
flag.txt  snap
root@beginner-os-security:~# cat flag.txt 
THM{YouGotRoot}
```
{: .nolineno }

Answer : THM{YouGotRoot}