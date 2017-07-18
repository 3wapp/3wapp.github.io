---
title: "ssrf"
date: 2016-01-25 16:23
---

# SSRF

## SSRF 概述

SSRF(Server-Side Request Forgery:服务器端请求伪造) 是一种由攻击者构造形成由服务端发起请求的一个安全漏洞。一般情况下，SSRF攻击的目标是从外网无法访问的内部系统。（正是因为它是由服务端发起的，所以它能够请求到与它相连而与外网隔离的内部系统）

SSRF 形成的原因大都是由于服务端提供了从其他服务器应用获取数据的功能且没有对目标地址做过滤与限制。比如从指定URL地址获取网页文本内容，加载指定地址的图片，下载等等。

* 攻击者利用ssrf可以实现的攻击主要有5种：

1.可以对外网、服务器所在内网、本地进行端口扫描，获取一些服务的banner信息;

2.攻击运行在内网或本地的应用程序（比如溢出）;

3.对内网web应用进行指纹识别，通过访问默认文件实现;

4.攻击内外网的web应用，主要是使用get参数就可以实现的攻击（比如struts2，sqli等）;

5.利用file协议读取本地文件等。

## SSRF 漏洞的寻找

* 1.web功能寻找

    + 分享：通过URL地址分享网页内容
    + 转码服务：通过URL地址把原地址的网页内容调优使其适合手机屏幕浏览
    + 线翻译：通过URL地址翻译对应文本的内容
    + 图片加载与下载：通过URL地址加载或下载图片
    + 图片、文章收藏功能
    + 未公开的api实现以及其他调用URL的功能

    详情参考：[SSRF漏洞的挖掘经验][1]

## 实例

* [SSRF攻击实例解析][2]


## common example

* get image and save

```
<?php
if (isset($_POST['url'])){
    $content = file_get_contents($_POST['url']);
    $filename = './images/'.rand().'img.jpg';
    file_put_contents($filename, $content);
    $img = "<img src=\"".$filename."\"/>";
}
echo $img;
```

* use curl

```
if (isset($_POST['link'])){                                                          
    $link = $_POST['link'];                                                          
    $filename = './images/'.rand().'.txt';                                                         
    $curlobj = curl_init($link);                                                                                                                
    $fp = fopen($filename, 'w');                                                     
    curl_setopt($curlobj, CURLOPT_FILE, $fp);   #output                                        
    curl_setopt($curlobj, CURLOPT_HEADER, 0);   #0:不显示响应头信息                                  
    curl_exec($curlobj);                                                             
    curl_close($curlobj);                                                            
    fclose($fp);                                                                     
    $fp = fopen($filename, 'r');                                                     
    $result = fread($fp, filesize($filename));                                       
    fclose($fp);                                                                     
    echo $result;                                                                    
} 
```

可以用来扫端口

* post: link=http:127.0.0.1:22/

output banner:

> SSH-2.0-OpenSSH_7.1p2 Debian-2 Protocol mismatch. 

* post: link=http:127.0.0.1:25/

error port ,output warning

> Warning: fread(): Length parameter must be greater than 0 in /var/www/ssrf.php on line 22

** 危害 **

* 扫描主机，端口

* 访问本地文件，或外网不可达的地址，内网弱口令多

** search ssrf **

* url key

```
share
wap
url
link
src
source
target
u
3g
display
sourceURI
imageURL
domain
```

** bypass **

* @

> http://abc@127.0.0.1

* add port

> http://127.0.0.1:8000

* short url

> http://dwz.cn//11SMa 

* 可以指向任意ip的域名:xip.io

```
10.0.0.1.xip.io         10.0.0.1
www.10.0.0.1.xip.io     10.0.0.1
mysite.10.0.0.1.xip.io  10.0.0.1 
```

* ip 地址进制转换

```
115.239.210.26 = 16373751032    #IPy.IP('115.239.210.26').int()
```
** http://www.baidu.com@10.10.10.10 与 http://10.10.10.10 请求是相同的

** 防御 **

* 过滤返回信息，验证远程服务器对请求的响应是比较容易的方法。如果web应用是去获取某一种类型的文件。那么在把返回结果展示给用户之前先验证返回的信息是否符合标准。

* 统一错误信息，避免用户可以根据错误信息来判断远端服务器的端口状态。

* 限制请求的端口为http常用的端口，比如，80,443,8080,8090。

* 黑名单内网ip。避免应用被用来获取获取内网数据，攻击内网。

* 禁用不需要的协议。仅仅允许http和https请求。可以防止类似于file:///,gopher://,ftp:// 等引起的问题。

[1]: https://sobug.com/article/detail/11
[2]: http://www.freebuf.com/articles/web/20407.html

