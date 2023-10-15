---
title: Identity and Access Management
author: CYB3RM3
name: CYB3RM3 | Identity and Access Management
date: 2023-09-17 10:53:20 +0100
categories: [TryHackMe, Security Engineer]
tags: [IAAM, Intro, Access Management, Identity]
---

Learn about identification, authentication, authorisation, accounting, and identity management.

THM Room : [https://tryhackme.com/room/iaaaidm](https://tryhackme.com/room/iaaaidm)


## TASK 1 Introduction
###  What is the name of the room recommended to finish before this one? 
Answer : Security Principles

## TASK 2 IAAA Model
### You are granted access to read and send an email. What is the name of this process?
Answer : Authorisation

### Which process would require you to enter your username?
Answer : Identification

### Although you have write access, you should only make changes if necessary for the task. Which process is required to enforce this policy?
Answer : Accountability

## TASK 3 Identification
### Which of the following cannot be used for identification?

    1. Email address
    2. Mobile number with international code
    3. Year of birth
    4. Passport number

Answer : 3


### Which of the following cannot be used for identification?

    1. Landline phone number
    2. Street number
    3. Health insurance card number
    4. Student ID number

Answer : 2

## TASK 4 Authentication

Answer the following questions using the correct item number from the numbered list below.

    1. Something you know
    2. Something you have
    3. Something you are
    4. 2FA 

### When you want to check your email, you enter your username and password. What kind of authentication is your email provider using?

Answer : 1

### Your bank lets you finish most of your banking operations using its app. You can log in to your banking app by providing a username and a password and then entering the code received via SMS. What kind of authentication is the banking app using?

Answer : 4

### Your new landline phone system at home allows callers to leave you a message when the call is not picked up. You can call your home number and enter a secret number to listen to recorded messages. What kind of authentication is being used here?

Answer : 1

### You have just started working at an advanced research centre. You learned that you need to swipe your card and enter a four-digit PIN whenever you want to use the elevator. Under which group does this authentication fall?

Answer : 4

## TASK 5 Authorisation and Access Control
In the following questions, answer with 1 or 2 to indicate:

    1. Authorisation
    2. Access Control

### The new policy states that the secretary should be able to send an email on the manager’s behalf. What is this policy dictating?

Answer : 1

### You shared a document with your colleague and gave them view permissions so they could read without making changes. What would ensure that your file won’t be modified?

Answer : 2

### The hotel management decided that the cleaning staff needed access to all the hotel rooms to do their work. What phase is this decision part of?

Answer : 1

## TASK 6 Accountability and Logging
###  Ensure you have read the above before moving on. 
No Answer.

## TASK 7 Identity Management
### What does IdM stand for?
Answer : Identity Management

### What does IAM stand for?
Answer : Identity and Access Management

## TASK 8 Attacks Against Authentication
### The attacker could authenticate using the user’s response when the authentication protocol required a password encrypted with a shared key. What is the name of the attack? 

Answer : replay attack

## TASK 9 Access Control Models
Answer the following questions using the correct item number from the numbered list below.

    1. DAC
    2. RBAC
    3. MAC

### You are sharing a document via a network share and giving edit permission only to the accounting department. What example of access control is this?
Answer : 2

### You published a post on a social media platform and made it only visible to three out of your two hundred friends. What kind of access control did you use?
Answer : 1

## TASK 10 Single Sign-On

"SSO allows organisations to authenticate users once before granting them access to the resources required for their work. We can achieve many advantages from this. We will mention a few.

    One strong password: Expecting a user to remember a single strong password is more acceptable than asking them to remember ten different strong passwords.
    Easier MFA: Adding MFA to every different service is a humongous task to accomplish and maintain. With SSO, MFA needs to be enabled and configured once.
    Simpler Support: Support requests like password reset become more straightforward as they are now confined to a single account.
    Efficiency: A user does not need to log in every time they need to access a new service."

### What does SSO stand for?
Answer : Single Sign-On

### Does SSO simplify MFA use as it needs to be set up once? (Yea/Nay)
Answer : YEA

### Is it true that SSO can be cumbersome as it requires the user to remember and input different passwords for the various services? (Yea/Nay)
Answer : NAY

### Does SSO allow users to access various services after signing in once? (Yea/Nay)
Answer : YEA

### Does the user need to create and remember a single password when using SSO? (Yea/Nay)
Answer : YEA

## TASK 11 Scenarios

![Flag](/images/thm/iaaaidm/image_1.png)
_Flag_

Answer : {THM_ACCESS_CONTROL}

## TASK 12 Conclusion
###  Ensure that you have taken notes of the concepts and terms presented in this room. 
No Answer.

