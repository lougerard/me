---
title: Osquery - The Basics
author: CYB3RM3
name: CYB3RM3 | Osquery - The Basics
date: 2022-01-08 16:20:36 +0100
categories: [TryHackMe, Investigation]
tags: [Windows, OSquery, Relational Databse, SQL]
---

Let's cover the basics of Osquery.

THM Room [https://tryhackme.com/room/osqueryf8](https://tryhackme.com/room/osqueryf8)


## TASK 1 : Introduction
### Ready to learn Osquery! 
No Answer

## TASK 2 : Installation
### Attached VM was started. Ready to proceed.  
No Answer

## TASK 3 : Interacting with the Osquery Shell
### What is the Osquery version?
By the help menu, we can get general information by running the .show command :

```sql
osquery> .show
[1mosquery[0m - being built, with love.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
osquery 4.6.0.2
using SQLite 3.34.0

General settings:
     Flagfile:
       Config: filesystem (\Program Files\osquery\osquery.conf)
       Logger: filesystem (\Program Files\osquery\log\)
  Distributed: tls
     Database: ephemeral
   Extensions: core
       Socket: \\.\pipe\shell.em

Shell settings:
         echo: off
      headers: on
         mode: pretty
    nullvalue: ""
       output: stdout
    separator: "|"
        width:
[...]
```
{: .nolineno }

Answer : 4.6.0.2

### What is the SQLite version?
Answer : 3.34.0

### What is the default output mode?
Answer : pretty

### What is the meta-command to set the output to show one value per line?
Checking help again :

```sql
osquery> .help
Welcome to the osquery shell. Please explore your OS!
You are connected to a transient 'in-memory' virtual database.

[...]
.mode MODE       Set output mode where MODE is one of:
                   csv      Comma-separated values
                   column   Left-aligned columns see .width
                   line     One value per line
                   list     Values delimited by .separator string
                   pretty   Pretty printed SQL results (default)
[...]
```
{: .nolineno }

Answer : .mode line

### What are the 2 meta-commands to exit osqueryi?
Answer : .exit, .quit

## TASK 4 : Schema Documentation
### What table would you query to get the version of Osquery installed on the Windows endpoint?
The next questions are based on Osquery 4.6.0. Using filters correctly i got the answers :

![osquery_info](/images/thm/osqueryf8/osqueryf8_1.png)
_osquery info_

Answer : osquery_info

### How many tables are there for this version of Osquery?
Answer : 266

### How many of the tables for this version are compatible with Windows?
Answer : 96

### How many tables are compatible with Linux?
Answer : 155

### What is the first table listed that is compatible with both Linux and Windows?
Answer : arp_cache

## TASK 5 : Creating queries
### What is the query to show the username field from the users table where the username is 3 characters long and ends with 'en'? (use single quotes in your answer) 
Answer : select username from users where username like '_en'

## TASK 6 : Using Kolide Fleet
### What is the Osquery Enroll Secret?

![osquery Enroll Secret](/images/thm/osqueryf8/osqueryf8_2.png)
_osquery Enroll Secret_

Answer : k3hFh30bUrU7nAC3DmsCCyb1mT8HoDkt

### What is the Osquery version?

![osquery Version](/images/thm/osqueryf8/osqueryf8_3.png)
_osquery Version_

Answer : 4.2.0

### What is the path for the running osqueryd.exe process?

![osquery Path](/images/thm/osqueryf8/osqueryf8_4.png)
_osquery Path_

With the following query : "SELECT * FROM processes" then filtering on cwd=osqueryd.exe

Answer : c:\Users\Administrator\Desktop\launcher\windows\osqueryd.exe

## TASK 7 : Osquery extensions
### According to the polylogyx readme, how many 'features' does the plug-in add to the Osquery core?
Check the github link <https://github.com/polylogyx/osq-ext-bin> : 

![osquery Core Version](/images/thm/osqueryf8/osqueryf8_5.png)
_osquery Core Version_

![osquery Core](/images/thm/osqueryf8/osqueryf8_6.png)
_osquery Core_

Answer : 23

## TASK 8 : Linux and Osquery
### What is the 'current_value' for kernel.osrelease?

```sql
osquery> SELECT * FROM kernel_info;
+-----------------------+------------+---------+--------+
| version               | arguments  | path    | device |
+-----------------------+------------+---------+--------+
| 4.4.0-17763-Microsoft | init=/init | /kernel |        |
+-----------------------+------------+---------+--------+
```
{: .nolineno }

Answer : 4.4.0-17763-Microsoft

### What is the uid for the bravo user?

```sql
osquery> SELECT * FROM users WHERE username="bravo";
+------+------+------------+------------+----------+-------------+-------------+-----------+------+
| uid  | gid  | uid_signed | gid_signed | username | description | directory   | shell     | uuid |
+------+------+------------+------------+----------+-------------+-------------+-----------+------+
| 1002 | 1002 | 1002       | 1002       | bravo    | ,,,         | /home/bravo | /bin/bash |      |
+------+------+------------+------------+----------+-------------+-------------+-----------+------+
or SELECT uid FROM users WHERE username="bravo";
```
{: .nolineno }

Answer : 1002

### One of the users performed a 'Binary Padding' attack. What was the target file in the attack?

```sql
osquery> select * from shell_history;
+------+------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| uid  | time | command                                                                                                                                                                                                                                                                                                      | history_file                  |
+------+------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 1000 | 0    |                                                                                                                                                                                                                                                                                                              | /home/tryhackme/.bash_history |
| 1000 | 0    | exit                                                                                                                                                                                                                                                                                                         | /home/tryhackme/.bash_history |
| 1000 | 0    | pwd                                                                                                                                                                                                                                                                                                          | /home/tryhackme/.bash_history |
| 1000 | 0    | ls                                                                                                                                                                                                                                                                                                           | /home/tryhackme/.bash_history |
| 1000 | 0    | cp ../charlie/notes .                                                                                                                                                                                                                                                                                        | /home/tryhackme/.bash_history |
| 1000 | 0    | md5sum notes                                                                                                                                                                                                                                                                                                 | /home/tryhackme/.bash_history |
| 1000 | 0    | mv notes notsus                                                                                                                                                                                                                                                                                              | /home/tryhackme/.bash_history |
| 1000 | 0    | dd if=/dev/zero bs=1 count=1 >> notsus                                                                                                                                                                                                                                                                       | /home/tryhackme/.bash_history |
| 1000 | 0    | md5sum notsus                                                                                                                                                                                                                                                                                                | /home/tryhackme/.bash_history |
| 1000 | 0    | exit 
```
{: .nolineno }

Answer : notsus

### What is the hash value for this file?

```console
tryhackme@WIN-FG4Q5UQP406:~$ md5sum notsus
3df6a21c6d0c554719cffa6ee2ae0df7  notsus
```
{: .nolineno }

Answer : 3df6a21c6d0c554719cffa6ee2ae0df7

### Check all file hashes in the home directory for each user. One file will not show any hashes. Which file is that?

```sql
osquery> select md5,directory from hash where path='/home/tryhackme/fleet.zip';
W0108 05:30:55.110817   694 filesystem.cpp:134] Cannot read file that exceeds size limit: /home/tryhackme/fleet.zip
+-----+-----------------+
| md5 | directory       |
+-----+-----------------+
|     | /home/tryhackme |
+-----+-----------------+
```
{: .nolineno }

Trial/error on file in users home's directory.

Answer : fleet.zip

### There is a file that is categorized as malicious in one of the home directories. Query the Yara table to find this file. Use the sigfile which is saved in '/var/osquery/yara/scanner.yara'. Which file is it?
Checking interesting files to scan :

```console
tryhackme@WIN-FG4Q5UQP406:/home/alpha$ ls
tryhackme@WIN-FG4Q5UQP406:/home/alpha$ cd ../bravo/
tryhackme@WIN-FG4Q5UQP406:/home/bravo$ ls
tryhackme@WIN-FG4Q5UQP406:/home/bravo$ cd ../charlie/
tryhackme@WIN-FG4Q5UQP406:/home/charlie$ ls
notes
tryhackme@WIN-FG4Q5UQP406:/home/charlie$ cd ../tryhackme/
tryhackme@WIN-FG4Q5UQP406:~$ ls
fleet  fleet.zip  notsus  server.cert  server.csr  server.key
tryhackme@WIN-FG4Q5UQP406:~$
```
{: .nolineno }

```sql
osquery> select * from yara WHERE sigfile='/var/osquery/yara/scanner.yara' and path='/home/charlie/notes';
+---------------------+------------------------------------+-------+-----------+--------------------------------+------------------------------------+------+
| path                | matches                            | count | sig_group | sigfile                        | strings                            | tags |
+---------------------+------------------------------------+-------+-----------+--------------------------------+------------------------------------+------+
| /home/charlie/notes | eicar_av_test,eicar_substring_test | 2     |           | /var/osquery/yara/scanner.yara | $eicar_regex:0,$eicar_substring:1b |      |
+---------------------+------------------------------------+-------+-----------+--------------------------------+------------------------------------+------+
```
{: .nolineno }

Answer : notes

### What were the 'matches'?
Answer : eicar_av_test,eicar_substring_test

### Scan the file from Q#3 with the same Yara file. What is the entry for 'strings'?

```sql
osquery> select * from yara WHERE sigfile='/var/osquery/yara/scanner.yara' and path='/home/tryhackme/notsus';
+------------------------+----------------------+-------+-----------+--------------------------------+---------------------+------+
| path                   | matches              | count | sig_group | sigfile                        | strings             | tags |
+------------------------+----------------------+-------+-----------+--------------------------------+---------------------+------+
| /home/tryhackme/notsus | eicar_substring_test | 1     |           | /var/osquery/yara/scanner.yara | $eicar_substring:1b |      |
+------------------------+----------------------+-------+-----------+--------------------------------+---------------------+------+
```
{: .nolineno }

Answer : $eicar_substring:1b

## TASK 9 : Windows and Osquery

### What is the description for the Windows Defender Service?
If you already know  the service name for WIndows Defender then you get directly 

```sql
osquery> select description from services where name="WinDefend";
+--------------------------------------------------------------------------+
| description                                                              |
+--------------------------------------------------------------------------+
| Helps protect users from malware and other potentially unwanted software |
+--------------------------------------------------------------------------+
```
{: .nolineno }

Otherwise, tried with the wildcard search :

```sql
osquery> select name,description from services where name like "WinD%";
+-----------+--------------------------------------------------------------------------+
| name      | description                                                              |
+-----------+--------------------------------------------------------------------------+
| WinDefend | Helps protect users from malware and other potentially unwanted software |
+-----------+--------------------------------------------------------------------------+
```
{: .nolineno }

Answer : Helps protect users from malware and other potentially unwanted software

### There is another security agent on the Windows endpoint. What is the name of this agent?

```sql
osquery> SELECT name,publisher from programs;
+--------------------------------------------------------------------+-----------------------+
| name                                                               | publisher             |
+--------------------------------------------------------------------+-----------------------+
| VMware Tools                                                       | VMware, Inc.          |
| AlienVault Agent                                                   | AlienVault Inc.       |
| Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.24.28127        | Microsoft Corporation |
| Microsoft Visual C++ 2019 X64 Additional Runtime - 14.24.28127     | Microsoft Corporation |
| Amazon SSM Agent                                                   | Amazon Web Services   |
| Google Chrome                                                      | Google LLC            |
| Microsoft Visual C++ 2015-2019 Redistributable (x64) - 14.24.28127 | Microsoft Corporation |
| Microsoft Visual C++ 2019 X86 Minimum Runtime - 14.24.28127        | Microsoft Corporation |
| Amazon SSM Agent                                                   | Amazon Web Services   |
| Microsoft Visual C++ 2015-2019 Redistributable (x86) - 14.24.28127 | Microsoft Corporation |
| Microsoft Visual C++ 2019 X86 Additional Runtime - 14.24.28127     | Microsoft Corporation |
+--------------------------------------------------------------------+-----------------------+
```
{: .nolineno }

Answer : AlienVault Agent

### What is required with win_event_log_data?
Checking .shema win_event_log_data

Answer : source

### How many sources are returned for win_event_log_channels?

```console
C:\Users\Administrator>osqueryi --allow-unsafe --extension "C:\Program Files\osquery\extensions\osq-ext-bin\plgx_win_extension.ext.exe"
Using a [1mvirtual database[0m. Need help, type '.help'
osquery> Done StartDriver.
osquery> select count (*) from win_event_log_channels;
+-----------+
| count (*) |
+-----------+
| 1076      |
+-----------+
```
{: .nolineno }

Answer : 1076

### What is the schema for win_event_log_data?
Query the schema for win_event_log_data :

```sql
osquery> .schema win_event_log_data
CREATE TABLE win_event_log_data(`time` BIGINT, `datetime` TEXT, `source` TEXT, `provider_name` TEXT, `provider_guid` TEXT, `eventid` INTEGER, `task` INTEGER, `level` INTEGER, `keywords` BIGINT, `data` TEXT, `eid` TEXT HIDDEN);

```
{: .nolineno }

Answer : 

```sql
CREATE TABLE win_event_log_data(`time` BIGINT, `datetime` TEXT, `source` TEXT, `provider_name` TEXT, `provider_guid` TEXT, `eventid` INTEGER, `task` INTEGER, `level` INTEGER, `keywords` BIGINT, `data` TEXT, `eid` TEXT HIDDEN);
```
{: .nolineno }

### The previous file scanned on the Linux endpoint with Yara is on the Windows endpoint.  What date/time was this file first detected? (Answer format: YYYY-MM-DD HH:MM:SS)
First we need the exact source text for windows defender :

```sql
osquery> select * from win_event_log_channels where source like "%defend%";
+------------------------------------------------+
| source                                         |
+------------------------------------------------+
| Microsoft-Windows-Windows Defender/Operational |
| Microsoft-Windows-Windows Defender/WHC         |
+------------------------------------------------+
```
{: .nolineno }

Then googling the Microsoft Defender page <https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide> give us the eventid for PUA : 1116

Finally we can query the win_event_log_data :

```sql
osquery> select datetime from win_event_log_data where source="Microsoft-Windows-Windows Defender/Operational" and eventid="1116";
+--------------------------------+
| datetime                       |
+--------------------------------+
| 2021-04-01T00:50:44.637359900Z |
| 2021-04-01T00:51:09.673408800Z |
+--------------------------------+
```
{: .nolineno }

Answer : 2021-04-01T 00:50:44

### What is the query to find the first Sysmon event? Select only the event id, order by date/time, and limit the output to only 1 entry.
I did it in 3 steps :

1- get the source :

```sql
osquery> select time,eventid from win_event_log_data where source like "%sysmon%";
E0108 06:58:49.428690  3816 plgx_win_evt_log_data_table.cpp:41] Provide 'source' as input in query. Use 'win_event_log_channels' table for help.
osquery> select time,eventid from win_event_log_channels where source like "%sysmon%";
Error: no such column: time
osquery> select eventid from win_event_log_channels where source like "%sysmon%";
Error: no such column: eventid
osquery> select * from win_event_log_channels where source like "%sysmon%";
+--------------------------------------+
| source                               |
+--------------------------------------+
| Microsoft-Windows-Sysmon/Operational |
+--------------------------------------+
```
{: .nolineno }

2- craft initial query : 

```sql
select eventid from win_event_log_data where source="Microsoft-Windows-Sysmon/Operational"
```
{: .nolineno }

3- apply condition ORDERBY and limit to 1 : ORDER BY datetime LIMIT 1;

Answer : 

```sql
select eventid from win_event_log_data where source="Microsoft-Windows-Sysmon/Operational" ORDER BY datetime LIMIT 1;
```
{: .nolineno }

### What is the Sysmon event id?
Result from the query of the previous question.

Answer : 16

## TASK 10 : Conclusion 
### Leveled up with Osquery! 
No Answer.