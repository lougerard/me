---
title: Burp Suite - Other Modules
author: CYB3RM3
name: CYB3RM3 | Burp Suite - Other Modules
date: 2021-09-19 14:51:36 +0100
categories: [TryHackMe, Web]
tags: [Web, BurpSuite]
---

THM Room [https://tryhackme.com/room/burpsuiteom](https://tryhackme.com/room/burpsuiteom)

## TASK 1 : Introduction - Outline
### Deploy the machine attached to this task !
No Answer.

## TASK 2 : Decoder - Overview
### Familiarise yourself with the Decoder interface.
No Answer.

## TASK 3 : Decoder - Encoding/Decoding
### Base64 encode the phrase: Let's Start Simple. What is the base64 encoded version of this text ?
Using the decoder : TGV0J3MgU3RhcnQgU2ltcGxl

We can also confirm in the terminal :

```console
┌──(kaliuser㉿kali)- [~]
└─$ echo "Let's Start Simple" | base64
TGV0J3MgU3RhcnQgU2ltcGxlCg==
```
Answer : TGV0J3MgU3RhcnQgU2ltcGxl

### URL Decode this data: %4e%65%78%74%3a%20%44%65%63%6f%64%69%6e%67. What is the plaintext returned ?
Answer : Next: Decoding

### Use Smart Decode to decode this data: &#x25;&#x33;&#x34;&#x25;&#x33;&#x37; . What is the decoded text ?
Answer : 47

### Encode this phrase: Encoding Challenge. Start with base64 encoding. Take the output of this and convert it into ASCII Hex. Finally, encode the hex string into octal. What is the final string ?

```text
Encoding Challenge > RW5jb2RpbmcgQ2hhbGxlbmdl > 5257356a62325270626d6367513268686247786c626d646c > 24034214a720270024142d541357471232250253552c1162d1206c
```
{: .nolineno }
Answer : 24034214a720270024142d541357471232250253552c1162d1206c

## TASK 4 : Decoder - Hashing
### Using Decoder, what is the SHA-256 hashsum of the phrase: Let's get Hashing! ? Convert this into an ASCII Hex string for the answer to this question.

![Hashing](/images/thm/burpModules/Burp Suite_ modules_4.png)
_Hashing_

Answer : 6b72350e719a8ef5af560830164b13596cb582757437e21d1879502072238abe

### Generate an MD4 hashsum of the phrase: Insecure Algorithms. Encode this as base64 (not ASCII Hex) before submitting.

![hashsum](/images/thm/burpModules/Burp Suite_ modules_6.png)
_hashsum_

Answer : TcV4QGZZN7y7lwYFRMMoeA==

### Now read the problem specification below:
"Some joker has messed with my SSH key! There are four keys in the directory, and I have no idea which is the real one. The MD5 hashsum for my key is 3166226048d6ad776370dc105d40d9f8 -- could you find it for me?"
Submit the correct key name as your answer.

![keys](/images/thm/burpModules/Burp Suite_ modules_5.png)
_keys_

Answer : key3

## TASK 5 : Comparer - Overview
### Familiarise yourself with the Comparer interface.
No Answer.

## TASK 6 : Comparer - Example
### Navigate to http://10.10.189.188/support/login. Try to login with an invalid username and password -- capture the request in the Burp Proxy.
No Answer

### Send the request to Repeater with Ctrl + R (or Mac equivalent), or by right-clicking on the request in Proxy and choosing to "Send to Repeater".
No Answer.

### Send the request, then right-click on the response and choose "Send to Comparer".
No Answer.

### In the Repeater tab, change the credentials to (see below) and send the request again, then pass the new response into Comparer.

```text
Username: support_admin
Password: w58ySK4W
```
{: .nolineno }

No Answer

### Compare the two responses  by word. How many differences does Comparer detect in total ?

![Comparer](/images/thm/burpModules/Burp Suite_ modules_1.png)
_Comparer_

Answer : 9

## TASK 7 : Sequencer - Overview
### Familiarise yourself with the Live capture and Manual load interfaces. We will be looking more in-depth at the Live capture interface in the next task.
No Answer.

## TASK 8 : Sequencer - Live Capture
### Follow the steps above to perform entropy analysis on the loginToken set by the /admin/login route of our target web app.

![Sequencer](/images/thm/burpModules/Burp Suite_ modules_2.png)
_Sequencer_

![Entropy](/images/thm/burpModules/Burp Suite_ modules_3.png)
_Entropy_

No Answer

### [Bonus Question -- Optional] Try performing the capture again, but this time monitor your requests in Wireshark. Can you see why live capturing the requests for this analysis can be described as "loud"?
No Answer.

## TASK 9 : Sequencer - Analysis
### Take some time to look through the tests that Burp used to generate its summary. You don't need to understand all of these, but it is important to know that they exist.
No Answer.

## TASK 10 : Room Conclusion
### I understand how to use Decoder, Sequencer, and Comparer!
No Answer.
