---
title: Volatility
author: CYB3RM3
name: CYB3RM3 | Volatility
date: 2022-01-22 14:10:22 +0100
categories: [TryHackMe, Forensics]
tags: [Forensics, Volatility]
---

Learn how to perform memory forensics with Volatility!

THM Room [https://tryhackme.com/room/bpvolatility](https://tryhackme.com/room/bpvolatility)


## TASK 1 : Intro
### Install Volatility onto your workstation of choice or use the provided virtual machine. On Debian-based systems such as Kali this can be done via `apt-get install volatility`
No Answer

## TASK 2 : Obtaining Memory Samples
### What memory format is the most common?
Answer : .raw

### The Window's system we're looking to perform memory forensics on was turned off by mistake. What file contains a compressed memory image?
Answer : hiberfil.sys

### How about if we wanted to perform memory forensics on a VMware-based virtual machine?
Answer : .vmem

## TASK 3 : Examining Our Patient
### First, let's figure out what profile we need to use. Profiles determine how Volatility treats our memory image since every version of Windows is a little bit different. Let's see our options now with the command `volatility -f MEMORY_FILE.raw imageinfo`

```console
voluser@vol-server:~$ volatility -f cridex.vmem imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/voluser/cridex.vmem)
                      PAE type : PAE
                           DTB : 0x2fe000L
                          KDBG : 0x80545ae0L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2012-07-22 02:45:08 UTC+0000
     Image local date and time : 2012-07-21 22:45:08 -0400
```
{: .nolineno }

No Answer.

### Running the imageinfo command in Volatility will provide us with a number of profiles we can test with, however, only one will be correct. We can test these profiles using the pslist command, validating our profile selection by the sheer number of returned results. Do this now with the command `volatility -f MEMORY_FILE.raw --profile=PROFILE pslist`. What profile is correct for this memory image?

From the above result :

```console
[...]
Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
[...]
```
{: .nolineno }

Answer : WinXPSP2x86

### Take a look through the processes within our image. What is the process ID for the smss.exe process? If results are scrolling off-screen, try piping your output into less

```console
voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 pslist
Volatility Foundation Volatility Framework 2.6
Offset(V)  Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit       
                   
---------- -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ -----------
-------------------
0x823c89c8 System                    4      0     53      240 ------      0                                           
                   
0x822f1020 smss.exe                368      4      3       19 ------      0 2012-07-22 02:42:31 UTC+0000              
                   
0x822a0598 csrss.exe               584    368      9      326      0      0 2012-07-22 02:42:32 UTC+0000              
                   
0x82298700 winlogon.exe            608    368     23      519      0      0 2012-07-22 02:42:32 UTC+0000              
                   
0x81e2ab28 services.exe            652    608     16      243      0      0 2012-07-22 02:42:32 UTC+0000              
                   
0x81e2a3b8 lsass.exe               664    608     24      330      0      0 2012-07-22 02:42:32 UTC+0000              
                   
0x82311360 svchost.exe             824    652     20      194      0      0 2012-07-22 02:42:33 UTC+0000              
                   
0x81e29ab8 svchost.exe             908    652      9      226      0      0 2012-07-22 02:42:33 UTC+0000              
                   
0x823001d0 svchost.exe            1004    652     64     1118      0      0 2012-07-22 02:42:33 UTC+0000              
                   
0x821dfda0 svchost.exe            1056    652      5       60      0      0 2012-07-22 02:42:33 UTC+0000              
                   
0x82295650 svchost.exe            1220    652     15      197      0      0 2012-07-22 02:42:35 UTC+0000              
                   
0x821dea70 explorer.exe           1484   1464     17      415      0      0 2012-07-22 02:42:36 UTC+0000              
                   
0x81eb17b8 spoolsv.exe            1512    652     14      113      0      0 2012-07-22 02:42:36 UTC+0000              
                   
0x81e7bda0 reader_sl.exe          1640   1484      5       39      0      0 2012-07-22 02:42:36 UTC+0000              
                   
0x820e8da0 alg.exe                 788    652      7      104      0      0 2012-07-22 02:43:01 UTC+0000              
                   
0x821fcda0 wuauclt.exe            1136   1004      8      173      0      0 2012-07-22 02:43:46 UTC+0000              
                   
0x8205bda0 wuauclt.exe            1588   1004      5      132      0      0 2012-07-22 02:44:01 UTC+0000
```
{: .nolineno }

Answer : 368

### In addition to viewing active processes, we can also view active network connections at the time of image creation! Let's do this now with the command `volatility -f MEMORY_FILE.raw --profile=PROFILE netscan`. Unfortunately, something not great is going to happen here due to the sheer age of the target operating system as the command netscan doesn't support it.

```console
voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 netscan
Volatility Foundation Volatility Framework 2.6
ERROR   : volatility.debug    : This command does not support the profile WinXPSP2x86
```
{: .nolineno }

No Answer.

### It's fairly common for malware to attempt to hide itself and the process associated with it. That being said, we can view intentionally hidden processes via the command `psxview`. What process has only one 'False' listed?

```console
voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 netscan
Volatility Foundation Volatility Framework 2.6
ERROR   : volatility.debug    : This command does not support the profile WinXPSP2x86
voluser@vol-server:~$ 


It's fairly common for malware to attempt to hide itself and the process associated with it. That being said, we can view intentionally hidden processes via the command `psxview`. What process has only one 'False' listed?

voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 psxview
Volatility Foundation Volatility Framework 2.6
Offset(P)  Name                    PID pslist psscan thrdproc pspcid csrss session deskthrd ExitTime
---------- -------------------- ------ ------ ------ -------- ------ ----- ------- -------- --------

0x02498700 winlogon.exe            608 True   True   True     True   True  True    True     
0x02511360 svchost.exe             824 True   True   True     True   True  True    True     
0x022e8da0 alg.exe                 788 True   True   True     True   True  True    True     
0x020b17b8 spoolsv.exe            1512 True   True   True     True   True  True    True     
0x0202ab28 services.exe            652 True   True   True     True   True  True    True     
0x02495650 svchost.exe            1220 True   True   True     True   True  True    True     
0x0207bda0 reader_sl.exe          1640 True   True   True     True   True  True    True     
0x025001d0 svchost.exe            1004 True   True   True     True   True  True    True     
0x02029ab8 svchost.exe             908 True   True   True     True   True  True    True     
0x023fcda0 wuauclt.exe            1136 True   True   True     True   True  True    True     
0x0225bda0 wuauclt.exe            1588 True   True   True     True   True  True    True     
0x0202a3b8 lsass.exe               664 True   True   True     True   True  True    True     
0x023dea70 explorer.exe           1484 True   True   True     True   True  True    True     
0x023dfda0 svchost.exe            1056 True   True   True     True   True  True    True     
0x024f1020 smss.exe                368 True   True   True     True   False False   False    
0x025c89c8 System                    4 True   True   True     True   False False   False    
0x024a0598 csrss.exe               584 True   True   True     True   False True    True
```
{: .nolineno }

Answer : csrss.exe

### In addition to viewing hidden processes via psxview, we can also check this with a greater focus via the command 'ldrmodules'. Three columns will appear here in the middle, InLoad, InInit, InMem. If any of these are false, that module has likely been injected which is a really bad thing. On a normal system the grep statement above should return no output. Which process has all three columns listed as 'False' (other than System)?

```console
voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 ldrmodules
Volatility Foundation Volatility Framework 2.6
Pid      Process              Base       InLoad InInit InMem MappedPath
-------- -------------------- ---------- ------ ------ ----- ----------
       4 System               0x7c900000 False  False  False \WINDOWS\system32\ntdll.dll
     368 smss.exe             0x48580000 True   False  True  \WINDOWS\system32\smss.exe
     368 smss.exe             0x7c900000 True   True   True  \WINDOWS\system32\ntdll.dll
     584 csrss.exe            0x00460000 False  False  False \WINDOWS\Fonts\vgasys.fon
     584 csrss.exe            0x4a680000 True   False  True  \WINDOWS\system32\csrss.exe
     584 csrss.exe            0x75b40000 True   True   True  \WINDOWS\system32\csrsrv.dll
     584 csrss.exe            0x75b50000 True   True   True  \WINDOWS\system32\basesrv.dll
     584 csrss.exe            0x7e720000 True   True   True  \WINDOWS\system32\sxs.dll
     584 csrss.exe            0x77e70000 True   True   True  \WINDOWS\system32\rpcrt4.dll
     584 csrss.exe            0x7c800000 True   True   True  \WINDOWS\system32\kernel32.dll
     584 csrss.exe            0x77dd0000 True   True   True  \WINDOWS\system32\advapi32.dll
     584 csrss.exe            0x77fe0000 True   True   True  \WINDOWS\system32\secur32.dll
     584 csrss.exe            0x7e410000 True   True   True  \WINDOWS\system32\user32.dll
     584 csrss.exe            0x7c900000 True   True   True  \WINDOWS\system32\ntdll.dll
     584 csrss.exe            0x77f10000 True   True   True  \WINDOWS\system32\gdi32.dll
     584 csrss.exe            0x75b60000 True   True   True  \WINDOWS\system32\winsrv.dll
     608 winlogon.exe         0x01000000 True   False  True  \WINDOWS\system32\winlogon.exe
     608 winlogon.exe         0x01630000 True   True   True  \WINDOWS\system32\xpsp2res.dll
[...]
```
{: .nolineno }

Answer : csrss.exe

### Processes aren't the only area we're concerned with when we're examining a machine. Using the 'apihooks' command we can view unexpected patches in the standard system DLLs. If we see an instance where Hooking module: <unknown> that's really bad. This command will take a while to run, however, it will show you all of the extraneous code introduced by the malware.

```console
volatility -f cridex.vmem --profile=WinXPSP2x86 apihooks
[...]
************************************************************************
Hook mode: Usermode
Hook type: Inline/Trampoline
Process: 1484 (explorer.exe)
Victim module: Secur32.dll (0x77fe0000 - 0x77ff1000)
Function: Secur32.dll!EncryptMessage at 0x77fea5fb
Hook address: 0x146a1e0
Hooking module: <unknown>

Disassembly(0):
0x77fea5fb e9e0fb4789       JMP 0x146a1e0
0x77fea600 51               PUSH ECX
0x77fea601 51               PUSH ECX
0x77fea602 56               PUSH ESI
0x77fea603 8d45f8           LEA EAX, [EBP-0x8]
0x77fea606 50               PUSH EAX
0x77fea607 ff7508           PUSH DWORD [EBP+0x8]
0x77fea60a 6a01             PUSH 0x1
0x77fea60c e87683ffff       CALL 0x77fe2987
0x77fea611 8bf0             MOV ESI, EAX

Disassembly(1):
0x146a1e0 83ec0c           SUB ESP, 0xc
0x146a1e3 33c0             XOR EAX, EAX
0x146a1e5 3944241c         CMP [ESP+0x1c], EAX
0x146a1e9 53               PUSH EBX
0x146a1ea 8b5c241c         MOV EBX, [ESP+0x1c]
0x146a1ee 0f85e7000000     JNZ 0x146a2db
0x146a1f4 394304           CMP [EBX+0x4], EAX
0x146a1f7 89               DB 0x89
[...]
```
{: .nolineno }

No Answer.

### Injected code can be a huge issue and is highly indicative of very very bad things. We can check for this with the command `malfind`. Using the full command `volatility -f MEMORY_FILE.raw --profile=PROFILE malfind -D <Destination Directory>` we can not only find this code, but also dump it to our specified directory. Let's do this now! We'll use this dump later for more analysis. How many files does this generate?

```console
voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 malfind -D  .
Volatility Foundation Volatility Framework 2.6
Process: csrss.exe Pid: 584 Address: 0x7f6f0000
Vad Tag: Vad  Protection: PAGE_EXECUTE_READWRITE
Flags: Protection: 6

0x7f6f0000  c8 00 00 00 91 01 00 00 ff ee ff ee 08 70 00 00   .............p..
0x7f6f0010  08 00 00 00 00 fe 00 00 00 00 10 00 00 20 00 00   ................
0x7f6f0020  00 02 00 00 00 20 00 00 8d 01 00 00 ff ef fd 7f   ................
0x7f6f0030  03 00 08 06 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x7f6f0000 c8000000         ENTER 0x0, 0x0
0x7f6f0004 91               XCHG ECX, EAX
0x7f6f0005 0100             ADD [EAX], EAX
0x7f6f0007 00ff             ADD BH, BH
0x7f6f0009 ee               OUT DX, AL
0x7f6f000a ff               DB 0xff
0x7f6f000b ee               OUT DX, AL
0x7f6f000c 087000           OR [EAX+0x0], DH
0x7f6f000f 0008             ADD [EAX], CL
0x7f6f0011 0000             ADD [EAX], AL
0x7f6f0013 0000             ADD [EAX], AL
0x7f6f0015 fe00             INC BYTE [EAX]
0x7f6f0017 0000             ADD [EAX], AL
0x7f6f0019 0010             ADD [EAX], DL
0x7f6f001b 0000             ADD [EAX], AL
0x7f6f001d 2000             AND [EAX], AL
0x7f6f001f 0000             ADD [EAX], AL
0x7f6f0021 0200             ADD AL, [EAX]
0x7f6f0023 0000             ADD [EAX], AL
0x7f6f0025 2000             AND [EAX], AL
0x7f6f0027 008d010000ff     ADD [EBP-0xffffff], CL
0x7f6f002d ef               OUT DX, EAX
0x7f6f002e fd               STD
0x7f6f002f 7f03             JG 0x7f6f0034
0x7f6f0031 0008             ADD [EAX], CL
0x7f6f0033 06               PUSH ES
0x7f6f0034 0000             ADD [EAX], AL
0x7f6f0036 0000             ADD [EAX], AL
0x7f6f0038 0000             ADD [EAX], AL
0x7f6f003a 0000             ADD [EAX], AL
0x7f6f003c 0000             ADD [EAX], AL
0x7f6f003e 0000             ADD [EAX], AL

[...]

voluser@vol-server:~$ ls
cridex_memdump.zip                 process.0x82298700.0x4c540000.dmp  process.0x82298700.0x6a230000.dmp
cridex.vmem                        process.0x82298700.0x4dc40000.dmp  process.0x82298700.0x73f40000.dmp
process.0x81e7bda0.0x3d0000.dmp    process.0x82298700.0x4ee0000.dmp   process.0x82298700.0xf9e0000.dmp
process.0x821dea70.0x1460000.dmp   process.0x82298700.0x554c0000.dmp  process.0x822a0598.0x7f6f0000.dmp
process.0x82298700.0x13410000.dmp  process.0x82298700.0x5de10000.dmp
voluser@vol-server:~$ ls | grep "dmp" | wc -l
12
```
{: .nolineno }

Executing the command then counting the result dumping to the current directory (-D .)

Answer : 12

### Last but certainly not least we can view all of the DLLs loaded into memory. DLLs are shared system libraries utilized in system processes. These are commonly subjected to hijacking and other side-loading attacks, making them a key target for forensics. Let's list all of the DLLs in memory now with the command `dlllist`

```console
voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 dlllist
Volatility Foundation Volatility Framework 2.6
************************************************************************
System pid:      4
Unable to read PEB for task.
************************************************************************
smss.exe pid:    368
Command line : \SystemRoot\System32\smss.exe


Base             Size  LoadCount LoadTime                       Path
---------- ---------- ---------- ------------------------------ ----
0x48580000     0xf000     0xffff                                \SystemRoot\System32\smss.exe
0x7c900000    0xaf000     0xffff                                C:\WINDOWS\system32\ntdll.dll
************************************************************************
csrss.exe pid:    584
Command line : C:\WINDOWS\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,3072,512 Windows=On SubSystem
Type=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitializ
ation,2 ProfileControl=Off MaxRequestThreads=16
Service Pack 3

Base             Size  LoadCount LoadTime                       Path
---------- ---------- ---------- ------------------------------ ----
0x4a680000     0x5000     0xffff                                \??\C:\WINDOWS\system32\csrss.exe
0x7c900000    0xaf000     0xffff                                C:\WINDOWS\system32\ntdll.dll
0x75b40000     0xb000     0xffff                                C:\WINDOWS\system32\CSRSRV.dll
0x75b50000    0x10000        0x3                                C:\WINDOWS\system32\basesrv.dll
0x75b60000    0x4b000        0x2                                C:\WINDOWS\system32\winsrv.dll
0x77f10000    0x49000        0x5                                C:\WINDOWS\system32\GDI32.dll
0x7c800000    0xf6000       0x10                                C:\WINDOWS\system32\KERNEL32.dll
0x7e410000    0x91000        0x6                                C:\WINDOWS\system32\USER32.dll
0x7e720000    0xb0000        0x1                                C:\WINDOWS\system32\sxs.dll
0x77dd0000    0x9b000        0x5                                C:\WINDOWS\system32\ADVAPI32.dll
0x77e70000    0x92000        0x3                                C:\WINDOWS\system32\RPCRT4.dll
0x77fe0000    0x11000        0x2                                C:\WINDOWS\system32\Secur32.dll
************************************************************************
winlogon.exe pid:    608
Command line : winlogon.exe
Service Pack 3
[...]
```
{: .nolineno }

No Answer.

### Now that we've seen all of the DLLs running in memory, let's go a step further and pull them out! Do this now with the command `volatility -f MEMORY_FILE.raw --profile=PROFILE --pid=PID dlldump -D <Destination Directory>` where the PID is the process ID of the infected process we identified earlier (questions five and six). How many DLLs does this end up pulling?

```console
voluser@vol-server:~$ mkdir dumpdll
voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 --pid=PID dlldump -D dumpdll/
Volatility Foundation Volatility Framework 2.6
Process(V) Name                 Module Base Module Name          Result
---------- -------------------- ----------- -------------------- ------
ERROR   : volatility.debug    : Invalid PID PID
voluser@vol-server:~$ volatility -f cridex.vmem --profile=WinXPSP2x86 --pid=584 dlldump -D dumpdll/
Volatility Foundation Volatility Framework 2.6
Process(V) Name                 Module Base Module Name          Result
---------- -------------------- ----------- -------------------- ------
0x822a0598 csrss.exe            0x04a680000 csrss.exe            OK: module.584.24a0598.4a680000.dll
0x822a0598 csrss.exe            0x07c900000 ntdll.dll            OK: module.584.24a0598.7c900000.dll
0x822a0598 csrss.exe            0x075b40000 CSRSRV.dll           OK: module.584.24a0598.75b40000.dll
0x822a0598 csrss.exe            0x077f10000 GDI32.dll            OK: module.584.24a0598.77f10000.dll
0x822a0598 csrss.exe            0x07e720000 sxs.dll              OK: module.584.24a0598.7e720000.dll
0x822a0598 csrss.exe            0x077e70000 RPCRT4.dll           OK: module.584.24a0598.77e70000.dll
0x822a0598 csrss.exe            0x077dd0000 ADVAPI32.dll         OK: module.584.24a0598.77dd0000.dll
0x822a0598 csrss.exe            0x077fe0000 Secur32.dll          OK: module.584.24a0598.77fe0000.dll
0x822a0598 csrss.exe            0x075b50000 basesrv.dll          OK: module.584.24a0598.75b50000.dll
0x822a0598 csrss.exe            0x07c800000 KERNEL32.dll         OK: module.584.24a0598.7c800000.dll
0x822a0598 csrss.exe            0x07e410000 USER32.dll           OK: module.584.24a0598.7e410000.dll
0x822a0598 csrss.exe		0x075b60000 winsrv.dll           OK: module.584.24a0598.75b60000.dll

voluser@vol-server:~$ cd dumpdll/
voluser@vol-server:~/dumpdll$ ls | wc -l
12
```
{: .nolineno }

Answer : 12

## TASK 4 : Post Actions
### Upload the extracted files to VirusTotal for examination. 
No ANswer.

### Upload the extracted files to Hybrid Analysis for examination - Note, this will also upload to VirusTotal but for the sake of demonstration we have done this separately.
No Answer.

### What malware has our sample been infected with? You can find this in the results of VirusTotal and Hybrid Anaylsis.
Loooking on hybrid analysis the name of our file :

![Cridex](/images/thm/bpvolatility/bpvolatility_1.png)
_Cridex_

Answer : Cridex

## TASK 5 : Extra Credit
### Check out the resources provided above! 
No Answer.