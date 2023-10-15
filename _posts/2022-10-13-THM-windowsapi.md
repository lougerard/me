---
title: Introduction to Windows API
author: CYB3RM3
name: CYB3RM3 | Introduction to Windows API
date: 2022-10-13 09:57:51 +0100
categories: [TryHackMe, Red Teaming]
tags: [Windows, API, Introduction]
---

Learn how to interact with the win32 API and understand its wide range of use cases

THM Room [https://tryhackme.com/room/windowsapi](https://tryhackme.com/room/windowsapi)


## TASK 1 : Introduction
### Read the above and continue to the next task. 
No Answer

## TASK 2 : Subsystem and Hardware Interaction
### Does a process in the user mode have direct hardware access? (Y/N) 
No, to have direct hardware access, you need to be in kernel mode.

Answer : N

### Does launching an application as an administrator open the process in kernel mode? (Y/N)
No, administrator is not kernel mode either.

Answer : N

## TASK 3 : Components of the Windows API
### What header file imports and defines the User32 DLL and structure? 
I first search for the keywords : "User32.DLL headers" on google and found a topic <https://stackoverflow.com/questions/22304715/which-header-file-loads-the-dlls-in-win32-api> on Stackoverflow :

![User32.dll](/images/thm/windowsapi/windowsapi_1.png)
_User32.dll_

This thread mention the windows.h header :

![windows.h](/images/thm/windowsapi/windowsapi_2.png)
_windows.h_

So I did a new research with this information and found the user32.dll in the Wikipedia page for Windows.h <https://en.wikipedia.org/wiki/Windows.h>:

![windows.h](/images/thm/windowsapi/windowsapi_3.png)
_windows.h_

Answer : winuser.h

### What parent header file contains all other required child and core header files?

From previous search : windows.h

Answer : Windows.h

## TASK 4 : OS Libraries
### What overarching namespace provides P/Invoke to .NET? 

From P/Invoke documentation from Microsoft .Net :

 "P/Invoke is a technology that allows you to access structs, callbacks, and functions in unmanaged libraries from your managed code. Most of the P/Invoke API is contained in two namespaces: System and System.Runtime.InteropServices. Using these two namespaces give you the tools to describe how you want to communicate with the native component."

Answer : system

### What memory protection solution obscures the process of importing API calls?

 "Each API call of the Win32 library resides in memory and requires a pointer to a memory address. The process of obtaining pointers to these functions is obscured because of ASLR (Address Space Layout Randomization) implementations; each language or package has a unique procedure to overcome ASLR. Throughout this room, we will discuss the two most popular implementations: P/Invoke and the Windows header file."

Answer : ASLR

## TASK 5 : API Call Structure
### Which character appended to an API call represents an ANSI encoding? 

![ANSI Ecnoding](/images/thm/windowsapi/windowsapi_4.png)
_ANSI Ecnoding_

Answer : A

### Which character appended to an API call represents extended functionality?

Answer : Ex

### What is the memory allocation type of 0x00080000 in the VirtualAlloc API call?

Let's go on Microsoft documentation <https://learn.microsoft.com/en-us/search/?terms=VirtualAlloc&scope=Desktop>:

![VirtualAlloc](/images/thm/windowsapi/windowsapi_5.png)
_VirtualAlloc_

Then i searched for 0x00080000 code :

![0x00080000](/images/thm/windowsapi/windowsapi_6.png)
_0x00080000_

Answer : MEM_RESET

## TASK 6 : C API Implementations
### Do you need to define a structure to use API calls in C? (Y/N) 

 "Microsoft provides low-level programming languages such as C and C++ with a pre-configured set of libraries that we can use to access needed API calls."

Answer : N

## TASK 7 : .NET and PowerShell API Implementations

### What method is used to import a required DLL? 

From the example sample :

![DllImport](/images/thm/windowsapi/windowsapi_7.png)
_DllImport_

Answer : DllImport

### What type of method is used to reference the API call to obtain a struct?

From TASK 4 :

![External](/images/thm/windowsapi/windowsapi_8.png)
_External_

Answer : External

## TASK 8 : Commonly Abused API Calls 

### Which API call returns the address of an exported DLL function? 

![GetProcAddress](/images/thm/windowsapi/windowsapi_9.png)
_GetProcAddress_

Answer : GetProcAddress

### Which API call imports a specified DLL into the address space of the calling process?
Answer : LoadLibraryA

## TASK 9 : Malware Case Study
### What Win32 API call is used to obtain a pseudo handle of our current process in the keylogger sample? 

From the API calls explanation we can answer the questions 1-4 :

![API Calls](/images/thm/windowsapi/windowsapi_10.png)
_API Calls_

But we can also answer this question by observing the given source code. The API call used by the "GetModuleHandle()" comes from the "curProcess.ProcessName" where the "curProcess" is the API call  "GetCurrentProcess()" on a process :

![GetCurrentProcess](/images/thm/windowsapi/windowsapi_11.png)
_GetCurrentProcess_

Answer : GetCurrentProcess

### What Win32 API call is used to set a hook on our current process in the keylogger sample?

From the source code, the API call "SetWindowsHookEx()" is our answer as it's applying on our "curProcess.ProcessName" :

![SetWindowsHookEx](/images/thm/windowsapi/windowsapi_12.png)
_SetWindowsHookEx_

Answer : SetWindowsHookEx

### What Win32 API call is used to obtain a handle from the pseudo handle in the keylogger sample?

![GetModuleHandle](/images/thm/windowsapi/windowsapi_13.png)
_GetModuleHandle_

It's simply the definition of the "GetModuleHandler" API call.

Answer : GetModuleHandle

### What Win32 API call is used unset the hook on our current process in the keylogger sample?

For the last one, we can view in the sample code in the "Main()" function that an "UnhookWindowsHookEx" API call is done after the application end running :

![UnhookWindowsHookEx](/images/thm/windowsapi/windowsapi_14.png)
_UnhookWindowsHookEx_

Answer : UnhookWindowsHookEx

### What Win32 API call is used to allocate memory for the size of the shellcode in the shellcode launcher sample?

We can anwser again with the help of the definition of the API calls :

![API calls](/images/thm/windowsapi/windowsapi_15.png)
_API calls_

But if we analyse the source code we can see a call to a function "VirtualAlloc" which takes in parameters the size of the shellcode ("shellcode.length") :

![VirtualAlloc](/images/thm/windowsapi/windowsapi_16.png)
_VirtualAlloc_

Answer : VirtualAlloc

### What native method is used to write shellcode to an allocated section of memory in the shellcode launcher sample?

The source code shows a call to a "Copy()" function with the "shellcode" in parameter and an address space :

![Marshal.Copy](/images/thm/windowsapi/windowsapi_17.png)
_Marshal.Copy_

Answer : Marshal.Copy

### What Win32 API call is used to create a new execution thread in the shellcode launcher sample?

Create functions are often named "Create[...]" so with no doubt here, the API call is "CreateThread()" and we can see it is also assigned to a variable "hthread" in the code :

![CreateThread](/images/thm/windowsapi/windowsapi_18.png)
_CreateThread_

Answer : CreateThread

### What Win32 API call is used to wait for the thread to exit in the shellcode launcher sample?

The last call API is done on "WaitForSingleObject()" which takes the "hthread" as parameter :

![WaitForSingleObject](/images/thm/windowsapi/windowsapi_19.png)
_WaitForSingleObject_

Answer : WaitForSingleObject

## TASK 10 : Conclusion 
### Read the above and continue learning!
No Answer.