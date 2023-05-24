---
title: Content Discovery  
author: CYB3RM3
name: CYB3RM3 | Content Discovery  
date: 2021-10-03 10:49:15 +0100
categories: [TryHackMe, Web]
tags: [Web]
---

Learn the various ways of discovering hidden or private content on a webserver that could lead to new vulnerabilities.
THM Room [https://tryhackme.com/room/contentdiscovery](https://tryhackme.com/room/contentdiscovery)


## TASK 1 : What Is Content Discovery?
### What is the Content Discovery method that begins with M?
Answer : Manually

### What is the Content Discovery method that begins with A?
Answer : Automated

### What is the Content Discovery method that begins with O?
Answer : OSINT

## TASK 2 : Manually Discovery - Robots.txt
### What is the directory in the robots.txt that isn't allowed to be viewed by web crawlers?

```console
root@ip-10-10-17-217:~# curl http://10.10.45.128/robots.txt
User-agent: *
Allow: /
Disallow: /staff-portal
```
{: .nolineno }

Answer : /staff-portal

## TASK 3 : Manual Discovery - Favicon
### What framework did the favicon belong to?

>[...] OWASP host a database of common framework icons that you can use to check against the targets favicon <https://wiki.owasp.org/index.php/OWASP_favicon_database>[...]

Looking to this database and we see it's all md5 of several common favicon. Let's get the md5 for or favicon here :

```console
root@ip-10-10-17-217:~# curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1406  100  1406    0     0  11158      0 --:--:-- --:--:-- --:--:-- 11158
f276b19aabcb4ae8cda4d22625c6735f  -
```
{: .nolineno }

Compare this md5 on the webpage and i got f276b19aabcb4ae8cda4d22625c6735f:cgiirc (0.5.9)

Answer : cgiirc

## TASK 4 : Manual Discovery - Sitemap.xml
### What is the path of the secret area that can be found in the sitemap.xml file? 

```console
root@ip-10-10-17-217:~# curl http://10.10.45.128/sitemap.xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    [...]
    <url>
        <loc>http://10.10.45.128/s3cr3t-area</loc>
        <lastmod>2021-07-19T13:07:32+00:00</lastmod>
        <priority>0.80</priority>
    </url>
</urlset>
```
{: .nolineno }

Answer : /s3cr3t-area

## TASK 5 : Manually Discovery - HTTP Headers
### What is the flag value from the X-FLAG header? 

```console
/urlset>root@ip-10-10-1curl http://10.10.45.128 -v
* Rebuilt URL to: http://10.10.45.128/
*   Trying 10.10.45.128...
* TCP_NODELAY set
* Connected to 10.10.45.128 (10.10.45.128) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.10.45.128
> User-Agent: curl/7.58.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx/1.18.0 (Ubuntu)
< Date: Sat, 02 Oct 2021 16:14:56 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-FLAG: THM{HEADER_FLAG}
< 
<!--
This page is temporary while we work on the new homepage @ /new-home-beta
-->
```
{: .nolineno }

Answer : THM{HEADER_FLAG}

## TASK 6 : Manual Discovery - Framework Stack
### What is the flag from the framework's administration portal?

```console
root@ip-10-10-17-217:~# curl http://10.10.45.128/
<!--
This page is temporary while we work on the new homepage @ /new-home-beta
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Acme IT Support - Home</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.12.0/css/all.css" integrity="sha384-ekOryaXPbeCpWQNxMwSWVvQ0+1VrStoPJq54shlYhR8HzQgig1v5fas6YgOqLoKz" crossorigin="anonymous">
        <link rel="stylesheet" href="/assets/bootstrap.min.css">
    <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
[...]
<!--
Page Generated in 0.03203 Seconds using the THM Framework v1.2 ( https://static-labs.tryhackme.cloud/sites/thm-web-framework )
```
{: .nolineno }

Going to the link in the comment and looking in documentation :

![Documentation](/images/thm/contentdiscovery/contentdiscovery_1.png)
_Documentation_

![Framework login](/images/thm/contentdiscovery/contentdiscovery_2.png)
_Framework login_

Answer : THM{CHANGE_DEFAULT_CREDENTIALS}

## TASK 7 : OSINT - Google Hacking / Dorking
### What Google dork operator can be used to only show results from a particular site?
Answer : site:

## TASK 8 : OSINT - Wappalyzer
### What online tool can be used to identify what technologies a website is running?
Answer : Wappalyzer

## TASK 9 : OSINT - Wayback Machine
### Update me.. 
No Answer

## TASK 10 : OSINT - GitHub
### What is Git? 
Answer : version control system

## TASK 11 : OSINT - S3 Buckets
### What URL format do Amazon S3 buckets end in? 
Answer : .s3.amazonaws.com

## TASK 12 : Automated Discovery

3 method here (ffuf, dirb, gobuster) :

```console
root@ip-10-10-79-200:~# ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.141.27/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.141.27/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

assets                  [Status: 301, Size: 178, Words: 6, Lines: 8]
contact                 [Status: 200, Size: 3108, Words: 747, Lines: 65]
customers               [Status: 302, Size: 0, Words: 1, Lines: 1]
development.log         [Status: 200, Size: 27, Words: 5, Lines: 1]
monthly                 [Status: 200, Size: 28, Words: 4, Lines: 1]
news                    [Status: 200, Size: 2538, Words: 518, Lines: 51]
private                 [Status: 301, Size: 178, Words: 6, Lines: 8]
robots.txt              [Status: 200, Size: 46, Words: 4, Lines: 3]
sitemap.xml             [Status: 200, Size: 1383, Words: 260, Lines: 43]
:: Progress: [4655/4655] :: Job [1/1] :: 4236 req/sec :: Duration: [0:00:01] :: Errors: 0 ::
```
{: .nolineno }

```console
root@ip-10-10-79-200:~# dirb http://10.10.141.27/ /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sun Oct  3 09:40:13 2021
URL_BASE: http://10.10.141.27/
WORDLIST_FILES: /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt

-----------------

GENERATED WORDS: 4654                                                          

---- Scanning URL: http://10.10.141.27/ ----
==> DIRECTORY: http://10.10.141.27/assets/                                                                          
+ http://10.10.141.27/contact (CODE:200|SIZE:3108)                                                                  
+ http://10.10.141.27/customers (CODE:302|SIZE:0)                                                                   
+ http://10.10.141.27/development.log (CODE:200|SIZE:27)                                                            
+ http://10.10.141.27/monthly (CODE:200|SIZE:28)                                                                    
+ http://10.10.141.27/news (CODE:200|SIZE:2538)                                                                     
==> DIRECTORY: http://10.10.141.27/private/                                                                         
+ http://10.10.141.27/robots.txt (CODE:200|SIZE:46)                                                                 
+ http://10.10.141.27/sitemap.xml (CODE:200|SIZE:1383)                                                              
                                                                                                                    
---- Entering directory: http://10.10.141.27/assets/ ----
==> DIRECTORY: http://10.10.141.27/assets/avatars/                                                                  
                                                                                                                    
---- Entering directory: http://10.10.141.27/private/ ----
+ http://10.10.141.27/private/index.php (CODE:200|SIZE:49)                                                          
                                                                                                                    
---- Entering directory: http://10.10.141.27/assets/avatars/ ----
                                                                                                                    
-----------------
END_TIME: Sun Oct  3 09:40:24 2021
DOWNLOADED: 18616 - FOUND: 8
```
{: .nolineno }

```console
root@ip-10-10-79-200:~# gobuster dir --url http://10.10.141.27/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.141.27/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2021/10/03 09:41:13 Starting gobuster
===============================================================
/assets (Status: 301)
/contact (Status: 200)
/customers (Status: 302)
/development.log (Status: 200)
/monthly (Status: 200)
/news (Status: 200)
/private (Status: 301)
/robots.txt (Status: 200)
/sitemap.xml (Status: 200)
===============================================================
2021/10/03 09:41:14 Finished
===============================================================
```
{: .nolineno }


### What is the name of the directory beginning "/mo...." that was discovered?
Answer : /monthly

### What is the name of the log file that was discovered?
Answer : /development.log