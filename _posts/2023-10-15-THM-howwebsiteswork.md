---
title: How websites work
author: CYB3RM3
name: CYB3RM3 | How websites work
date: 2023-10-15 16:15:15 +0100
categories: [TryHackMe, How The Web Works]
tags: [Website, Intro, Pre Security]
---

To exploit a website, you first need to know how they are created.

THM Room : [https://tryhackme.com/room/howwebsiteswork](https://tryhackme.com/room/howwebsiteswork)



## TASK 1 How websites work
### What term best describes the component of a web application rendered by your browser?
Answer : Front End

## TASK 2 HTML
### Let's play with some HTML! On the right-hand side, you should see a box that renders HTML - If you enter some HTML into the box and click the green "Render HTML Code" button, it will render your HTML on the page; you should see an image of some cats.
No Answer.

### One of the images on the cat website is broken - fix it, and the image will reveal the hidden text answer!
Answer : 

```console
HTMLHERO
```
{: .nolineno }

### Add a dog image to the page by adding another img tag (< img >) on line 11. The dog image location is img/dog-1.png. What is the text in the dog image?
Answer : 

```console
DOGHTML
```
{: .nolineno }

## TASK 3 JavaScript
### Click the "View Site" button on this task. On the right-hand side, add JavaScript that changes the demo element's content to "Hack the Planet"
Answer : 
```console
JSISFUN
```
{: .nolineno }

### Add the button HTML from this task that changes the element's text to "Button Clicked" on the editor on the right, update the code by clicking the "Render HTML+JS Code" button and then click the button.
No Answer.

## TASK 4 Sensitive Data Exposure
### View the website on this task. What is the password hidden in the source code? 
Answer : testpasswd

## TASK 5 HTML Injection
### View the website on this task and inject HTML so that a malicious [link to hacker.com](http://hacker.com) is shown. 
Answer : HTML_INJ3CTI0N