---
title: "Cmdline"
date: 2016-03-11 14:57
---

## zip

```
zip  [-aABcdDeEfFghjklLmoqrRSTuvVwXyz!@$] [--longoption ...]  [-b path]
       [-n suffixes] [-t date] [-tt date] [zipfile [file ...]]  [-xi list]

-0  store only
-1 compress faster
```

```
zip test.zip test
```

## wget

常用命令:

需要下载某个目录下面的所有文件。

```
wget -c -r -np -k -L -p www.xxx.org/pub/path/
```

在下载时。有用到外部域名的图片或连接。如果需要同时下载就要用-H参数。

```
wget -np -nH -r --span-hosts www.xxx.org/pub/path/
```

参数：

```
-b, –background     启动后转入后台执行
-c      断点续传
-t, –tries=NUMBER   设定最大尝试链接次数(0 表示无限制)
-w, –wait=SECONDS   两次尝试之间间隔SECONDS秒
–waitretry=SECONDS  在重新链接之间等待1…SECONDS秒
–random-wait        在下载之间等待0…2*WAIT秒
-r      递归下载，下载指定网页某一目录下（包括子目录）的所有文件
-nd     递归下载时不创建一层一层的目录，把所有的文件下载到当前目录
-np     递归下载时不搜索上层目录，如wget -c -r www.xxx.org/pub/path/
        没有加参数-np，就会同时下载path的上一级目录pub下的其它文件
-k      将绝对链接转为相对链接，下载整个站点后脱机浏览网页，最好加上这个参数
-L      递归时不进入其它主机，如wget -c -r www.xxx.org/ 
-l, –level=NUMBER   最大递归深度 (inf 或 0 代表无穷)
-p      下载网页所需的所有文件，如图片等

-A, –accept=LIST    分号分隔的被接受扩展名的列表
-R, –reject=LIST    分号分隔的不被接受的扩展名的列表
-D, –domains=LIST   分号分隔的被接受域的列表
-i      后面跟一个文件，文件内指明要下载的URL

-d, –debug          打印调试输出
-q, –quiet          安静模式(没有输出)

--header            设置请求头

-O      将文件下载到指定的目录中
-P      保存文件之前先创建指定名称的目录
```

## curl 

参数

```
-X/--request [GET|POST|PUT|DELETE|…]  使用指定的http method发出 http request
-H/--header                           设定header
-i/--include                          显示response的header
-d/--data                             设定 http parameters 
-v/--verbose                          显示详细信息
-u/--user                             使用者帐号，密码
-b/--cookie                           cookie
```

* sample

```
# set header
curl -v -i -H "Content-Type: application/json" http://www.example.com/users

# post params
curl -X POST -d "param1=value1&param2=value2"
curl -X POST -d "param1=value1" -d "param2=value2"

# 存cookie
curl -i -X POST -d username=kent -d password=kent123 -c  ~/cookie.txt  http://www.rest.com/auth

# 载入cookie
curl -i --header "Accept:application/json" -X GET -b ~/cookie.txt http://www.rest.com/users/1

# HTTP Basic Authentication
curl -i --user kent:secret http://www.rest.com/api/foo'
```

## netstat

* 参数

```
-p      显示进程号或程序
```

* sample

`netstat -anp | grep 8080` 查看8080端口占用, 需要root权限, 显示信息更多