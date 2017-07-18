## http协议请求头格式

> 特别提醒：请求报头后面有一个“回车换行”，平常使用的时候容易忽然这一点造成问题。

```
{method} {path} {http_version}(CRLF)
{header_name}: {header_value}(CRLF)
...more header info(CRLF)
(CRLF)
{content}
```

* 格式中的变量说明

```
method: GET,POST,PUT,DELETE 等等
path: URL路径部分，如：/index.html
version：如：http/1.1
header_name: 如：Host
header_value: 如： www.eertime.com
```

## 常用请求头

* Accept

Accept请求报头域用于指定客户端接受哪些类型的信息。eg：Accept：image/gif，表明客户端希望接受GIF图象格式的资源；Accept：text/html，表明客户端希望接受html文本。

* Accept-Charset

Accept-Charset请求报头域用于指定客户端接受的字符集。eg：Accept-Charset:iso-8859-1,gb2312.

如果在请求消息中没有设置这个域，缺省是任何字符集都可以接受。

* Accept-Encoding

Accept-Encoding请求报头域类似于Accept，但是它是用于指定可接受的内容编码。eg：Accept-Encoding:gzip,deflate.

如果请求消息中没有设置这个域, 服务器假定客户端对各种内容编码都可以接受。

* Accept-Language

Accept-Language请求报头域类似于Accept，但是它是用于指定一种自然语言。eg：Accept-Language:zh-cn.如果请求消息中没有设置这个报头域，服务器假定客户端对各种语言都可以接受。

* Authorization

Authorization请求报头域主要用于证明客户端有权查看某个资源。当浏览器访问一个页面时，如果收到服务器的响应代码为401（未授权），可以发送一个包含Authorization请求报头域的请求，要求服务器对其进行验证。

* Connection

HTTP/1.1 applications that do not support persisitent connections MUST include the "close" connection option in every message

* Host（发送请求时，该报头域是必需的）

> HTTP/1.1协议中，客户端必须包含 Host 请求头

Host请求报头域主要用于指定被请求资源的Internet主机和端口号，它通常从HTTP URL中提取出来的.

eg：在浏览器中输入：http://www.eertime.com/index.html, 浏览器发送的请求消息中，就会包含Host请求报头域: Host：www.eertime.com, 此处使用缺省端口号80，若指定了端口号，则变成：Host：www.eertime.com:指定端口号

* User-Agent

User-Agent请求报头域允许客户端将它的操作系统、浏览器和其它属性告诉服务器。不过，这个报头域不是必需的，如果我们自己编写一个浏览器，不使用User-Agent请求报头域，那么服务器端就无法得知我们的信息了。

* Demo

```
GET /index.php HTTP/1.1\r\n
Host: www.eertime.com\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3\r\n
Accept-Encoding: gzip, deflate\r\n
Connection: keep-alive\r\n
Cache-Control: max-age=0\r\n
\r\n
```

## HTTP 内容协商

HTTP内容协商有两种机制，

一种是服务端把文档可用版本列表发给客户端让用户选，这可以使用 300 Multiple Choices 状态码来实现。这种方案有不少问题，首先多一次网络往返；其次服务端同一文档的某些版本可能是为拥有某些技术特征的客户端准备的，而普通用户不一定了解这些细节。举个例子，服务端通常可以将静态资源输出为压缩和未压缩两个版本，压缩版显然是为支持压缩的客户端而准备的，但如果让普通用户选，很可能选择错误的版本。

另一种是服务端根据客户端发送的请求头中某些字段自动发送最合适的版本。可以用于这个机制的请求头字段又分两种：内容协商专用字段（Accept 字段）、其他字段。

### Accept 字段

Accept 字段，详见下表：

请求头字段	| 说明	| 响应头字段
 --- | ---- | -----
Accept |	告知服务器发送何种媒体类型	| Content-Type
Accept-Language |	告知服务器发送何种语言	| Content-Language
Accept-Charset |	告知服务器发送何种字符集	| Content-Type
Accept-Encoding	| 告知服务器采用何种压缩方式	| Content-Encoding

例如客户端发送以下请求头：

```
Accept:*/*
Accept-Encoding:gzip,deflate,sdch
Accept-Language:zh-CN,en-US;q=0.8,en;q=0.6
```

表示它可以接受任何 MIME 类型的资源；支持采用 gzip、deflate 或 sdch 压缩过的资源；可以接受 zh-CN、en-US 和 en 三种语言，并且 zh-CN 的权重最高（q 取值 0 - 1，最高为 1，最低为 0，默认为 1），服务端应该优先返回语言等于 zh-CN 的版本。

浏览器的响应头可能是这样的：


Content-Type: text/javascript
Content-Encoding: gzip
表示这个文档确切的 MIME 类型是 text/javascript；文档内容进行了 gzip 压缩；响应头没有 Content-Language 字段，通常说明返回版本的语言正好是请求头 Accept-Language 中权重最高的那个。

若没输出 Content-Encoding 表明内容未经过压缩
