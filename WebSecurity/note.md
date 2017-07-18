---
title: "Note"
date: 2016-01-26 18:49
---


[win10 ubuntu双系统][1]

[1]: http://support.lenovo.com.cn/lenovo/wsi/htmls/detail_20151111145810868.html

## web服务器

WEB服务器一个奇怪的特性，就是如果没有返回响应而WEB服务器又接受了请求，那么请求的内容将原封不动的写入WEB日志，不会进行HTTP编码

## URL shortening

URL shortening，即短地址，把URL变短，服务器通过查询短地址，提供302跳转到目的地址。

长短地址之间映射的方法有很多：MD5抽样，唯一ID+BASE62。

+ 唯一ID+BASE62

Python有现成类库两枚，short_url (不带DB，只有ID<->base62，有生成最小位数参数，DB自选，一般选择NoSQL)，
另一个是shorten (可存储到redis或Memory)。

## common port

21,22,23,25,53,79,80,81,82,83,84,85,110,111,119,135,139,143,443,445,465,512,513,514,554,563,585,636,808,873,990,995,1025,1027,1080,1352,1433,1521,1525,1900,1935,2049,2100,2121,2401,3128,3306,3389,4443,4899,5000,5432,5556,5560,5631,5800,5900,5901,6000,6009,7001,7778,8000,8009,8080,8081,8082,8083,8084,8085,8090,8091,8092,8181,8455,8888,8989,9060,9080,9090,9443,28017,50000,65301

## 提权

* win

```
new user <Username> <Password> /add
cd C:\WINNT\SYSTEM32\
net localgroup administrators <Username> /ad
```

## 系统常见敏感信息漏洞

## win32 + apache

短文件名漏洞

## cookie欺骗漏洞

## binwalk

参数：

* -e

提取文件

* if=输入文件

* of=输出文件

* skip=<跳过的字节数>

* count=<要提取的字节数>

## PHP审计工具 RIPS

[download and install][5]

[5]: http://rips-scanner.sourceforge.net/ 