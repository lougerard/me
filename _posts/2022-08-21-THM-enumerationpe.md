---
title: Enumeration 
author: CYB3RM3
name: CYB3RM3 | Enumeration 
date: 2022-08-21 10:43:05 +0100
categories: [TryHackMe, Post Compromise]
tags: [Enumeration, Collect Intels, Red Team]
---

This room is an introduction to enumeration when approaching an unknown corporate environment.

THM Room [https://tryhackme.com/room/enumerationpe](https://tryhackme.com/room/enumerationpe)


## TASK 1 : Introduction
### What command would you use to start the PowerShell interactive command line?

If you don't know this, you can find the answer from the text : "We just issued the command powershell.exe to start the PowerShell interactive command line in the terminal below."

Answer : powershell.exe

## TASK 2 : Purpose
### In SSH key-based authentication, which key does the client need?
Again, this question is trivial when you knows ssh but from the text : " the public key is installed on a server. Consequently, the server would trust any system that can prove knowledge of the related private key."

Answer : private key

## TASK 3 : Linux Enumeration
###  What is the Linux distribution used in the VM?
Connecting on the target machine via SSH and printing the /etc/os-release file : 

```
root@ip-10-10-120-247:~# ssh user@10.10.204.207
The authenticity of host '10.10.204.207 (10.10.204.207)' can't be established.
ECDSA key fingerprint is SHA256:IFP+sTfHTDm72Ta2zfK9XjKASr30+ya4ic/ApEIziio.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.204.207' (ECDSA) to the list of known hosts.
user@10.10.204.207's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-120-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun 21 Aug 07:36:37 UTC 2022

  System load:  0.08              Processes:             121
  Usage of /:   62.2% of 6.53GB   Users logged in:       0
  Memory usage: 26%               IPv4 address for eth0: 10.10.204.207
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

user@red-linux-enumeration:~$ cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.4 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.4 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```
{: .nolineno }

We can now see the linux distribution and the version number

Answer : Ubuntu

### What is its version number?

Answer : 20.04.4

### What is the name of the user who last logged in to the system?

Wen can view the last logged on user by typing the command "last" in linux :

```
user@red-linux-enumeration:~$ last
user     pts/0        10.10.120.247    Sun Aug 21 07:36   still logged in
reboot   system boot  5.4.0-120-generi Sun Aug 21 07:23   still running
reboot   system boot  5.4.0-120-generi Mon Jun 20 13:10 - 13:13  (00:02)
randa    pts/0        10.20.30.1       Mon Jun 20 11:00 - 11:01  (00:00)
reboot   system boot  5.4.0-120-generi Mon Jun 20 09:58 - 11:01  (01:03)
```
{: .nolineno }

Answer : randa

### What is the highest listening TCP port number?

We can see the listening connection with netstat command. First, let's see the help :

```
user@red-linux-enumeration:~$ netstat --help
usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
       netstat [-vWnNcaeol] [<Socket> ...]
       netstat { [-vWeenNac] -i | [-cnNe] -M | -s [-6tuw] }

        -r, --route              display routing table
        -i, --interfaces         display interface table
        -g, --groups             display multicast group memberships
        -s, --statistics         display networking statistics (like SNMP)
        -M, --masquerade         display masqueraded connections

        -v, --verbose            be verbose
        -W, --wide               don't truncate IP addresses
        -n, --numeric            don't resolve names
        --numeric-hosts          don't resolve host names
        --numeric-ports          don't resolve port names
        --numeric-users          don't resolve user names
        -N, --symbolic           resolve hardware names
        -e, --extend             display other/more information
        -p, --programs           display PID/Program name for sockets
        -o, --timers             display timers
        -c, --continuous         continuous listing

        -l, --listening          display listening server sockets
        -a, --all                display all sockets (default: connected)
        -F, --fib                display Forwarding Information Base (default)
        -C, --cache              display routing cache instead of FIB
        -Z, --context            display SELinux security context for sockets

  <Socket>={-t|--tcp} {-u|--udp} {-U|--udplite} {-S|--sctp} {-w|--raw}
           {-x|--unix} --ax25 --ipx --netrom
  <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25) 
    netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP) 
    x25 (CCITT X.25) 
user@red-linux-enumeration:~$
```
{: .nolineno }

There are several interesting switches to use :

    -l to display only listenning connection

    -v for verbose

    -a to display all sockets

    -t to print only tcp sockets

```
user@red-linux-enumeration:~$ netstat -lva -t
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 ip-10-10-204-207:domain 0.0.0.0:*               LISTEN     
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN     
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0      0 localhost:953           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ldap            0.0.0.0:*               LISTEN     
tcp        0      0 localhost:ircd          0.0.0.0:*               LISTEN     
tcp        0    280 ip-10-10-204-207.eu:ssh ip-10-10-120-247.:53368 ESTABLISHED
tcp        0      1 ip-10-10-204-207.:59010 api.snapcraft.io:https  SYN_SENT   
tcp        0      1 ip-10-10-204-207.:37082 api.snapcraft.io:https  SYN_SENT   
tcp        0      1 ip-10-10-204-207.:42706 api.snapcraft.io:https  SYN_SENT   
tcp        0      1 ip-10-10-204-207.:42708 api.snapcraft.io:https  SYN_SENT   
tcp6       0      0 red-linux-enumer:domain [::]:*                  LISTEN     
tcp6       0      0 ip6-localhost:domain    [::]:*                  LISTEN     
tcp6       0      0 [::]:ftp                [::]:*                  LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
tcp6       0      0 ip6-localhost:953       [::]:*                  LISTEN     
tcp6       0      0 [::]:ldap               [::]:*                  LISTEN 
```
{: .nolineno }

We can see that some ports is not displayed in numeric, so we can add the -n switch to our command :

```
user@red-linux-enumeration:~$ netstat -lvan -t | grep "LISTEN"
tcp        0      0 10.10.204.207:53        0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:389             0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:6667          0.0.0.0:*               LISTEN     
tcp6       0      0 fe80::e5:24ff:fe6d:7:53 :::*                    LISTEN     
tcp6       0      0 ::1:53                  :::*                    LISTEN     
tcp6       0      0 :::21                   :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
tcp6       0      0 ::1:953                 :::*                    LISTEN     
tcp6       0      0 :::389                  :::*                    LISTEN 
```
{: .nolineno }

We now have the highest TCP port listening.

Answer : 6667

### What is the program name of the service listening on it?

We can add the -p for printing programs informations :

```
user@red-linux-enumeration:~$ sudo netstat -lvanp -t
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 10.10.204.207:53        0.0.0.0:*               LISTEN      611/named           
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      611/named           
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      580/systemd-resolve 
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      683/sshd: /usr/sbin 
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      611/named           
tcp        0      0 0.0.0.0:389             0.0.0.0:*               LISTEN      722/slapd           
tcp        0      0 127.0.0.1:6667          0.0.0.0:*               LISTEN      712/inspircd        
tcp        0    304 10.10.204.207:22        10.10.120.247:53368     ESTABLISHED 1000/sshd: user [pr 
tcp6       0      0 fe80::e5:24ff:fe6d:7:53 :::*                    LISTEN      611/named           
tcp6       0      0 ::1:53                  :::*                    LISTEN      611/named           
tcp6       0      0 :::21                   :::*                    LISTEN      635/vsftpd          
tcp6       0      0 :::22                   :::*                    LISTEN      683/sshd: /usr/sbin 
tcp6       0      0 ::1:953                 :::*                    LISTEN      611/named           
tcp6       0      0 :::389                  :::*                    LISTEN      722/slapd 
```
{: .nolineno }

Answer : inspircd

### There is a script running in the background. Its name starts with THM. What is the name of the script?

To check the processes running in background, we can use the "ps" command :

```
user@red-linux-enumeration:~$ ps -aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.9  1.1 102716 11484 ?        Rs   07:23   0:08 /sbin/init auto automatic-ubiquity noprompt
root           2  0.0  0.0      0     0 ?        S    07:23   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   07:23   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   07:23   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I    07:23   0:00 [kworker/0:0-memcg_kmem_cache]
root           6  0.0  0.0      0     0 ?        I<   07:23   0:00 [kworker/0:0H-kblockd]
root           8  0.0  0.0      0     0 ?        I    07:23   0:00 [kworker/u30:0-events_unbound]
root           9  0.0  0.0      0     0 ?        I<   07:23   0:00 [mm_percpu_wq]
root          10  0.0  0.0      0     0 ?        S    07:23   0:00 [ksoftirqd/0]
root          11  0.0  0.0      0     0 ?        I    07:23   0:00 [rcu_sched]
root          12  0.0  0.0      0     0 ?        S    07:23   0:00 [migration/0]
root          13  0.0  0.0      0     0 ?        S    07:23   0:00 [idle_inject/0]
root          14  0.0  0.0      0     0 ?        S    07:23   0:00 [cpuhp/0]
root          15  0.0  0.0      0     0 ?        S    07:23   0:00 [kdevtmpfs]
root          16  0.0  0.0      0     0 ?        I<   07:23   0:00 [netns]
root          17  0.0  0.0      0     0 ?        S    07:23   0:00 [rcu_tasks_kthre]
root          18  0.0  0.0      0     0 ?        S    07:23   0:00 [kauditd]
root          19  0.0  0.0      0     0 ?        S    07:23   0:00 [khungtaskd]
root          20  0.0  0.0      0     0 ?        S    07:23   0:00 [oom_reaper]
root          21  0.0  0.0      0     0 ?        I<   07:23   0:00 [writeback]
root          22  0.0  0.0      0     0 ?        S    07:23   0:00 [kcompactd0]
root          23  0.0  0.0      0     0 ?        SN   07:23   0:00 [ksmd]
root          24  0.0  0.0      0     0 ?        SN   07:23   0:00 [khugepaged]
root          70  0.0  0.0      0     0 ?        I<   07:23   0:00 [kintegrityd]
root          71  0.0  0.0      0     0 ?        I<   07:23   0:00 [kblockd]
root          72  0.0  0.0      0     0 ?        I<   07:23   0:00 [blkcg_punt_bio]
root          73  0.0  0.0      0     0 ?        S    07:23   0:00 [xen-balloon]
root          74  0.0  0.0      0     0 ?        I<   07:23   0:00 [tpm_dev_wq]
root          75  0.0  0.0      0     0 ?        I<   07:23   0:00 [ata_sff]
root          76  0.0  0.0      0     0 ?        I<   07:23   0:00 [md]
root          77  0.0  0.0      0     0 ?        I<   07:23   0:00 [edac-poller]
root          78  0.0  0.0      0     0 ?        I<   07:23   0:00 [devfreq_wq]
root          79  0.0  0.0      0     0 ?        S    07:23   0:00 [watchdogd]
root          80  0.0  0.0      0     0 ?        I    07:23   0:00 [kworker/u30:1-events_power_efficient]
root          84  0.0  0.0      0     0 ?        S    07:23   0:00 [kswapd0]
root          85  0.0  0.0      0     0 ?        S    07:23   0:00 [ecryptfs-kthrea]
root          87  0.0  0.0      0     0 ?        I<   07:23   0:00 [kthrotld]
root          88  0.0  0.0      0     0 ?        I<   07:23   0:00 [acpi_thermal_pm]
root          89  0.0  0.0      0     0 ?        S    07:23   0:00 [xenbus]
root          90  0.0  0.0      0     0 ?        S    07:23   0:00 [xenwatch]
root          91  0.0  0.0      0     0 ?        S    07:23   0:00 [scsi_eh_0]
root          92  0.0  0.0      0     0 ?        I<   07:23   0:00 [scsi_tmf_0]
root          93  0.0  0.0      0     0 ?        S    07:23   0:00 [scsi_eh_1]
root          94  0.0  0.0      0     0 ?        I<   07:23   0:00 [scsi_tmf_1]
root          96  0.0  0.0      0     0 ?        I<   07:23   0:00 [vfio-irqfd-clea]
root          97  0.0  0.0      0     0 ?        I<   07:23   0:00 [ipv6_addrconf]
root         106  0.0  0.0      0     0 ?        I<   07:23   0:00 [kworker/0:1H-kblockd]
root         107  0.0  0.0      0     0 ?        I<   07:23   0:00 [kstrp]
root         110  0.0  0.0      0     0 ?        I<   07:23   0:00 [kworker/u31:0]
root         123  0.0  0.0      0     0 ?        I<   07:23   0:00 [charger_manager]
root         157  0.0  0.0      0     0 ?        I<   07:23   0:00 [cryptd]
root         197  0.0  0.0      0     0 ?        I<   07:23   0:00 [kdmflush]
root         226  0.0  0.0      0     0 ?        I<   07:23   0:00 [raid5wq]
root         273  0.0  0.0      0     0 ?        S    07:23   0:00 [jbd2/dm-0-8]
root         274  0.0  0.0      0     0 ?        I<   07:23   0:00 [ext4-rsv-conver]
root         344  0.1  1.3  60316 13404 ?        S<s  07:23   0:01 /lib/systemd/systemd-journald
root         363  0.0  0.0      0     0 ?        I<   07:23   0:00 [ipmi-msghandler]
root         374  0.4  0.6  22728  6160 ?        Ss   07:23   0:03 /lib/systemd/systemd-udevd
root         482  0.0  0.0      0     0 ?        I<   07:24   0:00 [kaluad]
root         483  0.0  0.0      0     0 ?        I<   07:24   0:00 [kmpath_rdacd]
root         484  0.0  0.0      0     0 ?        I<   07:24   0:00 [kmpathd]
root         485  0.0  0.0      0     0 ?        I<   07:24   0:00 [kmpath_handlerd]
root         486  0.0  1.8 280196 17996 ?        SLsl 07:24   0:00 /sbin/multipathd -d -s
root         495  0.0  0.0      0     0 ?        S<   07:24   0:00 [loop0]
root         498  0.0  0.0      0     0 ?        S<   07:24   0:00 [loop1]
root         499  0.0  0.0      0     0 ?        S<   07:24   0:00 [loop2]
root         502  0.0  0.0      0     0 ?        S<   07:24   0:00 [loop3]
root         503  0.0  0.0      0     0 ?        S<   07:24   0:00 [loop4]
root         506  0.0  0.0      0     0 ?        S<   07:24   0:00 [loop5]
root         507  0.0  0.0      0     0 ?        S<   07:24   0:00 [loop6]
root         511  0.0  0.0      0     0 ?        S<   07:24   0:00 [loop7]
root         515  0.0  0.0      0     0 ?        S    07:24   0:00 [jbd2/xvda2-8]
root         516  0.0  0.0      0     0 ?        I<   07:24   0:00 [ext4-rsv-conver]
systemd+     531  0.0  0.6  90872  6108 ?        Ssl  07:24   0:00 /lib/systemd/systemd-timesyncd
systemd+     578  0.0  0.7  27256  7468 ?        Ss   07:24   0:00 /lib/systemd/systemd-networkd
systemd+     580  0.0  1.2  24532 12044 ?        Ss   07:24   0:00 /lib/systemd/systemd-resolved
root         593  0.0  0.9 239276  9176 ?        Ssl  07:24   0:00 /usr/lib/accountsservice/accounts-daemon
root         594  0.0  1.5 1232040 15784 ?       Ssl  07:24   0:00 /usr/bin/amazon-ssm-agent
root         598  0.0  0.2   6812  2840 ?        Ss   07:24   0:00 /usr/sbin/cron -f
message+     599  0.0  0.4   7568  4656 ?        Ss   07:24   0:00 /usr/bin/dbus-daemon --system --address=systemd: -
root         604  0.0  0.3   8480  3384 ?        S    07:24   0:00 /usr/sbin/CRON -f
bind         611  0.0  2.2 216200 22068 ?        Ssl  07:24   0:00 /usr/sbin/named -f -u bind
root         613  0.1  1.8  29656 18444 ?        Ss   07:24   0:01 /usr/bin/python3 /usr/bin/networkd-dispatcher --ru
root         614  0.0  1.0 238028 10564 ?        Ssl  07:24   0:00 /usr/lib/policykit-1/polkitd --no-debug
syslog       616  0.0  0.4 224492  4920 ?        Ssl  07:24   0:00 /usr/sbin/rsyslogd -n -iNONE
root         619  0.4  4.0 726824 40484 ?        Ssl  07:24   0:03 /usr/lib/snapd/snapd
root         622  0.0  0.7  17296  7836 ?        Ss   07:24   0:00 /lib/systemd/systemd-logind
root         624  0.0  1.3 395440 13560 ?        Ssl  07:24   0:00 /usr/lib/udisks2/udisksd
daemon       629  0.0  0.2   3792  2400 ?        Ss   07:24   0:00 /usr/sbin/atd -f
root         635  0.0  0.3   6808  3016 ?        Ss   07:24   0:00 /usr/sbin/vsftpd /etc/vsftpd.conf
Debian-+     646  0.0  1.0  20580 10708 ?        Ss   07:24   0:00 /usr/sbin/snmpd -LOw -u Debian-snmp -g Debian-snmp
randa        655  0.0  0.0   2608   532 ?        Ss   07:24   0:00 /bin/sh -c /home/randa/THM-24765.sh
randa        657  0.0  0.3   6892  3208 ?        S    07:24   0:00 /bin/bash /home/randa/THM-24765.sh
randa        658  0.0  0.0   5476   516 ?        S    07:24   0:00 sleep 10000
root         683  0.0  0.7  12172  6992 ?        Ss   07:24   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 sta
root         684  0.0  0.2   5600  2268 ttyS0    Ss+  07:24   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,
root         697  0.0  1.1 314452 11040 ?        Ssl  07:24   0:00 /usr/sbin/ModemManager
root         698  0.0  0.1   5828  1764 tty1     Ss+  07:24   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
irc          712  0.0  0.5   9012  5780 ?        Ss   07:24   0:00 /usr/sbin/inspircd --config=/etc/inspircd/inspircd
openldap     722  0.0  0.5 1159116 5440 ?        Ssl  07:24   0:00 /usr/sbin/slapd -h ldap:/// ldapi:/// -g openldap 
root         732  0.0  2.6 1318008 25948 ?       Sl   07:24   0:00 /usr/bin/ssm-agent-worker
root         770  0.1  2.0 107912 20820 ?        Ssl  07:24   0:01 /usr/bin/python3 /usr/share/unattended-upgrades/un
root         990  0.0  0.0      0     0 ?        I    07:31   0:00 [kworker/0:1-events]
root        1000  0.0  0.9  13924  9080 ?        Ss   07:36   0:00 sshd: user [priv]
user        1020  0.0  0.9  19048  9524 ?        Ss   07:36   0:00 /lib/systemd/systemd --user
root        1021  0.0  0.0      0     0 ?        I    07:36   0:00 [kworker/0:2]
user        1022  0.0  0.3 104072  3416 ?        S    07:36   0:00 (sd-pam)
user        1147  0.0  0.5  14056  5440 ?        S    07:36   0:00 sshd: user@pts/0
user        1148  0.0  0.5   8276  5108 pts/0    Ss   07:36   0:00 -bash
user        1174  0.0  0.3   9080  3572 pts/0    R+   07:38   0:00 ps -aux
root        1175  0.0  0.7  17080  7000 ?        Rs   07:38   0:00 /usr/bin/systemd-tmpfiles --clean
```
{: .nolineno }

Answer : THM-24765.sh

## TASK 4 : Windows Enumeration
### What is the full OS Name? 
On Windows we can look at the system informations with the "systeminfo" comand :

```
PS C:\Users\user> systeminfo

Host Name:                 RED-WIN-ENUM
OS Name:                   Microsoft Windows Server 2019 Datacenter
OS Version:                10.0.17763 N/A Build 17763
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          EC2
Registered Organization:   Amazon.com
Product ID:                00430-00000-00000-AA155
Original Install Date:     3/17/2021, 2:59:06 PM
System Boot Time:          8/21/2022, 7:55:30 AM
System Manufacturer:       Amazon EC2
System Model:              t3a.small
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: AMD64 Family 23 Model 1 Stepping 2 AuthenticAMD ~2200 Mhz 
BIOS Version:              Amazon EC2 1.0, 10/16/2017
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC) Coordinated Universal Time
Total Physical Memory:     2,016 MB
Available Physical Memory: 290 MB
Virtual Memory: Max Size:  2,400 MB
Virtual Memory: Available: 692 MB
Virtual Memory: In Use:    1,708 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 30 Hotfix(s) Installed.
                           [01]: KB5015731
                           [02]: KB4470502
                           [03]: KB4470788
                           [04]: KB4480056
                           [05]: KB4486153
                           [06]: KB4493510
                           [07]: KB4499728
                           [08]: KB4504369
                           [09]: KB4512577
                           [10]: KB4512937
                           [11]: KB4521862
                           [12]: KB4523204
                           [13]: KB4535680
                           [14]: KB4539571
                           [15]: KB4549947
                           [16]: KB4558997
                           [17]: KB4562562
                           [18]: KB4566424
                           [19]: KB4570332
                           [20]: KB4577586
                           [21]: KB4577667
                           [22]: KB4587735
                           [23]: KB4589208
                           [24]: KB4598480
                           [25]: KB4601393
                           [26]: KB5000859
                           [27]: KB5015811
                           [28]: KB5012675
                           [29]: KB5014031
                           [30]: KB5014797
Network Card(s):           1 NIC(s) Installed.
                           [01]: Amazon Elastic Network Adapter
                                 Connection Name: Ethernet 3
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.10.0.1
                                 IP address(es)
                                 [01]: 10.10.30.90
                                 [02]: fe80::f8e1:5707:ebfb:4783
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed. 
```
{: .nolineno }

Answer : Microsoft Windows Server 2019 Datacenter

### What is the OS Version?

From the systeminfo command above.

Answer : 10.0.17763

### How many hotfixes are installed on this MS Windows Server?

From the systeminfo command too.
Answer : 30

### What is the lowest TCP port number listening on the system?

We can use the same command as for linux to print out the listening connection :

```
PS C:\Users\user> netstat -ano -p TCP

Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:22             0.0.0.0:0              LISTENING       2148
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       856
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       972
  TCP    0.0.0.0:5357           0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:47001          0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:49664          0.0.0.0:0              LISTENING       496
  TCP    0.0.0.0:49665          0.0.0.0:0              LISTENING       340
  TCP    0.0.0.0:49666          0.0.0.0:0              LISTENING       964
  TCP    0.0.0.0:49667          0.0.0.0:0              LISTENING       1932
  TCP    0.0.0.0:49668          0.0.0.0:0              LISTENING       2104
  TCP    0.0.0.0:49670          0.0.0.0:0              LISTENING       608
  TCP    0.0.0.0:49675          0.0.0.0:0              LISTENING       628
  TCP    10.10.30.90:22         10.10.120.247:57640    ESTABLISHED     2148
  TCP    10.10.30.90:53         0.0.0.0:0              LISTENING       2104
  TCP    10.10.30.90:139        0.0.0.0:0              LISTENING       4
  TCP    127.0.0.1:53           0.0.0.0:0              LISTENING       2104
```
{: .nolineno }

Answer : 22

### What is the name of the program listening on that port?

From the netstat command we got the PID associated with this connection.

We can thus look at the PID 2148 :

```
PS C:\Users\user> ps | findstr "2148"
    121      12     1636       7628       0.03   2148   0 sshd
```
{: .nolineno }

This can aslo be found by checking the tasklit running : 

```
PS C:\Users\user> tasklist | findstr "2148"
sshd.exe                      2148 Services                   0      7,628 K
```
{: .nolineno }

Answer : sshd.exe

## TASK 5 : DNS, SMB, and SNMP
### Knowing that the domain name on the MS Windows Server of IP 10.10.30.90 is redteam.thm, use dig to carry out a domain transfer. What is the flag that you get in the records?
To answer this question, we need to request a domain transfer using the "dig" command :

```
root@ip-10-10-120-247:~# dig -t AXFR redteam.thm @10.10.30.90

; <<>> DiG 9.11.3-1ubuntu1.13-Ubuntu <<>> -t AXFR redteam.thm @10.10.30.90
;; global options: +cmd
redteam.thm.		3600	IN	SOA	red-win-enum. hostmaster. 5 900 600 86400 3600
redteam.thm.		3600	IN	NS	red-win-enum.
first.redteam.thm.	3600	IN	A	10.10.254.1
flag.redteam.thm.	3600	IN	TXT	"THM{DNS_ZONE}"
second.redteam.thm.	3600	IN	A	10.10.254.2
tryhackme.redteam.thm.	3600	IN	CNAME	tryhackme.com.
redteam.thm.		3600	IN	SOA	red-win-enum. hostmaster. 5 900 600 86400 3600
;; Query time: 9 msec
;; SERVER: 10.10.30.90#53(10.10.30.90)
;; WHEN: Sun Aug 21 09:31:17 BST 2022
;; XFR size: 7 records (messages 1, bytes 295)
```
{: .nolineno }

Answer : THM{DNS_ZONE}

### What is the name of the share available over SMB protocol and starts with THM?

We can list the share with the "net share" command :

```
PS C:\Users\user> net share

Share name   Resource                        Remark

-------------------------------------------------------------------------------
C$           C:\                             Default share
IPC$                                         Remote IPC
ADMIN$       C:\Windows                      Remote Admin
Internal     C:\Internal Files               Internal Documents
THM{829738}  C:\Users\user\Private           Enjoy SMB shares
Users        C:\Users
The command completed successfully.
```
{: .nolineno }

Answer : THM{829738}

### Knowing that the community string used by the SNMP service is public, use snmpcheck to collect information about the MS Windows Server of IP 10.10.30.90. What is the location specified?

We can query the SNM with the snmpcheck.rb script as follows and then open the file generated :

```
root@ip-10-10-120-247:/opt/snmpcheck# ./snmpcheck.rb 10.10.30.90 -c public > res.txt
root@ip-10-10-120-247:/opt/snmpcheck# nano res.txt 

snmpcheck.rb v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)

[+] Try to connect to 10.10.30.90:161 using SNMPv1 and community 'public'

[*] System information:

  Host IP address               : 10.10.30.90
  Hostname                      : RED-WIN-ENUM
  Description                   : Hardware: AMD64 Family 23 Model 1 Stepping 2 AT/AT COMPATIBLE - Software: Windows $
  Contact                       : TryHackMe
  Location                      : THM{SNMP_SERVICE}
  Uptime snmp                   : 00:44:53.68
  Uptime system                 : 00:44:39.20
  System date                   : 2022-8-21 08:40:23.8
  Domain                        : WORKGROUP

[*] User accounts:
[...]
```
{: .nolineno }

Answer : THM{SNMP_SERVICE}

## TASK 6 : More Tools for Windows
### What utility from Sysinternals Suite shows the logged-in users?
Answer : PsLoggedOn

## TASK 7 : Conclusion
### Congratulations on finishing this room. It is time to continue your journey with the next room in this module. 
No Answer.