---
title: Introduction to Antivirus
author: CYB3RM3
name: CYB3RM3 | Introduction to Antivirus
date: 2022-10-13 11:56:49 +0100
categories: [TryHackMe, Host Evasions]
tags: [Windows, Antivirus, Introduction]
---

Understand how antivirus software works and what detection techniques are used to bypass malicious file checks.

THM Room [https://tryhackme.com/room/introtoav](https://tryhackme.com/room/introtoav)

## TASK 1 : Introduction
### Let's get started! 

No Answer

## TASK 2 : Antivirus Software 


### What was the virus name that infected John McAfee's PC? 

 "McAfee Associates, Inc. started the first AV software implementation in 1987. It was called "VirusScan," and its main goal at that time was to remove a virus named "Brain" that infected John McAfee's computer.  Later, other companies joined in the battle against viruses. AV software was called scanners, and they were command-line software that searched for malicious patterns in files."

Answer : Brain

### Which PC Antivirus vendor implemented the first AV software on the market?

From previous question : McAfee.

Answer : McAfee

### Antivirus software is a _____-based security solution.

 "What is AV software?

  Antivirus (AV) software is an extra layer of security that aims to detect and prevent the execution and spread of malicious files in a target operating system.

  It is a host-based application that runs in real-time (in the background) to monitor and check the current and newly downloaded files. The AV software inspects and decides whether files are malicious using different techniques, which will be covered later in this room."

Answer : Host

## TASK 3 : Antivirus Features 
###  Which AV feature analyzes malware in a safe and isolated environment?

 "An emulator is an Antivirus feature that does further analysis on suspicious files. Once an emulator receives a request, the emulator runs the suspect (exe, DLL, PDF, etc.) files in a virtualized and controlled environment. It monitors the executable files' behavior during the execution, including the Windows APIs calls, Registry, and other Windows files. The following are examples of the artifact that the emulator may collect:

  API calls
  Memory dumps
  Filesystem modifications
  Log events
  Running processes
  Web requests

  An emulator stops the execution of a file when enough artifacts are collected to detect malware."

Answer : Emulator

### An _______ feature is a process of restoring or decrypting the compressed executable files to the original.

 "PE (Portable Executable) Parsing and Unpackers

  Malware hides and packs its malicious code by compressing and encrypting it within a payload. It decompresses and decrypts itself during runtime to make it harder to perform static analysis. Thus, AV software must be able to detect and unpack most of the known packers (UPX, Armadillo, ASPack, etc.) before the runtime for static analysis.

  Malware developers use various techniques, such as Packing, to shrink the size and change the malicious file's structure. Packing compresses the original executable file to make it harder to analyze. Therefore, AV software must have an unpacker feature to unpack protected or compressed executable files into the original code.

  Another feature that AV software must have is Windows Portable Executable (PE) header parser. Parsing PE of executable files helps distinguish malicious and legitimate software (.exe files). The PE file format in Windows (32 and 64 bits) contains various information and resources, such as object code, DLLs, icon files, font files, and core dumps."

Answer : unpacker

### Read the above to proceed to the next task, where we discuss the AV detection techniques.
No Answer.

## TASK 4 : Deploy the VM 
### Once you've deployed the VM, it will take a few minutes to boot up. Then, progress to the next task!
No Answer.

## TASK 5 : AV Static Detection
### What is the sigtool tool output to generate an MD5 of the AV-Check.exe binary? 
By using "sigtool.exe" in the ClamAV directory, we can find  the md5 of the AV-Check.exe sample :

```console
C:\Users\thm\Desktop\Samples>"C:\Program Files\ClamAV\sigtool.exe" --md5 AV-Check.exe
f4a974b0cf25dca7fbce8701b7ab3a88:6144:AV-Check.exe
```
{: .nolineno }

Answer : f4a974b0cf25dca7fbce8701b7ab3a88:6144:AV-Check.exe

### Use the strings tool to list all human-readable strings of the AV-Check binary. What is the flag?

To answer this question, we can use the "Strings" command to retreive all human-readable strings in a binary. Let's first check if it's already installed :

```console
C:\Users\thm\Desktop\Samples>Strings

Strings v2.54 - Search for ANSI and Unicode strings in binary images.
Copyright (C) 1999-2021 Mark Russinovich
Sysinternals - www.sysinternals.com

usage: Strings [-a] [-f offset] [-b bytes] [-n length] [-o] [-s] [-u] <file or directory>
-a     Ascii-only search (Unicode and Ascii is default)
-b     Bytes of file to scan
-f     File offset at which to start scanning.
-o     Print offset in file string was located
-n     Minimum string length (default is 3)
-s     Recurse subdirectories
-u     Unicode-only search (Unicode and Ascii is default)
-nobanner
       Do not display the startup banner and copyright message.
```
{: .nolineno }

It's OK, so we can now specify our binary :

```console
C:\Users\thm\Desktop\Samples>Strings AV-Check.exe

Strings v2.54 - Search for ANSI and Unicode strings in binary images.
Copyright (C) 1999-2021 Mark Russinovich
Sysinternals - www.sysinternals.com

!This program cannot be run in DOS mode.
.text
`.rsrc
@.reloc
[...]
--AV Found: {0}
--AV software is not found!
THM{Y0uC4nC-5tr16s}
z\V
WrapNonExceptionThrows
AV-Check
Copyright
[...]
```
{: .nolineno }

We can simplify the search in the result by piping the "findstr" command :

```console
C:\Users\thm\Desktop\Samples>Strings AV-Check.exe | findstr "THM"
THM{Y0uC4nC-5tr16s}
```
{: .nolineno }

Answer : THM{Y0uC4nC-5tr16s}

## TASK 6 : Other Detection Techniques 
### Which detection method is used to analyze malicious software inside virtual environments? 

 "Another method for dynamic detection is Sandboxing. A sandbox is a virtualized environment used to run malicious files separated from the host computer. This is usually done in an isolated environment, and the primary goal is to analyze how the malicious software acts in the system. Once the malicious software is confirmed, a unique signature and rule will be created based on the characteristic of the binary. Finally, a new update will be pushed into the cloud database for future use."

Answer : Dynamic Detection

## TASK 7 : AV Testing and Fingerprinting 
### For the C# AV fingerprint, try to rewrite the code in a different language, such as Python, and check whether VirusTotal flag it as malicious. 

I write an example AV check in python, based on a process listing example <https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/> using "psutil" tool :

```python
import psutil
# Iterate over all running process
AV_Check = { 
    "MsMpEng.exe", "AdAwareService.exe", "afwServ.exe", "avguard.exe", "AVGSvc.exe", 
    "bdagent.exe", "BullGuardCore.exe", "ekrn.exe", "fshoster32.exe", "GDScan.exe", 
    "avp.exe", "K7CrvSvc.exe", "McAPExe.exe", "NortonSecurity.exe", "PavFnSvr.exe", 
    "SavService.exe", "EnterpriseService.exe", "WRSA.exe", "ZAPrivacyService.exe"}
print("[+] Begin scanning for host AV")
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        if processName in AV_Check:
            print("[!] AV FOUND : " + processName , ' ::: ', processID)
            exit("[-] End scanning for host AV")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
```
{: .nolineno }

I tested this in a Windows VM running Eset Security :

```console
C:\Users\test\Desktop>python3 scan_av.py
[+] Begin scanning for host AV
[!] AV FOUND : ekrn.exe  :::  2208
[-] End scanning for host AV
```
{: .nolineno }

I submit my python script in VirusTotal <https://www.virustotal.com/gui/file/a632c1fe575e8678651756d0f6816fe8c69c01c06da7e9ca81ab749c2e520dfc/details> and it doesn't flag it as malicious :

![VirusTotal](/images/thm/introtoav/introtoav_1.png)
_VirusTotal_

![VirusTotal](/images/thm/introtoav/introtoav_2.png)
_VirusTotal_

No Answer.

### Read the Above!
No Answer.

## TASK 8 : Conclusion 
### Congrats on completing the room, and keep learning!
No Answer.