---
title:  Linux modules
name: CYB3RM3 | Linux modules
author: CYB3RM3
date:   2021-09-14 20:24:31 +0100
categories: [TryHackMe, Linux]
tags: [Linux]
---

Learn linux modules in a fun way
THM Room [https://tryhackme.com/room/linuxmodules](https://tryhackme.com/room/linuxmodules)

## TASK 1 : Let's Introduce 

### Read the above.
    

No Answer  

## TASK 2 : du 

### Read the above.
    

No Answer

## TASK 3 : Grep, Egrep, Fgrep 

### Read the above
    

No Answer

### Is there a difference between egrep and fgrep? (Yea/Nay)
    

Answer : YEA  

### Which flag do you use to list out all the lines NOT containing the 'PATTERN'?
    

Answer : -v  

### Download the above given file and answer the following questions.
    

No Answer  

### What user did you find in that file?
    
```console
grep -i "user" gre.txt  
uxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7FuSeR:bobthebuilder6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6f  
```

Answer : bobthebuilder  

### What is the password of that user?
    
```console
grep -i "pass" gre.txt  
qEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTthispAsSwOrDistoosensitive:'LinuxIsGawd'XqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTX  
```

Answer : LinuxIsGawd  

### Can you find the comment that user just left?
    
```console
grep "comment" grep.txt  
8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2comment:'fs0ciety'u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM  
```

Answer : fs0ciety

## TASK 4 : Did someone said STROPS? 

### Press any key to continue...
    

No Answer  

## TASK 5 : tr 

### Read the Above.
    

No Answer  

### Run tr --help command and tell how will you select any digit character in the string ?
    
```console
tr --help  
Usage: tr [OPTION]... SET1 [SET2]  
Translate, squeeze, and/or delete characters from standard input,  
writing to standard output.  
  
 -c, -C, --complement use the complement of SET1  
 -d, --delete delete characters in SET1, do not translate  
 -s, --squeeze-repeats replace each sequence of a repeated character  
 that is listed in the last specified SET,  
 with a single occurrence of that character  
 -t, --truncate-set1 first truncate SET1 to length of SET2  
 --help display this help and exit  
 --version output version information and exit  
  
SETs are specified as strings of characters. Most represent themselves.  
Interpreted sequences are:  
  
 NNN character with octal value NNN (1 to 3 octal digits)  
  backslash  
 a audible BEL  
 b backspace  
 f form feed  
 n new line  
 r return  
 t horizontal tab  
 v vertical tab  
 CHAR1-CHAR2 all characters from CHAR1 to CHAR2 in ascending order  
 [CHAR*] in SET2, copies of CHAR until length of SET1  
 [CHAR*REPEAT] REPEAT copies of CHAR, REPEAT octal if starting with 0  
 [:alnum:] all letters and digits  
 [:alpha:] all letters  
 [:blank:] all horizontal whitespace  
 [:cntrl:] all control characters  
 [:digit:] all digits  
 [:graph:] all printable characters, not including space  
 [:lower:] all lower case letters  
 [:print:] all printable characters, including space  
 [:punct:] all punctuation characters  
 [:space:] all horizontal or vertical whitespace  
 [:upper:] all upper case letters  
 [:xdigit:] all hexadecimal digits  
 [=CHAR=] all characters which are equivalent to CHAR  
  
Translation occurs if -d is not given and both SET1 and SET2 appear.  
-t may be used only when translating. SET2 is extended to length of  
SET1 by repeating its last character as necessary. Excess characters  
of SET2 are ignored. Only [:lower:] and [:upper:] are guaranteed to  
expand in ascending order; used in SET2 while translating, they may  
only be used in pairs to specify case conversion. -s uses the last  
specified SET, and occurs after translation or deletion.  
  
GNU coreutils online help: &lt;http://www.gnu.org/software/coreutils/&gt;  
Full documentation at: &lt;http://www.gnu.org/software/coreutils/tr&gt;  
or available locally via: info '(coreutils) tr invocation'  
```

Answer : :digit:

### What sequence is equivalent to [a-zA-Z] set ?
    

Answer : :alpha:

### What sequence is equivalent to selecting hexadecimal characters ?
    

Answer : :xdigit:  

## TASK 6 : awk

### Read the above.
    

Answer : Hardware  

### Download the above given file, and use awk command to print the following output:  
      
    ippsec:34024  
    john:50024  
    thecybermentor:25923  
    liveoverflow:45345  
    nahamsec:12365  
    stok:1234
    
```console
awk 'BEGIN{FS=" "; OFS=":"} {print $1,$4}' awk.txt  
ippsec:34024  
john:50024  
thecybermentor:25923  
liveoverflow:45345  
nahamsec:12365  
stok:1234  
```

Well, i also tried the below command that return the good lines :

```console
awk 'BEGIN{OFS=":"} {print $1,$4}' awk.txt
```

But this was not the answer needed.  

Answer : awk 'BEGIN{FS=" "; OFS=":"} {print $1,$4}' awk.txt

### How will you make the output as following (there can be multiple; answer it using the above specified variables in BEGIN pattern):  
      
    ippsec, john, thecybermentor, liveoverflow, nahamsec, stok,
    
```console
awk 'BEGIN{ORS=","} {print $1}' awk.txt  
ippsec,john,thecybermentor,liveoverflow,nahamsec,stok,  
```

Answer : awk 'BEGIN{ORS=","} {print $1}' awk.txt

## TASK 7 : sed 

### How would you substitute every 3rd occurrence of the word 'hack' to 'back' on every line inside the file file.txt ?
    
Answer : sed 's/hack/back/3g' file.txt  

### How will you do the same operation only on 3rd and 4th line in file.txt?   

Answer : sed '3,4 s/hack/back/3g' file.txt

### Download the given file, and try formatting the trailing spaces in sed1.txt with a colon(:).
    
```console
root@ip-10-10-89-122:~/Desktop# sed 's/ */:/g' sed1.txt  
:u:s:e:r:p:a:s:s:w:o:r:d:  
:h:a:x:o:r:l:s:a:t:s:d:f:  
:n:o:m:a:n:d:a:d:x:i:f:t:o:x:1:2:3:  
:n:o:b:i:t:a:s:h:i:z:u:k:a:&lt;:3:  
:x:a:d:m:i:n:x:n:e:e:d:m:e:?:$:  
:p:e:t:e:r:p:a:n:T:i:n:k:e:r:B:e:l:l:6:9:  
:s:a:t:a:n:G:O:A:T:  
```

Answer : sed 's/ */:/g' sed1.txt

### View the sed2 file in the directory. Try putting all alphabetical values together, to get the answer for this question.
    
```console
root@ip-10-10-89-122:~/Desktop# sed 's/[0-9]*//g' sed2.txt  
CONGRATULATIONS  
YOU  
MADE  
IT  
THROUGH  
THIS  
SMALL  
LITTLE  
CHALLENGE  
```

Answer : CONGRATULATIONS YOU MADE IT THROUGH THIS SMALL LITTLE CHALLENGE

### What pattern did you use to reach that answer string ?
    

The regex use in the previous question works, but is not the one which was intended here, so i just replace the regex expression by [[:digit:]].

```console
root@ip-10-10-89-122:~/Desktop# sed 's/[[:digit:]]//g' sed2.txt  
CONGRATULATIONS  
YOU  
MADE  
IT  
THROUGH  
THIS  
SMALL  
LITTLE  
CHALLENGE  
```

Answer : 's/[[:digit:]]//g'

### Alternatively, you can use tr to remove all the digits, and then pipe the output in sed to remove trailing whitespaces.
    
```console
cat sed2.txt | tr '[:digit:]' ' ' | sed 's/ *//g'
```             

[Update] Another good way suggested by a room do-er. You can simply use tr -d command to delete all the digits from the file.

```console
cat sed2.txt | tr -d '[:digit:]'
```                

No Answer  

### What did she sed?(In double quotes)
    

Just a reference from the first line of this ## TASK.  

Answer : "That's What"

## TASK 8 : xargs

### Read the above.
    

No Answer

### You're working in a team and your team leader sent you a list of files that needs to be created ASAP within current directory so that he can fake the synopsis report (that needs to be submitted within a minute or 2) to the invigilator and change the permissions to read-only to only you(Numberic representation). You can find the files list in the "one" folder.  
    Use the following flags in ASCII order:  
      
     - Verbose  
     - Take argument as "files"  
    

Few keywords in this question : read-ony to you (chomd 400), verbose and take argument as "files" (-I file -t) in ASCII.  

Answer : 

```console
cat file | xargs -I files -t sh -c “touch files; chmod 400 files”  
```

### Your friend trying to run multiple commands in one line, and wanting to create a short version of rockyou.txt, messed up by creating files instead of redirecting the output into "shortrockyou". Now he messed up his home directory by creating a ton of files. He deleted rockyou wordlist in that one liner and can't seem to download it and do all that long process again.  
    He now seeks help from you, to create the wordlist and remove those extra files in his directory. You being a pro in linux, show him how it's done in one liner way.  
    Use the following flags in ASCII order:  
      
     - Take argument as "word"  
     - Verbose  
     - Max number of arguments should be 1 in for each file
    

You can find the files for this TASK in two folder.  

Few keywords too here : argument as word (-I word), max number of arguments equal 1 (-n 1) and verbose again (-t)  

Answer :

```console
ls | xargs -I word -n 1 -t sh -c ‘echo word &gt;&gt; shortrockyou; rm word’
```

### Which flag to use to specify max number of arguments in one line.
    

Answer : -n

### How will you escape command line flags to positional arguments?
    

Answer : --  

## TASK 9 : sort and uniq

### Read the above.
    

No Answer

### Download the file given for this TASK, find the uniq items after sorting the file. What is the 2271st word in the output ?  
    
    
```console
root@ip-10-10-230-20:~/Desktop# sort test.test | uniq &gt; sorted.txt  
root@ip-10-10-230-20:~/Desktop# sed -n '2271p' sorted.txt  
lollol  
```

Answer : lollol  

What was the index of term 'michele' ?

Use grep on the sorted file to get the word requested and the -n flag the print the line number :  


```console
root@ip-10-10-230-20:~/Desktop# grep -n 'michele' sorted.txt  
2550:michele  
```

Answer : 2550  






## TASK 10 : cURL 

### Read the above
    

No Answer  

### Which flag allows you to limit the download/upload rate of a file?
    

Just take a look on the table above ;-)

Or you can choose the --help way :

```console
root@ip-10-10-230-20:~/Desktop# curl --help | grep 'limit'  
 --limit-rate &lt;speed&gt; Limit transfer speed to RATE  
-Y, --speed-limit &lt;speed&gt; Stop transfers slower than this  
-y, --speed-time &lt;seconds&gt; Trigger 'speed-limit' abort after this time  
```

Answer : --limit-rate

### How will you curl the webpage of [https://tryhackme.com/](https://tryhackme.com) specifying user-agent as 'juzztesting'
    
```console
root@ip-10-10-230-20:~/Desktop# curl --help | grep 'agent'  
-A, --user-agent &lt;name&gt; Send User-Agent &lt;name&gt; to server  
```

Answer : curl -A juzztesting https://tryhackme.com/  

### Can curl perform upload operations?(Yea/Nah)
    
```console
root@ip-10-10-230-20:~/Desktop# curl --help | grep 'upload'  
-a, --append Append to target file when uploading  
 --crlf Convert LF to CRLF in upload  
-T, --upload-file &lt;file&gt; Transfer local FILE to destination  
```

Answer : YEA  

## TASK 11 : wget

### Read the above
    

No Answer

### How will you enable time logging at every new activity that this tool initiates?
    
```console
root@ip-10-10-230-20:~/Desktop# wget --help | grep 'time'  
 -N, --timestamping don't re-retrieve files unless newer than  
 requests in timestamping mode  
 --no-use-server-timestamps don't set the local file's timestamp by  
 -T, --timeout=SECONDS set all timeout values to SECONDS  
 --dns-timeout=SECS set the DNS lo  
```

Answer : -N  

### What command will you use to download https://xyz.com/mypackage.zip using wget, appending logs to an existing file named "package-logs.txt"
    
```console
root@ip-10-10-230-20:~/Desktop# wget --help | grep 'append'  
 -a, --append-output=FILE append messages to FILE  
```

Answer : wget -a package-logs.txt https://xyz.com/mypackage.zip  

### Write the command to read URLs from "file.txt" and limit the download speed to 1mbps.
    
```console
root@ip-10-10-230-20:~/Desktop# wget --help | grep 'download'  
 -i, --input-file=FILE download URLs found in local or external FILE  
 -nc, --no-clobber skip downloads that would download to  
 -c, --continue resume getting a partially-downloaded file  
 --start-pos=OFFSET start downloading from zero-based position OFFSET  
 --spider don't download anything  
 --limit-rate=RATE limit download rate to RATE  
[...]  
  
root@ip-10-10-230-20:~/Desktop# wget --help | grep 'limit'  
 -t,  --tries=NUMBER              set number of retries to NUMBER (0 unlimits)  
      --limit-rate=RATE           limit download rate to RATE  
```

Answer : wget -t file.txt --limit-rate=1  

## TASK 12 : xxd

### Read the above.
    

No Answer

### How will you seek at 10th byte(in hex) in file.txt and display only 50 bytes ?
    

Offset 10 -&gt; -s 0xA  
display 50 bytes -&gt; length of 50 bytes -&gt; -l 50 -b  

Answer : xxd -s 0xA -l 50 -b file.txt  

### How to display a n bytes of hexdump in 3 columns with a group of 3 octets per row from file.txt ? (Use flags alphabetically)
    

Take a look in the table and the quick note just below the table !  

Answer : xxd -g 3 -c 3 file.txt  

### Which has more precedence over the other -c flag or -g flag ?
    

The note below the table give us the answer : "[...] -c flag precedes over -g."

Answer : -c  

### Download the file and find the value of flag.
    
```console
root@ip-10-10-230-20:~/Desktop# xxd -p -r flag.txt | cat  
flag{wh3sdw0lw1gl9oqasad2fs48as}  
```

Answer : flag{wh3sdw0lw1gl9oqasad2fs48as}  

## TASK 13 : Others modules

### Read the last learning
    

No Answer  

### It's safe to run systemctl command and experiment on your main linux system neither following a proper guide or having any prior knowledge ? (Right/Wrong)
    

"[...] Note: If you don't know what you're doing, try using service instead [...]" and without this note, systemctl is doing changes on systemd's level so it's better that you know what you are doing while using it.  

Answer : Wrong  

### How will you import a given PGP private key. (Suppose the name of the file is key.gpg)
    

Let's google [it](https://knowledge.broadcom.com/external/article/180118/how-to-use-pgp-command-line-to-create-an.html) to have the exact syntax :  

pgp --import (input)

Answer : pgp --importkey.gpg  

### How will you list all port activity if netstat is not available on a machine ? (Full Name)
    

Answer : Sockets Statistics  

### What command can be used to fix a broken/irregular/weird acting terminal shell ?
    

_"reset command  
  
 Say if your terminal is not working properly, any problem is occurring, but you can't afford to close the shell, you're just one reset command away to get your shell back to normal."_  

Answer : Reset  

## TASK 14 : Is it night yet ? 

### Press F to pay respect
    
F : Easy nah ?  

Answer : F  








