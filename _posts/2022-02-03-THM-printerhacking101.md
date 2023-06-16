---
title: Printer Hacking 101
author: CYB3RM3
name: CYB3RM3 | Printer Hacking 101
date: 2022-02-03 20:46:44 +0100
categories: [TryHackMe, Printer]
tags: [Printer]
---

Learn about (and get hands on with) printer hacking and understand the basics of IPP.

THM Room [https://tryhackme.com/room/printerhacking101](https://tryhackme.com/room/printerhacking101)


## TASK 1 : Introduction
### Read the above
No Answer.

## TASK 2 : IPP Port
### What port does IPP run on?
IPP (Internet Printing Protocol) use the port TCP 631 by default.

Answer : 631

## TASK 3 : Targeting & Exploitation
###  How would a simple printer TCP DoS attack look as a one-line command?

Check the cheatsheet <http://hacking-printers.net/wiki/index.php/Printer_Security_Testing_Cheat_Sheet> linked in the task for TCP DoS :

![TCP DoS attack](/images/thm/printerhacking101/printerhacking101_1.png)
_TCP DoS attack_

Answer : while true; do nc printer 9100; done

### Review the cheat sheet provided in the task reading above. What attack are printers often vulnerable to which involves sending more and more information until a pre-allocated buffer size is surpassed?

![Buffer overflows](/images/thm/printerhacking101/printerhacking101_2.png)
_Buffer overflows_

Answer : Buffer overflows

### Connect to the printer per the instructions above. Where's the Fox_Printer located?

I used the first method (connect on the URL IP:PORT) then navigated to printers tab :

![Connexion](/images/thm/printerhacking101/printerhacking101_3.png)
_Connexion_

Found there the Fox_Printer then clicking on its name, i found the location of the printer :

![Printer Location](/images/thm/printerhacking101/printerhacking101_4.png)
_Printer Location_

Answer : Skidy's basement

### What is the size of a test sheet?

Printed a test page to get the size of the test print :

![Test sheet size](/images/thm/printerhacking101/printerhacking101_5.png)
_Test sheet size_

Answer : 1k

## TASK 4 : Conclusion 
### Check that your printer isn't vulnerable, why not nmap scan it to see? 
No Answer.

### Go learn more about printers through further research and experimentation. Congrats on completing this room!
No Answer.