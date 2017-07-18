---
title: "XHR"
date: 2016-03-21 11:44
---

## XMLHttpRequest

现在所有浏览器都支持XMLHttpRequest对象，(IE5,IE6使用ActiveObject)。

XMLHttpRequest用于在后台与服务器交换数据。

## 创建XHR对象

```
var xmlhttp = new XMLHttpRequest();
```

## XHR 请求

```
xmlhttp.open("GET", "file", true);
xmlhttp.send();

xmlhttp.open("POST", "ajax.html", true);
xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencode");
xmlhttp.send("name=janes&passwd=123456");
```

```
open(method, url, async)
    method: 请求的类型，GET or POST
    url: 文件在服务器的位置
    async:true(异步)， flasse(同步)
    
send(string)
    string: 仅用于POST请求

serRequestHeader(header,value)
    header:请求头名称
    value:请求头的值
```

注：

* POST vs GET

1.特定情况使用POST

```
无法使用缓存文件（更新服务器上的文件或数据库）
向服务器发送大量数据（POST没有数据量限制）
发送包含未知字符串的用户输入时
```

* open async

XHR对象用于AJAX的话，async必须设置为true, 

## 服务器响应

```
responseText
    获得字符串形式的响应数据
responseXML
    获得XML形式的响应数据
```

## onreadystatechange 事件

当请求被发送到服务器时，执行一些基于响应的任务

每当readyState 改变时，就会触发onreadystatechange事件

readyState属性存有XMLHttpRequest的状态信息

```
onreadystatechange
    存储函数或函数名，每当readyState属性改变时，就会调用该函数

readyState
    0: 请求未初始化
    1: 服务器连接已建立
    2: 请求已接收
    3: 请求处理中
    4: 请求已完成，且响应就绪

state
    200: OK
    404: not found
```