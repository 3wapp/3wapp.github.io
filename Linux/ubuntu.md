---
title: "Ubuntu"
date: 2016-01-27 21:54
---

# ubuntu

## 修改时区

`cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`

修改为中国时区, 即时生效

## lamp

首先切换到root下

1.安装mysql5

```
apt-get install mysql-server mysql-client
```

然后在红色区域设置密码

2.安装apache2

```
apt-get install apache2
```

现在,输入localhost,你应该看到apache2的测试页:

3.安装php5

```
apt-get install php5 libapache2-mod-php5
```

然后重启

```
/etc/init.d/apache2 restart
```

4.进行测试

当然，因为就算是root权限，但是www目录默认的权限不足，依然写不进去，所以自己chmod改下吧，创建1.php

```
<?php
echo '123';
?>
```

出现123就成功

5.当然这还不够，php获得MySQL支持

```
apt-get install php5-mysql php5-curl php5-gd php5-idn php-pear php5-imagick php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode php5-snmp php5-sqlite php5-tidy php5-xmlrpc php5-xsl
```

重新启动apache:

```
/etc/init.d/apache2 restart
```

6.安装phpmyadmin

```
apt-get install phpmyadmin
```

然后将创建一个链接 ：

```
ln -l /usr/share/phpmyadmin /var/www
```

OK了。

7.最后修改一下根目录

```
/etc/apache2/apache2.conf
/etc/apache2/sites-available/000-default.conf
```

根据自己的需要改下即可。

```
/etc/init.d/apache2 restart
```

OK

