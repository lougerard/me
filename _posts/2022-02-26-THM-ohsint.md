---
title: OhSINT  
author: CYB3RM3
name: CYB3RM3 | OhSINT 
date: 2022-02-26 23:22:16 +0100
categories: [TryHackMe, RedTeam]
tags: [RedTeam, OSINT, Recon]
---

Are you able to use open source intelligence to solve this challenge?

THM Room [https://tryhackme.com/room/ohsint](https://tryhackme.com/room/ohsint)

## TASK 1 : ohsint
### What is this users avatar of?

Used Exiftool on the image :

```console
user$ ./exiftool WindowsXP.jpg
ExifTool Version Number         : 12.40
File Name                       : WindowsXP.jpg
Directory                       : .
File Size                       : 229 KiB
File Modification Date/Time     : 2022:02:20 12:55:41+01:00
File Access Date/Time           : 2022:02:26 22:26:39+01:00
File Inode Change Date/Time     : 2022:02:26 22:20:19+01:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
XMP Toolkit                     : Image::ExifTool 11.27
GPS Latitude                    : 54 deg 17' 41.27" N
GPS Longitude                   : 2 deg 15' 1.33" W
Copyright                       : OWoodflint
Image Width                     : 1920
Image Height                    : 1080
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1920x1080
Megapixels                      : 2.1
GPS Latitude Ref                : North
GPS Longitude Ref               : West
GPS Position                    : 54 deg 17' 41.27" N, 2 deg 15' 1.33" W
```
{: .nolineno }

From here, i found interesting informations like Copyright : OWoodflint.

Googling the copyright name found, i got a Twitter account :

![Twitter Account](/images/thm/ohsint/ohsint_1.png)
_Twitter Account_

From there, i can see what profile picture is use as avatar :

![Profile picture](/images/thm/ohsint/ohsint_2.png)
_Profile picture_

Answer : cat

### What city is this person in?
Googling the copyright name found : OWoodflint, i also found and github account :

![Github Account](/images/thm/ohsint/ohsint_3.png)
_Gihtub Account_

The author present himself briefly and says where's from :

![Author Location](/images/thm/ohsint/ohsint_4.png)
_Author Location_

Answer : London

### Whats the SSID of the WAP he connected to?
From a tweet, i got a BSSID :

Before going futher, i looked at the difference between BSSID and SSID <https://www.juniper.net/documentation/en_US/junos-space-apps/network-director3.7/topics/concept/wireless-ssid-bssid-essid.html>:

![SSID vs BSSID](/images/thm/ohsint/ohsint_5.png)
_SSID vs BSSID_

Then i searched a tool to convert BSSID to SSID identifier and found WIGLE <https://wigle.net/>. On this website, i could do the following search with the BSSID :

![SSID](/images/thm/ohsint/ohsint_6.png)
_SSID_

It gives me the SSID.

Answer : UnileverWiFi

### What is his personal email address?
Looking around this account, i found an email address :

![Email address](/images/thm/ohsint/ohsint_7.png)
_Email address_

Answer : OWoodflint@gmail.com

### What site did you find his email address on?
Answer : Github

### Where has he gone on holiday?
Found a wordpress website too :

![Wordpress](/images/thm/ohsint/ohsint_8.png)
_Wordpress_

We can learn on this that the author was on on holidays at New Yark :

![Holidays](/images/thm/ohsint/ohsint_9.png)
_Holidays_

Answer : New York

### What is this persons password?
Inspecting the html from the wordpress blog, i can see a particular style <p> as it was colored as #FFFFFF so white. Looks like hidden data :

```html
<p style="color:#ffffff;" class="has-text-color">pennYDr0pper.!</p>
```
{: .nolineno }

Highlight all the blog text and it reveals this informations :

![Password](/images/thm/ohsint/ohsint_10.png)
_Password_

Answer : pennYDr0pper.!