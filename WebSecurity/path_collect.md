---
title: "文件读取漏洞路径收集"
date: 2016-05-12 15:37
---

代码在做渗透测试当中会在某些情况可以读取系统文件，例如MySQL注入当中利用load_file函数读取系统文件

这里收集一下服务器通常存在的文件，可以通过读取相关敏感文件达到快速获取信息的目的。

```
/etc/passwd
/etc/shadow
/etc/issue
/etc/fstab
/etc/host.conf
/etc/motd
/etc/ld.so.conf
/etc/sysconfig/network-scripts/ifcfg-eth0
/etc/sysconfig/network-scripts/ifcfg-eth1
/var/www/htdocs/index.php
/var/www/conf/httpd.conf
/var/www/htdocs/index.html
/var/httpd/conf/php.ini
/var/httpd/htdocs/index.php
/var/httpd/conf/httpd.conf
/var/httpd/htdocs/index.html
/var/httpd/conf/php.ini
/var/www/index.html
/var/www/index.php
/opt/www/conf/httpd.conf
/opt/www/htdocs/index.php
/opt/www/htdocs/index.html
/usr/local/apache/htdocs/index.html
/usr/local/apache/htdocs/index.php
/usr/local/apache2/htdocs/index.html
/usr/local/apache2/htdocs/index.php
/usr/local/httpd2.2/htdocs/index.php
/usr/local/httpd2.2/htdocs/index.html
/tmp/apache/htdocs/index.html
/tmp/apache/htdocs/index.php
/etc/httpd/htdocs/index.php
/etc/httpd/conf/httpd.conf
/etc/httpd/htdocs/index.html
/www/php/php.ini
/www/php4/php.ini
/www/php5/php.ini
/www/conf/httpd.conf
/www/htdocs/index.php
/www/htdocs/index.html

/usr/local/httpd/conf/httpd.conf
/apache/apache/conf/httpd.conf
/apache/apache2/conf/httpd.conf
/etc/apache/apache.conf
/etc/apache2/apache.conf
/etc/apache/httpd.conf
/etc/apache2/httpd.conf
/etc/apache2/vhosts.d/00_default_vhost.conf
/etc/apache2/sites-available/default

/etc/phpmyadmin/config.inc.php
/etc/mysql/my.cnf
/etc/httpd/conf.d/php.conf
/etc/httpd/conf.d/httpd.conf

/etc/httpd/logs/error_log
/etc/httpd/logs/error.log
/etc/httpd/logs/access_log
/etc/httpd/logs/access.log
/home/apache/conf/httpd.conf
/home/apache2/conf/httpd.conf

/var/log/apache/error_log
/var/log/apache/error.log
/var/log/apache/access_log
/var/log/apache/access.log
/var/log/apache2/error_log
/var/log/apache2/error.log
/var/log/apache2/access_log
/var/log/apache2/access.log
/var/www/logs/error_log
/var/www/logs/error.log
/var/www/logs/access_log
/var/www/logs/access.log
/usr/local/apache/logs/error_log
/usr/local/apache/logs/error.log
/usr/local/apache/logs/access_log
/usr/local/apache/logs/access.log

/var/log/error_log
/var/log/error.log
/var/log/access_log
/var/log/access.log

/usr/local/apache/logs/access_logaccess_log.old
/usr/local/apache/logs/error_logerror_log.old

/etc/php.ini
/bin/php.ini
/etc/init.d/httpd
/etc/init.d/mysql

/etc/httpd/php.ini
/usr/lib/php.ini
/usr/lib/php/php.ini
/usr/local/etc/php.ini
/usr/local/lib/php.ini
/usr/local/php/lib/php.ini
/usr/local/php4/lib/php.ini
/usr/local/php4/php.ini
/usr/local/php4/lib/php.ini
/usr/local/php5/lib/php.ini
/usr/local/php5/etc/php.ini
/usr/local/php5/php5.ini
/usr/local/apache/conf/php.ini

/usr/local/apache/conf/httpd.conf
/usr/local/apache2/conf/httpd.conf

/usr/local/apache2/conf/php.ini
/etc/php4.4/fcgi/php.ini
/etc/php4/apache/php.ini
/etc/php4/apache2/php.ini
/etc/php5/apache/php.ini
/etc/php5/apache2/php.ini
/etc/php/php.ini
/etc/php/php4/php.ini
/etc/php/apache/php.ini
/etc/php/apache2/php.ini
/web/conf/php.ini
/usr/local/Zend/etc/php.ini
/opt/xampp/etc/php.ini
/var/local/www/conf/php.ini
/var/local/www/conf/httpd.conf
/etc/php/cgi/php.ini
/etc/php4/cgi/php.ini
/etc/php5/cgi/php.ini

/php5/php.ini
/php4/php.ini
/php/php.ini
/PHP/php.ini

/apache/php/php.ini

/xampp/apache/bin/php.ini
/xampp/apache/conf/httpd.conf
/NetServer/bin/stable/apache/php.ini
/home2/bin/stable/apache/php.ini

/home/bin/stable/apache/php.ini

/var/log/mysql/mysql-bin.log
/var/log/mysql.log
/var/log/mysqlderror.log
/var/log/mysql/mysql.log
/var/log/mysql/mysql-slow.log
/var/mysql.log

/var/lib/mysql/my.cnf
/usr/local/mysql/my.cnf
/usr/local/mysql/bin/mysql
/etc/mysql/my.cnf
/etc/my.cnf

/usr/local/cpanel/logs
/usr/local/cpanel/logs/stats_log
/usr/local/cpanel/logs/access_log
/usr/local/cpanel/logs/error_log
/usr/local/cpanel/logs/license_log
/usr/local/cpanel/logs/login_log
/usr/local/cpanel/logs/stats_log
/usr/local/share/examples/php4/php.ini
/usr/local/share/examples/php/php.ini
```

## history

```
~/.bash_history

~/.mysql_history
```

## nginx

```
/etc/nginx/nginx.conf

/var/log/nginx/error.log
/var/log/nginx/nginx_error.log
/usr/local/nginx/logs/error.log
/var/log/nginx/access.log


```

## LINUX常见路径：

```
/etc/passwd
/etc/shadow
/etc/fstab
/etc/host.conf
/etc/motd
/etc/ld.so.conf
/var/www/htdocs/index.php
/var/www/conf/httpd.conf
/var/www/htdocs/index.html
/var/httpd/conf/php.ini
/var/httpd/htdocs/index.php
/var/httpd/conf/httpd.conf
/var/httpd/htdocs/index.html
/var/httpd/conf/php.ini
/var/www/index.html
/var/www/index.php
/opt/www/conf/httpd.conf
/opt/www/htdocs/index.php
/opt/www/htdocs/index.html
/usr/local/apache/htdocs/index.html
/usr/local/apache/htdocs/index.php
/usr/local/apache2/htdocs/index.html
/usr/local/apache2/htdocs/index.php
/usr/local/httpd2.2/htdocs/index.php
/usr/local/httpd2.2/htdocs/index.html
/tmp/apache/htdocs/index.html
/tmp/apache/htdocs/index.php
/etc/httpd/htdocs/index.php
/etc/httpd/conf/httpd.conf
/etc/httpd/htdocs/index.html
/www/php/php.ini
/www/php4/php.ini
/www/php5/php.ini
/www/conf/httpd.conf
/www/htdocs/index.php
/www/htdocs/index.html
/usr/local/httpd/conf/httpd.conf
/apache/apache/conf/httpd.conf
/apache/apache2/conf/httpd.conf
/etc/apache/apache.conf
/etc/apache2/apache.conf
/etc/apache/httpd.conf
/etc/apache2/httpd.conf
/etc/apache2/vhosts.d/00_default_vhost.conf
/etc/apache2/sites-available/default
/etc/phpmyadmin/config.inc.php
/etc/mysql/my.cnf
/etc/httpd/conf.d/php.conf
/etc/httpd/conf.d/httpd.conf
/etc/httpd/logs/error_log
/etc/httpd/logs/error.log
/etc/httpd/logs/access_log
/etc/httpd/logs/access.log
/home/apache/conf/httpd.conf
/home/apache2/conf/httpd.conf
/var/log/apache/error_log
/var/log/apache/error.log
/var/log/apache/access_log
/var/log/apache/access.log
/var/log/apache2/error_log
/var/log/apache2/error.log
/var/log/apache2/access_log
/var/log/apache2/access.log
/var/www/logs/error_log
/var/www/logs/error.log
/var/www/logs/access_log
/var/www/logs/access.log
/usr/local/apache/logs/error_log
/usr/local/apache/logs/error.log
/usr/local/apache/logs/access_log
/usr/local/apache/logs/access.log
/var/log/error_log
/var/log/error.log
/var/log/access_log
/var/log/access.log
/usr/local/apache/logs/access_logaccess_log.old
/usr/local/apache/logs/error_logerror_log.old
/etc/php.ini
/bin/php.ini
/etc/init.d/httpd
/etc/init.d/mysql
/etc/httpd/php.ini
/usr/lib/php.ini
/usr/lib/php/php.ini
/usr/local/etc/php.ini
/usr/local/lib/php.ini
/usr/local/php/lib/php.ini
/usr/local/php4/lib/php.ini
/usr/local/php4/php.ini
/usr/local/php4/lib/php.ini
/usr/local/php5/lib/php.ini
/usr/local/php5/etc/php.ini
/usr/local/php5/php5.ini
/usr/local/apache/conf/php.ini
/usr/local/apache/conf/httpd.conf
/usr/local/apache2/conf/httpd.conf
/usr/local/apache2/conf/php.ini
/etc/php4.4/fcgi/php.ini
/etc/php4/apache/php.ini
/etc/php4/apache2/php.ini
/etc/php5/apache/php.ini
/etc/php5/apache2/php.ini
/etc/php/php.ini
/etc/php/php4/php.ini
/etc/php/apache/php.ini
/etc/php/apache2/php.ini
/web/conf/php.ini
/usr/local/Zend/etc/php.ini
/opt/xampp/etc/php.ini
/var/local/www/conf/php.ini
/var/local/www/conf/httpd.conf
/etc/php/cgi/php.ini
/etc/php4/cgi/php.ini
/etc/php5/cgi/php.ini
/php5/php.ini
/php4/php.ini
/php/php.ini
/PHP/php.ini
/apache/php/php.ini
/xampp/apache/bin/php.ini
/xampp/apache/conf/httpd.conf
/NetServer/bin/stable/apache/php.ini
/home2/bin/stable/apache/php.ini
/home/bin/stable/apache/php.ini
/var/log/mysql/mysql-bin.log
/var/log/mysql.log
/var/log/mysqlderror.log
/var/log/mysql/mysql.log
/var/log/mysql/mysql-slow.log
/var/mysql.log
/var/lib/mysql/my.cnf
/usr/local/mysql/my.cnf
/usr/local/mysql/bin/mysql
/etc/mysql/my.cnf
/etc/my.cnf
/usr/local/cpanel/logs
/usr/local/cpanel/logs/stats_log
/usr/local/cpanel/logs/access_log
/usr/local/cpanel/logs/error_log
/usr/local/cpanel/logs/license_log
/usr/local/cpanel/logs/login_log
/usr/local/cpanel/logs/stats_log
/usr/local/share/examples/php4/php.ini
/usr/local/share/examples/php/php.ini
```

## windows常见路径（可以将c盘换成d,e盘）

```
c:\windows\php.ini
c:\boot.ini
c:\1.txt
c:\a.txt

c:\CMailServer\config.ini
c:\CMailServer\CMailServer.exe
c:\CMailServer\WebMail\index.asp
c:\program files\CMailServer\CMailServer.exe
c:\program files\CMailServer\WebMail\index.asp
C:\WinWebMail\SysInfo.ini
C:\WinWebMail\Web\default.asp
C:\WINDOWS\FreeHost32.dll
C:\WINDOWS\7i24iislog4.exe
C:\WINDOWS\7i24tool.exe

c:\hzhost\databases\url.asp

c:\hzhost\hzclient.exe
C:\Documents and Settings\All Users\「开始」菜单\程序\7i24虚拟主机管理平台\自动设置[受控端].lnk

C:\Documents and Settings\All Users\「开始」菜单\程序\Serv-U\Serv-U Administrator.lnk
C:\WINDOWS\web.config
c:\web\index.html
c:\www\index.html
c:\WWWROOT\index.html
c:\website\index.html
c:\web\index.asp
c:\www\index.asp
c:\wwwsite\index.asp
c:\WWWROOT\index.asp
c:\web\index.php
c:\www\index.php
c:\WWWROOT\index.php
c:\WWWsite\index.php
c:\web\default.html
c:\www\default.html
c:\WWWROOT\default.html
c:\website\default.html
c:\web\default.asp
c:\www\default.asp
c:\wwwsite\default.asp
c:\WWWROOT\default.asp
c:\web\default.php
c:\www\default.php
c:\WWWROOT\default.php
c:\WWWsite\default.php
C:\Inetpub\wwwroot\pagerror.gif
c:\windows\notepad.exe
c:\winnt\notepad.exe
C:\Program Files\Microsoft Office\OFFICE10\winword.exe
C:\Program Files\Microsoft Office\OFFICE11\winword.exe
C:\Program Files\Microsoft Office\OFFICE12\winword.exe
C:\Program Files\Internet Explorer\IEXPLORE.EXE
C:\Program Files\winrar\rar.exe
C:\Program Files\360\360Safe\360safe.exe
C:\Program Files\360Safe\360safe.exe
C:\Documents and Settings\Administrator\Application Data\360Safe\360Examine\360Examine.log
c:\ravbin\store.ini
c:\rising.ini
C:\Program Files\Rising\Rav\RsTask.xml
C:\Documents and Settings\All Users\Start Menu\desktop.ini
C:\Documents and Settings\Administrator\My Documents\Default.rdp
C:\Documents and Settings\Administrator\Cookies\index.dat
C:\Documents and Settings\Administrator\My Documents\新建 文本文档.txt
C:\Documents and Settings\Administrator\桌面\新建 文本文档.txt
C:\Documents and Settings\Administrator\My Documents\1.txt
C:\Documents and Settings\Administrator\桌面\1.txt
C:\Documents and Settings\Administrator\My Documents\a.txt
C:\Documents and Settings\Administrator\桌面\a.txt
C:\Documents and Settings\All Users\Documents\My Pictures\Sample Pictures\Blue hills.jpg
E:\Inetpub\wwwroot\aspnet_client\system_web\1_1_4322\SmartNav.htm
C:\Program Files\RhinoSoft.com\Serv-U\Version.txt
C:\Program Files\RhinoSoft.com\Serv-U\ServUDaemon.ini
C:\Program Files\Symantec\SYMEVENT.INF
C:\Program Files\Microsoft SQL Server\80\Tools\Binn\sqlmangr.exe
C:\Program Files\Microsoft SQL Server\MSSQL\Data\master.mdf
C:\Program Files\Microsoft SQL Server\MSSQL.1\MSSQL\Data\master.mdf
C:\Program Files\Microsoft SQL Server\MSSQL.2\MSSQL\Data\master.mdf
C:\Program Files\Microsoft SQL Server\80\Tools\HTML\database.htm
C:\Program Files\Microsoft SQL Server\MSSQL\README.TXT
C:\Program Files\Microsoft SQL Server\90\Tools\Bin\DdsShapes.dll
C:\Program Files\Microsoft SQL Server\MSSQL\sqlsunin.ini
C:\MySQL\MySQL Server 5.0\my.ini
C:\Program Files\MySQL\MySQL Server 5.0\my.ini
C:\Program Files\MySQL\MySQL Server 5.0\data\mysql\user.frm
C:\Program Files\MySQL\MySQL Server 5.0\COPYING
C:\Program Files\MySQL\MySQL Server 5.0\share\mysql_fix_privilege_tables.sql
C:\Program Files\MySQL\MySQL Server 4.1\bin\mysql.exe
c:\MySQL\MySQL Server 4.1\bin\mysql.exe
c:\MySQL\MySQL Server 4.1\data\mysql\user.frm
C:\Program Files\Oracle\oraconfig\Lpk.dll
C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\aspnet_state.exe
C:\WINDOWS\system32\inetsrv\w3wp.exe
C:\WINDOWS\system32\inetsrv\inetinfo.exe
C:\WINDOWS\system32\inetsrv\MetaBase.xml
C:\WINDOWS\system32\inetsrv\iisadmpwd\achg.asp
C:\WINDOWS\system32\config\default.LOG
C:\WINDOWS\system32\config\sam
C:\WINDOWS\system32\config\system
c:\CMailServer\config.ini
c:\program files\CMailServer\config.ini
c:\tomcat6\tomcat6\bin\version.sh
c:\tomcat6\bin\version.sh
c:\tomcat\bin\version.sh
c:\program files\tomcat6\bin\version.sh
C:\Program Files\Apache Software Foundation\Tomcat 6.0\bin\version.sh
c:\Program Files\Apache Software Foundation\Tomcat 6.0\logs\isapi_redirect.log
c:\Apache2\Apache2\bin\Apache.exe
c:\Apache2\bin\Apache.exe
c:\Apache2\php\license.txt
C:\Program Files\Apache Group\Apache2\bin\Apache.exe
/usr/local/tomcat5527/bin/version.sh
/usr/share/tomcat6/bin/startup.sh
/usr/tomcat6/bin/startup.sh
c:\Program Files\QQ2007\qq.exe
c:\Program Files\Tencent\qq\User.db
c:\Program Files\Tencent\qq\qq.exe
c:\Program Files\Tencent\qq\bin\qq.exe
c:\Program Files\Tencent\qq2009\qq.exe
c:\Program Files\Tencent\qq2008\qq.exe
c:\Program Files\Tencent\qq2010\bin\qq.exe
c:\Program Files\Tencent\qq\Users\All Users\Registry.db
C:\Program Files\Tencent\TM\TMDlls\QQZip.dll
c:\Program Files\Tencent\Tm\Bin\Txplatform.exe
c:\Program Files\Tencent\RTXServer\AppConfig.xml
C:\Program Files\Foxmal\Foxmail.exe
C:\Program Files\Foxmal\accounts.cfg
C:\Program Files\tencent\Foxmal\Foxmail.exe
C:\Program Files\tencent\Foxmal\accounts.cfg
C:\Program Files\LeapFTP 3.0\LeapFTP.exe
C:\Program Files\LeapFTP\LeapFTP.exe
c:\Program Files\GlobalSCAPE\CuteFTP Pro\cftppro.exe
c:\Program Files\GlobalSCAPE\CuteFTP Pro\notes.txt
C:\Program Files\FlashFXP\FlashFXP.ini
C:\Program Files\FlashFXP\flashfxp.exe
c:\Program Files\Oracle\bin\regsvr32.exe
c:\Program Files\腾讯游戏\QQGAME\readme.txt
c:\Program Files\tencent\腾讯游戏\QQGAME\readme.txt
c:\Program Files\tencent\QQGAME\readme.txt
C:\Program Files\StormII\Storm.exe
3.网站相对路径:

/config.php
../../config.php
../config.php
../../../config.php
/config.inc.php
./config.inc.php
../../config.inc.php
../config.inc.php
../../../config.inc.php
/conn.php
./conn.php
../../conn.php
../conn.php
../../../conn.php
/conn.asp
./conn.asp
../../conn.asp
../conn.asp
../../../conn.asp
/config.inc.php
./config.inc.php
../../config.inc.php
../config.inc.php
../../../config.inc.php
/config/config.php
../../config/config.php
../config/config.php
../../../config/config.php
/config/config.inc.php
./config/config.inc.php
../../config/config.inc.php
../config/config.inc.php
../../../config/config.inc.php
/config/conn.php
./config/conn.php
../../config/conn.php
../config/conn.php
../../../config/conn.php
/config/conn.asp
./config/conn.asp
../../config/conn.asp
../config/conn.asp
../../../config/conn.asp
/config/config.inc.php
./config/config.inc.php
../../config/config.inc.php
../config/config.inc.php
../../../config/config.inc.php
/data/config.php
../../data/config.php
../data/config.php
../../../data/config.php
/data/config.inc.php
./data/config.inc.php
../../data/config.inc.php
../data/config.inc.php
../../../data/config.inc.php
/data/conn.php
./data/conn.php
../../data/conn.php
../data/conn.php
../../../data/conn.php
/data/conn.asp
./data/conn.asp
../../data/conn.asp
../data/conn.asp
../../../data/conn.asp
/data/config.inc.php
./data/config.inc.php
../../data/config.inc.php
../data/config.inc.php
../../../data/config.inc.php
/include/config.php
../../include/config.php
../include/config.php
../../../include/config.php
/include/config.inc.php
./include/config.inc.php
../../include/config.inc.php
../include/config.inc.php
../../../include/config.inc.php
/include/conn.php
./include/conn.php
../../include/conn.php
../include/conn.php
../../../include/conn.php
/include/conn.asp
./include/conn.asp
../../include/conn.asp
../include/conn.asp
../../../include/conn.asp
/include/config.inc.php
./include/config.inc.php
../../include/config.inc.php
../include/config.inc.php
../../../include/config.inc.php
/inc/config.php
../../inc/config.php
../inc/config.php
../../../inc/config.php
/inc/config.inc.php
./inc/config.inc.php
../../inc/config.inc.php
../inc/config.inc.php
../../../inc/config.inc.php
/inc/conn.php
./inc/conn.php
../../inc/conn.php
../inc/conn.php
../../../inc/conn.php
/inc/conn.asp
./inc/conn.asp
../../inc/conn.asp
../inc/conn.asp
../../../inc/conn.asp
/inc/config.inc.php
./inc/config.inc.php
../../inc/config.inc.php
../inc/config.inc.php
../../../inc/config.inc.php
/index.php
./index.php
../../index.php
../index.php
../../../index.php
/index.asp
./index.asp
../../index.asp
../index.asp
../../../index.asp
```