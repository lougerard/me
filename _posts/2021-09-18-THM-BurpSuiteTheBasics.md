---
title: Burp Suite - The Basics 
name: CYB3RM3 | Burp Suite - The Basics 
date: 2021-09-18 14:48:50
categories: [CTF]
tags: [TryHackMe, Web]
---

Burp Suite: The Basics 
THM Room [https://tryhackme.com/room/burpsuitebasics](https://tryhackme.com/room/burpsuitebasics)

# Table of contents
1. [TASK 1 : Outline](#Outline)
2. [TASK 2 : What is Burp Suite ?](#What)
3. [TASK 3 : Features of Burp Community](#Features)
4. [TASK 4 : Installation](#Installation)
5. [TASK 5 : The Dashnoard](#Dashnoard)
6. [TASK 6 : Navigation](#Navigation)
7. [TASK 7 : Options](#Options)
8. [TASK 8 : Introduction to the Burp Proxy](#BurpProxy)
9. [TASK 9 : Connecting through the Proxy (FoxyProxy)](#Connecting)
10. [TASK 10 : Proxying HTTPS](#Proxying)
11. [TASK 11 : The Burp Suite Browser](#Browser)
12. [TASK 12 : Scoping and Targeting](#Scoping)
13. [TASK 13 : Site Map and Issue Definitions](#SiteMap)
14. [TASK 14 : Example Attack](#Attack)
15. [TASK 15 : Room Conclusion](#Conclusion)


## **TASK 1 : Outline** <a name="Outline"></a>

* #### Deploy the machine attached to the TASK by pressing the green "Start Machine" button, as well as the AttackBox (using the "Start AttackBox" button at the top of the page) if you are not using your own machine
    
No Answer  

## **TASK 2 : What is Burp Suite ?** <a name="What"></a>

* #### Which edition of Burp Suite will we be using in this module ?
    
Answer : Burp Suite Community  

* #### Which edition of Burp Suite runs on a server and provides constant scanning for target web apps ?
Answer : Burp Suite Enterprise  

* #### Burp Suite is frequently used when attacking web applications and ______ applications.

Answer : Mobile  

## **TASK 3 : Features of Burp Community** <a name="Features"></a>

* #### Which Burp Suite feature allows us to intercept requests between ourselves and the target ?

Just read the text !  

Answer : Proxy  
  

* #### Which Burp tool would we use if we wanted to bruteforce a login form ?
    

Answer : Intruder  

## **TASK 4 : Installation** <a name="Installation"></a>

* #### If you have chosen not to use the AttackBox, make sure that you have a copy of Burp Suite installed before proceeding.
    

No Answer  

## **TASK 5 : The Dashnoard** <a name="Dashnoard"></a>

* #### Open Burp Suite and have a look around the dashboard. Make sure that you are comfortable with it before moving on.
    

No Answer

## **TASK 6 : Navigation** <a name="Navigation"></a>

* #### Get comfortable navigating around the top menu bars.
    

No Answer  

## **TASK 7 : Options** <a name="Options"></a>

* #### Change the Burp Suite theme to dark mode
    

No Answer  

* #### In which Project options sub-tab can you find reference to a "Cookie jar" ?
    

Answer : Sessions  

* #### In which User options sub-tab can you change the Burp Suite update behaviour ?
    

Answer : Misc  

* #### What is the name of the section within the User options "Misc" sub-tab which allows you to change the Burp Suite keybindings ?
    

Answer : Hotkeys

* #### If we have uploaded Client-Side TLS certificates in the User options tab, can we override these on a per-project basis (Aye/Nay) ?
    

Answer : AYE

* #### There are many more configuration options available. Take the time to read through them.  In the next section, we will cover the Burp Proxy -- a much more hands-on aspect of the room.
    

No Answer  

## **TASK 8 : Introduction to the Burp Proxy** <a name="BurpProxy"></a>

* #### Which button would we choose to send an intercepted request to the target in Burp Proxy ?

It's forwardingthe request to the destination.  

Answer : Forward  

* #### [Research] What is the default keybind for this ?  Note: Assume you are using Windows or Linux (i.e. swap Cmd for Ctrl). Take a look in the Hotkeys in Misc tab from the User Options !  

Answer : ctrl+f

## **TASK 9 : Connecting through the Proxy (FoxyProxy)** <a name="Connecting"></a>

* #### Read through the options in the right-click menu. There is one particularly useful option that allows you to intercept and modify the response to your request. What is this option ?

Intercept a request with burp then go to proxy intercept and take a look in the right-click menu !

![](/web/image/458-e589f08c/2021-09-18%2011_36_03-TryHackMe%20_%20Burp%20Suite_%20The%20Basics.png)  

Answer : Response to this request  

* #### [Bonus Question -- Optional] Try installing FoxyProxy standard and have a look at the pattern matching features.
    

No Answer  

## **TASK 10 : Proxying HTTPS** <a name="Proxying"></a>

* #### If you are not using the AttackBox, configure Firefox (or your browser of choice) to accept the Portswigger CA certificate for TLS communication through the Burp Proxy.
    

No Answer  

## **TASK 11 : The Burp Suite Browser** <a name="Browser"></a>

* #### Using the in-built browser, make a request to http://10.10.7.65/ and capture it in the proxy.
    

No Answer

## **TASK 12 : Scoping and Targeting** <a name="Scoping"></a>

* #### Add http://10.10.7.65/ to your scope and change the Proxy settings to only intercept traffic to in-scope targets. See the difference between the amount of traffic getting caught by the proxy before and after limiting the scope.
    
No Answer

## **TASK 13 : Site Map and Issue Definitions** <a name="SiteMap"></a>

* #### Take a look around the site on http://10.10.7.65/ -- we will be using this a lot throughout the module. Visit every page linked to from the homepage, then check your sitemap -- one endpoint should stand out as being very unusual !  Visit this in your browser (or use the "Response" section of the site map entry for that endpoint)  What is the flag you receive?
    
After visiting the website, i see a special request GET /5yjR2GLcoGoij2ZK HTTP/1.1 which give us the flag in the response : THM{NmNlZTliNGE1MWU1ZTQzMzgzNmFiNWVk}  

Answer : THM{NmNlZTliNGE1MWU1ZTQzMzgzNmFiNWVk}  

* #### Look through the Issue Definitions list. What is the typical severity of a Vulnerable JavaScript dependency?
    
Just search about "Vulnerable JavaScript dependency" in the Issue Definitions list.  

Answer : Low  

## **TASK 14 : Example Attack** <a name="Attack"></a>

* #### Try typing: &lt;script* #### alert("Succ3ssful XSS")&lt;/script* #### , into the "Contact Email" field. You should find that there is a client-side filter in place which prevents you from adding any special characters that aren't allowed in email addresses :
    

No Answer  

* #### Fortunately for us, client-side filters are absurdly easy to bypass. There are a variety of ways we could disable the script or just prevent it from loading in the first place.  Let's focus on simply bypassing the filter for now.  First, make sure that your Burp Proxy is active and that the intercept is on.
    
No Answer  

* #### Now, enter some legitimate data into the support form. For example: "pentester@example.thm" as an email address, and "Test Attack" as a query. Submit the form -- the request should be intercepted by the proxy.
    
No Answer  

* #### With the request captured in the proxy, we can now change the email field to be our very simple payload from above: &lt;script* #### alert("Succ3ssful XSS")&lt;/script* #### . After pasting in the payload, we need to select it, then URL encode it with the Ctrl + U shortcut to make it safe to send. This process is shown in the GIF below :
    
No Answer  

* #### Finally, press the "Forward" button to send the request.  You should find that you get an alert box from the site indicating a successful XSS attack !
    
No Answer

* #### Congratulations, you bypassed the filter ! Don't expect it to be quite so easy in real life, but this should hopefully give you an idea of the kind of situation in which Burp Proxy can be useful. 
    

No Answer  

## **TASK 15 : Room Conclusion** <a name="Conclusion"></a>

* #### I understand the fundamentals of using Burp Suite!
    
No Answer