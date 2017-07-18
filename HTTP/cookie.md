---
title: "Cookie"
date: 2016-03-08 12:36
---

## Cookie 的格式

cookie是存储在浏览器中的字符串， 由键值对 key=value构成，键值对之间由一个##分号##和一个##空格##隔开。

## cookie 的属性选项

每个cookie都有一定的属性，如什么时候失效，要发送到哪个域名，哪个路径等等。这些属性是通过cookie选项来设置的，cookie选项包括：expires、domain、path、secure、HttpOnly。在设置任一个cookie时都可以设置相关的这些属性，当然也可以不设置，这时会使用这些属性的默认值。在设置这些属性时，属性之间由一个分号和一个空格隔开。代码示例如下：

```
"key=name; expires=Thu, 25 Feb 2016 04:18:00 GMT; domain=ppsc.sankuai.com; path=/; secure; HttpOnly"
```

* expires

expires选项用来设置“cookie 什么时间内有效”。expires其实是cookie失效日期，expires必须是 GMT 格式的时间

如expires=Thu, 25 Feb 2016 04:18:00 GMT表示cookie讲在2016年2月25日4:18分之后失效，对于失效的cookie浏览器会清空。

如果没有设置该选项，则默认有效期为session，即会话cookie。这种cookie在浏览器关闭后就没有了。

* domain 和 path

domain选项用来设置cookie该发到哪个域名，path选项用来设置cookie该发往哪个路径。如某个 cookie 设置为domain=ppsc.sankuai.com; path=/pub; ，表示：若请求的地址域名是“ppsc.sankuai.com”，路径是“/pub”或“/pub下的任一子目录”如/pub/example、/pub/example/doc时，浏览器才会将这个cookie自动添加到请求头部中。比如请求地址为http://ppsc.sankuai.com/pub时，该cookie会被发送，但请求地址为http://ppsc.sankuai.com/时，该cookie不会被发送。

如某个 cookie 设置为domain=sankuai.com; path=/; ，表示：若请求的地址域名是“sankuai.com”或其子域如“ ppsc.sankuai.com”、“dx.ppsc.sankuai.com”等，路径是“/”或其下的任一子目录如/pub/example、/pub/example/doc时，浏览器才会将这个cookie自动添加到请求头部中。

所以domain和path2个选项共同决定了cookie何时被浏览器自动添加到请求头部中发送出去。如果没有设置这两个选项，则会使用默认值。domain的默认值为设置该cookie的网页所在的域名，path默认值为设置该cookie的网页所在的目录。

* secure

secure选项用来设置cookie只在确保安全的请求中才会发送。当请求是HTTPS或者其他安全协议时，包含 secure 选项的 cookie 才能被发送至服务器。

默认情况下，cookie不会带secure选项(即为空)。所以默认情况下，不管是HTTPS协议还是HTTP协议的请求，cookie 都会被发送至服务端。但要注意一点，secure选项只是限定了在安全情况下才可以传输给服务端，但并不代表你不能看到这个 cookie。


这里有个坑需要注意下：

> 如果想在客户端即网页中通过 js 去设置secure类型的 cookie，必须保证网页是https协议的。在http协议的网页中是无法设置secure类型cookie的。

* httpOnly

这个选项用来设置cookie是否能通过 js 去访问。默认情况下，cookie不会带httpOnly选项(即为空)，所以默认情况下，客户端是可以通过js代码去访问（包括读取、修改、删除等）这个cookie的。当cookie带httpOnly选项时，客户端则无法通过js代码去访问（包括读取、修改、删除等）这个cookie。

另外要特别注意：

> 在客户端是不能通过js代码去设置一个httpOnly类型的cookie的，这种类型的cookie只能通过服务端来设置。


## 如何设置 cookie？

cookie既可以由服务端来设置，也可以由客户端来设置。

* 服务端设置 cookie

不管你是请求一个资源文件（如 html/js/css/图片），还是发送一个ajax请求，服务端都会返回response。而response header中有一项叫set-cookie，是服务端专门用来设置cookie的。

注意:

不能将多个cookie放在一个set-cookie字段中，set-cookie字段的值就是普通的字符串，每个cookie还设置了相关属性选项。

当你要想设置多个 cookie，需要添加同样多的set-Cookie字段。

服务端可以设置cookie 的所有选项：expires、domain、path、secure、HttpOnly

* 客户端设置 cookie

注意：

客户端可以设置cookie 的下列选项：expires、domain、path、secure（有条件：只有在https协议的网页中，客户端设置secure类型的 cookie 才能成功），但无法设置HttpOnly选项。

## 如何修改、删除

* 修改 cookie

要想修改一个cookie，只需要重新赋值就行，旧的值会被新的值覆盖。但要注意一点，在设置新cookie时，path/domain/secure/HttpOnly这几个选项一定要旧cookie 保持一样。否则不会修改旧值，而是添加了一个新的 cookie。

* 删除 cookie

删除一个cookie 也挺简单，也是重新赋值，只要将这个新cookie的expires 选项设置为一个过去的时间点就行了。但同样要注意，path/domain/secure/HttpOnly这几个选项一定要旧cookie 保持一样。

## cookie 编码

cookie其实是个字符串，但这个字符串中逗号、分号、空格被当做了特殊符号。所以当cookie的 key 和 value 中含有这3个特殊字符时，需要对其进行额外编码，一般会用escape进行编码，读取时用unescape进行解码

## 跨域请求中 cookie

默认情况下，在发生跨域时，cookie 作为一种 credential 信息是不会被传送到服务端的。必须要进行额外设置才可以


