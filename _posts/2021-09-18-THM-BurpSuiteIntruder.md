---
title: Burp Suite - Intruder
author: CYB3RM3
name: CYB3RM3 | Burp Suite - Intruder
date: 2021-09-19 11:19:20 +0100
categories: [TryHackMe, Web]
tags: [Web, BurpSuite]
---

Learn how to use Repeater to duplicate requests in Burp Suite
THM Room [https://tryhackme.com/room/burpsuiteintruder](https://tryhackme.com/room/burpsuiteintruder)


## TASK 1 : Outline

###  Deploy the machine!
You should also deploy the AttackBox (using the "Start AttackBox" button at the top of the page) if you are not using your own attack VM.
Note: If you are not using the AttackBox and want to connect to this machine without the VPN, you can do so using this link once the machine has fully loaded and an IP address is displayed: https://10-10-36-215.p.thmlabs.com.

No Answer.


## TASK 2 : What is Intruder ?
### Which section of the Options sub-tab allows you to define what information will be captured in the Intruder results ?
Answer : Attack Results

### In which Intruder sub-tab can we define the "Attack type" for our planned attack ?
Answer : Positions

## TASK 3 : Position
### Have a play around with the positions selector. Make sure that you are comfortable with the processes of adding, clearing, and automatically selecting positions.
No Answer.

### Clear all selected positions
All positions are already selected, just click the "clear position" button.

No Answer.

### Select the value of the "Host" header and add it as a position.
Higligh the "host" value and click the button "set position"

No Answer.

### Clear this position, then click the "Auto" button again to reselect the default positions. Your editor should be back looking like it did in the first screenshot of this task.
No Answer.

## TASK 4 : Introduction
### Read the Attack Types Introduction.
No Answer.

## TASK 5 : Sniper
### f you were using Sniper to fuzz three parameters in a request, with a wordlist containing 100 words, how many requests would Burp Suite need to send to complete the attack?
requests = numberOfWords * numberOfPositions = 100 * 3

Answer : 300

### How many sets of payloads will Sniper accept for conducting an attack?
Answer : 1

### Sniper is good for attacks where we are only attacking a single parameter, aye or nay? :
[...] This quality makes Sniper very good for single-position attacks [...]

Answer : AYE

## TASK 6 : Battering Ram
### As a hypothetical question: you need to perform a Battering Ram Intruder attack on the example request above.
If you have a wordlist with two words in it (admin and Guest) and the positions in the request template look like this:
                        username=§pentester§&password=§Expl01ted§

What would the body parameters of the first request that Burp Suite sends be?                       

Answer : username=admin&password=admin

## TASK 7 : Pitchfork
### What is the maximum number of payload sets we can load into Intruder in Pitchfork mode?
Reading the text give us the info.

Answer : 20

## TASK 8 : Cluster Bomb
### We have three payload sets. The first set _Burp modify header flagcontains 100 lines; the second contains 2 lines; and the third contains 30 lines. How many requests will Intruder make using these payload sets in a Cluster Bomb attack ?
[...] This attack-type can create a huge amount of traffic (equal to the number of lines in each payload set multiplied together) [...]

Answer : 6000

## TASK 9 : Payloads
### Which payload type lets us load a list of words into a payload set ?
Answer : Simple list

### Which Payload Processing rule could we use to add characters at the end of each payload in the set ?
Kepp a look in the dropdown menu for adding a payload processing !

![Payload processing rule](/images/thm/burpIntruder/Burp Suite_ Intruder_1.png)
_Payload processing rule_

Answer : Add suffix

## TASK 10 : Example
### Download and unzip the BastionHostingCreds.zip zipfile. It doesn't matter whether you do this by clicking the download link in the task or by using the files hosted on your deployed machine.
No Answer.

### The zip file should contain four wordlists. These contain lists of leaked emails, usernames, and passwords, respectively. The last list contains the combined email and password lists. We will be using the usernames.txt and passwords.txt lists.
No Answer.

### Navigate to http://10.10.90.45/support/login in your browser. Activate the Burp Proxy and try to log in, catching the request in your proxy. 
Note: It doesn't matter what credentials you use here -- we just need the request.
No Answer.

### Send the request from the Proxy to Intruder by right-clicking and selecting "Send to Intruder" or by using the Ctrl + I shortcut. 
No Answer.

### Load the payloads.
No Answer.

### We have done all we need to do for this very simple attack, so go ahead and click the "Start Attack" button. A warning about the rate-limiting in Burp Community will appear. Click "Ok" and start the attack !
Note: This will take a few minutes to complete in Burp Community -- hence the relatively small lists in use

No Answer.

### Once we have sorted our results, one request should stand out as being different !
You should find the username m.rivera with the password : letmein1

No Answer.

### Well done, you have successfully bruteforced the support login page with a credential stuffing attack !
No Answer.

## TASK 11 : Challenge
### Which attack type is best suited for this task ?
Answer : Sniper

### Configure an appropriate position and payload (the tickets are stored at values between 1 and 100), then start the attack. You should find that at least five tickets will be returned with a status code of 200, indicating that they exist.
Set up the sniper payload like this :

![Payload Sets](/images/thm/burpIntruder/Burp Suite_ Intruder_2.png)
_Payload Sets_

No Answer.

### Either using the Response tab in the Attack Results window or by looking at each successful (i.e. 200 code) request manually in your browser, find the ticket that contains the flag. What is the flag ?
When sorted by Status code, you'll find 5 tickets available (request 0 with no paylaod return a 404 not found) :

![Attack](/images/thm/burpIntruder/Burp Suite_ Intruder_3.png)
_Attack_

Visit all tickets pages and you'll find the flag !

Answer : THM{MTMxNTg5NTUzMWM0OWRlYzUzMDVjMzJl}

## TASK 12 : Extra Mile
### Navigate to  http://10.10.90.45/admin/login/. Activate the Burp Proxy and attempt to log in. Capture the request and send it to Intruder.
No Answer.

### Configure the positions the same way as we did for bruteforcing the support login:
 1- Set the attack type to be "Pitchfork".
 2- Clear all of the predefined positions and select only the username and password form fields. The other two positions will be handled by our macro.

No Answer.

### Now switch over to the Payloads sub-tab and load in the same username and password wordlists we used for the support login attack. Up until this point, we have configured Intruder in almost the same way as our previous credential stuffing attack; this is where things start to get more complicated.
No Answer.

### With the username and password parameters handled, we now need to find a way to grab the ever-changing loginToken and session cookie. Unfortunately, Recursive Grep won't work here due to the redirect response, so we can't do this entirely within Intruder -- we will need to build a macro.
No Answer.

### Now that we have a macro defined, we need to set Session Handling rules that define how the macro should be used.
No Answer.

### Now we need to switch back over to the Details tab and look at the "Rule Actions" section. 
No Answer.

### Click "Ok", and we're done !
No Answer.

### Phew, that was a long process ! You should now have a macro defined that will substitute in the CSRF token and session cookie. All that's left to do is switch back to Intruder and start the attack !
Note: You should be getting 302 status code responses for every request in this attack. If you see 403 errors, then your macro is not working properly. 

No Answer.

### As with the support login credential stuffing attack we carried out, the response codes here are all the same (302 Redirects). Once again, order your responses by Length to find the valid credentials. Your results won't be quite as clear-cut as last time -- you will see quite a few different response lengths: however, the response that indicates a successful login should still stand out as being quite significantly shorter.
When the attack is finished, you'll have :

![Attack](/images/thm/burpIntruder/Burp Suite_ Intruder_4.png)
_Attack_

The admin user is o.bennett and password bella1 !

No Answer.

### Use the credentials you just found to log in (you may need to refresh the login page before entering the credentials).
Log in with this credentials ! done !

![Graph](/images/thm/burpIntruder/Burp Suite_ Intruder_5.png)
_Graph_

No Answer.

## TASK 13 : Conclusion

### I can use Intruder !
No Answer.

### [Bonus Question -- Optional] Use Intruder to automate the column enumeration of the Union SQLi in the Repeater Extra Mile exercise.
No Answer.

