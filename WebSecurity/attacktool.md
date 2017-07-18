---
title: "AttackTool"
date: 2016-01-26 18:49
---

[2]: https://github.com/lijiejie/htpwdScan
[3]: http://drops.wooyun.org/tools/1548
[5]: http://www.openwall.com/php_mt_seed/
[6]: https://github.com/pwning/public-writeup/tree/master/hitcon2015/web300-giraffes-coffee
[7]: http://www.gat3way.eu/poc/wtrt/

## Nikto

Nikto Web Scanner is a Web server scanner that tests Web servers for dangerous files/CGIs, outdated server software and other problems.

# Brute Force

## 字典

```
metasploit  /usr/share/metasploit-framework/data/john/wordlists/password.lst
```

## php mt_rand seed crack

tool:

* [php_mt_seed][5]

样例:

[hitcon 2015 web300][6]

mt_rand rainbow:

[mt_rand rainbow][7]

## htpwdScan

[github htpwdScan][2]

* install

```
cd ~/ctf
git clone https://github.com/lijiejie/htpwdScan.git
cd htpwdScan
chmod u+x
sudo ln -s ~/ctf/htpwdScan/htpwdScan.py /usr/local/bin/htpwdscan    #cofirm htpwdScan.py begin with "#!/usr/bin/env python"
htpwdscan -h    # to run
```

* use

先用 -debug 查看 request and response， after confirming, then crack 

htpwdScan.py 默认使用 htpp post method， if use get, use -get

脚本会自动替换\r \n \t等空白字符
  
**http get crack**

```
htpwdscan -f http_get.txt -d username=top_shortlist_name.txt password=10k_most_common_passwd.txt -get -err="Username and/or password incorrect"
```

> http_get.txt -- use brupsuite get http request, save to file

```
GET /dvwa/vulnerabilities/brute/?Login=Login HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://localhost/dvwa/vulnerabilities/brute/
Cookie: security=low; PHPSESSID=ij8gd7u55olpvsd39r0ki35cb1
Connection: close
```

http proxy check

```
htpwdscan -u=http://www.baidu.com -get -proxylist=available.txt -checkproxy -suc="百度一下"

# or check by website that to crack
htpwdscan -f=post.txt -proxylist=proxies.txt -checkproxy -suc="用户名或密码错误" 
```

## webscarab

## CeWL - Custom Word List generator

# SQL

