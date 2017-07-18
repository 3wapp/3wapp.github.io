---
title: "phpmyadmin install and configure"
date: 2016-01-19 21:42
---

* 安装 phpmyadmin

```
sudo apt-get install phpmyadmin
```
安装过程中会出现配置信息

1. 服务器选择 apache2 
2. 配置 database for phpmyadmin, choose yes
3. input mysql password
4. input password for phpmyadmin, and confirm 

apache配置文件, 增加一个 alias

/etc/apache2/mods-enabled/alias.conf

文件增加

```
Alias /phpmyadmin /usr/share/phpmyadmin

<Directory /usr/share/phpmyadmin>
    Options FollowSymlinks
    DirectoryIndex index.php
    
    <IfModule mod_php5.c>
        AddType appliction/x-httpd-php .php
        
        php_flag magic_quotes_gpc Off
        php_flag track_vars On
        php_flag register_globals Off
        php_admin_flag allow_url_fopen Off
        php_value include_path .
        php_admin_value upload_tmp_dir /var/lib/phpmyadmin/tmp
        php_admin_value open_basedir /usr/share/phpmyadmin/:/etc/phpmyadmin/:/var/lib/phpmyadmin/:/usr/share/php/php-gettext/
    </IfModule>
</Directory>
```

* 访问phpmyadmin

```
http://127.0.0.1/phpmyadmin
```

用户名密码为 mysql 的用户名和密码
