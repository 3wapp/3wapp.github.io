# sqlmap

## 简介

### sqlmap支持五种不同的注入模式：

* 1、基于布尔的盲注，即可以根据返回页面判断条件真假的注入
* 2、基于时间的盲注，即不能根据页面返回内容判断任何信息，用条件语句查看时间延迟语句是否执行（即页面返回时间是否增加）来判断
* 3、基于报错注入，即页面会返回错误信息，或者把注入的语句的结果直接返回在页面中
* 4、联合查询注入，可以使用union的情况下的注入
* 5、堆查询注入，可以同时执行多条语句的执行时的注入

## 常见用法

```
# 爆后端数据库, eg. mysql
sqlmap.py -u url --dbms                                       
sqlmap.py -u url  --dbms "后端数据库名" --dbs
# 爆数据库表
sqlmap.py -u url  --dbms "后端数据库名" --tables  
# 显示当前连接数据库名               
sqlmap.py -u url  --dbms "后端数据库名" --current-db   
# 列出数据库表中的表名          
sqlmap.py -u url --dbms "后端数据库名" --tables  -D "数据库名"   
# 列出数据库名中的表名内容                     
sqlmap.py -u url --dbms "后端数据库名" --columns  -T "表名" -D "数据库名"   
# 获取字段里面的内容           
sqlmap.py -u url --dbms "后端数据库名" --dump  -C "字段,字段"  -T "表名" -D "数据库名"
# dmup
sqlmap.py -u url --dbms "后端数据库名"--dump
# 搜索特定字段
sqlmap.py -u url --dbms "后端数据库名" -D "数据库名" -search -C admin,password

# referer 注入
sqlmap -u url --referer=1 --level 3 -p referer

# 改header
sqlmap --header="X-Forwarded-For: 127.0.0.1

# 改 host
sqlmap --host="localhost"

# 随机 User-Agent
sqlmap --random-agent

# file-read读取web文件
sqlmap -u url –file-read “/etc/passwd” -v 2

# file-write写入文件到web
sqlmap -u url –file-write /localhost/mm.php –file-dest /var/www/html/xx.php -v 2  
```

### 指定注入技术: `--technique=TECH`

这个参数可以指定sqlmap使用的探测技术，默认情况下会测试所有的方式。支持的探测方式如下：

```
B: Boolean-based blind SQL injection（布尔型注入）
E: Error-based SQL injection（报错型注入）
U: UNION query SQL injection（可联合查询注入）
S: Stacked queries SQL injection（可多语句查询注入）
T: Time-based blind SQL injection（基于时间延迟注入）
```

### `-v VERBOSE`

详细级别：0-6（默认为1）:

```
0：只显示Python的回溯，错误和关键消息。
1：显示信息和警告消息。
2：显示调试消息。
3：有效载荷注入。
4：显示HTTP请求。
5：显示HTTP响应头。
6：显示HTTP响应页面的内容
```

## --level

不同的level等级，SQLMAP所采用的策略也不近相同，

* 当–level的参数设定为2或者2以上的时候，sqlmap会尝试注入Cookie参数
* 当–level参数设定为3或者3以上的时候，会尝试对User-Angent，referer进行注入

## --no-cast

Added switch --no-cast to avoid use cast-alike statements during data fetching. This can also be used to decrease the payloads length

## 经验

### 发现跑出的数据都是毫无意义的字符

* SQLMAP会提示你加`–-hex`或者`-–no-cast`,有时会有帮助
* 用的是time-based注射，建议增加延时–time-sec等参数
* 增加level的数值

### unable to connect to the target url

* 可能是time-out设置的太小，出现问题
* 可能是WAF直接把请求拦截掉了，因此得不到响应

有些waf比较友善，过滤后会提示“参数不合法”，但是也有些waf则直接把请求拦下来无提示导致应答超时，这样在测试时会消耗大量的时间等待响应, 解决方案：减少time-out进行检测, 在跑数据时改回time-out

### possible integer casting detected

* 如果是在手工测试，建议到这里可以停止了，节省时间。
* 如果是在扫描器扫描的盲注，那么到这里坚决无视警告继续下去

## 参数解析

* option

```
-r <filename>
> sqlmap -r login.txt
```


txt文件

    + burpsuite 保存的文件

    + 自己构造

    ```
    POST /vuln.php HTTP/1.1
    Host: www.target.com
    User-Agent: Mozilla/4.0

    id=1
    ```

### Options（选项）：

| arg | note |
| --- | ---- |
|--version |显示程序的版本号并退出 |
|-h,  --help| 显示此帮助消息并退出 |
| -hh | 显示更详细的帮助信息并退出 |
|-v VERBOSE | 详细级别：0-6（默认为1）|


### Target（目标）：

> 以下至少需要设置其中一个选项，设置目标URL

| arg | note |
| --- | ---- |
| -d DIRECT | 直接连接到数据库|
| -u URL, --url=URL | 目标URL|
| -l LIST | 从Burp或WebScarab代理的日志中解析目标|
| -r REQUESTFILE | 从一个文件中载入HTTP请求|
| -g GOOGLEDORK | 处理Google dork的结果作为目标URL|
| -c CONFIGFILE | 从INI配置文件中加载选项|

### Request（请求）：

> 这些选项可以用来指定如何连接到目标URL

| arg | note |
| --- | ---- |
| --data=DATA  | 通过POST发送的数据字符串 |
| --cookie=COOKIE  | HTTP Cookie头 (--level >= 2 才尝试对cookie注入)|
| --cookie-urlencode URL  | 编码生成的cookie注入 |
| --drop-set-cookie  | 忽略响应的Set Cookie头信息 |
| --user-agent=AGENT  | 指定 HTTP User Agent头 (--level >= 3 才尝试对agent注入) |
| --random-agent  | 使用随机选定的HTTP User Agent头 |
| --referer=REFERER  | 指定 HTTP Referer头,(--level >= 3 才尝试对referer注入)|
| --headers=HEADERS  | 换行分开，加入其他的HTTP头 |
| --auth-type=ATYPE  | HTTP身份验证类型（基本，摘要或NTLM）(Basic, Digest or NTLM) |
| --auth-cred=ACRED  | HTTP身份验证凭据（用户名:密码） |
| --auth-cert=ACERT  | HTTP认证证书（key_file，cert_file） |
| --proxy=PROXY  | 使用HTTP代理连接到目标URL |
| --proxy-cred=PCRED  | HTTP代理身份验证凭据（用户名：密码） |
| --ignore-proxy  | 忽略系统默认的HTTP代理 |
| --delay=DELAY  | 在每个HTTP请求之间的延迟时间，单位为秒 |
| --timeout=TIMEOUT  | 等待连接超时的时间（默认为30秒） |
| --retries=RETRIES  | 连接超时后重新连接的时间（默认3） |
| --scope=SCOPE  | 从所提供的代理日志中过滤器目标的正则表达式 |
| --safe-url=SAFURL  | 在测试过程中经常访问的url地址 |
| --safe-freq=SAFREQ  | 两次访问之间测试请求，给出安全的URL |

## Enumeration（枚举）：

> 这些选项可以用来列举后端数据库管理系统的信息、表中的结构和数据|此外，您还可以运行您自己的SQL语句

| arg | note |
| --- | ---- |
| -b, --banner  | 检索数据库管理系统的标识 |
| --current-user  | 检索数据库管理系统当前用户 |
| --current-db  | 检索数据库管理系统当前数据库 |
| --is-dba  | 检测DBMS当前用户是否DBA |
| --users  | 枚举数据库管理系统用户 |
| --passwords  | 枚举数据库管理系统用户密码哈希 |
| --privileges  | 枚举数据库管理系统用户的权限 |
| --roles  | 枚举数据库管理系统用户的角色 |
| --dbs  | 枚举数据库管理系统数据库 |
| -D DBname |  要进行枚举的指定数据库名 |
| -T TBLname  | 要进行枚举的指定数据库表（如：-T tablename | --columns） |
| --tables  | 枚举的DBMS数据库中的表 |
| --columns  | 枚举DBMS数据库表列 |
| --dump  | 转储数据库管理系统的数据库中的表项 |
| --dump-all  | 转储所有的DBMS数据库表中的条目 |
| --search  | 搜索列（S），表（S）和/或数据库名称（S） |
| -C COL  | 要进行枚举的数据库列 |
| -U USER  | 用来进行枚举的数据库用户 |
| --exclude-sysdbs  | 枚举表时排除系统数据库 |
| --start=LIMITSTART  | 第一个查询输出进入检索 |
| --stop=LIMITSTOP  | 最后查询的输出进入检索 |
| --first=FIRSTCHAR  | 第一个查询输出字的字符检索 |
| --last=LASTCHAR  | 最后查询的输出字字符检索 |
| --sql-query=QUERY | 要执行的SQL语句 |
| --sql-shell  | 提示交互式SQL的shell |

### Optimization（优化）：

> 这些选项可用于优化SqlMap的性能

| arg | note |
| --- | ---- |
| -o  | 开启所有优化开关 |
| --predict-output  | 预测常见的查询输出 |
| --keep-alive  | 使用持久的HTTP（S）连接 |
| --null-connection  | 从没有实际的HTTP响应体中检索页面长度 |
| --threads=THREADS  | 最大的HTTP（S）请求并发量（默认为1） |

### Injection（注入）：

> 这些选项可以用来指定测试哪些参数， 提供自定义的注入payloads和可选篡改脚本

| arg | note |
| --- | ---- |
| -p TESTPARAMETER |  可测试的参数 |
| --dbms=DBMS  | 强制后端的DBMS为此值 |
| --os=OS  | 强制后端的DBMS操作系统为这个值 |
| --prefix=PREFIX |  注入payload字符串前缀 |
| --suffix=SUFFIX  | 注入payload字符串后缀 |
| --tamper=TAMPER  | 使用给定的脚本篡改注入数据 |
| --no-cast | Turn off payload casting mechanism |
| --no-escape | Turn off string escaping mechanism |
| --dbms-cred=DBMS..  | DBMS authentication credentials (user:password)
| --invalid-bignum | Use big numbers for invalidating values |
| --invalid-logical | Use logical operations for invalidating values |
| --invalid-string | Use random strings for invalidating values |
| --skip=SKIP | Skip testing for given parameter(s) |
| --skip-static | Skip testing parameters that not appear to be dynamic |


### Detection（检测）：

> 这些选项可以用来指定在SQL盲注时如何解析和比较HTTP响应页面的内容

| arg | note |
| --- | ---- |
| --level=LEVEL  | 执行测试的等级（1-5，默认为1） |
| --risk=RISK  | 执行测试的风险（0-3，默认为1） |
| --string=STRING  | 查询时有效时在页面匹配字符串 |
| --regexp=REGEXP  | 查询时有效时在页面匹配正则表达式 |
| --text-only |  仅基于在文本内容比较网页 |

### Techniques（技巧）：

> 这些选项可用于调整具体的SQL注入测试

| arg | note |
| --- | ---- |
| --technique=TECH  | SQL注入技术测试（默认BEUST） |
| --time-sec=TIMESEC  | DBMS响应的延迟时间（默认为5秒） |
| --union-cols=UCOLS  | 定列范围用于测试UNION查询注入 |
| --union-char=UCHAR  | 用于暴力猜解列数的字符 |

### Fingerprint（指纹）：

| arg | note |
| --- | ---- |
| -f,--fingerprint  | 执行检查广泛的DBMS版本指纹 |

### Brute force（蛮力）：

> 这些选项可以被用来运行蛮力检查

| arg | note |
| --- | ---- |
| --common-tables |  检查存在共同表 |
| --common-columns  | 检查存在共同列 |

### User-defined function injection（用户自定义函数注入）：
> 这些选项可以用来创建用户自定义函数

| arg | note |
| --- | ---- |
| --udf-inject  | 注入用户自定义函数 |
| --shared-lib=SHLIB  | 共享库的本地路径

### File system access（访问文件系统）：

> 这些选项可以被用来访问后端数据库管理系统的底层文件系统

| arg | note |
| --- | ---- |
| --file-read=RFILE  | 从后端的数据库管理系统文件系统读取文件 |
| --file-write=WFILE |  编辑后端的数据库管理系统文件系统上的本地文件 |
| --file-dest=DFILE  | 后端的数据库管理系统写入文件的绝对路径 |

### Operating system access（操作系统访问）：

> 这些选项可以用于访问后端数据库管理系统的底层操作系统

| arg | note |
| --- | ---- |
| --os-cmd=OSCMD  | 执行操作系统命令 |
| --os-shell  | 交互式的操作系统的shell |
| --os-pwn  | 获取一个OOB shell，meterpreter或VNC |
| --os-smbrelay  | 一键获取一个OOB shell，meterpreter或VNC |
| --os-bof  | 存储过程缓冲区溢出利用 |
| --priv-esc  | 数据库进程用户权限提升 |
| --msf-path=MSFPATH  | Metasploit Framework本地的安装路径 |
| --tmp-path=TMPPATH |  远程临时文件目录的绝对路径 |

###Windows注册表访问：

> 这些选项可以被用来访问后端数据库管理系统Windows注册表

| arg | note |
| --- | ---- |
| --reg-read  | 读一个Windows注册表项值 |
| --reg-add  | 写一个Windows注册表项值数据 |
| --reg-del  | 删除Windows注册表键值 |
| --reg-key=REGKEY  | Windows注册表键 |
| --reg-value=REGVAL  | Windows注册表项值 |
| --reg-data=REGDATA  | Windows注册表键值数据 |
| --reg-type=REGTYPE |  Windows注册表项值类型 |

> 这些选项可以用来设置一些一般的工作参数

| arg | note |
| --- | ---- |
| -t TRAFFICFILE  | 记录所有HTTP流量到一个文本文件中 |
| -s SESSIONFILE  | 保存和恢复检索会话文件的所有数据 |
| --flush-session  | 刷新当前目标的会话文件 |
| --fresh-queries  | 忽略在会话文件中存储的查询结果 |
| --eta  | 显示每个输出的预计到达时间 |
| --update |  更新SqlMap |
| --save  | file保存选项到INI配置文件 |
| --batch  | 从不询问用户输入，使用所有默认配置|

### Miscellaneous（杂项）：

| arg | note |
| --- | ---- |
| --beep  | 发现SQL注入时提醒 |
| --check-payload |  IDS对注入payloads的检测测试 |
| --cleanup S | qlMap具体的UDF和表清理DBMS |
| --forms  | 对目标URL的解析和测试形式 |
| --gpage=GOOGLEPAGE  | 从指定的页码使用谷歌dork结果 |
| --page-rank |  Google dork结果显示网页排名（PR） |
| --parse-errors  | 从响应页面解析数据库管理系统的错误消息 |
| --replicate  | 复制转储的数据到一个sqlite3数据库 |
| --tor |  使用默认的Tor（Vidalia/ Privoxy/ Polipo）代理地址 |
| --wizard  | 给初级用户的简单向导界面 |

## note

* 大量出现 unable to connect ，表明流量被WAF拦截

1 使用tamper

2

| --user-agent "Googlebot (http://www.google.com/)   
| --user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20100101 Firefox/16.0"

3 设置延迟时间或线程数

| --threads 线程数   
| --delay 延迟

### 绕过 waf 的tamper

| No | tamper | note |
| --- | ---- | ------ |
|01 | apostrophemask.py  | 用UTF-8全角字符替换单引号字符 |
|02 | apostrophenullencode.py    |    用非法双字节unicode字符替换单引号字符|
|03 | appendnullbyte.py      |  在payload末尾添加空字符编码|
|04 | base64encode.py    |    对给定的payload全部字符使用Base64编码|
|05 | between.py     |   分别用“NOT BETWEEN 0 AND #”替换大于号“>”，“BETWEEN # AND #”替换等于号“=”|
|06 | bluecoat.py    |    在SQL语句之后用有效的随机空白符替换空格符，随后用“LIKE”替换等于号“=”|
|07 | chardoubleencode.py   |     对给定的payload全部字符使用双重URL编码（不处理已经编码的字符）|
|08 | charencode.py     |   对给定的payload全部字符使用URL编码（不处理已经编码的字符）|
|09 | charunicodeencode.py    |    对给定的payload的非编码字符使用Unicode URL编码（不处理已经编码的字符）|
|10 | concat2concatws.py   |     用“CONCAT_WS(MID(CHAR(0), 0, 0), A, B)”替换像“CONCAT(A, B)”的实例|
|11 | equaltolike.py    |    用“LIKE”运算符替换全部等于号“=”|
|12 | greatest.py     |   用“GREATEST”函数替换大于号“>”|
|13 | halfversionedmorekeywords.py    |    在每个关键字之前添加MySQL注释|
|14 | ifnull2ifisnull.py     |   用“IF(ISNULL(A), B, A)”替换像“IFNULL(A, B)”的实例|
|15 | lowercase.py     |   用小写值替换每个关键字字符|
|16 | modsecurityversioned.py    |    用注释包围完整的查询|
|17 | modsecurityzeroversioned.py     |   用当中带有数字零的注释包围完整的查询|
|18 | multiplespaces.py    |    在SQL关键字周围添加多个空格|
|19 | nonrecursivereplacement.py    |   用representations替换预定义SQL关键字，适用于过滤器|
|20 | overlongutf8.py    |    转换给定的payload当中的所有字符|
|21 | percentage.py    |    在每个字符之前添加一个百分号|
|22 | randomcase.py     |   随机转换每个关键字字符的大小写|
|23 | randomcomments.py  |      向SQL关键字中插入随机注释|
|24 | securesphere.py   |    添加经过特殊构造的字符串|
|25 | sp_password.py     |   向payload末尾添加“sp_password” for automatic obfuscation from DBMS logs|
|26 | space2comment.py   |     用“/**/”替换空格符|
|27 | space2dash.py    |    用破折号注释符“--”其次是一个随机字符串和一个换行符替换空格符|
|28 | space2hash.py    |    用磅注释符“#”其次是一个随机字符串和一个换行符替换空格符|
|29 | space2morehash.py   |     用磅注释符“#”其次是一个随机字符串和一个换行符替换空格符|
|30 | space2mssqlblank.py  |      用一组有效的备选字符集当中的随机空白符替换空格符|
|31 | space2mssqlhash.py    |    用磅注释符“#”其次是一个换行符替换空格符|
|32 | space2mysqlblank.py   |     用一组有效的备选字符集当中的随机空白符替换空格符|
|33 | space2mysqldash.py   |     用破折号注释符“--”其次是一个换行符替换空格符|
|34 | space2plus.py    |    用加号“+”替换空格符|
|35 | space2randomblank.py    |    用一组有效的备选字符集当中的随机空白符替换空格符|
|36 | unionalltounion.py   |     用“UNION SELECT”替换“UNION ALL SELECT”|
|37 | unmagicquotes.py    |    用一个多字节组合%bf%27和末尾通用注释一起替换空格符|
|38 | varnish.py     |   添加一个HTTP头“X-originating-IP”来绕过WAF|
|39 | versionedkeywords.py    |    用MySQL注释包围每个非函数关键字|
|40 | versionedmorekeywords.py     |   用MySQL注释包围每个关键字|
|41 | xforwardedfor.py   |     添加一个伪造的HTTP头“X-Forwarded-For”来绕过WAF|
