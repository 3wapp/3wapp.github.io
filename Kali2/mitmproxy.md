---
title: "MitmProxy"
date: 2016-03-08 16:45
---

## 0x01 mitmproxy

mitmproxy 是一个基于python的中间人代理的框架。

* install 

[官方安装文档][1]

注意:

[虚拟机安装lxml内存不够报错][2]

## 0x02 介绍

首次运行mitmproxy

```
$mitmproxy
```

会在当前用户目录下生成文件夹"~/.mitmproxy/"

```
$ cd ~/.mitmproxy/
$ ls
mitmproxy-ca-cert.cer   # 安卓上使用  
mitmproxy-ca-cert.pem   # 非windows平台使用
mitmproxy-dhparam.pem
mitmproxy-ca-cert.p12   # windows上使用  
mitmproxy-ca.pem        # 私钥

```

## 0x03 操作模式

* 常规代理 --default

常规代理模式是最简单的代理方式，可以访问HTTP网站，针对HTTPS网站，可以在客户端设备上通过浏览器打开 mitm.it 网页，安装符合客户端设备的证书，就可以访问HTTPS站点了。 

* 透明代理

在透明代理模式下，不需要任何客户端配置，流量是直接进入代理的网络层转发出去，代理设备不能改变客户端的任何请求。 

> 如果在mitmproxy代理设备之前有NAT(网络地址转换)设备，mitmproxy代理设备将无法识别目标地址，客户端需要进行相应配置， 参考 [夹杂NAT设备时客户端配置][3]

要达到透明代理的目的，需要两个额外的组件

1.重定向机制，透明地将一个到互联网的服务器的TCP连接重路由到一个监听中的代理服务器。通常用代理服务器在同一个主机上的防火墙来实现，比如linux下的iptables或OSX中的pf

2.获取原始目标地址，这由mitmproxy的一个模块完成

itable设置:

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```
命令：

```
mitmproxt -T --host
```

* 反向代理

反向代理模式下，客户端认为代理服务器就是它要访问的原始服务器，觉察不到代理服务器的存在。 

* 上游代理

上游代理模式可以将客户端所有的请求无条件的转发传输给上游的代理服务器


## 0x04 mitmproxy交互

[mitmproxy基本操作][4]

快捷键：

```
h: 左移
j: 上移
k: 下移
l: 右移
space: 向下翻页

q: quit

r: replay request
```

## 0x05 libmproxy

* HTTPRequest (libmproxy.models.HTTPRequest)

```
anticache:
        Modifies this request to remove headers that might produce a cached
        response. That is, we remove ETags and If-Modified-Since headers.

anticomp:
        Modifies this request to remove headers that will compress the
        resource's data.

body:None

constrain_encoding:
        Limits the permissible Accept-Encoding values, based on what we can
        decode appropriately.

content:
        The raw (encoded) HTTP message body

        See also: :py:attr:`text`

cookies:
        The request cookies.
        An empty :py:class:`ODict` object if the cookie monster ate them all.

copy:None

decode:
            Decodes body based on the current Content-Encoding header, then
            removes the header. If there is no Content-Encoding header, no
            action is taken.

            Returns:
                True, if decoding succeeded.
                False, otherwise.

encode:
            Encodes body with the encoding e, where e is "gzip", "deflate" or "identity".

            Returns:
                True, if decoding succeeded.
                False, otherwise.

first_line_format:
        HTTP request form as defined in `RFC7230 <https://tools.ietf.org/html/rfc7230#section-5.3>`_.

        origin-form and asterisk-form are subsumed as "relative".

form_in:None

form_out:None

from_state:None

get_cookies:None

get_decoded_content:
            Returns the decoded content based on the current Content-Encoding
            header.
            Doesn't change the message iteself or its headers.

get_form_multipart:None

get_form_urlencoded:None

get_path_components:None

get_query:None

get_state:None

headers:
        Message headers object

        Returns:
            netlib.http.Headers

host:
        Target host. This may be parsed from the raw request
        (e.g. from a ``GET http://example.com/ HTTP/1.1`` request line)
        or inferred from the proxy mode (e.g. an IP in transparent mode).

        Setting the host attribute also updates the host header, if present.

http_version:
        Version string, e.g. "HTTP/1.1"

method:
        HTTP request method, e.g. "GET".

multipart_form:
        The multipart form data as an :py:class:`ODict` object.
        None if there is no data or the content-type indicates non-form data.

path:
        HTTP request path, e.g. "/index.html".
        Guaranteed to start with a slash.

path_components:
        The URL's path components as a list of strings.
        Components are unquoted.

port:
        Target port

pretty_host:
        Similar to :py:attr:`host`, but using the Host headers as an additional preferred data source.
        This is useful in transparent mode where :py:attr:`host` is only an IP address,
        but may not reflect the actual destination as the Host header could be spoofed.

pretty_url:
        Like :py:attr:`url`, but using :py:attr:`pretty_host` instead of :py:attr:`host`.

query:
        The request query string as an :py:class:`ODict` object.
        None, if there is no query.

replace:
            Replaces a regular expression pattern with repl in the headers, the
            request path and the body of the request. Encoded content will be
            decoded before replacement, and re-encoded afterwards.

            Returns the number of replacements made.

scheme:
        HTTP request scheme, which should be "http" or "https".

set_cookies:None

set_form_urlencoded:None

set_path_components:None

set_query:None

set_state:None

text:
        The decoded HTTP message body.
        Decoded contents are not cached, so accessing this attribute repeatedly is relatively expensive.

        .. note::
            This is not implemented yet.

        See also: :py:attr:`content`, :py:class:`decoded`

timestamp_end:
        Last byte timestamp

timestamp_start:
        First byte timestamp

url:
        The URL string, constructed from the request's URL components

urlencoded_form:
        The URL-encoded form data as an :py:class:`ODict` object.
        None if there is no data or the content-type indicates non-form data.

wrap:None
```

## 0x06 demo

### 数据监听

抓取含 passwd 或 password 数据包，借鉴Mitmproxy官网代码。

```python
# -*- coding:utf-8 -*-

"""
author: janes
date:2016/03/08
"""

import logging

from libmproxy import controller
from libmproxy import proxy

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class StickyMaster(controller.Master):
    def __init__(self, server):
        controller.Master.__init__(self, server)

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def findword(self, request):
        """
        params:
            request: HTTPRequest object
        """
        words = ['passwd', 'password']

        content = request.content
        log.debug("content:{}".format(content))

        querylist = request.get_query()
        log.debug("query:{q}".format(q=querylist))

        # find in url
        for param in querylist:
            """
            param is a tuple(key, value)
            """
            if any([index != -1 for index in map(param[0].find, words)]):
                return 'GET'

        # find in content
        if any([index != -1 for index in map(content.find, words)]):
            return 'POST'

        return None

    def handle_request(self, flow):
        """
        params:
            flow: HTTPFlow object
        """
        request = flow.request

        flag = self.findword(request)

        if flag:
            record(request, flag)

        flow.reply()

    def handle_response(self, flow):
        flow.reply()

def record(request, flag):
    url = request.url
    log.info(url)
    if flag == "POST":
        content = request.content
        log.info(content)
    else:
        log.info(request.get_query())
        # params = {p[0]:p[1] for p in request.get_query()}


if __name__ == "__main__":
    config = proxy.ProxyConfig(port=8001)
    server = proxy.ProxyServer(config)
    master = StickyMaster(server)
    master.run()
```

终端运行：

```
$ python fetch_password.py

$ python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...

$ curl --proxy localhost:8008 -v http://localhost:8000/?password=123456

DEBUG:__main__:query:[('password', '123456')]
INFO:__main__:http://localhost:8000/?password=123456
INFO:__main__:[('password', '123456')]
```




[1]: http://docs.mitmproxy.org/en/stable/install.html
[2]: http://stackoverflow.com/questions/24455238/lxml-installation-error-ubuntu-14-04-internal-compiler-error
[3]: http://docs.mitmproxy.org/en/stable/models.html
[4]: https://greenrobot.me/devpost/how-to-debug-android-http-get-started/