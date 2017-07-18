---
title: "configure"
date: 2016-05-12 10:49
---

## note

> php命令行执行和浏览器访问是不一样的，命令行执行可能出现某些函数不能使用，而通过浏览器访问是正常的

## configuration

```
php.ini
httpd.conf
.htaccess
ini_set()
```

## install pcntl

已经安装php的情况下，可以按如下方式安装 pcntl。

```
$sudo su
# apt-get install php-dev  
# tar -zxvf php-5.3.15.tar.gz  // 下载与你已安装的php对应的版本
# cd php-5.3.15/ext/pcntl/
# phpize && ./configure && make install
# echo "extension=pcntl.so" >> /etc/php.ini     //append to php.ini file
# service apache2 restart

checking if everything is ok.

# php -m | grep pcntl
pcntl
```