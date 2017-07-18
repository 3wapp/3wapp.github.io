---
title: "note"
date: 2016-05-19 10:52
---

###CGI

CGI全称是“公共网关接口”(Common Gateway Interface)，HTTP服务器与你的或其它机器上的程序进行“交谈”的一种工具，其程序须运行在网络服务器上。

CGI可以用任何一种语言编写，只要这种语言具有标准输入、输出和环境变量。如php,perl,tcl等

### FastCGI

FastCGI像是一个常驻(long-live)型的CGI，它可以一直执行着，只要激活后，不会每次都要花费时间去fork一次(这是CGI最为人诟病的fork-and-execute 模式)。它还支持分布式的运算, 即 FastCGI 程序可以在网站服务器以外的主机上执行并且接受来自其它网站服务器来的请求。

FastCGI是语言无关的、可伸缩架构的CGI开放扩展，其主要行为是将CGI解释器进程保持在内存中并因此获得较高的性能。众所周知，CGI解释器的反复加载是CGI性能低下的主要原因，如果CGI解释器保持在内存中并接受FastCGI进程管理器调度，则可以提供良好的性能、伸缩性、Fail- Over特性等等。

** FastCGI与CGI特点 **

1. 如CGI，FastCGI也具有语言无关性.
2. 如CGI, FastCGI在进程中的应用程序，独立于核心web服务器运行,提供了一个比API更安全的环境。(APIs把应用程序的代码与核心的web服务器链接在一起，这意味着在一个错误的API的应用程序可能会损坏其他应用程序或核心服务器; 恶意的API的应用程序代码甚至可以窃取另一个应用程序或核心服务器的密钥。)
3. FastCGI技术目前支持语言有：C/C++、Java、Perl、Tcl、Python、SmallTalk、Ruby等。相关模块在Apache, ISS, Lighttpd等流行的服务器上也是可用的。
4. 如CGI，FastCGI的不依赖于任何Web服务器的内部架构，因此即使服务器技术的变化, FastCGI依然稳定不变。
　　
** FastCGI的工作原理 **
　　
1. Web Server启动时载入FastCGI进程管理器（IIS ISAPI或Apache Module)
2. FastCGI进程管理器自身初始化，启动多个CGI解释器进程(可见多个php-cgi)并等待来自Web Server的连接。
3. 当客户端请求到达Web Server时，FastCGI进程管理器选择并连接到一个CGI解释器。Web server将CGI环境变量和标准输入发送到FastCGI子进程php-cgi。
4. FastCGI子进程完成处理后将标准输出和错误信息从同一连接返回Web Server。当FastCGI子进程关闭连接时，请求便告处理完成。FastCGI子进程接着等待并处理来自FastCGI进程管理器(运行在Web Server中)的下一个连接。 在CGI模式中，php-cgi在此便退出了。
　　
在上述情况中，你可以想象CGI通常有多慢。每一个Web请求PHP都必须重新解析php.ini、重新载入全部扩展并重初始化全部数据结构。使用FastCGI，所有这些都只在进程启动时发生一次。一个额外的好处是，持续数据库连接(Persistent database connection)可以工作。

** FastCGI的不足 **

因为是多进程，所以比CGI多线程消耗更多的服务器内存，PHP-CGI解释器每进程消耗7至25兆内存，将这个数字乘以50或100就是很大的内存数。
　　
Nginx 0.8.46+PHP 5.2.14(FastCGI)服务器在3万并发连接下，开启的10个Nginx进程消耗150M内存（15M*10=150M），开启的64个php-cgi进程消耗1280M内存（20M*64=1280M），加上系统自身消耗的内存，总共消耗不到2GB内存。如果服务器内存较小，完全可以只开启25个php-cgi进程，这样php-cgi消耗的总内存数才500M。数据摘自Nginx 0.8.x + PHP 5.2.13(FastCGI)搭建胜过Apache十倍的Web服务器(第6版)

### PHP-CGI

PHP-CGI是PHP自带的FastCGI管理器。启动PHP-CGI，使用如下命令：```php-cgi -b 127.0.0.1:9000```

** PHP-CGI的不足 **

1. php-cgi变更php.ini配置后需重启php-cgi才能让新的php-ini生效，不可以平滑重启
2. 直接杀死php-cgi进程,php就不能运行了。(PHP-FPM和Spawn-FCGI就没有这个问题,守护进程会平滑从新生成新的子进程。）

### PHP-FPM

PHP-FPM是一个PHP FastCGI管理器，是只用于PHP的,可以在 http://php-fpm.org/download下载得到. PHP-FPM提供了更好的PHP进程管理方式，可以有效控制内存和进程、可以平滑重载PHP配置，比spawn-fcgi具有更多有点，所以被PHP官方收录了。在./configure的时候带 –enable-fpm参数即可开启PHP-FPM。

使用PHP-FPM来控制PHP-CGI的FastCGI进程 `/usr/local/php/sbin/php-fpm{start|stop|quit|restart|reload|logrotate}`

```
--start 启动php的fastcgi进程
--stop 强制终止php的fastcgi进程
--quit 平滑终止php的fastcgi进程
--restart 重启php的fastcgi进程
--reload 重新平滑加载php的php.ini
--logrotate 重新启用log文件 
```

### Spawn-FCGI

Spawn-FCGI是一个通用的FastCGI管理服务器，它是lighttpd中的一部份，很多人都用Lighttpd的Spawn-FCGI进行FastCGI模式下的管理工作，不过有不少缺点。 Spawn-FCGI目前已经独成为一个项目，更加稳定一些，也给很多Web 站点的配置带来便利。已经有不少站点将它与nginx搭配来解决动态网页。

使用Spawn-FCGI来控制php-CGI的FastCGI进程了

```
/usr/local/bin/spawn-fcgi -a 127.0.0.1 -p 9000 -C 5 -u www-data -g www-data -f /usr/bin/php-CGI
参数含义如下:
-f 指定调用FastCGI的进程的执行程序位置，根据系统上所装的PHP的情况具体设置
-a 绑定到地址addr
-p 绑定到端口port
-s 绑定到unix socket的路径path
-C 指定产生的FastCGI的进程数，默认为5(仅用于PHP)
-P 指定产生的进程的PID文件路径
-u和-g FastCGI使用什么身份(-u 用户 -g 用户组)运行，Ubuntu下可以使用www-data，其他的根据情况配置，如nobody、apache等
```

### PHP-FPM与spawn-CGI对比测试

PHP-FPM的使用非常方便,配置都是在PHP-FPM.ini的文件内，而启动、重启都可以从php/sbin/PHP-FPM中进行。更方便的是修改php.ini后可以直接使用PHP-FPM reload进行加载，无需杀掉进程就可以完成php.ini的修改加载
结果显示使用PHP-FPM可以使php有不小的性能提升。PHP-FPM控制的进程cpu回收的速度比较慢,内存分配的很均匀。

Spawn-FCGI控制的进程CPU下降的很快,而内存分配的比较不均匀。有很多进程似乎未分配到,而另外一些却占用很高。可能是由于进程任务分配的不均匀导致的.而这也导致了总体响应速度的下降。而PHP-FPM合理的分配，导致总体响应的提到以及任务的平均。

PHP-FPM与Spawn-FCGI功能比较 http://php-fpm.org/about/

PHP-FPM、Spawn-FCGI都是守护php-cgi的进程管理器。