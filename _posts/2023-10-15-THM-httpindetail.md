---
title: HTTP in detail
author: CYB3RM3
name: CYB3RM3 | HTTP in detail
date: 2023-10-15 16:25:15 +0100
categories: [TryHackMe, How The Web Works]
tags: [HTTP, Intro, Pre Security]
---

Learn about how you request content from a web server using the HTTP protocol

THM Room : [https://tryhackme.com/room/httpindetail](https://tryhackme.com/room/httpindetail)


## TASK 1 What is HTTP(S)?
### What does HTTP stand for?
Answer : HyperText Transfer Protocol

### What does the S in HTTPS stand for?
Answer : secure

### On the mock webpage on the right there is an issue, once you've found it, click on it. What is the challenge flag?
Answer : THM{INVALID_HTTP_CERT}

## TASK 2 Requests And Responses
### What HTTP protocol is being used in the above example?
Answer : HTTP/1.1

### What response header tells the browser how much data to expect?
Answer : Content-Length

## TASK 3 HTTP Methods
### What method would be used to create a new user account?
Answer : POST

### What method would be used to update your email address?
Answer : PUT

### What method would be used to remove a picture you've uploaded to your account?
Answer : DELETE

### What method would be used to view a news article?
Answer : GET

## TASK 4 HTTP Status Codes
### What response code might you receive if you've created a new user or blog post article?
Answer : 201

### What response code might you receive if you've tried to access a page that doesn't exist?
Answer : 404

### What response code might you receive if the web server cannot access its database and the application crashes?
Aswner : 503

### What response code might you receive if you try to edit your profile without logging in first?
Answer : 401

## TASK 5 Headers
### What header tells the web server what browser is being used?
Answer : User-Agent

### What header tells the browser what type of data is being returned?
Answer : Content-Type

### What header tells the web server which website is being requested?
Host

## TASK 6 Cookies
### Which header is used to save cookies to your computer?
Answer : Set-Cookie

## TASK 7 Making Requests
### Make a GET request to /room
Answer : THM{YOU'RE_IN_THE_ROOM}

### Make a GET request to /blog and using the gear icon set the id parameter to 1 in the URL field
Answer : THM{YOU_FOUND_THE_BLOG}

### Make a DELETE request to /user/1
Answer : THM{USER_IS_DELETED}

### Make a PUT request to /user/2 with the username parameter set to admin
Answer : THM{USER_HAS_UPDATED}

### POST the username of thm and a password of letmein to /login
Answer : THM{HTTP_REQUEST_MASTER}