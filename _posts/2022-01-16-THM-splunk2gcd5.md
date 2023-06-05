---
title: Splunk 2
author: CYB3RM3
name: CYB3RM3 | Splunk 2
date: 2022-01-16 15:16:02 +0100
categories: [TryHackMe, Investigation]
tags: [Windows, SIEM, Logs, Splunk]
---

Part of the Blue Primer series. This room is based on version 2 of the Boss of the SOC (BOTS) competition by Splunk.

THM Room [https://tryhackme.com/room/splunk2gcd5](https://tryhackme.com/room/splunk2gcd5)


## TASK 1 : Deploy!
### Deployed the virtual machine and connected to the website found at 10.10.246.201:8000 
No Answer

## TASK 2 : Dive into the data
### I'm ready to get hunting with Splunk. 
No Answer

## TASK 3 : 100 series questions
### Amber Turing was hoping for Frothly to be acquired by a potential competitor which fell through, but visited their website to find contact information for their executive team. What is the website domain that she visited? 
Firstly i searched traffic from Amber :

```sql
index="botsv2" sourcetype="pan:traffic" amber
```
{: .nolineno }

Then i get her IP adress 10.0.2.101 so i could try to filter for sites :

```sql
index="botsv2" 10.0.2.101 sourcetype="stream:HTTP" | table site
```
{: .nolineno }

But this query returned many values, so we need to exclude duplicates and non relevant entries :

```sql
index="botsv2" 10.0.2.101 sourcetype="stream:HTTP" NOT(site=*.microsoft.com OR site=*.windowsupdate.com OR site=*.bing.com OR site=*.digicert.com OR site=*.akamaized.net OR site=*msn.com OR site=*.adnxs.com OR *office.net OR *symcd.com OR site=*gvt1*)
| dedup site 
| table site
```
{: .nolineno }

From the list, Berkbeer website seems to be the right answer !

Answer : www.berkbeer.com



### Amber found the executive contact information and sent him an email. What image file displayed the executive's contact information? Answer example: /path/image.ext
An interesting field is URI_PATH  for this request. And the executive may be resume by searching *ceo* somewhere :

```sql
index="botsv2" 10.0.2.101 sourcetype="stream:HTTP" www.berkbeer.com *ceo*
```
{: .nolineno }

Looking the uri_path give us the answer.

Answer : /images/ceoberk.png

### What is the CEO's name? Provide the first and last name.
I firstly search the CEO email adress before his name.

Just looking the content of the result from next question and filtering with :

```sql
index="botsv2" sourcetype="stream:smtp" aturing@froth.ly berk*
```
{: .nolineno }

Answer : Martin Berk

### What is the CEO's email address?
I began to search for Amber informations like her email. This following query give me that email : aturing@froth.ly

```sql
index="botsv2" sourcetype="stream:smtp" amber
```
{: .nolineno }

Then adding some extra information like the domain Amber is looking for :

```sql
index="botsv2" sourcetype="stream:smtp" aturing@froth.ly berkbeer*
```
{: .nolineno }

This returned me 2 emails : mberk@berkbeer.com and hbernhard@berkbeer.com

When reading the content of the result, mberk seems to be the CEO.

Answer : mberk@berkbeer.com

### After the initial contact with the CEO, Amber contacted another employee at this competitor. What is that employee's email address?

Answer : hbernhard@berkbeer.com

### What is the name of the file attachment that Amber sent to a contact at the competitor?
Looking for the attachment_filename field the query returning the conversation between Amber and Bernhard :

```sql
index="botsv2" sourcetype="stream:smtp" aturing@froth.ly hbernhard@berkbeer.com
```
{: .nolineno }

Answer : Saccharomyces_cerevisiae_patent.docx

### What is Amber's personal email address?
This one was quite trials and error by decoding the base64 content from the previous results between Benhard and Amber.

Answer : ambersthebest@yeastiebeast.com

## TASK 4 : 200 series questions
### What version of TOR Browser did Amber install to obfuscate her web browsing? Answer guidance: Numeric with one or more delimiter.
Search for tor.exe and Amber kewords :

```sql
index="botsv2" amber tor.exe
```
{: .nolineno }

Then i looked through the interesting fields and found in the process field the answer : 

![TOR Browser](/images/thm/splunk2gcd5/splunk2gcd5_1.png)
_TOR Browser_

Answer : 7.0.4

### What is the public IPv4 address of the server running www.brewertalk.com?
I searched for the website in the destination ip field :

```sql
index="botsv2" www.brewertalk.com
```
{: .nolineno }

![Brewertalk IP](/images/thm/splunk2gcd5/splunk2gcd5_2.png)
_Brewertalk IP_

The answer must be a public IP address so it could not be 172.31.X.X

Answer : 52.42.208.228

### Provide the IP address of the system used to run a web vulnerability scan against www.brewertalk.com.
In the same query, i found the IP for the system used to run a scan in the source IP :

![Source IP](/images/thm/splunk2gcd5/splunk2gcd5_3.png)
_Source IP_

Answer : 45.77.65.211

### The IP address from Q#2 is also being used by a likely different piece of software to attack a URI path. What is the URI path? Answer guidance: Include the leading forward slash in your answer. Do not include the query string or other parts of the URI. Answer example: /phpinfo.php

Adding the IP from Q2 in the last query :

```sql
index="botsv2" www.brewertalk.com 52.42.208.228
```
{: .nolineno }

Then looking the uri_path for sensitive informations and i found a PHP page : /member.php

![URI Path](/images/thm/splunk2gcd5/splunk2gcd5_4.png)
_URI Path_

Answer : /member.php

### What SQL function is being abused on the URI path from the previous question?
The attack is from the source IP address, so let's change the query and set up the uri_path found the searching about form_data  :

```sql
index="botsv2" brewertalk.com src_ip="45.77.65.211" uri_path="/member.php" 
| dedup form_data 
| table form_data
```
{: .nolineno }

![updatexml](/images/thm/splunk2gcd5/splunk2gcd5_5.png)
_updatexml_

Answer : updatexml

### What was the value of the cookie that Kevin's browser transmitted to the malicious URL as part of an XSS attack? Answer guidance: All digits. Not the cookie name or symbols like an equal sign.
Let search for Kevin with a sourcetype in http stream. Then adding the hint (tag="error") and looking to cookie field :

```sql
index="botsv2" kevin sourcetype="stream:http" tag="error"
| table cookie
```
{: .nolineno }

![Cookie](/images/thm/splunk2gcd5/splunk2gcd5_6.png)
_Cookie_

Answer : 1502408189

### What brewertalk.com username was maliciously created by a spear phishing attack?
Checking the hint give us the stolen CSRF token (1bc3eab741900ab25c98eee86bf20feb). let's search about this and looking for unique result. Form_data seems good. I table this request then :

```sql
index="botsv2" 1bc3eab741900ab25c98eee86bf20feb 
| table form_data
```
{: .nolineno }

![Malicious Username](/images/thm/splunk2gcd5/splunk2gcd5_7.png)
_Malicious Username_

This give me the username.

Answer : kIagerfield

## TASK 5 : 300 series questions
### Mallory's critical PowerPoint presentation on her MacBook gets encrypted by ransomware on August 18. What is the name of this file after it was encrypted? 
Let's begin with the keyword search as usual :

```sql
index="botsv2" mallory
```
{: .nolineno }

This gives me the hostname of Mallory's Mac Air : MACLORY-AIR13

Then adding this information to the query and searching for powerpoint :

```sql
index="botsv2" mallory host="MACLORY-AIR13" (*.ppt OR *.pptx)
```
{: .nolineno }

![Filename](/images/thm/splunk2gcd5/splunk2gcd5_8.png)
_Filename_

Answer : Frothly_marketing_campaign_Q317.pptx.crypt

### There is a Games of Thrones movie file that was encrypted as well. What season and episode is it? 
I use the following query to find the answer :

```sql
index="botsv2" got (*.crypt)
```
{: .nolineno }

![GoT](/images/thm/splunk2gcd5/splunk2gcd5_9.png)
_GoT_

Answer : S07E02

### Kevin Lagerfield used a USB drive to move malware onto kutekitten, Mallory's personal MacBook. She ran the malware, which obfuscates itself during execution. Provide the vendor name of the USB drive Kevin likely used. Answer Guidance: Use time correlation to identify the USB drive.
Searching for keyword given like kutekitte and usb then checked the usefull field and found in name the "pack_hardware_usb_devices" which seems good.

```sql
index="botsv2" kutekitten usb name="pack_hardware-monitoring_usb_devices"
```
{: .nolineno }

This request shows up the following informations : 

![USB Device](/images/thm/splunk2gcd5/splunk2gcd5_10.png)
_USB Device_

Let's google this vendor ID for USB drives :

![USB Vendor](/images/thm/splunk2gcd5/splunk2gcd5_11.png)
_USB Vendor_

Answer : Alcor Micro Corp.

### What programming language is at least part of the malware from the question above written in?
First, i search :

```sql
index="botsv2" kutekitten "\\/Users*"
```
{: .nolineno }

Then in the field, i  check extra users and Splunk gives me "decorations.username"=mkraeusen. So let's add this to the query :

```sql
index="botsv2" kutekitten "\\/Users*" "decorations.username"=mkraeusen
```
{: .nolineno }

I note and interesting field : columns.md5 so i click on it :

```sql
index="botsv2" kutekitten "\\/Users*" "decorations.username"=mkraeusen "columns.md5"=72d4d364ed91dd9418d144a2db837a6d
```
{: .nolineno }

Now copy paste this md5 hash to Virustotal :

![Virustotal](/images/thm/splunk2gcd5/splunk2gcd5_12.png)
_Virustotal_

Answer : Perl

### When was this malware first seen in the wild? Answer Guidance: YYYY-MM-DD

![Virustotal First seen](/images/thm/splunk2gcd5/splunk2gcd5_13.png)
_Virustotal First seen_

Also from Virustotal.

Answer : 2017-01-17

### The malware infecting kutekitten uses dynamic DNS destinations to communicate with two C&C servers shortly after installation. What is the fully-qualified domain name (FQDN) of the first (alphabetically) of these destinations?
From destination tab on Virustotal for this hash :

![Domain](/images/thm/splunk2gcd5/splunk2gcd5_14.png)
_Domain_

Answer : eidk.duckdns.org

### From the question above, what is the fully-qualified domain name (FQDN) of the second (alphabetically) contacted C&C server?
Answer : eidk.hopto.org

## TASK 6 : 400 series questions

### A Federal law enforcement agency reports that Taedonggang often spear phishes its victims with zip files that have to be opened with a password. What is the name of the attachment sent to Frothly by a malicious Taedonggang actor?
Relevant keyword : frothly, *.zip then filter on sourcetype "wineventlog"

```sql
index="botsv2" frothly *.zip sourcetype=wineventlog
```
{: .nolineno }

![Attachment](/images/thm/splunk2gcd5/splunk2gcd5_15.png)
_Attachment_

Answer : invoice.zip

### What is the password to open the zip file?
Searching into the body of the mail by adding the password keyword :

```sql
index="botsv2" invoice.zip password 
| spath "content_body{}" | table "content_body{}"
```
{: .nolineno }

![Password](/images/thm/splunk2gcd5/splunk2gcd5_16.png)
_Password_

Answer : 912345678

### The Taedonggang APT group encrypts most of their traffic with SSL. What is the "SSL Issuer" that they use for the majority of their traffic? Answer guidance: Copy the field exactly, including spaces.

Querying ssl from splunk :

```sql
index="botsv2" ssl
```
{: .nolineno }

Then checking then interesting fields : ssl_issuer :

![ssl_issuer](/images/thm/splunk2gcd5/splunk2gcd5_17.png)
_ssl_issuer_

Answer : C = US

### What unusual file (for an American company) does winsys32.dll cause to be downloaded into the Frothly environment?
First query gives me a protocol use for file transfert : FTP

```sql
index="botsv2" winsys32.dll 
```
{: .nolineno }
A second query gives me the method : RETR

```sql
index="botsv2" sourcetype="stream:ftp" | stats count by method
```
{: .nolineno }
The last query show the answer :

```sql
index="botsv2" sourcetype="stream:ftp" method="RETR"
```
{: .nolineno }

![stream:ftp](/images/thm/splunk2gcd5/splunk2gcd5_18.png)
_stream:ftp_

Anser :

```console
나는_데이비드를_사랑한다.hwp
```
{: .nolineno }

### What is the first and last name of the poor innocent sap who was implicated in the metadata of the file that executed PowerShell Empire on the first victim's workstation? Answer example: John Smith
Using the links given : 

![Victim](/images/thm/splunk2gcd5/splunk2gcd5_19.png)
_Victim_

Answer : Ryan Kovar

### Within the document, what kind of points is mentioned if you found the text?
idem.

![invoice.doc](/images/thm/splunk2gcd5/splunk2gcd5_20.png)
_invoice.doc_

Answer : CyberEastEgg

### To maintain persistence in the Frothly network, Taedonggang APT configured several Scheduled Tasks to beacon back to their C2 server. What single webpage is most contacted by these Scheduled Tasks? Answer example: index.php or images.html
Using the query :

```sql
index="botsv2" \\Software\\Microsoft\\Network sourcetype=WinRegistry
```
{: .nolineno }

Checking the most use data and decode from base64 :

![process.php](/images/thm/splunk2gcd5/splunk2gcd5_21.png)
_process.php_

Answer : process.php

## TASK 7 : Conclusion 
### You leveled up your Splunk-fu thanks to the BOTSv2 dataset. 
No Answer.