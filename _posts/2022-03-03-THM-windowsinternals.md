---
title: Windows Internals
author: CYB3RM3
name: CYB3RM3 | Windows Internals  
date: 2022-03-03 13:55:15 +0100
categories: [TryHackMe, Host Evasions]
tags: [Sysinternals, Windows]
---

Learn and understand the fundamentals of how Windows operates at its core.

THM Room [https://tryhackme.com/room/windowsinternals](https://tryhackme.com/room/windowsinternals)


## TASK 1 : Introduction
### Start the provided machine and move on to the next tasks.

No Answer

## TASK 2 : Processes
###  Open the provided file: "Logfile.PML" in Procmon and answer the questions below. 

No Answer.

### What is the process ID of "notepad.exe"?

Opening the logfile with procmon then switch in the process tree view :

![Procmon.exe](/images/thm/windowsinternals/windowsinternals_1.png)
_Procmon.exe_

![Process Tree](/images/thm/windowsinternals/windowsinternals_2.png)
_Process Tree_

Answer : 5984

### What is the parent process ID of the previous process?

Answer : 3412

### What is the integrity level of the process?

Opening one notepad.exe in the list :

![Integrity level](/images/thm/windowsinternals/windowsinternals_3.png)
_Integrity level_

Answer : high

## TASK 3 : Threads
###  Open the provided file: "Logfile.PML" in Procmon and answer the questions below. 

No Answer.

### What is the thread ID of the first thread created by notepad.exe?

![Thread ID](/images/thm/windowsinternals/windowsinternals_4.png)
_Thread ID_

Answer : 5908

### What is the stack argument of the previous thread?

Filtered with just "show thread activity" :

![Thread Activity filter](/images/thm/windowsinternals/windowsinternals_5.png)
_Thread Activity filter_

Then added the filter "contain thread" :

![Thread Activity filter 2](/images/thm/windowsinternals/windowsinternals_6.png)
_Thread Activity filter 2_

I opened the first event from notepad.exe as "thread" and it has thread ID from previous question : 5908 :

![Thread ID](/images/thm/windowsinternals/windowsinternals_7.png)
_Thread ID_

Answer : 6584

## TASK 4 : Virtual Memory
### Read the above and answer the questions below. 

No Answer.

### What is the total theoretical maximum virtual address space of a 32-bit x86 system?

Answer : 4 GB

### What default setting flag can be used to reallocate user process address space?

Answer : increaseUserVA

### Open the provided file: "Logfile.PML" in Procmon and answer the questions below.

No Answer.

### What is the base address of "notepad.exe"?

Hint : Listed as the operation Load Image.

First i searched the event for notepad.exe "load image" :

![Operation](/images/thm/windowsinternals/windowsinternals_8.png)
_Operation_

Then looking the process tab for the address :

![Process Address](/images/thm/windowsinternals/windowsinternals_9.png)
_Process Address_

Answer : 0x7ff652ec0000

## TASK 5 : Dynamic Link Libraries
### Open the provided file: "Logfile.PML" in Procmon and answer the questions below. 

No Answer.

### What is the base address of "ntdll.dll" loaded from "notepad.exe"?

On the same process tab as for notepad.exe address :

![ntdll.dll](/images/thm/windowsinternals/windowsinternals_10.png)
_ntdll.dll_

Answer : 0x7ffd0be200000

### What is the size of "ntdll.dll" loaded from "notepad.exe"?

Answer : 0x1ec000

### How many DLLs were loaded by "notepad.exe"?

Using the filters : process name is "notepad.exe", operation is "load image" and path ends with ".dll" :

![Notepad filter](/images/thm/windowsinternals/windowsinternals_11.png)
_Notepad filter_

![Notepad filter 2](/images/thm/windowsinternals/windowsinternals_12.png)
_Notepad filter 2_

Answer : 51

## TASK 6 : Portable Executable Format
### Read the above and answer the questions below. 

No Answer.

### What PE component prints the message "This program cannot be run in DOS mode"?

Answer : DOS STUB

### Open "notepad.exe" in Detect It Easy and answer the questions below.

No Answer.

### What is the entry point reported by DiE?

Looking in the DIE app :

![Entry Point](/images/thm/windowsinternals/windowsinternals_13.png)
_Entry Point_

Answer : 000000014001acd0

### What is the value of "NumberOfSections"?

![NumberOfSections Value](/images/thm/windowsinternals/windowsinternals_14.png)
_NumberOfSections Value_

Answer : 0006

### What is the virtual address of ".data"?

Hint : Found in the Section tab of the PE window

![.data address](/images/thm/windowsinternals/windowsinternals_15.png)
_.data address_

Answer : 00024000

### What string is located at the offset "0001f99c"?

![Offset](/images/thm/windowsinternals/windowsinternals_16.png)
_Offset_

Answer : Microsoft.Notepad

## TASK 7 : Interacting with Windows Internals

### Open a command prompt and execute the provided file: "inject-poc.exe" and answer the questions below. 

No Answer.

### Enter the flag obtained from the executable below.

![Flag](/images/thm/windowsinternals/windowsinternals_17.png)
_Flag_

Answer : THM{1Nj3c7_4lL_7h3_7h1NG2}

## TASK 8 : Conclusion 
### Read the above and continue learning! 

No Answer.