---
title: "Proxy"
date: 2016-03-08 12:58
---

## HTTP 代理

HTTP 代理是位于服务端和客户端之间的中间实体，在各个端点之间来回传送HTTP报文

按照用途分为：

* 内容过滤
* 科学上网
* Web缓存。维护服务器常用文档的一个副本，增加客户端的访问速度
* 反向代理。反向代理可以接收发给服务器的真实请求，然后按需交给真实的服务器，类似路由的功能

按照代理对客户端的可见性分为：

* 透明代理
* 非透明代理

## 连接代理为何要用绝对路径

早期的 HTTP 设计中，客户端只会与单个服务器进行通信，所以一旦 TCP 连接建立起来以后，只需要相对路径。

但代理就有问题，客户端首先和代理建立 TCP 连接，但由于传递的请求头中使用相对路径，代理就不知道使用什么 IP 和 端口来向远端的服务器建立 TCP 连接。所以，对于早期的 HTTP 1.0，强制客户端发给代理时使用完整路径，如

```
GET http://www.douban.com/ HTTP /1.0
```

较新的 HTTP 1.1 则规定了必须包含 Host 头部。所以对于 HTTP 1.1 的代理来说，完整 URL 不是必须的。但由于网络上还有大量旧版代理，Host 头部代理或许根本不识别，所以现在浏览器在使用代理时，还是会使用完整 URL

测试如下

```
[1]:
$nc -lvp 8000
$curl l0calhost:8000

nc >>>
listening on [any] 8000 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 34456
GET / HTTP/1.1
Host: localhost:8000
User-Agent: curl/7.47.0
Accept: */*


[2]:
$ nc -lvp 8088
$curl --proxy localhost:8088 l0calhost:8000

nc >>>
listening on [any] 8088 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 47468
GET http://localhost:8000/ HTTP/1.1
Host: localhost:8000
User-Agent: curl/7.47.0
Accept: */*
Proxy-Connection: Keep-Alive
```

比较会发现

> 向代理发送完整的绝对路径 URL。而在普通情况下只会发送相对路径，不需要主机名。

> 用 Proxy-Connection 头部代替 Connection 头部发送给代理服务器

## 为什么要用 Proxy-Connection 头部

Connection 头部是为了减少建立 TCP 连接的次数，复用连接产生的。默认 HTTP 1.1 是 Keepalive，但 1.0 的代理则不识别此头部。对于不认识的头部，代理会直接转发，以保持向后兼容性。

假如 Connection: Keep-alive 发给了代理，代理不识别转发给了服务器，而恰巧服务器识别此头部，便会出现严重问题。服务器和浏览器都保持连接，而代理则中断了连接。

为解决这个问题，出现了一个新的头部 Proxy-Connection。如果 1.1 的代理，代理会改写为 Connection 头部。如果 1.0 的代理，那么会直接转发此头部，服务器发现 Proxy-Connection 后，就会采用非长连接的方式。

## 服务器不一定支持绝对路径的URL

当客户端比如浏览器认为自己在向一个代理服务器发送HTTP请求时，会在请求行中使用绝对路径的URL，如果它认为自己在向目标服务器直接发送请求时，则请求行中只会包含相对路径的URL（完整URL的path部分）。

这是遵循了[RFC2616(5.1.2小节)][1]标准的规定。遵照标准，服务器必须能正确解析这两种形式的请求行，但是有些服务器不能正确解析请求行中包含绝对路径的情况，会返回HTTP/4XX或者HTTP/5XX错误

[1]: http://www.ieff.org/rfc/rfc2616.txt