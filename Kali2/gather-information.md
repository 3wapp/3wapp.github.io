---
title: "Gather Information"
date: 2016-04-26 17:32
---

## 参考

[Freebuf Kali Linux在渗透测试中信息收集][1]

## 一句话介绍

### 域名信息

```
whois     通过Whoist据库查询域名的注册信息，Whois数据库是提供域名的注册人信息，包括联系方式，管理员名字，管理员邮箱等等，其中也包括DNS服务器的信息.
host      简单的 dns 查询
nslookup
dig       dns 查询， 具有更灵活和清晰的显示信息
dnsenum   查询主机IP地址, 该域名的DNS服务器， 该域名的MX记录
dnsdict6
fierce
dMitry
```

### 域名信息

* nslookup
> 查询DNS的记录，查看域名解析是否正常

```
# 直接查询， 返回 A 记录
nslookup domain [dns-server]

nslookup -q=type domain [dns-server]
# type 类型
A 地址记录 --创建到IP地址的记录
AAAA 地址记录 
AFSDB Andrew文件系统数据库服务器记录 
ATMA ATM地址记录 
CNAME 别名记录 --别名记录，它允许将多个记录映射到同一台计算机
HINFO 硬件配置记录，包括CPU、操作系统信息 
ISDN 域名对应的ISDN号码 
MB 存放指定邮箱的服务器 
MG 邮件组记录 
MINFO 邮件组和邮箱的信息记录 
MR 改名的邮箱记录 
MX 邮件服务器记录 
NS 名字服务器记录 
PTR 反向记录 
RP 负责人记录 
RT 路由穿透记录 
SRV TCP服务器信息记录 
TXT 域名对应的文本信息 
X25 域名对应的X.25地址记录
```

若没指定dns-server，用系统默认的dns服务器
 


[2016 cctf dns 查询注入]
```
nslookup -q=txt "loli.club" ns.loli.club
```

[1]: http://www.freebuf.com/articles/system/58096.html
[2]: http://bobao.360.cn/ctf/detail/159.html